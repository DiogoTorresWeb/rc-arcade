// O que torna o carro do Nick Ho fluido? Lê: opções do Lenis (captura do construtor), código dos gatilhos do carro,
// CSS do carro e do contêiner sticky, ticker do GSAP. Só lê; não altera nada no site deles.
import { launch, sleep, URL_SITE, OUT } from './lib.mjs';
import fs from 'node:fs';
const { browser, page } = await launch(false);
await page.evaluateOnNewDocument(() => {
  window.__lenisOpts = [];
  let L;
  Object.defineProperty(window, 'Lenis', {
    configurable: true,
    get() { return L; },
    set(v) {
      L = function (...a) { try { window.__lenisOpts.push(JSON.parse(JSON.stringify(a[0] || {}, (k, x) => typeof x === 'function' ? 'fn:' + x.toString().slice(0, 140) : x))); } catch (e) { window.__lenisOpts.push('erro'); } return new v(...a); };
      L.prototype = v.prototype; Object.assign(L, v);
    },
  });
});
await page.goto(URL_SITE, { waitUntil: 'load', timeout: 60000 });
await sleep(7000);
const total = await page.evaluate(() => document.documentElement.scrollHeight);
let y = 0; while (y < total) { y += 400; await page.evaluate((v) => window.scrollTo(0, v), y); await sleep(250); }
await page.evaluate(() => window.scrollTo(0, 0)); await sleep(1200);
const r = await page.evaluate(() => {
  const out = {};
  out.lenisOpts = window.__lenisOpts;
  out.lenisInstance = (() => { const l = window.lenis || window.__lenis; return l ? { lerp: l.options?.lerp, duration: l.options?.duration, smoothWheel: l.options?.smoothWheel, syncTouch: l.options?.syncTouch, wheelMultiplier: l.options?.wheelMultiplier } : null; })();
  out.gsap = { version: gsap.version, lagSmoothing: (() => { try { return gsap.ticker.lagSmoothing ? 'fn' : 'n/a'; } catch (e) { return 'erro'; } })(), normalize: !!ScrollTrigger.isTouch };
  const sec = document.getElementById('calendar');
  const sticky = sec.querySelector('.agenda_sticky');
  const car = sticky.querySelector('img, picture img, div[class*=car], [class*=car]');
  const css = (el, props) => { if (!el) return null; const c = getComputedStyle(el); const o = {}; props.forEach((p) => o[p] = c[p]); o.cls = el.className?.toString?.().slice(0, 80); o.tag = el.tagName; const r = el.getBoundingClientRect(); o.rect = [Math.round(r.left), Math.round(r.top + scrollY), Math.round(r.width), Math.round(r.height)]; return o; };
  const props = ['position', 'top', 'transform', 'willChange', 'transition', 'filter', 'backfaceVisibility', 'contain', 'zIndex', 'overflow', 'objectFit', 'imageRendering', 'pointerEvents'];
  out.sticky = css(sticky, props);
  out.stickyChain = []; for (let e = sticky; e && e !== document.body; e = e.parentElement) out.stickyChain.push(css(e, ['position', 'transform', 'willChange', 'overflow', 'height']));
  out.kids = [...sticky.querySelectorAll('*')].slice(0, 12).map((e) => css(e, props));
  out.car = css(car, props);
  // gatilhos da seção
  out.triggers = ScrollTrigger.getAll().filter((st) => st.trigger && (st.trigger === sec || sec.contains(st.trigger)) && !(st.trigger.className || '').toString().includes('agenda_item')).map((st) => ({
    trig: (st.trigger.className || '').toString().slice(0, 50) + (st.trigger.id ? '#' + st.trigger.id : ''), start: String(st.vars.start), end: String(st.vars.end), scrub: st.vars.scrub, markers: !!st.vars.markers,
    onEnter: st.vars.onEnter ? st.vars.onEnter.toString().slice(0, 700) : null, onLeave: st.vars.onLeave ? st.vars.onLeave.toString().slice(0, 700) : null,
    onEnterBack: st.vars.onEnterBack ? st.vars.onEnterBack.toString().slice(0, 700) : null, onLeaveBack: st.vars.onLeaveBack ? st.vars.onLeaveBack.toString().slice(0, 700) : null, onToggle: st.vars.onToggle ? st.vars.onToggle.toString().slice(0, 500) : null,
    anim: st.animation ? { type: st.animation.constructor.name, dur: st.animation.duration(), vars: JSON.stringify(st.animation.vars || {}, (k, v) => typeof v === 'function' ? 'fn' : v).slice(0, 400), kids: (st.animation.getChildren ? st.animation.getChildren(false, true, false) : []).slice(0, 4).map((t) => JSON.stringify(t.vars, (k, v) => typeof v === 'function' ? 'fn' : (v instanceof Element ? 'el' : v)).slice(0, 300)) } : null,
  }));
  // carro: tweens ativos sobre ele
  out.tweens = (car ? gsap.getTweensOf(car).concat(gsap.getTweensOf(sticky), gsap.getTweensOf(car.parentElement)) : []).slice(0, 8).map((t) => ({ dur: t.duration(), vars: JSON.stringify(t.vars, (k, v) => typeof v === 'function' ? 'fn' : (v instanceof Element ? 'el' : v)).slice(0, 300) }));
  out.scripts = [...document.scripts].map((s) => s.src || ('inline:' + s.textContent.length)).filter((s) => !/gtag|google|facebook|clarity|hotjar/.test(s));
  return out;
});
fs.writeFileSync(`${OUT}/carro-fluidez.json`, JSON.stringify(r, null, 1));
console.log(JSON.stringify(r.lenisOpts), JSON.stringify(r.lenisInstance), JSON.stringify(r.gsap));
console.log('STICKY', JSON.stringify(r.sticky));
console.log('CAR', JSON.stringify(r.car));
for (const t of r.triggers) console.log('TRIG', JSON.stringify(t));
console.log('TWEENS', JSON.stringify(r.tweens));
await browser.close();
