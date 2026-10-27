# 04 — Referências e conversão: como um site de experiência premium convence operador e organizador

> Tipo: **estudo** (fotografia de 27/10/2026). Não se reescreve: se algo mudar, acrescenta-se uma
> entrada datada no fim. Estado do projeto continua em `../../CURRENT_STATUS.md`.
> Pergunta: que estrutura, narrativa, prova e mecanismo de conversão fazem um site de fabricante ou
> operador de experiência premium converter **operadores e organizadores**, e como isso se aplica
> ao RC Arcade, cruzando `REFERENCIAS.md`, `DESIGN-DIRECTION.md`, `ESTRUTURA-DO-SITE.md`,
> `DIRECAO-DE-ARTE-V2.md`, `CONCORRENTES.md` e `PLANO-IMPLEMENTACAO-V2.md`.
>
> **Legenda usada em todo o arquivo:**
> **CONFIRMADO** = vi na página aberta ou no código. **INFERÊNCIA** = conclusão minha a partir do
> que vi. **NÃO VERIFICADO** = não consegui abrir ou só vi resumo de terceiros.

---

## Resumo em 10 linhas: as 5 decisões que mais mudam o desenho do site

1. **O botão principal deixa de ser "Contacto" e vira "ver funcionando"** (demostración: presencial ou por vídeo ao vivo). Quem vende equipamento para operador pede demo, não "mensagem" (AXSIM, Sandbox VR).
2. **"¿Cabe en tu espacio?" vira ficha técnica de instalação**: m², altura, energia, internet, pessoas na operação, duração da sessão. Todo franqueador sério mostra isso (BattleKart, Immersive Gamebox, Sandbox VR). É a maior objeção do operador e o RC Arcade **ainda não tem os números**.
3. **O dossiê PDF do cliente entra como segundo botão, sem pedir e-mail.** Quase todas as referências oferecem um PDF (Nick Ho, BattleKart, Sandbox, Simworx). O RC Arcade já tem um pronto ("Launch Edition 2026").
4. **"Media y Artículos" não entra enquanto não houver imprensa.** No lugar, um **registro de pista** com eventos reais e datados (Jornada de puertas abiertas, estreno lona, Open Rcarcade de julho/26). A prova é real e a seção não fica vazia.
5. **O carro que desce só vale com foto de cima de verdade.** Sem ela, a saída honesta é um **traçado do circuito em linha** com um marcador que anda pela rolagem, e não uma vista de cima inventada por IA. O efeito é curto, sem prender a rolagem e com versão parada para quem desliga animação.

---

## 1. Dezesseis referências reais, abertas uma a uma

Critério de escolha: categorias vizinhas do RC Arcade (fabricante de simulador, karting e atração
para parque, VR em local físico, arena de esports, venue de entretenimento, marca de piloto). Todas
foram abertas em 27/10/2026 pelo leitor web (texto da página). Duas também foram lidas no código
(Nick Ho; Racetech na página de contato). **Nenhuma foi medida no navegador nesta rodada:**
tamanho de letra, espaço e ritmo de rolagem continuam a medir.

### 1.1 Racetech Systems: concorrente direto (carro RC + FPV + pista modular)
- **Links:** https://www.racetechsystems.com/ e https://www.racetechsystems.com/contact
- **O que a página faz (CONFIRMADO):** hero → "para venues" (carro RC real, FPV ao vivo, controles de simulador, 4 a 10 jogadores) → imagem da pista "Your Venue. Your Track." → inovação → três blocos (FPV, pista modular, personalização) → rodapé.
- **Prova:** nenhuma. Sem vídeo, sem venue citado, sem depoimento. Só um selo "Experience UK" sem explicação.
- **CTA:** "Enquire Now" e "Contact Us", ambos para um formulário de 4 campos (nome, sobrenome, e-mail, mensagem), **sem texto de privacidade e sem promessa de resposta**.
- **Tirar para o RC Arcade:** nada de forma. Serve de régua: o RC Arcade vence se mostrar o que eles não mostram (vídeo real, telemetria, números, local onde ver). Isso confirma `CONCORRENTES.md` de 23/09.
- **Não tirar:** o formulário genérico.

### 1.2 AXSIM: fabricante de simulador full-motion (fornece o F1® Arcade)
- **Links:** https://axsim.racing/ e https://axsim.racing/venue-solutions/
- **Estrutura (CONFIRMADO):** home com hero "experiências extraordinárias" → **divisão de público** (venue × uso privado) → herança → prova (F1® Arcade + 3 métricas) → formulário. A página de venue: promessa ("experiências para onde voltam") → por que simulador → por que AXSIM (inclui software de gestão) → "feito em torno do seu venue" (lista de tipos de venue) → **calculadora de retorno com aviso de que os números são indicativos** → formulário.
- **CTA:** **"Book a Demo"** na página de venue. Formulário curto: nome, e-mail, mensagem.
- **Observação (CONFIRMADO):** as 3 métricas aparecem como "0+" no texto lido. Provavelmente é contador animado que só preenche com JavaScript (INFERÊNCIA). Quem lê sem JS, robô de busca incluído, vê zero.
- **Tirar:** demo como CTA; lista de tipos de venue ("centros de ocio, FEC, hostelería, atracciones"); a ideia de calculadora **com aviso** (só no futuro, com dados reais).
- **Não tirar:** contador que nasce em zero.

### 1.3 BattleKart: kart elétrico com realidade aumentada (franquia)
- **Links:** https://www.battlekart.com/ e https://www.battlekart.com/en/franchise/
- **Home (CONFIRMADO):** 100% público final (reservar, vale-presente, modos de jogo, "BattleKart em números", avaliações). O operador só encontra o caminho pelo menu e pelo rodapé ("Open your franchise").
- **Página de franquia (CONFIRMADO), a mais completa de todas:** promessa → conceito → por que (único, confiável, fácil de operar, flexível, futuro) → rede (mapa) → públicos (inclui "eventos corporativos podem chegar a ~30% do faturamento", dado deles) → **requisitos do espaço** (60×30 m recomendado, mínimo 24×45 m, pé-direito de 4 a 20 m, sem colunas) → investimento (a partir de ~450 mil €) → perfil do franqueado → **processo em 7 passos** → suporte contínuo → **depoimentos de franqueados com nome e cidade** → brochura para baixar → formulário.
- **Problema visto (CONFIRMADO):** os números se contradizem na mesma página: 2,6 mi × 3 mi × 4,3 mi de jogadores; 50 × 74 centros; 9 × 10+ países. Número desencontrado tira confiança.
- **Tirar:** requisitos técnicos explícitos; processo em passos; depoimento de quem opera; brochura.
- **Não tirar:** misturar B2C e B2B na home; números sem fonte única.

### 1.4 Immersive Gamebox (antes Electric Gamebox): salas imersivas por franquia
- **Link:** https://www.immersivegamebox.com/franchise
- **Estrutura (CONFIRMADO):** promessa → 3 pilares → **perfil de parceiro procurado** (só operador multiunidade; diz claramente que não quer franqueado de unidade única) → mercados abertos (mapa) → **requisitos técnicos** (cada caixa 3,6×3,6×3,6 m, trifásico, 150 A para 8 caixas, internet dedicada) → produto → prova (avaliações, imprensa com logos) → "Apply now" → FAQ com investimento (taxa, pacote, preço por unidade).
- **Tirar:** dizer para quem **não** é (filtra contato ruim); requisitos elétricos e de rede; FAQ com dinheiro.
- **Não tirar:** inconsistências (8–10 × 6–8 unidades por local, Alemanha listada duas vezes).

### 1.5 Sandbox VR: VR em grupo, site separado para franquia
- **Link:** https://franchise.sandboxvr.com/ (a página https://www.sandboxvr.com/franchise só aponta para ele)
- **Estrutura (CONFIRMADO):** hero com 4 provas curtas → oportunidade (investidores nomeados) → suporte incluído → "um negócio que se divulga sozinho" (o cliente leva um vídeo do jogo para casa) → depoimentos de franqueados → o que você recebe → o que pedimos → **seção para dono de imóvel** (área, pé-direito mínimo de 2,75 m, ar-condicionado) → **processo em 9 passos** → prêmios e imprensa.
- **CTA:** "Request Information", "View Brochure", "Watch demo".
- **Problema visto (CONFIRMADO):** cita um mercado de 72,8 bi de dólares sem fonte.
- **Tirar:** "o produto gera conteúdo" (o RC Arcade tem o mesmo argumento, CONTENIDO no dossiê p.14); três CTAs de intensidade diferente (pedir informação, ler a brochura, ver a demo).
- **Não tirar:** número de mercado sem fonte.

### 1.6 K1 Speed: kart elétrico indoor, franquia internacional
- **Link:** https://www.k1speed.com/franchise.html
- **Estrutura (CONFIRMADO):** promessa → prova (desde 2003, "100+ locais") → 3 depoimentos de donos com cidade → **requisitos financeiros** → 3 modelos de investimento → processo em 5 passos → formulário.
- **Formulário (CONFIRMADO):** nome, e-mail, telefone, endereço, tipo de investimento, território, país, região, cidade, mensagem. Promessa vaga ("entraremos em contato em breve").
- **Tirar:** perguntar **onde** o projeto vai ficar (cidade). Para o RC Arcade, cidade + tipo de espaço qualifica o contato.
- **Não tirar:** formulário de 10 campos para o primeiro contato; contagem desatualizada no depoimento (42+ × 107).

### 1.7 HOLOGATE: VR para centros de lazer
- **Links:** https://www.hologate.com/ e https://www.hologate.com/entertainment/
- **Estrutura (CONFIRMADO):** home dividida por mercado (defesa × entretenimento) → números (450+ sistemas, 50+ países). Página de entretenimento: promessa → argumentos de operador (**receita por m², 1 atendente por sistema**, catálogo, liderança) → linhas de produto → logos de parceiros e associações (IAAPA, AAMA) → catálogo de jogos → newsletter.
- **Problema visto (CONFIRMADO):** os números regionais do mapa somam ~370, não 450+. Nenhum depoimento ou caso. O único contato é "CONTACT" no menu.
- **Tirar:** argumentos na língua do operador (m², pessoal por sistema, rotação); associação setorial como prova, **se o cliente for membro**.
- **Não tirar:** "líder mundial" sem prova; contato escondido.

### 1.8 Simworx: simuladores e cinemas 4D para parques
- **Link:** https://www.simworx.co.uk/
- **Estrutura (CONFIRMADO):** hero → produtos → **processo** (conceito, fabricação, filme, instalação, pós-venda, mídia) → projetos recentes com parque e cidade → logos de clientes (Ferrari, Parques Reunidos, Oceanogràfic Valencia…) → **5 depoimentos com nome, cargo e parque** → "Want to chat about a project?" → formulário de projeto.
- **Formulário (CONFIRMADO):** nome, empresa, orçamento, tipo de atração, site, produtos de interesse, **requisitos de espaço**, anexo, e-mail, telefone, país.
- **Tirar:** **prova colada ao formulário** (os depoimentos vêm logo antes); campo "espaço disponível"; anexo (o operador manda a planta).
- **Não tirar:** 11 campos de uma vez. Ao RC Arcade falta tudo o que dá credibilidade a esse formulário (logos, casos).

### 1.9 Triotech: atrações interativas para parques e FEC
- **Link:** https://www.trio-tech.com/
- **Estrutura (CONFIRMADO):** hero com vídeo → **"Quem é você?"** com 6 portas (parque, FEC, atração, museu/zoo, escritório de design, "só curioso") → projetos recentes → apresentação → carreira → newsletter.
- **Tirar:** o seletor de público em primeira pessoa é a forma mais clara de aplicar a variante (b) do item 5.
- **Não tirar:** zero telefone ou e-mail visível na home.

### 1.10 Vesaro: simuladores de corrida e voo (casa e comercial)
- **Link:** https://www.vesaro.com/
- **Estrutura (CONFIRMADO):** hero "The Art of Simulation" → faixa de logos → divisão privado × comercial → parceria Lamborghini → usos (eventos, mídia) → produto em destaque → depoimento de piloto → notícias (incluindo presença na IAAPA Europe 2026) → rodapé com telefone e e-mail.
- **Tirar:** **notícias como prova de vida** (feira, evento, entrega): é o que pode substituir "Media y Artículos" no RC Arcade.
- **Não tirar:** faixa de logos de marcas famosas, a menos que sejam clientes reais.

### 1.11 CXC Simulations: simulador full-motion
- **Link:** https://www.cxcsimulations.com/
- **Estrutura (CONFIRMADO):** hero com **3 botões de público** (casa, empresa, projetos especiais) → texto de posicionamento → 2 notícias → rodapé.
- **Tirar:** a divisão de público já no topo, em botões.
- **Não tirar:** home rala, sem prova nem CTA de compra.

### 1.12 Racing Unleashed: lounges de sim racing (inclui Madrid)
- **Links:** https://www.racing-unleashed.com/ e https://www.racing-unleashed.com/partners-franchises
- **Estrutura (CONFIRMADO):** menu com lounges por cidade (Zurique, Cham, Munique, **Madrid**, mais duas franquias), reservar corrida, reservar evento ("nos nossos lounges" ou **"no seu local"**). A página de parceiros divide parceiro de marca e franqueado e manda para formulário próprio.
- **Tirar:** a separação **evento no meu espaço × evento no seu espaço**, que é exatamente a via "Evento temporal" do RC Arcade.
- **Não tirar:** página de parceiros sem números nem requisitos (no trecho lido).

### 1.13 Sixes Social Cricket: venue de entretenimento social
- **Link:** https://sixescricket.com/ (Awwwards, categoria esportes)
- **Estrutura (CONFIRMADO):** hero **com o formulário de reserva dentro** (tipo: reserva rápida até 30 pessoas **ou "Event Enquiry"**, local, data, hora, pessoas) → experiências → comida → avaliações → locais → ocasiões (corporativo, despedidas…) → contador "Sixes Hit" → grupo grande → newsletter **com caixa de privacidade** → rodapé com "Franchises" e "Invest In Sixes".
- **Problema visto (CONFIRMADO):** o contador aparece com **zeros** no texto lido.
- **Tirar:** começar o formulário com **"o que você quer?"** (tipo de pedido) em vez de nome e e-mail.
- **Não tirar:** contador zerado.

### 1.14 HyperX Arena Las Vegas: arena de esports
- **Link:** https://www.hyperxarenalasvegas.com/
- **Estrutura (CONFIRMADO):** calendário de eventos (com exportar para Google/Apple/Outlook) → lounge de jogo → arena (**ficha do espaço: ~2.800 m², tela LED de 15 m, 3 salas VIP, palco**) → parceiros → "Book Your Event" / "Plan An Event".
- **Tirar:** a **ficha do espaço em números** para quem organiza evento; calendário só com datas reais (para a via Competición).
- **Não tirar:** dois caminhos de contato diferentes (/book-your-event × /contact-us).

### 1.15 Nick Ho Motorsports: complemento ao que já está em `REFERENCIAS.md`
- **Links:** https://nickho-motorsports.nl/ e https://www.awwwards.com/sites/nick-ho
- **Prêmio (CONFIRMADO):** Site of the Day no Awwwards em 11/10/2026, nota 7,24. Na avaliação técnica, animação teve 8,20 e **acessibilidade 6,20**, a nota mais baixa. Tecnologias: GSAP, Three.js, Webflow. Feito pela BORING (Amsterdã), parceira Webflow.
- **"Media & articles" (CONFIRMADO no código):** carrossel Swiper, 3 cartões por tela, cursor de "arrastar", setas anterior/próximo. Cada cartão traz **imagem + título + link para fora**. **Não mostra o nome do veículo nem a data** (só dá para deduzir pela URL: racexpress.nl, autosport.nu, erasmusmagazine.nl). Atrás, a palavra gigante em SVG com 5% de opacidade que se move com a rolagem (`data-svg-scroll`), mais um degradê.
- **Contato (CONFIRMADO no código):** título "Contact", frase curta, **4 campos todos obrigatórios** (nome, sobrenome, e-mail, mensagem), proteção anti-robô Cloudflare Turnstile, **nenhum texto de privacidade**. O botão visível é um link `href="#"` que "clica" um botão escondido. É gambiarra de estilo; leitor de tela e teclado podem se perder (INFERÊNCIA, coerente com a nota 6,20). Fundo com a palavra gigante do mesmo jeito.
- **Guia de patrocínio (CONFIRMADO):** PDF baixado direto, **sem pedir e-mail**, com a frase "quer saber mais?".
- **E-mails divergentes:** .com no topo e .nl no rodapé (CONFIRMADO).
- **Tirar:** o **gesto** da palavra fantasma ao fundo (o RC Arcade já usa CARRERA no topo; repetir em 1 ou 2 seções de fechamento, não em todas); PDF sem barreira; cartões de mídia.
- **Não tirar:** cartão sem veículo e data; formulário sem informação de privacidade (na Espanha não passa, ver item 3); botão falso; e-mails desencontrados.

### 1.16 Lando Norris: site de piloto de F1 (OFF+BRAND)
- **Link:** https://landonorris.com/ · prêmio confirmado na página da agência: https://www.awwwards.com/offbrand/
- **Estrutura (CONFIRMADO no texto lido):** próxima corrida em destaque → mensagem do piloto com assinatura → **sequência de fotos com legenda de lugar e ano** → dentro × fora da pista → galeria de capacetes por ano → loja → parceiros → redes. Feito em Webflow, com animações Rive (CONFIRMADO pelos arquivos). Movimento de rolagem: só há pistas no texto ("tap to lock", "Back to scroll"). **NÃO VERIFICADO** como ele funciona.
- **Tirar:** **toda foto com lugar e data na legenda**. É a forma mais barata de transformar foto em prova, e o RC Arcade tem as datas das pastas.
- **Não tirar:** a escala de produção (WebGL, Rive). Para um site em HTML estático sem equipe, o custo não se paga.

### Abertas sem sucesso (não entram como referência)
- **Zero Latency VR** (https://zerolatencyvr.com/): a página voltou vazia, só com o título. Pela imprensa (Blooloop, RePlay), o modelo é parceria com operador existente (ex.: SpeedPark Angers, França). NÃO VERIFICADO no site.
- **Sodikart** (https://www.sodikart.com/en/): deu erro 404.
- **Carlos Sainz Center** (kart premium em Madri, seria a referência espanhola): o domínio que tentei não existe e a busca só trouxe páginas de terceiros. NÃO VERIFICADO.
- **F1® Arcade**: redireciona para /es; não segui porque já está em `CONCORRENTES.md`.

### O padrão que se repete nas páginas que falam com operador

| Elemento | Quem tem (CONFIRMADO) | O RC Arcade hoje |
|---|---|---|
| Divisão de público logo no começo | AXSIM, CXC, Triotech, Vesaro, Hologate | Não; "Tres vías" fica no fim |
| Requisitos de espaço e técnica em números | BattleKart, Gamebox, Sandbox, HyperX | Não; faltam os m² do cliente |
| Processo em passos ("o que acontece depois") | BattleKart (7), Sandbox (9), K1 (5), Simworx | Não |
| PDF / brochura | Nick Ho, BattleKart, Sandbox, Simworx, Triotech | O dossiê existe e não está no site |
| Prova com nome e lugar | Simworx, BattleKart, K1, Sandbox | Não há casos (ver item 4) |
| CTA de demonstração | AXSIM ("Book a Demo"), Sandbox ("Watch demo") | Não |
| Texto de privacidade junto ao formulário | Sixes (newsletter) | A fazer |
| Promessa de prazo de resposta | **Nenhuma das 16** | Oportunidade, se o cliente puder cumprir |

**INFERÊNCIA:** como nenhuma referência promete prazo de resposta, uma promessa curta e cumprida
("respondemos en 24 h laborables") diferencia. Mas só entra se o cliente se comprometer.

---

## 2. Narrativa por rolagem: o que existe, quanto custa e o carro que desce

### 2.1 O que a pesquisa diz sobre prender a rolagem (CONFIRMADO)
- **Nielsen Norman Group, "Scrolljacking 101"** (Sara Paul, 06/08/2023,
  https://www.nngroup.com/articles/scrolljacking-101/): mudar velocidade ou direção da rolagem
  desorienta a maioria; os efeitos longos parecem site quebrado. Quem chega com tarefa (o operador)
  é o mais impaciente. Texto para ler dentro do efeito é o pior caso. No celular piora. Se for usar:
  curto, vertical, abaixo da dobra, sem texto importante dentro, e evitar no celular.
- **WCAG 2.3.3, "Animation from Interactions"** (nível AAA,
  https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html): movimento disparado
  pela rolagem, como paralaxe, precisa poder ser desligado. A técnica aceita é respeitar
  `prefers-reduced-motion`, a preferência do sistema de "reduzir movimento". Mudar só cor ou
  opacidade não conta como movimento.
- Isso confirma a regra já escrita em `DESIGN-DIRECTION.md` ("sequestro de scroll, nunca").

### 2.2 As técnicas, lado a lado

| Técnica | Exemplo real | O que exige | Peso | Celular | Acessibilidade | Risco |
|---|---|---|---|---|---|---|
| Entrada leve ao aparecer | Nick Ho (`data-reveal`), plano P0.3 do projeto | só código | quase zero | bom | fácil desligar | virar "efeito de template" se tudo entra igual |
| Camada fixa com deriva (o carro do Nick Ho) | Nick Ho, medido em 27/10 | **1 imagem recortada de cima** | 1 imagem (AVIF) | ele cola o carro na borda | desligar = carro parado | baixo, se for curto |
| Seção presa + animação ligada à rolagem | biblioteca GSAP ScrollTrigger (https://gsap.com/docs/v3/Plugins/ScrollTrigger/) | biblioteca + cuidado | biblioteca ~dezenas de KB (INFERÊNCIA) | instável com a barra do navegador | precisa versão parada | **é o "prender a rolagem" da NN/g** |
| Sequência de quadros em canvas | ajudante oficial do GSAP, demo com **147 quadros** (https://gsap.com/docs/v3/HelperFunctions/helpers/imageSequenceScrub); protótipo do projeto em `cliente/fotos-pista/canvas-sequence-test.html` | dezenas de quadros reais | **o mais pesado**: N imagens | pesado em 4G | precisa versão parada | quadros não carregados = buraco |
| Vídeo controlado pela rolagem | — | vídeo com muitos quadros-chave | médio | Safari/iPhone costuma travar (INFERÊNCIA; o estudo de caso da Codrops sobre isso deu erro 403) | idem | engasgo |
| Animação por rolagem só em CSS | MDN (https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_scroll-driven_animations) | só CSS | zero | bom | `prefers-reduced-motion` resolve | suporte: ~88% global; Firefox só a partir da 159, Safari a partir da 26 (https://caniuse.com/mdn-css_properties_animation-timeline). Precisa versão sem efeito |
| Traçado de linha + objeto seguindo o caminho | — | desenho vetorial (SVG) do circuito | poucos KB | bom | fácil | baixo; suporte ~97% (https://caniuse.com/css-motion-paths) |
| 3D / WebGL | Nick Ho (Three.js no topo), Lando Norris | modelo 3D ou mapa de profundidade | alto | caro na bateria | difícil | o mais caro de manter |

### 2.3 O "carro que desce": seis caminhos

O efeito medido no Nick Ho **não prende a rolagem**: o carro entra e sai por gatilho e só desliza
~10% da rolagem. Isso é bom e deve ser mantido. O que falta é imagem.

| Opção | Imagem necessária | Fica bom? | Observação |
|---|---|---|---|
| **A. Igual ao Nick Ho** (carro de cima, fixo, deriva, passos acendem) | **foto de cima, recortada**, ~1400×2500 px | **melhor** | não existe no disco (`TASKS.md`); candidatos: pasta Dropbox "Open Rcarcade/360" e "action5" |
| B. Giro 360° conforme rola | 24 a 36 fotos do carro girando | bom, mas pesado | só se a pasta "360" for mesmo um giro de produto. NÃO VERIFICADO: ninguém abriu essa pasta |
| C. Vista FPV como sequência ("a rolagem é o acelerador") | quadros do vídeo FPV | muito forte para o produto | os 25 quadros atuais têm 1024×381 px, baixa resolução; pede o clipe dedicado já pedido em `TASKS.md` |
| **D. Traçado do circuito + marcador** | **nenhuma foto**: só o desenho do circuito em linha | bom e honesto | usa a linguagem de transmissão de corrida (mapa da pista com a posição do carro), coerente com o HUD do projeto. O marcador pode ser o isótipo da marca |
| E. Recorte 3/4 do #22 andando na diagonal | o recorte que já existe | médio | não "desce de frente"; serve para provar o movimento (já previsto em `TASKS.md`) |
| F. Gerar a vista de cima por IA a partir da 3/4 | — | **não** | seria fabricar uma imagem do produto. Fere a regra do projeto ("tratar foto real pode; gerar cena nova não"). Só com decisão explícita do Diogo e do cliente |

**Recomendação (INFERÊNCIA):** pedir ao cliente a foto de cima. É um pedido barato: celular ou
câmera apontado **reto para baixo** (escada ou suporte), carro parado sobre fundo liso e claro, luz
difusa (sombra fraca facilita o recorte), maior resolução possível, enviado por Dropbox e não por
WhatsApp. Enquanto não chega, construir a **D** (traçado + marcador), que não depende de foto e já
tem a cara do produto. A **A** entra por cima quando a foto chegar.

**Onde usar:** uma vez só. Ou em "Qué es" (4 passos do piloto, como `TASKS.md` já planeja), ou
em "Cómo trabajamos" (os passos do operador, ver item 5). **Em nenhuma seção com números que o
operador precisa ler** (regra de `ESTRUTURA-DO-SITE.md` bloco 4).

**Regras de execução:** sem prender a rolagem; com `prefers-reduced-motion`, carro parado e passos
visíveis; no celular, carro na borda (como o Nick Ho faz); se o JavaScript falhar, a lista aparece
normal (o mesmo "falha aberto" da intro).

---

## 3. Contato e orçamento: a anatomia que converte

### 3.1 O que as referências pedem (CONFIRMADO)

| Site | Campos | Privacidade junto | Prazo prometido |
|---|---|---|---|
| Nick Ho | 4, todos obrigatórios | não | não |
| Racetech | 4 | não | não |
| AXSIM | 3 (nome, e-mail, mensagem) | não visto | não |
| Simworx | 11 (orçamento, tipo, espaço, anexo…) | não visto | não |
| K1 Speed | 10 (território, tipo de investimento…) | não visto | "em breve" |
| Sixes | começa por **tipo de pedido** | sim (newsletter) | não |

### 3.2 O que o YouTube acrescentou (falas, não estatística)
Legendas automáticas baixadas e lidas; os quadros dos vídeos não foram extraídos. **O pipeline
completo de vídeo não rodou** (ver "não verificado").
- **Eddie Park, revisão de home B2B** (https://www.youtube.com/watch?v=QAgyj8lowLw, 6 min): o título
  responde "qual o resultado" e "o que faz"; benefício vago ("mais eficiência") atrapalha; número só
  convence se for concreto e do produto. Para o RC Arcade: "6 simuladores, 1 circuito" é concreto;
  "aumenta tu facturación" não é.
- **Ryan Stewart com David Martin** (https://www.youtube.com/watch?v=uIv0k6ij1kc, 28 min): no B2B
  pode-se fazer perguntas que qualificam (qual serviço, orçamento, site), mas sem exagero; formulário
  em 2 passos (contato primeiro, qualificação depois); página de obrigado com "o que acontece agora";
  e **concentrar o site no serviço que mais rende**, porque três ofertas iguais confundiam. Isso
  pesa a favor da variante (a) do item 5.
- **Exit Five, "B2B Website Teardown"** (https://www.youtube.com/watch?v=m5_-_kq583w, 59 min):
  "plantar a bandeira no título", ou seja, nomear o público ("para centros de ocio…") para quem é
  dele se reconhecer em um segundo. Uma convidada de uma empresa de demo interativa cita um relatório
  próprio: entre as 100 maiores empresas de software, 35% não responderam ao pedido de demo e a
  resposta média levou 2 dias. **É número de fornecedor, dito no vídeo; não abri o relatório.**
  Serve só como sinal de que responder rápido diferencia.
- **Nielsen Norman Group** (texto, não vídeo): formulário curto, com rótulo acima do campo, no máximo
  1 ou 2 campos opcionais marcados e erro explicado em texto (Kathryn Whitenton, 01/05/2016,
  https://www.nngroup.com/articles/web-form-design/). E no B2B vale dar **preço de exemplo** quando o
  preço exato depende do projeto (Jakob Nielsen, 09/04/2006,
  https://www.nngroup.com/articles/show-prices-for-common-scenarios/).

### 3.3 Proposta para o RC Arcade (INFERÊNCIA, a validar com o cliente)

**Três portas, uma ao lado da outra, nesta ordem:**
1. **Formulário curto** (principal), que começa pelo que a pessoa quer:
   - ¿Qué buscas? → Instalación fija · Evento · Competición · Otra cosa *(obrigatório; é o campo que mais qualifica)*
   - Nombre · Empresa · Email **ou** teléfono *(um dos dois)*
   - Ciudad / provincia *(obrigatório: decide se cabe visita)*
   - Espacio aproximado *(opcional, em faixas)* ou Fecha del evento *(aparece só se escolheu Evento)*
   - Mensaje *(opcional)*
   - Botão com verbo e resultado: **"Solicitar demostración"** (instalação) ou **"Pedir propuesta"** (evento). "Enviar" sozinho, não.
2. **WhatsApp** (link `wa.me` com texto pronto **genérico**, sem dado pessoal na URL). Na Espanha o
   comercial costuma responder por ali (INFERÊNCIA). O cliente ainda não disse se prefere.
3. **Descargar dossier** (o PDF "Launch Edition 2026"), sem pedir e-mail. A NN/g argumenta que se
   ganha confiança antes de pedir contato.

**Prova colada ao botão** (como a Simworx faz): uma imagem real com telemetria legível + a linha
"6 simuladores · 1 circuito · tiempo por vuelta medido" + **nome e rosto de quem responde**, se o
cliente topar. A promessa de prazo só entra se o cliente se comprometer.

**Depois de enviar:** página de obrigado com 3 passos ("te llamamos / vemos tu espacio /
demostración") e o link do dossiê. Isso também evita o erro silencioso do site estático.

### 3.4 O que a lei espanhola pede para esse formulário

**CONFIRMADO no BOE**, Lei 34/2002 (LSSI), https://www.boe.es/buscar/act.php?id=BOE-A-2002-13758:
- **Art. 10 (aviso legal):** o site precisa mostrar de forma permanente, fácil e gratuita: nome ou
  razão social, endereço, e-mail, dados de registro (ex.: Registro Mercantil) e **NIF**. Uma página
  "Aviso legal" ligada no rodapé resolve.
- **Art. 21:** mandar publicidade por e-mail exige pedido ou autorização expressa. Logo, se o
  cliente quiser mandar novidades, precisa de **uma caixa separada, desmarcada**, só para isso. A
  exceção (cliente com contrato prévio, produtos parecidos) exige oferecer descadastro simples em
  cada mensagem.

**CONFIRMADO na AEPD** (agência espanhola de proteção de dados), FAQ do dever de informar
(https://www.aepd.es/preguntas-frecuentes/2-tus-obligaciones-como-responsable-del-tratamiento/6-el-deber-de-informacion)
e blog de 03/12/2018
(https://www.aepd.es/prensa-y-comunicacion/blog/la-importancia-de-la-informacion-por-capas-en-el-reglamento-general-de):
a AEPD recomenda informar **em camadas**: uma **primeira camada curta junto ao formulário**, sem
faltar nada relevante, com link para a política completa.

**NÃO VERIFICADO no texto oficial** (o PDF da guia da AEPD deu erro 500; vi a lista em material de
terceiros que segue o modelo AEPD, como a guia da UPM): os itens habituais da primeira camada são
**Responsable · Finalidad · Legitimación · Destinatarios · Derechos · Información adicional**.
Rascunho de primeira camada (a revisar por advogado, com dados reais do cliente):

> **Responsable:** [razón social], [NIF]. **Finalidad:** responder a tu solicitud de información,
> demostración o presupuesto. **Legitimación:** aplicación de medidas precontractuales a petición
> tuya. **Destinatarios:** no se ceden datos, salvo obligación legal y proveedores que nos prestan
> el servicio del formulario. **Derechos:** acceso, rectificación, supresión y demás, en [email].
> **Más información:** [Política de privacidad].

**INFERÊNCIA (conferir com advogado):**
- Para só **responder** o pedido, a base legal é "medida pré-contratual a pedido do interessado" e
  **não exige caixa de consentimento**. A caixa "He leído la política" é costume, não obrigação.
  Ela só é obrigatória para marketing (art. 21 acima).
- Site estático precisa de um serviço externo para receber o formulário. Esse fornecedor trata
  dados por conta do cliente e deve aparecer em "Destinatarios". Se a hospedagem for fora da UE
  (o GitHub Pages é americano), isso entra na política.
- Proteção anti-robô (reCAPTCHA, Turnstile) e análise de visitas podem gravar cookies; aí entra o
  aviso de cookies. Site sem análise e sem anti-robô de terceiros pode dispensá-lo. NÃO VERIFICADO
  para este caso.
- **O formulário do Nick Ho (sem nenhum texto de privacidade) não serve de modelo jurídico.**

---

## 4. Prova sem casos de cliente, sem inventar nada

O RC Arcade tem o melhor ativo da categoria (vídeo real com telemetria, coisa que a Racetech não
tem) e nenhum caso de operador. As referências mostram que dá para provar em degraus, do mais forte
ao mais fraco:

1. **Ver ao vivo** (o mais forte): demonstração presencial no circuito que já existe, ou chamada de
   vídeo com a pista ligada. Exige do cliente: endereço, quem atende e quando.
2. **Vídeo sem corte, datado**: 30 a 60 s de uma corrida real, com a telemetria legível e legenda
   "grabado en [lugar], [fecha]". O vídeo de 42 s atual não serve como peça final (WhatsApp,
   1024×576, câmera na mão; ver `DESIGN-DIRECTION.md`).
3. **Ficha técnica verificável**: o que se mede (tempo de volta, posição, diferença), capacidade
   (até 6), exigências do espaço. **Corrigir antes** "8 ms" e "Vuelta 4/6 — P1", que não estão no
   inventário (`CURRENT_STATUS.md`).
4. **Registro de pista** no lugar de "Media y Artículos": eventos reais com data e lugar (Jornada de
   puertas abiertas; estreno lona; Open Rcarcade, fotos de 1 a 3/7/26 segundo
   `MATERIAL-RECEBIDO.md`). Formato: cartões como os do Nick Ho, **mas com lugar e data** (o que ele
   não faz e o Lando faz). Exige do cliente: confirmar datas, lugares e autorização de imagem.
5. **Quem está por trás**: nome e rosto dos responsáveis (no material aparecem "ximodj navarro" e David
   Navarro Rodríguez como donos das pastas; **o papel deles na empresa não está confirmado**). Pessoa
   com nome é prova num mercado sem casos.
6. **Processo explicado**: o que acontece do contato à primeira corrida (BattleKart, Sandbox, K1).
   Só com os passos reais do cliente.
7. **"Edición de lanzamiento"**: a palavra é do próprio dossiê ("LAUNCH EDITION · 2026"). Assumir que
   é novo é mais crível que fingir trajetória. Um programa "primeros operadores" só entra se o
   cliente oferecer condições reais.

**Nunca:** depoimento inventado; logo de marca que aparece na foto como se fosse parceira (Red Bull,
Hyundai, Ford e Sonax estão nos adesivos da pista, `PLANO-IMPLEMENTACAO-V2.md`); contador que nasce
em zero (AXSIM, Sixes e o contador do Nick Ho aparecem zerados no texto lido); "líder" ou número de
mercado sem fonte (Sandbox, Hologate); o mesmo dado com valores diferentes (BattleKart).

---

## 5. A espinha do site: duas variantes

As duas mantêm o que já foi aprovado (topo CARRERA, "Qué es" em timeline, manifesto do operador).
O que muda é a ordem, os botões e três blocos novos: ficha técnica, processo e registro de pista.

### Variante (a): instalação fixa na frente (premissa atual, **não confirmada por escrito**)

| # | Seção | Promessa (o que a pessoa entende) | Prova | CTA |
|---|---|---|---|---|
| — | Cabeçalho fixo | — | — | **Solicitar demostración** (sempre visível) |
| 1 | Topo (CARRERA) | "Carrera real en primera persona, para tu centro de ocio" (planta a bandeira: nomeia o público) | foto/vídeo real | Solicitar demostración · Descargar dossier |
| 2 | Qué es | entende a mecânica em 20 s | 4 fotos reais, 1 por passo | — (aqui pode entrar o carro, item 2.3) |
| 3 | La prueba | já funciona, não é conceito | vídeo sem corte, datado, telemetria | Verlo en directo |
| 4 | Para el operador | por que isso dá retorno no seu espaço | 6 simuladores · 1 circuito · sessões cronometradas | — |
| 5 | ¿Cabe en tu espacio? → **ficha técnica** | sei se cabe antes de ligar | m², altura, energia, internet, pessoas, duração da sessão, compacto × completo | **Envíanos tu plano** |
| 6 | **Cómo trabajamos** (novo) | sei o que acontece depois | passos reais do cliente | — |
| 7 | **Registro de pista** (no lugar de Media) | isto está acontecendo | eventos datados com foto | — |
| 8 | Otras vías | também faço evento ou liga | 1 linha cada | Pedir propuesta de evento |
| 9 | Contacto | falo com uma pessoa, sei quando respondem | prova colada ao botão (item 3.3) | formulário · WhatsApp · dossier |
| 10 | Rodapé | — | aviso legal, privacidade | "¿Quieres pilotar? Dónde probarlo" (público final, separado) |

**Por que assim:** as referências que falam com operador (BattleKart, Gamebox, Sandbox, K1) têm uma
página só para ele, e o vídeo do Ryan Stewart mostra o ganho de concentrar no serviço principal.

**O que exige do cliente:** confirmação por escrito da prioridade; m², pé-direito, energia, internet,
pessoas na operação, duração da sessão; passos reais do processo; endereço e horário para
demonstração; contato comercial e preferência formulário × WhatsApp; datas e fotos dos eventos;
autorização de imagem; aceitar o PDF do dossiê no site; dados do aviso legal (razão social, NIF,
endereço, registro).

### Variante (b): as três vias com o mesmo peso

| # | Seção | Promessa | Prova | CTA |
|---|---|---|---|---|
| 1 | Topo | "Carreras FPV con coches RC reales: para tu centro, tu evento o tu liga" | foto/vídeo real | **3 botões** (como a CXC) |
| 2 | Qué es | mecânica | fotos | — |
| 3 | La prueba | funciona | vídeo datado | — |
| 4 | **"¿Qué quieres hacer?"** (seletor em 1ª pessoa, como a Triotech) | me reconheço numa porta | — | Instalar · Organizar un evento · Montar una competición |
| 5a | Instalación fija | cabe e rende | ficha técnica + processo | Solicitar demostración |
| 5b | Evento temporal | levam até mim | montagem, dias, espaço mínimo, transporte, **preço de exemplo** (NN/g) | Pedir propuesta |
| 5c | Competición | formato de liga | regras, ranking, calendário **só com datas reais** (o calendário do Nick Ho e da HyperX servem aqui) | Inscribir mi centro / Proponer una liga |
| 6 | Registro de pista | acontece | eventos datados | — |
| 7 | Contacto | o formulário já chega com a via escolhida | prova colada | formulário · WhatsApp · dossier |

**Atenção (INFERÊNCIA):** numa página única, três vias completas deixam o site longo e repetitivo, o
mesmo problema dos `.arg`/`.scale`/`.way` que `DIRECAO-DE-ARTE-V2.md` já critica. Melhor: home curta
com o seletor e **três páginas próprias** (`/instalacion`, `/eventos`, `/competicion`). Em HTML
estático isso é simples.

**O que exige do cliente:** tudo da variante (a) **mais**: logística de evento (montagem, dias, área,
transporte, energia no local, preço de exemplo ou faixa); formato da competição (regras, quem pode
inscrever, calendário real). **Sem esses dados, as portas 5b e 5c ficam vazias e é melhor não
abrir.** Por isso a (a) é a mais segura para o material de hoje.

---

## 6. O que faria o site parecer genérico ou feito por IA, e como evitar

| Risco | Onde já aparece | Como evitar |
|---|---|---|
| Três cartões iguais com título + frase | `.arg`, `.scale`, `.way` (`DIRECAO-DE-ARTE-V2.md` §13) | cada seção com composição própria (plano V2); a ficha técnica como tabela de especificação real |
| Número vazio ou zerado | AXSIM, Sixes, contador do Nick Ho | número escrito no HTML; animação só por cima, nunca no lugar |
| Adjetivo sem prova ("revolucionario", "líder", "único") | Sandbox, Hologate | trocar por dado ou por imagem; se não há dado, cortar |
| Copiar o efeito sem a razão | Nick Ho tem 113 gatilhos de rolagem e nota 6,20 de acessibilidade | 1 efeito assinatura (o carro ou o traçado) + entradas leves; todo o resto parado |
| Prender a rolagem | NN/g | nunca; o carro desliza, não segura |
| Imagem do produto gerada por IA | tentação do "carro de cima" | foto real ou desenho assumido (traçado); nunca falsa foto |
| Logo de terceiro lido como parceria | Red Bull na foto de "Tres vías" | recorte e desfoque já planejados; nada de faixa de logos |
| Formulário "Contact / Submit" | Nick Ho, Racetech | verbo + resultado; campo "¿Qué buscas?" |
| Notas internas visíveis | hoje no site ("Lo que todavía falta…", `TASKS.md`) | remover antes de mostrar ao cliente |
| Texto com cara de IA em espanhol ("eleva tu negocio", tríades, travessões) | risco de qualquer copy gerada | passar a skill `humanizer` e pedir revisão a um nativo; usar as frases do dossiê, que são do cliente |
| Seção montada sem conteúdo ("Media" vazia) | pedido de 27/10 | registro de pista com o que existe; sem conteúdo, a seção não entra |
| Cara de "Nick Ho com outra cor" | regra zero do `CLAUDE.md` | tirar o mecanismo (deriva, palavra fantasma, PDF), não o layout; nossa grade, nossa tipografia, nosso HUD |
| Site pesado no celular | vídeo e sequência de quadros | meta do Google: maior elemento visível carregado em até **2,5 s** para 75% das visitas (https://web.dev/articles/lcp); sequência de quadros só com versão leve no celular |

---

## Fontes abertas (27/10/2026)

**Referências de site**
- https://www.racetechsystems.com/ · https://www.racetechsystems.com/contact
- https://axsim.racing/ · https://axsim.racing/venue-solutions/
- https://www.battlekart.com/ · https://www.battlekart.com/en/franchise/
- https://www.immersivegamebox.com/franchise
- https://www.sandboxvr.com/franchise · https://franchise.sandboxvr.com/
- https://www.k1speed.com/franchise.html
- https://www.hologate.com/ · https://www.hologate.com/entertainment/
- https://www.simworx.co.uk/
- https://www.trio-tech.com/
- https://www.vesaro.com/
- https://www.cxcsimulations.com/
- https://www.racing-unleashed.com/ · https://www.racing-unleashed.com/partners-franchises
- https://sixescricket.com/
- https://www.hyperxarenalasvegas.com/
- https://nickho-motorsports.nl/ (texto + código HTML baixado) · https://www.awwwards.com/sites/nick-ho · https://weareboring.nl/
- https://landonorris.com/
- https://www.awwwards.com/websites/sports/ (lista onde o Nick Ho aparece)

**Rolagem, acessibilidade e desempenho**
- https://www.nngroup.com/articles/scrolljacking-101/
- https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html
- https://gsap.com/docs/v3/Plugins/ScrollTrigger/
- https://gsap.com/docs/v3/HelperFunctions/helpers/imageSequenceScrub
- https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_scroll-driven_animations
- https://caniuse.com/mdn-css_properties_animation-timeline · https://caniuse.com/css-motion-paths
- https://web.dev/articles/lcp

**Conversão e formulários**
- https://www.nngroup.com/articles/web-form-design/
- https://www.nngroup.com/articles/show-prices-for-common-scenarios/
- YouTube (só as legendas automáticas): https://www.youtube.com/watch?v=QAgyj8lowLw ·
  https://www.youtube.com/watch?v=uIv0k6ij1kc · https://www.youtube.com/watch?v=m5_-_kq583w

**Lei**
- https://www.boe.es/buscar/act.php?id=BOE-A-2002-13758 (LSSI, arts. 10 e 21)
- https://www.aepd.es/preguntas-frecuentes/2-tus-obligaciones-como-responsable-del-tratamiento/6-el-deber-de-informacion
- https://www.aepd.es/prensa-y-comunicacion/blog/la-importancia-de-la-informacion-por-capas-en-el-reglamento-general-de

## O que não foi verificado

- **Medição visual:** nenhuma das 16 referências foi medida no navegador nesta rodada (tamanho de
  letra, espaçamento, ritmo). "Media & articles" e o contato do Nick Ho foram lidos **no código**, não
  medidos; o deslize horizontal e a palavra fantasma em movimento não foram cronometrados.
- **Pipeline de vídeo incompleto:** dos 3 vídeos do YouTube só li as legendas automáticas; não
  extraí quadros nem fiz a análise de viabilidade completa. Não há vídeo assistido de dissecação de
  scrollytelling: a busca só trouxe tutoriais de "site premiado em 2 horas", descartados por serem
  receita de efeito, não análise.
- **Bloqueados ou com erro:** Zero Latency (página vazia), Sodikart (404), Carlos Sainz Center
  (domínio não encontrado), Gartner sobre jornada de compra B2B (403), estudo de caso da Codrops sobre
  vídeo × quadros (403), guia PDF da AEPD (erro 500), F1® Arcade (redirecionamento não seguido).
- **Lista de itens da primeira camada** (Responsable, Finalidad…): vista só em material de terceiros
  que segue o modelo AEPD, não no texto oficial. Rascunho jurídico precisa de advogado.
- **Cookies / anti-robô / hospedagem fora da UE:** conclusões são INFERÊNCIA; não abri a guia de
  cookies da AEPD.
- **"Respostas por WhatsApp funcionam melhor na Espanha":** INFERÊNCIA de costume, sem fonte.
- **Formulários de BattleKart, Gamebox e Sandbox:** os campos ficam em outra página ou em JS e não
  apareceram no texto lido.
- **Números dos concorrentes** (jogadores, centros, investimento) foram copiados como **eles**
  publicam; vários se contradizem na própria página. Não são dados de mercado.
- **Estatística de resposta a pedidos de demo (35%, 2 dias):** dita num vídeo por uma empresa que
  vende demo interativa; relatório não aberto.
- **Pasta "360" do Dropbox do cliente:** ninguém abriu; não se sabe se é giro de produto (opção B do
  item 2.3) ou foto 360° do espaço.
- **Papel de "ximodj navarro" e David Navarro Rodríguez** na empresa: só se sabe que compartilharam as
  pastas.
- **Lando Norris:** como a rolagem dele funciona não foi visto; só pistas no texto.
