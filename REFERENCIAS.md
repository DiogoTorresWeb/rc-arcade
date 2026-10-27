# Referências visuais — guardadas para quando o site for mexido

> Tipo: **referência** — só se acrescenta. Cada entrada traz quem mandou, quando
> e **por que serve**. Link sem motivo escrito não entra: daqui a um mês ninguém
> lembra por que ele estava aqui.

## Como estas referências podem ser usadas

**Regra zero do projeto (`CLAUDE.md`):** não copiar a estrutura de nenhum site
pronto só trocando o tema. Já deu errado uma vez, no site do irmão.

Logo, o uso correto é o que está em
`../../Recursos/aprendizados/de-referencia-se-extrai-informacao-nao-aparencia.md`:
medir a referência de verdade (abrir no navegador, ver espaçamento, escala de
tipografia, ritmo do rolar) e **extrair a informação** — não imitar a aparência.

---

## [2026-10-18] Nick Ho Motorsports — mandada pelo Diogo

**https://nickho-motorsports.nl/**

**Por que está aqui:** o Diogo mandou para ser usada como referência quando o
RC Arcade for mexido de novo. Fica **parada** até lá, por decisão dele.

**O que é:** site de um piloto neerlandês de automobilismo (Porsche Carrera
Cup). Não vende produto — o objetivo é **conseguir patrocinador**, com botão
"Become partner" e um guia de patrocínio para baixar.

**Por que encaixa no RC Arcade:** a direção de arte V2 deste projeto já nasceu
de uma raspagem da **Porsche**, então o vocabulário de automobilismo já é o
registro escolhido aqui — esta referência fica na mesma faixa, não abre uma
frente nova. E o site é **B2B de relacionamento**, igual ao RC Arcade: ele
precisa convencer uma empresa a fechar, não um consumidor a comprar por impulso.

**Seções que ele tem** (útil para comparar com `ESTRUTURA-DO-SITE.md`): hero com
o número do carro, sobre, histórico de carreira em fases, galeria, calendário
de corridas com contagem regressiva para a próxima, logos de patrocinadores,
imprensa, e contato com formulário.

**Tratamento visual, pelo que dá para ver no HTML:** vídeo hospedado em CDN com
indicação de "Sound on" e "drag" (sugere vídeo com som e interação de arrastar),
imagens em AVIF e mapas de profundidade em escala de cinza. Feito em **Webflow**
por uma agência (weareboring.nl), com vídeo em Bunny Stream.

**Não verificado:** fundo escuro, escala real da tipografia e animação ao rolar
são inferência a partir do HTML, não medição. **Quando a hora chegar, abrir no
navegador e medir** em vez de confiar nesta anotação.

**O que provavelmente vale olhar lá:** o contador para a próxima corrida (o RC
Arcade tem ligas e eventos), a faixa de logos de parceiros, e como o histórico
em fases é montado — o RC Arcade tem o mesmo problema de contar uma trajetória.

---

## Pendência: a referência da Porsche perdeu o link

A `DIRECAO-DE-ARTE-V2.md` abre com "o que a raspagem da Porsche encontrou", mas
**o endereço exato não ficou guardado em lugar nenhum** desta pasta. Quando a V2
voltar à mesa, recuperar qual página foi raspada e registrar aqui — referência
sem endereço não dá para conferir nem para voltar.

---

## [2026-10-27] Nick Ho Motorsports — o "carro que desce" MEDIDO (não é inferência)

Medido no navegador (Chrome por protocolo, 1440×810 e 390×844) e lido no código público do site.
Complementa a entrada de 18/10, cujo "não verificado" fica resolvido para esta seção.

**O que é:** a seção "RACE CALENDAR 2026" (`section_agenda#calendar`, fundo preto). Um carro de
corrida **visto de cima, com a frente para baixo** (imagem AVIF responsiva, 1440×2579 no PC e
390×698 no celular) fica numa camada `sticky` no meio da seção; a lista de corridas passa por ele
e cada item acende em amarelo (`#fed60a`) ao cruzar o centro da tela. No PC o título se divide
("RACE … 2026") ao redor do carro.

**Geometria medida:** PC — carro de 320×573 px, centralizado (x=560 de 1440), parado em y≈67–89.
Celular — 183×327 px colado na **borda direita** (x=271 de 390, cortado pela borda), y≈201–299;
o título passa por baixo do carro.

**Três movimentos, não um só:**
1. **Entra e sai por gatilho, não preso à rolagem.** Quando o marcador `start` chega ao centro da
   tela, o carro vem de `-100vh` até 0 em 0,8 s (`expo.out`). Quando o marcador `end` passa do
   centro, sai para `+100vh` em 0,8 s (`expo.in`) e só então gira 180° (fora da tela). Rolar de
   volta repete ao contrário. No celular o `end` só dispara depois do fim da lista (o carro fica
   estacionado a lista toda).
2. **Desliza devagar enquanto está parado** (esse é o "desce conforme rola"): a camada `sticky`
   tem `yPercent` de −12 para +12, preso à rolagem (`scrub`), do começo ao fim da passagem pela
   seção. Medido: ≈9,5% do movimento da rolagem (+95 px em 1020 px no celular).
3. **Cada item da lista acende** em amarelo (0,2 s) ao cruzar o centro e volta (0,6 s) ao sair.

**A "ré" que o Diogo notou é real, num caso específico:** se o carro entrou e você para no meio e
volta antes do fim, ele sobe **de frente para baixo** (rotação 0): top 74→21→19→11→−18→−101→−325→
−789 em ≈0,8 s. Se já tinha passado do fim, ele volta pela base com a rotação 180° (de frente para
cima, "pra frente"). Ou seja: só gira depois de sair por baixo.

**Como é feito:** página Webflow com GSAP 3.15 + ScrollTrigger (113 gatilhos na página inteira,
quase todos paralaxe), Lenis, Three.js (o efeito de profundidade do topo) e um script customizado
(Slater, módulo `62406.js`). O código é público (servido a todo visitante); serviu para entender o
**mecanismo**. A implementação do RC Arcade é nossa, não cópia.

**Ainda não medido:** a seção "Media & Articles" (cartões que deslizam na horizontal, título gigante
fantasma ao fundo) e o formulário de contato.
