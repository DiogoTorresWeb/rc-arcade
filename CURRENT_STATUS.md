# RC Arcade — status atual

> Tipo: **estado** — reescrito quando muda. Não acumula histórico.
> Atualizado: 28/10/2026 (passagem da madrugada) · Revisar até: 27/11/2026 · Dono: Diogo
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
| ¿Cabe en tu espacio? | Formato antigo; faltam as medidas em m² do cliente | no ar; plano V2 item 6 |
| Tres vías | Formato antigo; foto com banner da Red Bull, que nunca se altera | no ar; plano V2 item 5 |
| Contacto | Redesenhada (fechamento silencioso); sem aprovação explícita do Diogo | no ar; faltam dados do cliente |
| **Ideias novas** (pedido de 27/10, só plano) | scroll com o carro descendo; modelo de "Contacto"; "Media y Artículos" — todos do nickho-motorsports.nl | `TASKS.md` |

## Próximo passo (pivô de 27/10: estratégia e acervo antes do scroll)

1. **Acervo:** conferir se o download de "Open Rcarcade" terminou (`cliente/acervo-dropbox/`), extrair os 3 zips,
   completar `cliente/ACERVO.md`. Ver os vídeos novos (`RC ARCADE CHESTE HD`, 7 "Avatar" de `estreno lona`)
   com o pipeline completo e procurar a **vista de cima do carro** em `360`, `action5` e nas 23 fotos.
2. **Estratégia:** quatro estudos prontos em `estudo/estrategia-2026-10/` (01 mercado, 02 SEO/GEO, 03 voz do comprador, 04 referências). Ler, corrigir `CONCORRENTES.md`, fazer a síntese, passar o
   revisor cego. A síntese em Fable depende de o Diogo liberar créditos (senão, Opus).
3. **Diogo decide depois da síntese:** cabeçalho A ou B; se `hero-teste` entra na `main` (versão antiga fica na
   tag `antes-v2-2026-10-27`); onde entra o scroll; "ré" ou não. Só então o V0, numa branch.
4. Depois, `PLANO-IMPLEMENTACAO-V2.md` no item 4.

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
