"""Gera estudo/carro-43/carro-v1.html: o 43 desenhado em vetor, visto de cima (frente para baixo).
Teste para o Diogo ver antes de animar. Nao mexe no site. Rodar: python -I gerar-carro-v1.py"""
import math
import os
import random

AQUI = os.path.dirname(os.path.abspath(__file__))
random.seed(43)

# contorno da carroceria (frente = baixo). viewBox 200 x 440
CORPO = ("M52 62 Q100 34 148 62 L156 150 L158 262 L150 362 Q142 412 100 424 "
         "Q58 412 50 362 L42 262 L44 150 Z")


def mancha(cx, cy, r):
    """polígono irregular, estilo 'rachadura' da pintura"""
    n = random.randint(6, 9)
    pts = []
    for i in range(n):
        a = 2 * math.pi * i / n + random.uniform(-0.25, 0.25)
        rr = r * random.uniform(0.35, 1.15)
        pts.append("%.1f,%.1f" % (cx + rr * math.cos(a), cy + rr * math.sin(a)))
    return '<polygon points="%s"/>' % " ".join(pts)


def campo(y0, y1, qtd, rmin, rmax):
    out = []
    for _ in range(qtd):
        out.append(mancha(random.uniform(44, 156), random.uniform(y0, y1), random.uniform(rmin, rmax)))
    return "".join(out)


# traseira e teto: mais branco; capô: mais preto com rachaduras brancas finas
brancas = campo(52, 150, 34, 4, 11) + campo(150, 262, 40, 3, 10) + campo(262, 420, 30, 2, 6)
pretas_no_teto = campo(70, 230, 16, 3, 7)

svg = f"""<svg class="carro" viewBox="0 0 200 440" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Coche RC de rally número 43, visto desde arriba">
  <defs>
    <clipPath id="c"><path d="{CORPO}"/></clipPath>
    <linearGradient id="brilho" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity=".0"/><stop offset=".5" stop-color="#fff" stop-opacity=".16"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
    <filter id="sombra" x="-30%" y="-10%" width="160%" height="130%"><feGaussianBlur stdDeviation="7"/></filter>
  </defs>
  <!-- sombra no chão -->
  <ellipse cx="100" cy="236" rx="82" ry="196" fill="#000" opacity=".45" filter="url(#sombra)"/>
  <!-- rodas: pneu preto, aro branco aparecendo por dentro -->
  <g>
    <rect x="14" y="86" width="26" height="44" rx="7" fill="#0b0b0c" stroke="#6d7077" stroke-width="1.2"/><rect x="33" y="94" width="7" height="30" rx="3" fill="#f1f1ee"/>
    <rect x="160" y="86" width="26" height="44" rx="7" fill="#0b0b0c" stroke="#6d7077" stroke-width="1.2"/><rect x="162" y="94" width="7" height="30" rx="3" fill="#f1f1ee"/>
    <rect x="14" y="320" width="26" height="44" rx="7" fill="#0b0b0c" stroke="#6d7077" stroke-width="1.2"/><rect x="33" y="328" width="7" height="30" rx="3" fill="#f1f1ee"/>
    <rect x="160" y="320" width="26" height="44" rx="7" fill="#0b0b0c" stroke="#6d7077" stroke-width="1.2"/><rect x="162" y="328" width="7" height="30" rx="3" fill="#f1f1ee"/>
  </g>
  <!-- asa traseira -->
  <rect x="48" y="28" width="104" height="14" rx="3" fill="#0c0d0e"/>
  <rect x="44" y="26" width="8" height="26" rx="2" fill="#0c0d0e"/><rect x="148" y="26" width="8" height="26" rx="2" fill="#0c0d0e"/>
  <rect x="54" y="31" width="92" height="3" rx="1.5" fill="#2a2c30"/>
  <!-- carroceria -->
  <path d="{CORPO}" fill="#101113" stroke="#9a9da4" stroke-width="1.6" stroke-linejoin="round"/>
  <g clip-path="url(#c)">
    <g fill="#f2f2ee">{brancas}</g>
    <g fill="#101113">{pretas_no_teto}</g>
    <!-- teto: faixa branca limpa onde fica o 43 -->
    <rect x="70" y="112" width="60" height="70" rx="10" fill="#f4f4f0" opacity=".92"/>
    <!-- vidros laterais -->
    <path d="M52 172 L74 176 L74 252 L50 258 Z" fill="#1c1e22"/>
    <path d="M148 172 L126 176 L126 252 L150 258 Z" fill="#1c1e22"/>
    <!-- parabrisa aberto e traseiro -->
    <path d="M70 196 L130 196 L136 272 L64 272 Z" fill="#17181b"/>
    <path d="M72 200 L128 200 L130 214 L70 214 Z" fill="#2a2d33"/>
    <!-- listras verdes do capô e das caixas de roda -->
    <path d="M60 396 Q50 352 66 300" fill="none" stroke="#3ee03a" stroke-width="9" stroke-linecap="round"/>
    <path d="M140 396 Q150 352 134 300" fill="none" stroke="#3ee03a" stroke-width="9" stroke-linecap="round"/>
    <path d="M52 372 L52 330" stroke="#3ee03a" stroke-width="5" stroke-linecap="round"/>
    <path d="M148 372 L148 330" stroke="#3ee03a" stroke-width="5" stroke-linecap="round"/>
    <!-- faróis -->
    <path d="M62 408 Q72 400 84 404 L82 412 Q72 414 64 418 Z" fill="#050506"/>
    <path d="M138 408 Q128 400 116 404 L118 412 Q128 414 136 418 Z" fill="#050506"/>
    <!-- grade frontal -->
    <rect x="76" y="414" width="48" height="8" rx="2" fill="#2b2d31"/>
    <!-- ovais azuis (SONIC) -->
    <ellipse cx="100" cy="364" rx="14" ry="7" fill="#1f74d6"/>
    <ellipse cx="100" cy="76" rx="14" ry="6.5" fill="#1f74d6"/>
    <!-- número 43 no teto (lido de lado, como na pintura real) -->
    <text x="100" y="156" text-anchor="middle" transform="rotate(90 100 147)" font-family="Anton, Impact, 'Archivo Black', sans-serif" font-size="40" font-weight="700" fill="#f08a1c" letter-spacing="1">43</text>
    <!-- bandeira no teto -->
    <rect x="86" y="186" width="28" height="9" fill="#2a4aa0"/>
    <path d="M86 192 H114 M86 189 H114" stroke="#d93232" stroke-width="1.4"/>
    <!-- brilho de verniz -->
    <rect x="42" y="60" width="116" height="364" fill="url(#brilho)"/>
  </g>
  <!-- câmera FPV no teto, lente para a frente (para baixo) -->
  <g>
    <rect x="84" y="228" width="32" height="30" rx="4" fill="#5b5f66"/>
    <rect x="86" y="230" width="28" height="9" rx="2" fill="#7b8088"/>
    <circle cx="100" cy="262" r="11" fill="#17181a"/>
    <circle cx="100" cy="262" r="6.5" fill="#050506"/>
    <circle cx="97.5" cy="259.5" r="2" fill="#4a5b78" opacity=".7"/>
  </g>
  <!-- espelhos/ganchos -->
  <circle cx="58" cy="150" r="2.4" fill="#c7c9cc"/><circle cx="142" cy="150" r="2.4" fill="#c7c9cc"/>
</svg>"""

html = f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Teste do carro 43 (vetor, v1)</title>
<style>
  body{{margin:0;background:#0a0b0d;color:#b1b0ab;font:14px/1.5 system-ui,sans-serif;padding:24px}}
  h1{{font-size:15px;font-weight:600;margin:0 0 4px;color:#fff}}
  p{{margin:0 0 16px;max-width:60ch}}
  .linha{{display:flex;gap:40px;align-items:flex-end;flex-wrap:wrap}}
  .carro{{display:block;height:auto}}
  .grande .carro{{width:320px}}
  .pequeno .carro{{width:183px}}
  .tag{{font:500 11px/1.4 ui-monospace,monospace;letter-spacing:.12em;text-transform:uppercase;margin-top:8px;color:#8a8984}}
</style></head><body>
<h1>Carro 43 visto de cima — teste em vetor (v1)</h1>
<p>Desenhado a partir das fotos DSC09882, 09884 e 09861 (carro nº 43 com câmera FPV no teto). Frente para baixo, como no Nick Ho. Só para avaliar; não está no site.</p>
<div class="linha">
  <div class="grande">{svg}<div class="tag">PC · 320 px</div></div>
  <div class="pequeno">{svg.replace('id="c"', 'id="c2"').replace('url(#c)', 'url(#c2)').replace('id="brilho"', 'id="brilho2"').replace('url(#brilho)', 'url(#brilho2)').replace('id="sombra"', 'id="sombra2"').replace('url(#sombra)', 'url(#sombra2)')}<div class="tag">Celular · 183 px</div></div>
</div>
</body></html>"""

with open(os.path.join(AQUI, "carro-v1.html"), "w", encoding="utf-8") as f:
    f.write(html)
print("ok", len(html), "bytes")
