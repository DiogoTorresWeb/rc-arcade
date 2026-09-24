# Direção de arte V2 — crítica profunda e plano de evolução

Escrito em 24/09/2026, a pedido explícito do Diogo: elevar o projeto de "bom
front-end" pra "direção de arte profissional". **Nenhum código foi alterado
pra produzir este documento** — é só diagnóstico e plano. Metodologia: (1) ler
o `index.html` inteiro linha a linha, (2) abrir o site publicado ao vivo
(`diogotorresweb.github.io/rc-arcade`) e capturar screenshot real de cada
seção em mobile, (3) **raspar `racing.porsche.com` de novo, mais fundo** —
não só tipografia como da vez passada, mas paleta completa, tratamento de
imagem, altura de seção e dispositivos de assinatura visual, via
`getComputedStyle` e captura de tela real, não memória do que o site "parece
ser".

## O que a raspagem da Porsche encontrou que eu não tinha visto antes

Isso muda a leitura do que falta no RC Arcade, então vem primeiro:

1. **A paleta da Porsche não é preto/branco/vermelho puro.** Tem
   `rgb(78, 40, 139)` e `rgb(138, 26, 255)` — um **roxo** usado como acento
   secundário numa seção específica (provavelmente linha de uma parceria/
   liga). O RC Arcade usa exatamente 3 cores em 100% do site (preto, prata,
   vermelho) do primeiro ao último pixel. Isso é consistência, mas também é
   **monotonia** — nenhum momento de surpresa cromática em nenhum lugar da
   página.
2. **Seções com altura de 1146px a 5777px.** A Porsche não faz "blocos
   uniformes que se repetem" — faz passagens editoriais longas, cada uma com
   seu próprio ritmo interno. O RC Arcade tem 6 seções de conteúdo com
   `padding-block: clamp(88px,12vh,152px)` **idêntico**, todas a mesma
   altura relativa, todas na mesma estrutura (título + parágrafo + grid).
3. **Existe uma seção de arquivo histórico em preto e branco**, com fotos de
   1950-alguma-coisa e números de ano gigantes sobrepostos (tipo `194X` em
   ~120px), num carrossel horizontal com corte duro entre frames — como um
   filme. Isso é um **dispositivo de marca própria**: conta a história da
   Porsche sem precisar de texto. O RC Arcade não tem nenhum equivalente —
   não há nenhum momento do site que só a RC Arcade poderia ter.
4. **Fotos em recorte retrato 10:16** (não só paisagem 16:9) numa seção tipo
   "garage", cada carro/piloto como um cartão vertical. O RC Arcade só usa
   enquadramento paisagem — hero 16:9/3:4 e a foto da prova em 3:2. Nunca um
   recorte vertical fechado tipo still de revista.
5. **Fundo desfocado (`blur(32px)`) derivado da própria foto**, usado atrás
   de conteúdo como halo ambiente — não é gradiente decorativo, é a imagem
   borrada virando cenário. O RC Arcade usa gradiente linear plano
   (`linear-gradient(...rgba(10,11,13,...)`) em todo lugar que precisa
   escurecer uma imagem.

Isso é a régua. Agora a crítica do projeto atual.

---

## 1. Identidade visual
**Nota: sólida, mas emprestada demais da Porsche sem nenhuma torção própria.**
A paleta (preto `#0A0B0D`, prata `#B1B0AB`, vermelho `#E31B23`) é do cliente,
correta. A tipografia (Archivo, peso 400, frase capitalizada) foi copiada do
*registro* da Porsche, não só inspirada por ele — o que é honesto (documentado
em `DESIGN-DIRECTION.md`), mas o resultado é que hoje o RC Arcade **parece um
clone de paleta trocada** de uma página de motorsport genérica, não uma marca
com rosto próprio. Falta pelo menos um elemento que só existe aqui.

## 2. Hierarquia
O H1 do hero (`clamp(2.5rem,6.4vw,5rem)`) e o H2 de cada seção
(`clamp(1.875rem,3.6vw,2.875rem)`) criam só **dois** degraus de importância
no site inteiro. Toda seção "pesa" visualmente igual. A única exceção real é
o `.statement` em "Para el operador" (`Hasta seis simuladores...`,
linha 583) — que é o melhor momento de hierarquia do site, e está sozinho.

## 3. Tipografia
Correta tecnicamente (Archivo + JetBrains Mono, subset latin, decisão medida
na Porsche). O problema não é a fonte — é que ela é usada **do mesmo jeito em
toda parte**. Todo H2 do site tem o mesmo peso 400, o mesmo tracking, a mesma
relação com o parágrafo abaixo. Não há nenhum momento tipográfico "grande e
quebrado" tipo o `194X` da Porsche — um número ou palavra que ocupa a tela
sozinho, sem função de dado, só de impacto.

## 4. Composição
Todo bloco de conteúdo é: título alinhado à esquerda → parágrafo → grid de
2, 3 ou 4 colunas iguais. Isso se repete em "Qué es", "Operador", "Escalas" e
"Vías" sem variação de layout. Nenhuma seção quebra a grade de coluna única
(`--maxw: 1260px` centralizado). Comparado à Porsche (que alterna full-bleed,
carrossel, colunas assimétricas, cartão vertical), o RC Arcade é
**um template CSS bem executado**, não uma composição desenhada seção a
seção.

## 5. Ritmo entre seções
Medido: `padding-block` de **todas as 6 seções de conteúdo é o mesmo**
(`clamp(88px,12vh,152px)`, linha 51 e 102). Isso é o oposto do que a Porsche
faz (seções de 596px a 5777px, cada uma durando o tempo que o conteúdo dela
precisa). O efeito no RC Arcade: rolar a página tem a cadência de um
metrônomo, não de uma narrativa.

## 6. Uso de espaço negativo
Bom localmente (o "Statement" em "Operador" respira, os `spec` em "La
prueba" têm ar), mas **não existe nenhuma seção 100% vazia proposital** —
nenhum momento "silencioso" entre dois momentos de informação. A Porsche usa
isso o tempo todo pra dar peso ao que vem antes/depois.

## 7. Imagens e enquadramentos
**Este é o ponto mais fraco do projeto.** O site inteiro tem **duas fotos**:
o hero (`hero-*.jpg`) e uma foto em "La prueba" (`prueba-1600.jpg`, 3:2). Um
site que existe pra provar "isto é real, não é conceito" (a frase do próprio
cliente) devería ser **dominado por fotografia real**, e hoje é dominado por
texto com duas fotos de apoio. O cliente tem mais de 20 fotos profissionais
disponíveis (`cliente/fotos-pista/DSC0986*.jpg`, e a pasta "RCA publicacion
insta" com 16 fotos catalogadas em `MATERIAL-RECEBIDO.md`) — praticamente
nenhuma foi usada.

## 8. Sistema de cores
3 cores, 100% do tempo, sem variação. Correto pro brief, mas sem nenhum
"momento" — nunca um vermelho vira protagonista de tela cheia, nunca o prata
vira fundo de uma seção inteira pra dar respiro do preto.

## 9. Elementos distintivos da marca
O `.tag` com filete vermelho antes do rótulo (linha 256) é o elemento mais
"assinatura" que existe hoje — reaparece 8 vezes e é reconhecível. Fora
isso, **nada no site seria reconhecido como "RC Arcade" se o logo fosse
removido**. O HUD de telemetria (voltagem, Mbps, ms) é uma boa ideia, mas só
aparece de verdade em 2 lugares (hero e "La prueba") — não virou um sistema.

## 10. Microinterações
Existem e são bem feitas: sublinhado do nav crescendo da esquerda
(linha 125-129), botão descendo 1px no clique (linha 151), scrollbar
customizada (linha 74-79), foco visível vermelho. São detalhes de
engenharia de front-end sólidos — não são o problema deste projeto.

## 11. Motion
**Desequilibrado.** 100% do movimento do site está no hero (intro + entrada
do conteúdo + contador de tempo) e na seção "La prueba" (contador). As
outras 5 seções (`Qué es`, `Operador`, `Escalas`, `Vías`, `Contacto`)
**aparecem instantaneamente**, sem nenhuma transição de entrada — nem o
fade+translate leve que o próprio `DESIGN-DIRECTION.md` já autoriza
("transição entre seções: leve e rápida, ≤250ms").

## 12. Sensação de produto premium
Chega a "limpo e profissional". Não chega a "caro" porque falta o que
diferencia os dois: momentos de risco controlado. Tudo no site é seguro —
grid de 2-4 colunas, título+parágrafo, filete cinza. Marca cara tem pelo
menos um momento por página que quebra o próprio sistema de propósito.

## 13. O que parece genérico ou "AI-designed"
- Os 4 `.arg` em "Operador" (linha 564-580): título + frase, título + frase,
  4 vezes, grid 2x2. É a estrutura mais comum de "seção de benefícios" que
  existe — reconhecível em milhares de landing pages geradas por IA.
- Os 2 `.scale` em "Escalas" (linha 592-611): mesmo padrão, tag + título +
  lista. Funcional, mas zero personalidade.
- `.way` em "Vías" (linha 626-653): tag + título + parágrafo + botão, 3 vezes
  em linha. É o padrão "3 planos de preço" com os nomes trocados.

## 14. O que parece derivado de template
A resposta curta: **a página inteira**, no sentido de que toda seção segue
`<h2> + <p class="lead"> + <grid></grid>`. Isso não é ruim como esqueleto de
implementação (é limpo, é manutenível) — é ruim como **composição final**,
porque um visitante que rola a página sente que está vendo o mesmo
componente reestilizado 5 vezes, não 5 decisões de design diferentes.

## 15. O que poderia virar assinatura visual própria
Três candidatos reais, específicos deste cliente (não genéricos):
- **A grafitagem/arte urbana na parede do circuito**, mencionada em
  `DESIGN-DIRECTION.md` ("Grafite/arte urbana pintada na parede do
  circuito") e nunca usada. É textura real, do espaço real, que nenhum
  concorrente (ver `CONCORRENTES.md`) tem.
- **O HUD de telemetria como sistema**, não como decoração pontual —
  transformar voltagem/Mbps/latência/cronômetro num vocabulário gráfico que
  aparece em cabeçalho de seção, não só dentro do hero e de uma foto.
- **O cronômetro/delta como elemento tipográfico grande** (tipo o `194X` da
  Porsche) — hoje `00:42.381` só aparece pequeno, no canto. Ele é o dado mais
  "de marca" que a RC Arcade tem (é literalmente único dela) e está
  sub-utilizado.

---

## 5 problemas que mais diminuem a percepção de qualidade

1. **Só 2 fotos no site inteiro**, quando o argumento central do produto é
   "isto é real" — a escassez de imagem é o oposto do argumento que o site
   precisa fazer.
2. **Ritmo de seção idêntico repetido 6 vezes** — `padding-block` igual,
   estrutura título+parágrafo+grid igual, sem nenhuma quebra.
3. **Zero movimento fora do hero** — 5 das 6 seções de conteúdo aparecem sem
   transição nenhuma, o que faz o site "morrer" depois dos primeiros 3
   segundos.
4. **Nenhum elemento que só a RC Arcade poderia ter** — a grafitagem do
   espaço, a assinatura sonora do cronômetro, o cockpit físico, nada disso
   virou vocabulário visual do site.
5. **`.arg`, `.scale` e `.way` são o mesmo componente com 3 nomes** — o
   visitante reconhece o padrão na segunda seção e passa a "escanear" em vez
   de ler, porque a forma já não promete nada novo.

## 5 oportunidades que mais aumentariam essa percepção

1. **Trazer 6-10 fotos reais do cliente pro corpo do site** (a pasta "RCA
   publicacion insta" já está catalogada e não foi tocada) — inclusive em
   recorte retrato, quebrando o hábito 16:9.
2. **Variar a altura/ritmo de pelo menos 2 seções** — deixar "La prueba" (que
   já é a mais forte) respirar mais, e comprimir/fundir "Escalas" com "Vías"
   pra cortar repetição.
3. **Dar entrada de scroll leve às seções** (fade+translate, ≤250ms, já
   autorizado no `DESIGN-DIRECTION.md`) — o motion que existe é bom, só está
   mal distribuído.
4. **Um momento tipográfico grande com o cronômetro/delta** — usar
   `00:42.381` ou `+0.814` em escala de título (não de legenda) em pelo
   menos uma transição de seção.
5. **Textura real do espaço** (grafite/mural) como elemento gráfico de fundo
   em UMA seção — não decoração aleatória, o padrão real fotografado do
   circuito do cliente.

## O que deve permanecer
- A paleta e a regra "vermelho só como sinal, nunca fundo" — está correta e
  é do cliente.
- O sistema `.tag` (filete + rótulo mono) — é o elemento mais reconhecível
  que existe hoje.
- A intro e o tratamento do hero — já validado pelo Diogo, não mexer.
- O HUD de telemetria como conceito — só precisa virar sistema, não ser
  descartado.
- A engenharia de motion existente (nav, botão, scrollbar, contador) — é
  craft real, só falta cobertura.

## O que deve ser removido
- A repetição estrutural idêntica entre `.arg`, `.scale` e `.way` — pelo
  menos uma dessas três precisa de uma composição visualmente diferente das
  outras duas, mesmo mantendo o conteúdo.
- O `padding-block` uniforme entre todas as seções — precisa virar uma
  decisão por seção, não uma variável global aplicada sem exceção.

## O que deve ser radicalmente reinterpretado
- **"La prueba"**: hoje é uma foto pequena com HUD sobreposto ao lado de uma
  lista de specs. Esse é o bloco com a melhor matéria-prima do site (a prova
  real) e a composição mais tímida. Merece ocupar a tela de um jeito que
  nenhuma outra seção ocupa.
- **A ausência de fotografia como um todo**: não é um ajuste, é uma decisão
  de composição que falta ser tomada — quantas fotos, em que proporção de
  tela, em que pontos da rolagem.

---

## Direção de arte V2 — prioridades

### P0 — muda a percepção de qualidade imediatamente
1. Trazer 4-6 fotos reais adicionais do cliente pro corpo do site (mínimo:
   uma em "La prueba", uma em "Vías" ou "Escalas", uma em recorte retrato).
2. Reinterpretar "La prueba" pra ocupar mais tela e ganhar um enquadramento
   diferente das outras seções — é a prova do produto, não pode ter o peso
   visual de uma seção de FAQ.
3. Dar entrada de scroll (fade+translate leve) às seções que hoje aparecem
   sem transição.

### P1 — constrói vocabulário de marca próprio
4. Um momento tipográfico grande com o cronômetro/delta, fora do hero.
5. Quebrar a repetição entre `.arg`/`.scale`/`.way`: escolher uma delas pra
   ter um layout visualmente distinto (ex: "Vías" em coluna assimétrica em
   vez de 3 iguais).
6. Variar `padding-block` por seção em vez de usar o valor global em todas.

### P2 — se fizer sentido, depois do P0/P1 validados
7. Textura real do espaço (grafite/mural do circuito) como fundo de uma
   seção.
8. Uma cor de acento secundária pontual — só se surgir do material real do
   cliente (ex: uma cor que já existe nas fotos/pista), não inventada do
   zero.
9. Rodar `impeccable animate` sobre as seções já reinterpretadas, depois que
   a composição nova estiver definida (não antes — animar uma composição que
   ainda vai mudar é retrabalho).

**Nenhuma dessas mudanças foi aplicada.** Este documento é só direção — a
implementação é a próxima conversa.
