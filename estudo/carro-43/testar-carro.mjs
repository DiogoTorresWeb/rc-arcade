// Teste do carro que desce: rola a seção "Cómo trabajamos" em passos, fotografa o estado e registra data-state / linhas acesas.
// Uso (da pasta do projeto, com o servidor local no ar): node estudo/carro-43/testar-carro.mjs [url] [pasta]
import { createRequire } from 'node:module';
import { readdirSync, mkdirSync, existsSync } from 'node:fs';
import { join } from 'node:path';

const cache = join(process.env.LOCALAPPDATA || '', 'npm-cache', '_npx');
let pupPath = null;
for (const d of existsSync(cache) ? readdirSync(cache) : []) {
  const p = join(cache, d, 'node_modules', 'puppeteer-core');
  if (existsSync(p)) { pupPath = p; break; }
}
if (!pupPath) { console.error('puppeteer-core não encontrado'); process.exit(1); }
const puppeteer = createRequire(import.meta.url)(pupPath);
const URL_ = process.argv[2] || 'http://localhost:8795/index.html';
const OUT = process.argv[3] || 'estudo/carro-43/_teste';
mkdirSync(OUT, { recursive: true });
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const browser = await puppeteer.launch({ executablePath: 'C:/Program Files/Google/Chrome/Application/chrome.exe', headless: 'new', args: ['--no-sandbox'] });

for (const tela of [{ nome: 'pc', width: 1440, height: 900, mobile: false }, { nome: 'celular', width: 390, height: 844, mobile: true }]) {
  const page = await browser.newPage();
  await page.setViewport({ width: tela.width, height: tela.height, deviceScaleFactor: 1, isMobile: tela.mobile, hasTouch: tela.mobile });
  const erros = [];
  page.on('pageerror', (e) => erros.push(String(e)));
  page.on('console', (m) => { if (m.type() === 'error') erros.push(m.text()); });
  await page.goto(URL_, { waitUntil: 'networkidle2' });
  await sleep(2600); // cortina de entrada
  const topo = await page.evaluate(() => { const r = document.getElementById('race').getBoundingClientRect(); return { y: r.top + scrollY, h: r.height }; });
  console.log(tela.nome, 'race topo', Math.round(topo.y), 'altura', Math.round(topo.h));
  // pontos: antes, começo, meio, fim, depois
  // r.top relativo ao topo da janela: 450 = começa; o carro fica preso até r.bottom = altura da janela
  const rt = (v) => topo.y - v;
  const pontos = [
    ['0-antes', rt(tela.height * 0.95)],
    ['1-comeco', rt(tela.height * 0.45)],
    ['2-meio', rt(0)],
    ['3-meio2', rt(-tela.height * 0.55)],
    ['4-saindo', rt(-(topo.h - tela.height * 1.2))],
    ['5-depois', rt(-(topo.h - tela.height * 0.5))],
  ];
  for (const [nome, y] of pontos) {
    // rola em passos para o gatilho disparar como na vida real
    const atual = await page.evaluate(() => scrollY);
    const passos = 8;
    for (let i = 1; i <= passos; i++) { await page.evaluate((v) => window.scrollTo(0, v), atual + ((y - atual) * i) / passos); await sleep(40); }
    await sleep(1100);
    const info = await page.evaluate(() => ({
      estado: document.querySelector('.race__lane').getAttribute('data-state'),
      rot: document.querySelector('.race__rot').style.getPropertyValue('--rot'),
      acesas: [...document.querySelectorAll('.race .process__row')].map((r) => r.classList.contains('is-lit') ? 1 : 0).join(''),
      carro: (() => { const i = document.querySelector('.race__car'); return { ok: i.complete && i.naturalWidth > 0, w: i.naturalWidth }; })(),
      scrollX: document.documentElement.scrollWidth - innerWidth,
    }));
    console.log(tela.nome, nome, JSON.stringify(info));
    await page.screenshot({ path: join(OUT, `${tela.nome}-${nome}.png`) });
  }
  console.log(tela.nome, 'erros:', erros.length ? erros : 'nenhum');
  await page.close();
}
await browser.close();
