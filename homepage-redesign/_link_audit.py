"""
One-shot link auditor for the Perfect 2 Trade redesign mockup.

Rewrites placeholder href="#" links based on element context:
  - category cards / brand logos / top-level nav  -> category-garden-seasonal.html
  - sub-category tiles & mega-menu sub links     -> category-garden-chemicals.html
  - product / offer / related-product cards      -> product-algon-cleaner.html
  - "View bag" / "View basket"                   -> cart.html
  - "Checkout"                                   -> checkout.html
  - "Continue shopping" / "Return to shop"       -> index.html
  - "Lost your password?"                        -> account-lost-password.html
Footer info-page links (Contact us, T&Cs, Privacy, etc.) are left as "#".

BS4 is used only for context-aware *decisions*; replacements are applied by
exact source-position so file whitespace / formatting is preserved.
"""

import re
from bs4 import BeautifulSoup
from pathlib import Path

ROOT = Path(__file__).parent

CAT_PARENT = "category-garden-seasonal.html"
CAT_SUB    = "category-garden-chemicals.html"
PRODUCT    = "product-algon-cleaner.html"
CART       = "cart.html"
CHECKOUT   = "checkout.html"
LOGIN      = "account-login.html"
LOST_PW    = "account-lost-password.html"
HOME       = "index.html"

TOP_LEVEL = {
    "garden & seasonal", "homeware", "paints & decorative",
    "electricals", "health & beauty", "pet care",
}

FOOTER_LABELS = {
    "contact us", "terms & conditions", "delivery information",
    "returns policy", "privacy policy", "about perfect 2 trade",
    "trade accounts", "blog & advice", "privacy policy.",
}

# Phrase -> destination; checked against link text (lowered, whitespace-normalised)
PHRASES = [
    ("lost your password",        LOST_PW),
    ("back to sign in",           LOGIN),
    ("your account",              LOGIN),
    ("view bag",                  CART),
    ("view basket",               CART),
    ("checkout",                  CHECKOUT),
    ("continue shopping",         HOME),
    ("return to shop",            HOME),
    ("browse all brands",         CAT_PARENT),
    ("shop the range",            CAT_PARENT),
    ("see all garden",            CAT_SUB),
    ("shop all garden",           CAT_PARENT),
    ("shop all homeware",         CAT_PARENT),
    ("shop all paints",           CAT_PARENT),
    ("shop all electricals",      CAT_PARENT),
    ("shop all health",           CAT_PARENT),
    ("shop all pet",              CAT_PARENT),
]

def has_ancestor_class(el, cls):
    for p in el.parents:
        if hasattr(p, "get") and cls in (p.get("class") or []):
            return True
    return False

def has_any_ancestor_class(el, classes):
    for p in el.parents:
        if hasattr(p, "get"):
            pc = p.get("class") or []
            if any(c in pc for c in classes):
                return True
    return False

def text_of(a):
    return re.sub(r"\s+", " ", a.get_text(" ").replace("\xa0", " ")).strip().lower()

def decide(a):
    cls = a.get("class") or []
    txt = text_of(a)

    # 0. Explicit skips
    if a.has_attr("data-cart-toggle"):
        return None  # JS-controlled toggle — must stay href="#"
    if "filter-top__link" in cls and a.get("aria-current") == "page":
        return None  # current-page filter link
    if "pagination__link" in cls:
        return None  # leave pagination unwired in mockup
    if txt in FOOTER_LABELS:
        return None  # footer info pages have no destination
    if txt == "calculate shipping":
        return None  # no shipping calculator page
    if txt == "terms and conditions" and a.parent and a.parent.name == "span":
        return None  # inline legal-copy reference, no page

    # 1. Class-based context
    if "logo"                 in cls: return HOME
    if "footer-logo"          in cls: return HOME
    if "category-card"        in cls: return CAT_PARENT
    if "subcat-tile"          in cls: return CAT_SUB
    if "product-card"         in cls: return PRODUCT
    if "related-card"         in cls: return PRODUCT
    if any(c.startswith("offer-card") for c in cls): return PRODUCT
    if "mega__promo"          in cls: return CAT_PARENT
    if "mega__shop-all"       in cls: return CAT_PARENT
    if "search-chip"          in cls: return CAT_SUB
    if "filter-list__viewall" in cls: return CAT_SUB
    if any(c.startswith("cart-line") for c in cls): return PRODUCT

    # 2. Ancestor-based context
    if has_any_ancestor_class(a, ["brand-row", "brand-block__logos"]):
        return CAT_PARENT
    if has_ancestor_class(a, "mega__col"):
        return CAT_SUB
    # Search overlay: product cards -> product page; category list -> parent cat
    if has_ancestor_class(a, "search-products"):
        return PRODUCT
    if has_ancestor_class(a, "search-links") and txt in TOP_LEVEL:
        return CAT_PARENT

    # 3. Top-level nav: <li class="has-mega"><a href="#">PARENT</a>
    #    OR any <li><a href="#">PARENT</a> inside .primary-nav__inner
    parent = a.parent
    if parent and getattr(parent, "name", None) == "li":
        if "has-mega" in (parent.get("class") or []) and txt in TOP_LEVEL:
            return CAT_PARENT
    if has_ancestor_class(a, "primary-nav__inner") and txt in TOP_LEVEL:
        return CAT_PARENT

    # 4. Phrase-based CTA buttons / link-arrows
    for needle, dest in PHRASES:
        if needle in txt:
            return dest

    return None


def process(path: Path):
    src = path.read_text(encoding="utf-8")
    soup = BeautifulSoup(src, "html.parser")

    # Collect decisions in document order
    decisions = [decide(a) for a in soup.find_all("a", href="#")]

    # Match each href="#" in source by position (same order as soup walk)
    positions = [m.start() for m in re.finditer(r'href="#"', src)]
    if len(positions) != len(decisions):
        print(f"  !! position/decision mismatch in {path.name}: {len(positions)} vs {len(decisions)}")
        return 0, src.count('href="#"'), []

    # Apply replacements right-to-left so earlier positions remain valid
    new_src = src
    changes = 0
    skipped = []
    HREF = 'href="#"'
    for i, dest in reversed(list(enumerate(decisions))):
        pos = positions[i]
        if dest:
            new_src = new_src[:pos] + f'href="{dest}"' + new_src[pos + len(HREF):]
            changes += 1
        else:
            # Capture the surrounding line for diagnostic
            line_start = new_src.rfind("\n", 0, pos) + 1
            line_end = new_src.find("\n", pos)
            line = new_src[line_start:line_end if line_end != -1 else None].strip()[:120]
            skipped.append(line)

    if changes:
        path.write_text(new_src, encoding="utf-8")

    remaining = new_src.count('href="#"')
    return changes, remaining, list(reversed(skipped))


if __name__ == "__main__":
    files = sorted(p for p in ROOT.glob("*.html"))
    total_changed = total_remaining = 0
    for f in files:
        changed, remaining, skipped = process(f)
        total_changed += changed
        total_remaining += remaining
        print(f"{f.name:40s}  changed: {changed:3d}   remaining #: {remaining:3d}")
        if 0 < remaining <= 20:
            for line in dict.fromkeys(skipped):
                print(f"    skipped: {line}")
    print(f"\nTOTAL  changed: {total_changed}   remaining #: {total_remaining}")
