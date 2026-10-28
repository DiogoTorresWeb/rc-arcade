# Passagem — Proposta ao cliente RC Arcade (HTML), noite de 28/10/2026

> Esta passagem **aponta** para os arquivos, não os substitui. Se algo aqui contradiz `CURRENT_STATUS.md` ou o `SISTEMA.md` da base, valem eles.
> Modelo de passagem do projeto (não o handoff da Anthropic). Esta sessão cuida **só da proposta**; o refino do site (`index.html`) continua em outra sessão.

> **Para continuar:** abrir conversa nova na pasta do projeto (`rc-arcade`) e dizer **"continuar a proposta do RC Arcade"**; a IA lê esta passagem primeiro.

**Pasta:** `C:\Users\Diogo Torres\diogo-base\Projetos\rc-arcade\cliente\propuesta\` (fora do git de propósito: tem capturas do site antigo e dados do cliente).
**Regra de convivência:** esta sessão **não mexe** em `index.html`, `assets/` nem nas páginas legais do site. A outra sessão mexe.

## O que o Diogo quer desta sessão (nas palavras dele, resumido)
Pegar o HTML da proposta e **ajustá-lo até estar totalmente bom usando o modelo de votos da agência**: cada bloco da proposta
recebe voto **me pega / talvez / sai** e uma nota livre, e o que ficar entra; com **passo a passo** e **modelos para trocar**
(variantes de cada bloco: texto, ordem, tamanho). Ele não quer encher o contexto da sessão do site com isso, por isso vai para cá.

## O modelo de votos (ler antes de montar)
1. `Recursos/aprendizados/referencia-se-garimpa-e-se-vota-numa-pagina.md` — **página por etapas**, um cartão por item, com link/"repare em"/"cuidado", voto (me pega / talvez / não) + nota livre, **salvo num banco que a IA lê** (artefato com banco; usar a skill `artifact-capabilities`). **Nada é cortado escondido:** o que a IA tiraria entra numa etapa própria, com o motivo.
2. `Recursos/aprendizados/voto-de-gosto-nao-mede-venda.md` — cada cartão leva **duas perguntas**: "me pega?" (gosto) e "o cliente chamaria / o dono responderia? sim/não/porquê" (venda). **Antes de ir ao voto, o revisor cego responde a segunda sem saber dos votos.**
3. `Recursos/professor/RODA.md` item 9 e `Recursos/professor/estudo/identidade-visual/fontes/escolhas-do-diogo.md` (como foram lidos os votos de 18/10) e as páginas de exemplo em `Recursos/professor/estudo/identidade-visual/paginas/` e `.../votos/`.
4. Regra da base: `diogo-base/SISTEMA.md` e `diogo-base/CLAUDE.md`. Profundidade: método e fontes antes de opção; revisor cego antes de mostrar; modelo forte para estratégia/texto, modelo pequeno para tarefa mecânica; **sempre passar `model` ao criar agente**.

## Estado da proposta (fatos)
- **Arquivo final:** `propuesta-mejora-rcarcade.html` (espanhol, tuteo, um arquivo só, ~0,8 MB com imagens e fontes embutidas). Gerado por `python -I build.py` a partir de `plantilla.html` + `legal.html`. Conferir com `node ver.mjs` (capturas PC e celular em `img/_v-*.png`; precisa do Chrome e do `puppeteer-core` do cache do npx).
- **Blocos hoje:** 01 números (Lighthouse antes/depois) · 02 o que já mudamos (antes/depois + listas + 3 capturas) · 03 pontos fracos do site atual (tabela) · 04 Google Meu Negócio e Instagram · 05 "aviso de amigo" legal (4 itens visíveis + bloco que se abre) · 06 redes sociais (3 modelos de post + 6 tipos de publicação + como levaríamos) · 07 como seguimos ("adelante", 20 min, o que precisamos) · rodapé.
- **Modelos de post:** `posts.html` (3 posts 1080×1350 em HTML/CSS) → `render.mjs` gera `img/post-*-final.png`; fotos tratadas por `preparar.py` (mesmo acerto de cor do site). Fotos vêm de `cliente/acervo-dropbox/extraido/insta/` (originais 4000×5000, fora do git).
- **Dados medidos:** `lh/lh-old.json` (rcarcade.es) e `lh/lh-new.json` (site novo), Lighthouse móvel simulado, 28/10/2026, **uma rodada cada**.
- **Revisão cega já feita:** nota 5/10 e correções aplicadas — `Recursos/revisor-cego/revisoes/2026-10-28-propuesta-rcarcade.md`. Pesquisa legal (Opus, fontes oficiais): `estudo/estrategia-2026-10/08-alertas-legais-es.md`. Contexto do cliente: `PLANO-DE-MELHORIA.md`, `estudo/estrategia-2026-10/05-site-antigo-rcarcade-es.md`, `cliente/ACERVO.md`.
- `corrigir.py` foi um conserto **único, já aplicado**: não rodar de novo.

## Regras que não podem quebrar
- **Nada inventado:** número, evento, depoimento, preço. Dado que falta vira convite ou fica fora. Sem preço no documento (fica para a chamada).
- **Velocidade:** só citar o que sobrevive nas duas medições (Lighthouse simulado **e** observado). O LCP saiu da comparação porque o do site novo **observado** (2,5 s) é pior que o do antigo (0,7 s) por causa da cortina de entrada; **não prometer "rápido"** até a outra sessão corrigir. Medir de novo (3 rodadas, mediana) antes de reaparecer com número de tempo.
- **Tom:** de amigo, sem acusar. Não dizer que o logo/foto foram feitos por IA; não expor datas de modificação. Texto legal é orientação, "a confirmar" marcado, não é assessoria jurídica; patrocínio e direito de imagem de pessoas ficam fora.
- **Promessa:** nada de "traz contratos". O objetivo do Diogo é fechar o site e talvez a gestão de redes; o fecho é o convite "adelante".
- **Antes de mandar ao cliente:** revisor cego de novo na versão final. O Diogo revisa e envia (a IA não envia nada ao cliente).
- Python com aspas dentro de comando do shell quebra: gravar o script com a ferramenta de escrever e rodar o arquivo.

## Pedido novo do Diogo (28/10 noite, depois da passagem escrita): refazer os posts
Disse que o HTML da proposta "ficou perfeito", mas **os 3 modelos de post de Instagram estão ruins**: "parece que você pegou a foto dele e jogou um texto em cima".
Quer: **tratar a imagem como fizemos com a hero** (P&B de alto contraste, palavra gigante, filete vermelho), um estilo **mais vendável e com estratégia de marketing** (qual linha visual seguir, qual tipo de post por objetivo), e **pesquisar um repositório aberto do GitHub** sobre cuidado de posts/Instagram, **testar um** e ver se encaixa, **só para a parte de redes sociais**, não para o projeto todo. Quer sair de "legal, mas 60 de 100".
- Pesquisa já pedida (agente em segundo plano): `estudo/redes-sociais/01-repos-e-estilos.md` (repositórios, estilos de referência, formatos, 2 candidatos a testar). Ler primeiro; se o arquivo não existir, rodar a pesquisa de novo (modelo sonnet para listar, revisor cego para a recomendação).
- Os posts atuais: `posts.html` + `render.mjs` + `preparar.py` (ver acima). O teste do candidato escolhido vai numa página de voto (mesmo modelo me pega / talvez / sai, com "o cliente pararia de rolar? sim/não/porquê").

## Primeiro trabalho desta sessão
1. Ler os 3 documentos do modelo de votos e um exemplo de página de voto anterior. **O primeiro bloco a votar são os posts** (seção acima).
2. **Perguntar ao Diogo só o que travar** (ele pediu: dúvida besta se pergunta, sem parar o trabalho).
3. Montar a **página de voto da proposta** (artefato privado com banco): uma etapa por bloco (01 a 07), cada cartão com a captura/trecho do bloco, "repare em", "cuidado", voto me pega/talvez/sai, nota livre e "o dono responderia? sim/não/porquê"; mais uma etapa "o que eu tiraria" com o motivo.
4. **Variantes ("modelos para trocar")** para os blocos que mais pesam: abertura (título/resumo), a seção legal (curta × completa), o fecho (convite × proposta com pacote), e a ordem dos blocos.
5. Passar o revisor cego na pergunta "o dono responderia?" **antes** de mostrar; ler os votos do banco; ajustar `plantilla.html`/`legal.html`; regerar; revisor cego final; entregar o arquivo ao Diogo.
6. Ao fim: atualizar `CURRENT_STATUS.md` (linha da proposta) e `HISTORICO.md`; lição que vale para outro projeto vai para `Recursos/aprendizados/`.
