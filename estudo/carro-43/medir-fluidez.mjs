// Mede a fluidez ao rolar pela seção do carro: intervalos entre quadros (rAF) com CPU 4x mais lenta (celular fraco).
// Sem GPU real no robô os números são pessimistas; serve para comparar antes e depois. Uso: node estudo/carro-43/medir-fluidez.mjs [url] [pc|celular] [lento]
import { createRequire } from 'node:module';
import { readdirSync, existsSync } from 'node:fs';
import { join } from 'node:path';
const cache = join(process.env.LOCALAPPDATA || '', 'npm-cache', '_npx');
let pupPath = null;
for (const d of existsSync(cache) ? readdirSync(cache) : []) { const p = join(cache, d, 'node_modules', 'puppeteer-core'); if (existsSync(p)) { pupPath = p; break; } }
const puppeteer = createRequire(import.meta.url)(pupPath);
const URL_ = process.argv[2] || 'http://localhost:8795/index.html';
const TELA = process.argv[3] || 'pc';
const LENTO = process.argv[4] === 'lento' ? 4 : 1;
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const dims = TELA === 'pc' ? { width: 1440, height: 900, mobile: false } : { width: 390, height: 844, mobile: true };
const browser = await puppeteer.launch({ executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe', headless: 'new', args: ['--no-sandbox'] });
const page = await browser.newPage();
await page.setViewport({ width: dims.width, height: dims.height, deviceScaleFactor: dims.mobile ? 2 : 1, isMobile: dims.mobile, hasTouch: dims.mobile });
const cdp = await page.createCDPSession();
await page.goto(URL_, { waitUntil: 'networkidle2' });
await sleep(2600);
if (LENTO > 1) await cdp.send('Emulation.setCPUThrottlingRate', { rate: LENTO });
const topo = await page.evaluate(() => { const r = document.getElementById('race').getBoundingClientRect(); return { y: r.top + scrollY, h: r.height }; });
await page.evaluate((v) => window.scrollTo(0, v), topo.y - dims.height * 1.1); await sleep(1500);
await page.evaluate(() => {
  window.__d = []; window.__lt = []; let t = performance.now();
  window.__big = []; const f = (n) => { window.__d.push(n - t); if (n - t > 33.4) window.__big.push({ ms: Math.round(n - t), y: Math.round(scrollY), estado: document.querySelector('.race__lane').dataset.state }); t = n; window.__on && requestAnimationFrame(f); };
  window.__on = true; requestAnimationFrame(f);
  try { new PerformanceObserver((l) => l.getEntries().forEach((e) => window.__lt.push(Math.round(e.duration)))).observe({ entryTypes: ['longtask'] }); } catch (e) {}
});
const fim = topo.y + topo.h - dims.height * 0.5;
for (let y = topo.y - dims.height * 1.1; y < fim; y += 30) { await page.evaluate((v) => window.scrollTo(0, v), y); await sleep(16); }
for (let y = fim; y > topo.y - dims.height * 1.1; y -= 30) { await page.evaluate((v) => window.scrollTo(0, v), y); await sleep(16); }
const r = await page.evaluate(() => { window.__on = false; const d = window.__d.slice(5).sort((a, b) => a - b); const q = (p) => d[Math.floor(d.length * p)]; return { quadros: d.length, mediana: +q(.5).toFixed(1), p95: +q(.95).toFixed(1), p99: +q(.99).toFixed(1), max: +d[d.length - 1].toFixed(1), acima33ms: d.filter((x) => x > 33.4).length, acima50ms: d.filter((x) => x > 50).length, longTasks: window.__lt.length, ltMax: Math.max(0, ...window.__lt), engasgos: window.__big }; });
console.log(TELA, LENTO > 1 ? 'CPU 4x' : 'CPU normal', JSON.stringify(r));
await browser.close();
