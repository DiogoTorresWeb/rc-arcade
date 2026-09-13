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

**Não instalado ainda:** o Diogo precisa rodar, dentro do Claude Code, na
pasta deste projeto:
```
/plugin marketplace add anthropics/claude-plugins-official
/plugin install superpowers@claude-plugins-official

/plugin marketplace add DietrichGebert/ponytail
/plugin install ponytail@ponytail

/plugin marketplace add JuliusBrussee/caveman
/plugin install caveman@caveman
```
Isso não dá pra fazer por aqui (é comando de dentro da sessão local dele).
