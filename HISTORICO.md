# RC Arcade — histórico

> Tipo: **histórico** — só se acrescenta. Entrada datada no fim, nunca reescrita.
> Responde "como chegamos aqui". Onde estamos: `CURRENT_STATUS.md`. Por que é assim: `DECISIONS.md`.
> Regra: `../../SISTEMA.md`.

## 13/09/2026 — Etapa 1: material do cliente lido

Dossiê comercial (20 páginas, espanhol), vídeo real de 42 s e 3 pastas de Dropbox chegaram e
foram inventariados em `cliente/MATERIAL-RECEBIDO.md`. Direção de design e estrutura da página
escritas (`DESIGN-DIRECTION.md`, `ESTRUTURA-DO-SITE.md`). Documento de alinhamento ao cliente
em espanhol. Nenhuma linha de site escrita ainda, de propósito.

Retrato do que o cliente respondeu e do que faltava, **movido de `CURRENT_STATUS.md` em
27/10/2026** (texto original, só a primeira linha ajustada):

---

O material abaixo é do levantamento de **13/09**, quando nenhuma linha de site existia ainda.
Retrato do que o cliente entregou e do que foi decidido na Etapa 1.

**Cliente:** RC ARCADE — pilotagem de carro RC real com câmera FPV, vista em
primeira pessoa, num circuito físico. Espanha, material todo em espanhol.
Contatos identificados no Dropbox: **ximodj navarro** e **David Navarro
Rodriguez**.

**Onde estamos:** fim da Etapa 1 / começo da Etapa 2 do método
(`diogo-base/Areas/agencia/metodo.md`). O material do cliente foi lido e
inventariado em `cliente/MATERIAL-RECEBIDO.md`. Nenhuma linha de site escrita
ainda, de propósito.

**Combinado com o cliente:** começar pelo site; pacote digital completo pode
fechar depois.

## Etapa 1 — o que o material já respondeu

- **O que é o produto:** carro RC real + FPV + cockpit (volante, pedais, tela).
  Até 6 simuladores simultâneos num circuito compartilhado, com tempo de volta
  e posição medidos. Mecânica em 4 passos: elige → siéntate → conduce → compite.
- **Como o cliente se posiciona (palavras dele):** *"No miras la carrera.
  Estás dentro de ella."* — a frase-âncora do dossiê. Visão de marca:
  *"Convertir cada circuito en un lugar donde cualquiera pueda sentirse piloto."*
- **O argumento B2B pro operador:** diferenciação (difícil de confundir com
  outra atração), escalabilidade (adapta ao espaço), rotação (sessões e
  competições programáveis), conteúdo (gera conversa e material visual).
- **Os 4 públicos finais:** famílias, jovens, aficionados de RC, empresas/eventos.
- **Identidade visual:** já existe e está definida — vermelho (energia e
  competição), preto (tecnologia e profundidade), prata (precisão e caráter
  mecânico), com sistema de logo completo em 9 variações.
- **Prova de que funciona:** vídeo real de 42s de uma sessão rodando, com
  telemetria na tela (voltagem, 25Mbps, latência). Não é conceito, já opera.

## Etapa 1 — o que ainda falta (não preencher com suposição)

1. **Qual das 3 vias o site prioriza.** O dossiê apresenta três modelos de
   negócio como iguais — instalação fixa, evento temporal e formato competição.
   Cada um fala com um comprador diferente. **Um site não consegue priorizar
   os três.** Essa é a decisão que trava o resto.
2. **O site fala com o operador (B2B) ou com o público final (B2C)?** O dossiê
   é B2B puro. Mas as fotos de Instagram e a pasta "Jornada de puertas
   abiertas" indicam operação já aberta ao público. Pode ser que precise dos
   dois, com caminhos separados — mas isso precisa ser decisão, não acidente.
3. **Concorrentes** — nada no material, ninguém levantou ainda.
4. **Dados operacionais:** onde fica, se já tem unidade aberta, contato
   comercial que vai no site.

**Regra de honestidade (herdada do método):** nada marcado como "falta" pode
ser preenchido com suposição. Campo vazio, nunca chute.

## Impacto na Etapa 3 (design)

A marca **já existe**. Isso muda como a técnica do @matheusgomes vai ser usada:
o Claude Design não vai inventar a identidade — vai construir o sistema de
design **web** (tokens, componentes, escala tipográfica, estados) fiel ao que
já está definido. A referência do Behance entra como padrão de layout, não
como fonte da identidade. Detalhe em `cliente/MATERIAL-RECEBIDO.md`.

---

(Em 27/10 já não valem estas duas linhas do retrato: "Concorrentes — nada no material" — foram
levantados em 23/09, ver `CONCORRENTES.md`; e "nenhuma linha de site escrita" — o site existe.)

## 23/09/2026 — Material real tratado, concorrentes, hero

Fotos e logos reais do Dropbox trazidos para o projeto. Vídeo de 42 s analisado e técnica de
sequência de imagens validada com o material real. Dúvida "DriftStation vs RC Arcade" resolvida
pelo Diogo: é só o nome do espaço físico. Três concorrentes/referências levantados
(`CONCORRENTES.md`). Hero duotone preto e prata formalizado como direção.

## 24/09/2026 — Primeira versão do site, refino Porsche, Direção de Arte V2

- `index.html` criado (blocos 1-4 e 6; 5 parcial; 7 e 8 como pendência honesta).
- Refino no registro Porsche medido ao vivo: Archivo + JetBrains Mono auto-hospedadas, intro de
  racing 1x por sessão, logo "solo nombre" no centro, hero reenquadrado com o carro #22.
- Crítica "Direção de Arte V2" (o site era um componente reestilizado 6 vezes), plano
  `PLANO-IMPLEMENTACAO-V2.md` e Design Gate (GO com ajustes).
- Implementados: P1.1 "Qué es" (timeline), P1.3 "Para el operador" (manifesto), item 6
  "Contacto" (fechamento silencioso). Publicado no GitHub Pages.

## 30/09/2026 e 18/10/2026

30/09: status corrigido (dizia "nenhuma linha de site escrita"). 18/10: referência visual do Nick
Ho Motorsports guardada em `REFERENCIAS.md`, parada até a V2 voltar.

## 27/10/2026 — Retomada e teste do topo (branch `hero-teste`)

- Retomada a partir de `AGORA.md` + git. Auditoria de contexto: os arquivos de estado do projeto
  estavam defasados (nada de P1.1, P1.3 e "Contacto"); este passe os reescreveu e criou este
  histórico.
- Opus leu o site: esqueleto e divisão de tarefas por modelo. Achados confirmados no código:
  "8 ms" e "Vuelta 4/6 — P1" em "La prueba" sem fonte no inventário do cliente; notas internas
  (`TASKS.md`, `ESTRUTURA-DO-SITE.md`) visíveis no site publicado; menu sem link para "Tres vías".
- Teste do topo pedido pelo Diogo (referência: pôster "SEPTEMBER" e Behance "Autrix"):
  palavra gigante CARRERA atrás do carro. Pesquisa técnica (Opus) não achou biblioteca pronta que
  mantenha o texto em HTML; a técnica reaproveitada é a de empilhar camadas do mesmo quadro
  (nickho-motorsports.nl, razorpay.com/m/bold). Pesquisa de texto (Opus) deu 8 palavras e 4
  conjuntos de frases; o Diogo escolheu CARRERA e o conjunto "operador".
- Recorte do carro #22: `rembg` + modelo BiRefNet (MIT). Pegou também o caminhão desfocado do
  fundo; removido por polígono ao longo da borda do carro. A cor do recorte vem do próprio hero
  tratado (alinhado ao pixel). Recorte móvel: o quadro 2400×3200 de `hero-mobile.jpg` foi
  localizado por correspondência de imagem (97%) porque o script que o gerou não foi guardado.
- Defeito antigo achado e corrigido no caminho: o cronômetro "Mejor vuelta" ficava escondido sob
  a foto no celular (`.readout` sem posicionamento).
- Validação: Chrome controlado por DevTools Protocol em 1440, 1024, 768 e 390 px (o painel do
  app corta a captura; ver `runbooks/capturar-telas.md`). `impeccable detect`: zero achados novos
  em relação à `main`.

## 27/10/2026 (fim do dia) — Avaliação do topo e passagem

- O Diogo avaliou o topo: "funcionou bem"; versão atual finalizada, refinos depois. Escolha entre
  cabeçalho A e B não registrada.
- `localhost` não abria no celular dele; foi dado o endereço da rede local (192.168.1.6:8791). Não
  se confirmou que abriu (firewall do Windows em "Público").
- Pedido novo, só plano: copiar do `nickho-motorsports.nl` o scroll em que o carro desce (PC pelo
  meio, celular pelo canto, volta de ré se rolar para cima), mais os modelos de "Contacto" e de
  "Media y Artículos". Na mensagem o nome saiu "nickromotorsports.nl"; vale o link que ele mandou,
  `nickho-motorsports.nl`, que já está em `REFERENCIAS.md`.
- Princípio registrado: qualidade da entrega decide a ferramenta (ver `DECISIONS.md`).
- Passagem: estado, tarefas, decisões e histórico atualizados antes de limpar a conversa.

## 27/10/2026 (noite) — Referência do scroll do carro medida; plano V0 sem código

- Medido de verdade o "carro que desce" do `nickho-motorsports.nl` (entrada de 27/10 em
  `REFERENCIAS.md`): é a seção "RACE CALENDAR"; o carro é uma imagem **vista de cima** que entra e
  sai por gatilho (0,8 s), desliza devagar preso à rolagem e vai "de ré" se você para no meio e volta.
- Achado que muda o plano: não temos imagem do carro vista de cima (as 4 fotos do disco são
  3/4; as 16 fotos do Instagram não estão no disco).
- O Diogo explicou a frase cortada: a divisão por modelo "funcionou bem para a entrega de hoje" e
  quer escalar esse jeito de trabalhar. Virou a lição 57 (`Recursos/aprendizados/`).
- Passagem rodada ao fim do dia. Nenhuma linha de código foi escrita nesta etapa.
- Verificado o repositório do cliente (entrada acima em `TASKS.md`): sem foto do carro de cima no
  disco; Dropbox conectado vazio; links das pastas nunca foram registrados. O Diogo cobrou a
  passagem (handoff) várias vezes; esta é a primeira feita de fato.

## 27/10/2026 (madrugada) — Pivô: redocumentar, acervo completo e estratégia antes do scroll

- O Diogo respondeu às perguntas do handoff com uma mudança de rumo: antes de qualquer scroll, **redocumentar
  o RC Arcade, rodar a pesquisa de estratégia com o maior modelo disponível** (cruzamento de referências,
  SEO, marketing, o que funciona para este cliente) e **olhar todo o material** (dossiê, vídeo, Dropbox). Cabeçalho
  A ou B ficou "ainda não sei"; sobre a `hero-teste`, quer **versão antiga e nova separadas** para medir o
  caminhar antes e depois (talvez repositórios separados no GitHub).
- Feito: tag local `antes-v2-2026-10-27` no ponto da `main` (site no ar); dossiê novo (PDF) recebido e guardado
  em `cliente/`; vídeo reenviado era idêntico ao já guardado; os 3 links do Dropbox chegaram e as pastas foram
  baixadas inteiras (registro em `cliente/ACERVO.md`, links só em arquivo local).
- Regra nova do Diogo: **nunca perder material do cliente**, usado ou não (`CLAUDE.md`, "Regra do acervo").
  Motivo: ele teve de reenviar dossiê e vídeo porque o contexto dos materiais se perdeu.
- O modelo maior (Fable) falhou nas 4 pesquisas: exige créditos pagos na conta. A rodada foi refeita em Opus.
  Síntese final em Fable só com o Diogo liberando créditos.
- Pesquisas (em `estudo/estrategia-2026-10/`): 01 mercado e concorrentes, 02 SEO/GEO e 04 referências e conversão
  concluídas, e o 03 voz do comprador chegou depois da passagem (prova real primeiro; comprador faz conta e teme quebra). O 02 achou o domínio rcarcade.es do
  cliente (já 1º no Google) e a menção do El Hormiguero (07/10/2026), ambas a confirmar com ele.
- Achados que já corrigem documentos nossos: `CONCORRENTES.md` dizia que ninguém tinha telemetria (a Wehop,
  da China, promete até 6 jogadores com telemetria e ranking); a contagem de fotos do Instagram é **23**, não 16;
  `marca video.png`, que faltava desde 23/09, veio no Dropbox.

## 28/10/2026 — Estudo 05: o site atual do cliente
- Diogo perguntou desde quando o `rcarcade.es` existe e como foi feito. Copiei as 4 variações do site e as imagens
  (acervo, fora do git) e analisei: conteúdo de 15–17/09/2026, HTTPS só desde 01/10/2026, `.com` registrado em 21/04/2026
  (o `.com` teve dono anterior em 2011–2020). Data de registro do `.es` não é pública: perguntar ao cliente.
- Feito de um deck de 23 slides em página única, sem JavaScript nem CMS; logo e foto de abertura passaram pelo ChatGPT
  (assinatura C2PA da OpenAI). Nota minha: 5/10 como captação B2B (SEO 2, conversão 3, prova 3), 7/10 como apresentação.
- Detalhe em `estudo/estrategia-2026-10/05-site-antigo-rcarcade-es.md`.

## 28/10/2026 — Plano de melhoria em árvore, Google Meu Negócio e Instagram
- Pedido do Diogo: consolidar o que se traçou desde 27/10 num plano separado, auditar o Google Meu Negócio e o Instagram
  do cliente, e seguir o site etapa por etapa (hero fica; faltam formulário, WhatsApp, SEO e provas sociais).
- Google Meu Negócio visto no Maps: nome RCARCADE, categoria "Engenheiro", sem site, sem horário, zero avaliações, uma foto
  (logo), ponto cai no mar perto do Estreito de Gibraltar. Instagram: 11 posts, 422 seguidores (o 116 do estudo 02 estava velho).
- **El Hormiguero confirmado**: o vídeo de 07/10 é colaboração do @elhormiguero com @rcarcade, 6,2 mil curtidas, com
  agradecimento oficial. A "Jornada de puertas abiertas" é em Madrid (qui 2 e sex 3 de julho); Volrace Motorshow Zaragoza
  24–26/10 está no Instagram. Detalhe e árvore em `PLANO-DE-MELHORIA.md`.

## 28/10/2026 — Etapa 2.1 e 2.2 do site: contato, SEO e provas
- Na branch `hero-teste`, hero intocado: formulário de contato (monta a mensagem e abre WhatsApp ou correio do cliente, sem servidor),
  botão de WhatsApp flutuante, seção "Cómo trabajamos" (4 passos do próprio cliente), "Registro de pista" (Volrace Zaragoza
  24–26/10, El Hormiguero 07/10, jornada de puertas abiertas Madrid 2–3/07) e 3 comentários públicos do Instagram como prova
  **provisória** (sem nome de usuário). Saíram do ar as notas internas ("Pendiente", "TASKS.md", "Borrador").
- SEO: canonical, Open Graph, imagem de compartilhamento 1200×630, ícones, dados estruturados, `robots.txt` e `sitemap.xml`
  (endereço provisório do GitHub Pages; trocar quando for para o domínio do cliente).
- Conferido no navegador (computador e celular 390 px): sem rolagem lateral, formulário valida e monta a mensagem certa.
  Erro achado e corrigido no caminho: uma quebra de linha dentro do texto do script derrubava o script inteiro.

## 28/10/2026 — Fotos do cliente abertas, razão social e proposta visual
- As 23 fotos do Dropbox são de câmera profissional (4000 × 5000) e o vídeo do evento tem tomadas aéreas da pista: a "vista de cima do
  carro" existe. Isso muda o diagnóstico do site: o problema não é falta de material, é que o site usa 2 fotos. Proposta com as
  fotos reais nos lugares: `cliente/acervo-dropbox/extraido/board-visual.html` (fora do git; aguarda aprovação do Diogo).
- Razão social e NIF: agente de pesquisa (Sonnet) não achou empresa. Na OEPM a marca RC ARCADE (M4407321) está em tramitação desde
  05/10/2026 no nome de uma pessoa física. Não se buscou NIF/endereço de pessoa; vem do cliente. Links da bio do Instagram: um é
  `rcarcade.com`, o outro `rcardace.com` (erro de digitação, domínio inexistente).

## 28/10/2026 (tarde) — Aprovação e passagem
- O Diogo aprovou o quadro visual e a execução. Pediu: síntese da estratégia com modelo forte sem estourar limite, execução focada em PageSpeed e atenção do contratante, bordas finas sutis (estilo Apple, mais leves), rodapé institucional sério, e nada perdido.
- O quadro visual passou a ficar versionado em `estudo/visual/board-visual.html` (as fotos continuam fora do git, no acervo local).
- Sessão encerrada com passagem: o estado está em `PLANO-DE-MELHORIA.md`, `TASKS.md` e `CURRENT_STATUS.md`.

## 28/10/2026 (noite) — Síntese e revisão cega
- Um agente (Opus, sem web) escreveu `estudo/estrategia-2026-10/06-sintese.md` a partir dos estudos 01 a 05, do plano e do quadro visual.
- O revisor cego deu 6/10. Achados aceitos e aplicados: a ordem não obedecia ao risco da premissa "instalação fixa" (agora as perguntas ao cliente saem primeiro e as seções esperam); o corte das três vias se apoiava num formulário que não mede nada (só abre WhatsApp ou e-mail); vídeo decidido sem ser visto; `noindex` e `canonical` passaram para o começo; El Hormiguero virou prova de existência; publicar no `.es` virou conversa com o cliente; PageSpeed e jurídico corrigidos.
- Conferido no quadro visual: a síntese segue a direção aprovada. Pontos abertos: a foto 9864 está em "Qué es" mas fora da lista das 12; a 9861 está na lista de uso e na de banner Red Bull; o vídeo em "La prueba" seria um terceiro movimento (o quadro diz só dois).

## 28/10/2026 (noite) — Regra do protótipo
- O Diogo esclareceu: antes de aprovação e pagamento do cliente, tudo é protótipo e imagem não bloqueia (rosto, banner da Red Bull, nomes de outras empresas). Usar a melhor foto. A síntese e o status foram ajustados; a regra está também em `CLAUDE.md`. Cuidado mantido: o protótipo com essas fotos não vai ao repositório público.

## 28/10/2026 (noite) — Decisões do Diogo e cabeçalho B
- Foco em evento com uma parte de instalação fixa; cabeçalho B como padrão; protótipo público com aviso de "en construcción"; prova liberada. Detalhe em `DECISIONS.md`. A regra anterior de repositório público (protótipo não vai ao GitHub Pages) está **superada**: ele pode ficar público com o aviso.

## 28/10/2026 (noite) — Site V3 montado
- Fotos reais tratadas e leves (`scripts/preparar-fotos.py`), clipe da pista de 1 MB, bordas sutis, carrinho da rolagem, rodapé institucional, páginas legais, textos B2B para evento e instalação fixa (redator Opus, `estudo/estrategia-2026-10/07-textos-es.md`).
- Camada de rastreio com consentimento (`assets/track.js`, `runbooks/rastreo.md`), IDs vazios.
- Robô de auto-revisão (`scripts/revisar-visual.mjs`) e Lighthouse: 97/100/100/100. Achados e corrigidos no caminho: rodapé com linhas curtas, painel de cookies aberto, título fantasma com contraste ruim, ordem de títulos, LCP que pulou para 3,3 s por causa da intro (corrigido).
- Revisor cego sobre o site construído: pedido, parecer pendente.

## 28/10/2026 (noite, 2) — Revisão cega do site V3 e correções
- Revisor cego (Opus): 5/10. Aceito e corrigido: faixa de cookies com Aceitar destacado (agora três botões iguais, primeiro item do teclado, aparece só com ferramenta ativa, vence em 24 meses, revogar apaga cookies e recarrega); textos legais que contradiziam o código; etiqueta fixa que cobria botões (foi para o cabeçalho); vídeo sem pausa (WCAG 2.2.2); contraste do WhatsApp; link para `#contacto` travado pela intro; GA4 contando a visita em dobro; frases sem prova ("el mismo equipo detrás", "Nadie la confunde", "Mejor vuelta").
- Decisão minha, avisar o Diogo: botão "Pedir propuesta" agora aparece também ao lado do menu no cabeçalho B do PC (o revisor mostrou que sem ele não havia botão fixo de proposta).
- Não resolvido por depender do cliente: respostas comerciais (modelo, preço, pessoas por hora, m², montagem, seguro, razão social).

## 28/10/2026 (noite, 3) — Publicação e proposta ao cliente
- **Site V3 publicado** por ordem do Diogo: commit `1fae62f`, `hero-teste` → `main` (avanço simples; `origin/main` estava dentro da `hero-teste`). Conferido no ar: título e `track.js` (200). Medida pública (Lighthouse, celular): 96/100/100/100, LCP 1,6 s; site antigo `rcarcade.es`: 74/89/96/91, LCP 13,5 s, 4,3 MB, **zero cookies e zero JavaScript** (por isso, hoje, sem infração de cookies; falta a identificação do titular).
- **Proposta ao cliente** em espanhol (`cliente/propuesta/`, fora do git) e **três modelos de post** feitos com fotos reais e o sistema visual (`posts.html`, `render.mjs`, `build.py`). Pesquisa legal (Opus, fontes oficiais) em `estudo/estrategia-2026-10/08-alertas-legais-es.md`, tom "aviso de amigo", sem patrocínio nem direito de imagem.

## 28/10/2026 (noite, 4) — Refino a partir do Nick Ho
- Sessão da proposta aberta à parte (passagem `runbooks/passagem-2026-10-28-noite-proposta.md`), com o modelo de votos me pega/talvez/sai. Pesquisa de repositórios para posts: `estudo/redes-sociais/01-repos-e-estilos.md`.
- Teste do carrinho do site no ar: anda e gira com a rolagem, mas é um mini-traçado de ~70 px na margem direita. Agente (sonnet) mediu o Nick Ho: `estudo/refino-v4/nickho/MEDICAO.md`. Montado o laboratório `estudo/refino-v4/lab.html` (foto P&B→cor, vídeo que cresce, linhas e paralaxe, carro grande no centro) para o Diogo votar antes de aplicar.

## 28/10/2026 (noite, 5) — Votos no laboratório e passagem do site
- O Diogo votou: A (títulos dentro da foto, a cores; P&B só numa galeria por tópicos), C (revelação ao descer, quer no site todo), fonte Anton adotada; B (vídeo em tela cheia perde qualidade no PC) e D (carro grande) em aberto. Causa medida da perda no PC: clipe vertical 540×960. Frentes separadas: proposta na outra sessão, site nesta. Passagem: `runbooks/passagem-2026-10-28-noite-site.md`.
- Voto em D (mesma noite): lista vermelha aprovada e fontes do laboratório aprovadas; carro do laboratório reprovado (cruzava a página no celular). Pedido: carro real do cliente visto de cima, com a coreografia do Nick Ho (desce e some; volta ao contrário; ré se parar e voltar); se não der bem feito, o carro sai.

## 28/10/2026 (noite, 6) — Texto antigo × V3 e passagem do site
- Comparação às cegas dos textos (V3 = texto-1, site do cliente = texto-2, ordem sorteada, chave fora do projeto): revisor cego deu V3 7/10 e antigo 4/10; minha análise (escrita antes) coincidiu. Resultado: V3 é a base; 6 ideias curtas do antigo candidatas; defeitos novos achados ("simuladores" × "No es un videojuego", telemetria "de ejemplo", repetições). Nada aplicado ao site.
- Correção do Diogo: "organização sem site gigante" não é enxugar nem compactar, e muito menos trazer tudo do site antigo; é usar bem o que temos. Galeria por tópicos (P&B no hover) fica mais abaixo; passos 1–4 com título dentro da foto, a cores.
- Passagem do site: `runbooks/passagem-2026-10-28-noite-site.md`. Lições gerais: `Recursos/aprendizados/` 58 e 59.

## 28/10/2026 (noite, 7) — Cortina de entrada mais curta
- Medido: a cortina levava ~2,7 s (logo, régua, abertura e desvanecer) até a foto do topo ficar visível. Encurtada para ~1,8 s (logo 0,55 s, abertura aos 0,7 s, saída aos 1,3 s, foto assenta em 1,1 s; failsafe 3 s). Mesmo desenho, só mais rápido; `prefers-reduced-motion` intacto.
- Lighthouse local, celular, mediana de 3: nota 97 → 97, LCP 1,5 s → 1,5 s, Speed Index 4,55 s → 4,3 s. A cortina era parte do atraso, não todo: falta olhar o peso das imagens do topo e de baixo.
- Publicado na `main` por ordem do Diogo ("manda o site").

## 28/10/2026 (noite, 8) — Peso das imagens, 4 passos e sistema de revelação (local, sem publicar)
- Fotos do topo de JPG para WebP (q74): peso total no celular 789 → 687 KB; Speed Index 4,3 → 4,2 s (ganho pequeno: o que ainda pesa é o desenho do topo, não as imagens). Regra para a galeria futura: foto só carrega ao abrir a aba, WebP em dois tamanhos, orçamento de ~700 KB ao abrir.
- 4 passos: número e título (Anton) dentro da foto, a cores; a frase explicativa volta para baixo (o Diogo achou o texto grande demais dentro da imagem). Celular com foto 4/3; no PC, textos um pouco maiores. **Aprovado pelo Diogo.**
- Sistema de revelação (`.rv`, `[data-rise]`, `data-parallax`, ~60 linhas de JS sem biblioteca): títulos de seção sobem de máscara, cartões (passos, argumentos, formas, escalas, processo) sobem em escada, paralaxe só na faixa grande. Ativa só com JS e sem "reduzir animações". A faixa do operador virou "UNA PISTA. HASTA SEIS PILOTOS." em Anton gigante sobre a foto da pista inteira (DSC09875, `pista-completa-*`); a foto do escudo aceso segue em `assets/fotos/operador-*` para a galeria. Lighthouse local: 97/100/100/100 (um `aria-label` em `<p>` custou 3 pontos e foi trocado por texto para leitor de tela); robô sem erro.

## 28/10/2026 (noite, 9) — Galería por temas (local, sem publicar)
- Inventário: 23 fotos do Instagram + 8 quadros do vídeo `RC ARCADE CHESTE HD.mp4` (o Diogo achou as imagens do vídeo "um absurdo de boas"; extraídos a cada 2 s, recorte 4:5, mesmo acerto de cor; receita em `scripts/preparar-fotos.py`, variável `QUADROS_CHESTE`). Não existia foto de evento no acervo do Instagram: os quadros do vídeo viraram o tópico **Eventos**.
- Tópicos (proposta minha, **a aprovar**): Eventos 8 · Pista 5 · Cabinas 4 · Coches 5 · Marcas en pista 6 (o "Eventos" do plano antigo virou o de verdade; "Marcas en pista" descreve o que se vê: Red Bull, Hyundai, Ford, Dunlop). Foto de passos reaproveitada sem peso extra.
- Bloco de altura fixa com abas (teclado: setas, Home, End), carrossel com snap e setas no PC; só a aba aberta carrega (medido: 5 arquivos ao abrir, 8 depois de abrir Coches). PC: preto e branco que ganha cor no hover; celular: a foto que chega ao centro ganha cor (teste do Diogo, se ficar ruim, só PC). Link "Galería" no menu. Robô sem erro; Lighthouse local 96/100/100/100.

## 28/10/2026 (noite, 10) — Quadro visual relido: o que já foi feito e o que falta
- O Diogo cobrou o quadro `estudo/visual/board-visual.html` ("Como sair do site 2.0 do site deles"), que não constava da passagem. Comparado com o site: feito (fotos reais com um tratamento só, passos com foto, faixa grande, escalas, imprensa em cartões, rodapé institucional, contato). Faltavam: capas dos cartões de imprensa, foto no alto das seções de texto, o carro com a pista real de cima, os vídeos de Cheste.
- Feito agora (local): capas dos 3 cartões de imprensa (quadro f13 do vídeo para TV, foto 9873 para Zaragoza, quadro f27 aéreo para Madrid) e foto no alto de cada cartão de "Dos formas" (Evento: quadro f26 (arco Dunlop com equipe e público); Instalación fija: foto 9874; TV passou a usar a foto 9893. O Diogo reprovou a primeira escolha (quadro f15, foto 9905 e quadro f13)). Receita em `scripts/preparar-fotos.py`. "Cómo trabajamos" fica sem foto: não há imagem de montagem no acervo (pedir ao cliente).
- Selos de apoio (UE, Generalitat, Kit Digital): conferido em ACERVO, dossiê e logos do cliente; **nada** que indique apoio público. O espaço reservado no rodapé continua; só entra selo se o cliente mandar arquivo e texto oficiais.

## 28/10/2026 (noite, 11) — Correção de honestidade nas fotos
- Cartões de imprensa: tirei as fotos de TV e Zaragoza (origem não confirmada) e o de Madrid passou a usar a foto de celular de 3-7-26 11:17, da pasta Open Rcarcade (dentro das datas da jornada). 12 das 15 fotos de julho foram recuperadas do zip parcial e registradas em `cliente/ACERVO.md`.
- Galería: o tópico "Eventos" (8 quadros, todos do mesmo vídeo de Cheste) fazia parecer 8 eventos diferentes; renomeado para "Con público" (legendas "Con público · 01…"). Ordem do Diogo: foto repetida do mesmo evento pode ficar; o texto não pode sugerir eventos diferentes. Enquanto não houver fotos confirmadas de cada evento, os cartões ficam como estão.

## 28/10/2026 (noite, 12) — Crédito da agência e carro de rally
- Pedido do Diogo: dar a entender ao cliente que o site é de empresa nossa. Adicionado "· Por Agencia Bienquisto" no rodapé (PC e celular). A versão no topo foi tirada a pedido do Diogo: o crédito fica só no final. Grafia dos documentos da base: Bienquisto (nome de trabalho, DEC-014). **Local, ainda não publicado.**
- **Decisão do Diogo: o "carro de cima" usa o carro de rally** (o das fotos de estúdio e do topo do site), não o carro esportivo branco/azul do vídeo de Cheste.

## 28/10/2026 (noite, 13) — Passagem 2 e o erro da passagem que perde fontes
- O Diogo cobrou que a passagem anterior deixou fontes para trás (quadro visual aprovado, ACERVO, vídeo de Cheste, material de julho). Causa: passagem escrita de memória, sem inventário. Escrita a **passagem 2** (`runbooks/passagem-2026-10-28-noite-site-2.md`), um manifesto de fontes com 6 perguntas de abertura, decisões acumuladas, o que falta e "o que se sabe e o que NÃO se sabe".
- `TASKS.md` recebeu faixa "desatualizado desde 13/09". `CURRENT_STATUS.md` passou a apontar a passagem 2 e o quadro visual. Regra global provisória em `~/.claude/CLAUDE.md`; lição nº 60 e o estudo em HTML (`Recursos/aprendizados/passagem-perde-fontes-do-projeto.html`) para o Diogo rodar um estudo à parte.
- Passagem 2 testada às cegas duas vezes (sessão fria, agente `revisor-cego`): **7/10 e 7/10**. As lacunas da 1ª rodada (10) e da 2ª (9) foram corrigidas em `CURRENT_STATUS.md`, `cliente/ACERVO.md`, `TASKS.md` e na própria passagem. Registrado no HTML do estudo como dado para decidir se o inventário deve ser gerado por script.
- **Decisão do Diogo (28/10, fim da noite): o "carro que desce" usa o carro de rally nº 43 com câmera FPV.** Handoff rodado em seguida.

## 28/10/2026 (noite, 14) — Carro 43: tentativa de vista de cima
- Fotos candidatas vistas (9882, 9884, 9901, 9861): **nenhuma é de cima de verdade**. A 9861 chega mais perto (43 a uns 60°), mas está cortado pelo banner da Red Bull e pela torre; a 9882 mostra os dois carros em 3/4 alto.
- IA para refazer de cima (Diogo autorizou ~0,75 crédito): **bloqueada**. O plano da conta é grátis (1,42 crédito) e o modelo recusou ("requires basic plan or higher"); os outros modelos custam 4,5 créditos para 3 versões. **Nada foi gasto.** Recorte de referência `ref-43-a.jpg` foi enviado à ferramenta (some em 24 h).
- Plano B (grátis): carro desenhado em vetor, `estudo/carro-43/gerar-carro-v1.py` → `carro-v1.html` e `.png`. Avaliação minha: lê como carro, mas parece ícone de brinquedo (pintura em "confete", rodas soltas, proporção alongada) e o preto some no fundo preto do site. **Não recomendado para o site.** Nada mudou em `index.html`.

## 28/10/2026 (noite, 15) — Carro 43 de cima feito por IA e montado em Cómo trabajamos (local)
- Os 50 créditos que o Diogo colocou estavam na conta `diogoyt1212` do Higgsfield; a ligação MCP da sessão usa **outra** conta (1,42 crédito, plano grátis). Contorno: gerar pelo Chrome do Diogo (site do Higgsfield, modelo Nano Banana Pro, 2 créditos por imagem). Duas rodadas de 3 versões (12 créditos). A 2ª rodada (pedido firme: preto com rachaduras brancas, câmera no teto) ficou fiel; escolhida a 1ª (bandeira, SONIC, listras verdes). O "Eh" no teto e o "OINOS" são o "43" e o "SONIC" invertidos (a pintura real se lê de trás para frente). Baixada para `estudo/carro-43/ia-43-original.png` (896×1200, com marca d'água fora do carro). **Decisão do Diogo: "ficou ótima, decide você".**
- Recorte (`estudo/carro-43/recortar-carro.py`): o primeiro comeu os paralamas brancos (o Diogo notou "partes faltando perto da roda"); refeito com segmentação por bacia sobre o gradiente + fechamento morfológico. Webp com transparência 280 e 488 px (49 e 97 KB, `scripts/preparar-carro.py`).
- Montagem (`index.html`): a seção Cómo trabajamos virou lista grande (Anton) com o carro numa coluna `sticky`; quatro camadas (lane > slide ±12 % > pos entra/sai 0,8 s expo.out/expo.in > rot 180° fora da tela); estados `top/mid/bottom`; passos acendem em vermelho cumulativo; celular: coluna de 100 px, carro de 120 px sobrando 10 px por lado; `reduced-motion`: carro parado. O mini-traçado `#circuit` fica oculto enquanto a seção está na tela. Teste: `estudo/carro-43/testar-carro.mjs` (estados e fotos); robô sem erro; Lighthouse celular local 96 e 92, 100/100/100.
- Vetor v1 (`carro-v1.*`) fica como descartado.

## 29/10/2026 (madrugada, 16) — Auditoria do carro (pedido do Diogo: "subindo parece caindo", "parece colado", "o que o Nick Ho faz que esquecemos?")
- Método: filmei o carro quadro a quadro em 3 cenários (descendo tudo, subindo depois de sair, subindo no meio) em PC e celular, com folhas de contato (`filmar-carro.mjs`, `folha-contato.py`).
- **Achado principal:** subindo no meio da lista, o carro descia ~400 px junto com a página (a pista solta da tela quando o topo da seção passa do começo) e só depois o gatilho o mandava para cima. Os gatilhos de entrada/saída passaram para dentro da zona presa (entra com `r.top < −120`, sai com `> −80`; fim `r.bottom < 1,05·vh`), a lista ganhou `padding-top: 34vh` e o passo acende pelo centro, não pelo topo.
- Outros achados: sombra (`drop-shadow`) dentro da camada que gira virava ao contrário e não aparecia no preto → brilho vermelho (`.race__pos::before`); imagem crua de estúdio (clara, borda com farelo cinza) → tratamento de cor/grão/exposição/vinheta e limpeza de borda em `scripts/preparar-carro.py`; cinza do título com contraste 2,3:1 → 3,9:1; número pequeno aceso em vermelho (contra o `SISTEMA-VISUAL.md`) → branco; primeiro quadro engasgava ao decodificar a foto → `decode()` antecipado.
- Nick Ho (`24-carro-fluidez.mjs`, MEDICAO §7): a fluidez vem de **Lenis em todo o site (lerp 0,1, wheelMultiplier 0,7)** mais `will-change: transform`, carro `absolute` dentro de sticky e gatilhos sem animação própria. Adotado só o equivalente local (lerp 0,1 no deslize). Lenis no site todo fica para voto do Diogo.
- Engasgo que sobrou (67–133 ms) acontece na seção seguinte (fotos da galeria carregando), não no carro.
- (29/10, 01h) O Diogo viu a versão local e disse "tá parecido com antes": o tratamento de cor tinha sido tímido e o movimento não aparece em foto parada. Reforço visual em `scripts/preparar-carro.py`: abertura/fechamento morfológico da silhueta, saturação do verde −28 % e do laranja −16 %, luz vermelha de contorno cozida (halo de 5 e 12 px de desfoque só fora do carro). Imagens agora `carro-43-300.webp` e `carro-43-532.webp` (532×1059); CSS: largura ×1,09, brilho CSS de fundo reduzido para .09. Lição: mudança de movimento precisa de vídeo ou de passo a passo para o Diogo conferir; imagem parada não mostra.
- (29/10, 01h30) O Diogo reprovou o contorno vermelho cozido ("volta o que tava antes") e pediu: carro ~10 % mais escuro (opacidade 88–90 %) e borda esmaecida em todo o contorno; se não der certo, voltar ao **primeiro teste de todos**. Feito: revertidos `index.html`, `scripts/preparar-carro.py` e as imagens ao estado do commit `df02a8a`; acrescentados `opacity:.9` no CSS e o esmaecimento da borda (distância até a borda, `smoothstep` em 9 px). **Para o plano B:** copiar `estudo/carro-43/versoes/v0-primeiro-teste-280.webp` e `-488.webp` para `assets/fotos/carro-43-280.webp` e `-488.webp` e tirar o `opacity`. Versões v1 (tratado) e v2 (contorno vermelho, 300/532) também guardadas lá.

## 29/10/2026 (madrugada, 17) — Publicado
- Ordem do Diogo ("publique e resume os próximos passos"): `git push origin hero-teste:main` (544bca2 → b33da37). Foi junto o crédito "Por Agencia Bienquisto" do rodapé, o carro nº 43 em Cómo trabajamos (opacidade 90 %, borda esmaecida) e os documentos. Capturas de teste saíram do repositório (`.gitignore` em `estudo/carro-43/_*`).
- Conferido no endereço público: `race__lane` presente, foto do carro 200 (98 KB), crédito no rodapé. Lighthouse celular no público: 96 / 100 / 100 / 100, LCP 1,7 s, 628 KB.
