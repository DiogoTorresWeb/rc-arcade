# RC Arcade — status atual

> Tipo: **estado** — reescrito quando muda. Não acumula histórico.
> Atualizado: 28/10/2026 (noite, cortina encurtada e publicada) · Revisar até: 27/11/2026 · Dono: Diogo
> Regra: `../../SISTEMA.md`. Lições que valem aqui: `../../Recursos/aprendizados/INDEX.md`.
> Última passagem: `runbooks/passagem-2026-10-28-tarde.md`.
> Como chegamos aqui: `HISTORICO.md`. Por que é assim: `DECISIONS.md`. Próximos passos: `TASKS.md`.

**Cliente:** RC ARCADE (Espanha, material em espanhol) — pilotagem de carro RC real com câmera
FPV em primeira pessoa, num circuito físico; até 6 simuladores simultâneos, tempo de volta e
posição medidos. Site B2B para operador de centro de lazer. Identidade já existe: vermelho
`#E31B23`, preto `#0A0B0D`, prata `#B1B0AB`.

## Onde estamos (28/10 noite): site V3 **publicado** (main = hero-teste, commit 1fae62f)

**No ar desde 28/10/2026 (ordem do Diogo, "do jeito que está"):** `main` → GitHub Pages, https://diogotorresweb.github.io/rc-arcade/ (a versão antiga está na tag `antes-v2-2026-10-27`). Medido no endereço público (celular, Lighthouse): **96 · 100 · 100 · 100**, LCP 1,6 s, 722 KB; o site antigo `rcarcade.es` no mesmo teste: 74 · 89 · 96 · 91, LCP 13,5 s, 4,3 MB.
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
2. **Proposta ao cliente (28/10 noite):** `cliente/propuesta/propuesta-mejora-rcarcade.html` (espanhol, um arquivo só; fora do git): números antes/depois, trocas feitas, pontos fracos do site atual, Google Meu Negócio, Instagram, "aviso de amigo" legal (pesquisa em `estudo/estrategia-2026-10/08-alertas-legais-es.md`) e 3 modelos de post (evento, instalação fixa, perfil) em `cliente/propuesta/`. Gerar de novo: `python -I cliente/propuesta/build.py`. **Diogo revisa e envia.**
   Revisor cego da proposta: 5/10, correções aplicadas (tirei o LCP da comparação, texto legal enxuto com itens extras em "Para el siguiente paso", fecho com convite "adelante", sem promessa de contrato).
   **Achado sobre o NOSSO site:** no teste do Google o LCP *observado* do site novo foi 2,5 s contra 0,7 s do antigo (o simulado dá 1,6 s contra 13,5 s) e o Speed Index simulado é 4,7 s contra 2,0 s. A cortina da intro atrasa a primeira imagem visível. Investigar (reduzir a intro) antes de vender "rápido" ao cliente.
   **Sessão da proposta:** não abriu (o app estava em Remote Control, que não inicia sessão). Abrir pelo app e dizer "continuar a proposta do RC Arcade": passagem `runbooks/passagem-2026-10-28-noite-proposta.md` (modelo de votos me pega/talvez/sai; primeiro bloco: **refazer os 3 posts**, hoje fracos; pesquisa `estudo/redes-sociais/01-repos-e-estilos.md`).
   **Texto do site antigo × V3 (feito):** cego V3 7/10 × antigo 4/10; V3 fica como base, trazer só 6 ideias curtas do antigo (tabela contra simulador, público, marca, team building, lista dos 5 dados, rotação), trocar "simuladores" por puestos, tirar telemetria "de ejemplo"; **aguarda o "pode" do Diogo** (`estudo/estrategia-2026-10/09-texto/`). Correção dele: organizar o site não é enxugá-lo nem trazer o texto antigo todo.
   **Refino do site (60% → 100%):** votos do Diogo no laboratório `estudo/refino-v4/lab.html` (A: títulos dentro da foto nos passos, a cores, e galeria P&B por tópico abaixo; C: revelação no site todo; fonte Anton; D: lista vermelha aprovada, carro só se for o real e como o do Nick Ho, senão sai; B pendente). Medição do Nick Ho: `estudo/refino-v4/nickho/MEDICAO.md`. **Passagem para continuar: `runbooks/passagem-2026-10-28-noite-site.md`** (dizer "continuar o site do RC Arcade"). Cortina de entrada **já encurtada** (2,7 s → 1,8 s; Speed Index local 4,55 → 4,3 s, nota 97 igual). Próximo: ver o peso das imagens do topo e de baixo (Speed Index ainda ~4,3 s), depois os 4 passos com título dentro da foto.
   Refino do site (Diogo vê ~60% do resultado): referência nickdemotorsports.nl (fotos P&B que colorem no hover, vídeo em tela cheia, elementos no scroll, confirmar o carro no traçado) e skills de design/B2B. Mostrar visualmente antes de aplicar. Ainda não começou.
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
