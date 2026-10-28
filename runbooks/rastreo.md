# Rastreio do site — como ligar cada ferramenta

> Tipo: **runbook** — 28/10/2026. Código: `assets/track.js` e o bloco `window.RCA_TRACK` no fim do `index.html`.

O site já nasce com uma camada única de rastreio. **Hoje todos os identificadores estão vazios**, então nenhuma
ferramenta externa carrega. Para ligar uma, o cliente passa o código e a gente preenche **uma linha** no `index.html`:

```js
window.RCA_TRACK = { gtm: '', ga4: '', meta: '', clarity: '', endpoint: '' };
```

## O que o cliente (ou a agência) precisa criar e passar

| Ferramenta | O que criar | O que preencher | Para que serve |
|---|---|---|---|
| **Google Tag Manager** (recomendado) | Contêiner web | `gtm: 'GTM-XXXXXXX'` | Um lugar só para GA4, Meta e o resto, sem mexer no código |
| Google Analytics 4 | Propriedade GA4 | `ga4: 'G-XXXXXXXXXX'` (só se **não** usar GTM) | Visitas, origem, eventos |
| Meta Pixel | Pixel no Gerenciador de Eventos | `meta: '1234567890'` (só se **não** usar GTM) | Medir e otimizar anúncios |
| API de Conversões da Meta | Token de acesso + um endpoint (ver abaixo) | `endpoint: 'https://…'` | Medição que não depende do navegador; recupera o que bloqueadores cortam |
| Microsoft Clarity | Projeto Clarity | `clarity: 'xxxxxxxxxx'` | Mapa de calor e gravação de sessão |
| Google Search Console / Bing | Verificar o domínio | meta de verificação no `<head>` | Aparecer no Google e achar problemas |

Com GTM, `ga4`/`meta`/`clarity` ficam vazios: as tags vivem dentro do contêiner e leem os eventos abaixo.

## Regras que o código já cumpre (Espanha, RGPD, LSSI)
- **Nada carrega antes do consentimento.** Consent Mode v2 começa com tudo negado; a faixa pede Analítica e Marketing.
- **Aceitar e recusar têm o mesmo peso** (três botões iguais: Rechazar, Ajustes, Aceptar todo) e a escolha se muda em "Preferencias de cookies" (rodapé). A faixa é o primeiro item do teclado, a escolha vence em 24 meses, e **retirar o consentimento apaga os cookies e recarrega a página**.
- **A faixa só aparece quando há ao menos um ID configurado** (ou em `index.html?cookies=1`, para mostrar ao cliente): sem ferramenta, não há o que consentir.
- **Nenhum dado pessoal entra em evento** (nome, telefone, e-mail). Só metadados: botão, seção, canal, interesse, campanha.
- Sem ID configurado, nada externo é baixado: o PageSpeed não muda.
- Escolha guardada em `localStorage` (`rca_consent_v1`); a animação de entrada usa `sessionStorage` (`rca_intro_v1`).

## Eventos (nomes no dataLayer)

| Evento | Quando dispara | Meta (`meta_event`) | GA4 |
|---|---|---|---|
| `page_view` | Abrir a página | PageView | page_view |
| `section_view` | Cada seção vista (1x) | — | personalizado |
| `scroll_depth` | 25, 50, 75, 90 % | — | personalizado |
| `cta_propuesta` | Botão "Pedir propuesta" (cabeçalho, topo, menu, cartões) | — | personalizado (`label` diz onde) |
| `cta_formas`, `cta_medidas` | Botões secundários | — | personalizado |
| `form_start` | Primeiro foco no formulário | — | personalizado |
| `generate_lead` | Enviou pelo WhatsApp ou pelo correo (`channel`, `interest`) | **Lead** | **generate_lead** (marcar como conversão) |
| `click_whatsapp`, `click_email` | Cliques em WhatsApp/correo (flutuante, rodapé, contato) | **Contact** | personalizado |
| `click_social` | Clique no Instagram | — | personalizado |
| `video_play` | Clipe da pista começa | ViewContent | personalizado |
| `consent_update` | Mudou a escolha de cookies | — | — |

Todo evento leva `event_id` (para **deduplicar** o Pixel do navegador com a API de Conversões) e, se a visita veio de campanha,
`utm_source/medium/campaign/content/term`, `fbclid`, `gclid`, `ttclid`.

## Atribuição do WhatsApp
Quem pede por WhatsApp não passa por um "obrigado" que se possa medir. Por isso a mensagem leva no fim `Ref: instagram/cpc/campanha`
(o utm da visita) quando existe. O cliente vê de onde veio o contato; no GTM/GA4 o `generate_lead` leva o mesmo utm.

## API de Conversões da Meta (servidor)
O site é estático e não tem servidor. O código já envia, só com consentimento de marketing, um aviso (`navigator.sendBeacon`) para o
`endpoint` com: `event_name`, `event_id`, `event_time`, URL, `fbp`, `fbc` (montado do `fbclid`) e parâmetros. **Sem e-mail, telefone ou nome.**
Falta do lado do cliente/agência um receptor desse aviso que repasse à Meta com o token:
1. mais simples: **GTM de servidor** (Stape ou Google Cloud) com a tag de API de Conversões;
2. ou uma função serverless (Cloudflare Worker / Vercel) que recebe o JSON e chama `graph.facebook.com/<pixel>/events`.
O token **nunca** vai para o código do site (regra de segurança do projeto): fica no receptor.

## Antes de ligar em produção
- [ ] Cliente passa os IDs e autoriza as ferramentas.
- [ ] `cookies.html` e `privacidad.html` ajustadas às ferramentas realmente ativas (hoje listam as previstas).
- [ ] Titular, NIF e domicílio nas páginas legais.
- [ ] Testar com GTM Preview, Meta "Testar eventos" e GA4 DebugView.
- [ ] Medir o PageSpeed de novo (GTM e Pixel pesam; carregam só após consentimento).
