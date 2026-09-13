# RC Arcade — instruções pra qualquer IA trabalhando aqui

Site B2B pra empresa de pilotagem de carrinho RC com câmera FPV. Cliente:
operadores de centro de lazer, eventos, ligas de competição — não é o mesmo
tipo de decisão de compra do site do Paulo (fotógrafo, decisão emocional
B2C). Ver `CURRENT_STATUS.md` pro estado atual e `../../Areas/agencia/metodo.md`
pro método completo da agência.

## Regra zero
Não copiar a estrutura de nenhum site pronto (nem o do Paulo) só trocando o
tema. Já deu errado uma vez (site do irmão). O que se reaproveita é o método.

## Regra de honestidade
Nenhum dado do cliente pode ser inventado: depoimento, nome de evento,
categoria de serviço, número, estatística. Campo vazio, nunca chute. Se faltar
informação, perguntar ou marcar como pendente em `CURRENT_STATUS.md` — nunca
preencher com suposição.

## Documentação como fonte da verdade
Três arquivos nesta pasta: `CURRENT_STATUS.md` (onde está), `DECISIONS.md`
(o que foi decidido e por quê), `TASKS.md` (o que falta). Se não está neles,
não aconteceu. Ver `estudo/vibe-coding-toolkit.md` pras ferramentas adotadas
(Superpowers primeiro; o resto só quando fizer sentido).

## Segurança (herdado do `diogo-base/CLAUDE.md`)
Nunca hardcode segredo/chave de API. `.env` + `.gitignore` antes do primeiro
commit real de código. Rotacionar qualquer chave que vazar.
