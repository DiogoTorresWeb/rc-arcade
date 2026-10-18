# RC Arcade — status atual

> Tipo: **estado** — reescrito quando muda. Não acumula histórico.
> Atualizado: 18/10/2026 · Revisar até: 18/11/2026 · Dono: Diogo
> Regra: `../../SISTEMA.md`. Lições que valem aqui: `../../Recursos/aprendizados/INDEX.md`.

**Onde o projeto está (30/09):** o site saiu do papel. Em 24/09 foram feitos a
estrutura em HTML/CSS, o registro visual "Porsche" (intro, logo ao centro,
tipografia), o Design Gate na Direção de Arte V2 e três itens do plano — "Qué
es" como timeline horizontal, "Para el operador" como manifesto e "Contacto"
como fechamento silencioso. Está publicado no GitHub Pages.
**Próximo passo:** seguir `PLANO-IMPLEMENTACAO-V2.md`.
**Referências visuais guardadas para essa hora:** `REFERENCIAS.md` — o Diogo mandou a do Nick Ho Motorsports em 18/10.

O material abaixo é do levantamento de **13/09**, quando nenhuma linha de site
existia ainda. Continua valendo como retrato do que o cliente entregou e do que
foi decidido na Etapa 1 — só não descreve mais o estado do código.

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
