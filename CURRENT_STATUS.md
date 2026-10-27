# RC Arcade — status atual

> Tipo: **estado** — reescrito quando muda. Não acumula histórico.
> Atualizado: 27/10/2026 (passagem do fim do dia) · Revisar até: 27/11/2026 · Dono: Diogo
> Regra: `../../SISTEMA.md`. Lições que valem aqui: `../../Recursos/aprendizados/INDEX.md`.
> Como chegamos aqui: `HISTORICO.md`. Por que é assim: `DECISIONS.md`. Próximos passos: `TASKS.md`.

**Cliente:** RC ARCADE (Espanha, material em espanhol) — pilotagem de carro RC real com câmera
FPV em primeira pessoa, num circuito físico; até 6 simuladores simultâneos, tempo de volta e
posição medidos. Site B2B para operador de centro de lazer. Identidade já existe: vermelho
`#E31B23`, preto `#0A0B0D`, prata `#B1B0AB`.

## Onde estamos, seção por seção (pre-check de 27/10)

Site no ar: `main` → GitHub Pages, https://diogotorresweb.github.io/rc-arcade/.

| Seção | Estado | Onde |
|---|---|---|
| Topo (hero) | **Versão atual finalizada** pelo Diogo ("funcionou bem"); voltamos para refinos depois. Palavra CARRERA atrás do carro recortado. Falta registrar: cabeçalho A ou B? | branch `hero-teste` (17ef1d9), **não está na `main`** |
| Qué es | Redesenhada (timeline) | no ar |
| La prueba | Formato antigo. "8 ms" e "Vuelta 4/6 — P1" sem fonte no inventário | no ar; plano V2 item 7 |
| Para el operador | Redesenhada (manifesto) | no ar |
| ¿Cabe en tu espacio? | Formato antigo; faltam as medidas em m² do cliente | no ar; plano V2 item 6 |
| Tres vías | Formato antigo; foto com banner da Red Bull, que nunca se altera | no ar; plano V2 item 5 |
| Contacto | Redesenhada (fechamento silencioso); sem aprovação explícita do Diogo | no ar; faltam dados do cliente |
| **Ideias novas** (pedido de 27/10, só plano) | scroll com o carro descendo; modelo de "Contacto"; "Media y Artículos" — todos do nickho-motorsports.nl | `TASKS.md` |

## Próximo passo

1. **Diogo:** dizer se o cabeçalho é A (`?hero=a`, sem barra) ou B (`?hero=b`, logo no centro +
   menu no canto) e se a branch `hero-teste` entra na `main`.
2. **Claude, em sessão nova:** abrir `nickho-motorsports.nl` no navegador e **medir** como o carro
   desce no scroll (tecnologia, paradas, diferença PC/celular) antes de planejar; confirmar o
   entendimento com o Diogo; só então fazer o V0. Uma unidade por vez, com aprovação entre elas.
3. Depois, `PLANO-IMPLEMENTACAO-V2.md` no item 4 (o plano ainda diz "nenhum passo executado").

## Em aberto (nada disto foi corrigido ainda)

- **"La prueba" mostra "8 ms" e "Vuelta 4/6 — P1"**: não estão no inventário do cliente (só
  "latência em ms" e "12 voltas, posição 02"). Podem estar no vídeo; conferir ou trocar.
- **Notas internas visíveis no site**: "Lo que todavía falta del cliente" e os nomes `TASKS.md` e
  `ESTRUTURA-DO-SITE.md` em "Escalas" e "Contacto".
- **SEO**: `<title>` e meta description ainda usam a frase antiga; o menu não tem "Tres vías". A frase
  "No miras la carrera…" saiu do topo e está provisória como rótulo em "Qué es".
- **`rc-arcade/CLAUDE.md`**: não se confirmou se uma sessão nova nesta pasta o carrega sozinha
  (`/context` → "Memory files").
- **Ver no celular**: `localhost` só abre no PC. Na mesma rede Wi‑Fi, `http://<IP do PC>:8791/…`
  (era 192.168.1.6); o firewall do Windows pode bloquear — não se confirmou que abriu.

## Dados do cliente que ainda faltam (não preencher com suposição)

Qual das 3 vias o site prioriza (premissa: instalação fixa, **não confirmada por escrito**);
medidas reais em m²; contato comercial e se prefere formulário ou WhatsApp; onde fica e se há
unidade aberta ao público; clipe de vídeo dedicado para o topo; as 16 fotos "RCA publicacion
insta" (não estão no disco). **Não há artigos nem imprensa** no material — "Media y Artículos" não
entra com texto inventado.

## Onde cada coisa mora

| Pergunta | Arquivo |
|---|---|
| Regras de trabalho deste projeto | `CLAUDE.md` |
| Tokens, movimento, HUD, hero | `DESIGN-DIRECTION.md` |
| Crítica de qualidade visual | `DIRECAO-DE-ARTE-V2.md` |
| Plano de execução e ordem | `PLANO-IMPLEMENTACAO-V2.md` |
| Revisão do plano antes de codar | `DESIGN-GATE-V2.md` |
| Estrutura de blocos da página | `ESTRUTURA-DO-SITE.md` |
| Referências visuais guardadas | `REFERENCIAS.md` |
| Material do cliente | `cliente/MATERIAL-RECEBIDO.md` |
| Capturar telas em vários tamanhos | `runbooks/capturar-telas.md` |
