document.documentElement.classList.add('js');

// Header shadow once the page scrolls
const hdr = document.querySelector('.hdr');
const onScroll = () => hdr && hdr.classList.toggle('scrolled', window.scrollY > 8);
window.addEventListener('scroll', onScroll, { passive: true });
onScroll();

// Mobile menu
const menuBtn = document.querySelector('.menu-btn');
const nav = document.querySelector('#mainnav');
if (menuBtn && nav) {
  const setOpen = (open) => {
    nav.classList.toggle('open', open);
    menuBtn.setAttribute('aria-expanded', String(open));
    menuBtn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    menuBtn.innerHTML = open ? menuBtn.dataset.close : menuBtn.dataset.open;
    document.body.style.overflow = open ? 'hidden' : '';
  };
  menuBtn.addEventListener('click', () => setOpen(!nav.classList.contains('open')));
  nav.addEventListener('click', (e) => { if (e.target.closest('a')) setOpen(false); });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && nav.classList.contains('open')) { setOpen(false); menuBtn.focus(); } });
}

// Gentle reveal on scroll
const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
const rv = document.querySelectorAll('.rv');
if (!reduce && 'IntersectionObserver' in window) {
  const io = new IntersectionObserver((entries) => {
    for (const e of entries) if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
  }, { rootMargin: '0px 0px -8% 0px' });
  rv.forEach((el) => io.observe(el));
} else {
  rv.forEach((el) => el.classList.add('in'));
}

// Enquiry form: show who the message goes to, offer a copy fallback, open an email draft
const enquiry = document.querySelector('#enquiry');
if (enquiry) {
  const topic = enquiry.elements.topic;
  const route = document.querySelector('#route');
  const routeName = document.querySelector('#route-name');
  const routeEmail = document.querySelector('#route-email');
  const copyBtn = document.querySelector('#copy-email');
  const addr = () => topic.value + '@example.com';
  const showRoute = () => {
    if (!topic.value) { route.hidden = true; return; }
    routeName.textContent = topic.selectedOptions[0].dataset.name;
    routeEmail.textContent = addr();
    routeEmail.href = 'mailto:' + addr();
    copyBtn.textContent = 'Copy address';
    route.hidden = false;
  };
  topic.addEventListener('change', showRoute);
  copyBtn.addEventListener('click', async () => {
    try { await navigator.clipboard.writeText(addr()); copyBtn.textContent = 'Copied'; }
    catch { copyBtn.textContent = 'Select the address to copy it'; }
  });
  const presets = { '#sales': 'sales', '#delivery': 'delivery', '#accounts': 'accounts', '#operations': 'operations' };
  const preselect = (hash) => {
    const key = presets[hash];
    if (!key) return;
    const opt = topic.querySelector(`option[data-key="${key}"]`);
    if (opt) { topic.value = opt.value; opt.selected = true; showRoute(); }
  };
  preselect(location.hash);
  window.addEventListener('hashchange', () => preselect(location.hash));
  enquiry.addEventListener('submit', (event) => {
    event.preventDefault();
    const who = enquiry.elements.name.value.trim();
    const text = enquiry.elements.message.value.trim() + (who ? '\n\n' + who : '');
    const subject = encodeURIComponent(topic.selectedOptions[0].text);
    window.location.href = 'mailto:' + addr() + '?subject=' + subject + '&body=' + encodeURIComponent(text);
  });
}

// Site search: matches any word, best matches first, help when results are thin
const search = document.querySelector('#site-search');
if (search) {
  const query = search.elements.q;
  const list = document.querySelector('.results');
  const items = Array.from(list.children);
  const status = document.querySelector('#search-status');
  const help = document.querySelector('#search-help');
  const web = document.querySelector('#web-search');
  const update = () => {
    const terms = query.value.trim().toLowerCase().split(/\s+/).filter(Boolean);
    let count = 0;
    for (const li of items) {
      const text = (li.textContent + ' ' + li.dataset.keywords).toLowerCase();
      const score = terms.filter((t) => text.includes(t)).length;
      li.dataset.score = score;
      li.hidden = terms.length > 0 && score === 0;
      if (!li.hidden) count++;
    }
    items.slice().sort((a, b) => b.dataset.score - a.dataset.score).forEach((li) => list.appendChild(li));
    status.textContent = !terms.length ? 'All pages' : count ? `${count} ${count === 1 ? 'page' : 'pages'} found` : 'No pages found';
    help.hidden = !terms.length || count > 2;
    web.href = 'https://www.google.com/search?q=' + encodeURIComponent('' + query.value.trim());
  };
  query.addEventListener('input', update);
  search.addEventListener('submit', (e) => { e.preventDefault(); update(); });
  document.querySelectorAll('.suggest button').forEach((b) => b.addEventListener('click', () => { query.value = b.textContent; update(); query.focus(); }));
  const q = new URLSearchParams(location.search).get('q');
  if (q) query.value = q;
  update();
}
