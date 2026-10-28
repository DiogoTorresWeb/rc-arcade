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
