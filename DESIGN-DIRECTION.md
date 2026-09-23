# Direção de design — RC Arcade

Escrito em 13/09/2026, a partir do material do cliente e da conversa com o
Diogo sobre "futurista, mas com conversão".

## Tokens reais, extraídos do dossiê (não chutados)

Amostrados por análise de pixel das páginas do PDF do cliente — o vermelho é
idêntico no logo (p.17) e nos acentos de seção (p.6), então é o valor de marca
de verdade.

| Token | Valor | Papel (palavras do cliente) |
|---|---|---|
| `--rc-red` | **#E31B23** | Energia e competição. Acento, nunca fundo de área grande. |
| `--rc-black` | **#0A0B0D** | Fundo profundo da página. |
| `--rc-surface` | **#191A1E** | Superfície de card/seção — é o cinza-preto dominante do dossiê. |
| `--rc-silver` | **#B1B0AB** | Precisão e caráter mecânico. Texto secundário, réguas, detalhe. |
| `--rc-silver-dim` | **#8B8D8C** | Texto terciário, legendas. |
| branco | #FFFFFF | Texto principal. |

Escala e tipografia ficam pra Etapa 3 (Claude Design). O que está travado aqui
é a paleta, porque ela veio do cliente e não é negociável.

## A pergunta do "futurismo" — e a resposta

O Diogo trouxe como referência sites com narrativa contínua em scroll (o
exemplo dele: uma barbearia onde a câmera vai da rua até dentro da loja). Ele
mesmo já apontou o problema: esses sites costumam converter mal.

**A resposta pro RC Arcade é melhor do que copiar esse padrão.**

Esses sites usam movimento porque o produto deles é parado — uma loja, um
imóvel. Precisam inventar movimento pra criar sensação. **O RC Arcade não
precisa inventar nada: o produto dele É uma câmera em movimento.** A imagem
FPV real, gravada do carro, é mais impressionante que qualquer transição
animada — e já existe, já está filmada, e já temos permissão de usar.

Então a regra é:

> **O movimento do site é o movimento do produto. Nada de movimento decorativo
> por cima de conteúdo parado.**

Isso entrega a sensação de futuro que o Diogo quer, sem pagar o preço de
conversão, porque o movimento não está atrasando a informação — ele É a
informação.

## A segunda camada: a linguagem de HUD

No vídeo da sessão real aparece um overlay de telemetria na tela do piloto:
voltagem (12.3v), taxa de transmissão (25Mbps), latência em ms, barras de
sinal. E no dossiê (p.10) aparece o cronômetro: `00:42.381`, voltas, posição,
diferença `+0.814`.

Essa é a linguagem visual "futurista" que o site pode usar **com legitimidade**,
porque é literalmente o que o piloto vê:

- Números grandes em fonte monoespaçada
- Cronômetro e deltas de tempo como elemento gráfico, não só como dado
- Réguas finas, cantos marcados, indicadores de estado — vocabulário de HUD
- Vermelho como sinal (marcador ativo, melhor volta), não como enfeite

**O site deve parecer a tela do cockpit, não um template escuro genérico de
"tecnologia".** Essa é a diferença entre futurismo emprestado e futurismo que
vem do produto.

## Inventário de movimento — o que entra e o que não entra

**Entra (movimento que É o produto):**
- Vídeo FPV real em tela cheia no topo, mudo, em loop, com poster frame
- Cronômetro contando / delta de tempo animando quando entra na tela
- Contadores dos números de capacidade (6 simuladores, etc.)
- Micro-interação em elemento de HUD (barra de sinal, indicador de estado)

**Não entra (movimento que atrasa informação):**
- Sequestro de scroll — nunca. O operador que veio ver capacidade e rotação
  não pode perder o controle da página.
- Animação de entrada que esconde os números do operador até ele rolar
- Parallax por cima de texto
- Animação de abertura da página (intro) — custa os primeiros 3 segundos, que
  são os que decidem

**Com cuidado:**
- Transição entre seções: leve e rápida (≤250ms), nunca bloqueante
- Respeitar `prefers-reduced-motion` — quem desligou animação no sistema vê a
  versão estática, e o site continua fazendo sentido

## A restrição honesta: peso e mobile

Site com vídeo pesado morre em conexão móvel, e é exatamente aí que o tal
"baixa conversão" acontece — não é o movimento em si, é o carregamento.
Regras:
- Vídeo sempre com poster frame (primeiro frame como imagem), carregamento
  preguiçoso, e nunca como bloqueio pro conteúdo aparecer
- Versão estática funcional: se o vídeo não carregar, a página continua
  vendendo sozinha
- O conteúdo que o operador precisa (capacidade, escala, contato) nunca fica
  atrás de um vídeo

## Onde o padrão "cinema em scroll" pode entrar

Num lugar só: a seção de "como se sente" — a passagem do lado de fora do
circuito pra dentro da visão FPV. É a única parte da página onde a emoção vale
mais que a informação. Curta, e com o resto da página sem isso.

**Técnica confirmada (23/09/2026, referências reais verificadas ao vivo):**
"canvas image sequence" — mesma técnica de página de produto da Apple. Extrai
frames reais do vídeo FPV do carro derrapando na pista e o scroll "dirige"
através deles (scrollbar vira acelerador, não navegação). Serve bem porque:
- Usa foto/frame **real** do cliente, sem gerar nada por IA.
- É curto e sincronizado 1:1 com o progresso do scroll — diferente do
  "sequestro" proibido acima porque não é uma cutscene forçada, é o único
  trecho da página onde pinar a seção é intencional e breve.
- **Cuidado explícito:** não repetir o padrão do Ford M-Sport Raptor
  (`msport-raptor.com`) — o próprio Awwwards rotula aquilo como "scroll
  hijack" porque prende o scroll numa câmera 3D renderizada (CGI, não foto
  real) por tempo longo demais. Usar só nessa seção, curto, e nunca no resto
  da página.
- Fora dessa seção, o padrão do hero continua sendo vídeo ambiente em loop
  sem interação de scroll (confirmado como padrão real de marca pesada:
  Porsche `racing.porsche.com`, McLaren `mclaren.com` — nenhum dos dois
  sequestra scroll).

**Tratamento de imagem pra stills:** duotone (mapear a foto pras cores da
marca — preto `#0A0B0D` + vermelho `#E31B23`, ou preto + prata `#B1B0AB`),
grain/textura de película, e motion blur direcional/radial (esticar o blur
na direção do movimento a partir do carro em foco, tipo filtro de blur
direcional do Photoshop/After Effects) — tratamento de cor/textura em cima de
pixel real. A regra "sem IA" do projeto é sobre não fabricar cena/pessoa/
depoimento falso, não sobre proibir ferramenta de IA — **ampliar/tratar uma
foto real do cliente com IA (upscale, extensão de enquadramento, etc.) é
permitido**, igual foi feito no hero da La Norma (confirmado pelo Diogo em
23/09/2026); o que não entra é gerar cena nova do zero. Não achei referência
de site específico fazendo esse tratamento num carro (marcar como técnica a
testar, não como cópia de exemplo visto).

**Vídeo real analisado (23/09/2026):** o cliente mandou `VID-20260909-WA00791.mp4`
(WhatsApp, 1024x576, 42.5s, salvo em `cliente/videos/drift-driftstation-20260909.mp4`).
Análise frame a frame (ffmpeg, não só resumo do vídeo):
- **Qualidade:** 1024x576 é resolução de WhatsApp (o original do cliente era maior,
  isso já é a versão comprimida). Tem artefato de bloco visível em área de detalhe
  (mural, tela do simulador) e a câmera é de mão, sem estabilização.
- **Conteúdo:** é um vídeo tipo "tour do espaço", não uma gravação dedicada de
  drift — a maior parte mostra o simulador (volante + tela curva com HUD de
  telemetria, confirmando ao vivo os números 12.3V/25Mbps/ms/barra de sinal já
  descritos acima) e planos gerais da pista com carros pequenos e devagar.
- **Achado bom:** em ~39.5-42.5s tem a única sequência de vários frames
  consecutivos com movimento real do vídeo inteiro — um carro parado acelera e
  passa raspando por uma câmera fixa baixa, gerando motion blur de verdade.
  Extraído (25 frames nativos, ffmpeg) e testado como canvas image sequence de
  verdade em `cliente/fotos-pista/canvas-sequence-test.html` (frames tratados em
  `build_sequence.py` → `sequence-launch/`) — **a técnica funciona**, o scroll
  pina a seção e "acelera" o carro. Mas: é lançada em linha reta, não é
  literalmente um drift lateral, e na resolução de origem fica granulada em
  tela grande — ok como prova de conceito, não como entrega final.
- **Atenção — nome da marca:** o ambiente físico do vídeo tem letreiro grande
  "DriftStation" (banner, mural de grafite, adesivo na parede) — diferente de
  "RC Arcade", que aparece só na tela de splash do simulador (visto no logo
  baixado, `cliente/logos/principal.png`). Não sei se "DriftStation" é o nome
  do espaço onde o cliente testa/grava (parceiro, pista alugada) ou outra
  relação — **perguntar ao Diogo/cliente antes de usar esse vídeo no site**,
  porque tem letreiro de terceiro aparecendo em quase todo frame.
- **Recomendação:** pedir ao cliente um clipe novo, dedicado, câmera fixa (não
  de mão), 5-10s, resolução maior que WhatsApp (enviar por Dropbox/cabo, não
  por WhatsApp) — o ganho de qualidade pra essa técnica é grande e o pedido é
  barato pro cliente atender.

**Primeiro protótipo com foto (23/09/2026):** testado com foto real do cliente
(`DSC09861.jpg`, pasta "RCA publicacion insta" do Dropbox, 23 fotos DSLR
profissionais da pista — a melhor fonte de imagem que temos hoje). Script em
`cliente/fotos-pista/treat_hero.py` (Python/PIL): crop 16:9, duotone,
grain, blur radial mantendo o carro em primeiro plano nítido e borrando o
fundo/pista pra sensação de velocidade. Duas variantes geradas:
`hero-duotone-preto-prata.jpg` (bate com a regra de token — vermelho só
acento) e `hero-duotone-preto-vermelho.jpg` (**descartada**: vermelho
cobrindo a imagem inteira viola a própria regra deste documento de "acento,
nunca fundo de área grande"). Mockup de contexto em
`cliente/fotos-pista/preview-hero.html`. Isso é o hero como still tratado —
**ainda não é o "canvas image sequence"** confirmado acima, porque essa
técnica precisa de vídeo real de drift/corrida, e o que existe hoje no
Dropbox do cliente (pasta `action5`) é câmera fixa do galpão (montagem da
pista + público do open-house), não FPV/onboard em ação. Ainda não descartar
a técnica de vídeo — só não foi possível testar ainda por falta de material.

## Ferramentas confirmadas pra implementação do movimento (Etapa 4/5)

Verificado em 23/09/2026 (reel de @kevin.snippet, conteúdo real, sem exagero,
biblioteca conhecida e checada): duas bibliotecas de JS puro, sem depender de
React — compatíveis com o export HTML/CSS/JS do Claude Design.

- **GSAP** — pra tudo que já está definido acima como "entra": cronômetro
  contando, contador de número de capacidade, micro-interação de HUD,
  transição de seção ≤250ms. É o motor certo pro "movimento que É o produto",
  não movimento decorativo.
- **Lenis** — scroll suave (inércia), não sequestro de scroll. Compatível com
  a regra "nunca sequestro" porque só deixa o scroll nativo mais fluido, não
  assume controle da página. Tem opção de respeitar `prefers-reduced-motion`
  — configurar isso explicitamente na implementação.
- **React Bits** — não serve. É biblioteca de componente React; o export
  atual é HTML puro. Descartado pra este projeto, a menos que o site vire um
  projeto React no futuro.

## Referência do Behance (pra Etapa 3)

Critério de busca pro passo do Claude Design, coerente com tudo acima:
- Buscar por **dashboard / telemetry / racing UI dark**, não por "landing page
  bonita"
- Escolher projeto **completo** (que mostre tipografia, grid, ícones e estados)
- Descartar referência que seja só estética escura sem estrutura de dados —
  precisamos de vocabulário de números e HUD, não de fundo preto com gradiente
