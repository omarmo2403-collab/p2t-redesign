# Perfect 2 Trade — Redesign

A static HTML/CSS redesign for [perfect2trade.uk](https://perfect2trade.uk) (UK trade supplies e-commerce).

**Live preview:** https://omarmo2403-collab.github.io/p2t-redesign/homepage-redesign/

## Stack
- Vanilla HTML + CSS (single shared `styles.css`)
- Minimal inline JS for the mobile drawer, mega-menu accordion, cart dropdown, and product modal
- No frameworks in the main site
- Optional Bootstrap 4.4 drop-in lives under `homepage-redesign/bootstrap-port/`

## Project layout
```
homepage-redesign/
  index.html
  category-garden-seasonal.html
  category-garden-chemicals.html
  product-algon-cleaner.html
  account-login.html
  account-lost-password.html
  cart.html
  checkout.html
  styles.css
  design.md
  CLAUDE.md
  assets/
  bootstrap-port/
```

## Local preview
```bash
python -m http.server 8765 -d homepage-redesign
```
Then open http://localhost:8765/

## Design system
See [`homepage-redesign/design.md`](homepage-redesign/design.md) for the full design system reference — typography, colour tokens, components, breakpoints.
