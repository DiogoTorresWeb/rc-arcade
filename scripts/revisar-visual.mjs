// Auto-revisão do site: abre num Chrome de verdade, rola tudo, fotografa cada seção e acusa problema.
// Uso (da pasta do projeto, com o servidor local no ar):
//   node scripts/revisar-visual.mjs [url] [pasta-de-saida]
// Padrão: http://localhost:8791/index.html  e  runbooks/revisao-visual/
// Usa o puppeteer-core que vem junto do Lighthouse (npx lighthouse instala). Ver runbooks/medir-e-revisar.md
import { createRequire } from 'node:module';
import { readdirSync, mkdirSync, writeFileSync, existsSync } from 'node:fs';
import { join } from 'node:path';

const cache = join(process.env.LOCALAPPDATA || '', 'npm-cache', '_npx');
let pupPath = null;
for (const d of existsSync(cache) ? readdirSync(cache) : []) {
  const p = join(cache, d, 'node_modules', 'puppeteer-core');
  if (existsSync(p)) { pupPath = p; break; }
}
if (!pupPath) { console.error('puppeteer-core não encontrado: rode "npx --yes lighthouse --version" uma vez.'); process.exit(1); }
const puppeteer = createRequire(import.meta.url)(pupPath);

const URL_ = process.argv[2] || 'http://localhost:8791/index.html';
const OUT = process.argv[3] || 'runbooks/revisao-visual';
const CHROME = process.env.CHROME_PATH || 'C:/Program Files/Google/Chrome/Application/chrome.exe';
mkdirSync(OUT, { recursive: true });

const telas = [
  { nome: 'pc', width: 1440, height: 900, mobile: false },
  { nome: 'celular', width: 390, height: 844, mobile: true },
];
const relatorio = [];
const browser = await puppeteer.launch({ executablePath: CHROME, headless: 'new', args: ['--no-sandbox'] });

for (const t of telas) {
  const page = await browser.newPage();
  await page.setViewport({ width: t.width, height: t.height, deviceScaleFactor: 1, isMobile: t.mobile, hasTouch: t.mobile });
  const erros = [], falhas = [];
  page.on('pageerror', e => erros.push('JS: ' + e.message));
  page.on('console', m => { if (m.type() === 'error') erros.push('console: ' + m.text()); });
  page.on('response', r => { if (r.status() >= 400) falhas.push(r.status() + ' ' + r.url()); });
  await page.evaluateOnNewDocument(() => {
    try { sessionStorage.setItem('rca_intro_v1', '1'); localStorage.setItem('rca_consent_v1', JSON.stringify({ a: false, m: false, t: 1 })); } catch (e) {}
  });
  await page.goto(URL_, { waitUntil: 'networkidle2' });
  // rola devagar (para o lazy-load e os observadores agirem)
  const altura = await page.evaluate(() => document.documentElement.scrollHeight);
  for (let y = 0; y < altura; y += Math.round(t.height * 0.5)) {
    await page.evaluate(yy => window.scrollTo(0, yy), y);
    await new Promise(r => setTimeout(r, 140));
  }
  await new Promise(r => setTimeout(r, 800));

  const secoes = await page.evaluate(() => [...document.querySelectorAll('main > section, footer')].map(s => ({ id: s.id || s.tagName.toLowerCase(), top: s.getBoundingClientRect().top + scrollY, h: s.offsetHeight })));
  const dados = await page.evaluate(() => ({
    scrollLateral: document.documentElement.scrollWidth > innerWidth + 1,
    imagensQuebradas: [...document.images].filter(i => i.complete && i.naturalWidth === 0).map(i => i.currentSrc || i.src),
    h1: [...document.querySelectorAll('h1')].length,
    linksInternosQuebrados: [...document.querySelectorAll('a[href^="#"]')].map(a => a.getAttribute('href')).filter(h => h.length > 1 && !document.querySelector(h)),
    semAlt: [...document.images].filter(i => !i.hasAttribute('alt')).length,
    titulo: document.title,
    pesoImagens: performance.getEntriesByType('resource').filter(r => r.initiatorType === 'img' || /\.(webp|jpg|png|avif)/.test(r.name)).reduce((a, r) => a + (r.encodedBodySize || 0), 0),
  }));
  // estado dos observadores
  await page.evaluate(() => window.scrollTo(0, document.getElementById('prueba').offsetTop + 60));
  await new Promise(r => setTimeout(r, 1500));
  const video = await page.evaluate(() => { const v = document.getElementById('proofVideo'); return v ? { tocando: !v.paused, tempo: +v.currentTime.toFixed(1) } : null; });
  await page.evaluate(() => window.scrollTo(0, document.getElementById('que-es').offsetTop + 200));
  await new Promise(r => setTimeout(r, 900));
  const acesos = await page.evaluate(() => document.querySelectorAll('.is-lit').length);

  // fotos por seção
  for (const s of secoes) {
    await page.evaluate(yy => window.scrollTo(0, yy), Math.max(0, s.top - 40));
    await new Promise(r => setTimeout(r, 700));
    await page.screenshot({ path: join(OUT, `${t.nome}-${s.id}.png`) });
  }
  // faixa de cookies
  await page.close();
  // faixa de cookies: página nova, sem consentimento guardado
  const p2 = await browser.newPage();
  await p2.setViewport({ width: t.width, height: t.height, deviceScaleFactor: 1, isMobile: t.mobile, hasTouch: t.mobile });
  await p2.evaluateOnNewDocument(() => { try { sessionStorage.setItem('rca_intro_v1', '1'); localStorage.removeItem('rca_consent_v1'); } catch (e) {} });
  await p2.goto(URL_ + (URL_.includes('?') ? '&' : '?') + 'cookies=1', { waitUntil: 'networkidle2' });
  await new Promise(r => setTimeout(r, 3300));
  await p2.screenshot({ path: join(OUT, `${t.nome}-cookies.png`) });
  const faixa = await p2.evaluate(() => {
    const b = [...document.querySelectorAll('.cmp [data-cmp]')].map(x => { const r = x.getBoundingClientRect(); return [x.textContent, Math.round(r.width), Math.round(r.height), getComputedStyle(x).backgroundColor]; });
    return { aparece: !!document.querySelector('.cmp'), botoes: b, primeiroDoTeclado: !!(document.body.firstElementChild && document.body.firstElementChild.classList.contains('cmp')) };
  });
  await p2.close();

  relatorio.push({ tela: t.nome, altura, secoes: secoes.length, erros, falhas, ...dados, video, itensAcesos: acesos, faixaCookies: faixa });
}
await browser.close();
writeFileSync(join(OUT, 'relatorio.json'), JSON.stringify(relatorio, null, 2));
console.log(JSON.stringify(relatorio, null, 2));
