# Passagem 2 — RC Arcade, site, fim da noite de 28/10/2026

> Esta passagem **aponta** para os documentos, não os substitui. Se algo aqui contradiz `CURRENT_STATUS.md`, vale o `CURRENT_STATUS.md`.
> Handoff curto desta noite (foco no carro nº 43, skills sugeridas, armadilhas): `runbooks/handoff-2026-10-28-fim-da-noite.md`.
> Para continuar: abrir conversa nova na pasta do projeto e dizer **"continuar o site do RC Arcade"**.
> **Substitui** `passagem-2026-10-28-noite-site.md` (a primeira), que deixou fontes para trás. O erro está explicado em
> `Recursos/aprendizados/passagem-perde-fontes-do-projeto.html` (na base). **Esta passagem é um inventário, não uma narrativa.**

## 0. Antes de agir: 6 perguntas que a sessão nova responde sozinha (5 minutos)
1. O que mudou desde o último commit? `git log --oneline -5` e `git status --short`.
2. Que fontes de verdade existem? Leia a tabela da seção 1 **inteira**, não só as da primeira linha.
3. O que o cliente já mandou? `cliente/ACERVO.md` (registro de tudo que chegou) antes de dizer "não temos X".
4. O que o Diogo já aprovou por escrito? Seção 3 abaixo e `PLANO-DE-MELHORIA.md` ("Diretrizes aprovadas").
5. O que está só no computador e não foi publicado? Seção 2.
6. O que eu não sei? Seção 6 (origem das fotos e eventos). Dado sem origem não vira legenda, cartão nem texto.

## 1. Manifesto de fontes (tudo que existe; nada aqui é opcional)
| Fonte | O que é | Estado | Ler quando |
|---|---|---|---|
| `CLAUDE.md` | regras do projeto (honestidade, acervo, protótipo) | vigente | sempre |
| `CURRENT_STATUS.md` | **estado** do projeto | vigente | sempre, primeiro |
| `HISTORICO.md` | como chegamos aqui (só acrescenta) | vigente | para saber o porquê |
| `DECISIONS.md` | decisões e razões | vigente | antes de refazer algo decidido |
| `PLANO-DE-MELHORIA.md` | plano em árvore e **diretrizes aprovadas pelo Diogo em 28/10 tarde** (PageSpeed, bordas, rodapé, "nada perdido") | vigente | antes de propor qualquer coisa |
| **`estudo/visual/board-visual.html`** | **proposta visual aprovada (esta é a cópia que vale; a de `cliente/acervo-dropbox/extraido/` é anterior)** ("Como sair do site 2.0 do site deles"): diagnóstico das fotos, regras visuais, mockups, carro, sete sinais de empresa séria | **aprovado; parte feita (seção 4)** | **antes de propor foto, seção ou efeito** |
| **`cliente/ACERVO.md`** | registro de tudo que o cliente mandou (origem, data, tamanho, md5) e o que ainda não foi visto | vigente; **regra: conferir antes de dizer "não temos X"** | antes de afirmar ausência |
| `cliente/MATERIAL-RECEBIDO.md` | leitura do material (dossiê, Instagram, vídeos) | vigente | para o contexto do cliente |
| `SISTEMA-VISUAL.md` | tokens, fotos, erros a não repetir | vigente | antes de mexer em CSS |
| `DESIGN-DIRECTION.md`, `DIRECAO-DE-ARTE-V2.md` | direção de design | consulta | ao decidir visual |
| `REFERENCIAS.md` (raiz) e `estudo/refino-v4/nickho/MEDICAO.md` | referência (Nick Ho): o carro que desce e a coreografia medida (marcadores `start`/`end`, expo.out/expo.in, giro de 180° fora da tela) | consulta | ao fazer o carro |
| `estudo/refino-v4/lab.html` | laboratório votado (A, C, D, B) | fechado; votos na seção 3 | só para consultar |
| `estudo/estrategia-2026-10/` (01 a 09) | estratégia, SEO, voz do comprador, textos, **alertas legais**, **texto antigo × V3** | consulta | ao mexer em texto ou legal |
| `estudo/redes-sociais/` | repositórios e estilos de post | **é da outra sessão (proposta)** | não trazer para o site |
| `cliente/propuesta/`, `runbooks/passagem-2026-10-28-noite-proposta.md` | proposta ao cliente e os posts | **é da outra sessão** | não mexer daqui |
| `runbooks/medir-e-revisar.md`, `scripts/revisar-visual.mjs`, `runbooks/rastreo.md` | como medir (Lighthouse, robô) e rastreio | vigente | depois de cada mudança |
| `scripts/preparar-fotos.py` | receitas de TODAS as imagens do site (grade único) | vigente | para gerar imagem nova |
| `index.html` | **o site inteiro** (HTML, CSS e JS num arquivo só; ~100 KB) | vigente | sempre que mexer no site |
| `assets/` | fotos (`assets/fotos/`), fontes, vídeo (`assets/video/`), `track.js` (rastreio) | vigente | para trocar imagem ou peso |
| `aviso-legal.html`, `privacidad.html`, `cookies.html` | páginas legais com `[Pendiente: …]` | vigente | ao mexer em legal |
| `cliente/videos/`, `cliente/logos/`, `cliente/fotos-pista/`, `cliente/RCArcade_Dossier_Comercial_261027.pdf` | material do cliente de setembro (clipe do topo, logos, fotos de pista, dossiê comercial) | vigente | antes de pedir algo ao cliente |
| `MEMORY.md` (raiz do projeto) | lições locais do projeto | consulta | ao começar |
| `robots.txt`, `sitemap.xml`, `.nojekyll` | SEO e publicação (canonical ainda aponta para o `github.io`; trocar quando for ao domínio do cliente) | vigente | na ida ao ar |
| `cliente/acervo-dropbox/extraido/insta/` | **as 23 originais 4000×5000** de onde `preparar-fotos.py` lê (fora do git); sem elas o script não roda | vigente | para gerar imagem |
| `cliente/acervo-dropbox/extraido/web/` | `9882.jpg`… e `v02…v13.jpg`: **quadros parados** usados no quadro visual (numeração própria, **não** são os `f07…f28` do site) | consulta | só para ver o quadro visual |
| `cliente/acervo-dropbox/extraido/cont-video/` | o vídeo de Cheste e **duas extrações antigas** (`frames/f01–f15` e `hd01–hd15.jpg`), com numeração diferente da usada no site | consulta | não misturar |
| `cliente/RC-ARCADE-alineacion.pdf`, `cliente/alineacion-01.html`, `cliente/acervo-dropbox/site-antigo-rcarcade-es/` | alinhamento inicial e cópia do site antigo (`rcarcade.es`) | consulta | ao comparar com o site antigo |
| `scripts/shots.py`, `runbooks/capturar-telas.md`, `runbooks/revisao-visual/`, `estudo/vibe-coding-toolkit.md`, `CONCORRENTES.md`, `DESIGN-GATE-V2.md`, `ESTRUTURA-DO-SITE.md`, `ETAPA3-INPUTS-CLAUDE-DESIGN.md`, `PLANO-IMPLEMENTACAO-V2.md` | material de etapas antigas | **só histórico** | quase nunca |
| `TASKS.md` | **desatualizado desde 13/09** (tem faixa de aviso) | **não confiar** | nunca como estado |
| `runbooks/passagem-2026-10-28-noite-site.md` | passagem 1 do site | **substituída por esta** | só histórico |

## 2. Estado (28/10, noite)
- **No ar** (GitHub Pages, `main` = `544bca2`; no endereço público mediu-se 96 e ~722 KB, os 97/100/100/100 e ~714 KB abaixo são do servidor local): cortina de entrada curta (1,8 s), fotos do topo em WebP, 4 passos com título na foto, sistema de revelação (`.rv`, `data-rise`, `data-parallax`), faixa "UNA PISTA. HASTA SEIS PILOTOS." com a pista inteira, galeria por temas (aba "Con público"), capas dos cartões de imprensa (só Madrid com foto), fotos no alto de "Dos formas". Medido (celular, local): **97/100/100/100**, ~714 KB.
- **Só no computador (não publicado):** crédito "· Por Agencia Bienquisto" no rodapé (`index.html`). **Sem commit:** `CURRENT_STATUS.md`, `HISTORICO.md`, `TASKS.md`, `cliente/ACERVO.md`, as duas passagens e arquivos novos de `estudo/`. Fazer **commit de docs** no `hero-teste` na primeira oportunidade; o push continua só com "publica". O Diogo pediu o crédito **só no final**, não no topo.
- **Regra de publicação:** o trabalho vive no ramo `hero-teste`; publicar é `git push origin hero-teste:main` (a `main` local foi alinhada com a remota em 28/10; **o que vale é `origin/main`**). **Só com palavra explícita** ("publica", "sobe"). **"Manda o site" significa mandar o link**, não publicar (erro de 28/10). Commit de código leva `CURRENT_STATUS.md` e `HISTORICO.md` junto.
- **Arquivos não versionados** em `estudo/` (por exemplo `09-texto/cego/`, `refino-v4/nickho/*.mjs`, `_lab-*.png`): material de trabalho. Os PNG `_lab-*` são descartáveis; o resto pode entrar num commit de docs quando o Diogo quiser. Não misturar com commit de código do site.
- Link: https://diogotorresweb.github.io/rc-arcade/ · servidor local: `.claude/launch.json` (porta 8791) · celular no mesmo Wi-Fi: `http://192.168.1.6:8791/`.

> **Estado dos documentos:** `CURRENT_STATUS.md` foi reescrito nesta passagem (lista viva do que falta na seção "Próximo passo") e `cliente/ACERVO.md` foi corrigido (não diz mais que Cheste e as 23 fotos "não foram vistas"). Teste às cegas desta passagem: **7/10**; as 10 lacunas apontadas foram corrigidas aqui.

## 3. Decisões do Diogo (cumulativas; não reabrir)
- **Passos 1–4:** título dentro da foto, a cores, **texto pequeno** dentro; a frase explicativa fica **embaixo** da foto. Aprovado.
- **Revelação ao descer:** no site todo, como sistema e sem exagero (3 gestos). Aprovado. **Anton** como fonte de títulos de impacto (hoje só passos, faixa grande e palavra do topo; os `h2` ainda são Archivo, ver seção 5).
- **Lista que fica vermelha ao descer:** aprovada (ainda não implementada).
- **Carro que desce:** **modelo de rally** visto de cima (decisão de 28/10: "o de rally pode seguir"), coreografia do Nick Ho (desce e some; volta ao contrário ao subir; dá ré se parar e voltar); **se não ficar bem feito, o carro sai** e fica só a lista vermelha. **Atenção: há mais de um carro de rally no acervo**: o nº 22 "Power" (do topo do site, **sem** câmera) e carros de pintura branca/preta/verde **com câmera FPV** (fotos `DSC09882`, `9884`, `9901`; ao menos **duas unidades iguais**, uma com o nº 43 e outra com o nº 23, então não dá para afirmar que é um carro só). **DECIDIDO (Diogo, 28/10 fim da noite): usar o 43 com câmera** (pintura branca/preta/verde, câmera FPV no teto). **Ainda aberto (não respondido):** se o carro sair por não ficar bom, o mini-traçado ilustrativo que já está no site (`#circuit`, PC ≥ 1300 px) sai junto? Perguntar só se o carro for removido. O próprio quadro visual avisa que a foto 9882 "não é de cima de verdade" (ângulo inclinado, gira estranho).
- **Galeria:** abas + carrossel em bloco de altura fixa; P&B que ganha cor no hover (PC); no celular, cor ao centralizar (**tentar e olhar; se ficar ruim, só PC**). Aprovada em geral; tópicos e efeito do celular aguardam voto.
- **Protótipo:** imagem não é bloqueio (Red Bull, rosto, logos de terceiros), **mas a legenda e o rótulo não podem afirmar o que não se sabe** (o Diogo cobrou em 28/10: "o texto engana").
- **Peso:** orçamento de ~700 KB ao abrir; foto da galeria só carrega ao abrir a aba; toda imagem nova em WebP, dois tamanhos.
- **Texto:** V3 é a base; só 6 ideias curtas do antigo são candidatas e **aguardam o "pode"** (tabela contra simulador, fiabilidade antes de abrir a pista, o público como espetáculo, formatos nomeados, empresas/team building, marca como parte do recorrido); "simuladores" vira puestos/cockpits; a telemetria "de ejemplo" sai. **Nada disso foi aplicado ainda** (o site e o `CURRENT_STATUS.md` ainda dizem "simuladores"); depende do "pode" do Diogo. **Organizar o site não é enxugá-lo nem trazer o texto antigo todo.**
- **Modo de trabalhar (pedido dele):** rápido e assertivo; pergunta só quando falta decisão dele, com explicação clara; pode usar interview-me/grill-me (docs) se achar melhor. **Sempre passar `model` ao criar agente** (forte para estratégia e revisor cego; menor para medir e converter). Visão limpa: fechar com um parágrafo **Pronto.** em português simples.

## 4. O que o quadro visual prometia e onde está (conferido em 28/10)
Feito: fotos reais com um tratamento só, passos com foto, faixa grande, escalas, imprensa em cartões com título fantasma, rodapé institucional, contato, "zero resto de obra".
**Falta do quadro:** (a) carro com **a pista real de cima** (traçado desenhado a partir das tomadas aéreas, marcador e cronômetro por setor, ou o carro real de rally, ver seção 3); (b) **foto no título** de "La prueba" e "Cómo trabajamos" (a segunda não tem foto de montagem no acervo: pedir ao cliente); (c) **vídeos de Cheste** (v02, v03, v04, v08, v10, v13; voto B pendente: minha recomendação é fileira de vídeos verticais arrastáveis, que carregam ao tocar); (d) selos de apoio: **nada no acervo indica apoio público**, o espaço do rodapé fica reservado e só se preenche com arquivo e texto oficiais do cliente.

## 5. Falta fazer (ordem sugerida)
1. **Carro de rally visto de cima** (mecanismo medido em `REFERENCIAS.md` da raiz e em `estudo/refino-v4/nickho/MEDICAO.md`; versão de teste no lab, item D): fotos candidatas `DSC09882` (dois carros de cima) e `DSC09861`; refazer a vista de cima com IA só se ficar fiel (branco/preto com verde, câmera FPV); PNG/AVIF transparente ~320×573 PC e ~183×327 celular; mostrar ao Diogo antes de animar; **senão, remover**.
2. Lista que fica vermelha (aprovada). 3. Anton nos `h2` das seções (testar `ñ ¿ ¡ á é í ó ú`; já funciona em "SIÉNTATE").
4. **Voto do Diogo:** tópicos da galeria (Con público 8 · Pista 5 · Cabinas 4 · Coches 5 · Marcas en pista 6), efeito de cor no celular, foto da faixa grande (ele quer testar outra; alternativas no acervo: `DSC09893`, `DSC09875` já usada).
5. **Voto do Diogo** no vídeo (B) e o **"pode"** das 6 ideias do texto.
6. Fotos reais por evento (seção 6): hoje só o cartão de Madrid tem foto; TV e Zaragoza ficam só com a palavra até haver imagem confirmada.
7. Publicar o crédito do rodapé (só com "publica").

## 6. Origem do material: o que se sabe e o que NÃO se sabe
- **23 fotos profissionais** (`RCA-publicacion-insta.zip`, DSC09860–DSC09905, 4000×5000): usadas nos passos, faixa, escalas, contato e galeria. **Origem do evento: não confirmada.** Mesmo galpão (paredes brancas, escada, planta, pedestal laranja) das fotos de julho; **hipótese** de serem da jornada de Madrid (2–3 jul), **a confirmar com o cliente**.
- **Vídeo `RC ARCADE CHESTE HD.mp4`** (1080×1920, 59 s, evento num autódromo): os quadros f07, f09, f10, f11, f13, f15, f26, f28 estão na aba "Con público" (**um evento só**, por isso o rótulo não diz "Eventos"). Receita: `ffmpeg -i "cliente/acervo-dropbox/extraido/cont-video/RC ARCADE CHESTE HD.mp4" -vf fps=1/2 -q:v 2 <pasta>/f%02d.jpg` e depois `QUADROS_CHESTE=<pasta> python -I scripts/preparar-fotos.py` (no PowerShell: `$env:QUADROS_CHESTE="<pasta>"`). **O script regenera TODAS as imagens do site, não só as da galeria**, e precisa das originais em `extraido/insta/`. O quadro `f26` gera também a foto de "Dos formas, Evento" (`forma-evento`), o `f27` já não é usado (a capa de Madrid agora é a foto de celular de 3-7-26). Os "vídeos de Cheste" do quadro visual (`v02…v13`) são **quadros parados** de um vídeo só; **não há receita pronta para cortar clipes**: para vídeo de verdade, cortar com `ffmpeg -ss <início> -t <duração>` e ver cada trecho antes. Os quadros extraídos desta sessão estavam numa pasta temporária que **não existe mais**: refazer. **Cuidado:** já existe `cliente/acervo-dropbox/extraido/cont-video/frames/` (f01 a f15, **outra** extração, com intervalo diferente): não apontar `QUADROS_CHESTE` para ela, os números não batem com f07…f28 usados no site.
- **"Open Rcarcade"** (pasta enorme, 1–6 jul/26): **12 de 15 fotos** recuperadas de dentro do zip parcial para `cliente/acervo-dropbox/extraido/open-fotos/` (registradas no `ACERVO.md`); faltam `2-7-26 0 13 56`, `3-7-26 17 43 23`, `3-7-26 11 25 07`. A foto de **3-7-26 11:17** (visitante pilotando) é a capa de Madrid (datas da jornada). **Mais de 50 vídeos de julho nunca foram baixados nem vistos**; o link vive em `cliente/acervo-dropbox/LINKS.local.md` (**nunca copiar a chave para arquivo versionado**). Caminhos: baixar por arquivo, ou o Diogo clicar "Adicionar ao meu Dropbox".
- **7 vídeos "Avatar"** (`estreno lona`, ~8 GB): nenhum visto. **Também nunca vistos:** o áudio do vídeo de Cheste (não transcrito), as pastas `360/` e `action5/` do "Open Rcarcade", `test latencia.mov` e `RC Arcade Mad Ring Night.mp4` (só citados no `ACERVO.md`); `Editados` e `Jornada de puertas abiertas` vieram **vazias** do zip. **`logos rcarcade/`** (8 PNG): em `cliente/acervo-dropbox/extraido/cont-logos/`.
- **Eventos citados no site** (cartões de "Prensa y registro"): El Hormiguero 07/10 e Volrace Zaragoza 24–26/10 têm link público do Instagram, mas **a participação do cliente no El Hormiguero está "a confirmar"** (`CURRENT_STATUS.md`); a jornada de Madrid 2–3/07 vem do Instagram do cliente e das datas das fotos de julho. **Nenhuma foto do acervo está confirmada para El Hormiguero nem para Volrace.**

## 7. Pendências que dependem do cliente (não preencher com suposição)
Modelo comercial da instalação fixa, preço "desde", pessoas por hora, m² por escala, montagem, seguro; razão social, NIF e domicílio (páginas legais têm `[Pendiente]`); IDs de rastreio (GTM, GA4, Meta); logotipos de apoio (se houver); confirmação de telefone e e-mail comerciais; autorização de imagem das pessoas; fotos de montagem; fotos e vídeos por evento. Lista viva: "Dados do cliente que ainda faltam" em `CURRENT_STATUS.md`.

## 8. Como medir cada passo (todo passo mexe no peso)
`runbooks/medir-e-revisar.md`: robô `node scripts/revisar-visual.mjs http://localhost:8791/index.html <pasta>` e Lighthouse celular 3 vezes (mediana). Meta: **90+ no celular, 100 em acessibilidade/boas práticas/SEO** (hoje 97/100/100/100). Um `aria-label` em `<p>` custou 3 pontos de acessibilidade: texto para leitor de tela vai em `.sr-only`.

## 9. Lições desta sessão (já em `Recursos/aprendizados/`)
- Todas em `Recursos/aprendizados/passagem-perde-fontes-do-projeto.md` (lição nº 60): a passagem que perde fontes; "dado sem origem não vira legenda" (a aba "Eventos 01–08" sobre um evento só); "mandar o link não é publicar". Também há a memória `manda-o-site-e-mandar-o-link` (fora do repositório).
