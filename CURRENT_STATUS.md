# RC Arcade — status atual

> Tipo: **estado** — reescrito quando muda. Não acumula histórico.
> Atualizado: 28/10/2026 (tarde, passagem) · Revisar até: 27/11/2026 · Dono: Diogo
> Regra: `../../SISTEMA.md`. Lições que valem aqui: `../../Recursos/aprendizados/INDEX.md`.
> Como chegamos aqui: `HISTORICO.md`. Por que é assim: `DECISIONS.md`. Próximos passos: `TASKS.md`.

**Cliente:** RC ARCADE (Espanha, material em espanhol) — pilotagem de carro RC real com câmera
FPV em primeira pessoa, num circuito físico; até 6 simuladores simultâneos, tempo de volta e
posição medidos. Site B2B para operador de centro de lazer. Identidade já existe: vermelho
`#E31B23`, preto `#0A0B0D`, prata `#B1B0AB`.

## Onde estamos, seção por seção (pre-check de 27/10)

Site no ar: `main` → GitHub Pages, https://diogotorresweb.github.io/rc-arcade/.

| Seção | Estado | Onde |
|---|---|---|
| Topo (hero) | **Versão atual finalizada** pelo Diogo ("funcionou bem"); voltamos para refinos depois. Palavra CARRERA atrás do carro recortado. Falta registrar: cabeçalho A ou B? | branch `hero-teste` (17ef1d9), **não está na `main`** |
| Qué es | Redesenhada (timeline) | no ar |
| La prueba | Formato antigo. "8 ms" e "Vuelta 4/6 — P1" sem fonte no inventário | no ar; plano V2 item 7 |
| Para el operador | Redesenhada (manifesto) | no ar |
| ¿Cabe en tu espacio? | Formato antigo; sem medidas em m² (o cliente não deu). O "pendente" virou convite a mandar as medidas | `hero-teste` (28/10), não no ar |
| Tres vías | Formato antigo; foto com banner da Red Bull, que nunca se altera | no ar; plano V2 item 5 |
| Contacto | **Feito em 28/10:** formulário (monta mensagem e abre WhatsApp/correio do cliente), botão de WhatsApp flutuante, canais diretos. Números e e-mail são os públicos do cliente, **a confirmar** que são os comerciais | `hero-teste`, não no ar |
| Cómo trabajamos, Registro de pista | **Novas em 28/10:** 4 passos do próprio cliente; Volrace Zaragoza, El Hormiguero, jornada de Madrid; 3 comentários públicos como prova **provisória** | `hero-teste`, não no ar |
| **Ideias novas** (pedido de 27/10, só plano) | scroll com o carro descendo; modelo de "Contacto"; "Media y Artículos" — todos do nickho-motorsports.nl | `TASKS.md` |

## Próximo passo (28/10 tarde: o Diogo aprovou; ordem em `TASKS.md`, item PRIMEIRO)

Feitas na branch `hero-teste` (hero intocado): contato, SEO e provas (etapas 2.1 e 2.2). Aprovado o quadro visual
(`estudo/visual/board-visual.html`). Próximo, nesta ordem:
1. **Síntese da estratégia** (1 agente forte, só arquivos locais, saída `estudo/estrategia-2026-10/06-sintese.md`) + revisor cego.
2. **Linha de base do PageSpeed** do site de hoje; depois fotos, bordas e carro da rolagem; no fim, medir de novo.
3. **Sistema de bordas sutis** (tokens) e **rodapé institucional**; razão social e NIF só o cliente dá (a marca está em nome de pessoa física).
4. **Diogo decide:** cabeçalho A ou B; se `hero-teste` entra na `main` (antigo na tag `antes-v2-2026-10-27`); créditos do Fable.
Em segundo plano: terminar "Open Rcarcade"; transcrever o áudio do vídeo `RC ARCADE CHESTE HD`; ver os 7 vídeos "Avatar".

**Achados que já mudam o rumo (ainda sem decisão):** o botão principal talvez deva ser "Solicitar demostración";
o operador compra número (m², jogadores por hora, retorno), e o dossiê não traz nenhum — pedir ao cliente; há
concorrente chinês (Wehop) que também promete até 6 com telemetria; a carga mais forte que sobra é o vídeo real.
O estudo 02 achou que **o cliente já tem domínio próprio (rcarcade.es), com uma página antiga que é o 1º resultado no
Google**, e que o El Hormiguero (Antena 3) fez uma corrida num "simulador de RC Arcade" em 07/10/2026 (ser o mesmo cliente
não está confirmado). Isso muda onde publicar o site e o item "não há imprensa" abaixo. O estudo 03 mostra que o comprador faz conta (m², pessoas por hora, pessoal), teme quebra e peça, e desconfia de foto
feita por IA: o vídeo real com telemetria deve abrir o site. Detalhe nos estudos 01 a 04.
**Plano em árvore: `PLANO-DE-MELHORIA.md` (28/10).** Auditoria do Google Meu Negócio (categoria "Engenheiro", sem site, sem avaliações, ponto no mar) e do Instagram (11 posts, 422 seguidores; **El Hormiguero confirmado**: colaboração oficial com @rcarcade, 6,2 mil curtidas). Estudo 05 (28/10): o site do `.es` tem ~6 semanas (conteúdo de 15–17/09/2026, HTTPS só desde 01/10/2026), é um deck de 23 slides virado página única, com logo e foto de abertura retocados por ChatGPT (assinatura da OpenAI nos arquivos); nota 5/10 como site de captação. Data de registro do `.es` não verificada.

## Em aberto (nada disto foi corrigido ainda)

- **"La prueba" mostra "8 ms" e "Vuelta 4/6 — P1"**: não estão no inventário do cliente (só
  "latência em ms" e "12 voltas, posição 02"). Podem estar no vídeo; conferir ou trocar.
- **Notas internas visíveis no site**: "Lo que todavía falta del cliente" e os nomes `TASKS.md` e
  `ESTRUTURA-DO-SITE.md` em "Escalas" e "Contacto".
- **SEO**: `<title>` e meta description ainda usam a frase antiga; o menu não tem "Tres vías". A frase
  "No miras la carrera…" saiu do topo e está provisória como rótulo em "Qué es".
- **`rc-arcade/CLAUDE.md`**: não se confirmou se uma sessão nova nesta pasta o carrega sozinha
  (`/context` → "Memory files").
- **Ver no celular**: `localhost` só abre no PC. Na mesma rede Wi‑Fi, `http://<IP do PC>:8791/…`
  (era 192.168.1.6); o firewall do Windows pode bloquear — não se confirmou que abriu.

## Dados do cliente que ainda faltam (não preencher com suposição)

Qual das 3 vias o site prioriza (premissa: instalação fixa, **não confirmada por escrito**);
medidas reais em m²; contato comercial e se prefere formulário ou WhatsApp; onde fica e se há
unidade aberta ao público; clipe de vídeo dedicado para o topo; as 16 fotos "RCA publicacion
insta" (não estão no disco). **Não há artigos nem imprensa no material do cliente** (ver o El Hormiguero no estudo 02, a confirmar) — "Media y Artículos" não
entra com texto inventado.

## Onde cada coisa mora

| Pergunta | Arquivo |
|---|---|
| Regras de trabalho deste projeto | `CLAUDE.md` |
| Tokens, movimento, HUD, hero | `DESIGN-DIRECTION.md` |
| Crítica de qualidade visual | `DIRECAO-DE-ARTE-V2.md` |
| Plano de execução e ordem | `PLANO-IMPLEMENTACAO-V2.md` |
| Revisão do plano antes de codar | `DESIGN-GATE-V2.md` |
| Estrutura de blocos da página | `ESTRUTURA-DO-SITE.md` |
| Referências visuais guardadas | `REFERENCIAS.md` |
| Material do cliente (leitura) e registro de tudo que chegou | `cliente/MATERIAL-RECEBIDO.md` e `cliente/ACERVO.md` |
| Estudos de estratégia (27/10) | `estudo/estrategia-2026-10/` |
| Capturar telas em vários tamanhos | `runbooks/capturar-telas.md` |
