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
