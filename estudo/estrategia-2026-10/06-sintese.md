# 06 — Síntese da estratégia do RC Arcade

> Tipo: **estudo** — síntese de 28/10/2026. Fontes: estudos 01 a 05, plano, quadro visual.
> Revisada por revisor cego em 28/10 (nota 6/10); as correções dele já estão no texto abaixo.

Marcas: **[nós]** fazemos · **[cliente]** só ele dá · **[Diogo]** decide. "Suposição" = leitura minha, sem prova.

## 1. O que fazemos

O dono ou gerente de centro de lazer (e o organizador de evento) entende em 20 segundos que o RC Arcade é **carro de
verdade numa pista de verdade, pilotado de um cockpit com câmera a bordo, até 6 pessoas correndo juntas com tempo
medido**, vê isso em vídeo e foto reais, e pede proposta. Contra a Wehop (só fotos) e a Racetech (nada), o RC Arcade
ganha com **prova verificável**, não com adjetivo (01, 04). Os números de operação vêm do cliente; até lá o site
convida a mandar o espaço, nunca inventa.

## 2. Em que ordem

A ordem aprovada vale, com correções do revisor cego: as perguntas ao cliente saem **hoje** (custam uma mensagem e sete
das 10 decisões dependem delas). **Decisão do Diogo (28/10 noite), que resolve por ora a pergunta 1:** o site trata
**evento** como foco, porque é assim que o próprio cliente se apresenta, e ganha uma parte de **instalação fixa**; se
chegarem mais contratos de fixo, o foco vai para o fixo (segue onde houver mais resultado). Perguntar ao cliente
continua valendo. O material que o cliente mandou e o site dele já têm autorização assumida: a prova (vídeo, registro de
pista, comentários) pode entrar quando quisermos. Os demais ajustes estão marcados.

0a. **Hoje [Diogo → cliente]:** mandar as perguntas da seção 5.
0b. **Feito em 28/10 [nós]:** aviso fixo "Sitio en construcción · prototipo para el cliente" e a mesma frase no rodapé.
   Decisão do Diogo: o protótipo fica **público com o aviso** (o cliente sabe); sem `noindex`. O cabeçalho B (logo no
   centro, menu no canto direito) virou o padrão. O `canonical` ainda aponta para o `github.io`: trocar quando for ao `.es`.
0c. **Ajuste, antes de medir [nós]:** tirar ou dar fonte a "8 ms" e "Vuelta 4/6 — P1" em "La prueba". Conferi: ainda
   estão no `index.html` da `hero-teste` (linhas 731, 734, 744). "4/6 — P1" ainda contradiz o dossiê ("12 voltas,
   posição 02"). O `test latencia.mov` do acervo pode provar o número, mas está num zip parcial que pode não abrir.
1. **Linha de base do PageSpeed.** Ajuste: o PageSpeed Insights só mede o que está público (a `main`). Medir a `main`
   lá e a `hero-teste` no Lighthouse local, e anotar qual é qual.
2. **Bordas sutis (tokens).** Sem ajuste.
3. **Seções com foto — com evento como foco e uma parte de instalação fixa** (decisão do Diogo; reajustar se o cliente
   disser outra coisa). Ajustes: incluir
   **"La prueba" com o vídeo real** logo depois do topo, em fachada leve (imagem
   com botão de play; o vídeo só carrega no clique), **só depois de assistir os vídeos** (ninguém viu: o de 42 s é de WhatsApp,
   1024×576, e não serve de peça final; o de Cheste é vertical, 88 MB, com pessoas e, suposição, marca de terceiro) e com
   a autorização de imagem como condição para ir ao ar, **não para o protótipo** (Diogo, 28/10); onde hospedar (YouTube do cliente ou o site) é decisão em aberto;
   no protótipo, usar as melhores fotos mesmo com rosto ou marca de terceiro (a Red Bull é organizadora e tem permissão;
   banner nunca se altera); a conferência fica para antes de ir ao ar; cada
   foto em AVIF/WebP com vários tamanhos (as originais têm 4000×5000 px: pesam no celular, mas o 2,5 s do LCP mede o topo, que já é leve; foto abaixo, com
   carregamento preguiçoso, não entra nessa conta); "Tres vías"
   vira uma linha por via.
4. **Carro da rolagem:** opção 2 (pista de cima + marcador), só em "Qué es", sem prender a rolagem, parado para quem
   desliga animação. Sem ajuste.
5. **Rodapé institucional.** Ajuste: junto, a primeira camada de privacidade embaixo do formulário (04). Os dois
   esperam razão social e NIF.
6. **PageSpeed final.**
7. **Ajuste, novo:** combinar com o cliente se ele quer trocar a página do `.es` e qual domínio usa no comercial (o
   Instagram e o e-mail dele são `.com`; o `.es` tem ~6 semanas); se sim, publicar lá, redirecionar os outros
   endereços e trocar o `canonical` (hoje aponta
   para `github.io`). O `noindex` da prévia já saiu no passo 0b. **[cliente + Diogo]**

Em paralelo, fora do site, barato e de alto efeito **[cliente]**: categoria do Google Meu Negócio ("Engenheiro"),
endereço do site no perfil, link quebrado `rcardace.com` na bio do Instagram.

## 3. O que cortamos ou adiamos

- **Site de 8 páginas (02): adiado, com um meio-termo a avaliar.** `/competicion/` e as páginas de ficha esperam o
  dado do cliente. Mas `/eventos/` já tem material (formatos, "el equipo instala…", os cinco datos) e a busca real é
  por "alquiler… para eventos". O custo da página única é não ser achado por essas buscas e não ter o vídeo como
  assunto de uma página (02, D3). Comparar página única com home + `/eventos/` depois da pergunta 1.
- **Três vias com o mesmo peso (04, variante b): cortado por ora.** A justificativa antiga ("o formulário mede o que o
  mercado pede") era falsa: o formulário não envia nada a servidor, só abre o WhatsApp ou o e-mail com o texto pronto,
  então não mede nada. Para medir: o cliente anota a via de cada contato, ou se usa um serviço de formulário (entra
  na política de privacidade). Reabrir se a pergunta 1 mostrar que ele vende mais de uma via.
- **Dado pessoal na URL do WhatsApp:** nome, empresa e contato vão no link `wa.me`, contra o que o 04 pediu. Corrigir.
- **Calculadora de retorno, FAQ do operador, ficha com números: adiadas** até o dado do cliente (01, 03).
- **GSAP, sequência de quadros, 3D, carro recortado da 9882, vista de cima feita por IA: cortados** (peso, NN/g, honestidade).
- **GA4 e Clarity: adiados.** 90 dias só com Search Console e Bing, sem banner de cookies (02) — vale só se não houver YouTube nem
  anti-robô de terceiros na página (não verificado).
- **`llms.txt`, schema `FAQPage`/`Product`, versão em inglês:** por último ou nunca (02).
- **Selos oficiais, "respondemos en 24 h", PDF do dossiê:** só com arquivo, compromisso ou autorização do cliente.
- **Comentários do Instagram:** ficam pequenos e são os primeiros a sair; são público de TV, não comprador.

**Onde os documentos se contradizem e o que vale:**
- "Não há imprensa" (04, status antigo) × El Hormiguero: **vale o plano**, que viu a colaboração oficial em 28/10.
- 116 seguidores (02) × 422 (plano): **vale 422**, contado depois.
- "O vídeo tem de abrir o site" (03) × topo aprovado com foto: **vale o topo** (aprovado e leve); o vídeo vem na
  segunda tela. Se chegar o clipe dedicado, reabrir.
- Página única (plano, 04) × 8 páginas (02): **página única agora**.
- "Simulador" é perigoso, esconde o carro real (03) × "alquiler simuladores" é a busca real (02) × "Hasta seis
  simuladores" no site e no dossiê: **as duas metades valem.** A palavra fica no título e na descrição para ser
  achado; no texto visível, sempre colada a "coches reales".
- Botão "Solicitar demostración" (04, no ar) × "Cinco datos bastan para una primera propuesta" (site do cliente, 05):
  ver decisão 4.
- Quadro visual: a 9861 estava na lista de uso e na de fotos com banner da Red Bull. **Superado (Diogo, 28/10):** banner
  de terceiro não bloqueia o protótipo; usar se for a melhor foto.

## 4. As 10 decisões que mais mexem no resultado

1. **Falar com o operador (B2B) e deixar o formulário separar as vias.** Concentrar numa oferta converte mais que três
   iguais (04). Depende do **cliente** confirmar a via. O site só funciona sem isso até a pergunta 1 ser
   respondida; depois, a resposta pode mudar o topo, o botão e a ordem das seções (ver §6). "Concentrar converte mais"
   vem de uma fala de podcast lida por legenda automática: anedota, não medida.
2. **Prova real logo depois do topo:** vídeo datado ("grabado en [lugar], [fecha]"), leve, e só número com fonte. Foto
   de IA e número sem fonte derrubam a confiança na hora (03). **Cliente** (autorização) e **nós**.
3. **"¿Cabe en tu espacio?" vira ficha de operação:** m² com fila, pessoas por hora, pessoal, minutos por sessão,
   montagem. O comprador faz conta primeiro e lê "até 6" contra "30 karts" (03, 01). **Cliente.**
   A vantagem sobre a Wehop não é "ela só tem fotos": ela lista instalações reais com cidade e linka o YouTube, e o RC
   Arcade ainda não tem operador instalado. A vantagem real é o vídeo na própria página, se for bom.
4. **Um verbo só no botão: "Pedir propuesta"**, até o cliente confirmar que pode demonstrar (onde, quem, quando). É a
   promessa que ele já faz (05); "demostración" promete algo que não sabemos se existe. Trocar nos 3 botões do site
   (linhas 611, 626 e 667) e no assunto do e-mail do formulário (linha 1073). **Cliente; [Diogo] aprova.**
5. **Responder ao medo de quebra com fato:** quem conserta, peças, bateria, modo iniciante. É o medo nº 1 de quem
   opera (01, 03). Hoje só temos "el equipo instala… atiende incidencias", e no contexto de evento. **Cliente.**
6. **El Hormiguero como prova de existência** em "Prensa y registro", com data, fonte e link. Pesa para a IA (02), mas
   para o operador o "uau" é o último dos 9 critérios (03): a prova principal dele é vídeo mais ficha de operação. O
   vídeo é da Atresmedia, o cliente não autoriza embutir; citar com link, suposição sem checagem jurídica. Embutir só o
   post de colaboração do Instagram, com o cliente.
7. **Publicar no `rcarcade.es`, um endereço só.** A página velha já é o 1º resultado e é a que a IA cita; outro
   endereço compete com o próprio cliente (02, 05). Mas o `.com` do cliente também está vivo (atualizado em 01/10 e
   09/10) e `.es` contra `.com` não foi comparado: é conversa, não só acesso. **Cliente**; **[Diogo]** escolhe a
   hospedagem.
8. **Rodapé institucional e privacidade antes de publicar.** A LSSI exige nome, NIF e endereço; "empresa de verdade"
   é sinal que o comprador procura (04, quadro). **Cliente** (a marca está em nome de pessoa física: perguntar se há sociedade ou se é autônomo; no autônomo, a LSSI
   pede o endereço, que pode ser o da casa dele). Para a cláusula do formulário, a AEPD tem o Facilita_RGPD, grátis
   (versão atual não verificada); advogado só para o resto.
9. **Uma frase-definição em texto perto do topo e as mesmas palavras em todo lugar:** "RC Arcade", "coches RC" junto
   de "FPV", FPV explicado ("ves lo que ve el coche"). "FPV" sozinho é drone no Google (02); dono de centro pode não
   conhecer o termo (03). **Nós; [Diogo]** aprova uma linha no topo que nomeie o público.
10. **Fotografia própria, um tratamento só, entregue leve.** O cliente tem 23 fotos profissionais e o site usa 2
    (quadro): é o sinal nº 1 de empresa séria e o maior risco de PageSpeed. **Nós**; cliente para rostos.

## 5. O que ainda precisa do cliente

1. O que vocês mais vendem hoje: instalação fixa, evento ou competição?
2. Compacto e completo: m² com fila, pé-direito, tomada e internet, pessoas na operação, minutos por sessão, pessoas
   por hora, horas de montagem.
3. Podem fazer demonstração? Onde, quem atende, ao vivo ou por vídeo?
4. Quando um carro quebra: quem conserta, em quanto tempo, de onde vêm as peças? Bateria dura e carrega quanto? Há
   modo iniciante?
5. Quem controla o `rcarcade.es` e a hospedagem? Podemos trocar a página e redirecionar o `.com`?
6. É sociedade (SL) ou autônomo? Razão social ou nome, NIF e endereço; o WhatsApp e o e-mail do site são os comerciais?
7. Autorização: pessoas nas fotos e no vídeo de Cheste; embutir o post de colaboração do Instagram; dossiê PDF no site.
8. De onde vêm os "8 ms" e o "4/6 — P1" (o dossiê diz 12 voltas, posição 02)?

## 6. Riscos e pontos fracos desta síntese

- **A premissa "instalação fixa" é o ponto mais fraco.** Não está confirmada por escrito, e tudo que o cliente prova
  hoje é evento (El Hormiguero, Volrace, jornada de Madrid, Cheste); os "cinco datos" dele pedem fechas e duração.
  Suposição: hoje ele talvez venda sobretudo evento. Se a pergunta 1 disser isso, mudam a linha do topo, o botão e a
  ordem das seções.
- **A voz do comprador é emprestada:** quase toda vem de centros de simulador e FEC dos EUA e Reino Unido (03).
- **Não há volume de busca;** o SEO é escolha qualitativa (02).
- **A meta de PageSpeed pode ser medida errado:** sem tráfego não há dado de campo (os "75% das visitas"), e a prévia
  não é pública. Risco de comemorar nota de laboratório.
- **Jurídico é suposição** (base legal do formulário, cookies, classificação da atração): advogado confere.
- **A ordem das 10 é julgamento meu.** A decisão 4 contraria o botão no ar e o estudo 04: é a que mais merece o revisor.
- **Não vi** os vídeos nem o dossiê; do código, só conferi "8 ms", "4/6 — P1", o botão e o `canonical`.
- **Revisão cega (28/10, nota 6/10).** Corrigido acima: a ordem não obedecia ao próprio risco da premissa (agora as
  perguntas saem primeiro e as seções esperam); a justificativa do corte das três vias era falsa; vídeo decidido sem
  ser visto; página única sem comparar o meio-termo; `noindex` mudou para o passo 0b; El Hormiguero rebaixado a prova de
  existência; `.es` virou conversa; jurídico mais barato; LCP corrigido. Ele não verificou: o conteúdo dos vídeos, a
  página da Wehop, o texto da LSSI no BOE, os direitos de embutir da Atresmedia, a versão atual do Facilita_RGPD.
