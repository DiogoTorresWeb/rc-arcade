/* RC Arcade — camada de rastreio.
   Uma camada só (dataLayer) que alimenta GTM, GA4, Meta Pixel, Clarity e a API de Conversões.
   Regras: (1) nada carrega sem consentimento (Consent Mode v2, tudo negado por padrão);
   (2) sem ID configurado em window.RCA_TRACK, nenhuma ferramenta externa é carregada;
   (3) nenhum dado pessoal (nome, telefone, e-mail) entra em evento, só metadados;
   (4) falha aberta: se este arquivo não carregar, o site funciona igual.
   Como ligar cada ferramenta: runbooks/rastreo.md */
(function () {
  'use strict';
  var CFG = window.RCA_TRACK || {};
  var w = window, d = document;
  var KEY = 'rca_consent_v1';
  w.dataLayer = w.dataLayer || [];
  function gtag() { w.dataLayer.push(arguments); }

  /* ── Consent Mode v2: tudo negado até a pessoa decidir ── */
  gtag('consent', 'default', {
    ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied',
    analytics_storage: 'denied', functionality_storage: 'granted', security_storage: 'granted',
    wait_for_update: 500
  });

  var consent = { analytics: false, marketing: false };
  var loaded = {};

  var HAS_TOOLS = !!(CFG.gtm || CFG.ga4 || CFG.meta || CFG.clarity || CFG.endpoint);
  var MAX_AGE = 730 * 864e5; /* a escolha vence em 24 meses (guia da AEPD) */
  function readConsent() {
    try {
      var c = JSON.parse(localStorage.getItem(KEY));
      if (c && typeof c.a === 'boolean' && c.t && Date.now() - c.t < MAX_AGE) return c;
    } catch (e) {}
    return null;
  }
  function writeConsent(a, m) {
    try { localStorage.setItem(KEY, JSON.stringify({ a: a, m: m, t: Date.now() })); } catch (e) {}
  }

  /* ── utilidades ── */
  var uid = function () { return Math.random().toString(36).slice(2, 10) + Date.now().toString(36); };
  var qs = {};
  try { new URLSearchParams(location.search).forEach(function (v, k) { qs[k] = v; }); } catch (e) {}
  var attrib = {};
  ['utm_source', 'utm_medium', 'utm_campaign', 'utm_content', 'utm_term', 'fbclid', 'gclid', 'ttclid'].forEach(function (k) {
    if (qs[k]) attrib[k] = String(qs[k]).slice(0, 80);
  });
  var cookie = function (n) { var m = d.cookie.match(new RegExp('(?:^|; )' + n + '=([^;]*)')); return m ? decodeURIComponent(m[1]) : ''; };

  /* ── carregadores (só depois do consentimento e só com ID) ── */
  function inject(src, id) {
    if (loaded[id]) return; loaded[id] = 1;
    var s = d.createElement('script'); s.async = true; s.src = src; d.head.appendChild(s);
  }
  function loadTools() {
    var any = consent.analytics || consent.marketing;
    gtag('consent', 'update', {
      analytics_storage: consent.analytics ? 'granted' : 'denied',
      ad_storage: consent.marketing ? 'granted' : 'denied',
      ad_user_data: consent.marketing ? 'granted' : 'denied',
      ad_personalization: consent.marketing ? 'granted' : 'denied'
    });
    if (!any) return;
    if (CFG.gtm) {
      if (!loaded.gtm) {
        loaded.gtm = 1;
        w.dataLayer.push({ 'gtm.start': Date.now(), event: 'gtm.js' });
        inject('https://www.googletagmanager.com/gtm.js?id=' + encodeURIComponent(CFG.gtm), 'gtm-js');
      }
      return; /* com GTM, GA4, Meta e o resto vivem dentro do contêiner */
    }
    if (CFG.ga4 && consent.analytics) {
      inject('https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(CFG.ga4), 'ga4');
      if (!loaded.ga4cfg) { loaded.ga4cfg = 1; gtag('js', new Date()); gtag('config', CFG.ga4, { send_page_view: false }); }
    }
    if (CFG.meta && consent.marketing && !loaded.meta) {
      loaded.meta = 1;
      /* snippet oficial do Meta Pixel */
      (function (f, b, e, v, n, t, s) {
        if (f.fbq) return; n = f.fbq = function () { n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments); };
        if (!f._fbq) f._fbq = n; n.push = n; n.loaded = true; n.version = '2.0'; n.queue = [];
        t = b.createElement(e); t.async = true; t.src = v; s = b.getElementsByTagName(e)[0]; s.parentNode.insertBefore(t, s);
      })(w, d, 'script', 'https://connect.facebook.net/en_US/fbevents.js');
      w.fbq('init', CFG.meta); w.fbq('track', 'PageView');
    }
    if (CFG.clarity && consent.analytics && !loaded.clarity) {
      loaded.clarity = 1;
      (function (c, l, a, r, i, t, y) {
        c[a] = c[a] || function () { (c[a].q = c[a].q || []).push(arguments); };
        t = l.createElement(r); t.async = 1; t.src = 'https://www.clarity.ms/tag/' + i; y = l.getElementsByTagName(r)[0]; y.parentNode.insertBefore(t, y);
      })(w, d, 'clarity', 'script', CFG.clarity);
    }
  }

  /* ── evento: uma chamada alimenta tudo ── */
  var META = { generate_lead: 'Lead', click_whatsapp: 'Contact', click_email: 'Contact', video_play: 'ViewContent' };
  function track(name, params) {
    var id = uid();
    var p = {};
    params = params || {};
    for (var k in params) if (Object.prototype.hasOwnProperty.call(params, k)) p[k] = params[k];
    var payload = { event: name, event_id: id, page_path: location.pathname, page_title: d.title };
    for (var a in p) payload[a] = p[a];
    if (META[name]) payload.meta_event = META[name];
    for (var u in attrib) payload[u] = attrib[u];
    w.dataLayer.push(payload);
    /* sem GTM: GA4 e Meta direto */
    if (!CFG.gtm) {
      if (w.gtag_loaded_ga4 !== false && CFG.ga4 && consent.analytics) gtag('event', name, p);
      if (w.fbq && consent.marketing && META[name]) w.fbq('track', META[name], {}, { eventID: id });
    }
    /* servidor (API de Conversões da Meta, via endpoint do cliente): só com consentimento de marketing */
    if (CFG.endpoint && consent.marketing && META[name] && navigator.sendBeacon) {
      var fbc = cookie('_fbc') || (attrib.fbclid ? 'fb.1.' + Date.now() + '.' + attrib.fbclid : '');
      try {
        navigator.sendBeacon(CFG.endpoint, JSON.stringify({
          event_name: META[name], event_id: id, event_time: Math.floor(Date.now() / 1000),
          event_source_url: location.href, action_source: 'website',
          fbp: cookie('_fbp'), fbc: fbc, params: p
        }));
      } catch (e) {}
    }
  }
  w.rcaTrack = track;
  /* referência curta de campanha para somar à mensagem do WhatsApp (sem dado pessoal) */
  w.rcaTrack.ref = function () {
    var r = [];
    ['utm_source', 'utm_medium', 'utm_campaign'].forEach(function (k) { if (attrib[k]) r.push(attrib[k]); });
    return r.join('/');
  };

  /* ── eventos automáticos ── */
  d.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a,button,[data-track]');
    if (!a) return;
    var t = a.getAttribute('data-track');
    var href = a.getAttribute('href') || '';
    var label = a.getAttribute('data-track-label') || (a.textContent || '').trim().slice(0, 40);
    if (t) track(t, { label: label, section: (a.closest('section,header,footer') || {}).id || '' });
    else if (/wa\.me|api\.whatsapp/.test(href)) track('click_whatsapp', { label: label });
    else if (/^mailto:/.test(href)) track('click_email', { label: label });
    else if (/instagram\.com/.test(href)) track('click_social', { network: 'instagram' });
  }, true);

  var started = false;
  d.addEventListener('focusin', function (e) {
    if (!started && e.target.closest && e.target.closest('#contactForm')) { started = true; track('form_start'); }
  });

  /* profundidade de rolagem */
  var marks = [25, 50, 75, 90], hit = {}, ticking = false;
  function depth() {
    ticking = false;
    var h = d.documentElement.scrollHeight - innerHeight;
    if (h <= 0) return;
    var p = scrollY / h * 100;
    marks.forEach(function (m) { if (p >= m && !hit[m]) { hit[m] = 1; track('scroll_depth', { percent: m }); } });
  }
  addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(depth); } }, { passive: true });

  /* seção vista (uma vez cada) e vídeo */
  if ('IntersectionObserver' in w) {
    var seen = {};
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (en) {
        if (en.isIntersecting && !seen[en.target.id]) { seen[en.target.id] = 1; track('section_view', { section: en.target.id }); }
      });
    }, { threshold: .35 });
    d.querySelectorAll('main section[id]').forEach(function (s) { io.observe(s); });
  }
  var vid = d.querySelector('[data-track-video]');
  if (vid) {
    vid.addEventListener('play', function once() { track('video_play', { label: 'pista' }); vid.removeEventListener('play', once); });
  }

  /* ── faixa de consentimento (aceitar e recusar com o mesmo peso) ── */
  function closeBanner(el) { if (el && el.parentNode) el.parentNode.removeChild(el); d.documentElement.classList.remove('has-cmp'); }
  function wipe() {
    try { if (w.fbq) w.fbq('consent', 'revoke'); } catch (e) {}
    try { if (w.clarity) w.clarity('consent', false); } catch (e) {}
    var host = location.hostname, parts = host.split('.');
    d.cookie.split(';').forEach(function (c) {
      var n = c.split('=')[0].trim();
      if (/^(_ga|_gid|_gat|_fbp|_fbc|_clck|_clsk|CLID|MR|SM)/.test(n)) {
        ['', host, '.' + host, '.' + parts.slice(-2).join('.')].forEach(function (dom) {
          d.cookie = n + '=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/' + (dom ? '; domain=' + dom : '');
        });
      }
    });
  }
  function apply(a, m, el) {
    var downgrade = (consent.analytics && !a) || (consent.marketing && !m);
    consent.analytics = a; consent.marketing = m; writeConsent(a, m);
    if (downgrade) { closeBanner(el); wipe(); location.reload(); return; } /* o que já carregou só some recarregando */
    loadTools(); closeBanner(el);
    track('consent_update', { analytics: a, marketing: m });
  }
  function banner() {
    var el = d.createElement('div');
    el.className = 'cmp'; el.setAttribute('role', 'dialog'); el.setAttribute('aria-label', 'Preferencias de cookies');
    el.innerHTML =
      '<p class="cmp__t"><b>Cookies</b> Usamos cookies propias y de terceros para medir las visitas y mejorar la publicidad. Tú decides.</p>' +
      '<div class="cmp__set" hidden>' +
      '<label><input type="checkbox" checked disabled> Necesarias <span>siempre activas</span></label>' +
      '<label><input type="checkbox" id="cmpA"> Analítica <span>medir visitas y uso</span></label>' +
      '<label><input type="checkbox" id="cmpM"> Marketing <span>medir y mejorar campañas</span></label>' +
      '</div>' +
      '<div class="cmp__b">' +
      '<button type="button" class="btn btn--ghost" data-cmp="no">Rechazar</button>' +
      '<button type="button" class="btn btn--ghost" data-cmp="set">Ajustes</button>' +
      '<button type="button" class="btn btn--ghost" data-cmp="yes">Aceptar todo</button>' +
      '</div>' +
      '<p class="cmp__l"><a href="cookies.html">Política de cookies</a></p>';
    el.addEventListener('click', function (e) {
      var b = e.target.closest('[data-cmp]'); if (!b) return;
      var k = b.getAttribute('data-cmp');
      if (k === 'yes') apply(true, true, el);
      else if (k === 'no') apply(false, false, el);
      else if (k === 'set') {
        var s = el.querySelector('.cmp__set');
        if (s.hidden) { s.hidden = false; b.textContent = 'Guardar'; }
        else apply(el.querySelector('#cmpA').checked, el.querySelector('#cmpM').checked, el);
      }
    });
    d.body.insertBefore(el, d.body.firstChild); /* primeiro item do teclado */
    d.documentElement.classList.add('has-cmp');
  }
  w.rcaConsentOpen = function () { var old = d.querySelector('.cmp'); if (old) closeBanner(old); banner(); };

  /* ── arranque ── */
  var saved = readConsent();
  if (saved) { consent.analytics = saved.a; consent.marketing = saved.m; loadTools(); }
  else {
    /* sem nenhuma ferramenta configurada não há o que consentir: a faixa só aparece quando houver ID (ou em ?cookies=1) */
    var show = function () { if (HAS_TOOLS && !d.querySelector('.cmp')) setTimeout(function () { if (!d.querySelector('.cmp')) banner(); }, 2400); };
    if (d.readyState === 'complete') show(); else addEventListener('load', show);
  }
  d.addEventListener('click', function (e) {
    if (e.target.closest && e.target.closest('[data-cmp-open]')) { e.preventDefault(); w.rcaConsentOpen(); }
  });
  /* vindo das páginas legais (index.html?cookies=1): abre as preferências */
  if (qs.cookies) { var openIt = function () { w.rcaConsentOpen(); }; if (d.readyState === 'complete') openIt(); else addEventListener('load', openIt); }
  w.rcaTrack.hasTools = HAS_TOOLS;
  track('page_view');
})();
