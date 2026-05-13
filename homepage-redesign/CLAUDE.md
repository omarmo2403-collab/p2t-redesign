# CLAUDE.md — Agent guide for the Perfect 2 Trade redesign

This file gives Claude / agents working in this repo the context needed to extend the design without re-deriving decisions every time.

## Read this first

📖 **[`design.md`](./design.md)** — the complete design system: colour tokens, type scale, breakpoints, component patterns, motion, mobile drawer pattern, do's and don'ts. **Every new page or component must follow it.**

If you're building a new page, the rule is:
1. Open `design.md`
2. Reuse existing CSS custom properties (`--ink`, `--paper`, `--paper-2`, `--accent`, `--serif`, `--sans`, `--container`, `--section-y`, `--gutter`)
3. Reuse existing components (`.section-head`, `.category-card`, `.offer-card`, `.brand-row`, `.trust`, `.link-arrow`, `.btn`, `.eyebrow`)
4. Match the responsive cascade (1024 → 768 → 640 → 420)
5. Only introduce new tokens or components when the design genuinely calls for it — and add the new pattern to `design.md` when you do

## Project layout

```
homepage-redesign/
├── index.html          ← the homepage
├── styles.css          ← the single stylesheet
├── design.md           ← design system reference (READ FIRST)
├── CLAUDE.md           ← this file
├── assets/             ← logos, hero, category, and product images (local)
└── bootstrap-port/     ← Bootstrap 4.4 drop-in version for WP/WooCommerce projects
```

## Working principles

- **Stick to the refined editorial aesthetic** — editorial, warm-neutral, typography-led
- **Don't introduce frameworks** (no Tailwind, no Bootstrap in the main page — the `bootstrap-port/` is the only Bootstrap-using variant)
- **No JavaScript frameworks** — the page uses a single inline `<script>` for the mobile drawer and accordion. Keep dependencies minimal.
- **Cache-bust on CSS changes** — bump the `?v=` query string on the stylesheet link in `index.html` whenever you change `styles.css`, so users see updates without manual refresh
- **Mobile responsiveness is first-class** — every change must work cleanly on iPhone SE through Pro Max widths (320–430px). Test the 4 breakpoints in `design.md`.

## When adding a new page

1. Copy the `<head>`, header, and footer blocks from `index.html` as the shell
2. Drop in new sections using the existing component patterns from `design.md`
3. Keep section-y rhythm (paper → sand → paper → sand → dark band → dark footer)
4. Reuse the mobile drawer mark-up + script verbatim (it powers nav across all pages)
5. Add the new page's CSS to `styles.css` (don't create new stylesheets) under a clearly-labelled section header

## When changing colours / typography / spacing

Edit the `:root` custom properties at the top of `styles.css` so the change propagates everywhere. Update `design.md` to reflect the new tokens.

## When adding new images

- Editorial lifestyle photos from Unsplash. **Always download locally to `assets/`** — never hot-link.
- Product images: process white backgrounds to transparent via the PIL flood-fill pattern (see `design.md` section 8). Save as PNG.
- Naming: `category-{slug}.jpg`, `hero-{topic}.jpg`, `offer-{slug}.png`.

## When integrating into the WordPress / WooCommerce project

Use `bootstrap-port/` as the reference. Hand off the CSS to a developer who will convert the markup into PHP templates using WP/WC functions (see `design.md` section 10 for the mapping table).
