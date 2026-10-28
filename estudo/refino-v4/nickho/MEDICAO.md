# Medição do site nickho-motorsports.nl (28/10/2026)

Como: Chrome real (modo headless) controlado por puppeteer-core 25; desktop 1440x810 e celular 390x844 (DPR 2, toque,
user agent de iPhone). Rolagem com `window.scrollTo` em passos de 150-400 px, 350-700 ms de espera. Nada do projeto alterado.
Scripts `01` a `23` e dados `.json` nesta pasta. **MEDI** = lido no navegador. **INFERI** = conclusão minha.
Stack lida (MEDI): Webflow + GSAP 3.15 (ScrollTrigger, SplitText) + Lenis + Swiper 12 + three.js r128 + hls.js 1.6.11.

## 1. Seção "Media & Articles" (y ≈ 5631 px)

**A premissa confere no desktop: foto P&B que ganha cor ao passar o mouse.**
MEDI, mecanismo (só CSS; sem JS, sem blend, sem canvas, sem duas imagens):
- Cada cartão tem uma `<img>` (4:3, `object-fit: cover`, cantos arredondados, `loading="lazy"`).
- Normal: filtro `saturate(0)`. Hover: `saturate(1)` mais zoom `scale(1.04)`, só sob `(hover: hover) and (pointer: fine)`.
- Cor: **0,4 s**, curva `cubic-bezier(.25,.1,.25,1)` (ease). Zoom na entrada **0,6 s** `cubic-bezier(.22,1,.36,1)`; na saída 0,4 s.
- Quadro a quadro: saturação 0,14, 0,41, 0,65, 1 em ~0,4 s; escala 1,01 a 1,04. Nenhuma animação GSAP na imagem.

Celular (MEDI):
- Largura ≤ 479 px: regra `filter: none`, **as fotos já nascem coloridas**; nada acontece ao tocar nem ao entrar na tela.
- Tablet com toque (768 px, testado): sem hover, as fotos ficam **presas em P&B** (INFERI: falha deles, não cobriram 480-1023 px).

Carrossel (MEDI): Swiper, 5 cartões, espaço 16 px. Desktop: 3 por vez, **1200 ms**, curva `cubic-bezier(.16,1,.3,1)`
(sai rápido, pousa devagar), `touchRatio` 0,8, sem loop; botões «‹‹ ››» no canto. Celular: 1 cartão + ponta do próximo, 300 ms.
Legenda cinza (50% de opacidade), 2 linhas.

Título gigante ao fundo (MEDI): `<svg>` com letras já em contornos (1392x743 px), absoluto, `pointer-events: none`, cinza quase
branco, escala vertical ~0,97 e deslocamento em y amarrados à rolagem, com gradiente por cima. Mesma técnica em "GALLERY".
No celular não apareceu na captura (não medi o motivo).

Peso (MEDI, cabeçalho HTTP): 5 imagens **AVIF**: 673x383 = 24 KB; 1920x1280 = 214 KB; 676x391 = 31 KB; 1024x682 = 35 KB;
680x453 = 22 KB. Soma ≈ 326 KB. Uma foto é grande demais (1920 px para mostrar 416 px).
Capturas: `media-d-1-antes.png`, `media-d-2-hover.png`, `media-d-3-sai.png`, `media-m-1-antes.png`.

## 2. Vídeo em tela cheia

**Não existe "abrir o vídeo": sem lightbox, sem fullscreen API, sem botão de play.** (MEDI)
- "Abre" por rolagem: a caixa de `section_video` (y ≈ 8116) **cresce** de 1008x567 (70% da largura) para 1440x810, raio de
  borda indo a 0, entre "topo da seção a 80% da janela" e "topo da seção no topo". Celular: 324x702 (83%) para 390x844.
  Capturas: `video-d-scroll-2/6/10.png`, `video-m-scroll-2/6/10.png`.
- Desktop: o cursor vira uma etiqueta amarela **"SOUND ON"** que segue o mouse (`video-d-2-hover-cursor.png`). O clique alterna
  o som ("SOUND OFF", `muted` false); novo clique silencia de novo (3 cliques testados). Há mais 2 etiquetas no HTML
  ("DRAG", "SEE MORE"); só "SOUND ON" aparece sobre o vídeo.
- Teclado: Espaço, M, K, Enter, Esc, F não mudaram `paused`, `muted` nem `fullscreenElement`. Sem controles nativos.
- Celular: o elemento do som tem `display: none`; **tocar não liga o som** (testado). Vídeo mudo, em loop, sem controle.
- Origem: Bunny Stream (`b-cdn.net`), HLS via hls.js. Playlist com 2 níveis H.264 + AAC: 720p (média 2,96 Mbps) e 1080p
  (média 5,50 Mbps). **21,5 s**, loop, mudo, `playsinline`, `preload="auto"`. Capa JPG 1920x1080 de **817 KB**.
- **Carrega desde a abertura da página**, sem esperar rolagem nem clique (`data-player-lazy=false`). Toca ao entrar na tela;
  no celular pausou ~2,5 telas depois da seção; no desktop não medi quando pausa.

Peso (MEDI, 1 rodada por condição, sem estrangulamento; bytes transferidos via CDP):

| Situação | Desktop | Celular 390 |
|---|---|---|
| Ao sair da tela de abertura, sem rolar | 10,1 MB (vídeo 9,0) | 10,3 MB (vídeo 9,2) |
| Depois de rolar tudo | 21,8 MB (b-cdn 18,4) | 17,6 MB (b-cdn 14,5) |
| Com `b-cdn.net` bloqueado (sem vídeo) | 1,1 MB / 3,4 MB após rolar | 1,0 MB / 3,1 MB |

- O vídeo é ~83% do peso. O clique custou quase nada: a subida de 720p para 1080p ocorreu também no celular sem clique
  (INFERI: adaptação automática do hls.js; no desktop o clique coincidiu, +5,5 MB).

## 3. Efeitos de entrada ao rolar

MEDI: `ScrollTrigger.getAll()` = **97 gatilhos no desktop, 113 no celular**. Desktop: 46 amarrados à rolagem (scrub) e 51 de
disparo ao entrar (`start` ≈ topo a 85% da janela, toca uma vez); 30 desses 51 são só as linhas do calendário.

**Os 5 mais visíveis:**
1. **Caixa do vídeo crescendo até a tela cheia** (scrub de largura, altura, raio). Ver seção 2.
2. **Herói em camadas:** canvas WebGL 1440x810 (three.js) com 3 imagens de profundidade (fundo, carro, piloto) mais
   `hero_image-wrapper`; cada uma sobe em velocidade diferente (`yPercent` scrub). Mouse movendo as camadas: não medi.
3. **Revelação por máscara de linha/palavra:** títulos, citação, história e calendário sobem de dentro de `overflow: clip`
   (SplitText em linhas e palavras).
4. **Fotos com paralaxe em moldura:** imagem com 120% da altura da moldura deslizando (`yPercent` scrub); 9 na história,
   2 ao redor da citação, 1 carro no calendário sticky.
5. **Títulos gigantes em SVG** ("MEDIA & ARTICLES", "GALLERY") com escala e posição amarradas à rolagem.

Outros (MEDI): 18 gatilhos de **linhas de grade verticais** que crescem em altura; capacete 3D em canvas 544x408 na parede de
patrocinadores (`scale` scrub); história em 5 passos (contador "1/5", botão "SKIP") com troca por fade; botão amarelo
"DOWNLOAD SPONSORGUIDE" cujas letras invertem de cor conforme o fundo; rolagem suave Lenis.

**Frase que muda de cor palavra por palavra: NÃO encontrei** (MEDI). Varredura de 1.570 elementos a cada 150 px de rolagem: a
citação "I'm driven by progress..." tem 3 trechos amarelos fixos e entra só por revelação de linhas. As únicas trocas de cor
com a rolagem são do botão e do cabeçalho. Se você viu o efeito, foi em outro site.

**Contadores (MEDI, no carregamento, não na rolagem):** a abertura mostra o "98" em SVG gigante que vira transição. As
estatísticas do herói (17, 14, 10+, 21) são **odômetro**: cada dígito é uma coluna 0-9 em máscara que desliza em Y
(de ~3 s a ~7 s após o início da navegação) e é trocada por dígito fixo.

Capturas: `scroll-d-1-frase-cor.png` (citação; nome enganoso, a cor é fixa), `scroll-d-2-paralaxe.png` (patrocinadores e
capacete), `scroll-d-3-agenda-entrando.png` (calendário). Celular: `scroll-m-*`.

## 4. Peso total e primeiro conteúdo (MEDI, 1 rodada cada, headless, sem GPU real)

| | Desktop | Celular 390 | Celular, 4G lento* |
|---|---|---|---|
| FCP (primeiro conteúdo) | 0,5 s | 0,5 s | 0,4 s |
| Evento `load` | 1,8 s | 1,8 s | não disparou antes de a abertura sumir (5,9 s sem vídeo) |
| Tela de abertura some | ~3,0 s | ~2,9 s | 8,7 s (6,7 s sem vídeo) |
| LCP | 4,8 s | n/c** | 10,7 s (8,7 s sem vídeo) |
| JavaScript | 0,69 MB, 53 arquivos | idem | idem |

\* 1,6 Mbps, 150 ms. \*\* LCP variou de 0,5 a 1,7 s entre rodadas; não confio.
O primeiro pixel é rápido, mas o conteúdo útil fica atrás de uma abertura de ~3 s, por escolha de design.

## 5. O que NÃO consegui medir
- Aparelho real (iOS/Android; o toque foi emulado) e desempenho de quadros (WebGL sem GPU real).
- Mouse no herói; arrasto e botões do carrossel (só li os parâmetros do Swiper); quando o vídeo pausa no desktop.
- Se a abertura espera o vídeo (no 4G demorou ~2 s a mais com vídeo, mas é 1 rodada). Os tempos variam centenas de ms
  entre execuções (TTFB oscilou de 0,1 a 1,0 s).
- Nada de código ou texto do site foi copiado; só descrevi mecanismos.

## 6. Para o RC Arcade (INFERI, decisão sua)
- P&B para cor no hover é CSS puro (~0 KB). Exigir `(hover: hover)` sem deixar tablet de toque preso em P&B.
- O vídeo deles é ~83% do peso e carrega antes de ser visto: usar `preload="none"`, capa leve, 720p, e som por botão visível.
- "Caixa que cresce até a tela cheia" entrega o efeito sem lightbox nem fullscreen.
