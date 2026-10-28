# RC Arcade — status atual

> Tipo: **estado** — reescrito quando muda. Não acumula histórico.
> Atualizado: 28/10/2026 (noite, refino do site publicado) · Revisar até: 27/11/2026 · Dono: Diogo
> Regra: `../../SISTEMA.md`. Lições que valem aqui: `../../Recursos/aprendizados/INDEX.md`.
> Última passagem: `runbooks/passagem-2026-10-28-noite-site-2.md` (manifesto completo de fontes; **substitui** a primeira da noite).
> Como chegamos aqui: `HISTORICO.md`. Por que é assim: `DECISIONS.md`. Próximos passos: seção "Próximo passo" abaixo (`TASKS.md` está desatualizado).

**Cliente:** RC ARCADE (Espanha, material em espanhol) — pilotagem de carro RC real com câmera
FPV em primeira pessoa, num circuito físico; até 6 simuladores simultâneos, tempo de volta e
posição medidos. Site B2B para operador de centro de lazer. Identidade já existe: vermelho
`#E31B23`, preto `#0A0B0D`, prata `#B1B0AB`.

## Onde estamos (28/10 noite): site V3 **publicado** (`main` = `hero-teste`, commit 544bca2)

**No ar desde 28/10/2026 (ordem do Diogo, "do jeito que está"):** `main` → GitHub Pages, https://diogotorresweb.github.io/rc-arcade/ (a versão antiga está na tag `antes-v2-2026-10-27`). Medido no endereço público (celular, Lighthouse): **96 · 100 · 100 · 100**, LCP 1,6 s, 722 KB; o site antigo `rcarcade.es` no mesmo teste: 74 · 89 · 96 · 91, LCP 13,5 s, 4,3 MB.
Medido no servidor local (celular): **desempenho 97 · acessibilidade 100 · boas práticas 100 · SEO 100**, LCP ~1,7 s, ~714 KB (28/10 noite, depois do refino); PC 99/100/100/100 (antes: 97/100/100/100, 603 KB).
O robô `scripts/revisar-visual.mjs` não acha erro, imagem quebrada, link quebrado nem rolagem lateral, em PC e celular.

| Seção | Estado |
|---|---|
| Topo (hero) | Intocado e aprovado; só mudaram os botões ("Pedir propuesta", "Evento o instalación fija") e o cabeçalho B (logo no centro, menu à direita) virou o padrão |
| Qué es | 4 passos com foto real cada (cartões de borda sutil); textos do redator, só com fonte |
| La prueba | Clipe real da pista em loop (1 MB, só carrega ao aparecer) + ficha com dados que têm fonte (12.3 V, 25 Mbps, 00:42.381, até 6). "8 ms" e "4/6 — P1" saíram |
| Lo que gana quien la contrata | Faixa de foto (escudo aceso) + 4 argumentos |
| Dos formas de contratarla | **Evento** e **Instalación fija** com o mesmo peso; competição como reforço |
| ¿Cabe en tu espacio? | Uma foto por escala; convite a mandar as medidas (sem m² inventado) |
| Cómo trabajamos | 4 passos do próprio cliente, em lista grande (Anton) que fica vermelha ao descer, com o carro nº 43 de cima passando ao lado (local, não publicado) |
| Prensa y registro | Título fantasma + cartões que deslizam (El Hormiguero, Volrace, Madrid) + cartão vazio "tu nota" + 3 comentários públicos (provisórios) |
| Contacto | Foto escurecida ao fundo; formulário (evento primeiro, cidade, WhatsApp sem telefone/correo na mensagem, referência de campanha) |
| Rodapé | Institucional: contato, legal (aviso, privacidade, cookies, preferências), **espaço reservado** para logotipos oficiais de apoio (não são selos reais) |
| Carrinho da rolagem | Carro no traçado **ilustrativo** (PC ≥ 1300 px) + régua vermelha de progresso em qualquer tela; itens acendem ao passar pelo centro |
| Rastreio | `assets/track.js`: dataLayer, Consent Mode v2, faixa de cookies, eventos, UTM, API de Conversões. **Todos os IDs vazios.** Guia: `runbooks/rastreo.md` |
| Páginas legais | `aviso-legal.html`, `privacidad.html`, `cookies.html` com campos `[Pendiente: …]` (titular, NIF, domicílio) |

## Próximo passo (28/10, fim da noite) — lista viva do que falta
Detalhe, decisões e manifesto de fontes: `runbooks/passagem-2026-10-28-noite-site-2.md` (**ler a seção 1 inteira**). Proposta visual aprovada: `estudo/visual/board-visual.html`.

**Site (esta conversa):**
1. **Carro de rally nº 43 com câmera FPV: FEITO E AUDITADO, LOCAL (29/10, 00h30), não publicado, aguarda o Diogo olhar.** Imagem feita por IA (Higgsfield, conta do Diogo, 12 créditos) a partir das fotos 9882 e 9884; vista de cima, frente para baixo; o "Eh" do teto e o "OINOS" são o "43" e o "SONIC" **de cabeça para baixo** (a pintura real se lê de trás para frente; subindo, o carro vai de frente para cima e o 43 fica legível). Mora em **Cómo trabajamos** (os 4 passos do cliente viraram lista grande em Anton, que fica vermelha ao descer). Receitas: `estudo/carro-43/` e `scripts/preparar-carro.py`; testes `testar-carro.mjs`, `filmar-carro.mjs` (+ `folha-contato.py`), `medir-fluidez.mjs`. **Auditoria 29/10:** (a) ao subir, o carro descia ~400 px com a página e depois pulava para cima (parecia cair): os gatilhos ficavam fora da zona em que a pista está presa; agora entram/saem 80–120 px dentro dela; (b) sombra preta que virava ao girar e nem aparecia no fundo preto: trocada por brilho vermelho suave na camada que não gira; (c) imagem tratada como as fotos do site (cor, grão, exposição, vinheta), borda limpa e, depois que o Diogo disse que "parece igual": silhueta arredondada (sem farelos brancos), verde neon e laranja menos saturados (paleta preto/prata/vermelho) e **luz vermelha de contorno cozida na imagem** (margem de 22 px, 532×1059 e 300 px); (d) deslize ±12 % com suavização (lerp 0,1); (e) cinza dos títulos com contraste (3,9:1) e número pequeno aceso em branco, não vermelho; (f) foto decodificada antes de aparecer. Medido (local): Lighthouse celular 95–96 / 100 / 100 / 100, 722 KB; robô sem erro; 60 quadros/s no PC e nenhum quadro >33 ms em celular fraco simulado; sem rolagem lateral de 320 a 1920 px. **Do Nick Ho que ainda não usamos:** rolagem suave no site todo (Lenis, lerp 0,1, wheelMultiplier 0,7) — **voto do Diogo** (muda a sensação da página inteira). **Decisões abertas:** a pintura "de cabeça para baixo" (virar só os textos?); se o mini-traçado `#circuit` sai (hoje fica, só some enquanto o carro passa).
2. **Lista que fica vermelha: FEITA junto** (cada passo fica vermelho quando o topo passa do centro da tela e continua vermelho; volta ao subir).
3. Anton nos `h2` das seções (a lista de Cómo trabajamos já usa Anton).
4. **Votos do Diogo:** tópicos da galeria, efeito de cor no celular, foto da faixa grande, vídeos (B), "pode" das 6 ideias do texto.
5. Fotos reais por evento (hoje só Madrid tem foto; TV e Zaragoza sem). 6. Publicar o crédito "Por Agencia Bienquisto" do rodapé (só com "publica").
7. Do quadro visual ainda falta: foto no título de "La prueba" e "Cómo trabajamos" (esta pede foto de montagem ao cliente); vídeos de Cheste; selos de apoio (só com arquivo oficial do cliente).

**Material do cliente ainda não visto:** mais de 50 vídeos de julho ("Open Rcarcade"), 3 das 15 fotos de julho, 7 vídeos "Avatar", áudio do vídeo de Cheste (`cliente/ACERVO.md`).

**Proposta ao cliente (outra conversa):** `cliente/propuesta/propuesta-mejora-rcarcade.html` (fora do git; `python -I cliente/propuesta/build.py` gera de novo); passagem `runbooks/passagem-2026-10-28-noite-proposta.md`. **Não trazer para o site.**

**Mandar ao cliente** as perguntas da seção 5 de `estudo/estrategia-2026-10/06-sintese.md` e pedir os identificadores de rastreio, titular/NIF/domicílio, logotipos de apoio (se houver), telefone e e-mail comerciais, fotos de montagem e fotos por evento.

**Já feito e conferido (não refazer):** revisor cego do site (5/10, correções aplicadas: cookies, vídeo com pausa, contraste, promessas suavizadas); texto antigo × V3 às cegas (V3 7/10 × antigo 4/10, V3 é a base); passagem 2 testada às cegas (7/10, lacunas corrigidas).

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
unidade aberta ao público; clipe de vídeo dedicado para o topo; fotos de montagem (para "Cómo trabajamos"). **Não há artigos nem imprensa no material do cliente** (ver o El Hormiguero no estudo 02, a confirmar) — "Media y Artículos" não
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
| **Proposta visual aprovada (28/10), com o que falta** | `estudo/visual/board-visual.html` e `PLANO-DE-MELHORIA.md` |
| Estudos de estratégia (27/10) | `estudo/estrategia-2026-10/` |
| Capturar telas em vários tamanhos | `runbooks/capturar-telas.md` |
