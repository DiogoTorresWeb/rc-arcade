// Filma o carro em 3 cenários (descendo tudo / subindo depois de sair / subindo no meio) e grava quadros + dados.
// Uso: node estudo/carro-43/filmar-carro.mjs [url] [pasta] [pc|celular]
import { createRequire } from 'node:module';
import { readdirSync, mkdirSync, existsSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';

const cache = join(process.env.LOCALAPPDATA || '', 'npm-cache', '_npx');
let pupPath = null;
for (const d of existsSync(cache) ? readdirSync(cache) : []) {
  const p = join(cache, d, 'node_modules', 'puppeteer-core');
  if (existsSync(p)) { pupPath = p; break; }
}
const puppeteer = createRequire(import.meta.url)(pupPath);
const URL_ = process.argv[2] || 'http://localhost:8795/index.html';
const OUT = process.argv[3] || 'estudo/carro-43/_filme';
const TELA = process.argv[4] || 'pc';
mkdirSync(OUT, { recursive: true });
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const dims = TELA === 'pc' ? { width: 1440, height: 900, mobile: false } : { width: 390, height: 844, mobile: true };
const browser = await puppeteer.launch({ executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe', headless: 'new', args: ['--no-sandbox'] });
const page = await browser.newPage();
await page.setViewport({ width: dims.width, height: dims.height, deviceScaleFactor: 1, isMobile: dims.mobile, hasTouch: dims.mobile });
await page.goto(URL_, { waitUntil: 'networkidle2' });
await sleep(2600);
const topo = await page.evaluate(() => { const r = document.getElementById('race').getBoundingClientRect(); return { y: r.top + scrollY, h: r.height }; });
const vh = dims.height;
// r.top = v  <=>  scrollY = topo.y - v
const sy = (rtop) => topo.y - rtop;
const instant = async (y) => { await page.evaluate((v) => window.scrollTo(0, v), y); await sleep(1500); };

async function amostra() {
  return page.evaluate(() => {
    const car = document.querySelector('.race__car'), lane = document.querySelector('.race__lane'), rot = document.querySelector('.race__rot');
    const r = car.getBoundingClientRect();
    return { t: Math.round(performance.now()), estado: lane.getAttribute('data-state'), rot: rot.style.getPropertyValue('--rot') || '0', carTop: Math.round(r.top), carBot: Math.round(r.bottom), carH: Math.round(r.height), vis: r.bottom > 0 && r.top < innerHeight };
  });
}

async function cena(nome, deY, paraY, passo, intervaloMs, extra = 1800) {
  await instant(deY);
  const dados = [];
  const dir = paraY > deY ? 1 : -1;
  let y = deY, n = 0;
  const t0 = Date.now();
  while ((dir > 0 && y < paraY) || (dir < 0 && y > paraY)) {
    y += dir * passo;
    await page.evaluate((v) => window.scrollTo(0, v), y);
    await sleep(intervaloMs);
    if (n % 2 === 0) { const a = await amostra(); a.scroll = Math.round(y); dados.push(a); await page.screenshot({ path: join(OUT, `${TELA}-${nome}-${String(dados.length).padStart(3, '0')}.png`) }); }
    n++;
  }
  // depois de parar: o carro termina o que estava fazendo
  for (let i = 0; i < 6; i++) { await sleep(extra / 6); const a = await amostra(); a.scroll = Math.round(y); a.parado = true; dados.push(a); await page.screenshot({ path: join(OUT, `${TELA}-${nome}-${String(dados.length).padStart(3, '0')}.png`) }); }
  writeFileSync(join(OUT, `${TELA}-${nome}.json`), JSON.stringify(dados, null, 1));
  console.log(nome, dados.length, 'quadros em', Date.now() - t0, 'ms');
}

await cena('A-descendo', sy(vh * 1.0), sy(-(topo.h - vh * 0.2)), 30, 16);
await cena('B-subindo-depois-de-sair', sy(-(topo.h - vh * 0.5)), sy(vh * 0.95), 30, 16);
await cena('C-subindo-no-meio', sy(-vh * 0.2), sy(vh * 0.95), 30, 16);
await browser.close();
