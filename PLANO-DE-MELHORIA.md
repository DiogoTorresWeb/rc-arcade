# Plano de melhoria do RC Arcade — a árvore

> Tipo: **estado** (reescreve-se a cada etapa fechada; o que já foi feito vai para `HISTORICO.md`).
> Criado em 28/10/2026, consolidando os estudos 01 a 05 (`estudo/estrategia-2026-10/`) e a auditoria do Google
> Meu Negócio e do Instagram feita no mesmo dia. Marcas: **[nós]** fazemos · **[cliente]** só ele resolve ·
> **[Diogo]** decide. "Confirmado" = visto com os próprios olhos hoje; "Inferência" = suposição minha.

## Objetivo
Um operador de centro de lazer chega, entende em 20 segundos, vê prova real e pede uma demonstração (formulário ou
WhatsApp). Tudo abaixo serve a isso. A página de abertura (hero) **está aprovada**; só recebe ajuste pequeno se a
estratégia pedir.

## A árvore

```
RC ARCADE: de "apresentação bonita" a "máquina de pedir demonstração"
│
├── 1. BASE (o que o cliente já tem e está quebrado)
│   ├── 1.1 Site deles (rcarcade.es / .com) — nota 5/10, ver estudo 05
│   │   ├── Duas cópias que divergem (.es de 17/09, .com de 01 e 09/10), 4 endereços sem redirecionar
│   │   ├── Sem descrição, sem imagem de compartilhamento, sem ícone, sem robots/sitemap, sem dados estruturados
│   │   ├── Sem formulário, sem botão de WhatsApp, sem vídeo (só e-mail e dois telefones no fim)
│   │   └── Logo e foto de abertura passaram pelo ChatGPT (assinatura da OpenAI no arquivo)
│   ├── 1.2 Google Meu Negócio — existe, mas quase vazio (ver seção "Auditoria")
│   └── 1.3 Instagram @rcarcade — vivo, 422 seguidores, mas sem rumo visual (ver seção "Auditoria")
│
├── 2. SITE NOVO (nosso)  — etapa por etapa, uma por vez, em branch
│   ├── 2.1 Fundação: SEO, contato, arquivos        ← FEITO em 28/10 (branch hero-teste, falta só o aviso legal)
│   │   ├── título/descrição/imagem de compartilhamento/ícone/endereço canônico
│   │   ├── botão de WhatsApp fixo + formulário que monta a mensagem e abre o WhatsApp/correo do cliente (nada vai para servidor)
│   │   ├── LSSI/RGPD (aviso legal, privacidade, caixa de aceite): texto-base, **advogado confere**
│   │   └── tirar do ar as notas internas ("Lo que todavía falta…", "Borrador")
│   ├── 2.2 Provas sociais (provisórias, trocadas depois pelas do cliente final) ← FEITO em 28/10
│   │   ├── El Hormiguero (CONFIRMADO, ver abaixo) como prova principal
│   │   ├── "Registro de pista": Volrace Motorshow Zaragoza (24–26/10/2026), jornada de puertas abiertas (2–3/07, Madrid), sorteo
│   │   └── comentários públicos do Instagram, só como placeholder marcado (regras na seção "Provas sociais")
│   ├── 2.3 Resto da página (hero fica): Qué es → La prueba (vídeo real) → Para el operador → ¿Cabe en tu espacio? → Cómo trabajamos → Registro de pista → Contacto
│   ├── 2.4 O carro que anda com a rolagem (só com foto real de cima; senão traçado da pista) — decisão pendente
│   └── 2.5 Publicação: no endereço do cliente (rcarcade.es), com redirecionamento dos outros 3
│
├── 3. GOOGLE MEU NEGÓCIO (é do cliente; precisamos de acesso de gerente)
│   └── corrigir categoria, endereço/área de atuação, site, horário, descrição, fotos, perguntas e primeiras avaliações
│
├── 4. INSTAGRAM (visual e estratégia)
│   └── grade coerente, destaques úteis, link na bio para a página de demonstração, destaque "El Hormiguero"
│
├── 5. ARQUIVOS E ACERVO
│   ├── terminar o download da pasta Open Rcarcade (30 GB de ?), ver os vídeos novos com o pipeline completo
│   ├── procurar vista de cima do carro nas 23 fotos, em 360/ e action5/
│   └── tudo que chegar vai para cliente/ACERVO.md no mesmo dia
│
└── 6. PERGUNTAS AO CLIENTE (cada uma trava algo acima)
    └── lista na seção final
```

## Auditoria (28/10/2026)

### Google Meu Negócio — CONFIRMADO, olhado hoje no Google Maps
O perfil existe com o nome **RCARCADE**, e está longe de pronto:

| Item | Hoje | O que falta |
|---|---|---|
| Categoria | **"Engenheiro"** | errada: nenhum operador procura engenheiro. Precisa de uma categoria de entretenimento/experiência (ver qual o Google oferece em espanhol e testar) |
| Site | **vazio** (o Maps oferece "Adicionar website") | colocar o endereço do site novo |
| Horário | vazio | horário de atendimento ou "mediante cita" |
| Endereço | nenhum visível; o ponto no mapa cai **no mar, perto do Estreito de Gibraltar** | negócio de área de atuação: definir região atendida (Espanha) e corrigir o ponto |
| Avaliações | **zero** | primeiras avaliações de clientes reais, pedidas por eles (nunca inventadas) |
| Fotos | **uma só**, o logo (do proprietário) | fotos reais de pista, cabines, equipe, eventos |
| Descrição, perguntas e respostas, publicações | não aparecem | descrição de 750 caracteres, 3 a 5 perguntas frequentes, publicações de evento |
| Telefone | tem (é o mesmo do site) | confirmar que é o comercial |

*Inferência:* a categoria errada e a falta de site tiram o perfil de qualquer busca de operador. Corrigir isto é rápido e de graça.

### Instagram @rcarcade — CONFIRMADO, olhado hoje
- 11 publicações, **422 seguidores** (o estudo 02 dizia 116: estava desatualizado), segue 81. Bio: "Experiencias al volante de todos los tamaños." Link: `rcarcade.com` e mais um (não aberto). Destaques: "Eventos" e "STARTS".
- Conteúdo: sorteio de uma corrida grátis de 6 minutos, aviso do **Volrace Motorshow Zaragoza (24–26/10, Feria de Zaragoza)**, "Duelo de coches teledirigidos", "Presentación oficial: ¿Te imaginas competir desde dentro del coche?" e a **Jornada de puertas abiertas** (qui 2 e sex 3 de julho, Madrid), vídeos de cabine e pista. Uma publicação traz o selo "AI content" do Instagram.
- Visual: mistura cartazes bem acabados (preto, vermelho, neon) com vídeos crus sem capa. Falta uma grade coerente, e a bio fala ao consumidor ("experiencias") e não ao operador.
- **El Hormiguero (CONFIRMADO):** o vídeo de 07/10/2026 está publicado como colaboração entre `@elhormiguero` e `@rcarcade`, com 6,2 mil curtidas, e o perfil do programa escreve: "¡Gracias a @rcarcade por traernos esta experiencia!". Isso fecha a dúvida do estudo 02 e é **a melhor prova social que existe hoje**.
- O número de WhatsApp aparece no cartaz da apresentação oficial: já existe um contato público por WhatsApp (não copiado aqui; confirmar que é o comercial).

## Provas sociais: o que dá para usar já
1. **Principal:** El Hormiguero (colaboração oficial, 6,2 mil curtidas), com o link do vídeo. Pedir ao cliente autorização para embutir/citar.
2. **Registro de pista:** eventos datados que o próprio Instagram do cliente prova (Volrace Zaragoza, puertas abiertas em Madrid).
3. **Comentários do Instagram — provisórios.** Os do vídeo do El Hormiguero são aplauso do público de TV ("Me ha encantado, ha sido chulísimo", "una auténtica pasada", "¡Brutal! ¡Quiero!") e **pedidos de acesso** ("¿Dónde se puede hacer esto?", "pago si hace falta"). Regras: 1) marcar como provisório no código; 2) citar o texto com a origem "Comentario público en Instagram, oct. 2026", **sem o nome de usuário** até haver autorização; 3) tirar quando houver depoimento real de cliente final. Atenção: é público de consumidor, **não comprador B2B**: serve de calor, não de prova de retorno.
4. O que um operador quer de verdade (estudo 03): número de operação, retorno por m², histórico de quebras. Isso só vem do cliente.

## Ordem de execução (uma etapa por vez, cada uma fecha com commit e doc atualizado)
1. **Etapa 2.1 Fundação** (SEO, WhatsApp, formulário, jurídico-base, limpeza). Tudo [nós], com uma decisão [Diogo]: onde o formulário envia (ver abaixo).
2. **Etapa 2.2 Provas** (El Hormiguero, registro de pista, comentários provisórios).
3. **Etapa 2.3 Resto da página**, seção por seção, hero intocado.
4. **Google Meu Negócio e Instagram** em paralelo, quando o cliente der acesso: preparo as mudanças por escrito, ele (ou o Diogo, com acesso de gerente) aplica.
5. **Acervo/Open Rcarcade** continua em segundo plano; resolve a decisão do carro (2.4).
6. **Publicação** só depois da revisão cega e da confirmação do cliente sobre domínio.

## Decisões abertas [Diogo]
- **Formulário (resolvido em 28/10):** feito sem servidor: o visitante preenche, o site monta a mensagem e abre o WhatsApp (ou o correio) do cliente. Se um dia quiserem receber num painel, liga-se um serviço de recebimento. Falta o cliente confirmar que o telefone e o e-mail são os comerciais.
- Cabeçalho A ou B; se `hero-teste` entra na `main` (a versão de hoje está guardada na marca `antes-v2-2026-10-27`).
- Créditos do Fable para a síntese final.

## Perguntas ao cliente [cliente]
1. Quem fez o site, desde quando existe, por que há duas versões, quem controla o domínio `rcarcade.es`?
2. O telefone/WhatsApp e o e-mail da página são os comerciais? Prefere formulário ou WhatsApp?
3. Dá acesso de gerente ao perfil do Google e ao Instagram? Qual categoria prefere?
4. Existe logo original em vetor? (o atual é feito por IA, com letras ilegíveis no painel)
5. Endereço ou região atendida; onde fica a base e se há demonstração aberta ao público.
6. m², altura, energia, internet, pessoas na operação, duração da sessão, preço/modelo de negócio.
7. Autorização de imagem das pessoas nas fotos e vídeos; autorização para usar o vídeo do El Hormiguero.
8. Onde estão as pastas `Editados` e `Jornada de puertas abiertas` do Dropbox (a segunda parece ser a jornada de Madrid).
