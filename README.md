# Media Support website redesign (concept)

A redesign concept for the Media Support website. It keeps the existing red, white and charcoal brand and the business information from the current site.

**This repository is private and should stay private.** It contains Media Support's name, branding and staff contact details. Do not make the repository public or switch on a public GitHub Pages site without the company's approval.

## View it

- **Computer:** download the repository (Code → Download ZIP), extract it and open `index.html` in a browser.
- **Phone preview:** `preview/Media_Support_Website.html` is the whole site in one file, with all pages stacked on one scrolling page, for phone file previews that can't open multi-page sites.

## What's in here

| Path | What it is |
| --- | --- |
| `index.html` … `search.html` | The nine pages: Home, Services, four service pages, Delivery help, Contact, Search |
| `style.css`, `site.js`, `airport.webp` | Shared styles, interactions and hero photo |
| `preview/` | Single-file version for phone previews |
| `docs/Media_Support_Website_Review.pdf` | Full review: scorecard, before/after, findings and open decisions |
| `tools/` | Scripts that generate the pages and the single-file preview |

## Editing

Page content lives in `tools/v3_build.py`; styles in `tools/v3_style.css`; scripts in `tools/v3_site.js`. To rebuild:

```bash
python3 tools/v3_build.py . . tools          # writes the pages, style.css and site.js into the repository root
python3 tools/single.py . preview/Media_Support_Website.html
```

The build reads `airport.webp` from the folder given as the second argument.

## Before going live

- Replace the email-draft contact form with server-side submission and a POPIA privacy notice.
- Host the logo (preferably SVG) and a favicon with the site instead of loading the logo from mediasupport.co.za.
- Replace the hand-built search index with real site search.
- Confirm every name, number and email with the team (see the decisions list in the review).
