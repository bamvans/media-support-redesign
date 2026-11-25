# Distribution company website: redesign demo

A working demo of a website redesign for a South African media distribution business. The company name, staff names, emails, phone numbers and addresses are placeholders (`Your Company`, `sales@example.com`, `011 000 0000`).

## View it

- **Live demo:** GitHub Pages serves this repository.
- **Computer:** download the repository (Code → Download ZIP), extract it and open `index.html`.
- **Phone file preview:** `preview/Your_Company_Website.html` is the whole site in one file, with all pages stacked on one scrolling page.

## What's in here

| Path | What it is |
| --- | --- |
| `index.html` … `search.html` | The nine pages: Home, Services, four service pages, Delivery help, Contact, Search |
| `style.css`, `site.js`, `airport.webp` | Shared styles, interactions and hero photo |
| `preview/` | Single-file version for phone previews |
| `tools/` | Scripts that generate the pages and the single-file preview |

## Editing

Page content lives in `tools/v3_build.py`, styles in `tools/v3_style.css` and scripts in `tools/v3_site.js`. To rebuild:

```bash
python3 tools/v3_build.py . . tools
python3 tools/single.py . preview/Your_Company_Website.html
```

## Before using it for a real company

- Put in the real name, logo, contacts and addresses, with the company's approval.
- Replace the email-draft contact form with server-side submission and a POPIA privacy notice.
- Replace the hand-built search index with real site search.
