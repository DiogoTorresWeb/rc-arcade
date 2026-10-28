# RC Arcade — status atual

> Tipo: **estado** — reescrito quando muda. Não acumula histórico.
> Atualizado: 28/10/2026 (noite, site V3) · Revisar até: 27/11/2026 · Dono: Diogo
> Regra: `../../SISTEMA.md`. Lições que valem aqui: `../../Recursos/aprendizados/INDEX.md`.
> Última passagem: `runbooks/passagem-2026-10-28-tarde.md`.
> Como chegamos aqui: `HISTORICO.md`. Por que é assim: `DECISIONS.md`. Próximos passos: `TASKS.md`.

**Cliente:** RC ARCADE (Espanha, material em espanhol) — pilotagem de carro RC real com câmera
FPV em primeira pessoa, num circuito físico; até 6 simuladores simultâneos, tempo de volta e
posição medidos. Site B2B para operador de centro de lazer. Identidade já existe: vermelho
`#E31B23`, preto `#0A0B0D`, prata `#B1B0AB`.

## Onde estamos (28/10 noite): site V3 montado na branch `hero-teste`

Site no ar hoje: `main` → GitHub Pages, https://diogotorresweb.github.io/rc-arcade/ (ainda a versão antiga). **A V3 está só na `hero-teste`, não commitada.**
Medido no servidor local (celular): **desempenho 97 · acessibilidade 100 · boas práticas 100 · SEO 100**, LCP 1,5 s, 789 KB; PC 99/100/100/100 (antes: 97/100/100/100, 603 KB).
O robô `scripts/revisar-visual.mjs` não acha erro, imagem quebrada, link quebrado nem rolagem lateral, em PC e celular.

| Seção | Estado |
|---|---|
| Topo (hero) | Intocado e aprovado; só mudaram os botões ("Pedir propuesta", "Evento o instalación fija") e o cabeçalho B (logo no centro, menu à direita) virou o padrão |
| Qué es | 4 passos com foto real cada (cartões de borda sutil); textos do redator, só com fonte |
| La prueba | Clipe real da pista em loop (1 MB, só carrega ao aparecer) + ficha com dados que têm fonte (12.3 V, 25 Mbps, 00:42.381, até 6). "8 ms" e "4/6 — P1" saíram |
| Lo que gana quien la contrata | Faixa de foto (escudo aceso) + 4 argumentos |
| Dos formas de contratarla | **Evento** e **Instalación fija** com o mesmo peso; competição como reforço |
| ¿Cabe en tu espacio? | Uma foto por escala; convite a mandar as medidas (sem m² inventado) |
| Cómo trabajamos | 4 passos do próprio cliente |
| Prensa y registro | Título fantasma + cartões que deslizam (El Hormiguero, Volrace, Madrid) + cartão vazio "tu nota" + 3 comentários públicos (provisórios) |
| Contacto | Foto escurecida ao fundo; formulário (evento primeiro, cidade, WhatsApp sem telefone/correo na mensagem, referência de campanha) |
| Rodapé | Institucional: contato, legal (aviso, privacidade, cookies, preferências), **espaço reservado** para logotipos oficiais de apoio (não são selos reais) |
| Carrinho da rolagem | Carro no traçado **ilustrativo** (PC ≥ 1300 px) + régua vermelha de progresso em qualquer tela; itens acendem ao passar pelo centro |
| Rastreio | `assets/track.js`: dataLayer, Consent Mode v2, faixa de cookies, eventos, UTM, API de Conversões. **Todos os IDs vazios.** Guia: `runbooks/rastreo.md` |
| Páginas legais | `aviso-legal.html`, `privacidad.html`, `cookies.html` com campos `[Pendiente: …]` (titular, NIF, domicílio) |

## Próximo passo (28/10 noite)

1. **Revisor cego já passou (nota 5/10) e as correções reais foram aplicadas:** faixa de cookies com botões iguais e só quando há ferramenta, revogação que apaga cookies, etiqueta de protótipo no cabeçalho (não cobre mais conteúdo), botão de pausa no vídeo, WhatsApp com contraste AA, promessas sem prova suavizadas, botão "Pedir propuesta" visível no cabeçalho do PC. **O que ele aponta e só o cliente resolve:** modelo comercial da instalação fixa, preço "desde", pessoas por hora, m², montagem, seguro, razão social (as respostas que o comprador procura).
2. **Diogo decide:** se `hero-teste` entra na `main` e vai ao ar (o site antigo fica na tag `antes-v2-2026-10-27`); créditos do Fable.
3. **Mandar ao cliente** as perguntas da seção 5 de `estudo/estrategia-2026-10/06-sintese.md` e pedir os identificadores de rastreio
   (GTM, GA4, Pixel da Meta), titular/NIF/domicílio, logotipos oficiais de apoio, confirmação de que telefone e e-mail são os comerciais.
4. Em segundo plano: terminar "Open Rcarcade"; transcrever o áudio do vídeo `RC ARCADE CHESTE HD`; ver os 7 vídeos "Avatar"; trocar os
   3 comentários provisórios por depoimentos reais.

## Decisões vigentes do Diogo (28/10)
- **Protótipo:** até o cliente aprovar e pagar, nada de imagem é bloqueio (rosto, Red Bull, logos). Banner de terceiro nunca se altera.
  Fica **público**, com aviso "Sitio en construcción · prototipo para el cliente" (e no rodapé); sem `noindex`.
- **Foco:** evento e instalação fixa com o mesmo peso; vai para onde vierem mais contratos.
- **Rastreio de ponta** desde o começo, com consentimento correto (ver `runbooks/rastreo.md`).
- Detalhe em `DECISIONS.md`. Sistema visual e erros a evitar: `SISTEMA-VISUAL.md`. Como medir e revisar: `runbooks/medir-e-revisar.md`.

**Achados que seguem valendo:** o cliente tem domínio próprio (`rcarcade.es`) com página antiga que é o 1º resultado no Google (o `canonical`
do protótipo ainda aponta para o `github.io`: trocar ao publicar no `.es`); concorrente chinês (Wehop) também promete até 6;
o comprador faz conta (m², pessoas por hora) e o dossiê não traz número: pedir ao cliente. Plano em árvore: `PLANO-DE-MELHORIA.md`.

## Em aberto
- **Dados legais:** razão social, NIF e domicílio (a marca está em nome de pessoa física); páginas legais têm `[Pendiente]`.
- **Textos que dependem do cliente:** m² por escala, pessoas por hora, preço, demonstração, peças/suporte, latência.
- **Carrinho da rolagem:** o traçado é ilustrativo; se o cliente mandar a planta da pista, redesenhar fiel.
- **Servidor da API de Conversões:** o site já envia o aviso; falta o receptor (GTM de servidor ou função serverless).
- **`rc-arcade/CLAUDE.md`**: não se confirmou se uma sessão nova nesta pasta o carrega sozinha (`/context` → "Memory files").

## Dados do cliente que ainda faltam (não preencher com suposição)

Qual das 3 vias o site prioriza (premissa: instalação fixa, **não confirmada por escrito**);
medidas reais em m²; contato comercial e se prefere formulário ou WhatsApp; onde fica e se há
unidade aberta ao público; clipe de vídeo dedicado para o topo; as 16 fotos "RCA publicacion
insta" (não estão no disco). **Não há artigos nem imprensa no material do cliente** (ver o El Hormiguero no estudo 02, a confirmar) — "Media y Artículos" não
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
| Material do cliente (leitura) e registro de tudo que chegou | `cliente/MATERIAL-RECEBIDO.md` e `cliente/ACERVO.md` |
| Estudos de estratégia (27/10) | `estudo/estrategia-2026-10/` |
| Capturar telas em vários tamanhos | `runbooks/capturar-telas.md` |
