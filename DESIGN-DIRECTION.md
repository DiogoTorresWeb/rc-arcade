# Direção de design — RC Arcade

Escrito em 13/09/2026, a partir do material do cliente e da conversa com o
Diogo sobre "futurista, mas com conversão".

## Tokens reais, extraídos do dossiê (não chutados)

Amostrados por análise de pixel das páginas do PDF do cliente — o vermelho é
idêntico no logo (p.17) e nos acentos de seção (p.6), então é o valor de marca
de verdade.

| Token | Valor | Papel (palavras do cliente) |
|---|---|---|
| `--rc-red` | **#E31B23** | Energia e competição. Acento, nunca fundo de área grande. |
| `--rc-black` | **#0A0B0D** | Fundo profundo da página. |
| `--rc-surface` | **#191A1E** | Superfície de card/seção — é o cinza-preto dominante do dossiê. |
| `--rc-silver` | **#B1B0AB** | Precisão e caráter mecânico. Texto secundário, réguas, detalhe. |
| `--rc-silver-dim` | **#8B8D8C** | Texto terciário, legendas. |
| branco | #FFFFFF | Texto principal. |

Escala e tipografia ficam pra Etapa 3 (Claude Design). O que está travado aqui
é a paleta, porque ela veio do cliente e não é negociável.

## A pergunta do "futurismo" — e a resposta

O Diogo trouxe como referência sites com narrativa contínua em scroll (o
exemplo dele: uma barbearia onde a câmera vai da rua até dentro da loja). Ele
mesmo já apontou o problema: esses sites costumam converter mal.

**A resposta pro RC Arcade é melhor do que copiar esse padrão.**

Esses sites usam movimento porque o produto deles é parado — uma loja, um
imóvel. Precisam inventar movimento pra criar sensação. **O RC Arcade não
precisa inventar nada: o produto dele É uma câmera em movimento.** A imagem
FPV real, gravada do carro, é mais impressionante que qualquer transição
animada — e já existe, já está filmada, e já temos permissão de usar.

Então a regra é:

> **O movimento do site é o movimento do produto. Nada de movimento decorativo
> por cima de conteúdo parado.**

Isso entrega a sensação de futuro que o Diogo quer, sem pagar o preço de
conversão, porque o movimento não está atrasando a informação — ele É a
informação.

## A segunda camada: a linguagem de HUD

No vídeo da sessão real aparece um overlay de telemetria na tela do piloto:
voltagem (12.3v), taxa de transmissão (25Mbps), latência em ms, barras de
sinal. E no dossiê (p.10) aparece o cronômetro: `00:42.381`, voltas, posição,
diferença `+0.814`.

Essa é a linguagem visual "futurista" que o site pode usar **com legitimidade**,
porque é literalmente o que o piloto vê:

- Números grandes em fonte monoespaçada
- Cronômetro e deltas de tempo como elemento gráfico, não só como dado
- Réguas finas, cantos marcados, indicadores de estado — vocabulário de HUD
- Vermelho como sinal (marcador ativo, melhor volta), não como enfeite

**O site deve parecer a tela do cockpit, não um template escuro genérico de
"tecnologia".** Essa é a diferença entre futurismo emprestado e futurismo que
vem do produto.

## Inventário de movimento — o que entra e o que não entra

**Entra (movimento que É o produto):**
- Vídeo FPV real em tela cheia no topo, mudo, em loop, com poster frame
- Cronômetro contando / delta de tempo animando quando entra na tela
- Contadores dos números de capacidade (6 simuladores, etc.)
- Micro-interação em elemento de HUD (barra de sinal, indicador de estado)

**Não entra (movimento que atrasa informação):**
- Sequestro de scroll — nunca. O operador que veio ver capacidade e rotação
  não pode perder o controle da página.
- Animação de entrada que esconde os números do operador até ele rolar
- Parallax por cima de texto
- Animação de abertura da página (intro) — custa os primeiros 3 segundos, que
  são os que decidem

**Com cuidado:**
- Transição entre seções: leve e rápida (≤250ms), nunca bloqueante
- Respeitar `prefers-reduced-motion` — quem desligou animação no sistema vê a
  versão estática, e o site continua fazendo sentido

## A restrição honesta: peso e mobile

Site com vídeo pesado morre em conexão móvel, e é exatamente aí que o tal
"baixa conversão" acontece — não é o movimento em si, é o carregamento.
Regras:
- Vídeo sempre com poster frame (primeiro frame como imagem), carregamento
  preguiçoso, e nunca como bloqueio pro conteúdo aparecer
- Versão estática funcional: se o vídeo não carregar, a página continua
  vendendo sozinha
- O conteúdo que o operador precisa (capacidade, escala, contato) nunca fica
  atrás de um vídeo

## Onde o padrão "cinema em scroll" pode entrar

Num lugar só: a seção de "como se sente" — a passagem do lado de fora do
circuito pra dentro da visão FPV. É a única parte da página onde a emoção vale
mais que a informação. Curta, e com o resto da página sem isso.

## Referência do Behance (pra Etapa 3)

Critério de busca pro passo do Claude Design, coerente com tudo acima:
- Buscar por **dashboard / telemetry / racing UI dark**, não por "landing page
  bonita"
- Escolher projeto **completo** (que mostre tipografia, grid, ícones e estados)
- Descartar referência que seja só estética escura sem estrutura de dados —
  precisamos de vocabulário de números e HUD, não de fundo preto com gradiente
