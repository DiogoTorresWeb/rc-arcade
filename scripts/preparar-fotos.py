"""Prepara as fotos do acervo para o site: recorte, acerto de cor único e tamanhos leves.

Uso (da pasta do projeto):  python -I scripts/preparar-fotos.py

As originais (4000x5000) moram em cliente/acervo-dropbox/extraido/insta e NÃO vão ao git.
A saída vai para assets/fotos/ em WebP (e AVIF onde compensa).
O acerto de cor é o mesmo para todas: sombras frias, vermelho vivo, grão leve — o tratamento do topo.
"""
import os
import numpy as np
from PIL import Image, ImageEnhance

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORIG = os.path.join(RAIZ, "cliente", "acervo-dropbox", "extraido", "insta")
SAIDA = os.path.join(RAIZ, "assets", "fotos")
os.makedirs(SAIDA, exist_ok=True)

rng = np.random.default_rng(7)


def acerto(im):
    """Um tratamento só para todas as fotos."""
    a = np.asarray(im.convert("RGB")).astype(np.float32) / 255.0
    # contraste suave em S
    a = np.clip((a - 0.5) * 1.08 + 0.5, 0, 1)
    lum = (a[..., 0] * 0.3 + a[..., 1] * 0.59 + a[..., 2] * 0.11)[..., None]
    # sombras frias (puxa o azul nas partes escuras)
    sombra = np.clip(1 - lum * 2.2, 0, 1)
    a[..., 2] += sombra[..., 0] * 0.035
    a[..., 0] -= sombra[..., 0] * 0.012
    # vermelho um pouco mais vivo
    a[..., 0] = np.clip(a[..., 0] * 1.025, 0, 1)
    # grão leve
    a += rng.normal(0, 0.011, a.shape[:2])[..., None]
    out = Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8))
    return ImageEnhance.Color(out).enhance(1.06)


def recorte(im, caixa):
    w, h = im.size
    x0, y0, x1, y1 = caixa
    return im.crop((int(x0 * w), int(y0 * h), int(x1 * w), int(y1 * h)))


def salvar(im, nome, larguras, q=74, avif=False):
    for L in larguras:
        h = round(im.height * L / im.width)
        r = im.resize((L, h), Image.LANCZOS)
        r.save(os.path.join(SAIDA, f"{nome}-{L}.webp"), "WEBP", quality=q, method=6)
        if avif:
            r.save(os.path.join(SAIDA, f"{nome}-{L}.avif"), "AVIF", quality=52, speed=6)
    print(nome, larguras)


def abrir(n):
    return Image.open(os.path.join(ORIG, f"DSC0{n}.jpg")).convert("RGB")


# (arquivo, nome, recorte relativo (x0,y0,x1,y1), larguras)
FOTOS = [
    ("9882", "paso-elige", (0, 0, 1, 1), [560, 880]),     # dois carros, vista alta
    ("9871", "paso-sientate", (0, 0, 1, 1), [560, 880]),    # cockpits em fila
    ("9884", "paso-conduce", (0, 0, 1, 1), [560, 880]),     # câmera FPV montada no carro
    ("9897", "paso-compite", (0, 0, 1, 1), [560, 880]),     # carro numa curva
    ("9893", "escala-compacto", (0, 0.05, 1, 0.65), [640, 1000]),
    ("9875", "escala-completo", (0, 0.12, 1, 0.72), [640, 1000]),
]
for n, nome, caixa, L in FOTOS:
    salvar(acerto(recorte(abrir(n), caixa)), nome, L)

# faixa larga do operador: escudo aceso (recorte largo para PC, retrato para celular)
im = abrir("9876")
salvar(acerto(recorte(im, (0, 0.03, 1, 0.46))), "operador-faixa", [1280, 1920], q=72)
salvar(acerto(recorte(im, (0, 0.0, 1, 0.78))), "operador-retrato", [640, 960], q=72)

# contacto: pórtico aceso, escurecido para ficar de fundo
im = acerto(recorte(abrir("9877"), (0, 0.0, 1, 0.85)))
im = ImageEnhance.Brightness(im).enhance(0.55)
salvar(im, "contacto-fondo", [960, 1600], q=62)

# clipe de pista (poster do vídeo): quadro do vídeo de Cheste é tratado à parte pelo ffmpeg
print("ok")
