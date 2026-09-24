# Design Gate — revisão crítica do PLANO-IMPLEMENTACAO-V2.md

Escrito em 24/09/2026. Papel assumido: diretor de arte + frontend lead
revisando o trabalho de outra pessoa antes de liberar código. **Nenhum código
foi alterado.** Fontes lidas por completo pra este gate:
`DIRECAO-DE-ARTE-V2.md`, `PLANO-IMPLEMENTACAO-V2.md`, `DESIGN-DIRECTION.md`,
`cliente/MATERIAL-RECEBIDO.md`, `index.html`.

Formato: 10 perguntas do Diogo, cada uma com veredito e, quando aplicável,
correção concreta. Achados que mudam o plano estão marcados **[APLICADO NO
PLANO]** quando já editei o `PLANO-IMPLEMENTACAO-V2.md` em resposta a este
gate.

---

## 1. As 6 composições são realmente diferentes, ou só trocamos nome de componente?

**Veredito: AJUSTAR.**

Testando as 6 duas a duas, achei duas colisões reais:

- **"Operador" (manifesto) e "Contacto" (manifesto minimal)** são, como
  escritas no plano, a mesma ideia duas vezes: "declaração grande + lista de
  apoio abaixo". Diferem em tamanho, não em espécie.
- **"Escalas" (comparison) e "Vías" (split assimétrico)** também colidem:
  ambas são, na prática, "duas colunas de peso desigual". Sem uma diferença
  de tratamento além do texto, um visitante que rolar as duas seguidas vai
  reconhecer o mesmo layout de novo — exatamente o problema que o plano
  deveria resolver.

**Correção concreta:** diferenciar por **tratamento de imagem**, não só por
proporção de coluna — "Vías" ganha foto em primeiro plano (sujeito nítido),
"Escalas" **não tem foto em primeiro plano nenhuma**, só uma atmosfera de
fundo bem discreta (ver item 6). Isso torna as duas seções estruturalmente
parecidas (2 colunas) mas visualmente distintas (uma é sobre uma foto, a
outra é sobre espaço vazio). Pra "Operador" x "Contacto": "Contacto" perde
o tratamento de tipografia grande — vira só texto corrido pequeno, sem
nenhum elemento de impacto, porque a seção **não tem dado** pra sustentar
impacto (dado inventado seria contra a regra de honestidade). **[APLICADO NO
PLANO]**

---

## 2. "La prueba" em immersive/full-bleed: aumenta narrativa ou só aumenta uma foto?

**Veredito: AJUSTAR — a versão original do plano só aumentava uma foto.**

Reler o P0.1 como estava escrito: "a foto cresce... segunda imagem
(`DSC09861`) menor, ancorando o canto — díptico." Isso é redimensionamento,
não narrativa. Um díptico só conta como narrativa se as duas imagens tiverem
uma relação (antes/depois, geral/detalhe, ação/resultado) — duas fotos largas
de pista lado a lado, do mesmo tipo de enquadramento, não criam essa relação,
só repetem o mesmo tipo de imagem duas vezes.

**Correção concreta:** cancelar o díptico forçado. "La prueba" cresce com
**uma imagem só** (a que já existe, `prueba-1600.jpg`), e a narrativa vem do
HUD sobreposto virar o protagonista real da composição — não é "foto grande
com dado em cima", é "o dado é a razão da foto estar em tela cheia". Isso
também resolve o achado do item 7 (ver abaixo): o full-bleed deixa de ser
"foto bonita grande" (que qualquer marca de carro faz) e passa a ser
"telemetria real ocupando a tela" (que só a RC Arcade tem). `DSC09861` sai
desta seção e vai para "Vías" (ver item 6). **[APLICADO NO PLANO]**

---

## 3. "Vías" vai ter hierarquia real, ou só deixa de ter 3 cards iguais?

**Veredito: AJUSTAR.**

O plano original resolve 3-iguais virando 1-grande + 2-iguais-menores. É
melhor, mas ainda deixa "Evento temporal" e "Formato competición" como
clones um do outro em escala reduzida — троca o problema de lugar, não
resolve.

**Correção concreta:** os dois secundários passam a ter **papéis diferentes
entre si**, não só tamanho diferente do principal:
- "Evento temporal" vira uma linha de texto direta com link, sem moldura de
  card — é uma opção real, mas rápida de ler.
- "Formato competición" vira uma nota pequena, estilo legenda/rodapé — o
  próprio texto já diz que ela é "apoio, prova social, não é porta de
  entrada" (`index.html` linha 649), então o tratamento visual deveria
  **concordar com o que o texto já afirma**, em vez de dar o mesmo peso de
  card às três vias, inclusive à que o próprio conteúdo diz que pesa menos.
**[APLICADO NO PLANO]**

---

## 4. O cronômetro/delta está sendo tratado como identidade, ou como decoração?

**Veredito: AJUSTAR — o próprio plano original já admitia essa dúvida sem resolvê-la.**

O P1.5 original terminava com uma pergunta de validação ("esse número
comunica algo sozinho, ou só parece bonito?") sem responder. Um elemento
tipográfico grande com `00:42.381` sozinho, aparecendo **uma vez**, sem
rótulo, é decoração — parece bonito, mas não ensina nada que o resto da
página já não tenha dito.

**Correção concreta — dois requisitos pra isso contar como identidade e não
decoração:**
1. **Tem que aparecer mais de uma vez** com o mesmo tratamento tipográfico
   (mono, `tabular-nums`) — a versão grande de transição, mais a versão que
   já existe no hero e em "La prueba". Um elemento só é "sistema" se se
   repete; se aparece uma vez só, é efeito especial.
2. **Nunca sozinho sem o rótulo do que é** — mesmo em escala grande, a
   palavra "Mejor vuelta" (ou equivalente) tem que estar presente, só que
   pequena — do jeito que o hero já faz (`.readout` linha 210-219). Retirar
   o rótulo pra "limpar" a composição tira o dado do contexto e transforma
   número real em número decorativo.
**[APLICADO NO PLANO]**

---

## 5. A grafitagem tem evidência suficiente pra entrar agora?

**Veredito: APROVADO — mas a justificativa do plano original era otimista demais.**

O plano já tratava isso como P2 exploratório, sem prometer implementação —
isso está certo. Mas ao reler `DESIGN-DIRECTION.md` linha 178-179 encontrei
um dado que o plano não usou: a análise frame-a-frame **já registrou**
"artefato de bloco visível em área de detalhe (**mural**, tela do
simulador)" — ou seja, já sabíamos que a região do grafite tem compressão
visível, antes mesmo de tentar extrair um frame novo. O plano descrevia isso
como "incerto, vamos testar"; a leitura correta é "já temos evidência prévia
de que a qualidade ali é ruim".

**Correção concreta:** manter em P2, mas mudar o tom de "vamos ver se serve"
pra "evidência já registrada sugere que não serve em tela grande — só vale a
pena testar se o Diogo achar um motivo específico pra insistir". Isso evita
gastar um ciclo de trabalho testando algo que o próprio projeto já documentou
como improvável. **[APLICADO NO PLANO]**

---

## 6. Estamos dependendo demais das duas fotos disponíveis?

**Veredito: AJUSTAR — não pela quantidade, pelo encaixe errado.**

Duas fotos pra 6 seções é uma dependência real (nomeei isso no plano
original), mas o problema maior que achei revendo as fotos de novo é que
**as duas estavam atribuídas ao lugar errado**:

- `DSC09861` mostra **três carros circulando ao mesmo tempo** — é a prova
  visual mais forte que existe pra "até 6 simuladores simultâneos", o
  argumento central de "Vías/Instalación fija" e de "Para el operador". No
  plano original ela ia pra "La prueba", que já tem sua própria foto de
  ação (`prueba-1600.jpg`) — desperdiçando o encaixe mais óbvio que existe.
- `DSC09865` é uma foto **vazia, atmosférica, com desfoque de fundo forte**
  (pórtico Hyundai, pista sem carro em primeiro plano). Não tem sujeito de
  ação — é melhor como **textura ambiente de fundo em baixa opacidade** do
  que como foto protagonista. No plano original ela virava a foto principal
  de "Vías", que precisa exatamente do oposto (ação, capacidade, prova).

**Correção concreta:**
- `DSC09861` (ação, múltiplos carros) → vai pra **"Vías/Instalación fija"**
  (P1.2), reforçando literalmente o argumento de capacidade.
- `DSC09865` (vazia, atmosférica) → vira **fundo de baixa opacidade em
  "Escalas"** (não foto protagonista) — resolve dois problemas de uma vez:
  dá a "Escalas" seu próprio tratamento de imagem (diferente de "Vías", ver
  item 1) e usa a foto certa pro clima certo.
- "La prueba" fica só com a foto que já tinha (ver item 2) — **nenhuma foto
  nova entra nela**.

Isso não elimina a dependência de só termos 2 fotos novas — só corrige o
encaixe. A dependência de fundo continua real e fica registrada como item
de ação separado (pedir mais fotos do Dropbox ao cliente), não escondida.
**[APLICADO NO PLANO]**

**Achado extra, não estava no plano original:** `DSC09861` tem um banner
**"Red Bull Racing" como elemento gráfico dominante do quadro** (confirmado
ao reabrir a foto agora). Usá-la na seção que vende a instalação RC Arcade
pro operador, com a marca de um patrocinador terceiro como elemento mais lido
da composição, compete com a própria marca do cliente no momento errado.
**Correção:** o recorte pra "Vías" precisa **cortar ou desfocar o banner**
(a mesma técnica de motion blur radial já validada em `treat_hero_v2.py`
resolve isso sem inventar nada — só direciona o blur pra cobrir o banner em
vez do fundo genérico). **[APLICADO NO PLANO]**

---

## 7. Existe alguma decisão inspirada na Porsche que pode deixar o RC Arcade derivativo?

**Veredito: AJUSTAR — uma decisão específica, o P1.5.**

O "momento tipográfico grande" do P1.5 é, sem rodeio, a mesma jogada que a
Porsche faz na seção de arquivo (`194X` gigante sobre foto). A diferença que
salva a ideia: o número da Porsche é decorativo-histórico, o nosso é dado
real de produto (`00:42.381`) — então o *motivo* de usar tipografia grande é
diferente, mesmo que o *gesto* seja parecido. Ainda assim, sem cuidado na
execução, pode ficar visualmente idêntico ao que vimos no site deles.

**Correção concreta:** onde a Porsche usa foto em preto-e-branco atrás do
número gigante, o RC Arcade **não usa foto nenhuma** atrás do
cronômetro/delta — só o fundo `--rc-black` liso, com o número em
`JetBrains Mono` (a Porsche usa a fonte serifada/display deles, não mono).
Menos ornamento no fundo = a diferença fica no material (dado real vs. still
de arquivo), não só na cor da fonte. **[APLICADO NO PLANO]**

A "immersive/full-bleed" de "La prueba" (item 2) também nasceu olhando a
Porsche, mas depois da correção do item 2 (HUD como protagonista, não a
foto) ela já não se parece com nenhuma seção específica da Porsche — o HUD
de telemetria é o elemento que garante isso. Sem essa correção, seria
derivativa; com ela, não é mais.

---

## 8. Existe algum elemento importante da identidade atual que estamos prestes a perder?

**Veredito: BLOQUEADOR.**

Este é o achado mais sério do gate. O `DESIGN-DIRECTION.md` linha 134 tem
uma regra dura, já escrita antes deste ciclo: **"o conteúdo que o operador
precisa (capacidade, escala, contato) nunca fica atrás de um vídeo"** —
e por extensão, atrás de imagem. O P0.1 original dizia: *"as specs...
passam a viver dentro do HUD da foto grande, não numa `<dl>` separada"*.

Isso quebra a regra na prática: hoje `.specs` (linha 293-296 do `index.html`)
é uma `<dl>` de verdade, sempre visível, independente da foto carregar ou
não. Se as 4 métricas (voltagem, Mbps, latência, melhor volta) passarem a
existir só como texto sobreposto numa foto grande, dois riscos reais:
1. **Se a foto não carregar** (conexão ruim, erro de rede), o operador perde
   o dado — exatamente o cenário que a regra de `DESIGN-DIRECTION.md` já
   previa e proibiu.
2. **Contraste de texto sobre foto variável é mais frágil** do que texto
   sobre fundo sólido — já corrigimos um problema de AA real neste projeto
   (vermelho 4.1:1), e texto direto sobre pixel de foto sem chip de fundo
   sólido tende a reintroduzir esse tipo de falha.

**Correção concreta — obrigatória antes de qualquer código:** `<dl
class="specs">` **continua existindo como elemento HTML real**, com
conteúdo real, independente de a foto carregar. Ela pode ficar **visualmente
integrada** à composição (sobreposta num canto da foto grande, por exemplo,
como já acontece parcialmente no HUD de hoje) — mas com um chip de fundo
sólido (`--rc-surface` ou `--rc-black` com opacidade alta, não gradiente
transparente) atrás do texto, garantindo legibilidade e existência
independente da imagem. **[APLICADO NO PLANO — P0.1 reescrito]**

---

## 9. O plano resolve o diagnóstico principal ("um componente reestilizado 6 vezes")?

**Veredito: AJUSTAR, condicional às correções acima.**

Como estava escrito antes deste gate, a resposta seria "parcialmente" — os
achados dos itens 1, 2 e 3 mostram que duas colisões estruturais
sobreviveriam (manifesto×manifesto, comparison×split). Com as correções
aplicadas (tratamento de imagem diferente entre Vías/Escalas, remoção do
impacto tipográfico de "Contacto", papéis diferentes pros 2 caminhos
secundários de "Vías"), a resposta passa a ser **sim** — as 6 seções deixam
de compartilhar a mesma "forma" de solução, cada uma resolve o problema dela
de um jeito que as outras não resolveriam tão bem.

---

## 10. A ordem P0/P1/P2 maximiza impacto por esforço?

**Veredito: AJUSTAR.**

Dois problemas na ordem original:
1. **Prioridade (P0/P1/P2) e ordem de execução são coisas diferentes no
   plano, mas isso nunca foi dito explicitamente** — o P0.3 (motion) estava
   nomeado "P0" mas agendado como **passo 9**, depois de vários itens P1.
   Isso é uma decisão técnica correta (não anima uma composição que ainda
   vai mudar), mas sem a frase explicando isso, parece contradição.
2. **O primeiro passo de execução era o mais arriscado, não o mais seguro.**
   "La prueba" (P0.1) dependia de asset novo (na versão original) e —
   depois do achado do item 8 — é a mudança com risco real de violar uma
   regra já escrita do projeto. Começar por ela significa descobrir o
   problema do item 8 só depois de já ter mexido no código.

**Correção concreta:** inverter a ordem — começar pelas mudanças que não
dependem de asset novo e têm zero risco de regra quebrada (`Qué es`
timeline, `Operador` reordenação, `Contacto` simplificação), validar o
padrão de composição funciona, **só depois** entrar nas duas que mexem com
foto e HUD (`Vías`, `La prueba`), agora já sabendo exatamente qual regra
não pode ser quebrada. **[APLICADO NO PLANO — ordem de execução reescrita]**

---

## Resumo dos vereditos

| # | Pergunta | Veredito |
|---|---|---|
| 1 | 6 composições realmente diferentes? | AJUSTAR |
| 2 | "La prueba" ganha narrativa ou só tamanho? | AJUSTAR |
| 3 | "Vías" ganha hierarquia real? | AJUSTAR |
| 4 | Cronômetro é identidade ou decoração? | AJUSTAR |
| 5 | Grafitagem tem evidência suficiente? | APROVADO (com ressalva já aplicada) |
| 6 | Dependência excessiva de 2 fotos? | AJUSTAR (encaixe corrigido) |
| 7 | Alguma decisão vira clone da Porsche? | AJUSTAR (P1.5) |
| 8 | Algo da identidade atual em risco? | **BLOQUEADOR** (regra de conteúdo nunca atrás de imagem) |
| 9 | Resolve "componente reestilizado 6x"? | AJUSTAR → SIM, com as correções |
| 10 | Ordem P0/P1/P2 maximiza impacto/esforço? | AJUSTAR (ordem invertida) |

## Decisão

**GO COM AJUSTES.**

Todas as correções acima já foram incorporadas ao `PLANO-IMPLEMENTACAO-V2.md`
— não ficaram só registradas aqui. O bloqueador do item 8 era o único que
impediria começar a codar (violaria uma regra já escrita do próprio
projeto); com a correção aplicada (specs continuam sendo `<dl>` real, chip
de fundo sólido), ele deixa de bloquear.

Antes de tocar em código, falta só uma confirmação sua: a reatribuição de
fotos do item 6 (`DSC09861` → Vías, `DSC09865` → fundo de Escalas) muda o
plano de assets que você já tinha visto. Se concordar, o próximo passo real
é o passo 1 da ordem de execução revisada: `Qué es` (timeline), zero
dependência de asset novo.
