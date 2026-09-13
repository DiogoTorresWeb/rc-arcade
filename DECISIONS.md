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

**Não instalado ainda:** o Diogo precisa rodar, dentro do Claude Code, na
pasta deste projeto:
```
/plugin marketplace add anthropics/claude-plugins-official
/plugin install superpowers@claude-plugins-official
```
Isso não dá pra fazer por aqui (é um comando de dentro da sessão local dele).
