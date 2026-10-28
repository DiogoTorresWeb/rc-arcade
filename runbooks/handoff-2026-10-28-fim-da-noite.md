# Handoff — RC Arcade (site), fim da noite de 28/10/2026

> Curto de propósito. **Não repete** o que já está escrito: o inventário, as decisões e a lista do que falta moram em
> `runbooks/passagem-2026-10-28-noite-site-2.md` (testada às cegas, 7/10 duas vezes, lacunas corrigidas) e em `CURRENT_STATUS.md`.
> Se este texto contradiz o `CURRENT_STATUS.md`, vale o `CURRENT_STATUS.md`.

## Para começar
Abrir conversa nova na pasta `C:\Users\Diogo Torres\diogo-base\Projetos\rc-arcade` e dizer **"continuar o site do RC Arcade"**.
Antes de agir: ler a **seção 0 e a seção 1 inteira** da passagem 2 (as 6 perguntas de abertura e o manifesto de fontes) e responder
"o que existe no projeto que esta passagem não cita?". Quem não fizer isso repete o erro que gerou esta passagem
(`Recursos/aprendizados/passagem-perde-fontes-do-projeto.html`, na base).

## Onde estamos (uma olhada)
- **No ar** (`main` = `544bca2`): cortina curta, 4 passos com título na foto, revelação ao descer, faixa "Una pista. Hasta seis pilotos.",
  galeria por temas (aba "Con público"), capas de imprensa (só Madrid com foto), fotos em "Dos formas". https://diogotorresweb.github.io/rc-arcade/
- **Só no computador, sem commit:** crédito "· Por Agencia Bienquisto" no rodapé; atualizações de `CURRENT_STATUS.md`, `HISTORICO.md`, `TASKS.md`,
  `cliente/ACERVO.md`; as duas passagens; este handoff. **Publicar só com "publica"**: `git push origin hero-teste:main`.
  "Manda o site" = mandar o **link**.

## Foco da próxima sessão: o carro (decidido pelo Diogo)
**Carro de rally nº 43 com câmera FPV**, visto de cima, com a coreografia do Nick Ho: desce e some; volta ao contrário ao subir; dá ré se o
visitante parar e voltar. **Se não ficar bem feito, o carro sai** e fica só a lista vermelha (aprovada, ainda não feita).
Passos sugeridos (cada um mostrado ao Diogo antes do próximo):
1. Olhar as fotos candidatas (`DSC09882`, `DSC09884`, `DSC09901`, `DSC09861` em `cliente/acervo-dropbox/extraido/insta/`). Avisos: a 9882 é ângulo
   inclinado, não de cima de verdade; há **duas unidades iguais** com câmera (nº 43 e nº 23): escolher a do 43.
2. Conseguir a vista de cima: recortar o carro e **refazer a vista de cima com IA** (imagem para imagem, fiel: branco/preto/verde, câmera no teto).
   Há ferramentas de imagem conectadas (Higgsfield, ver `mcp__a5524996…`); **perguntar antes de gastar créditos**. Mostrar 2–3 opções ao Diogo.
3. PNG/AVIF transparente, ~320×573 no PC e ~183×327 no celular, leve (orçamento do site: ~700 KB ao abrir).
4. Animar como o Nick Ho (mecanismo em `REFERENCIAS.md` da raiz e `estudo/refino-v4/nickho/MEDICAO.md`): carro preso **só à seção**
   (sticky dentro da seção, nunca fixo na página), marcador `start` no centro faz entrar em ~0,8 s, `end` faz sair em ~0,8 s e só então gira 180°.
5. Medir (robô + Lighthouse 3 vezes) e testar no celular. Meta 90+ no celular, 100 nos outros três.
**Pergunta ainda aberta ao Diogo (só se o carro for removido):** o mini-traçado ilustrativo `#circuit` (PC ≥ 1300 px) sai junto?

## Depois do carro (ordem em `CURRENT_STATUS.md` → "Próximo passo")
Lista que fica vermelha → Anton nos `h2` → votos do Diogo (tópicos da galeria, cor no celular, foto da faixa grande, vídeos B, "pode" das 6 ideias do texto)
→ fotos reais por evento → publicar o crédito.

## Como o Diogo quer trabalhar (já combinado)
- **Rápido e assertivo**; só pergunta quando falta decisão dele, com explicação clara. Pode usar interview-me/grill-me (docs) se achar melhor.
- Ele **não é programador**: fechar respostas com um parágrafo **Pronto.** em português simples (o que mudou para ele e o que ele precisa fazer).
- **Sempre passar `model`** ao criar agente: forte para estratégia e revisor cego; menor para medir, converter e listar.
- **Mudança visual** vai para ele ver (print ou laboratório) antes de aplicar; ele vota por captura de tela ("aprovado", "não gostei").
- **Honestidade:** dado sem origem não vira legenda, rótulo nem texto. Foto de evento só em cartão do evento confirmado.
- Protótipo: imagem (rosto, Red Bull, logos) não é bloqueio; texto que afirma o que não se sabe é.

## Armadilhas já pagas (não estão nos outros documentos)
- **Heredoc com Python no shell quebra** com aspas e barras invertidas: gravar o script com a ferramenta de escrever e rodar o arquivo.
- **Foto em aba oculta** (`hidden`/`display:none`) com `loading="lazy"` não carrega: é o que faz a galeria pesar zero até abrir a aba.
- `aria-label` em `<p>` derruba a acessibilidade (97): texto para leitor de tela vai em `.sr-only`.
- Quadros do vídeo de Cheste: pasta temporária some entre sessões; refazer com o comando da passagem 2 §6. **Não** usar `cont-video/frames/`.
- Chrome para medir: `C:\Program Files\Google\Chrome\Application\chrome.exe`; Lighthouse e `puppeteer-core` vêm do cache do `npx`; `ffmpeg` está instalado (winget).
- Dropbox: o link com chave mora em `cliente/acervo-dropbox/LINKS.local.md` (fora do git); **nunca** copiar a chave para arquivo versionado.
- O conector GitHub do Claude dá erro por falta da variável `GITHUB_PAT` (o Diogo precisa criar a chave); **não atrapalha** o `git push`.

## Skills sugeridas para a próxima sessão (via ferramenta Skill)
- `superpowers:brainstorming` e `impeccable` (ou `design-taste-frontend`): antes de desenhar o carro e a imagem de cima.
- `animate` e `emil-design-eng` (ou `apple-design`): para a coreografia, a curva, a duração e a interrupção do movimento, e o `prefers-reduced-motion`.
- `humanizer`: qualquer texto novo em espanhol.
- Agente `revisor-cego` (com `model` forte): antes de publicar de novo ("o dono do centro de lazer pediria uma proposta?").
- `handoff` de novo ao fim; antes, conferir o manifesto da passagem contra a pasta (a lição desta noite).
- `anthropic-skills:grill-me` só se o Diogo quiser ser entrevistado sobre decisão difícil.
