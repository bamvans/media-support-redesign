"""Combine the built v3 site into one self-contained HTML file.
Usage: python3 -I single.py <site_dir> <out_file>"""
import sys, re, base64, pathlib
D = pathlib.Path(sys.argv[1]); OUT = pathlib.Path(sys.argv[2])
TITLES = {"index":"Home","services":"Services","airport":"Airport specialists","subscription":"Subscription & home delivery","networks":"Niche network delivery","marketing":"Direct marketing solutions","delivery-help":"Delivery help","contact":"Contact","search":"Search"}
PAGES = ["index", "services", "airport", "subscription", "networks", "marketing", "delivery-help", "contact", "search"]

css = (D / "style.css").read_text()
js = (D / "site.js").read_text()
img = "data:image/webp;base64," + base64.b64encode((D / "airport.webp").read_bytes()).decode()

home = (D / "index.html").read_text()
head = home[:home.index("<body>")]
head = re.sub(r'<link rel="stylesheet" href="style.css">', "", head)
head = re.sub(r'<script src="site.js" defer></script>', "", head)
head = re.sub(r'<meta property="og:image"[^>]*>', "", head)
head = head.replace("<title>", "<title>").replace("</head>", "")
header = home[home.index('<header class="hdr">'):home.index("</header>") + len("</header>")]
header = header.replace(' aria-current="page"', "")
import re as _re
header = _re.sub(r'<img referrerpolicy="no-referrer"[^>]*>', "", header)
tail = home[home.index("<footer>"):home.index("</body>")]

sections = []
for name in PAGES:
    h = (D / f"{name}.html").read_text()
    main = h[h.index('<main id="main">') + len('<main id="main">'):h.index("</main>")]
    main = main.replace('id="ask"', f'id="ask-{name}"').replace('href="#ask"', f'href="#ask-{name}"')
    label = TITLES[name]
    n = PAGES.index(name) + 1
    divider = f'<div class="pgbar"><div class="wrap"><span>Page {n} of {len(PAGES)}</span><strong>{label}</strong><a href="#pg-index">Back to top ↑</a></div></div>' if n > 1 else ''
    sections.append(f'<section class="pg" id="pg-{name}" aria-label="{label}">{divider}{main}</section>')
body = header + '<main id="main">' + "".join(sections) + "</main>" + tail

def relink(m):
    page, hash_ = m.group(1), m.group(2)
    if hash_:
        return f'href="{hash_}"'
    return f'href="#pg-{page}"'
body = re.sub(r'href="([a-z-]+)\.html(#[^"]*)?"', relink, body)
body = body.replace('action="search.html"', 'action="#pg-search"')
body = body.replace('src="airport.webp"', f'src="{img}"')

extra_css = """
/* Single-file version: every page is stacked on one long page, with a label at the start of each */
.pg{scroll-margin-top:70px}
.pgbar{background:var(--char);color:#fff;padding:14px 0;border-top:4px solid var(--red)}
.pgbar .wrap{display:flex;align-items:center;gap:14px;flex-wrap:wrap}
.pgbar span{font-size:12px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#ff8a8f}
.pgbar strong{font:800 20px/1.2 Manrope,sans-serif;letter-spacing:-.02em}
.pgbar a{margin-left:auto;color:#d9d6d7;font-size:14px}
/* Without JavaScript (e.g. some phone file previews) the menu button can't open, so show the links in a scrollable row */
html:not(.js) .menu-btn{display:none}
@media (max-width:900px){
  html:not(.js) .hdr-in{flex-wrap:wrap;padding:10px 0}
  html:not(.js) .mainnav{order:3;width:100%;margin:0;overflow-x:auto}
  html:not(.js) .mainnav>ul{gap:2px}
  html:not(.js) .mainnav>ul>li>a{white-space:nowrap;font-size:15px;padding:8px 12px;background:var(--soft)}
  html:not(.js) .mainnav .chev,html:not(.js) .mega{display:none}
}
"""
extra_js = """
// Single-file version: scroll to sections directly, without changing the address (phone previews can block that)
const topicFor = { sales: 'sales', delivery: 'delivery', accounts: 'accounts', operations: 'operations' };
document.addEventListener('click', (e) => {
  const a = e.target.closest('a[href^="#"]');
  if (!a) return;
  const id = a.getAttribute('href').slice(1);
  const el = id && document.getElementById(id);
  if (!el) return;
  e.preventDefault();
  const y = id === 'pg-index' ? 0 : el.getBoundingClientRect().top + window.scrollY - 70;
  window.scrollTo({ top: y, behavior: 'smooth' });
  const topic = document.querySelector('#topic');
  if (topic && topicFor[id]) {
    const opt = topic.querySelector('option[data-key="' + topicFor[id] + '"]');
    if (opt) { topic.value = opt.value; opt.selected = true; topic.dispatchEvent(new Event('change')); }
  }
});
"""
doc = (head + "<style>" + css + extra_css + "</style></head><body>"
       '<a class="skip" href="#main">Skip to content</a>' + body +
       "<script>" + js + extra_js + "</script></body></html>")
OUT.write_text(doc)
print("written", OUT, len(doc) // 1024, "KB")
