"""Builds the v3 Your Company mockup. Usage: python3 -I v3_build.py <out_dir> <assets_dir> <scripts_dir>"""
import sys, json, shutil, pathlib, html
OUT = pathlib.Path(sys.argv[1]); ASSETS = pathlib.Path(sys.argv[2]); SCR = pathlib.Path(sys.argv[3])
OUT.mkdir(parents=True, exist_ok=True)
if (ASSETS / "airport.webp").resolve() != (OUT / "airport.webp").resolve():
    shutil.copy(ASSETS / "airport.webp", OUT / "airport.webp")
shutil.copy(SCR / "v3_style.css", OUT / "style.css")
shutil.copy(SCR / "v3_site.js", OUT / "site.js")

LOGO = ""  # logo image removed in the demo; the text wordmark is used
ORIG = "https://example.com"
JHB_TEL, JHB = "+27110000000", "011 000 0000"
CPT_TEL, CPT = "+27210000000", "021 000 0000"

def svg(d, w=2):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{d}</svg>'
I = {
 "plane": svg('<path d="M3 11l18-7-7 17-3-8-8-2zm8 2L21 4"/>', 1.7),
 "home": svg('<path d="M3 11l9-8 9 8v10H3zm6 10v-7h6v7"/>', 1.7),
 "venue": svg('<path d="M3 21h18M5 21V8l7-5 7 5v13M9 21v-5h6v5M9 11h.01M15 11h.01"/>', 1.7),
 "mega": svg('<path d="M3 10v4h4l6 4V6L7 10H3zm13-1a4 4 0 0 1 0 6m2.5-8.5a7.5 7.5 0 0 1 0 11"/>', 1.7),
 "arrow": svg('<path d="M5 12h14m-6-6 6 6-6 6"/>'),
 "chev": svg('<path d="m6 9 6 6 6-6"/>'),
 "search": svg('<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>'),
 "menu": svg('<path d="M4 7h16M4 12h16M4 17h16"/>'),
 "close": svg('<path d="M6 6l12 12M18 6 6 18"/>'),
 "phone": svg('<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>', 1.8),
 "mail": svg('<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>', 1.8),
 "pin": svg('<path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>', 1.8),
 "box": svg('<path d="M21 8 12 3 3 8v8l9 5 9-5zM3 8l9 5 9-5M12 13v8"/>', 1.7),
 "alert": svg('<circle cx="12" cy="12" r="9"/><path d="M12 7v6m0 3.5h.01"/>', 1.8),
 "doc": svg('<path d="M7 3h7l5 5v13H7zM14 3v5h5M10 13h6M10 17h6"/>', 1.7),
 "gear": svg('<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1a1.7 1.7 0 0 0-1.1-1.5 1.7 1.7 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1a1.7 1.7 0 0 0 1.5-1.1 1.7 1.7 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.8.3H9a1.7 1.7 0 0 0 1-1.5V3a2 2 0 1 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.8V9a1.7 1.7 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z"/>', 1.5),
 "people": svg('<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0M16 4.5a3.5 3.5 0 0 1 0 7m5.5 8.5a6.5 6.5 0 0 0-4-6"/>', 1.7),
 "leaf": svg('<path d="M5 21c0-9 5-15 15-16-1 10-7 15-15 16zm0 0 8-8"/>', 1.7),
 "hand": svg('<path d="M7 11V5.5a1.5 1.5 0 0 1 3 0V10m0-5.5v-1a1.5 1.5 0 0 1 3 0V10m0-5a1.5 1.5 0 0 1 3 0v5m0-3a1.5 1.5 0 0 1 3 0v7a7 7 0 0 1-7 7h-1a7 7 0 0 1-6-3.4L3 13.5a1.5 1.5 0 0 1 2.6-1.5L7 14"/>', 1.6),
 "check": svg('<path d="m5 12 4.5 4.5L19 7"/>', 2.2),
 "school": svg('<path d="m2 9 10-5 10 5-10 5zM6 11v5c3 2.5 9 2.5 12 0v-5"/>', 1.7),
 "spark": svg('<path d="M12 3v4m0 10v4M3 12h4m10 0h4M6 6l2.5 2.5m7 7L18 18M6 18l2.5-2.5m7-7L18 6"/>', 1.7),
 "chat": svg('<path d="M21 12a8 8 0 0 1-11.8 7L4 20l1-4.6A8 8 0 1 1 21 12z"/>', 1.8),
 "clock": svg('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>', 1.8),
 "store": svg('<path d="M3 9h18l-1.5-5h-15zM4 9v11h16V9M9 20v-6h6v6"/>', 1.7),
}

SERVICES = [
 dict(slug="airport", name="Airport specialists", icon="plane",
      short="Newspapers and magazines in terminals, lounges and restricted areas, plus handouts to passengers.",
      best="Reaching travellers", tags=["Restricted areas","Merchandising","Passenger handouts"]),
 dict(slug="subscription", name="Subscription & home delivery", icon="home",
      short="Door-to-door delivery to your subscribers, 365 days a year, on morning and afternoon rounds.",
      best="Publishers with subscribers", tags=["Daily, weekly, monthly","Morning & afternoon rounds"]),
 dict(slug="networks", name="Niche network delivery", icon="venue",
      short="Your title in hotels, dealerships, salons, offices, schools, universities and other specialist venues.",
      best="Trade and controlled-free titles", tags=["Specialist venues","Schools & tertiary","Special projects"]),
 dict(slug="marketing", name="Direct marketing solutions", icon="mega",
      short="Samples, promotional material and product launches delivered to households in suburbs you choose.",
      best="Brands promoting a product", tags=["Product sampling","Promotions","Launches"]),
]
SVC = {s["slug"]: s for s in SERVICES}

def esc(s): return html.escape(s, quote=False)

def head(title, desc, extra=""):
    return f'''<!doctype html>
<html lang="en-ZA"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title><meta name="description" content="{html.escape(desc)}">
<meta name="theme-color" content="#cf121b"><meta property="og:type" content="website"><meta property="og:site_name" content="Your Company">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:image" content="airport.webp">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700&amp;family=Manrope:wght@500;700;800&amp;display=swap"><link rel="stylesheet" href="style.css"><script src="site.js" defer></script>{extra}</head>
<body><a class="skip" href="#main">Skip to content</a>'''

def header(cur):
    def ac(k): return ' aria-current="page"' if cur == k else ''
    mega = "".join(f'<a href="{s["slug"]}.html"><span class="ico">{I[s["icon"]]}</span><span><strong>{esc(s["name"])}</strong><span>{esc(s["best"])}</span></span></a>' for s in SERVICES)
    svc_cur = ' aria-current="page"' if cur in ("services",) + tuple(SVC) else ''
    return f'''<header class="hdr"><div class="wrap hdr-in">
<a class="brand" href="index.html" aria-label="Your Company home"><span><b>your</b>company</span></a>
<nav class="mainnav" id="mainnav" aria-label="Main"><ul>
<li class="has-menu"><a href="services.html"{svc_cur}>Services {I["chev"].replace("<svg ", '<svg class="chev" ')}</a><div class="mega"><div class="mega-grid">{mega}</div><a class="mega-foot link" href="services.html#fit">Not sure which fits? Compare services {I["arrow"]}</a></div></li>
<li><a href="delivery-help.html"{ac("delivery")}>Delivery help</a></li>
<li><a href="index.html#about">About</a></li>
<li><a href="contact.html"{ac("contact")}>Contact</a></li>
</ul></nav>
<div class="hdr-actions"><a class="iconbtn" href="search.html" aria-label="Search the site"{ac("search")}>{I["search"]}</a><a class="btn btn-sm hdr-call" href="tel:{JHB_TEL}">{I["phone"]}{JHB}</a>
<button class="iconbtn menu-btn" type="button" aria-controls="mainnav" aria-expanded="false" aria-label="Open menu" data-open='{I["menu"]}' data-close='{I["close"]}'>{I["menu"]}</button></div>
</div></header>'''

def footer():
    svc = "".join(f'<li><a href="{s["slug"]}.html">{esc(s["name"])}</a></li>' for s in SERVICES)
    return f'''<footer><div class="wrap">
<div class="foot-grid">
<div><div class="foot-brand"><b>your</b>company</div><p>Media distribution and direct marketing for publishers and brands across South Africa.</p></div>
<div><h2>Services</h2><ul>{svc}<li><a href="services.html#fit">Compare services</a></li></ul></div>
<div><h2>Help</h2><ul><li><a href="delivery-help.html">Late or missing delivery</a></li><li><a href="contact.html#needs">Who should I contact?</a></li><li><a href="contact.html#accounts">Invoices and payments</a></li><li><a href="search.html">Search the site</a></li></ul></div>
<div><h2>Offices</h2>
<div class="foot-office"><strong>Johannesburg head office</strong>Also covers KwaZulu-Natal<br><a href="tel:{JHB_TEL}">{JHB}</a></div>
<div class="foot-office"><strong>Cape Town</strong><a href="tel:{CPT_TEL}">{CPT}</a></div></div>
</div>
<div class="foot-bottom"><span>© Your Company</span><nav aria-label="Legal and account"><a href="{ORIG}/Privacy">Privacy</a><a href="{ORIG}/Terms">Terms</a><a href="{ORIG}/Login">Account holders: log in</a><a href="{ORIG}/Register">Register</a></nav></div>
</div></footer>
<div class="qbar" aria-label="Quick contact"><a class="btn btn-ghost" href="tel:{JHB_TEL}">{I["phone"]}Call us</a><a class="btn" href="contact.html#needs">Who to contact</a></div>
</body></html>'''

def page(name, title, desc, cur, body, extra=""):
    (OUT / name).write_text(head(title, desc, extra) + header(cur) + f'<main id="main">{body}</main>' + footer())

def svc_cards(feature=None):
    out = []
    for i, s in enumerate(SERVICES, 1):
        f = " svc-feature" if s["slug"] == feature else ""
        chips = f'<li class="best">Best for: {esc(s["best"].lower())}</li>' + "".join(f"<li>{esc(t)}</li>" for t in s["tags"])
        out.append(f'<a class="svc rv{f}" href="{s["slug"]}.html"><div class="svc-top"><span class="ico ico-lg">{I[s["icon"]]}</span><span class="svc-num">0{i}</span></div><h3>{esc(s["name"])}</h3><p>{esc(s["short"])}</p><ul class="chips">{chips}</ul><span class="link">Explore service {I["arrow"]}</span></a>')
    return '<div class="svc-grid">' + "".join(out) + "</div>"

def cta(title="Let’s talk distribution.", text="Tell us what you’re distributing and who you want to reach. We’ll point you to the right channel."):
    return f'''<section class="cta"><div class="wrap"><div class="cta-box rv">
<div><h2>{title}</h2><p>{text}</p></div>
<div class="cta-actions"><a class="cta-phone" href="tel:{JHB_TEL}">{I["phone"]}<span><small>Johannesburg head office</small><strong>{JHB}</strong></span></a><a class="cta-phone" href="tel:{CPT_TEL}">{I["phone"]}<span><small>Cape Town</small><strong>{CPT}</strong></span></a><a class="btn btn-white" href="contact.html#needs">Find the right person {I["arrow"]}</a></div>
</div></div></section>'''

ORG = {
 "@context": "https://schema.org", "@type": "Organization", "name": "Your Company", "url": "https://example.com/",
 "description": "Media distribution and direct marketing across South Africa.",
 "location": [
  {"@type": "Place", "name": "Johannesburg head office", "telephone": "+27 11 000 0000", "address": {"@type": "PostalAddress", "streetAddress": "Unit 1, Example Office Park", "addressLocality": "Johannesburg", "addressCountry": "ZA"}},
  {"@type": "Place", "name": "Cape Town office", "telephone": "+27 21 000 0000", "address": {"@type": "PostalAddress", "streetAddress": "Unit 2, Example Business Park, Cape Town", "addressLocality": "Cape Town", "addressCountry": "ZA"}}],
 "contactPoint": [{"@type": "ContactPoint", "telephone": "+27 11 000 0000", "contactType": "customer service", "areaServed": "ZA"}]}
JSONLD = '<script type="application/ld+json">' + json.dumps(ORG) + '</script>'

# ---------------- HOME ----------------
paths = [
 ("services.html", "box", "Distribute a publication", "Airports, homes or venues"),
 ("marketing.html", "mega", "Run a sampling campaign", "Households in chosen suburbs"),
 ("delivery-help.html", "alert", "My delivery is late or missing", "For subscribers and readers"),
 ("contact.html#accounts", "doc", "Invoices and payments", "Talk to our finance team"),
]
paths_html = "".join(f'<a class="path" href="{h}"><span class="ico">{I[ic]}</span><span><strong>{t}</strong><span>{s}</span></span>{I["arrow"].replace("<svg ", "<svg class=\"arrow\" ")}</a>' for h, ic, t, s in paths)

home = f'''
<section class="hero"><div class="wrap hero-grid">
<div><p class="eyebrow">Media distribution across South Africa</p>
<h1>Get your publications to the <em>right readers.</em></h1>
<p class="lead">From major airports to subscribers’ doorsteps, Your Company helps publishers and brands reach the audiences that matter to them.</p>
<div class="actions"><a class="btn" href="services.html">Explore services {I["arrow"]}</a><a class="btn btn-ghost" href="contact.html#needs">Talk to our team</a></div>
</div>
<div class="hero-media"><figure><img src="airport.webp" alt="Travellers walking through a bright airport terminal" width="1200" height="1300" fetchpriority="high"></figure>
</div>
</div></section>

<section class="paths"><div class="wrap"><div class="paths-card rv"><h2>How can we help?</h2><div class="paths-grid">{paths_html}</div></div></div></section>

<section class="section" id="services"><div class="wrap">
<div class="section-head"><div><p class="eyebrow">Our services</p><h2>Four ways to reach<br>your readers.</h2></div><p class="lead">Pick the channel that matches who you want to reach. Not sure? <a class="ul" href="services.html#fit">Compare services</a>.</p></div>
{svc_cards(feature="airport")}
</div></section>

<section class="section dark" id="coverage"><div class="wrap">
<p class="eyebrow">Where we work</p><h2>National reach, local rounds.</h2>
<p class="lead">Home delivery across five provinces and distribution at South Africa’s major airports.</p>
<div class="stats">
<div class="stat rv"><strong>365<span>.</span></strong><p>days a year delivery</p></div>
<div class="stat rv"><strong>6</strong><p>core airports</p></div>
<div class="stat rv"><strong>5</strong><p>provinces with home delivery</p></div>
<div class="stat rv"><strong>2</strong><p>offices: Johannesburg and Cape Town</p></div>
</div>
<div class="cover-grid">
<div class="panel rv"><h3><span class="ico">{I["home"]}</span>Home delivery areas</h3><dl class="regions">
<div><dt>Gauteng</dt><dd>Greater Johannesburg, Sandton, Rosebank, Randburg, Ekurhuleni, Pretoria</dd></div>
<div><dt>KwaZulu-Natal</dt><dd>Durban and surrounds, Pietermaritzburg</dd></div>
<div><dt>Western Cape</dt><dd>Cape Town and the Seaboard</dd></div>
<div><dt>Eastern Cape</dt><dd>Port Elizabeth</dd></div>
<div><dt>Free State</dt><dd>Bloemfontein</dd></div></dl></div>
<div class="panel rv"><h3><span class="ico">{I["plane"]}</span>Core airports</h3><ul class="airports"><li>O. R. Tambo International</li><li>Cape Town International</li><li>King Shaka International</li><li>Lanseria International</li><li>Port Elizabeth</li><li>Bloemfontein</li></ul></div>
</div></div></section>

<section class="section soft" id="about"><div class="wrap">
<div class="section-head"><div><p class="eyebrow">How we work</p><h2>Partners, not just couriers.</h2></div></div>
<div class="values">
<article class="value rv"><span class="ico ico-lg">{I["hand"]}</span><h3>Our approach to your business</h3><p>We work openly with publishers to tailor distribution and marketing plans, reach target audiences and build new readership.</p></article>
<article class="value rv"><span class="ico ico-lg">{I["people"]}</span><h3>Our people</h3><p>In line with our BEE policy, we train and support young entrepreneurs to build sustainable businesses, create jobs and develop skills.</p></article>
<article class="value rv"><span class="ico ico-lg">{I["leaf"]}</span><h3>Environmental consideration</h3><p>We work to reduce and offset our footprint, encourage non-motorised deliveries and train our teams in vehicle maintenance.</p></article>
</div></div></section>
<div class="soft">{cta()}</div>'''
page("index.html", "Your Company | Publication distribution & direct marketing in South Africa",
     "Airport, subscription, niche network and direct marketing distribution for publishers and brands across South Africa. Offices in Johannesburg and Cape Town.",
     "home", home, JSONLD)

# ---------------- SERVICES ----------------
fit = [
 ("airport.html", "I want to reach <b>travellers</b>", "Airport specialists"),
 ("subscription.html", "I need copies delivered to <b>my subscribers’ homes or offices</b>", "Subscription & home delivery"),
 ("networks.html", "I want my title in <b>hotels, venues, schools or universities</b>", "Niche network delivery"),
 ("marketing.html", "I want <b>samples or promotions</b> in particular suburbs", "Direct marketing solutions"),
 ("delivery-help.html", "I’m a <b>subscriber</b> and my delivery is late or missing", "Delivery help"),
]
fit_html = "".join(f'<li><a href="{h}"><span>{q}</span><span class="to">{esc(t)}</span>{I["arrow"]}</a></li>' for h, q, t in fit)
services = f'''
<section class="phero"><div class="wrap"><ol class="crumbs"><li><a href="index.html">Home</a></li><li aria-current="page">Services</li></ol>
<p class="eyebrow">Services</p><h1>Distribution that <em>fits your audience.</em></h1><p class="lead">Four services for publishers and brands across South Africa. Each one is built around a different kind of reader.</p></div></section>
<section class="section"><div class="wrap">{svc_cards(feature="airport")}</div></section>
<section class="section soft" id="fit"><div class="wrap"><div class="section-head"><div><p class="eyebrow">Compare</p><h2>Which service fits?</h2></div><p class="lead">Start with who you want to reach.</p></div>
<ul class="fit rv">{fit_html}</ul>
<p class="muted" style="margin-top:24px">Still unsure? Call <a class="ul" href="tel:{JHB_TEL}">{JHB}</a> or <a class="ul" href="mailto:sales@example.com?subject=Which%20service%20fits%3F">email sales &amp; operations</a>.</p></div></section>
<div class="soft">{cta()}</div>'''
page("services.html", "Services | Your Company", "Compare Your Company’s airport, subscription and home delivery, niche network and direct marketing services.", "services", services)

# ---------------- SERVICE DETAIL PAGES ----------------
SALES_CARD = lambda subj, title, text: f'''<div class="card"><h2>{title}</h2><p>{text}</p>
<a class="btn" href="mailto:sales@example.com?subject={subj}">{I["mail"]}Email sales &amp; operations</a>
<div class="mini"><span class="avatar">SL</span><span><strong>Sales lead</strong>Director · <a href="tel:+27820000000">082 000 0000</a></span></div>
<div class="mini"><span class="avatar">SD</span><span><strong>Sales director</strong>Director · <a href="mailto:director@example.com">director@example.com</a></span></div></div>'''
CALL_CARD = f'''<div class="card card-dark"><h2>Prefer to call?</h2><p>Johannesburg head office <a href="tel:{JHB_TEL}" style="color:#fff;font-weight:700">{JHB}</a><br>Cape Town <a href="tel:{CPT_TEL}" style="color:#fff;font-weight:700">{CPT}</a></p><a class="link" style="color:#fff" href="contact.html#needs">See everyone you can contact {I["arrow"]}</a></div>'''

def block(icon, title, text, items=None):
    li = ("<ul>" + "".join(f"<li>{esc(x)}</li>" for x in items) + "</ul>") if items else ""
    return f'<section class="block rv"><span class="ico ico-lg">{I[icon]}</span><div><h2>{title}</h2><p>{text}</p>{li}</div></section>'

def service_page(slug, lead, facts, blocks, aside, orig_path):
    s = SVC[slug]
    facts_html = "".join(f'<div class="fact"><strong>{a}</strong><span>{b}</span></div>' for a, b in facts)
    others = "".join(f'<a class="other" href="{o["slug"]}.html"><span class="ico">{I[o["icon"]]}</span><strong>{esc(o["name"])}</strong>{I["arrow"].replace("<svg ", "<svg class=\"arrow\" ")}</a>' for o in SERVICES if o["slug"] != slug)
    body = f'''
<section class="phero"><div class="wrap"><ol class="crumbs"><li><a href="index.html">Home</a></li><li><a href="services.html">Services</a></li><li aria-current="page">{esc(s["name"])}</li></ol>
<div class="phero-svc"><span class="ico ico-lg">{I[s["icon"]]}</span><div><h1>{esc(s["name"])}</h1><p class="lead">{lead}</p>
<ul class="chips"><li class="best">Best for: {esc(s["best"].lower())}</li></ul><a class="btn" href="#ask">{I["mail"]}Ask about this service</a></div></div>
<div class="facts">{facts_html}</div></div></section>
<section class="section"><div class="wrap detail"><div class="blocks">{"".join(blocks)}
<p><a class="link" href="{ORIG}{orig_path}">Read more {I["arrow"]}</a></p></div>
<aside class="aside" id="ask">{aside}{CALL_CARD}</aside></div></section>
<section class="section soft"><div class="wrap"><h2 style="font-size:clamp(28px,3vw,40px)">Other services</h2><div class="others">{others}</div></div></section>'''
    page(f"{slug}.html", f"{s['name']} | Your Company", s["short"], slug, body)

service_page("airport",
 "Put your publications in front of travellers at South Africa’s major airports, from restricted areas to passenger handouts.",
 [("6 core airports", "International and domestic"), ("Restricted areas", "Trained, cleared personnel"), ("End to end", "Collection to merchandising")],
 [block("plane", "Airport distribution and merchandising", "Trained personnel distribute local and international publications, including in restricted areas. We can handle the whole chain after delivery.", ["Collection","Warehousing","Packaging","Labelling","Merchandising"]),
  block("people", "Campaigns for travellers", "Plan passenger handouts at check-in or reach travellers through airport restaurants, car rental companies and hotels. Campaigns are tailored to your audience, with supply planned to limit waste."),
  block("pin", "Core airports", "O. R. Tambo, Cape Town, King Shaka and Lanseria international airports, plus Port Elizabeth and Bloemfontein.")],
 SALES_CARD("Airport%20specialists%20enquiry", "Plan an airport campaign", "Tell us the title or product, which airports, and roughly how many copies or handouts."),
 "/Our-Services/Airport-Specialists")

service_page("subscription",
 "Door-to-door delivery of newspapers and magazines to your subscribers’ homes and businesses, every day of the year.",
 [("365 days", "Delivery every day of the year"), ("2 rounds", "Morning and afternoon"), ("5 provinces", "Major metros and surrounds")],
 [block("clock", "Delivery 365 days a year", "Door-to-door distribution for daily, weekly and monthly publications. Morning and afternoon delivery rounds give publishers more flexibility."),
  '<section class="block rv" id="areas"><span class="ico ico-lg">' + I["pin"] + '</span><div><h2>Areas served</h2><dl class="regions" style="margin-top:6px">'
  '<div><dt>Gauteng</dt><dd class="muted">Greater Johannesburg, Sandton, Rosebank, Randburg, Ekurhuleni, Pretoria</dd></div>'
  '<div><dt>KwaZulu-Natal</dt><dd class="muted">Durban and surrounds, Pietermaritzburg</dd></div>'
  '<div><dt>Western Cape</dt><dd class="muted">Cape Town and the Seaboard</dd></div>'
  '<div><dt>Eastern Cape</dt><dd class="muted">Port Elizabeth</dd></div>'
  '<div><dt>Free State</dt><dd class="muted">Bloemfontein</dd></div></dl></div></section>'],
 SALES_CARD("Subscription%20%26%20home%20delivery%20enquiry", "Publishers", "Need copies delivered to your subscribers? Tell us the title, how often it’s published and the areas.")
 + f'<div class="card" id="delivery-help" style="border-color:#efc3c5;background:var(--pink)"><h2>Subscriber?</h2><p>Is your newspaper or magazine late, missing or damaged? We’ll help you report it.</p><a class="btn btn-ghost" href="delivery-help.html">{I["alert"]}Get delivery help</a></div>',
 "/Our-Services/Subscription-Home-Delivery-Services")

service_page("networks",
 "Connect trade and consumer publications with readers in specialist venues, education networks and special projects.",
 [("Specialist venues", "Hospitality, retail, offices"), ("Education", "Schools, colleges, universities"), ("Special projects", "Launches, drives, sampling")],
 [block("store", "Specialist venues", "Our networks reach readers where they spend time, so your title lands in front of the right people.", ["Hotels & guest houses","Lounges","Car rental","Dealerships","Restaurants & cafés","Wine estates","Gated communities","Retirement villages","Government offices","Embassies","Travel agents","Sport facilities","Retailers","Salons"]),
  block("school", "Schools and tertiary education", "Reach schools, colleges and universities through a dedicated network that helps publishers grow their newspaper and magazine programmes in education."),
  block("spark", "Special projects", "Develop campaigns that build readership and awareness.", ["Readership campaigns","Subscription drives","Controlled free distribution","Product sampling","Publication launches"])],
 SALES_CARD("Niche%20network%20delivery%20enquiry", "Find the right venues", "Tell us about your title and readers, and we’ll suggest venues that fit."),
 "/Our-Services/Niche-network-delivery-services")

service_page("marketing",
 "Put product samples, promotional material and new product launches directly into households in the suburbs you choose.",
 [("Households", "Delivered door to door"), ("You choose", "Target selected suburbs"), ("Physical", "Samples and printed material")],
 [block("mega", "Targeted promotions", "Reach households in selected suburbs with physical marketing materials, product samples or a new product launch."),
  block("box", "What you can send", "Anything you want in a customer’s hands rather than their inbox.", ["Product samples","Promotional material","Marketing material","Launch packs"]),
  block("pin", "Where", 'Households in the suburbs you choose, across our delivery areas. <a class="ul" href="subscription.html#areas">See areas served</a>.')],
 SALES_CARD("Direct%20marketing%20solutions%20enquiry", "Plan a promotion", "Tell us what you’re promoting, which suburbs, and when."),
 "/Our-Services/Direct-marketing-solutions")

# ---------------- DELIVERY HELP ----------------
body_tpl = "Publication:%0D%0ADelivery address:%0D%0ADate(s) affected:%0D%0AWhat happened (late, missing or damaged):%0D%0ABest number to reach me:%0D%0A"
delivery = f'''
<section class="phero"><div class="wrap"><ol class="crumbs"><li><a href="index.html">Home</a></li><li aria-current="page">Delivery help</li></ol>
<p class="eyebrow">For subscribers and readers</p><h1>Delivery <em>late, missing</em> or damaged?</h1>
<p class="lead">Let our client services team know. A few details help them trace your delivery quickly.</p>
<div class="hero actions" style="background:none;padding:0;display:flex;flex-wrap:wrap;gap:12px;margin-top:28px"><a class="btn" href="mailto:deliveries@example.com?subject=Delivery%20problem&amp;body={body_tpl}">{I["mail"]}Email client services</a><a class="btn btn-ghost" href="tel:{JHB_TEL}">{I["phone"]}Call {JHB}</a></div></div></section>
<section class="section"><div class="wrap">
<ol class="steps">
<li class="rv"><h3>Gather the details</h3><p>Have these ready:</p><ul class="checklist"><li>{I["check"]}Publication name</li><li>{I["check"]}Delivery address</li><li>{I["check"]}Date or dates affected</li><li>{I["check"]}Late, missing or damaged</li></ul></li>
<li class="rv"><h3>Email client services</h3><p>Use the button above. It opens an email to client services with these questions already filled in.</p><p style="margin-top:12px"><a class="ul" href="mailto:deliveries@example.com">deliveries@example.com</a></p></li>
<li class="rv"><h3>Or call us</h3><p>Johannesburg head office (also KwaZulu-Natal): <a class="ul" href="tel:{JHB_TEL}">{JHB}</a></p><p style="margin-top:8px">Cape Town: <a class="ul" href="tel:{CPT_TEL}">{CPT}</a></p></li>
</ol>
<div class="needs" style="margin-top:20px">
<div class="card rv"><h2>Moved or changing address?</h2><p>Subscriber address updates and subscriber lists are handled by our subscription data team.</p><div class="mini"><span class="avatar">ST</span><span><strong>Subscription data team</strong><a href="mailto:subscriptions@example.com">subscriptions@example.com</a></span></div></div>
<div class="card rv"><h2>Are you a publisher?</h2><p>If you’re a publisher with a question about your delivery service, contact our operations team.</p><div class="mini"><span class="avatar">OM</span><span><strong>Operations manager</strong>National operations · <a href="mailto:operations@example.com">operations@example.com</a></span></div></div>
</div></div></section>'''
page("delivery-help.html", "Delivery help | Your Company", "Report a late, missing or damaged newspaper or magazine delivery to Your Company client services.", "delivery", delivery)

# ---------------- CONTACT ----------------
def person(initials, name, role, primary=None, links=()):
    btn = f'<a class="btn btn-sm" href="{primary[0]}">{I["mail"]}{primary[1]}</a>' if primary else ""
    lk = "".join(f'<a href="{h}">{t}</a>' for h, t in links)
    return f'<div class="person"><span class="avatar">{initials}</span><div><h4>{name}</h4><p>{role}</p><div class="person-links">{btn}{lk}</div></div></div>'

needs = [
 ("sales", "box", "New business", "Distribute a publication or run a campaign", "Airport, home delivery, venue networks and direct marketing.",
  person("SL", "Sales lead", "Director · Sales and operations", ("mailto:sales@example.com?subject=Distribution%20enquiry", "Email sales"), [("tel:+27820000000", "082 000 0000"), ("mailto:sales@example.com", "sales@example.com")])
  + person("SD", "Sales director", "Director · Sales and operations", None, [("mailto:director@example.com", "director@example.com")])),
 ("delivery", "alert", "Deliveries", "A delivery is late, missing or damaged", "Include the publication, your delivery address and the date.",
  person("CS", "Client services", "Deliveries team", ("mailto:deliveries@example.com?subject=Delivery%20problem", "Email client services"), [("mailto:deliveries@example.com", "deliveries@example.com")])
  + person("ST", "Subscription data team", "Subscription data and systems · address updates and subscriber lists", None, [("mailto:subscriptions@example.com", "subscriptions@example.com")])),
 ("accounts", "doc", "Accounts", "Invoices, statements and payments", "Include your invoice or account number if you have it.",
  person("FM", "Finance manager", "Invoices, statements and payments", ("mailto:accounts@example.com?subject=Accounts%20enquiry", "Email accounts"), [("mailto:accounts@example.com", "accounts@example.com")])
  + person("FD", "Finance director", "Director · Finance", None, [("mailto:finance@example.com", "finance@example.com")])),
 ("operations", "gear", "Existing clients", "Operations, schedules and national logistics", "For publishers and brands already distributing with us.",
  person("OM", "Operations manager", "National operations manager", ("mailto:operations@example.com?subject=Operations%20enquiry", "Email operations"), [("mailto:operations@example.com", "operations@example.com")])),
]
tiles = "".join(f'<a class="need-tile" href="#{k}"><span class="ico">{I[ic]}</span><strong>{t}</strong><span>{tag} {I["arrow"].replace("<svg ", "<svg style=\"width:14px;height:14px;vertical-align:-2px\" ")}</span></a>' for k, ic, tag, t, _, _ in needs)
need_cards = "".join(f'<article class="need rv" id="{k}"><div class="need-head"><span class="ico ico-lg">{I[ic]}</span><div><p class="need-tag">{tag}</p><h3>{t}</h3><p>{d}</p></div></div>{ppl}</article>' for k, ic, tag, t, d, ppl in needs)

contact = f'''
<section class="phero"><div class="wrap"><ol class="crumbs"><li><a href="index.html">Home</a></li><li aria-current="page">Contact</li></ol>
<p class="eyebrow">Contact</p><h1>Get to the <em>right person,</em> first time.</h1><p class="lead">Choose what you need and we’ll show you who handles it.</p>
<nav class="need-tiles" aria-label="What do you need?">{tiles}</nav></div></section>
<section class="section" id="needs"><div class="wrap"><h2 class="sr" style="font-size:clamp(28px,3vw,40px)">Who should I contact?</h2><div class="needs">{need_cards}</div></div></section>
<section class="section soft" id="offices" style="padding-top:clamp(56px,7vw,90px)"><div class="wrap"><div class="section-head"><div><p class="eyebrow">Offices</p><h2>Call or visit.</h2></div></div>
<div class="offices">
<article class="office rv"><h3>Johannesburg head office</h3><span class="covers">Also covers KwaZulu-Natal</span><address>Unit 1, Example Office Park, Johannesburg</address>
<div class="row"><a class="btn" href="tel:{JHB_TEL}">{I["phone"]}Call {JHB}</a><a class="btn btn-ghost" href="https://www.google.com/maps/search/?api=1&amp;query=Johannesburg">{I["pin"]}Directions</a></div>
<details><summary>Postal address and fax</summary><p style="margin-top:8px">PO Box 0000, Johannesburg, 0000<br>Fax 086 000 0000</p></details></article>
<article class="office rv"><h3>Cape Town</h3><span class="covers">Western Cape</span><address>Unit 2, Example Business Park, Cape Town</address>
<div class="row"><a class="btn" href="tel:{CPT_TEL}">{I["phone"]}Call {CPT}</a><a class="btn btn-ghost" href="https://www.google.com/maps/search/?api=1&amp;query=Cape+Town">{I["pin"]}Directions</a></div></article>
</div></div></section>
<section class="section"><div class="wrap"><div class="formwrap rv">
<div><p class="eyebrow">Write to us</p><h2>Prefer to write it down?</h2><p class="lead">Pick a topic and we’ll address your email to the person who handles it. You review and send it from your own email.</p></div>
<form id="enquiry" class="form"><label for="topic">What can we help with?</label><select id="topic" name="topic" required>
<option value="">Select a topic</option>
<option value="sales" data-key="sales" data-name="Sales lead, Sales and operations">Distributing a publication or running a campaign</option>
<option value="deliveries" data-key="delivery" data-name="Client services">A delivery is late, missing or damaged</option>
<option value="subscriptions" data-name="Subscription data team, Subscription data">Subscriber lists or address updates</option>
<option value="accounts" data-key="accounts" data-name="Finance manager">Invoices, statements or payments</option>
<option value="operations" data-key="operations" data-name="Operations manager, National operations">Operations for an existing client</option>
<option value="sales" data-name="Sales lead, Sales and operations">Something else / not sure</option></select>
<p class="route" id="route" aria-live="polite" hidden><span>Goes to <b id="route-name"></b> · <a id="route-email" href="#"></a></span><button type="button" class="copy" id="copy-email">Copy address</button></p>
<label for="name">Your name and company <span class="opt">(optional)</span></label><input id="name" name="name" autocomplete="name">
<label for="message">Your message</label><textarea id="message" name="message" maxlength="1500" required placeholder="Example: Our magazine wasn’t delivered to 12 Main Road, Rosebank on Tuesday."></textarea>
<button class="btn" type="submit">{I["mail"]}Open email draft</button>
<p class="fallback">Nothing opened? Your device may not have an email app set up. Copy the address above and send from your usual email.</p></form>
</div><p style="margin-top:24px"><a class="link" href="{ORIG}/Contact-Us">Back to home {I["arrow"]}</a></p></div></section>'''
page("contact.html", "Contact | Your Company", "Find the right Your Company contact for new business, deliveries, accounts or operations. Offices in Johannesburg and Cape Town.", "contact", contact, JSONLD)

# ---------------- SEARCH ----------------
R = [
 ("index.html#about", "people", "About Your Company", "Our approach, people and environmental considerations.", "about bee entrepreneurs environment company who we are"),
 ("services.html", "box", "Services overview", "Compare the four distribution and marketing services.", "publication distribution marketing compare which service"),
 ("airport.html", "plane", "Airport specialists", "Airport distribution, merchandising and passenger campaigns.", "tambo lanseria king shaka warehouse warehousing airport logistics cape town aircraft travellers lounges merchandising handouts"),
 ("subscription.html", "home", "Subscription & home delivery", "Door-to-door delivery and areas covered.", "durban joburg johannesburg pretoria sandton rosebank randburg ekurhuleni pietermaritzburg port elizabeth gqeberha bloemfontein seaboard home newspaper subscription magazines areas coverage"),
 ("networks.html", "venue", "Niche network delivery", "Specialist venues, education and special projects.", "hotels schools universities colleges specialist niche venues salons dealerships embassies trade controlled free launches"),
 ("marketing.html", "mega", "Direct marketing solutions", "Product sampling and targeted promotions.", "product samples sampling suburbs promotions advertising flyers leaflets launch households"),
 ("delivery-help.html", "alert", "Delivery help", "Report a late, missing or damaged delivery.", "delivery late missing missed damaged complaint problem not delivered subscriber paper newspaper magazine "),
 ("contact.html#accounts", "doc", "Invoices and payments", "Contact our finance team.", "finance invoice invoices statement payment pay billing account accounts "),
 ("contact.html#operations", "gear", "Operations for existing clients", "Contact our national operations manager.", "operations existing client schedule logistics "),
 ("contact.html", "phone", "Contact Your Company", "Office numbers, people to contact and an enquiry form.", "phone call email sales johannesburg cape town kwazulu natal whatsapp office address directions fax postal"),
]
results = "".join(f'<li data-keywords="{k}"><a href="{h}"><span class="ico">{I[ic]}</span><span><strong>{esc(t)}</strong><p>{esc(d)}</p></span>{I["arrow"].replace("<svg ", "<svg class=\"arrow\" ")}</a></li>' for h, ic, t, d, k in R)
search = f'''
<section class="phero"><div class="wrap"><ol class="crumbs"><li><a href="index.html">Home</a></li><li aria-current="page">Search</li></ol>
<h1>What are you <em>looking for?</em></h1>
<form id="site-search" role="search" action="search.html"><label class="sr-only" for="query" style="position:absolute;left:-9999px">Search this site</label><div class="searchbox">{I["search"]}<input id="query" name="q" type="search" placeholder="Try airport, missed delivery or invoice" autocomplete="off"><button class="btn" type="submit">Search</button></div></form>
<div class="suggest"><span>Popular:</span><button type="button">missed delivery</button><button type="button">invoice</button><button type="button">airports</button><button type="button">Durban</button><button type="button">sampling</button></div></div></section>
<section class="section" style="padding-top:48px"><div class="wrap"><p class="status" id="search-status" role="status"></p><ul class="results">{results}</ul>
<div class="search-help" id="search-help" hidden>Can’t find it? Call <a class="ul" href="tel:{JHB_TEL}">{JHB}</a> or see <a class="ul" href="contact.html#needs">who to contact</a>.</div>
<p class="web muted">Can’t find it here? <a class="ul" id="web-search" href="https://www.google.com/search?q=">Search the web</a></p></div></section>'''
page("search.html", "Search | Your Company", "Search Your Company services, delivery help and contacts.", "search", search)

print("built", sorted(p.name for p in OUT.iterdir() if p.suffix == ".html"))
