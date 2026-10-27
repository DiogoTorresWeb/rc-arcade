# Capturar telas do site em vários tamanhos

> Tipo: **runbook** — reescrito quando o procedimento mudar. Passo a passo executável.

**Por que não o painel do navegador do app:** quando a tela emulada é maior que o painel, a captura
sai recortada (canto superior esquerdo), e o layout parece quebrado sem estar. E o
`chrome --headless --screenshot` fotografa a animação de entrada pela metade. Este script abre o
Chrome por DevTools Protocol, pula a intro, espera em tempo real e captura no tamanho pedido.

**Pré-requisitos:** Chrome em `C:\Program Files\Google\Chrome\Application\chrome.exe` (ou variável
`CHROME`); `python -m pip install websockets`.

1. Servidor, na pasta do projeto: `python -m http.server 8791`
2. Capturar (a saída vai para `RCA_OUT`, padrão a pasta temporária do sistema):

```bash
RCA_OUT=./capturas python -W ignore scripts/shots.py '[["A-1440",1440,810,0,"?hero=a",0],["A-1024",1024,768,0,"?hero=a",0],["A-768",768,1024,0,"?hero=a",0],["A-390",390,844,1,"?hero=a",0]]'
```

Cada item: `nome, largura, altura, celular(1/0), query, rolagem em px`, e um 7º campo opcional com uma
expressão JavaScript cujo resultado é impresso (útil para `getBoundingClientRect`).

3. Para ver a intro de racing, rode com `INTRO=1` (sem isso ela é pulada).
4. Se a captura discordar da medida por JavaScript, desconfie da captura primeiro.

**Tamanhos usados na validação:** 1440×810, 1024×768, 768×1024 (tablet em pé usa o recorte
retrato) e 390×844 (celular, `mobile=1`).
