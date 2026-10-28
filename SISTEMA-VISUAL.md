# RC Arcade — sistema visual (a árvore que liga site, Instagram e cartão)

> Tipo: **decisão/referência** — 28/10/2026. Fonte dos valores: `index.html` (`:root` e bloco "V3"). Detalhe de movimento: `DESIGN-DIRECTION.md`.

Uma regra só vale para tudo: **fundo preto, texto prata, um filete vermelho como sinal, fotografia real com o mesmo acerto de cor,
bordas finas quase invisíveis.** O site manda; o resto copia dele.

## Tokens
| O que | Valor | Uso |
|---|---|---|
| Preto | `#0A0B0D` | fundo de tudo |
| Superfície | `#191A1E` | cartões e campos |
| Prata | `#B1B0AB` · apagado `#8B8D8C` | texto corrido, rótulos |
| Vermelho | `#E31B23` | **só sinal gráfico** (filete, ponto, botão principal). Em texto pequeno reprova o contraste: nunca em corpo de texto |
| Linha | `rgba(255,255,255,.08)` · forte `.16` | borda de cartão e foto |
| Cartão | gradiente branco 4% → 1% + brilho de 1px no topo | cartão de produto estilo Apple, mais leve |
| Cantos | cartão 20 px · foto 16 px · botão e campo 12 px | |
| Fontes | Archivo 400/500 (texto) · JetBrains Mono (rótulo em caixa alta, números) · Anton (só palavras gigantes) | |

## Fotografia
- Todas as fotos passam por `scripts/preparar-fotos.py`: contraste suave, sombras frias, vermelho mais vivo, grão leve.
- Dois tamanhos de imagem: **faixa larga** (folego) e **vertical 4:5** (detalhe). Nunca quatro cartões iguais de foto sem hierarquia.
- Banner de terceiro (Red Bull etc.) **nunca se altera**. Para o protótipo, direito de imagem não bloqueia (ver `DECISIONS.md`).

## Movimento (só o que tem razão)
Régua vermelha de progresso no topo · carrinho que corre no traçado ilustrativo (PC largo) · itens que acendem ao passar pelo centro ·
clipe da pista em loop. Todo o resto parado e leve. `prefers-reduced-motion` = sem suavização.

## Como levar para outros lugares
- **Instagram:** fundo `#0A0B0D`, foto tratada com o mesmo script, um filete vermelho de 2 px acima do título, texto em Archivo, rótulo em caixa alta mono.
- **Cartão de visita:** preto, logo à esquerda, um filete vermelho, telefone e e-mail em mono prata; verso com uma foto da pista tratada.
- **Proposta/PDF:** mesma grade (fundo preto, títulos em Archivo 400, cartões com linha de 1 px).
- **Voz:** frases curtas, "tú", sem adjetivo vazio; "simulador" sempre junto de "coches reales"; só o que tem prova (ver `estudo/estrategia-2026-10/07-textos-es.md`).

## Erros a não repetir (lições deste projeto)
1. Número ou fato sem fonte no site ("8 ms", "Vuelta 4/6 — P1" já custaram retrabalho). Dado que falta vira convite, nunca chute.
2. Nenhuma foto pesada sem versões menores e `loading="lazy"`; o topo manda no PageSpeed.
3. Estrutura de site pronto copiada só trocando o tema (já deu errado com o site do irmão). Copiamos o método, não o layout.
4. Selo ou logotipo oficial inventado. Espaço reservado vale; selo falso não.
5. Segredo (token, chave) dentro do código. Fica fora do repositório.
6. Medir PageSpeed enquanto outra coisa pesada roda no mesmo computador (contamina a nota).
7. Rodar scripts com aspas dentro de comando de shell: gravar o script em arquivo e rodar o arquivo.
