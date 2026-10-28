# Medir e revisar o site sozinho

> Tipo: **runbook** — 28/10/2026. Ferramentas open source: **Lighthouse** (nota do Google) e um robô de revisão visual que usa o Chrome de verdade.

Pré-requisito: o servidor local do projeto no ar (`.claude/launch.json`, porta 8791) e o Chrome instalado.

## 1. Nota do Google (PageSpeed / Lighthouse)
```bash
export CHROME_PATH="C:/Program Files/Google/Chrome/Application/chrome.exe"
npx --yes lighthouse http://localhost:8791/index.html --only-categories=performance,accessibility,best-practices,seo --output=json --output-path=nota.json --chrome-flags="--headless=new --no-sandbox"
```
**Rodar sozinho:** com outra coisa pesada no computador a nota sai errada (aconteceu em 28/10). O servidor local não comprime
arquivos como o GitHub Pages; a nota real vem do endereço público (pagespeed.web.dev).

## 2. Robô de revisão visual
```bash
node scripts/revisar-visual.mjs http://localhost:8791/index.html runbooks/revisao-visual
```
Abre o site em tela de **PC (1440)** e **celular (390)**, rola tudo, fotografa cada seção e a faixa de cookies, e acusa:
erro de JavaScript, arquivo que não carrega (404), imagem quebrada, link interno quebrado, rolagem lateral, vídeo que não toca e
itens que não acendem. Relatório em `runbooks/revisao-visual/relatorio.json`; as fotos (`*.png`) não vão ao git.

## 3. Quando usar
Depois de cada mudança de seção: robô primeiro (acha o quebrado), Lighthouse depois (confere a nota), e olhar as fotos.
Meta: **desempenho ≥ 90 no celular, acessibilidade, boas práticas e SEO em 100**.

## Resultado de 28/10/2026 (site V3, servidor local)
Celular: desempenho 97 · acessibilidade 100 · boas práticas 100 · SEO 100 · LCP 1,5 s · 789 KB. PC: 99 · 100 · 100 · 100 · LCP 0,4 s. Linha de base antes das mudanças: 97/100/100/100, 603 KB.
