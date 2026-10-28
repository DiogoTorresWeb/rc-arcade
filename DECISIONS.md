# RC Arcade — decisões

## [2026-09-13] Estrutura inicial do projeto
**Decisão:** criar a pasta como repositório próprio dentro de
`diogo-base/Projetos/rc-arcade/` (já previsto no `.gitignore` da base — projeto
de cliente não versiona junto com a base pessoal).

**Método:** seguir `metodo.md` da agência à risca — a Regra Zero existe
justamente por causa do site do irmão (copiar estrutura do site do Paulo só
trocando tema, pra um público totalmente diferente). RC Arcade é B2B; Paulo é
B2C emocional. Não reaproveitar layout, só o método.

**Ferramenta adotada:** Superpowers (plugin oficial do Claude Code, gratuito) —
obriga o fluxo brainstorm → plano → implementação → revisão antes de qualquer
código. É a mesma ideia da Etapa 1 do método, só que como plugin de verdade em
vez de disciplina manual. Ver `estudo/vibe-coding-toolkit.md` pra origem e
resto das ferramentas do mesmo kit (a maioria não se aplica ainda — projeto
não tem código nenhum pra revisar, orquestrar ou linkar em grafo).

**Atualizado 13/09:** o playbook completo do toolkit foi lido de verdade (não só
a bio) e virou skill central em `professor/skills/vibe-coding-toolkit-setup/SKILL.md`
— vale pra todo projeto novo, não só este. Além do Superpowers, também adotamos
**Ponytail** (evita over-engineering) e **Caveman** (corta resposta enrolada e
mostra token economizado — o RTK do kit não é instalável, esses dois são).

**Instalado em 13/09/2026:** os 3 plugins foram instalados de verdade no
Claude Code local do Diogo (scope: user, vale pra qualquer projeto, não só
este). Precisou primeiro atualizar o Claude Code (`npm install -g
@anthropic-ai/claude-code@latest`) — a versão antiga não tinha `/plugin`
disponível. Comandos usados:
```
/plugin marketplace add anthropics/claude-plugins-official
/plugin install superpowers@claude-plugins-official

/plugin marketplace add DietrichGebert/ponytail
/plugin install ponytail@ponytail

/plugin marketplace add JuliusBrussee/caveman
/plugin install caveman@caveman
```

## [2026-09-13] Material do cliente recebido — Etapa 1 quase fechada

**O que chegou:** dossiê comercial em PDF (20 páginas, espanhol, "LAUNCH
EDITION 2026"), vídeo real de 42s de uma sessão rodando, e 3 pastas de
Dropbox (fotos de evento, fotos profissionais pra Instagram, e a pasta
`logos rcarcade` com os arquivos de marca).

**Qualidade do material:** alta. O cliente já sabe se posicionar — o dossiê
tem frase-âncora ("No miras la carrera. Estás dentro de ella."), mecânica em
4 passos, 4 públicos mapeados, argumento B2B pro operador, e identidade
visual completa. Inventariado em `cliente/MATERIAL-RECEBIDO.md`.

**Decisão de método:** a Etapa 1 NÃO fecha ainda, mesmo com material bom. O
dossiê apresenta 3 modelos de negócio (instalação fixa / evento temporal /
formato competição) como se fossem iguais, e não diz qual o site deve
priorizar. Um site que tenta atender os três não atende nenhum. Essa decisão
é do Diogo + cliente, não minha — fica como primeira tarefa em `TASKS.md`.

**Correção que afeta a Etapa 3:** a identidade visual do RC Arcade já existe
(vermelho/preto/prata com significado definido, sistema de logo em 9
variações, estética escura de corrida/tecnologia). Então a técnica do
@matheusgomes muda de papel: o Claude Design não inventa a identidade, ele
constrói o **sistema de design web** fiel à identidade que já existe. A
referência do Behance vira padrão de layout e estrutura, não fonte visual.

**Ponto de atenção (regra de honestidade):** as fotos das pastas mostram
pessoas identificáveis. Antes de qualquer foto ir pro site, confirmar
autorização de uso de imagem com o cliente.

## [2026-09-13] Documento de alinhamento como formato padrão

**Problema:** as perguntas da Etapa 1 (qual das 3 vias, B2B ou B2C) são
grandes demais pra WhatsApp, e o cliente mandou um dossiê muito bem feito —
responder com mensagem solta seria responder abaixo do nível dele.

**Decisão:** criar um documento de alinhamento em PDF, em espanhol, com
estrutura de 6 partes: o que entendi → o que já está resolvido → decisões com
recomendação → o que preciso receber → como seguimos.

**Princípio que guia o formato:** não perguntar aberto, oferecer decisão com
opções, recomendação e raciocínio. Cliente paga por opinião, não por menu.

**Virou reutilizável:** `professor/skills/documento-de-alinhamento/SKILL.md`
— serve pra próximo cliente e pra conversa de sociedade com o Paulo.

**Arquivos:** `cliente/RC-ARCADE-alineacion.pdf` (o que vai pro cliente) e
`cliente/alineacion-01.html` (fonte, pra editar e regerar).

## [2026-09-13] Autorização de material e premissa de trabalho

**Autorização:** o Diogo confirmou que todo o material enviado está liberado
para uso — as pessoas que aparecem nas fotos são da equipe do cliente, e o
dossiê foi montado justamente para ser utilizado. Isso encerra a pendência de
direito de imagem que eu tinha levantado. (Continua valendo o bom senso: usar
o que serve, não tudo indiscriminadamente.)

**Premissa de trabalho:** o Diogo relatou que a preferência do cliente é
praticamente 100% alinhada com as recomendações do documento de alinhamento —
instalação fixa como via principal, evento temporal como segunda porta,
competição como apoio; B2B como percurso principal com seção pública curta.
Ainda **não confirmado por escrito** (cliente viajando).

**Decisão:** seguir com essa premissa em vez de parar. Registrado como
premissa, não como fato — se o cliente voltar e corrigir, muda a seção de
vias e a pública; o resto da estrutura se sustenta.

## [2026-09-13] Direção de design: o movimento é o produto

**Contexto:** o Diogo trouxe como referência sites de narrativa contínua em
scroll (ex.: barbearia com câmera indo da rua até dentro da loja) — como
possibilidade de pensamento, não como regra, e já apontando que esse tipo de
site costuma converter mal.

**Decisão:** não copiar esse padrão. Esses sites inventam movimento porque o
produto deles é parado. O RC Arcade não precisa: o produto dele já é uma
câmera em movimento, e o vídeo FPV real é mais forte que qualquer transição
animada.

**Regra adotada:** o movimento do site é o movimento do produto; nada de
movimento decorativo sobre conteúdo parado. Sequestro de scroll está proibido
no caminho B2B — o operador não pode perder controle da página.

**Camada visual:** usar a linguagem de HUD que já existe no produto
(telemetria do vídeo: voltagem, Mbps, latência; cronômetro e deltas do dossiê)
como vocabulário gráfico. O site deve parecer a tela do cockpit, não um
template escuro genérico de tecnologia.

**Tokens de marca extraídos do dossiê por análise de pixel** (não chutados):
vermelho **#E31B23** (idêntico no logo e nos acentos), preto #0A0B0D,
superfície #191A1E, prata #B1B0AB. Detalhe em `DESIGN-DIRECTION.md`.

## [2026-10-27] Topo reaberto para teste — palavra gigante atrás do carro
**Status:** EM TESTE na branch `hero-teste` (não publicada). Direção, não lei: o Diogo pediu
"se for bom fica, mais ou menos escalamos, ruim voltamos". Reabre o topo, que o
`PLANO-IMPLEMENTACAO-V2.md` mandava não mexer.

**Decidido pelo Diogo, em entrevista (27/10):**
- Referência: pôster "SEPTEMBER" (palavra enorme atrás da montanha) e Behance "Autrix".
- Palavra gigante **CARRERA** (de 8 candidatas do Opus, todas ligadas ao material do cliente).
- 3 microtextos de canto, conjunto "operador": "Atracción FPV para centros de ocio", "Hasta 6
  simuladores, un circuito", "Coches RC reales en primera persona" (a de "alquiler" ficou fora:
  o dossiê não diz se é aluguel).
- Fonte **Anton** agora; testar outra mais para a frente, não agora.
- Botões do topo no estilo do print do Autrix (vermelho cheio + secundário translúcido).
- Sai do topo: o selo "Telemetría en cabina" com a bolinha e o ícone de sinal, e a frase
  "No miras la carrera. Estás dentro de ella." (vai para outra seção).
- Teste A/B do cabeçalho: A sem barra nenhuma sobre o topo; B logo RC no centro e só o menu no canto.

**Escolhas minhas, a confirmar:** a frase do cliente virou rótulo (`.tag`) acima do título de "Qué
es"; o parágrafo de apoio do topo ("Coches RC reales, cámara FPV…") foi removido do topo (segue na
meta description); o cronômetro "Mejor vuelta" foi mantido.

**Como é feito (não desfazer sem saber):** três camadas do mesmo quadro — foto, `<h1>` Anton em
`cqw`, carro recortado em WebP com transparência. O recorte usa só a máscara do BiRefNet; a cor vem
do próprio hero tratado, por isso alinha ao pixel. Um polígono remove o caminhão desfocado do fundo.

**Risco aceito:** o `<h1>` passa a ser só "Carrera" (os termos de busca ficam nos microtextos, no
`<title>` e na meta description — ainda não atualizados); o teto do carro cobre a base das letras,
e em telas muito largas o "E" pode lembrar um "F"; o recorte de 2560 px pesa 229 KB em WebP (em
AVIF seriam ~89 KB, otimização guardada se o teste ficar).

## [2026-10-27] Topo: versão atual finalizada (supera o "EM TESTE" da entrada anterior)
**Decidido pelo Diogo:** a versão atual do topo está finalizada ("funcionou bem"); voltamos nele
para refinos depois. Segue na branch `hero-teste`; **ainda não registrado**: se o cabeçalho é A ou
B e se a branch entra na `main`. Referência continua sendo direção, não lei.

## [2026-10-27] Qualidade da entrega decide a ferramenta
**Decidido pelo Diogo:** a escolha do recorte do carro com o caminho de melhor qualidade (rembg +
BiRefNet, que exigiu instalar o Visual C++ da Microsoft) em vez do mais rápido foi o acerto. Vira
modo de trabalho **pelo resultado, não pela ferramenta**: quando a qualidade final difere de
verdade, o caminho de melhor qualidade é o padrão e o custo de preparo se absorve; um modelo de IA
que não entrega algo que surpreenda é trocado por um melhor. Lição geral em
`../../Recursos/aprendizados/ferramenta-se-escolhe-pelo-resultado-de-entrega.md`.

## [2026-10-27] Estratégia antes do scroll; antes e depois separados; acervo sagrado
**Decidido pelo Diogo:** (1) antes de construir o scroll do carro, redocumentar o projeto e rodar a pesquisa de
estratégia completa (SEO, marketing, referências, o que funciona para este cliente) com o maior modelo
disponível; (2) a imagem do carro sai de "olhar tudo": dossiê, vídeo e Dropbox, e só se não houver nada se
discutem alternativas; (3) versão antiga e nova ficam separadas para medir o caminhar antes e depois (tag
`antes-v2-2026-10-27` na `main`; segundo repositório só se ele quiser dois endereços públicos);
(4) **regra global do projeto: nunca perder material do cliente** (`CLAUDE.md`).
**Escolha minha, a confirmar:** pesquisa em Opus porque o Fable exige créditos pagos; o cabeçalho A/B segue
em aberto.

## [2026-10-28 tarde] Execução do site V3: síntese primeiro, bordas sutis, rodapé institucional
**Decisão (Diogo):** aprovou o quadro visual (fotos reais do cliente em cada seção, carro da rolagem com a pista de cima) e pediu para executar tudo de forma pensada, mirando as metas de PageSpeed e o que prende a atenção do contratante. Antes, consolidar a estratégia com um modelo forte, sem estourar limite. Ideia visual dele: bordas finas e sutis como os cartões de produto da Apple, só que mais leves, e um rodapé institucional sério (aviso legal, dados da empresa, selos oficiais).
**Por quê:** o site tinha texto bom e quase nenhuma imagem; o cliente tinha 23 fotos profissionais e um vídeo aéreo que não eram usados.
**Como aplicar:** ordem e metas em `PLANO-DE-MELHORIA.md` ("Diretrizes aprovadas"). A pergunta dos selos (UE, Comunitat Valenciana) virou regra: só entram se o cliente os tiver de verdade.
**Escolhas minhas, a confirmar:** meta interna de nota 90+ no celular; síntese em 1 só agente (Opus) em vez de vários; carro da rolagem na opção 2 (traçado da pista de cima com marcador), por ser fiel ao produto e leve.

## [2026-10-28 noite] Foco em evento, parte de instalação fixa, cabeçalho B, protótipo público
**Decidido pelo Diogo:** (1) o site trata **evento** como foco, porque é como o cliente se apresenta no site oficial dele, e ganha uma parte de **instalação fixa**; onde chegarem mais contratos, o foco vai para lá. (2) **Cabeçalho B** (logo no centro, menu no canto direito), já como padrão no código; o A continua em `?hero=a`. (3) O protótipo fica **público**, com aviso pequeno e fixo "Sitio en construcción · prototipo para el cliente" (e no rodapé); sem `noindex`. (4) A **prova** (vídeo, registro de pista, comentários) pode entrar quando quisermos: o material veio do cliente e do site dele, autorização assumida. Antes: imagem de terceiro não bloqueia o protótipo (regra do protótipo em `CLAUDE.md`).

## [2026-10-28 noite] Rastreio de ponta desde o começo, estratégia para os dois focos, execução do quadro visual
**Decidido pelo Diogo:** (1) o site nasce com a infraestrutura de rastreio de um site de ponta (Meta, Google, API): `assets/track.js`, IDs vazios até o cliente passar, tudo só com consentimento. (2) Executar o quadro visual inteiro sem parar: fotos em cada seção, bordas sutis estilo Apple, carrinho da rolagem, rodapé institucional com espaço para apoios oficiais (espaço reservado, nunca selo inventado), textos fortes para evento e instalação fixa. (3) Usar modelos fortes para estratégia e menores para tarefas simples, com revisão automática no caminho.
**Escolhas minhas:** consentimento com aceitar/recusar de peso igual (guia da AEPD) e Consent Mode v2; o formulário não leva telefone nem correo no WhatsApp; a palavra CARRERA existe desde o início atrás da cortina da intro (só sobe 14 px ao abrir) para o PageSpeed não punir o topo; o carrinho corre num traçado ilustrativo (os quadros do vídeo são em perspectiva, não dá para medir a pista); botão "Pedir propuesta" em vez de "Solicitar demostración".

## [2026-10-28 noite] Votos do Diogo no laboratório de refino (estudo/refino-v4/lab.html)
**Decidido pelo Diogo:** (A) fotos com o título dentro da imagem entram nos 4 passos (elige/siéntate/conduce/compite), **a cores**; o preto e branco que ganha cor no hover vai para uma **galeria por tópicos mais abaixo** no site. (C) o efeito de linhas que aparecem ao descer foi o preferido: quer testar no site inteiro, de forma estratégica. (Fonte) **Anton** passa a ser a fonte dos títulos de impacto; o cliente não exige tipografia. (B) vídeo em tela cheia no PC perdeu qualidade: ele pediu minha opinião (manter com mais vídeos ao lado ou tirar). (D) carro grande: sem voto ainda.
**Por quê (medido):** o clipe do site é vertical (540×960, ~1 MB) e esticado em tela larga perde nitidez; o do Nick Ho pesa 10–22 MB e carrega desde o início.
**Escolhas minhas, a confirmar:** vídeos verticais arrastáveis que só carregam ao tocar (sem tela cheia forçada); revelação como sistema de no máximo 3 gestos, um momento forte por seção; tópicos da galeria: Pista, Cabinas, Coches, Eventos. Detalhe em `runbooks/passagem-2026-10-28-noite-site.md`.

## [2026-10-28 noite] D: lista vermelha fica; carro só se for o carro real e como o do Nick Ho
**Decidido pelo Diogo:** a lista que fica vermelha ao descer está aprovada, e as fontes do laboratório também. O carro como estava no laboratório **não serve** (no celular cruzava a página toda). Quer o carro **igual ao site de referência**, numa seção só: desce e some; ao voltar para cima volta ao contrário; se parar e voltar durante a descida, volta de ré. Tem de ser o **carro real do cliente** visto de cima (de vídeo, de take ou refeito com IA). **Se não ficar bem feito, o carro sai** e só fica o efeito da lista em vermelho.
**Por quê:** o carro era um desenho genérico e preso à tela toda; a graça da referência é a coreografia (entra por gatilho, desliza, sai, gira fora da tela).
**Como aplicar:** `runbooks/passagem-2026-10-28-noite-site.md` (item D) e o mecanismo medido em `REFERENCIAS.md` (27/10).
