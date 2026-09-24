# Plano de implementação — Direção de Arte V2

Escrito em 24/09/2026. Transforma o `DIRECAO-DE-ARTE-V2.md` em plano executável.
**Nenhum código foi alterado até aqui** — isto é só plano.

## Inventário real de assets (antes de planejar qualquer coisa)

Conferido no disco agora, não por memória do que os documentos anteriores
diziam — duas correções importantes em relação ao que o `DIRECAO-DE-ARTE-V2.md`
sugeria:

| Asset | Existe no disco? | Detalhe |
|---|---|---|
| `DSC09861.jpg` | ✅ Sim, 4000×5000 | Vários carros, pórtico Red Bull, rampa. **Não usado ainda.** |
| `DSC09862.jpg` | ✅ Sim, 4000×5000 | Já usado (recorte em `assets/prueba-1600.jpg`) |
| `DSC09864.jpg` | ✅ Sim, 4000×5000 | Já usado (hero) |
| `DSC09865.jpg` | ✅ Sim, 4000×5000 | Pórtico Hyundai, pista vazia, bom desfoque de fundo. **Não usado ainda.** |
| 25 frames extraídos do vídeo (`sequence-launch/`) | ✅ Sim, mas **1024×381, baixa resolução** | Prototípo do canvas-sequence, não serve pra tela cheia em produção |
| Vídeo bruto (`drift-driftstation-20260909.mp4`) | ✅ Sim, 1024×576 | É onde o grafite/mural foi visto originalmente (análise frame a frame já registrada em `DESIGN-DIRECTION.md`) — **não confirmado em nenhuma das 4 fotos DSLR**, só no vídeo |
| Mais 16 fotos ("RCA publicacion insta") | ❌ **Não estão no disco** | Só catalogadas em `MATERIAL-RECEBIDO.md` como existentes no Dropbox do cliente. Corrijo o que o `DIRECAO-DE-ARTE-V2.md` sugeriu: não posso usar o que não baixei. |
| Medidas de espaço (m²) | ❌ Não existe | Pendente do cliente |
| Clipe de vídeo dedicado | ❌ Não existe | Pendente do cliente (já registrado em `TASKS.md`) |
| Dados de contato/localização | ❌ Não existe | Pendente do cliente |

**Achado novo, relevante pro risco:** as 4 fotos DSLR têm **logos de
patrocinador de terceiros visíveis** (Red Bull, Hyundai, Ford, Sonax — são
adesivos reais nos carros/pórticos do espaço do cliente). Não é motivo pra não
usar as fotos (são do espaço físico real do cliente), mas os enquadramentos
escolhidos abaixo evitam colocar uma marca de terceiro como foco central da
composição.

**Conclusão prática:** o plano de imagem deste ciclo trabalha com **2 fotos
novas** (`DSC09861`, `DSC09865`) além das 2 já em uso. Não é "6-10 fotos" como
o V2 sugeriu como ideal — é o que existe de verdade hoje. Pedir mais fotos ao
cliente fica registrado como item separado, não bloqueia este plano.

---

## Matriz de composição — as 6 seções de conteúdo

Nenhuma repete `H2 + parágrafo + grid`. Linguagem visual continua coerente
(mesma paleta, mesma tipografia, mesmo `.tag`) — muda a **composição**, não o
sistema.

| # | Seção | Composição escolhida | O que muda estruturalmente | Foto usada |
|---|---|---|---|---|
| 1 | **Qué es** | **Timeline horizontal** (não grid 4 colunas) | Os 4 passos viram pontos numa linha contínua (a própria régua vermelha do `.hero__line` vira o fio condutor) — a ordem é a informação, então o layout agora *mostra* sequência, não só numera caixas | Nenhuma (mantém texto puro — é a seção mais "processo", não precisa de imagem) |
| 2 | **La prueba** | **Immersive / full-bleed, com o HUD como protagonista** | A foto que já existe (`prueba-1600.jpg`) cresce pra quase largura total, mas o que justifica o tamanho é a telemetria sobreposta, não a foto em si — **sem foto nova, sem díptico** (ver correção do Design Gate, item 2). As specs continuam sendo uma `<dl>` real, com chip de fundo sólido, nunca só texto solto sobre pixel de foto (ver item 8 do gate) | `prueba-1600.jpg` (já existe, cresce em área) |
| 3 | **Para el operador** | **Manifesto** (reforça o que já é o ponto forte) | O `.statement` (`Hasta seis simuladores...`) deixa de ser um parágrafo grande no fim e vira o elemento organizador da seção — os 4 argumentos viram uma lista corrida abaixo dele, não um grid 2×2 | Nenhuma |
| 4 | **¿Cabe en tu espacio?** | **Comparison, com atmosfera de fundo (sem foto em primeiro plano)** | Os 2 cards viram uma comparação direta com régua central divisória. Diferença do item 5 abaixo: aqui a foto é só **textura ambiente em baixa opacidade** atrás da comparação, nunca um sujeito nítido — é o que diferencia esta seção de "Vías" visualmente, não só em proporção | `DSC09865` (novo — pista vazia/atmosférica, baixa opacidade, fundo) |
| 5 | **Tres vías** | **Split assimétrico, com papéis diferentes entre os 2 secundários** | "Instalación fija" (via principal) ganha foto em primeiro plano e ocupa mais espaço. "Evento temporal" vira uma linha de texto direta com link (sem moldura de card). "Formato competición" vira nota pequena, estilo legenda — o texto já diz que ela é "apoio, prova social"; o tratamento visual passa a concordar com isso, em vez de dar o mesmo peso de card às 3 vias | `DSC09861` (novo — múltiplos carros em ação, prova capacidade; recorte precisa cortar/desfocar o banner "Red Bull Racing" que domina o quadro, mesma técnica de blur já validada) |
| 6 | **Contacto + Público (pendentes)** | **Fechamento silencioso, sem impacto tipográfico** | Sem tipografia grande — a seção não tem dado real pra sustentar um momento de impacto, e forçar um só pra "parecer completa" seria decoração vazia. Vira texto corrido pequeno, direto, com os avisos de pendência como nota — honestidade visual, sem tentar disfarçar que falta informação | Nenhuma |

Isso cobre 6 composições sem repetir nenhuma — inclusive as duas colisões que
o Design Gate encontrou na primeira versão deste plano (`DESIGN-GATE-V2.md`,
itens 1, 2 e 3): "Operador" e "Contacto" não são mais duas versões do mesmo
"manifesto", e "Escalas"/"Vías" se diferenciam pelo tratamento de imagem
(atmosfera de fundo vs. sujeito em primeiro plano), não só pela proporção de
coluna. Nenhuma composição copia layout da Porsche — ela foi usada só pra
descobrir os *padrões* (altura variável, foto dominante, tipografia grande),
não como template.

---

## Plano P0 — muda a percepção de qualidade imediatamente

### P0.1 — Reinterpretar "La prueba" como immersive/full-bleed

> **Revisado pelo Design Gate (`DESIGN-GATE-V2.md`, itens 2 e 8).** A versão
> original propunha um díptico com `DSC09861` e specs vivendo só dentro do
> HUD da foto — as duas ideias foram descartadas: díptico de duas fotos
> parecidas não cria narrativa (só tamanho), e specs sem `<dl>` real
> quebraria a regra já escrita em `DESIGN-DIRECTION.md` ("conteúdo que o
> operador precisa nunca fica atrás de imagem"). A versão abaixo já reflete
> a correção.

- **Objetivo visual:** o bloco que prova "isto é real" precisa parecer a coisa
  mais importante da página, não uma seção de specs com foto de apoio — e a
  razão de ocupar mais tela tem que ser o dado (telemetria), não só a foto.
- **Problema atual que resolve:** a foto está confinada a `grid-template-columns:
  1.35fr 1fr` (linha 273 do `index.html`) — perde pra qualquer seção de texto em
  peso visual, quando deveria vencer todas.
- **Arquivo/local exato:** `index.html`, seção `#prueba` (linhas 525-555) e
  regras `.proof*` (linhas 272-296).
- **O que será removido:** o grid de 2 colunas fixas (`1.35fr 1fr`).
- **O que será criado:** a foto que já existe (`prueba-1600.jpg`, **sem foto
  nova**) cresce pra quase 100% da largura do `.shell`. O HUD sobreposto
  cresce junto e vira o elemento visualmente dominante — não é "foto grande
  com dado em cima", é "o dado é o motivo da foto estar em tela cheia". A
  `<dl class="specs">` **continua existindo como HTML real**, com um chip de
  fundo sólido (`--rc-surface` ou preto com opacidade alta — nunca só
  gradiente transparente) atrás do texto, garantindo que ela existe e é
  legível mesmo se a imagem falhar ao carregar.
- **Comportamento visual esperado:** ao rolar até essa seção, a foto e a
  telemetria dominam o viewport quase como um segundo hero — reforça
  "prova", não "detalhe". Se a imagem falhar, as specs continuam visíveis
  (fundo sólido, não dependem do pixel da foto).
- **Dependências/assets:** nenhuma foto nova. Só CSS/layout.
- **Risco de quebrar algo:** contraste do HUD sobre a foto grande (mesma
  regra de AA já corrigida no hero) — testar com o detector da `impeccable`.
  Risco de regra quebrada (specs escondidas atrás de imagem) **eliminado**
  pela correção acima.
- **Como validar:** screenshot desktop+mobile lado a lado com a versão atual;
  rodar `impeccable detect` pra contraste; simular falha de carregamento da
  imagem (DevTools/network throttling) e confirmar que as specs continuam
  legíveis.

### P0.2 — Trazer as 2 fotos reais não usadas (`DSC09861`, `DSC09865`)

> **Revisado pelo Design Gate, item 6.** Os encaixes originais estavam
> trocados — `DSC09861` (ação, múltiplos carros) ia pra "La prueba" (que já
> tem foto de ação própria) e `DSC09865` (vazia, atmosférica) ia pra "Vías"
> (que precisa de prova de capacidade, não de clima). Corrigido abaixo.

- **Objetivo visual:** aumentar a presença de fotografia real no site, que
  hoje é o ponto mais fraco (2 fotos em 8 seções) — e usar cada foto pro
  argumento que ela realmente prova.
- **Problema atual que resolve:** o site defende "isto é real" quase só com
  texto.
- **Arquivo/local exato:** novos arquivos em `assets/` (`via-principal.jpg`,
  `escalas-bg.jpg`) + referência em `#vias` (P1.2) e `#escalas` (P1.4).
  **Não entra em `#prueba`** (ver P0.1 revisado).
- **O que será removido:** nada.
- **O que será criado:**
  - `DSC09861.jpg` → recorte pra **"Vías/Instalación fija"** — mostra 3
    carros circulando ao mesmo tempo, é a prova visual mais direta de
    capacidade multi-simulador que existe. **Precisa de blur/corte
    direcionado pra tirar o banner "Red Bull Racing"** (elemento dominante
    do quadro original) do centro de leitura — usar a mesma técnica de
    motion blur radial já validada em `treat_hero_v2.py`, direcionada pro
    banner em vez do fundo genérico.
  - `DSC09865.jpg` → recorte pra **fundo de "Escalas"**, em baixa opacidade,
    sem tratamento de sujeito nítido — é atmosfera, não protagonista.
- **Comportamento visual esperado:** duas fotografias reais novas aparecem
  no site, cada uma reforçando o argumento da seção onde está, não só
  "preenchendo espaço visual".
- **Dependências/assets:** já cobertos pelo inventário — nenhuma foto nova
  precisa ser pedida ao cliente pra isso.
- **Risco:** peso de página (mitigado com o mesmo padrão de `srcset`/`sizes`
  do hero); o corte do banner em `DSC09861` precisa ser conferido
  visualmente antes de aprovar — se o blur não for suficiente pra tirar a
  legibilidade do banner, recortar mais fechado no grupo de carros em vez de
  tentar desfocar.
- **Como validar:** medir peso total da página (hoje: 379KB no primeiro
  paint; meta: não passar de ~700KB mesmo com as fotos novas); conferir que
  nenhum logo de patrocinador terceiro é o elemento mais legível de nenhuma
  composição.

### P0.3 — Entrada de scroll pras seções que hoje aparecem sem transição

- **Objetivo visual:** distribuir o movimento que hoje só existe no hero pelo
  resto da página.
- **Problema atual que resolve:** `#que-es`, `#operador`, `#escalas`, `#vias`,
  `#contacto` aparecem instantaneamente ao rolar — o site "morre" depois dos
  primeiros 3 segundos.
- **Arquivo/local exato:** bloco `<script>` no fim do `index.html` (depois da
  linha 744, junto do `IntersectionObserver` que já existe pro cronômetro) +
  uma classe CSS nova tipo `.reveal` perto da linha 100.
- **O que será removido:** nada — é aditivo.
- **O que será criado:** um `IntersectionObserver` genérico que adiciona uma
  classe quando a seção entra na tela, disparando `opacity`+`translateY`
  leve (≤250ms, conforme a regra já escrita em `DESIGN-DIRECTION.md`).
- **Comportamento visual esperado:** cada seção "chega" suavemente ao entrar
  no viewport, uma vez, sem travar o scroll.
- **Dependências/assets:** nenhuma — é só JS/CSS, reaproveitando o padrão que
  o cronômetro do hero já usa.
- **Risco:** se mal calibrado, pode parecer "efeito de template de animação
  on-scroll" — o motion tem que ser sutil o bastante pra não virar o oposto
  do que o P0 quer resolver. Mitigação: mesma curva de easing (`--ease`) já
  usada no resto do site, delay curto, sem "bounce".
- **Como validar:** gravar o scroll da página inteira e conferir que nada
  pisca, quebra layout, ou aparece duas vezes (reentrada ao rolar pra cima e
  descer de novo); testar com `prefers-reduced-motion` ativado.

---

## Plano P1 — constrói vocabulário de marca próprio

### P1.1 — Timeline horizontal em "Qué es"

- **Objetivo visual:** parar de tratar sequência como grid de cards iguais.
- **Problema que resolve:** `.steps` (linha 250) é um grid de 4 colunas
  idênticas — não comunica "isto é uma sequência", só "isto é uma lista".
- **Arquivo/local exato:** `index.html`, `.steps`/`.step` (linhas 250-270) e
  o HTML de `#que-es` (linhas 493-521).
- **O que será removido:** o grid `repeat(4,1fr)` com borda direita entre
  colunas.
- **O que será criado:** uma linha horizontal contínua (reaproveitando o
  gesto do `.hero__line` vermelho) conectando os 4 números, com os textos
  pendurados abaixo/acima alternadamente ou em sequência simples — o fio
  vermelho é o dado novo, os cards desaparecem.
- **Comportamento visual esperado:** a seção comunica "passo 1 leva ao passo
  2" visualmente, não só numericamente.
- **Dependências/assets:** nenhuma.
- **Risco:** em mobile a timeline horizontal pode não caber — precisa virar
  vertical abaixo de ~700px, com a linha girando 90°. Testar cedo.
- **Como validar:** comparar com a versão atual lado a lado; conferir mobile
  primeiro (é o caso mais arriscado).

### P1.2 — Split assimétrico em "Tres vías"

> **Revisado pelo Design Gate, itens 3 e 6.** Além de dar mais espaço à via
> principal, os dois secundários agora têm **papéis diferentes entre si**
> (não só "menores") — e a foto certa (`DSC09861`) entra aqui, não em "La
> prueba".

- **Objetivo visual:** parar de repetir o mesmo card 3 vezes, e fazer o peso
  visual de cada via corresponder ao que o próprio texto já diz sobre ela.
- **Problema que resolve:** `.way` (linha 320) é literalmente o mesmo
  componente 3 vezes — o padrão "3 planos de preço" mais genérico que existe.
- **Arquivo/local exato:** `.ways`/`.way` (linhas 320-331) e HTML de `#vias`
  (linhas 622-655).
- **O que será removido:** a estrutura onde as 3 vias têm o mesmo peso visual
  e a mesma forma de card em linha.
- **O que será criado:**
  - "Instalación fija" ganha a foto `DSC09861` (recortada pra tirar o banner
    de patrocinador, ver P0.2) e ocupa a maior parte da seção.
  - "Evento temporal" vira uma **linha de texto direta com link**, sem
    moldura de card.
  - "Formato competición" vira uma **nota pequena, estilo legenda/rodapé**
    — o texto já diz que ela é "apoyo, prueba social, no es la puerta de
    entrada" (linha 649); o tratamento visual passa a concordar com isso.
- **Comportamento visual esperado:** fica visualmente óbvio qual é a via
  principal, e as outras duas não competem entre si por serem "cards
  iguais menores" — cada uma tem sua própria função de leitura.
- **Dependências/assets:** `DSC09861.jpg` (recorte novo, com correção de
  banner — ver P0.2).
- **Risco:** dar peso visual desigual pode parecer que as outras 2 vias
  importam menos do que deveriam pro negócio — mitigado porque a premissa já
  registrada em `ESTRUTURA-DO-SITE.md` confirma que instalação fixa é a via
  principal; isso reforça uma decisão já tomada, não inventa uma nova.
- **Como validar:** ler a seção sem o texto (só olhando a composição) e
  confirmar que dá pra entender qual é a via prioritária; confirmar que o
  banner de patrocinador não é o elemento mais legível da foto.

### P1.3 — Manifesto em "Para el operador" (reforçar o que já funciona)

- **Objetivo visual:** o `.statement` (linha 304) é o melhor momento do site
  hoje — ele devia organizar a seção, não ser o resumo dela no final.
- **Problema que resolve:** os 4 `.arg` em grid 2×2 competem com o
  `.statement` por atenção, quando deveriam alimentá-lo.
- **Arquivo/local exato:** `.args`/`.arg`/`.statement` (linhas 298-309) e
  HTML de `#operador` (linhas 560-585).
- **O que será removido:** o grid 2×2 dos 4 argumentos.
- **O que será criado:** os 4 argumentos viram uma lista corrida, mais
  discreta tipograficamente, **abaixo** do `.statement`, que sobe pro topo da
  seção e cresce.
- **Comportamento visual esperado:** quem rola a página lê primeiro "hasta
  seis simuladores simultáneos..." em destaque, depois os argumentos como
  detalhamento — inverte a ordem de importância visual pra bater com a
  ordem de importância real.
- **Dependências/assets:** nenhuma.
- **Risco:** baixo — é reorganização de hierarquia existente, não conteúdo
  novo.
- **Como validar:** teste de 5 segundos (mostrar a seção por 5s e perguntar o
  que ficou) — se a resposta for "seis simuladores" em vez de "diferenciación",
  funcionou.

### P1.4 — Comparison com atmosfera de fundo em "¿Cabe en tu espacio?"

> **Revisado pelo Design Gate, itens 1 e 6.** Ganha a foto `DSC09865` como
> fundo — mas só como atmosfera em baixa opacidade, nunca sujeito nítido.
> Essa é a diferença deliberada em relação a "Vías" (que tem foto em
> primeiro plano): sem isso, as duas seções seriam "duas colunas" com o
> mesmo tratamento e colidiriam de novo.

- **Objetivo visual:** a pergunta do título ("cabe no meu espaço?") merece
  uma resposta visual de comparação, não dois cards genéricos — e precisa se
  distinguir de "Vías", que também é uma composição de duas colunas.
- **Problema que resolve:** `.scales`/`.scale` (linha 312) é grid 2 colunas
  igual a qualquer seção de "planos".
- **Arquivo/local exato:** `.scales`/`.scale` (linhas 311-317) e HTML de
  `#escalas` (linhas 588-618).
- **O que será removido:** os 2 cards com borda superior igual.
- **O que será criado:** uma régua central dividindo as duas opções, com
  contraste tipográfico entre "compacto" (mais denso, menor) e "completo"
  (mais espaçoso, maior) — o próprio espaçamento vira parte do argumento.
  `DSC09865.jpg` entra como fundo de seção em baixa opacidade (textura de
  espaço vazio/pista), nunca como imagem nítida em primeiro plano.
- **Comportamento visual esperado:** a diferença de escala entre os dois
  planos aparece no próprio layout; a atmosfera de fundo dá clima de "espaço
  físico real" sem competir com o texto.
- **Dependências/assets:** `DSC09865.jpg` (recorte novo, baixa opacidade).
- **Risco:** a `.pending` (nota de medidas reais pendentes) precisa continuar
  visível e honesta dentro dessa composição nova — não pode sumir. O fundo em
  baixa opacidade precisa manter contraste de texto em AA mesmo com a foto
  atrás.
- **Como validar:** conferir que o aviso de "medidas pendentes" ainda está
  presente e legível; rodar `impeccable detect` pra contraste com o fundo
  novo; confirmar visualmente que esta seção não parece "a mesma coisa" que
  "Vías" ao rolar as duas em sequência.

### P1.5 — Momento tipográfico grande com cronômetro/delta

> **Revisado pelo Design Gate, itens 4 e 7.** A versão original deixava em
> aberto se isso era identidade ou decoração, sem responder. Agora tem dois
> requisitos obrigatórios pra contar como identidade — e o fundo é liso
> (`--rc-black`), não uma foto, justamente pra não copiar o gesto "número
> gigante sobre still em preto-e-branco" que é da Porsche.

- **Objetivo visual:** dar ao dado mais "só da RC Arcade" (o cronômetro) um
  momento de impacto que se repete como sistema, não um efeito único.
- **Problema que resolve:** `00:42.381` e `+0.814` só aparecem pequenos
  (`.readout__time` linha 216, `.proof__lap b` linha 285) — nunca em escala
  de título.
- **Arquivo/local exato:** entre `#prueba` e `#operador` (transição de
  seção), como um elemento novo, não uma seção inteira.
- **O que será removido:** nada.
- **O que será criado:** uma faixa curta com o delta ou o tempo em escala
  tipográfica grande, **sempre acompanhado do rótulo pequeno** ("Mejor
  vuelta" ou equivalente — nunca o número sozinho sem contexto), fundo liso
  `--rc-black`, tipografia `JetBrains Mono` (não a fonte display do resto do
  site — reforça que é leitura de instrumento, não título editorial).
- **Comportamento visual esperado:** um respiro visual grande entre "La
  prueba" e "Para el operador", com o dado real do produto — reconhecível
  como o mesmo sistema que aparece no hero e em "La prueba", não um efeito
  isolado.
- **Dependências/assets:** nenhuma (é o mesmo dado `00:42.381` já usado em
  outros dois lugares do site — condição obrigatória pra isso ser "sistema").
- **Risco:** se o rótulo for removido "pra limpar a composição", o elemento
  volta a ser decoração — **não remover o rótulo em nenhuma hipótese**.
- **Como validar:** confirmar que o mesmo tratamento tipográfico aparece em
  pelo menos 2 outros lugares do site (hero, "La prueba"); confirmar que o
  rótulo pequeno está presente mesmo na versão grande.

### P1.6 — `padding-block` variável por seção

- **Objetivo visual:** parar de ter o mesmo ritmo vertical entre todas as
  seções.
- **Problema que resolve:** `section{padding-block:var(--section)}` (linha
  102) aplica o mesmo valor em 100% das seções.
- **Arquivo/local exato:** linha 51 e 102, mais uma regra por `id` de seção.
- **O que será removido:** a aplicação global sem exceção.
- **O que será criado:** `#prueba` (agora immersive) ganha menos padding
  vertical (a foto já ocupa espaço); `#contacto` (fechamento minimal) ganha
  mais espaço em volta, pra parecer proposital, não incompleto.
- **Comportamento visual esperado:** o scroll deixa de ter cadência de
  metrônomo.
- **Dependências/assets:** nenhuma — depende das mudanças de P0.1 e P1.1-P1.4
  estarem prontas primeiro (senão não dá pra saber qual seção precisa de mais
  ou menos ar).
- **Risco:** baixo, é ajuste fino por último.
- **Como validar:** rolar a página inteira e sentir se algum trecho ainda
  parece "batendo o mesmo tambor" que o anterior.

---

## Plano P2 — exploratório, só se fizer sentido depois do P0/P1

### P2.1 — Textura real do espaço (grafite/mural)

> **Revisado pelo Design Gate, item 5.** A versão original tratava isso como
> "incerto, vamos testar". Existe evidência **já registrada** contra: a
> análise frame-a-frame anterior (`DESIGN-DIRECTION.md` linha 178-179) já
> encontrou "artefato de bloco visível em área de detalhe (**mural**, tela do
> simulador)" — ou seja, a região do grafite já foi observada com compressão
> visível, antes mesmo de qualquer tentativa nova de extração.

- **Objetivo visual:** um elemento gráfico que só a RC Arcade poderia ter.
- **Problema que resolve:** hoje nada no site é "só desta marca".
- **Arquivo/local exato:** a definir — provavelmente fundo de uma seção
  (`#vias` ou `#operador`).
- **O que será criado:** nada, por padrão. Um frame extraído de
  `drift-driftstation-20260909.mp4` só valeria a pena testar se o Diogo
  achar um motivo específico pra insistir, sabendo que a probabilidade de
  servir em tela grande já é baixa pela evidência acima.
- **Dependências/assets:** vídeo já está no disco.
- **Risco:** alto de retrabalho — extrair, tratar e só depois descobrir que
  não presta é gastar um ciclo inteiro num item que o próprio projeto já
  tinha razão pra desconfiar.
- **Como validar:** se decidir testar mesmo assim, extrair 1-2 candidatos
  primeiro (não 3-4) e decidir rápido, sem investir tratamento nenhum antes
  de confirmar que a resolução aguenta ampliação.

### P2.2 — Cor de acento secundária pontual

- **Objetivo visual:** um momento cromático que quebra o preto/prata/vermelho
  puro, do jeito que o roxo faz na Porsche.
- **Problema que resolve:** zero variação cromática em 100% do site.
- **O que será criado:** nada ainda — **isto é uma pergunta em aberto, não
  uma decisão.** A cor teria que vir de algo real do material do cliente
  (uma cor que já aparece nas fotos ou no espaço), não ser inventada do zero
  — isso contrariaria a regra de honestidade do projeto.
- **Risco:** se não houver uma cor real e legítima pra usar, este item não
  deve ser feito só pra "ter uma cor diferente".
- **Como validar:** perguntar ao Diogo/cliente antes de qualquer execução.

### P2.3 — Rodar `impeccable animate` e `impeccable detect` no resultado final

- Só depois que as composições de P0/P1 estiverem implementadas e aprovadas
  — animar uma composição que ainda vai mudar é retrabalho.

---

## Lista de assets necessários

**Já existem, só precisam de tratamento/recorte novo:**
- `DSC09861.jpg` → usar em P1.2 ("Vía principal" — recorte com correção de
  banner de patrocinador)
- `DSC09865.jpg` → usar em P1.4 (fundo de "Escalas", baixa opacidade)

**Já existem prontos, só precisam ser referenciados:**
- `assets/prueba-1600.jpg` (crescer no layout, P0.1 — **nenhuma foto nova
  entra em "La prueba"**)
- Vídeo `drift-driftstation-20260909.mp4` (pra explorar P2.1, sem garantia de
  uso — evidência já registrada sugere baixa probabilidade de servir)

**Não existem — pendentes do cliente (não bloqueiam o P0/P1):**
- Medidas reais de espaço (m²) — `#escalas`
- Clipe de vídeo dedicado — hero (já registrado em `TASKS.md`)
- Dados de contato/localização — `#contacto`
- Mais fotos do Dropbox ("RCA publicacion insta", 16 fotos catalogadas, 0
  baixadas) — se quiser mais variedade de imagem além das 2 usadas aqui

**Em aberto, decisão do Diogo:**
- Se vale a pena buscar o frame do grafite no vídeo (P2.1)
- Se existe uma cor secundária legítima pra usar (P2.2)

---

## O que será preservado

- Paleta de marca e a regra "vermelho só como sinal" — não muda.
- Tipografia (Archivo + JetBrains Mono, registro Porsche) — não muda.
- O sistema `.tag` (filete + rótulo mono) — reaproveitado em todas as
  composições novas, é o elemento mais "de marca" que já existe.
- Hero e intro — intocados, já validados.
- Toda a engenharia de motion existente (nav, botão, scrollbar, cronômetro,
  menu mobile) — só ganha companhia, nada é substituído.
- A regra de honestidade: seções com dado pendente continuam dizendo isso
  claramente — "Escalas" com composição mais deliberada (P1.4), "Contacto"
  sem tentar disfarçar a falta de dado com impacto visual que não existe.

## O que será removido

- O grid `repeat(4,1fr)` de `.steps` (vira timeline).
- A divisão de colunas fixas `1.35fr 1fr` de `.proof` (vira immersive).
- O grid `1fr 1fr` de `.args` (os 4 argumentos viram lista corrida).
- A simetria de 3 colunas iguais em `.ways` (vira split assimétrico).
- A simetria de 2 cards iguais em `.scales` (vira comparison com régua
  central).
- O `padding-block` idêntico aplicado sem exceção a todas as seções.

## Ordem exata de implementação

> **Revisado pelo Design Gate, item 10.** A ordem original começava pela
> mudança mais arriscada ("La prueba", que esbarrava na regra de conteúdo
> nunca atrás de imagem — já corrigida no P0.1, mas descoberta tarde
> demais). A ordem abaixo separa **prioridade** (P0/P1/P2, que não muda) de
> **sequência de execução** (que segue risco e dependência): as mudanças sem
> asset novo e sem risco de regra quebrada vêm primeiro, pra validar o
> padrão de composição antes de mexer nas duas seções que envolvem foto e
> HUD.

1. **P1.1 — "Qué es" (timeline).** Zero asset novo, zero risco de a11y —
   melhor lugar pra validar o padrão de composição nova antes de tudo.
2. **P1.3 — "Para el operador" (manifesto).** Reorganização de hierarquia
   existente, sem conteúdo novo, sem asset.
3. **"Contacto" — fechamento minimal.** A mais simples, sem tipografia de
   impacto, sem asset.
4. **Preparar assets** — recortar `DSC09861.jpg` (com correção de banner) e
   `DSC09865.jpg` (baixa opacidade); confirmar pesos finais. Só agora, depois
   de validar o padrão de composição nas 3 seções sem imagem.
5. **P1.2 — "Tres vías"** (usa `DSC09861`, já com a correção de hierarquia
   entre os 2 secundários).
6. **P1.4 — "Escalas"** (usa `DSC09865` como fundo, comparison com régua
   central).
7. **P0.1 — "La prueba"** (por último entre as seções, porque é a que mais
   depende de acertar o requisito do item 8 do gate: specs continuam `<dl>`
   real, com chip de fundo sólido, testado inclusive com a imagem falhando
   ao carregar).
8. **P1.6** — ajustar `padding-block` por seção, agora que todas as 6 têm
   composição final definida.
9. **P0.3** — aplicar entrada de scroll a todas as seções já reinterpretadas.
10. **P1.5** — inserir o momento tipográfico do cronômetro entre "La prueba"
    e "Para el operador", confirmando que o mesmo tratamento já existe em
    pelo menos 2 outros lugares do site antes de considerar concluído.
11. **Validação geral** — `impeccable detect`, screenshot desktop+mobile de
    cada seção, teste com `prefers-reduced-motion`, teste de falha de
    carregamento de imagem em "La prueba", medição de peso total da página.
12. **P2 (opcional, com o Diogo)** — só depois de 1-11 aprovados: explorar
    frame do grafite (P2.1, expectativa baixa) e cor secundária (P2.2, só
    com material real).

Nenhum passo acima foi executado. Este é só o plano, já revisado pelo
`DESIGN-GATE-V2.md`.
