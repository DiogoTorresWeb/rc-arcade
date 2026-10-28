# 05 — O site atual do cliente (rcarcade.es / rcarcade.com): desde quando, como foi feito, nota

> Tipo: **estudo** (análise de 28/10/2026, feita por mim, não por agente). Cópia completa do site em
> `cliente/acervo-dropbox/site-antigo-rcarcade-es/` (fora do git; registrada em `cliente/ACERVO.md`).
> Telefones e e-mail da página **não** estão copiados aqui (regra do estudo 02: confirmar com o cliente antes de usar).

## 1. Desde quando

| Fato | Valor | Como foi conferido |
|---|---|---|
| `rcarcade.com` registrado | **21/04/2026** (atualizado 20/06/2026; vence 21/04/2027), registrador espanhol Arsys/Nicline | WHOIS do `.com` (Verisign) — CONFIRMADO |
| O `.com` já teve outro dono antes | cópias em 2011 e certificados GoDaddy de 2019/2020: era de terceiros e o registro caiu | arquivo da internet + crt.sh — CONFIRMADO (o dono antigo não é o cliente) |
| Logo do site (`logo-emblema.png`) enviado | **22/06/2026** | cabeçalho `Last-Modified` — CONFIRMADO |
| Fotos e página `.es` enviadas | **15/09/2026**; página `.es` e foto de abertura: **17/09/2026** | `Last-Modified` — CONFIRMADO |
| Versão mais nova (só no `.com`) | **01/10/2026** (página, logo menor/maior e foto de abertura nova) e **09/10/2026** (foto do arco Dunlop trocada) | `Last-Modified` — CONFIRMADO |
| Certificado HTTPS do `.com` | emitido **01/10/2026** (Sectigo) | crt.sh — CONFIRMADO |
| `rcarcade.es`: conteúdo | página e fotos de **15–17/09/2026**; nenhuma cópia no arquivo da internet | `Last-Modified` — CONFIRMADO |
| `rcarcade.es`: certificado HTTPS | **um só**, emitido **01/10/2026** (Sectigo), o mesmo dia do `.com`; nenhum anterior nos registros públicos | crt.sh e leitura direta — CONFIRMADO |
| `rcarcade.es`: hospedagem | mesmos servidores de nome (Piensa Solutions) e mesmo servidor Apache do `.com`: **mesma conta de hospedagem** | DNS — CONFIRMADO |
| `rcarcade.es`: **data de registro do domínio** | WHOIS de `.es` não é público (Red.es) | **NÃO VERIFICADO.** Só o cliente (ou o painel do registrador) sabe. |

**Conclusão para o `.es`:** o site no ar tem **cerca de 6 semanas** (conteúdo de 15–17/09/2026) e só ganhou HTTPS em
01/10/2026. Antes disso não há rastro público. O domínio em si pode ter sido registrado antes, mas **não há prova**.
O `.es` ficou parado na versão de 17/09; a mais nova está no `.com` (01 e 09/10). São duas cópias que já divergem.

## 2. Como foi feito

**Uma única página HTML escrita à mão (ou por IA), sem nenhum programa de site por trás.**
- 27 KB, 558 linhas, **CSS dentro do arquivo**, **zero JavaScript**, sem WordPress nem construtor (sem `wp-login`, sem `wp-json`). Servidor Apache comum.
- 23 seções numeradas por comentários (`02 CONCEPTO` … `22 SIGUIENTE PASO`) e o rodapé "**Presentación corporativa · V1 2026**":
  é uma **apresentação (deck) de slides convertida em página**, um slide por seção.
- Fotos reais do cliente, cortadas no formato de slide (≈995×1166 px), enviadas todas ao mesmo tempo em 15/09.

**Há prova de IA em duas imagens (metadados assinados, não opinião):**
- `logo-emblema.png`: assinatura **C2PA da OpenAI** ("gpt-image", `trainedAlgorithmicMedia` = "gerado por IA"). **O logo do escudo foi feito com ChatGPT.** A versão do `.com` (01/10) foi redimensionada para 1024×1024 e perdeu a assinatura, mas é a mesma arte refeita.
- `hero-pista.png` (só no `.com`, 01/10/2026 15:15 UTC): assinatura C2PA do ChatGPT. É a **foto real da pista, retocada pelo ChatGPT**: sumiram o saco plástico, a caixa de papelão e os fios soltos do canto direito.
- As outras 15 fotos não têm metadados (foram reexportadas): **não dá para afirmar** se foram retocadas. À vista, são fotos reais do evento.

**Sobre o código:** o desenho (variáveis de cor, cortes inclinados, comparação "RCArcade vs Simulador", 23 seções repetindo
os mesmos 4 ou 5 blocos) tem **cara de código gerado por IA a partir do deck**, mas **não há prova** disso no arquivo. Fica como INFERÊNCIA.

## 3. Nota

**5 de 10 como site de captação B2B. 7 de 10 como apresentação corporativa na web.** (Opinião minha, com a régua abaixo.)

| Critério | Nota | Porquê |
|---|---|---|
| Texto e proposta | 7,5 | Claro, sem enrolação, bom "No es un videojuego. No es solo radiocontrol", tabela contra simulador, "Cinco datos bastan". Faltam números (m², preço, retorno) e prova (vídeo, depoimento). |
| Visual | 7 | Escuro com vermelho, fotos reais, hierarquia boa. Parece slide, não site: sem movimento, sem vídeo, sem a "sensação de estar dentro do carro". |
| Prova real | 3 | Só fotos paradas. **Nenhum vídeo**, e o vídeo é o que mais vende. |
| Conversão | 3 | Não tem formulário nem botão de pedir demonstração: só um e-mail e dois telefones no fim. |
| SEO e técnica | 2 | Sem descrição, sem imagem de compartilhamento, sem ícone, sem `robots`/`sitemap`, sem dados estruturados, sem redirecionamento entre as 4 versões (`.es`/`.com`, com/sem `www`). Fotos sem texto alternativo útil. Mesmo assim aparece em 1º para "rc arcade" (concorrência fraca). |
| Mobile | 5 | Um só ponto de quebra (860 px); funciona, mas sem cuidado. |
| Manutenção | 3 | Duas cópias divergentes; atualizar é editar arquivo à mão. |

## 4. O que isso muda para o nosso site

1. O nosso site não parte do zero: **tem de ser claramente melhor que isto** em prova (vídeo), conversão (formulário e "¿Cabe en tu espacio?") e SEO.
2. **Reaproveitar o texto do cliente é seguro e coerente** (a voz já é dele); a tabela e os "cinco dados" já existem lá.
3. **Logo oficial:** o do escudo é gerado por IA e tem arte com defeitos de detalhe (letras do painel ilegíveis). Perguntar ao cliente se há logo vetorial de origem (`marca video.png` e os 8 logos do Dropbox podem ser outros: conferir).
4. **A foto de abertura do `.com` é retocada por IA** (a cena é real, o saco plástico e a caixa foram removidos). Isso é aceitável como limpeza, mas **a regra de honestidade** pede dizer ao cliente que sabemos, e não passar por foto crua.
5. Perguntas novas para o cliente: quem fez o site (agência, ele mesmo, IA)? por que existem duas versões? quem controla o `rcarcade.es` (data de registro)? o logo tem arquivo original?
