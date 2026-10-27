# RC Arcade — tarefas

## Agora (Etapa 1 — entender antes de desenhar)

Material do cliente recebido e lido em 13/09/2026 — ver
`cliente/MATERIAL-RECEBIDO.md`. O que ele respondeu já está em
`CURRENT_STATUS.md`. O que falta:

- [ ] **DECISÃO QUE TRAVA O RESTO:** qual das 3 vias o site prioriza —
      instalação fixa (vender a atração pro operador), evento temporal
      (contratar pra feira/ativação) ou formato competição (liga/ranking)?
      O dossiê trata as três como iguais; o site não pode.
- [ ] **Definir o interlocutor:** o site fala com o operador que compra a
      atração (B2B, que é o tom do dossiê) ou com o público final que vai
      pilotar (B2C, que é o que as fotos de Instagram e a "jornada de puertas
      abiertas" sugerem)? Se forem os dois, precisam de caminhos separados.
- [x] Levantar 2-3 concorrentes/referências do nicho (FPV, RC, simuladores,
      atrações de centro de lazer) — feito em 23/09/2026, ver `CONCORRENTES.md`.
      Racetech Systems (concorrente direto, sem prova em vídeo — oportunidade),
      AXSIM (referência de como separar B2B/B2C na mesma página), F1 Arcade
      (só tom, não estrutura).
- [ ] Confirmar dados operacionais: onde fica, unidade aberta ao público?,
      contato comercial que vai no site
- [x] Instalar os 3 plugins (Superpowers, Ponytail, Caveman) no Claude Code
      — feito em 13/09/2026, scope user (vale pra todo projeto)
- [x] Baixar a pasta `logos rcarcade` do Dropbox — feito em 23/09/2026, 7 dos
      8 arquivos (faltou só `marca video.png`, sem link direto capturado) em
      `cliente/logos/`. Logo principal confirma a paleta já travada
      (preto/vermelho/prata) e mostra o conceito real: simulador com volante +
      tela mostrando o buggy numa pista externa de terra + HUD de telemetria —
      bate com a seção de linguagem HUD do `DESIGN-DIRECTION.md`.
- [x] Analisar vídeo real do cliente (WhatsApp, 42.5s) pra técnica canvas
      image sequence — feito em 23/09/2026, ver `DESIGN-DIRECTION.md` seção
      "Vídeo real analisado". Dúvida de marca "DriftStation vs RC Arcade"
      resolvida pelo Diogo: é só o nome do espaço físico, sem implicação de
      marca/parceria.
- [ ] **Pedir ao cliente um clipe novo dedicado** pra hero em vídeo: câmera
      fixa (não de mão), 5-10s, resolução maior que WhatsApp, enviado por
      Dropbox/cabo. O vídeo atual só prova a técnica (ver protótipo em
      `cliente/fotos-pista/canvas-sequence-test.html`), não serve como
      entrega final — baixa resolução, câmera de mão, lançamento reto (não
      drift lateral).
- [x] **Formalizar o hero visual** — fechado em 23/09/2026:
      `hero-duotone-preto-prata.jpg` é a direção confirmada pra Etapa 3
      enquanto o clipe de vídeo dedicado não chega (ver `DESIGN-DIRECTION.md`
      seção "Direção do hero — confirmada").

## Depois (só depois da Etapa 1 fechada)
- [ ] Etapa 2 — auditoria: o material já chegou (dossiê, vídeo de 42s, 3
      pastas de Dropbox com fotos profissionais e logos). Falta escolher o
      que entra no site e confirmar autorização de uso de imagem das pessoas
      que aparecem nas fotos
- [ ] Etapa 3 — tokens de design (cor, tipografia, espaçamento).
      Fluxo completo (12 passos + prompt exato) já documentado em
      `professor/estudo/matheus-gomes-design-system/RESOURCES.md`. Acesso
      confirmado: Claude Pro cobre o claude.ai/design; download das
      referências do Behance é manual (sem ChatGPT Work); etapa final roda
      no Claude Code (sem precisar de Codex). Nada bloqueando — só falta
      escolher a referência do Behance certa pro público B2B do RC Arcade.
- [ ] (opcional, decisão do Diogo) comentar "TASTE" no post do
      @viniestrategista pra receber a DM com as 5 configurações — hoje é só
      promessa, sem conteúdo público verificável (ver
      `estudo/viniestrategista-design.md`). Não é bloqueante pro projeto.
- [x] **Refino com a skill `impeccable` + linguagem Porsche** — 24/09/2026.
      Tipografia decidida (Archivo + JetBrains Mono auto-hospedadas, registro
      Porsche: peso 400, frase capitalizada — ver `DESIGN-DIRECTION.md`), intro
      de racing 1x por sessão com o wordmark subindo pro centro do cabeçalho,
      logo oficial extraído na variação "solo nombre" com fundo removido, hero
      reenquadrado com o carro centralizado. Detector da skill roda com 2
      achados restantes, ambos justificados (ver seção abaixo).
- [ ] **Pendências do refino** (não bloqueiam, mas ficam registradas):
      - `21st.dev` continua incompatível (React/Tailwind/shadcn; o site é HTML
        puro) — confirmado ao vivo em 24/09. O código de referência veio do
        próprio `racing.porsche.com`, medido no browser. Se quiser usar
        21st.dev de verdade, a decisão é migrar o site pra React.
      - GSAP e Lenis seguem aprovados mas **não foram usados**: a intro e os
        contadores saíram em JS puro, o que garante a regra de "fail open" sem
        depender de CDN. Reavaliar se a Etapa 5 pedir sequências mais complexas.
      - Detector: `cramped-padding` é falso positivo (o padding real medido é
        97px contra borda de 0.67px); `all-caps-body` são os rótulos curtos de
        HUD, que o próprio brief exige.
- [x] Etapa 4 (primeira versão) — `index.html` criado em 24/09/2026 com os
      blocos 1-4 e 6 de `ESTRUTURA-DO-SITE.md` construídos por completo
      (Topo, Qué es, La prueba, Para el operador, Tres vías), tokens de
      marca aplicados, tipografia ainda provisória (Etapa 3 não rodou).
      Bloco 5 parcial (faltam medidas reais de espaço). Blocos 7 e 8
      deixados como placeholder — sem dado operacional do cliente, não
      preenchidos com suposição.
- [x] Plano V2 — P1.1 "Qué es", P1.3 "Para el operador" e item 6 "Contacto" implementados e
      commitados em 24/09/2026 (aprovação explícita do Diogo só de P1.1 e P1.3).
- [x] **Topo (27/10/2026, branch `hero-teste`, commit 17ef1d9):** palavra CARRERA atrás do carro
      recortado. Versão atual **finalizada** pelo Diogo ("funcionou bem"); refinos depois.
      **Falta registrar:** cabeçalho A ou B? e merge na `main`?
- [ ] **PRIMEIRO (pivô de 27/10): estratégia e acervo.** (a) Conferir o download de "Open Rcarcade" e extrair
      os 3 zips de `cliente/acervo-dropbox/`, registrar tudo em `cliente/ACERVO.md`; (b) ver os vídeos novos
      (`RC ARCADE CHESTE HD`, 7 "Avatar" de `estreno lona`) com o pipeline completo (quadros + áudio) e
      garimpar a vista de cima do carro em `360`, `action5` e nas 23 fotos; (c) ler os 4 estudos de
      `estudo/estrategia-2026-10/` (os 4 estão prontos), corrigir `CONCORRENTES.md` e fazer
      a síntese; (d) revisor cego sobre a síntese; (e) só então decidir o scroll e o V0.
- [ ] **Scroll do carro — modelo do nickho-motorsports.nl, V0. MEDIDO em 27/10; falta decidir.**
      O que a referência faz de verdade está em `REFERENCIAS.md` (entrada de 27/10): carro de
      cima, entra e sai por gatilho (0,8 s), desliza devagar preso à rolagem, itens acendem ao
      passar pelo centro; PC no meio da página, celular colado na borda direita; "ré" quando para
      no meio e volta. **Plano do V0 (sem código ainda):** variante `?scroll=car` da seção "Qué es"
      (a timeline aprovada fica como padrão); os 4 passos reais (Elige/Siéntate/Conduce/Compite)
      fazem o papel da lista; JS puro com `IntersectionObserver` + transição CSS com o `--ease`
      do site (sem biblioteca, falha aberto) + deriva de -12% a +12% pela rolagem; destaque dos
      passos em prata/branco com filete vermelho (vermelho em texto pequeno reprova no AA, 4,2:1);
      `prefers-reduced-motion` = carro parado. **Decisões do Diogo antes de codar:** (1) onde
      entra — "Qué es" como variante (recomendado), bloco novo ou "Tres vías"; (2) **qual imagem
      do carro**: falta uma vista de cima — pedir ao cliente (pasta Dropbox "Open Rcarcade/360" e as
      16 fotos do Instagram) ou, só para provar o movimento, usar o recorte 3/4 do #22 sem girar;
      (3) manter a "ré" como na referência ou virar 180° na hora.
- [ ] **Repositório de fotos e dados do cliente — o que existe de verdade (verificado 27/10).**
      No disco: 4 fotos DSLR 3/4 (`cliente/fotos-pista/DSC09861/62/64/65`), vídeo de 42 s e 25
      quadros (`sequence-launch`), logos (só marca: `lateral*.png` são o letreiro; `principal.png`
      é o conceito do simulador). Fora do projeto, na Área de Trabalho: `RC Arcade Design System/`
      (da etapa do Claude Design: componentes `StepList`, `ContactForm`, `StatCard`, `SpecTable`,
      `QuoteBlock` em React + `cockpit.jpeg`, foto real do circuito e dos cockpits). **Nenhuma
      imagem do carro vista de cima.** O resto está no Dropbox do cliente (Open Rcarcade com
      `360` e `action5`; RCA publicacion insta; Rcarcade Cont com Editados, estreno lona,
      Jornada de puertas abiertas): o Dropbox conectado ao Claude está **vazio** e os links das
      pastas **não estão registrados em nenhum documento**. Contagem inconsistente: o inventário
      diz 16 fotos em "RCA publicacion insta" e `DESIGN-DIRECTION.md` diz 23. **Pendente:** o
      Diogo passar os links (ou adicionar as pastas ao Dropbox dele) para garimpar uma foto de
      cima do carro (360/action5 são os candidatos) e para registrar os links aqui.
- [ ] **Modelos de "Contacto" e de "Media y Artículos" do mesmo site (só plano).** Regra de
      honestidade: o material do cliente **não tem** artigos nem imprensa; sem conteúdo real a
      seção não entra com texto inventado (estrutura vazia marcada como pendência). "Contacto"
      depende do contato comercial que o cliente ainda não mandou.
- [ ] Plano V2 do item 4 em diante (assets de "Tres vías" e "Escalas", etc.) — retoma depois do
      teste do topo, uma unidade por vez.
- [ ] Etapa 6 — validar canal de captação (Google Ads/WhatsApp é do Paulo;
      B2B provavelmente é outro caminho — talvez LinkedIn ou contato direto
      com operadores)
