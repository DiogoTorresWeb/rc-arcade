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

## Regra do acervo: nunca perder material do cliente (Diogo, 27/10/2026)
Todo material que o cliente mandou (dossiê, vídeo, fotos, logos, pastas do Dropbox), usado ou não,
fica guardado inteiro e registrado em `cliente/ACERVO.md`. Nada é descartado por "não entrou no
site". Material novo entra no acervo e no registro **no mesmo dia em que chega**, com origem, data,
tamanho e impressão digital (md5). Os arquivos pesados moram em `cliente/acervo-dropbox/` e em
`cliente/` (fora do git por tamanho e por mostrar pessoas, o repositório do site é público); o
registro vai no git. Link de Dropbox com chave **nunca** vai para arquivo versionado. Antes de
dizer "não temos X", conferir o `ACERVO.md`. Perder contexto do material já custou caro nesta
conversa: o Diogo teve de reenviar o dossiê e o vídeo.

## Documentação como fonte da verdade
Três arquivos nesta pasta: `CURRENT_STATUS.md` (onde está), `DECISIONS.md`
(o que foi decidido e por quê), `TASKS.md` (o que falta). Se não está neles,
não aconteceu. Ver `estudo/vibe-coding-toolkit.md` pras ferramentas adotadas
(Superpowers primeiro; o resto só quando fizer sentido).

## Segurança (herdado do `diogo-base/CLAUDE.md`)
Nunca hardcode segredo/chave de API. `.env` + `.gitignore` antes do primeiro
commit real de código. Rotacionar qualquer chave que vazar.
