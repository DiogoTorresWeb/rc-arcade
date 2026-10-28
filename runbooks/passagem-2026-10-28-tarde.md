# Passagem — RC Arcade, tarde de 28/10/2026

> Esta passagem **aponta** para os documentos, não os substitui. Se algo aqui contradiz `CURRENT_STATUS.md`, vale o `CURRENT_STATUS.md`.
> Para continuar: abrir conversa nova na pasta do projeto e dizer **"continuar o RC Arcade"**.

**Projeto:** RC Arcade, site B2B em espanhol (carro RC real + câmera FPV + cockpit, até 6 simuladores). Pasta
`C:\Users\Diogo Torres\diogo-base\Projetos\rc-arcade`. Branch de trabalho: `hero-teste` (o `main` é o site no ar). Nada foi enviado ao
GitHub; o `git push` é do Diogo.

## Leia nesta ordem
1. `diogo-base/AGORA.md`, seção 4
2. `CURRENT_STATUS.md` (estado e próximo passo)
3. `PLANO-DE-MELHORIA.md`, seção "Diretrizes aprovadas" (metas de PageSpeed, bordas, rodapé, síntese)
4. `TASKS.md`, item PRIMEIRO (a ordem de execução)
5. `cliente/ACERVO.md` (tudo que o cliente mandou e onde está) e `estudo/estrategia-2026-10/` (estudos 01 a 05)
6. `estudo/visual/board-visual.html` (a proposta visual aprovada; abrir pelo servidor local, porta 8791)

## O que o Diogo aprovou e pediu hoje
- "Perfeito": executar o quadro visual (fotos reais em cada seção; carro da rolagem com a pista de cima, opção 2).
- **Antes de qualquer coisa: consolidar a estratégia com um modelo bom, sem estourar limite.** Metas: PageSpeed e o que prende a atenção do contratante.
- Visual: **bordas finas e sutis, estilo cartões de produto da Apple, mais leves**; experiência pensada do topo ao fim; **rodapé institucional sério** (aviso legal, dados da empresa, selos oficiais só se reais).
- **Nada se perde**; pesquisa só onde muda o resultado; ir atrás sozinho do que falta; na dúvida do pedido, perguntar.

## Primeiro trabalho da próxima sessão: a síntese
Um agente só, modelo forte (Opus; Fable só se o Diogo liberar créditos), **sem pesquisa na web**. Lê: estudos 01 a 05, `PLANO-DE-MELHORIA.md`,
o quadro visual. Entrega `estudo/estrategia-2026-10/06-sintese.md` (até 3 páginas): o que fazemos, em que ordem, o que cortamos, as 10 decisões
que mais mexem no resultado. Depois o agente `revisor-cego` recebe **só a síntese** e a pergunta "o que está errado ou exagerado aqui?".
Sempre passar `model` ao criar agente.

## Estado do trabalho (fatos)
- **Site (`hero-teste`)**: hero intocado e aprovado. Já feito: formulário de contato (monta mensagem e abre WhatsApp/correio do cliente, sem servidor),
  botão de WhatsApp flutuante, "Cómo trabajamos", "Registro de pista" (Volrace Zaragoza, El Hormiguero, jornada de Madrid), 3 comentários públicos como
  prova **provisória** (sem nome de usuário), SEO (canonical, Open Graph, ícones, JSON-LD, robots, sitemap com endereço provisório do GitHub Pages).
- **Falta no site**: linha de base do PageSpeed; sistema de bordas (tokens); fotos nas seções; carro da rolagem; rodapé institucional; aviso legal e privacidade.
- **Acervo**: 23 fotos profissionais (4000 × 5000) e o vídeo `RC ARCADE CHESTE HD` (tomadas aéreas da pista) extraídos em `cliente/acervo-dropbox/extraido/`.
  A pasta "Open Rcarcade" do Dropbox segue **parcial** (30 GB); os 7 vídeos "Avatar" e o áudio do vídeo CHESTE não foram vistos/transcritos.
- **Achados confirmados hoje**: site do cliente (`rcarcade.es`) tem ~6 semanas, feito de um deck de 23 slides, logo e foto de abertura retocados por ChatGPT (nota 5/10);
  Google Meu Negócio com categoria "Engenheiro", sem site, sem avaliações, ponto no mar; Instagram com 11 posts e 422 seguidores e dois links quebrados na bio
  (`rcardace.com` não existe); El Hormiguero confirmado como colaboração oficial; marca RC ARCADE em tramitação na OEPM (05/10/2026) **em nome de pessoa física**.
- **Razão social e NIF**: não há empresa pública achada; só o cliente dá. Dado de pessoa física não se busca.
- **Decisões do Diogo ainda abertas**: cabeçalho A ou B; se `hero-teste` entra na `main` (site antigo guardado na tag `antes-v2-2026-10-27`); créditos do Fable.
- **Perguntas ao cliente** (lista em `PLANO-DE-MELHORIA.md`): quem fez o site, contatos comerciais, acesso ao Google e Instagram, logo original, m², preço,
  autorização de imagem, selos oficiais, razão social/NIF.

## Cuidados
- Telefone e e-mail no site são os que o cliente publicou; falta ele confirmar que são os comerciais.
- Foto com banner da Red Bull nunca se altera; só entra se o enquadramento esconder a marca.
- Pessoas nas fotos/vídeo: autorização de imagem pendente; escolher quadros sem rosto até lá. Repositório do site é **público**: nada pesado nem com rosto vai ao git.
- Servidor local: `.claude/launch.json` **deste** projeto (python, porta 8791). Não copiar para outras pastas.
- Ao rodar Python com texto que tem aspas e `\n` dentro de comando do shell, o texto quebra (já derrubou os scripts do site uma vez): gravar o script com a
  ferramenta de escrever e rodar o arquivo. Depois de editar o site, conferir com `node --check` nos blocos de script.
- Commit de código exige estado e histórico do projeto em dia; mudança de próximo passo muda também o `AGORA.md` da base (máx. 150 linhas).

## Skills sugeridas
- `superpowers:brainstorming`, antes de decidir o desenho de cada seção nova.
- `impeccable` e `design-taste-frontend`, ao construir o sistema de bordas e as seções com foto.
- `claude-seo:seo-technical` ou o PageSpeed Insights, para medir a linha de base e conferir as metas.
- `watch:watch`, para o áudio e os quadros dos vídeos pendentes.
- `humanizer`, no texto em espanhol antes de publicar.
