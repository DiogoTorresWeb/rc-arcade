# RC Arcade — histórico

> Tipo: **histórico** — só se acrescenta. Entrada datada no fim, nunca reescrita.
> Responde "como chegamos aqui". Onde estamos: `CURRENT_STATUS.md`. Por que é assim: `DECISIONS.md`.
> Regra: `../../SISTEMA.md`.

## 13/09/2026 — Etapa 1: material do cliente lido

Dossiê comercial (20 páginas, espanhol), vídeo real de 42 s e 3 pastas de Dropbox chegaram e
foram inventariados em `cliente/MATERIAL-RECEBIDO.md`. Direção de design e estrutura da página
escritas (`DESIGN-DIRECTION.md`, `ESTRUTURA-DO-SITE.md`). Documento de alinhamento ao cliente
em espanhol. Nenhuma linha de site escrita ainda, de propósito.

Retrato do que o cliente respondeu e do que faltava, **movido de `CURRENT_STATUS.md` em
27/10/2026** (texto original, só a primeira linha ajustada):

---

O material abaixo é do levantamento de **13/09**, quando nenhuma linha de site existia ainda.
Retrato do que o cliente entregou e do que foi decidido na Etapa 1.

**Cliente:** RC ARCADE — pilotagem de carro RC real com câmera FPV, vista em
primeira pessoa, num circuito físico. Espanha, material todo em espanhol.
Contatos identificados no Dropbox: **ximodj navarro** e **David Navarro
Rodriguez**.

**Onde estamos:** fim da Etapa 1 / começo da Etapa 2 do método
(`diogo-base/Areas/agencia/metodo.md`). O material do cliente foi lido e
inventariado em `cliente/MATERIAL-RECEBIDO.md`. Nenhuma linha de site escrita
ainda, de propósito.

**Combinado com o cliente:** começar pelo site; pacote digital completo pode
fechar depois.

## Etapa 1 — o que o material já respondeu

- **O que é o produto:** carro RC real + FPV + cockpit (volante, pedais, tela).
  Até 6 simuladores simultâneos num circuito compartilhado, com tempo de volta
  e posição medidos. Mecânica em 4 passos: elige → siéntate → conduce → compite.
- **Como o cliente se posiciona (palavras dele):** *"No miras la carrera.
  Estás dentro de ella."* — a frase-âncora do dossiê. Visão de marca:
  *"Convertir cada circuito en un lugar donde cualquiera pueda sentirse piloto."*
- **O argumento B2B pro operador:** diferenciação (difícil de confundir com
  outra atração), escalabilidade (adapta ao espaço), rotação (sessões e
  competições programáveis), conteúdo (gera conversa e material visual).
- **Os 4 públicos finais:** famílias, jovens, aficionados de RC, empresas/eventos.
- **Identidade visual:** já existe e está definida — vermelho (energia e
  competição), preto (tecnologia e profundidade), prata (precisão e caráter
  mecânico), com sistema de logo completo em 9 variações.
- **Prova de que funciona:** vídeo real de 42s de uma sessão rodando, com
  telemetria na tela (voltagem, 25Mbps, latência). Não é conceito, já opera.

## Etapa 1 — o que ainda falta (não preencher com suposição)

1. **Qual das 3 vias o site prioriza.** O dossiê apresenta três modelos de
   negócio como iguais — instalação fixa, evento temporal e formato competição.
   Cada um fala com um comprador diferente. **Um site não consegue priorizar
   os três.** Essa é a decisão que trava o resto.
2. **O site fala com o operador (B2B) ou com o público final (B2C)?** O dossiê
   é B2B puro. Mas as fotos de Instagram e a pasta "Jornada de puertas
   abiertas" indicam operação já aberta ao público. Pode ser que precise dos
   dois, com caminhos separados — mas isso precisa ser decisão, não acidente.
3. **Concorrentes** — nada no material, ninguém levantou ainda.
4. **Dados operacionais:** onde fica, se já tem unidade aberta, contato
   comercial que vai no site.

**Regra de honestidade (herdada do método):** nada marcado como "falta" pode
ser preenchido com suposição. Campo vazio, nunca chute.

## Impacto na Etapa 3 (design)

A marca **já existe**. Isso muda como a técnica do @matheusgomes vai ser usada:
o Claude Design não vai inventar a identidade — vai construir o sistema de
design **web** (tokens, componentes, escala tipográfica, estados) fiel ao que
já está definido. A referência do Behance entra como padrão de layout, não
como fonte da identidade. Detalhe em `cliente/MATERIAL-RECEBIDO.md`.

---

(Em 27/10 já não valem estas duas linhas do retrato: "Concorrentes — nada no material" — foram
levantados em 23/09, ver `CONCORRENTES.md`; e "nenhuma linha de site escrita" — o site existe.)

## 23/09/2026 — Material real tratado, concorrentes, hero

Fotos e logos reais do Dropbox trazidos para o projeto. Vídeo de 42 s analisado e técnica de
sequência de imagens validada com o material real. Dúvida "DriftStation vs RC Arcade" resolvida
pelo Diogo: é só o nome do espaço físico. Três concorrentes/referências levantados
(`CONCORRENTES.md`). Hero duotone preto e prata formalizado como direção.

## 24/09/2026 — Primeira versão do site, refino Porsche, Direção de Arte V2

- `index.html` criado (blocos 1-4 e 6; 5 parcial; 7 e 8 como pendência honesta).
- Refino no registro Porsche medido ao vivo: Archivo + JetBrains Mono auto-hospedadas, intro de
  racing 1x por sessão, logo "solo nombre" no centro, hero reenquadrado com o carro #22.
- Crítica "Direção de Arte V2" (o site era um componente reestilizado 6 vezes), plano
  `PLANO-IMPLEMENTACAO-V2.md` e Design Gate (GO com ajustes).
- Implementados: P1.1 "Qué es" (timeline), P1.3 "Para el operador" (manifesto), item 6
  "Contacto" (fechamento silencioso). Publicado no GitHub Pages.

## 30/09/2026 e 18/10/2026

30/09: status corrigido (dizia "nenhuma linha de site escrita"). 18/10: referência visual do Nick
Ho Motorsports guardada em `REFERENCIAS.md`, parada até a V2 voltar.

## 27/10/2026 — Retomada e teste do topo (branch `hero-teste`)

- Retomada a partir de `AGORA.md` + git. Auditoria de contexto: os arquivos de estado do projeto
  estavam defasados (nada de P1.1, P1.3 e "Contacto"); este passe os reescreveu e criou este
  histórico.
- Opus leu o site: esqueleto e divisão de tarefas por modelo. Achados confirmados no código:
  "8 ms" e "Vuelta 4/6 — P1" em "La prueba" sem fonte no inventário do cliente; notas internas
  (`TASKS.md`, `ESTRUTURA-DO-SITE.md`) visíveis no site publicado; menu sem link para "Tres vías".
- Teste do topo pedido pelo Diogo (referência: pôster "SEPTEMBER" e Behance "Autrix"):
  palavra gigante CARRERA atrás do carro. Pesquisa técnica (Opus) não achou biblioteca pronta que
  mantenha o texto em HTML; a técnica reaproveitada é a de empilhar camadas do mesmo quadro
  (nickho-motorsports.nl, razorpay.com/m/bold). Pesquisa de texto (Opus) deu 8 palavras e 4
  conjuntos de frases; o Diogo escolheu CARRERA e o conjunto "operador".
- Recorte do carro #22: `rembg` + modelo BiRefNet (MIT). Pegou também o caminhão desfocado do
  fundo; removido por polígono ao longo da borda do carro. A cor do recorte vem do próprio hero
  tratado (alinhado ao pixel). Recorte móvel: o quadro 2400×3200 de `hero-mobile.jpg` foi
  localizado por correspondência de imagem (97%) porque o script que o gerou não foi guardado.
- Defeito antigo achado e corrigido no caminho: o cronômetro "Mejor vuelta" ficava escondido sob
  a foto no celular (`.readout` sem posicionamento).
- Validação: Chrome controlado por DevTools Protocol em 1440, 1024, 768 e 390 px (o painel do
  app corta a captura; ver `runbooks/capturar-telas.md`). `impeccable detect`: zero achados novos
  em relação à `main`.

## 27/10/2026 (fim do dia) — Avaliação do topo e passagem

- O Diogo avaliou o topo: "funcionou bem"; versão atual finalizada, refinos depois. Escolha entre
  cabeçalho A e B não registrada.
- `localhost` não abria no celular dele; foi dado o endereço da rede local (192.168.1.6:8791). Não
  se confirmou que abriu (firewall do Windows em "Público").
- Pedido novo, só plano: copiar do `nickho-motorsports.nl` o scroll em que o carro desce (PC pelo
  meio, celular pelo canto, volta de ré se rolar para cima), mais os modelos de "Contacto" e de
  "Media y Artículos". Na mensagem o nome saiu "nickromotorsports.nl"; vale o link que ele mandou,
  `nickho-motorsports.nl`, que já está em `REFERENCIAS.md`.
- Princípio registrado: qualidade da entrega decide a ferramenta (ver `DECISIONS.md`).
- Passagem: estado, tarefas, decisões e histórico atualizados antes de limpar a conversa.
