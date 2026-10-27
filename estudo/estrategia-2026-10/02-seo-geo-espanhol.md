# RC Arcade: como ser encontrado no Google da Espanha e citado pelas IAs

> Tipo: **estudo** (fotografia de 27/10/2026, não se reescreve; se mudar, faz-se outro).
> Pergunta: como o site deve ser encontrado e citado, no Google.es e nas respostas de IA,
> por quem decide comprar uma atração (operador de ocio, organizador de eventos,
> ayuntamiento, centro comercial, karting).
> Feito com: Google.es ao vivo (Chrome do Diogo), autocompletar do Google (es-ES), Modo IA do
> Google, documentação oficial do Google, OpenAI, Perplexity, GitHub, Microsoft e AEPD, e as
> páginas dos concorrentes abertas uma a uma.

## Resumo em 10 linhas

1. **O cliente já tem domínio próprio e já aparece no Google.** `rcarcade.es` (e `rcarcade.com`) mostra uma "Presentación Corporativa" que é o **1º resultado** para "rc arcade". O site que estamos fazendo (`github.io`) tem **zero páginas no Google**.
2. **O Modo IA do Google já cita o RC Arcade** quando a pergunta descreve o produto, mas usa a página antiga do cliente. Quando a pergunta é genérica ("busco una atracción nueva"), o RC Arcade **não aparece**.
3. **Existe imprensa real:** o *El Hormiguero* (Antena 3) fez uma corrida num "simulador de RC Arcade" em 07/10/2026. O nosso status diz "não há imprensa"; isso mudou.
4. O nicho exato ("coches RC + FPV + volante") quase não tem busca. Quem compra procura por **categoria vizinha**: "alquiler simuladores para eventos", "circuito rc para eventos", "atracciones para eventos", "team building".
5. Concorrência real no Google: **WarmUp Lap** (circuito RC para eventos, com FAQ, schema e llms.txt), empresas de simulador (Simtechpro, HiSpeedSim, Trackter) e, lá fora, **Racetech** e kits chineses.

**As 5 decisões que mais mudam a estrutura do site:**
- **D1. Publicar no `rcarcade.es`**, substituindo a página atual com redirecionamento, e mandar `.com` e `www`/sem-`www` para um endereço só. Hoje são 4 cópias da mesma página.
- **D2. Uma página por comprador, não uma página única:** `/centros-de-ocio/`, `/eventos/`, `/competicion/`, mais `/como-funciona/`, `/video/`, `/preguntas-frecuentes/`, `/presupuesto/`. Cerca de 8 páginas, nada de dezenas.
- **D3. O vídeo real ganha página própria** (`/video/`) e canal no YouTube. É a prova que nenhum concorrente tem, e o Google só indexa vídeo que é o assunto principal da página.
- **D4. Escrever para ser citado:** uma frase que define o produto, números que temos (até 6 pilotos, 4 passos, 2 escalas, 3 vias, 4 formatos) e as respostas que a IA pede e **ainda não temos** (m², tempo de montagem). Faltam do cliente.
- **D5. Página `/prensa/` + menções de terceiros** (El Hormiguero, FIOCIO, Eventoplus, revista da AECC). Para IA, o que os outros dizem pesa tanto quanto o que o site diz.

---

## Como ler este documento

- **CONFIRMADO**: vi com meus olhos numa página aberta hoje (link ao lado).
- **INFERÊNCIA**: conclusão minha a partir do que vi. Pode estar errada.
- **NÃO VERIFICADO**: não consegui conferir. Não usar como fato.

**Limites honestos (leia antes de tudo):**
- **Não tenho volume de busca, CPC nem "dificuldade".** Isso só sai de ferramenta paga ou do
  Planejador de Palavras-chave do Google Ads com conta. Nenhum número desses aparece aqui.
- Os sinais que usei são verificáveis: **autocompletar** do Google em espanhol da Espanha (só
  aparece sugestão quando há gente buscando; lista vazia é sinal fraco de pouca busca,
  **INFERÊNCIA**), "Otras personas también buscan", "Más preguntas", **tipo de página** que
  ranqueia e **quem** ranqueia.
- As buscas ao vivo foram feitas no Chrome do Diogo, no google.es. **O Google localizou em
  Valência** (os mapas mostram Valência). Em Madrid ou Barcelona o mapa local muda. Os
  resultados orgânicos nacionais (fabricantes, diretórios) tendem a mudar menos (**INFERÊNCIA**).
- A ferramenta de busca interna da IA (WebSearch) é dos EUA; por isso usei o Google.es real.
- O Perplexity pediu verificação anti-robô. **Não contornei.** Teste do Perplexity e do
  ChatGPT fica para o Diogo fazer à mão (roteiro na seção 6).

---

## 0. O que descobri no caminho e muda o plano

### 0.1 O cliente já tem site e domínio — CONFIRMADO

- `https://www.rcarcade.es` está no ar, título "RC Arcade — Presentación Corporativa", rodando
  num servidor Apache. `rcarcade.com` também, com o mesmo conteúdo (só muda o tamanho do
  logo e uma imagem). As 4 versões (`rcarcade.es`, `www.rcarcade.es`, `rcarcade.com`,
  `www.rcarcade.com`) respondem "200", **sem redirecionar** uma para a outra, sem
  `robots.txt`, sem `sitemap.xml`, sem meta description. (Conferido com `curl` hoje.)
- No Google.es, a busca `site:rcarcade.es OR site:rcarcade.com` traz **1 resultado**:
  a página do `.es`. A busca `site:diogotorresweb.github.io` traz **nenhum**.
- A página do cliente tem conteúdo que **não está no nosso dossiê**, escrito por eles:
  formatos *Race, Time Attack, Teams, Branded*; "configuración habitual entre cuatro y seis
  puestos"; "el equipo RCArcade instala, configura y prueba el sistema… atiende incidencias";
  "Cinco datos bastan para preparar una primera propuesta" (tipo de espaço, local e datas,
  público, duração, personalização); e uma tabela "RCArcade vs Simulador".
- A página **traz contato** (um e-mail `@rcarcade.com` e dois telefones `+34`). O nosso
  `CURRENT_STATUS.md` lista "contato comercial" como dado que falta. **Não copiei os números
  para cá.** Antes de usar, o Diogo confirma com o cliente que são esses os contatos do site
  novo (**NÃO VERIFICADO** se continuam valendo).

**Por que importa:** o domínio `.es` já tem algum histórico no Google e já é a página que o
Google e a IA conhecem como "RC Arcade". Publicar o site novo em outro endereço seria começar
do zero e competir com o próprio cliente.

### 0.2 Já existe imprensa nacional — CONFIRMADO (a ligação com o cliente é INFERÊNCIA forte)

- Antena 3, *El Hormiguero*, 07/10/2026: "La espectacular carrera de coches de radio control
  entre Pablo Motos y David Bustamante". O texto diz que eles pilotaram "un simulador de RC
  Arcade". Sem link para o site do cliente.
  [antena3.com](https://www.antena3.com/programas/el-hormiguero/espectacular-carrera-coches-radio-control-pablo-motos-david-bustamante_202610076ac6b6af48d2d008d0c92c53.html)
- A "Vista creada con IA" do Google, na busca sobre essa matéria, já liga o programa ao
  `rcarcade.es`. Que seja **o mesmo** RC Arcade do nosso cliente é **INFERÊNCIA forte**
  (mesmo nome, mesmo produto, circuito com ponte). **Confirmar com o cliente** e pedir o
  vídeo/autorização para citar.

### 0.3 O nome "RC Arcade" é disputado — CONFIRMADO

- Busca "rc arcade" no Google.es: além do `rcarcade.es`, aparecem um **app** "RC Arcade" no
  Google Play e na App Store (desenvolvedor Capygang), o **aRCadeRally** (carros RC reais
  controlados pela internet), vídeos do jogo de fliperama *Go By RC*, e um "RCADE" na Costa Rica.
- Busca "rcarcade" (junto): o Google pergunta "Quizás quisiste decir: arcade". Aparecem também
  `rcarcade.net` e `rcarcade.online` (de outra empresa, de simracing).
- Autocompletar de "rc arcade" (es-ES): "rc arcade game", "rc arcade mod", "rc arcade apk"…
  Ou seja: **quem digita só o nome hoje está procurando o jogo de celular** (**INFERÊNCIA**
  a partir das sugestões).
- O próprio cliente escreve de 3 jeitos: "RC ARCADE" (dossiê), "RCArcade" (site dele),
  "RC Arcade" (título). **Recomendo fixar uma grafia** para o site e para os dados
  estruturados (sugestão: "RC Arcade", que é como Antena 3 e o Google escrevem), e sempre
  colar um descritor: "RC Arcade, atracción de carreras con coches RC reales en primera persona".

### 0.4 Concorrentes que o `CONCORRENTES.md` ainda não tinha — CONFIRMADO

| Quem | O que é | Onde vi |
|---|---|---|
| **WarmUp Lap / "RC Racing Experience"** | Circuito RC modular para eventos e feiras, carros 1:28, cronometragem por transponder, 6 carros (máx. 8). **Sem FPV e sem cockpit.** Página com FAQ, schema `Service`, `FAQPage`, `BreadcrumbList`, e com `llms.txt`. | [warmuplap.es/circuito-rc-para-eventos](https://warmuplap.es/circuito-rc-para-eventos) |
| Rodamos Juntos, Alquilar Scalextric, Podium Slot, MOA Eventos, Kleem Eventos | Aluguel de circuito RC / scalextric / team building com RC | SERP de "alquiler circuito coches radiocontrol para eventos" |
| RC Experience 4x4 | Circuito RC 4x4 pago, montado na praça do C.C. El Saler (Valência) | SERP + Instagram (perfil não aberto) |
| Simtechpro, HiSpeedSim, Trackter, Whiplash, NLTech, Simufy, RaceGear | Aluguel e venda de simuladores para eventos e locais | SERP de "alquiler simuladores para eventos" |
| Racetech ("Speed Rush FPV Car Racing"), MIXR XR, VBR Racezone, fábricas chinesas ("FPV sand table racing"), Alibaba ("Equipo Comercial de Entretenimiento" 1:28 FPV com volante) | Mesma ideia, mercado internacional | SERP em inglês e "coche rc con volante y pedales fpv" |
| E1RC (loja de RC em Gijón) | Um youtuber (Alejandro Valderrey, 15/07/2026, ~6,5 mil visualizações) mostrou um circuito FPV com volante e pedais lá; o Modo IA do Google cita a E1RC como "centro de ocio permanente" | Descrição do vídeo lida com `yt-dlp`. A home da loja **não** fala de FPV: **NÃO VERIFICADO** que a E1RC opere isso |

---

## 1. Mapa de intenção em espanhol

Legenda da coluna "Sinal": **A** = aparece no autocompletar do Google es-ES (há gente
buscando); **A(var)** = o autocompletar sugere variações com cidade, o que indica busca local;
**–** = autocompletar vazio (sinal fraco de pouca busca); **R** = apareceu em "Otras personas
también buscan" ou "Más preguntas"; **?** = não testei. Nenhum número de volume.

### 1.1 Descoberta — o operador procura "algo novo"

| # | Consulta | Sinal |
|---|---|---|
| 1 | atracciones para centros de ocio | – |
| 2 | nuevas atracciones para centros de ocio | ? (autocompletar de "nuevas atracciones" só traz parques: PortAventura, Warner…) |
| 3 | atracciones para centros comerciales | A ("atracciones para niños en centros comerciales") |
| 4 | equipamiento para centros de ocio familiar | ? |
| 5 | centro de ocio indoor | A |
| 6 | ocio indoor + cidade | A(var) ("ocio indoor madrid") |
| 7 | atracciones novedosas centro de ocio | ? |
| 8 | ideas de negocio de ocio | A ("negocio de ocio", "como montar un negocio de ocio infantil") |
| 9 | franquicia ocio juvenil | A |
| 10 | atracción para karting indoor | ? |
| 11 | atracciones realidad virtual | A (categoria vizinha forte) |
| 12 | máquinas recreativas arcade | A ("maquinas recreativas arcade") |
| 13 | simulador de carreras para centro de ocio | ? |
| 14 | atracciones de realidad virtual en España | A |

### 1.2 Comparação — o comprador compara formatos

| # | Consulta | Sinal |
|---|---|---|
| 15 | simulador de conducción vs karting | ? |
| 16 | simulador de coches con movimiento | R |
| 17 | simulador de carreras profesional | R |
| 18 | realidad virtual o simulador para centro de ocio | ? |
| 19 | scalextric gigante vs radiocontrol | ? |
| 20 | coche rc con cámara fpv | A ("camara fpv coche rc", "kit fpv coche rc") |
| 21 | coches rc fpv | A (só a própria frase) |
| 22 | simulador radiocontrol | A ("simulador coches radiocontrol") |
| 23 | rentabilidad atracción centro de ocio | ? |

### 1.3 Compra e orçamento

| # | Consulta | Sinal |
|---|---|---|
| 24 | comprar simulador de carreras para negocio | ? (SERP traz fornecedores B2B) |
| 25 | simulador de carreras precio | R ("simulador de coches con movimiento precio") |
| 26 | proveedores de atracciones | – |
| 27 | proveedores de ocio | – |
| 28 | fabricante atracciones España | ? |
| 29 | instalaciones comerciales de simuladores | ? (RaceGear ranqueia com esse termo) |
| 30 | presupuesto atracción evento | ? |
| 31 | alquiler simulador f1 + cidade | A(var) ("madrid", "barcelona") |

### 1.4 Evento temporal, empresa e marca

| # | Consulta | Sinal |
|---|---|---|
| 32 | alquiler simuladores para eventos | A ("…madrid") |
| 33 | alquiler simulador de carreras | A |
| 34 | alquiler simuladores de conducción | A |
| 35 | simulador de carreras para eventos | A (só a frase) |
| 36 | alquiler atracciones para eventos | A ("…sevilla") |
| 37 | atracciones para eventos | A |
| 38 | atracciones para fiestas y eventos | A |
| 39 | alquiler circuito radiocontrol para eventos | – (mas a SERP é cheia de fornecedores) |
| 40 | circuito rc para eventos | – |
| 41 | alquiler scalextric gigante | A |
| 42 | actividades para eventos de empresa | A ("ideas de actividades para eventos empresariales") |
| 43 | actividades originales para empresas | A |
| 44 | eventos corporativos originales | A |
| 45 | team building + cidade | A(var) ("team building valencia", "alicante") |
| 46 | team building actividades | A |
| 47 | activaciones de marca | A ("…ejemplos", "…creativas", "…btl") |
| 48 | activaciones de marca centro comercial | – |
| 49 | experiencias para empresas | R |
| 50 | gamificación para eventos | ? (Eventoplus tem página) |

### 1.5 Ayuntamiento e festas populares

| # | Consulta | Sinal |
|---|---|---|
| 51 | ideas para fiestas de pueblo | A (muitas variações) |
| 52 | ideas originales para fiestas de pueblo | A |
| 53 | actividades para fiestas de pueblos | R |
| 54 | atracciones para fiestas patronales | – |
| 55 | actividades para ferias | A ("…de pueblo", "lúdicas para ferias") |
| 56 | espectáculos para fiestas de pueblos | R |
| 57 | ideas para comisiones de fiestas | R |

### 1.6 Competição

| # | Consulta | Sinal |
|---|---|---|
| 58 | carreras de coches radiocontrol | A |
| 59 | carreras rc + cidade | A(var) ("carreras rc madrid") |
| 60 | liga rc | A, mas as sugestões são de futebol e remo ("liga rcde", "liga rc1 de remo") |
| 61 | campeonato carreras rc fpv | ? (SERP é tomada por **drones**) |
| 62 | ranking carreras rc | ? |

### 1.7 Aficionado RC (público final, não comprador)

| # | Consulta | Sinal |
|---|---|---|
| 63 | circuito rc cerca de mi | A |
| 64 | circuito rc + cidade | A(var) (Sonseca, Toledo, Mollerussa…) |
| 65 | pista rc indoor | A |
| 66 | pista rc drift | A |
| 67 | fpv coche rc | A |
| 68 | coche rc con volante y pedales | – (mas a SERP tem Reddit, YouTube, Alibaba) |

### 1.8 Marca

| # | Consulta | Sinal |
|---|---|---|
| 69 | rc arcade | A, mas as sugestões são do **jogo de celular** |
| 70 | rcarcade | O Google corrige para "arcade" |

**Leitura do mapa (INFERÊNCIA):** o vocabulário do comprador é "**alquiler de simuladores**",
"**atracciones para eventos**", "**actividades para empresas**", "**team building**",
"**ocio indoor**". Ninguém procura "coche RC FPV con cockpit" porque a categoria é nova.
O site precisa **se apresentar como a resposta para essas buscas vizinhas**, não esperar que
procurem o nome do produto.

### 1.9 As 15+ buscas conferidas ao vivo no Google.es (27/10/2026)

"Dificuldade" aqui é **leitura qualitativa** (quem ranqueia e quão forte parece), não número.

| # | Consulta | Que tipo de página ranqueia | Quem aparece | Leitura |
|---|---|---|---|---|
| 1 | atracciones para centros de ocio | Mapa local de Valência + fabricante de parquinho + aluguel infantil + Tripadvisor | KOMPAN, amusements-park.com, fosati.com, Ilusiona, Tripadvisor ("GTC Valencia Circuito Virtual") | Intenção **mista e local, voltada ao consumidor**. Difícil e pouco útil para nós. |
| 2 | nuevas atracciones para centros de ocio indoor | Páginas de **fabricante** com lista de "atracciones novedosas" + vídeos Instagram/TikTok + mapa | Multiplay World, Beston (China), Funlandia, NinescapeLand | **Página de fabricante ranqueia.** Oportunidade média. |
| 3 | coches teledirigidos FPV atracción | Shopping, Amazon, **rcarcade.es em 1º nos resultados web**, YouTube | rcarcade.es, VelociRC, Alibaba | **Já ganhamos** (com a página antiga do cliente). |
| 4 | alquiler simuladores para eventos | **Resumo de IA** + páginas de serviço "alquiler" | Trackter, Simtechpro, HiSpeedSim, Whiplash, NLTech, Simufy (citados no resumo de IA) | Categoria vizinha, concorrida. A IA monta uma lista de fornecedores: **é aí que queremos entrar.** |
| 5 | rc arcade | rcarcade.es 1º; depois app, aRCadeRally, vídeos do jogo | — | Marca **confusa**. |
| 6 | rcarcade | "Quizás quisiste decir: arcade"; rcarcade.es, Instagram @rcarcade (116 seguidores), Facebook, **Antena 3**, rcarcade.net/.online | — | Entidade fraca, mas há prova de terceiro. |
| 7 | atracción coches radiocontrol primera persona centro de ocio | Instagram de RC Experience 4x4, blog infantil, aluguel de circuito, clubes de RC | rodamosjuntos, Club RC Silla/Olleria | **Resultados fracos = pouca concorrência.** Uma página bem feita compete. |
| 8 | actividades originales para eventos de empresa | **Listas** ("30 ideas…", "60 ideas…") de blogs + anúncios | Naboo, WhiteLion, Tuset Eventos, Cripthos (anúncio) | Difícil ranquear. **Melhor ser citado dentro dessas listas** (seção 5). |
| 9 | alquiler circuito coches radiocontrol para eventos | **Páginas de serviço** de fornecedores pequenos | rodamosjuntos, alquilarscalextric, **warmuplap (2x)**, podiumslot, moaeventos, kleemeventos | Concorrentes diretos e pequenos. **Ganhável** com página dedicada. |
| 10 | activaciones de marca centro comercial experiencia | Agências + blogs de marketing + imprensa de retail | Staff Global Group, Solucionic, HubSpot, P&P Medios, Retail Actual | Difícil. O canal é **a agência**, não o Google. |
| 11 | equipamiento para centros de ocio familiar FEC | Fabricantes chineses traduzidos | farkidsisland, KanbeiPlay, NanPlay, isunhong, Didi Land | Página de produto B2B ranqueia; concorrência de **baixa qualidade**. Oportunidade. |
| 12 | coche rc con volante y pedales fpv | Reddit, Hobbyking, Alibaba, vídeo de youtuber | Valderrey (vídeo na E1RC), Alibaba "1:28 FPV… Equipo Comercial" | Mostra que **kits chineses prontos existem** (ameaça). |
| 13 | atracciones para fiestas patronales ayuntamientos novedad | Agências de espetáculo com listas de ideias | ShowFlow, Espectáculos Vértigo, ViveJuego, Max Fun | O ayuntamiento compra **por agência**. Canal indireto. |
| 14 | competición carreras coches rc fpv liga ranking | Rankings de **drones** FPV | FPVGames, MultiGP, CDG FPV | "FPV" sozinho = drone. **Sempre escrever "coches RC" junto.** |
| 15 | comprar simulador de carreras para centro de ocio negocio | Mapa local (simuladores em Valência) + fornecedores de simracing | RaceGear, HiSpeedSim, Simtechpro, fbrand, ESTech | É o orçamento que disputamos. |
| 16 | equipamiento… / FPV RC car racing attraction for entertainment centers (inglês) | Quase só **vídeo social** (TikTok, Instagram, LinkedIn) | Racetech, MIXR XR, VBR Racezone, fábricas chinesas | Lá fora a categoria se vende **por vídeo curto**. |
| 17 | (Modo IA) "¿Qué empresas en España ofrecen una atracción de carreras de coches radiocontrol reales con cámara FPV y puestos con volante…?" | Resposta gerada | **RC Arcade em 1º** (fonte: rcarcade.es + Instagram), E1RC, WarmUp Lap, Rodamos Juntos, MOA, Simtechpro | Quem descreve o produto **acha** o RC Arcade. |
| 18 | (Modo IA) "Gestiono un centro de ocio en España y busco una atracción nueva…" | Resposta gerada | Aventura indoor, *Prison Island*, VR *free-roaming*, tiro de machado. **RC Arcade ausente.** | A categoria "carreras RC em FPV" **ainda não existe** na cabeça da IA. É o trabalho de GEO. |

Fontes desta tabela: buscas feitas em `google.es` com `hl=es&gl=es` em 27/10/2026; os
resultados mudam com o tempo e o lugar.

---

## 2. Arquitetura de páginas

### 2.1 Princípio

- **Uma página para cada pergunta de compra.** O operador de centro de ocio e o organizador de
  evento querem coisas diferentes (fixo × temporário). Numa página única, o Google não sabe
  para qual busca mostrar.
- **Poucas páginas, densas.** O guia de IA do Google avisa contra "large numbers of pages"
  feitas para manipular resultados (política de *scaled content abuse*).
  [Google: AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) — CONFIRMADO.
- **Nada de página com texto inventado.** Página sem dado real (m², preço, local) fica para
  depois. Isso segue a regra de honestidade da base.

### 2.2 Mapa proposto (no domínio `rcarcade.es`)

```
rcarcade.es/                         Início (hub)
├── /como-funciona/                  Os 4 passos + tecnologia (FPV, circuito, cronometragem)
├── /centros-de-ocio/                Instalação fixa  (via principal, premissa a confirmar)
├── /eventos/                        Evento temporal: feiras, festivais, ativações, empresas
├── /competicion/                    Ligas, rankings, finais
├── /video/                          Página do vídeo real com telemetria
├── /preguntas-frecuentes/           FAQ
├── /presupuesto/                    Pedido de proposta (os "cinco datos" do cliente)
├── /prensa/                         Só depois de o cliente confirmar El Hormiguero
└── /aviso-legal/ /privacidad/ /cookies/
```

**Fase 2, só se houver dado real:** `/eventos/empresas/` (team building) e
`/eventos/activaciones-de-marca/`, quando existir um caso real de cada; uma página de local
aberto ao público, se o cliente tiver um.

### 2.3 Title, meta description e H1 de cada página

O Google **não dá limite oficial** para o `<title>`; ele corta conforme a largura da tela.
[Google: title links](https://developers.google.com/search/docs/appearance/title-link) —
CONFIRMADO. Os tamanhos abaixo (cerca de 50–60 caracteres no título, 130–160 na descrição)
são **convenção de mercado** para não cortar — **INFERÊNCIA**. Contei os caracteres de cada um.

| URL | `<title>` (caracteres) | Meta description (caracteres) | H1 |
|---|---|---|---|
| `/` | RC Arcade \| Atracción de carreras RC en primera persona (55) | Coches radiocontrol reales, cámara FPV y puestos con volante y pedales en un circuito físico. Hasta 6 pilotos a la vez. Para centros de ocio y eventos. (151) | No miras la carrera. Estás dentro de ella. |
| `/como-funciona/` | Cómo funciona RC Arcade: coche real, cámara FPV y cockpit (57) | Elige, siéntate, conduce y compite: así funciona una carrera de coches RC reales pilotados desde un cockpit con cámara en primera persona y tiempos medidos. (156) | Cómo funciona: un coche real, visto desde dentro |
| `/centros-de-ocio/` | Atracción para centros de ocio: carreras RC FPV \| RC Arcade (59) | Atracción fija para centros de ocio y espacios comerciales: coches RC reales, hasta 6 puestos de pilotaje y ranking por tiempos. Compacto o completo. (149) | Una atracción fija para tu centro de ocio |
| `/eventos/` | Carreras RC para eventos, ferias y empresas \| RC Arcade (55) | Circuito de coches radiocontrol con cámara FPV para ferias, festivales, activaciones de marca y eventos de empresa. Con equipo técnico propio. (≈143) | Carreras RC en primera persona para tu evento |
| `/competicion/` | Ligas y rankings de carreras RC en FPV \| RC Arcade (50) | Formato competición: carreras por vueltas, contrarreloj y equipos, con tiempos y posiciones medidos en directo. Para ligas, rankings y finales en tu espacio. (157) | Ligas, rankings y finales |
| `/video/` | Vídeo de una carrera real con telemetría \| RC Arcade (52) | Mira una sesión real: el piloto conduce un coche RC desde el cockpit viendo la cámara del coche, con tiempo de vuelta, señal y voltaje en pantalla. (147) | Una carrera real, vista desde el cockpit |
| `/preguntas-frecuentes/` | Preguntas frecuentes sobre la atracción RC Arcade (49) | Espacio necesario, número de pilotos, montaje, operación y formatos: respuestas para operadores de ocio y organizadores de eventos. (131) | Preguntas frecuentes |
| `/presupuesto/` | Pide propuesta para tu espacio o evento \| RC Arcade (51) | Cuéntanos tipo de espacio o evento, ubicación y fechas, público, duración y personalización. Con esos cinco datos preparamos una primera propuesta. (147) | Pide una propuesta |
| `/prensa/` | RC Arcade en los medios: El Hormiguero y más (44) | Apariciones de RC Arcade en televisión y prensa, con enlaces a las piezas originales. Material de prensa y contacto para medios. (128) | RC Arcade en los medios |

Cuidados com os textos acima:
- "Hasta 6 pilotos", "4 pasos", "compacto/completo", "por vueltas, contrarreloj, equipos" e
  "equipo técnico" vêm do dossiê ou do site do cliente. Nada de preço, m² ou local.
- "Con equipo técnico propio" vem da página do cliente ("El equipo RCArcade instala,
  configura y prueba…"), mas ela fala de **evento**. **NÃO VERIFICADO** se vale também para a
  instalação fixa; por isso só aparece em `/eventos/`.
- A FAQ só entra no ar com as respostas que o cliente confirmar (m², idades, montagem).
- O H1 da home mantém a frase do cliente; o título da aba carrega a palavra-chave. Assim a
  marca fica e a busca entende (**INFERÊNCIA**).

### 2.4 Dados estruturados (schema.org): o que o Google ainda usa

Conferido na galeria oficial, atualizada em 16/10/2026.
[Google: search gallery](https://developers.google.com/search/docs/appearance/structured-data/search-gallery) — CONFIRMADO.

| Tipo | Gera resultado especial no Google hoje? | Usar onde | Observação |
|---|---|---|---|
| `Organization` | **Sim** (logo, nome, contato no painel) | Home | Com `name`, `url`, `logo`, `sameAs` (Instagram, Facebook, YouTube). Ajuda a separar o RC Arcade do app homônimo (**INFERÊNCIA**). |
| `WebSite` | Sim (nome do site) | Home | Fixa o nome "RC Arcade". |
| `BreadcrumbList` | **Sim** | Todas as subpáginas | Barato e útil. |
| `VideoObject` | **Sim** | Só em `/video/` | Obrigatórios: `name`, `thumbnailUrl`, `uploadDate`. `contentUrl` ou `embedUrl`. [Google: video structured data](https://developers.google.com/search/docs/appearance/structured-data/video) — CONFIRMADO. |
| `FAQPage` | **Não. Deixou de aparecer em 07/05/2026**; a documentação foi removida em 15/06/2026. | Opcional | A FAQ **visível** continua valendo para pessoas e IA. A marcação não dá mais nada no Google. [Google: updates](https://developers.google.com/search/updates) — CONFIRMADO. |
| `Product` | Só com `offers`, `review` ou `aggregateRating` | **Não usar agora** | Não temos preço nem avaliação. "Product snippets require either review or aggregateRating or offers". [Google: product snippet](https://developers.google.com/search/docs/appearance/structured-data/product-snippet) — CONFIRMADO. |
| `Service` | **Não está na galeria** | Opcional em `/centros-de-ocio/` e `/eventos/` | Não gera nada visual no Google. Pode ajudar outros sistemas a entender (**INFERÊNCIA**). O WarmUp Lap usa. |
| `Event` | Sim | Só para competição real, com data e local | Nunca evento inventado. |
| `LocalBusiness` | Sim | Só se houver local aberto ao público | Dado que falta. |

O Google diz que **nenhum schema especial é necessário** para aparecer nos recursos de IA, mas
que vale para resultados ricos.
[Google: AI features](https://developers.google.com/search/docs/appearance/ai-features) —
CONFIRMADO.

---

## 3. Busca por IA (GEO)

### 3.1 O que o Google diz oficialmente (CONFIRMADO)

Do guia de IA do Google (atualizado em 10/07/2026)
[developers.google.com/…/ai-optimization-guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
e da página de recursos de IA
[developers.google.com/…/ai-features](https://developers.google.com/search/docs/appearance/ai-features):

- **Não há truque especial.** "There are no additional requirements to appear in AI Overviews
  or AI Mode." O que vale é estar indexado e elegível para aparecer com trecho.
- O Google chama AEO/GEO de **SEO** e lista **5 mitos** que dá para ignorar no Google:
  `llms.txt` e marcações "especiais"; picotar o texto em pedaços ("chunking"); reescrever para
  IA; caçar **menções falsas**; exagerar em dados estruturados.
- O que ele pede: conteúdo **"non-commodity"** (experiência de primeira mão, ponto de vista
  próprio), boas imagens e vídeo, estrutura técnica limpa, Search Console verificado.
- O IA do Google trabalha por **"query fan-out"**: faz várias buscas relacionadas para uma
  pergunta. Ou seja, **as buscas vizinhas da seção 1 alimentam a resposta da IA**.

### 3.2 `llms.txt`: a ressalva

- É uma proposta de Jeremy Howard (setembro de 2024), não um padrão de buscador.
  [llmstxt.org](https://llmstxt.org/) — CONFIRMADO.
- **O Google Search ignora.** Changelog de 15/06/2026: esses arquivos "aren't needed for Google
  Search (and won't negatively or positively impact your visibility or rankings)", mas "it's
  fine if you want to maintain these files for other services".
  [Google: updates](https://developers.google.com/search/updates) — CONFIRMADO.
- **Recomendação:** custo de 10 minutos, sem efeito no Google. Fazer **por último**, se sobrar
  tempo. Não é prioridade.

### 3.3 Robôs das IAs: deixar entrar (CONFIRMADO)

| Robô | Para quê | Fonte |
|---|---|---|
| `OAI-SearchBot` | Aparecer nas respostas com busca do ChatGPT. Quem bloqueia não aparece. | [OpenAI bots](https://developers.openai.com/api/docs/bots) |
| `GPTBot` | Treino de modelo. Independente do de busca. | idem |
| `ChatGPT-User` | Visita quando um usuário pede; não decide se aparece. | idem |
| `PerplexityBot` | Aparecer no Perplexity. A Perplexity recomenda liberar. | [Perplexity bots](https://docs.perplexity.ai/guides/bots) |
| `Google-Extended` | Uso em treino/Gemini. **Não** afeta o Google Search. | [Google AI features](https://developers.google.com/search/docs/appearance/ai-features) |

Para um fabricante que **quer ser citado**: liberar todos no `robots.txt`. Bloquear o
`GPTBot` (treino) é escolha do cliente; não afeta a busca do ChatGPT.

### 3.4 O que faz um fabricante pequeno ser citado (com o que vimos hoje)

1. **Estar indexado no domínio que a IA já conhece.** O Modo IA citou `rcarcade.es`, não o
   `github.io` (CONFIRMADO, teste 17). Daí a decisão D1.
2. **Uma frase-definição, no topo, que a IA possa copiar.** Exemplo (dados do dossiê):
   *"RC Arcade es una atracción de carreras con coches radiocontrol reales: cada piloto
   conduce desde un puesto con volante, pedales y pantalla, viendo la cámara del coche en
   primera persona, sobre un circuito físico. Hasta seis pilotos compiten a la vez, con tiempo
   de vuelta y posición medidos."*
3. **Números que só nós temos.** Hoje: até 6 simuladores, configuração habitual de 4 a 6 postos,
   4 passos, 2 escalas, 3 vias, 4 formatos, 5 dados para a proposta, a telemetria do vídeo
   (12.3 V, 25 Mbps, melhor volta 00:42.381). **Falta o que o comprador e a IA perguntam:** no
   teste 17, o próprio Modo IA terminou perguntando "¿De qué espacio en metros cuadrados
   dispones?". Sem m², tempo de montagem e pessoal necessário, a resposta fica com o
   concorrente (o WarmUp Lap publica "de 2×3 m" a formatos grandes). **Pedir ao cliente.**
4. **Comparação honesta da categoria.** A IA respondeu ao gestor de ocio com uma tabela de
   categorias (VR, aventura, tiro de machado). Uma página que compare **RC Arcade × simulador ×
   karting × scalextric × VR** em critérios verificáveis (coche real ou virtual, nº de pilotos,
   público que assiste) dá à IA a peça que falta para incluir a categoria. O cliente já tem uma
   tabela "RCArcade vs Simulador" no site dele. (**INFERÊNCIA** de que isso aumenta a
   chance de ser citado; não há garantia.)
5. **Menções reais de terceiros.** O Google diz que a IA "can reflect what is said about your
   brand across the web", mas que menção fabricada não funciona. A do El Hormiguero é real.
   Ver seção 5.
6. **Bing conta para o Copilot.** O Bing Webmaster Tools tem um relatório "AI Performance"
   (citações no Copilot e nos resumos de IA do Bing, e "grounding queries").
   [Practical Ecommerce, 22/06/2026](https://www.practicalecommerce.com/bings-improved-ai-performance-section)
   — CONFIRMADO pela matéria; o anúncio oficial da Microsoft **não foi aberto**.
7. **Texto no HTML, não dentro de imagem ou só de animação.** O Google pede "keeping important
   content in text". Os números do HUD do nosso site precisam existir também como texto
   legível (já existem na lista de telemetria de "La prueba" — manter).

### 3.5 Checklist prático de GEO

- [ ] Site novo no `rcarcade.es`, indexado, com Search Console e Bing verificados.
- [ ] `robots.txt` liberando Googlebot, Bingbot, OAI-SearchBot, PerplexityBot.
- [ ] Frase-definição no início da home e de `/como-funciona/`.
- [ ] Uma grafia só: "RC Arcade", sempre com o descritor perto.
- [ ] `Organization` com `sameAs` para os perfis oficiais.
- [ ] FAQ visível com respostas curtas e diretas (sem marcação obrigatória).
- [ ] Página `/video/` com vídeo, transcrição curta e legenda.
- [ ] Números reais em texto; os que faltam, pedidos ao cliente.
- [ ] `/prensa/` com link para a Antena 3 (depois da confirmação).
- [ ] Teste mensal de perguntas nas IAs (seção 6).
- [ ] `llms.txt`: opcional, por último.

---

## 4. SEO técnico

### 4.1 Domínio

- **Usar `rcarcade.es`** (já existe, já ranqueia, é o que o Modo IA cita). CONFIRMADO que existe
  e está indexado; **NÃO VERIFICADO** quem é o dono do registro e quem controla o DNS: o
  Diogo precisa de acesso, ou o cliente faz a troca.
- **Escolher uma versão** (sugestão: `https://www.rcarcade.es/` ou sem `www`; tanto faz, desde
  que seja uma) e **redirecionar 301** as outras três, inclusive o `.com`. Hoje as quatro
  servem a mesma página: o Google pode dividir os sinais entre elas (**INFERÊNCIA**; o próprio
  Google recomenda reduzir conteúdo duplicado no guia de IA).
- **`.es` × `.com`:** para um mercado só na Espanha, `.es` diz "Espanha" a pessoas e ao Google.
  O `.com` fica como redirecionamento, útil se um dia houver versão internacional
  (**INFERÊNCIA**).
- **A página antiga do cliente vai embora com 301 para a home nova.** O conteúdo dela é bom
  e deve ser **aproveitado** nas páginas novas (formatos, processo, cinco dados).

### 4.2 Onde hospedar

- **GitHub Pages aceita domínio próprio** (apex e `www`; recomenda configurar os dois e
  verificar o domínio para evitar sequestro).
  [GitHub: custom domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages) — CONFIRMADO.
- **Ressalva:** o GitHub diz que o Pages não é feito para servir como hospedagem grátis de
  negócio online ou de transações comerciais; limite de 1 GB por site e 100 GB/mês de banda.
  [GitHub: limits](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits)
  — CONFIRMADO. Um site institucional sem venda não é "transação", mas é zona cinzenta
  (**INFERÊNCIA**). O cliente **já paga um Apache** (onde está o `rcarcade.es`); subir os
  arquivos lá é a saída mais simples. Decisão do Diogo com o cliente.
- **Hoje, no `github.io`:** o `robots.txt` só vale na raiz do host
  (`diogotorresweb.github.io/robots.txt`, que responde 404). Na pasta `/rc-arcade/` não dá para
  controlar. Mais um motivo para o domínio próprio (**INFERÊNCIA** a partir do 404 conferido).
- **Durante a construção**, se o `github.io` continuar como prévia, colocar
  `<meta name="robots" content="noindex">` nele, para não virar cópia do site oficial.

### 4.3 Idioma (hreflang)

- **Agora: não usar.** Só existe espanhol. `hreflang` serve para várias versões de idioma e
  exige que cada versão aponte para todas as outras, senão o Google ignora.
  [Google: localized versions](https://developers.google.com/search/docs/specialty/international/localized-versions) — CONFIRMADO.
- Manter `<html lang="es">` (já está). O Google não usa esse atributo para decidir o idioma,
  mas é correto para acessibilidade.
- **Inglês só se** o cliente quiser vender fora (feira IAAPA, concorrência da Racetech). Aí:
  `/en/` com hreflang `es`, `en` e `x-default`.

### 4.4 Velocidade, vídeo e Core Web Vitals

Metas oficiais (percentil 75 das visitas): **LCP ≤ 2,5 s**, **INP ≤ 200 ms**, **CLS ≤ 0,1**.
[web.dev/vitals](https://web.dev/articles/vitals) — CONFIRMADO.

O que vi no nosso `index.html` (CONFIRMADO no arquivo):
- Imagens já em `srcset`, `preload` do topo, fontes locais com `font-display: swap`, `loading="lazy"`
  em "La prueba". A pasta `assets/` tem 1,9 MB no total. Bom ponto de partida.
- A maior imagem é `hero-2560.jpg` (544 KB). Para telas grandes, vale testar WebP/AVIF
  (**INFERÊNCIA**).

Para o vídeo (o ativo mais forte):
- **Vídeo longo no YouTube**, embutido com "fachada" (uma imagem com botão de play, e o
  player só carrega no clique). Assim o vídeo não pesa no carregamento inicial nem trava o
  clique (**INFERÊNCIA**, prática comum para LCP e INP).
- **Vídeo de fundo do topo** (quando o cliente mandar o clipe): curto, sem som, comprimido,
  com imagem de capa (`poster`) que vira o elemento de LCP (**INFERÊNCIA**).
- O **scroll com o carro descendo** (ideia em `TASKS.md`) é o maior risco para INP e CLS: animar
  só `transform` e `opacity`, nada que mexa no layout, e respeitar "reduced motion" (o código já
  faz isso em outros pontos) (**INFERÊNCIA**).

### 4.5 Open Graph e cartões sociais

- **Hoje não existe nenhuma tag `og:` nem `twitter:`** no `index.html` (CONFIRMADO, contei 0).
  Quando alguém mandar o link no WhatsApp ou LinkedIn, sai sem imagem.
- Adicionar em cada página: `og:title`, `og:description`, `og:image` (1200×630, com o carro e
  o logo), `og:url`, `og:type`, `og:locale` = `es_ES`, `twitter:card` = `summary_large_image`.
- Também faltam `<link rel="canonical">` e favicon (CONFIRMADO, 0 no arquivo).

### 4.6 Antes de indexar: limpar o que é interno

O site no ar mostra texto de bastidor, o que derruba a confiança de um comprador e do Google
(CONFIRMADO no arquivo): "Lo que todavía falta del cliente", menções a `TASKS.md` e
`ESTRUTURA-DO-SITE.md`, e o rodapé "Borrador · 24.09.2026". **Tirar antes de apontar o
domínio.**

### 4.7 Sitemap, Search Console, Bing

- `sitemap.xml` com as ~8 páginas e a página de vídeo (pode ser um sitemap de vídeo; o `<loc>`
  é a página de vídeo). [Google: video SEO](https://developers.google.com/search/docs/appearance/video) — CONFIRMADO.
- **Search Console:** propriedade de **domínio** (verificação por DNS), envio do sitemap,
  inspeção das URLs principais. O tráfego de AI Overviews e Modo IA entra no relatório
  "Performance", tipo "Web"; o guia novo cita também um relatório de desempenho de IA
  generativa. [Google: AI features](https://developers.google.com/search/docs/appearance/ai-features) e
  [AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) — CONFIRMADO.
- **Bing Webmaster Tools:** importar do Search Console; ver o relatório "AI Performance".

### 4.8 Google Business Profile

- Só pode ter perfil quem atende o cliente **presencialmente**: local que o cliente visita, com
  equipe no horário, **ou** empresa que vai até o cliente (área de atendimento, com endereço
  oculto, em geral até 2 h de carro). Escritório virtual não pode.
  [Google: diretrizes do Perfil](https://support.google.com/business/answer/3038177?hl=es) — CONFIRMADO.
- Para o RC Arcade: **depende de dado que falta.** Se houver pista aberta ao público, perfil
  com endereço. Se só monta em evento, talvez "área de atendimento". Se for só fabricante/
  vendedor, provavelmente não se encaixa (**INFERÊNCIA**). Perguntar ao cliente.
- Por que importa: nas buscas 1, 2 e 15 o **mapa local aparece antes** dos resultados web.

---

## 5. Conteúdo e links que mexem o ponteiro num nicho pequeno

### 5.1 Conteúdo (em ordem de impacto, INFERÊNCIA)

1. **O vídeo real, com página própria e canal no YouTube.** No YouTube, buscar "RC Arcade" hoje
   traz o jogo *Go By RC* (CONFIRMADO via busca do YouTube). O campo está vazio. Título em
   espanhol com as palavras de busca, p. ex.: *"Carrera de coches RC en primera persona, con
   volante y pedales | RC Arcade"*. Descrição com a frase-definição e link para `/video/`.
   Capítulos com tempo na descrição (o Google usa para "momentos-chave").
   [Google: video SEO](https://developers.google.com/search/docs/appearance/video) — CONFIRMADO.
2. **Vídeos curtos** (Instagram/TikTok/Shorts). Nas buscas 2, 3, 7 e 16, o Google mostrou
   carrossel de vídeos de Instagram e TikTok (CONFIRMADO). Lá fora, os concorrentes vendem a
   categoria assim.
3. **Casos reais**, um por evento, com data, lugar, nº de participantes e fotos — **só com dado
   do cliente**. Candidatos: El Hormiguero (07/10/2026), a "Jornada de puertas abiertas" e o
   "Open RC Arcade" de julho de 2026 que aparecem nas pastas do Dropbox (nomes vistos no
   inventário; **NÃO VERIFICADO** o que foram).
4. **Comparativo da categoria** (ver 3.4, item 4).
5. **Guia** "Cómo elegir una atracción para un centro de ocio: espacio, rotación y público" —
   só se tiver dado próprio; guia genérico é exatamente o "commodity content" que o Google
   diz não valer.

### 5.2 Onde conseguir menção (todos abertos ou vistos hoje)

| Lugar | O que é | Como usar | Status |
|---|---|---|---|
| **Antena 3 / El Hormiguero** | Matéria de 07/10/2026 citando "RC Arcade" | Citar em `/prensa/`; o cliente pode pedir o link à produção (difícil, **INFERÊNCIA**) | CONFIRMADO ([link](https://www.antena3.com/programas/el-hormiguero/espectacular-carrera-coches-radio-control-pablo-motos-david-bustamante_202610076ac6b6af48d2d008d0c92c53.html)) |
| **FIOCIO** (Feria Valencia) | "La única feria en España, profesional e internacional del sector de ocio y del entretenimiento familiar". Última edição: 17–19/02/2026, Pavilhão 8. **Próxima: 2028** (sem data). Visitantes incluem centros de ocio, organizadores de eventos e **ayuntamientos**. | Expositor em 2028; página de notícias para nota de imprensa | CONFIRMADO ([fiocio.com](https://www.fiocio.com/)) |
| **IAAPA Expo Europe** | Feira europeia de atrações. 2027: 20–24/09, Viena. | Só se o cliente mirar fora da Espanha | CONFIRMADO ([iaapa.org](https://iaapa.org/expos-and-events/expo-europe)) |
| **Revista Centros Comerciales** | Meio oficial da AECC (centros e parques comerciais) desde 1980; publica sobre ocio em shopping | Nota de imprensa / artigo de opinião com caso real | CONFIRMADO ([revistacentroscomerciales.com](https://revistacentroscomerciales.com/)) |
| **AECC** | Associação Espanhola de Centros e Parques Comerciais | Associar-se / eventos do setor | Visto na SERP ([aedecc.com](https://www.aedecc.com/quienes-somos)); página **não aberta** |
| **AEPA** | Associação Espanhola de Parques de Atrações e Temáticos | Contato setorial | Visto na SERP ([aepa.es](http://www.aepa.es)); página **não aberta** |
| **Eventoplus** | Diretório de fornecedores de eventos com categoria "Actividades y Team Building" e páginas por cidade | Ficha de fornecedor: é o canal das agências | Visto na SERP ([eventoplus.com/directorio](https://www.eventoplus.com/directorio)); página **não aberta**, preço da ficha **NÃO VERIFICADO** |
| **Hi Retail** | Portal de retail; publicou em 24/09/2026 que ocio e entretenimento lideram o crescimento das vendas dos centros comerciais | Nota de imprensa; argumento de venda | Visto na SERP; página **não aberta** |
| **Listas "ideas para eventos de empresa"** | Naboo, WhiteLion, Tuset, Auditorio Cartuja | Pedir inclusão quando houver caso real | Vistos na SERP (busca 8) |
| **Alejandro Valderrey** (YouTube) | Youtuber de RC que já gravou um circuito FPV com volante | Convidar para gravar no RC Arcade | Vídeo CONFIRMADO via `yt-dlp`; contato **não buscado** |

Regra: **só menção verdadeira.** O Google diz que menção fabricada não funciona e que as
regras de spam valem para as respostas de IA.
[Google: AI optimization guide](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) — CONFIRMADO.

---

## 6. Plano de medição: os primeiros 90 dias, só com ferramenta grátis

### 6.1 Ferramentas e privacidade (RGPD/LSSI)

| Ferramenta | Para quê | Precisa de consentimento de cookies? |
|---|---|---|
| **Google Search Console** | Indexação, buscas, cliques, relatório de IA | Não: não instala nada no site |
| **Bing Webmaster Tools** | Bing + citações no Copilot ("AI Performance") | Não |
| **Microsoft Clarity** | Mapa de calor, gravação | **Sim.** Desde 31/10/2025 exige sinal de consentimento para visitantes do EEE, Reino Unido e Suíça. [Microsoft: consent mode](https://learn.microsoft.com/en-us/clarity/setup-and-installation/cookie-consent) — CONFIRMADO |
| **GA4** | Visitas e conversões | **Sim**, na leitura da AEPD: só fica isenta a medição de audiência feita **exclusivamente em nome do editor**, com dados estatísticos anônimos, **sem passar dados a terceiros** nem cruzar sites. [AEPD, guia de medição de audiência, jan/2024](https://www.aepd.es/guias/guia-cookies-analiticas-externas.pdf) — CONFIRMADO o texto. Que o GA4 não cumpra isso é **INFERÊNCIA** (envia dados ao Google). |

**Recomendação para começar (INFERÊNCIA):** dias 1–90 só com Search Console + Bing (zero
cookie, zero banner). Contar pedidos de proposta pelo próprio formulário/e-mail. Clarity ou
GA4 só depois, com banner que tenha "Rechazar" na primeira camada. O botão de recusa
obrigatório na primeira camada vem de resumo de blog da guia da AEPD de 2023 — **NÃO
VERIFICADO** no texto oficial. Aviso legal, política de privacidade e de cookies (exigidos pela
LSSI e RGPD) devem ser revisados por quem entende de direito; **não verifiquei** os artigos.

### 6.2 Calendário

| Quando | O que fazer | Como saber que deu certo (sem número inventado) |
|---|---|---|
| Semana 0 | **Linha de base:** print das 18 buscas da tabela 1.9 e dos 2 testes do Modo IA; Search Console do `rcarcade.es` (se o cliente der acesso) | Arquivo de base salvo com data |
| Semana 1–2 | Site no domínio, 301 das 4 versões, sitemap enviado ao Google e ao Bing, `robots.txt` | Todas as URLs "Indexada" na inspeção do Search Console |
| Semana 2–4 | Vídeo no YouTube + `/video/`; perfis sociais ligados no `sameAs` | Vídeo aparece no relatório de vídeo do Search Console |
| Mês 1 | Primeiro teste de IA (abaixo) | Comparar com a base |
| Mês 2 | 1 caso real publicado; ficha no Eventoplus; nota à revista da AECC | Cada menção nova anotada com link |
| Mês 3 | Revisão: que buscas trouxeram impressões, quais páginas, quais citações no Bing | Decidir quais páginas da fase 2 valem a pena |

### 6.3 O que acompanhar

- **Impressões de busca sem a marca** (filtrar "rc arcade" fora no Search Console): é o sinal de
  que o site está sendo achado por quem **não conhecia** o RC Arcade.
- **Consultas novas** que aparecem (o vocabulário real do comprador; corrige a seção 1).
- **Pedidos de proposta** e cliques em e-mail/telefone, contados à mão.
- **Citações de IA:** relatório do Bing + teste manual mensal.

### 6.4 Teste manual mensal nas IAs (o Diogo faz em 15 minutos)

Mesmas perguntas, sempre, em Modo IA do Google, ChatGPT (com busca) e Perplexity. Anotar:
o RC Arcade aparece? Com que link? Diz algo errado?

1. ¿Qué empresas en España ofrecen una atracción de carreras de coches radiocontrol reales con cámara FPV y volante?
2. Gestiono un centro de ocio en España y busco una atracción nueva y diferente. ¿Qué opciones hay y qué proveedores?
3. Busco una actividad original para un evento de empresa de 50 personas en Valencia.
4. ¿Qué atracciones puedo alquilar para una feria o un festival?
5. Ideas originales para las fiestas de un pueblo.
6. ¿Qué es RC Arcade?
7. Alternativas a los simuladores de F1 para eventos.
8. ¿Cuánto espacio necesita una atracción de carreras RC con cockpit? (mostra se a IA inventa m²)

**Metas realistas sem número inventado:** em 90 dias, (a) todas as páginas indexadas no
domínio certo; (b) a busca da marca mostrando só o site oficial no topo, sem duplicata; (c)
impressões, mesmo poucas, em buscas sem a marca do grupo "eventos"; (d) pelo menos uma menção
nova e real com link; (e) o RC Arcade aparecendo na pergunta 1 em mais de uma IA e, idealmente,
entrando na pergunta 2. Quanto tráfego isso dá **não dá para prever** sem volume de busca.

---

## Fontes abertas

**Documentação oficial**
- Google — AI optimization guide (10/07/2026): https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- Google — AI features and your website (10/12/2025): https://developers.google.com/search/docs/appearance/ai-features
- Google — Search updates / changelog (FAQ removido, llms.txt): https://developers.google.com/search/updates
- Google — Structured data search gallery (16/10/2026): https://developers.google.com/search/docs/appearance/structured-data/search-gallery
- Google — FAQPage (removido): https://developers.google.com/search/docs/appearance/structured-data/faqpage
- Google — Video structured data (24/09/2026): https://developers.google.com/search/docs/appearance/structured-data/video
- Google — Video SEO best practices (18/12/2025): https://developers.google.com/search/docs/appearance/video
- Google — Product snippet: https://developers.google.com/search/docs/appearance/structured-data/product-snippet
- Google — Title links: https://developers.google.com/search/docs/appearance/title-link
- Google — Localized versions / hreflang (21/09/2026): https://developers.google.com/search/docs/specialty/international/localized-versions
- Google — Diretrizes do Perfil de Empresa: https://support.google.com/business/answer/3038177?hl=es
- web.dev — Core Web Vitals: https://web.dev/articles/vitals
- OpenAI — Bots: https://developers.openai.com/api/docs/bots
- Perplexity — Bots: https://docs.perplexity.ai/guides/bots
- llms.txt — proposta: https://llmstxt.org/
- GitHub — Custom domains: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages
- GitHub — Pages limits: https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits
- Microsoft Clarity — Consent mode: https://learn.microsoft.com/en-us/clarity/setup-and-installation/cookie-consent
- AEPD — Guía uso de cookies para herramientas de medición de audiencia (jan/2024): https://www.aepd.es/guias/guia-cookies-analiticas-externas.pdf

**Cliente, imprensa e concorrência**
- rcarcade.es (página do cliente): https://www.rcarcade.es
- rcarcade.com (cópia): https://rcarcade.com
- Antena 3 / El Hormiguero, 07/10/2026: https://www.antena3.com/programas/el-hormiguero/espectacular-carrera-coches-radio-control-pablo-motos-david-bustamante_202610076ac6b6af48d2d008d0c92c53.html
- WarmUp Lap / RC Racing Experience: https://warmuplap.es/circuito-rc-para-eventos
- Vídeo de Alejandro Valderrey (15/07/2026): https://www.youtube.com/watch?v=kpjndjEh1KQ
- FIOCIO: https://www.fiocio.com/
- IAAPA Expo Europe: https://iaapa.org/expos-and-events/expo-europe
- Revista Centros Comerciales (AECC): https://revistacentroscomerciales.com/
- Bing AI Performance (matéria): https://www.practicalecommerce.com/bings-improved-ai-performance-section
- Google.es ao vivo, 18 buscas e 2 do Modo IA, 27/10/2026 (`hl=es&gl=es`, localizado em Valência)
- Autocompletar do Google es-ES (`suggestqueries.google.com`, `hl=es&gl=es`), ~60 sementes

## O que NÃO foi verificado

- **Volume de busca, CPC e dificuldade** de qualquer termo. Nenhum número aqui.
- Que o "RC Arcade" do *El Hormiguero* seja **o mesmo** cliente (INFERÊNCIA forte).
- Se o **e-mail e os telefones** da página `rcarcade.es` continuam valendo para o site novo.
- **Quem controla** o domínio `rcarcade.es`/`.com` e o servidor (só vi que é Apache, IPs 217.76.x).
- Resultados do **ChatGPT e do Perplexity** (Perplexity pediu verificação anti-robô; não contornei).
- Resultados do Google **fora de Valência** (Madrid, Barcelona).
- Se a **E1RC** (Gijón) opera de fato um circuito FPV aberto ao público (a home da loja não fala disso).
- Os perfis **Instagram @rcarcade** e **Facebook rcarcade** (vistos só como resultado do Google).
- As páginas da **AECC, AEPA, Eventoplus e Hi Retail** (vistas só na lista de resultados) e o preço da ficha do Eventoplus.
- O anúncio **oficial** da Microsoft sobre o relatório "AI Performance" do Bing.
- O texto oficial da guia geral de cookies da AEPD (2023) sobre o botão "Rechazar"; os artigos da **LSSI** sobre aviso legal.
- Se configurar domínio próprio no GitHub Pages **redireciona** o endereço `github.io` (a página do GitHub aberta não fala disso).
- A premissa de que **instalação fixa** é a via principal (segue não confirmada por escrito pelo cliente).
