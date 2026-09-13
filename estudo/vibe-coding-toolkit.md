# vibe-coding-toolkit — o que serve pro RC Arcade agora

Fonte: github.com/soumatheusgomes/vibe-coding-toolkit (repo público, MIT, do
criador @matheusgomes que o Diogo acompanha no Instagram). Lido de verdade em
13/09/2026 — isto não é a legenda de um reel, é o conteúdo real do repositório.

## Usa agora
- **Superpowers** — plugin oficial do Claude Code (gratuito, do marketplace
  da própria Anthropic). Obriga o fluxo brainstorm → plano → implementação →
  revisão antes de escrever código. É literalmente a Etapa 1 do método da
  agência, virada ferramenta. Instalar:
  ```
  /plugin marketplace add anthropics/claude-plugins-official
  /plugin install superpowers@claude-plugins-official
  ```
- **Quality gates (ESLint, regra de 350 linhas por arquivo)** — instala com um
  prompt colado no Claude Code, sem custo. Vale configurar assim que o projeto
  tiver o primeiro código, não antes.

## Serve mais pra frente (quando tiver código de verdade)
- **Ponytail** (persona que força simplicidade) e **Caveman** (corta
  enrolação da resposta) — plugins de terceiros, gratuitos, mudam como o
  Claude decide e comunica. Testar quando já estiver no meio da implementação.
- **Subagent orchestration** (ondas paralelas) — útil quando o projeto tiver
  várias frentes ao mesmo tempo; pra um site simples de cliente, provavelmente
  nem vai precisar.
- **Graphify** (grafo de conhecimento do código) — só faz sentido quando já
  existir código pra mapear. Zero uso hoje.

## Não é gratuito de verdade / tem custo escondido
- **RTK** (proxy de token) não é um pacote pra instalar — é um padrão que o
  autor construiu pra própria produção; teria que ser recriado do zero. Não
  vale o esforço agora.
- **Obsidian** — o próprio Diogo já deixou essa decisão pra depois (ver
  `organizacao-projetos`). O kit assume Obsidian pra memória de longo prazo;
  aqui, por enquanto, `MEMORY.md` + `DECISIONS.md` fazem o mesmo papel, sem
  depender de mais uma ferramenta.

## Regra de honestidade do próprio kit (bate com a nossa)
O toolkit também tem gate de qualidade e revisão antes de aceitar código —
mesmo espírito da regra de honestidade do método da agência: nada inventado,
tudo verificável.
