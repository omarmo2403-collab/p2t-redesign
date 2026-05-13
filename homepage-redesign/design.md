# Perfect 2 Trade — Design System

This document captures the design language, tokens, and patterns established during the homepage redesign. **Every new page or component should follow these principles** to keep the brand experience consistent.

The aesthetic direction is inspired by **Cox & Cox** — editorial, refined, warm-neutral palette, serif headings paired with a clean sans, generous whitespace, and high-quality photography. The execution stays grounded in the **Perfect 2 Trade** logo (navy + coral badge).

---

## 1. Design tone

- **Editorial, magazine-style** layouts — typography-led, not button-led
- **Warm and refined** — cream paper backgrounds, soft hairline dividers, never stark white
- **Trade-trustworthy** — typography signals quality; copy is direct, no marketing fluff
- **Photography-forward** — lifestyle shots and clean product PNGs do most of the visual work
- **Restrained interaction** — subtle hovers (4–6px lift, 1.03–1.06× zoom, hairline underline reveal). Avoid bouncy or animated UI.

---

## 2. Colour palette

All colours live as CSS custom properties in `:root`. Do not hardcode hex values in components.

```css
:root {
  --ink:        #1f2622;   /* near-black, green-grey lean — body text, dark surfaces */
  --ink-soft:   #4a5048;   /* secondary text */
  --muted:      #8a8f87;   /* tertiary text, eyebrow labels */
  --line:       #e3ddd2;   /* warm hairline divider */
  --paper:      #faf7f1;   /* off-white page background */
  --paper-2:    #f3ede2;   /* warmer sand for alternating section backgrounds */
  --accent:     #2f4a3a;   /* deep forest green — H1/H2 italic emphasis, hover states, trust band, badges */
  --gold:       #a98a55;   /* used sparingly — only the "Offers" nav link */
}
```

**Section rhythm:** alternate `--paper` and `--paper-2` between sections to create a soft tonal beat. Punctuate with one strong **dark accent block** (the trust band uses `--accent` green) and the **deep dark footer** (`#1a1f1c`) so the page reads as paper → sand → paper → sand → dark band → dark footer.

**The logo brand colours** (navy `#205080` and coral `#d05030`) live inside the PNG and aren't tokens — we use the warm-neutral system across the UI and let the logo provide brand colour where it appears.

---

## 3. Typography — Cox & Cox dual-font system

**Audited from coxandcox.co.uk live elements.** Cox uses two typefaces and assigns them by *role*, not by tag:

- **Serif** (Cox uses Baskerville URW, we use **Cormorant Garamond**) — display only: H1 and the big editorial H2. Weight 400. Subtle 0.005–0.022em tracking. NO italic. NO accent colour on emphasis. NEVER on tile labels, prices, body, or anything inside a grid/list.
- **Sans** (Cox uses Gill Sans Nova, we use **Jost**) — everything else: H3+, body, navigation, buttons, product names, prices, footer, eyebrows. Weights 400 / 500 / 600. Mostly normal letter-spacing.

| Token | Family | Use |
|---|---|---|
| `--serif` | Cormorant Garamond (400, 500, 600) | H1 / H2 display only |
| `--sans`  | Jost (400, 500, 600) | Body, H3+, nav, buttons, product cards, eyebrows, footer |

### Type scale (matching Cox & Cox specs)

| Element | Family | Size | Weight | Tracking | Transform |
|---|---|---|---|---|---|
| Body | Sans | **16px** / line-height 1.43 | 400 | normal | none |
| `h1` (display) | Serif | `clamp(34px, 4.6vw, 56px)` / lh 1.1 | 400 | 0.005em | none |
| `h2` (display) | Serif | `clamp(28px, 3.4vw, 44px)` / lh 1.15 | 400 | 0.022em | none |
| `h3` | Sans | 18px / lh 1.35 | 500 | 0.03em | none |
| `h4` | Sans | 14px | 500 | 0.10em | UPPERCASE |
| `h5` | Sans | 16px | 500 | 0.02em | none |
| Product name | Sans | 16px / lh 1.4 | 500 | 0.05em | none |
| Product price (now) | Sans | 17–22px | **600** | normal | none |
| Product price (was) | Sans | 14px strikethrough | 400 | normal | none |
| Button | Sans | 13px | **600** | 0.08em | UPPERCASE |
| Nav link | Sans | 13px | 500 | 0.10em | UPPERCASE |
| Eyebrow / label | Sans | 12px | 500 | 0.14em | UPPERCASE |
| `.link-arrow` | Sans | 13px | 600 | 0.08em | UPPERCASE |

### Body colour

Cox & Cox uses **#444** (`rgb(68,68,68)`) — a medium charcoal — for almost all text. Contrast comes from font *weight*, not colour darkness. We follow the same: body, headings, nav, footer all sit at `#444`. The `--ink` token (`#1f2622`) is reserved for the darkest UI surfaces (utility bar, hamburger bars, dark button backgrounds).

### Prices

All prices — featured offers, product cards, anywhere — use the **sans** family with weight 600 for the active price and weight 400 strikethrough for the original. This matches Cox & Cox's spec (Gill Sans Nova, ~16px weight 600, normal letter-spacing) and gives consistent scannable pricing across the site:

- **Now-price**: Sans Jost weight 600, size 17–22px (clamped — featured offers slightly larger than listing tiles), colour `#444`, normal tracking.
- **Was-price**: Sans Jost weight 400, 13–14px strikethrough, colour `#888`, normal tracking.
- **VAT label** (e.g. `(inc VAT)`): 12px sans, weight 400, colour `#888`.

The serif (Cormorant Garamond) is **never used for prices, tile labels, or anything inside a grid/list** — it stays reserved for `h1` and the big editorial `h2` page-level display headings only.

### Tile labels — always sans

Both **homepage category tiles** (`.category-card__label`) and **sub-category tiles** (`.subcat-tile h3`) use **Sans Jost** — Cox & Cox uses Gill Sans for tile grids and reserves Baskerville for the page-hero H2 only.

- Category tile label: Sans, `clamp(16px, 1.6vw, 19px)`, weight 500, ls 0.04em
- Sub-category tile heading: Sans, `clamp(17px, 1.6vw, 20px)`, weight 500, ls 0.02em
- Both: colour `#444`, sentence/title case (no uppercase), line-height 1.3

### Rules

- **Letter-spacing is mostly normal.** Only tracked elements: H4 (0.1em), eyebrows (0.14em), buttons & nav (0.08–0.1em), product price 'was' (none — strikethrough does the visual work).
- **No italic.** Cox doesn't use italic for emphasis — neither do we. `<em>` inside H1/H2 inherits everything (`font-style: normal; color: inherit`).
- **Capitalisation**: UPPERCASE only for H4 labels, nav links, buttons, eyebrows, and `.link-arrow`. Everything else is sentence/title case.
- **Line-height**: 1.43 for body, 1.1–1.35 for headings. Tight on display headings (1.1), generous on body and product names (1.4+).
- **Weights**: 400 (body, headings), 500 (sub-headings, product names, nav, eyebrows, buttons of lesser emphasis), 600 (buttons, prices, link-arrows — strong emphasis without going to a serif).
- **No underlines** on default links — use `.link-arrow` for textual CTAs (uppercase tracked sans with an accent bottom-border).

---

## 4. Layout tokens

```css
--container: 1200px;                       /* max-width of every section's container */
--gutter:    clamp(20px, 4vw, 32px);       /* horizontal page padding, fluid */
--section-y: clamp(56px, 7vw, 112px);      /* vertical section padding, fluid */
```

- Every section content sits inside `.container { max-width: var(--container); margin: 0 auto; padding: 0 var(--gutter); }`
- Section vertical padding: `padding: var(--section-y) 0;`
- Centre by `margin: 0 auto` on the container — sections themselves span full viewport

---

## 5. Responsive breakpoints

Four-step desktop-down cascade:

| Breakpoint | Used for |
|---|---|
| **default ≥1025px** | Full desktop — multi-column grids, hover mega menu |
| **`max-width: 1024px`** | Large tablet / small laptop. Mega menu disabled; hero stacks; brand grid drops to 4 cols; footer to 2 cols; trust band to 1 col. |
| **`max-width: 768px`** | Tablet. **Mobile drawer kicks in** (hamburger button + off-canvas nav). Offers single-column. |
| **`max-width: 640px`** | Phone. Tighter padding (`--gutter` becomes 16px). Categories in **2 columns**. Brands in 2 cols. Trust band vertical (icon above text). |
| **`max-width: 420px`** | Small phone. Categories stay 2 cols (tighter gap). Hamburger and icons scaled down. |

### Cox & Cox-style mobile header

At ≤768px the header restructures into a **single row**: `[hamburger left] [logo centred] [account + basket right]`, with the search bar as a full-width second row below. Logo is fluid `clamp(60px, 19vw, 78px)` so it scales smoothly across phone widths (iPhone SE through Pro Max stay in the 60–78px range).

### Mobile drawer

- Slides in from the **left** (Cox & Cox pattern)
- Includes a dedicated **close X button** at the top-right of the drawer (the hamburger animates to X but isn't always reliable as the only close affordance)
- Backdrop `rgba(15,25,22,.55)` fades in; tap to close
- `body.menu-open { overflow: hidden }` locks the page scroll
- ESC, link-tap, and viewport-grow also close
- **Mega menu sub-categories** become **collapsible accordions** inside the drawer — each top-level item has a `›` chevron that rotates 90° when expanded. Top-level taps toggle the accordion; sub-link taps navigate and close the drawer.

---

## 6. Component patterns

### Section heading
```html
<header class="section-head section-head--center">
  <span class="eyebrow">Shop by department</span>
  <h2>Featured categories</h2>
  <p>Short intro line, max ~60ch.</p>
</header>
```
- Eyebrow → H2 → intro paragraph
- `section-head--center` centres the block; remove modifier for left-aligned
- Bottom margin: `56px` (desktop), `32–40px` (mobile)

### Category card
- Image in a portrait `4:5` aspect ratio (`5:4` on very small mobile)
- Below the image: centred serif label only (**no "Shop now" CTA** — the whole card is the link)
- Label is the visual hero (`clamp(22px, 2.4vw, 30px)`)
- Hover: card lifts 4px, image scales 1.04×, label colour shifts to `--accent`

### Offer card
- Cream art panel (`5:4` aspect on desktop, `4:3` on mobile) with the product PNG centred and a soft `drop-shadow` filter
- Outlined "Save X%" badge top-left, sale price stack bottom-right (strikethrough was-price + large serif now-price in `--accent`)
- Body below the art: eyebrow → H3 → description → `.link-arrow` "Shop offer →"
- Product PNGs **must have transparent backgrounds** (use the flood-fill PIL script pattern) so the drop-shadow follows the silhouette, not a white rectangle

### Brand grid
- Single white panel with hairline-divider grid cells
- Cells `aspect-ratio: 5/4` (`1:1` on mobile)
- Logos `mix-blend-mode: multiply` to dissolve their white backgrounds into the white cell
- Logo `max-width: 75–88%`, `max-height: clamp(44px, 6vw, 72px)` — uniform visual scale regardless of original artwork
- `overflow: hidden` on cells so any brand-coloured logo backgrounds get clipped to the cell edge

### Trust band
- Background: `--accent` (deep forest green), text in cream
- Three items: line-icon + serif heading + sans sub-text
- Desktop: horizontal row with hairline dividers between items
- Mobile: vertical column, icon-above-text, all centred
- Icons coloured `#d8c89a` (warm gold) for contrast on the dark green

### Footer
- Background near-black `#1a1f1c`
- Four columns: brand intro (with logo on a small cream plate), customer services, company, contact
- Cream `#f3ede2` headings, soft `#c8c3b6` body links, accent on hover
- Footer base bar with `--ink-deep` border and tracked-uppercase copyright

### Form fields (`.field` + `.field__input`)
- Used by the account pages — single canonical input style for the whole site
- Top label is tiny tracked uppercase sans (`12px / 500 / 0.12em`, colour `--muted`); add `<span class="req">*</span>` for required
- Inputs: 14px 16px padding, 1px `--line` border, `--accent` border + 1px inset shadow on `:focus`; subtle warm border on hover (`#c9c1b3`)
- `.field__hint` for help text under an input (e.g. "A password will be sent to your email address.")
- `.checkbox` is an inline-flex label wrapping the native `<input type="checkbox">` (accent-coloured via `accent-color: var(--accent)`); `.checkbox--block` is the same but top-aligned for longer multi-line consent text
- `.account-notice` is a `--paper-2`-tinted notice panel (1px line border) for inline policy / privacy copy

### Mega menu (desktop)
- Full-width drop spanning the viewport
- Three columns of sub-category links + one promo card on the right (4-col grid on desktop)
- Hairline rule under each column heading
- Soft fade + 10px slide-up on hover (`.28s ease`)
- Parent nav item stays in hover state (accent + underline) while mega is open

### Cart mini-dropdown (`.cart-dock` + `.cart-dropdown`)
- Anchored to the basket icon in the header; opens on `:hover` / `:focus-within` (desktop only — hidden ≤1024px so the basket icon links straight to the cart page on tablet/mobile)
- 380px wide white panel with hairline border + soft shadow; small pseudo-element arrow points up at the icon
- Sections: `__head` (title + item count) → `.cart-items` list (max-height 320px, scrolls) → `__foot` (sub-total, `(excl. delivery)` caption, "View bag" ghost + "Checkout" primary buttons)
- Each `.cart-item` is a 3-column grid: 64px image plate (`--paper-2` bg, `mix-blend-mode: multiply` logo), name + qty/price meta, price + Remove button
- Empty state (`.cart-empty`): basket icon, "Your cart is currently empty.", ghost "Return to shop" button — mirrors the live WooCommerce mini-cart copy

### Account pages (`.account` + `.account-card`)
- `.account` section sits on `--paper`, generous vertical padding (`clamp(48px, 6vw, 96px)` top, `clamp(64px, 8vw, 112px)` bottom)
- Centred `.account__head` block: eyebrow + serif H1 (with `<em>` italic-style emphasis matching homepage hero) + lead paragraph
- `.account-grid` is a 2-column grid (`1fr 1fr`) on desktop, collapses to single column ≤768px; use `.account-grid--single` modifier for lost-password to centre a max-520px panel
- Each `.account-card` is white with 1px hairline border, padding `clamp(28px, 3.4vw, 48px)`
- `.account-card__head` separates from the form with a hairline divider (H2 + small lead paragraph)
- Form pattern: `.account-form` is flex column with 18px gap, each `.field` is label-above-input with 8px gap, `.account-row` is the inline "Remember me" + "Lost your password?" line

---

## 7. Spacing & rhythm rules

- **Section padding**: `var(--section-y) 0` (top and bottom equal)
- **Section heading bottom margin**: `56px` desktop, `32–40px` mobile
- **Card gap**: 40–48px on desktop, scales down to 20–32px on mobile
- **Card body padding**: 28–36px desktop, 20–24px mobile
- **Eyebrow bottom margin**: `18px` (desktop), `14–16px` (mobile)
- **H1 bottom margin**: `24px` (desktop), `18px` (mobile)
- **Paragraph bottom margin**: `24–36px` depending on whether a CTA follows

---

## 8. Imagery

### Hero
- **Editorial lifestyle photography** at Cox & Cox quality bar — soft natural light, real environments, plants/textures/wood
- Aspect: `5:4` landscape on desktop, `4:5` portrait full-bleed on mobile
- Mobile: image **above** copy, edge-to-edge (no horizontal gutter)
- Source: Unsplash is fine; download locally to `assets/`, never hot-link

### Category tiles
- Lifestyle or process shots — gardener pruning, brass door knob on wood, hands working with materials
- Aspect: `4:5` portrait on desktop, scales to `4:5` or `5:4` on mobile
- Compositional consistency: warm tones, natural light, single subject

### Product images (offers)
- Transparent PNGs with the white background removed via flood-fill (PIL script: walk inward from edges through near-white pixels and set their alpha to 0, walls of "real" colour stop the fill)
- Centred on the cream art panel with a soft 14–24px drop-shadow

### Logo
- **Header**: `assets/p2logo.png` — the original transparent logo, no backdrop, 76–88px tall
- **Footer**: same `assets/p2logo.png` superimposed on a small cream `padding: 14px 22px; border-radius: 3px` plate so the dark wordmark reads against the dark footer

### Brand logos
- Hot-linked from the original perfect2trade.uk CDN is acceptable as a placeholder; production should download locally
- Display via `mix-blend-mode: multiply` on a white cell so any white backgrounds merge seamlessly

---

## 9. Interaction & motion

- **Card hover**: `translateY(-4 to -6px)`, image `scale(1.03–1.06)`, optional `box-shadow` lift
- **Link arrow** (`.link-arrow`): hover widens `letter-spacing` from `0.24em → 0.28em` and tints colour to `--ink`
- **Nav underline**: animated from `left: 50%; right: 50%` to `left: 0; right: 0` (centre-out reveal) on hover
- **Drawer**: cubic-bezier `(.2, .8, .2, 1)` over `.32s`
- **Mega menu**: simple opacity + 10px translate over `.28s ease`
- **Page transitions / scroll animation**: none. The design relies on static elegance — don't introduce scroll-triggered animations.

---

## 10. Bootstrap 4.4 compatibility

The page can be dropped into a Bootstrap 4.4 / WooCommerce project. See `bootstrap-port/` for an example where Bootstrap is loaded **before** our `styles.css` so the cascade keeps our design rules winning. Key collision points:

- `.container` — Bootstrap's max-widths are overridden by our 1200px
- `.btn` — we use `.btn--primary` BEM variant; Bootstrap's `.btn-*` variants are untouched
- `.badge` — we use it as a small basket-count pill; Bootstrap's `.badge-pill` etc. variants are unused

When integrating into WordPress/WooCommerce:
- HTML markup → PHP templates (`front-page.php`, `header.php`, `footer.php`, page templates)
- Static product cards → WooCommerce product loops (`wc_get_products`, `the_product()`)
- Static category tiles → `WP_Term_Query` on `product_cat` taxonomy
- Menus → `wp_nav_menu()` with custom Walker for the mega-menu structure
- Enqueue our CSS via `wp_enqueue_style` in `functions.php`

---

## 11. File / asset conventions

```
homepage-redesign/
├── index.html
├── styles.css
├── design.md           ← this document
├── CLAUDE.md           ← AI agent guide that references design.md
├── assets/
│   ├── p2logo.png            (transparent header + footer logo)
│   ├── hero-garden.jpg       (hero lifestyle image)
│   ├── category-garden.jpg   (Garden & Seasonal tile)
│   ├── category-ironmongery.jpg
│   ├── offer-sika.png        (transparent product cutout)
│   ├── offer-deicer.png      (transparent product cutout)
│   └── ...
└── bootstrap-port/     (drop-in Bootstrap 4.4 version)
    ├── index.html
    └── styles.css
```

**Naming:**
- Category tiles: `category-{slug}.jpg`
- Hero images: `hero-{topic}.jpg`
- Offer product PNGs: `offer-{slug}.png` (must have transparent bg)
- Brand logos: original filenames (`brand-{name}.png`)

**Image sourcing priority:**
1. Real product imagery from the live site (with transparent BG processed via PIL)
2. Cox & Cox-style lifestyle photography from Unsplash (always downloaded locally)
3. Custom CSS editorial cards as a last-resort fallback (gradient backgrounds, oversized type)

---

## 12. What to NEVER do

- ✗ Hardcode hex values in components — always use the CSS custom properties
- ✗ Add bouncy / scroll-triggered animations
- ✗ Use `text-align: center` on body paragraphs (only on section heads and small captions)
- ✗ Stretch wide promo banners into portrait crops — they need their native aspect, or use cropped single-product PNGs
- ✗ Use Bootstrap default button styles, modal styles, or card components — they break the editorial tone
- ✗ Add `box-shadow` on most components — use it only on hover lifts (`0 24–40px 40–70px -28 to -40px rgba(31,38,34,.15–.35)`) and a single subtle shadow under the brand grid panel
- ✗ Use serif italics on the body text — italics only for H1/H2 emphasis
- ✗ Hide content on mobile that's visible on desktop (the mega menu sub-categories become accordion, not hidden)
