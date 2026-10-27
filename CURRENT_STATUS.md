# RC Arcade — status atual

> Tipo: **estado** — reescrito quando muda. Não acumula histórico.
> Atualizado: 27/10/2026 · Revisar até: 27/11/2026 · Dono: Diogo
> Regra: `../../SISTEMA.md`. Lições que valem aqui: `../../Recursos/aprendizados/INDEX.md`.
> Como chegamos aqui: `HISTORICO.md`. Por que é assim: `DECISIONS.md`.

**Cliente:** RC ARCADE (Espanha, material em espanhol) — pilotagem de carro RC real com câmera
FPV em primeira pessoa, num circuito físico; até 6 simuladores simultâneos, tempo de volta e
posição medidos. Site B2B para operador de centro de lazer. Identidade já existe: vermelho
`#E31B23`, preto `#0A0B0D`, prata `#B1B0AB`.

## Onde estamos

- **No ar** (`main` → GitHub Pages, https://diogotorresweb.github.io/rc-arcade/): `index.html`
  com o plano V2 em 3 de 12 itens — "Qué es" (timeline), "Para el operador" (manifesto), "Contacto"
  (fechamento silencioso). "Contacto" ainda **sem aprovação explícita** do Diogo.
- **Em teste, não publicado** (branch `hero-teste`): o topo com a palavra **CARRERA** gigante atrás
  do carro recortado, 3 microtextos de canto e botões estilo Autrix. Duas versões do cabeçalho:
  `?hero=a` (sem barra) e `?hero=b` (logo no centro + menu no canto). Para ver: na pasta do
  projeto, `python -m http.server 8791` e abrir `http://localhost:8791/index.html?hero=a`.

## Próximo passo (decisão do Diogo)

Avaliar o A/B do topo: **bom fica** (apaga a versão perdedora e faz merge), **mais ou menos
escala** (uma rodada de ajuste), **ruim volta** (apaga a branch). Depois, retomar o
`PLANO-IMPLEMENTACAO-V2.md` no item 4 (preparar os assets de "Tres vías" e "Escalas"; o plano ainda
diz "nenhum passo executado" — está defasado). Uma unidade por vez, com aprovação entre elas.

## Em aberto (nada disto foi corrigido ainda)

- **"La prueba" mostra "8 ms" e "Vuelta 4/6 — P1"**: não achei esses números no inventário do
  cliente (só "latência em ms" e "12 voltas, posição 02"). Podem estar no vídeo; conferir ou trocar.
- **Notas internas visíveis no site**: "Lo que todavía falta del cliente" e os nomes `TASKS.md` e
  `ESTRUTURA-DO-SITE.md` em "Escalas" e "Contacto".
- **SEO**: o `<title>` e a meta description ainda usam a frase antiga; o menu não tem link para
  "Tres vías". A frase do cliente "No miras la carrera…" saiu do topo e está provisória como
  rótulo em "Qué es".
- **Teste do `rc-arcade/CLAUDE.md`**: ainda não se confirmou se uma sessão nova aberta nesta
  pasta o carrega sozinha (`/context` → "Memory files").

## Dados do cliente que ainda faltam (não preencher com suposição)

Qual das 3 vias o site prioriza (premissa de trabalho: instalação fixa, **não confirmada por
escrito**); medidas reais em m²; contato comercial e se prefere formulário ou WhatsApp; onde fica e
se há unidade aberta ao público; clipe de vídeo dedicado para o topo; as 16 fotos "RCA publicacion
insta" (não estão no disco).

## Onde cada coisa mora

| Pergunta | Arquivo |
|---|---|
| Regras de trabalho deste projeto | `CLAUDE.md` |
| Tokens, movimento, HUD, hero | `DESIGN-DIRECTION.md` |
| Crítica de qualidade visual (15 dimensões) | `DIRECAO-DE-ARTE-V2.md` |
| Plano de execução e ordem | `PLANO-IMPLEMENTACAO-V2.md` |
| Revisão do plano antes de codar | `DESIGN-GATE-V2.md` |
| Estrutura de blocos da página | `ESTRUTURA-DO-SITE.md` |
| Referências visuais guardadas | `REFERENCIAS.md` |
| Material do cliente | `cliente/MATERIAL-RECEBIDO.md` |
| Como capturar telas em vários tamanhos | `runbooks/capturar-telas.md` |
