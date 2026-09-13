# Etapa 3 — inputs prontos pro fluxo do Claude Design

Preparado em 13/09/2026. Passo a passo completo da técnica está em
`professor/estudo/matheus-gomes-design-system/RESOURCES.md`.
Aqui é só o que colar em cada campo, já pensado pro RC Arcade.

## Antes de abrir o Claude Design

**Baixar o logo.** Pasta `logos rcarcade` no Dropbox (`Rcarcade Cont`).
Preferir `.svg`; se só tiver PNG, serve. Guardar em `cliente/assets/`.

**Escolher a referência no Behance.** Buscar por um destes termos:
```
racing dashboard dark ui
telemetry dashboard design
motorsport web design
```
Critério de escolha (o passo mais importante de todos):
- Projeto **completo** — que mostre tipografia, grid, ícones e estados, não
  só três telas bonitas. Referência crua faz o Claude Design inventar o resto.
- Que tenha **vocabulário de dados**: números grandes, tabelas, indicadores.
  Não adianta ser só fundo preto com gradiente.
- Descartar estética "gaming" genérica, neon e degradê decorativo.

**Baixar as imagens do projeto escolhido.** O Matheus usa o ChatGPT no modo
Work pra isso, mas você só tem o Free — então é manual: botão direito em cada
imagem do projeto → salvar. São umas 6-10, leva 2 minutos.

## Campo: Company name and blurb

```
RC ARCADE — sistema de diseño web
```

## Campo: Any other notes?

```
Sistema de diseño para la web de RC ARCADE: una experiencia de conducción con
coches de radiocontrol reales, cámara FPV en primera persona y cockpit con
volante y pedales, sobre un circuito físico. Hasta seis simuladores
simultáneos, con tiempos de vuelta medidos.

La web habla principalmente a operadores de centros de ocio que compran la
atracción (B2B), y en segundo lugar al público que viene a pilotar. Tono:
preciso, técnico y competitivo. Nunca infantil ni de parque de atracciones.

Identidad ya definida, respetarla exactamente:
- Rojo #E31B23 — energía y competición. Solo como acento y señal (elemento
  activo, mejor vuelta, llamada a la acción). Nunca como fondo de áreas
  grandes.
- Negro #0A0B0D — fondo profundo.
- Superficie #191A1E — tarjetas y secciones.
- Plata #B1B0AB — texto secundario, reglas finas, detalle mecánico.
Tema oscuro como principal.

Referencia conceptual clave: la interfaz debe parecer la pantalla del cockpit
del piloto, no una plantilla oscura genérica de tecnología. El producto ya
muestra telemetría en pantalla (voltaje, Mbps, latencia, barras de señal) y
cronómetro con vueltas, posición y diferencia de tiempo (00:42.381, +0.814).
Ese es el vocabulario gráfico que quiero: números grandes en monoespaciada,
cronómetros y deltas como elemento de diseño, reglas finas, esquinas
marcadas, indicadores de estado.

Evitar: degradados decorativos, brillos neón, estética gaming genérica,
iconos genéricos de tecnología.

Componentes que necesito: cabecera de sección, tarjeta de dato/estadística
grande, bloque de pasos numerados, tabla comparativa, tarjeta de escala o
plan, bloque de cita, formulario de contacto, botones (primario, secundario y
fantasma), y elementos tipo HUD (cronómetro, delta de tiempo, indicador de
señal).

Mobile completo y real, sin perder densidad de información en escritorio: el
operador consulta capacidad y medidas desde ordenador.
```

## Campos que ficam vazios
- `Link code from GitHub` — vazio (não há código ainda)
- `Link code from your computer` — vazio
- `Upload a .fig file` — vazio

## Campo: Add fonts, logos and assets
O logo do RC Arcade + todas as imagens baixadas do projeto do Behance.

## Quando ele fizer as perguntas (durante a geração)

Regra simples:
- Pergunta sobre **cor de marca** → responder com os valores acima. Nunca
  deixar ele decidir isso, já está definido pelo cliente.
- Pergunta sobre **público/tom** → operador B2B primeiro, público depois;
  tom preciso e competitivo.
- Pergunta puramente **estética** que a gente não decidiu (curvatura de canto,
  densidade de sombra, etc.) → "decida por mim", sem culpa.

## Depois de gerar
1. Share → Export HTML → **Project archive** (não "Standalone HTML")
2. Apagar o HTML solto que vem junto
3. Renomear a pasta pra `design-system-export`
4. Colar no ROOT do projeto
5. Rodar o prompt de triagem —
   `professor/estudo/matheus-gomes-design-system/prompt-triagem-design-system.md`
   — dentro do Claude Code, nesta pasta

## Sobre imagem gerada por IA
**Não usar neste projeto.** O argumento central do RC Arcade é "isto ya
funciona, aquí está la sesión real". Imagem gerada por IA contradiz
exatamente isso, e operador que desconfia de uma foto desconfia do resto.
O material real do cliente (vídeo FPV + fotos profissionais) é mais forte que
qualquer render. Único uso defensável, se algum dia fizer falta: textura de
fundo abstrata sem nada reconhecível — e nem isso é necessário hoje.
