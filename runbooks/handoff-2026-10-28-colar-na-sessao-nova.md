# Handoff curto (colar na sessão nova) — RC Arcade, site, 28/10/2026

> Este texto **aponta**; a passagem completa é `runbooks/passagem-2026-10-28-noite-site-2.md` (testada às cegas duas vezes, 7/10). Se algo aqui
> contradiz a passagem ou `CURRENT_STATUS.md`, valem eles. Cole este bloco inteiro como primeira mensagem da sessão nova.

**Projeto:** RC Arcade (`C:\Users\Diogo Torres\diogo-base\Projetos\rc-arcade`), site B2B em espanhol de simuladores com carrinhos RC reais e câmera FPV.
Ramo de trabalho `hero-teste`; no ar (`main` = `544bca2`): https://diogotorresweb.github.io/rc-arcade/

**Antes de qualquer ação:**
1. Leia `runbooks/passagem-2026-10-28-noite-site-2.md` **inteira** (a seção 1 é o manifesto de todas as fontes; a seção 0 tem 6 perguntas de abertura).
2. Depois `CURRENT_STATUS.md` (lista viva em "Próximo passo"), `estudo/visual/board-visual.html` (proposta visual aprovada) e `cliente/ACERVO.md`.
3. Rode `git status --short` e liste o que existe no projeto que a passagem **não cita**, como manda a regra global em `~/.claude/CLAUDE.md`.
4. **Antes de dizer "não temos X", confira o `ACERVO.md`.** Dado sem origem não vira legenda.

**Próximo trabalho: o "carro que desce".** Decidido pelo Diogo: **carro de rally nº 43 com câmera FPV**, visto de cima, coreografia do Nick Ho
(desce e some; volta ao contrário ao subir; dá ré se parar e voltar); **se não ficar bem feito, o carro sai** e fica só a lista vermelha ao descer
(já aprovada, ainda não feita). Medição: `REFERENCIAS.md` (raiz) e `estudo/refino-v4/nickho/MEDICAO.md`. Fotos candidatas: `DSC09882`, `9884`, `9901`
(a 9882 não é de cima de verdade). Mostrar ao Diogo antes de animar. **Pergunta ainda sem resposta, só se o carro for removido:** o mini-traçado
ilustrativo (`#circuit`) sai junto?

**Estado local sem commit:** crédito "Por Agencia Bienquisto" no rodapé (`index.html`), `CURRENT_STATUS.md`, `HISTORICO.md`, `TASKS.md`, `cliente/ACERVO.md`
e as duas passagens. Fazer **commit de docs** no `hero-teste`. **Publicar (`git push origin hero-teste:main`) só quando o Diogo disser "publica" ou "sobe".**
"Manda o site" significa mandar o **link**.

**Como trabalhar com o Diogo:** rápido e assertivo; pergunta só quando falta decisão dele; fecha cada resposta com um parágrafo **Pronto.** em português simples
(visão limpa); passar `model` ao criar agente (forte para estratégia e revisor cego, menor para medir e converter). Peso: orçamento de ~700 KB ao abrir;
medir Lighthouse (celular, 3 vezes) e rodar `scripts/revisar-visual.mjs` depois de cada mudança.

## Skills sugeridas para a sessão nova
- `superpowers:brainstorming` — antes de montar o carro (decidir como achar ou refazer a vista de cima).
- `animate` — coreografia do carro (curvas, duração, interrupção ao voltar a rolagem, `prefers-reduced-motion`).
- `impeccable` ou `design-taste-frontend` — acabamento visual do carro e da lista vermelha.
- `humanizer` — qualquer texto novo em espanhol (as 6 ideias do texto antigo, quando o Diogo der o "pode").
- `superpowers:verification-before-completion` — antes de dizer que algo está pronto (robô, Lighthouse, olhar no celular).
- Agente `revisor-cego` (com `model` forte) — antes de publicar e para testar a próxima passagem.

## Pendências de voto do Diogo (não decidir por ele)
Tópicos da galeria (Con público 8 · Pista 5 · Cabinas 4 · Coches 5 · Marcas en pista 6); efeito de cor no celular (tentar, se ficar ruim só PC); foto da faixa grande
(ele quer testar outra); vídeos de arrastar (recomendação: vídeos verticais que carregam ao tocar); "pode" das 6 ideias do texto antigo.

## Para o estudo à parte do Diogo
`Recursos/aprendizados/passagem-perde-fontes-do-projeto.html` (o erro de passagem que perde fontes; regra provisória em `~/.claude/CLAUDE.md`).
