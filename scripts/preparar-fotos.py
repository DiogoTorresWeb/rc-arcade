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

# pista inteira (faixa grande com paralaxe; PC largo, celular mais alto)
im = abrir("9875")
salvar(acerto(recorte(im, (0, 0.20, 1, 0.70))), "pista-completa", [1280, 1920], q=72)
salvar(acerto(recorte(im, (0, 0.14, 1, 0.78))), "pista-completa-m", [640, 960], q=72)

# galeria por tópicos (4:5, só 560 e 880; carregam ao abrir a aba)
for n in ["9867", "9874", "9877", "9893", "9897",            # pista
          "9860", "9873", "9905",                              # cabinas
          "9864", "9901", "9902",                              # coches
          "9861", "9862", "9865", "9868", "9876", "9889"]:     # marcas en pista
    salvar(acerto(abrir(n)), f"gal-{n}", [560, 880])

# galeria, tópico Eventos: quadros do vídeo `RC ARCADE CHESTE HD.mp4` (1080x1920), extraídos a cada 2 s com
#   ffmpeg -i "RC ARCADE CHESTE HD.mp4" -vf fps=1/2 -q:v 2 f%02d.jpg ; recorte 4:5 com deslocamento vertical por quadro
QUADROS = os.environ.get("QUADROS_CHESTE")
if QUADROS:
    for n, desloc in [("07", 0.0), ("09", 0.3), ("10", 0.0), ("11", 0.1), ("13", 0.4), ("15", 0.2), ("26", 0.1), ("28", 0.4)]:
        q = Image.open(os.path.join(QUADROS, f"f{n}.jpg")).convert("RGB")
        y0 = int(desloc * (q.height - 1350))
        salvar(acerto(q.crop((0, y0, 1080, y0 + 1350))), f"gal-ev-{n}", [560, 880])

# capa do cartão de Madrid de "Prensa y registro" (16:10; 330 e 660 de largura)
# Só entra foto cuja origem se confirma: a de 3-7-26 11:17 (celular, pasta Open Rcarcade) cai nas datas da jornada de Madrid (2-3 jul).
# TV (El Hormiguero) e Zaragoza (Volrace) ficam SEM foto até o cliente mandar imagem desses eventos.
OPEN = os.path.join(RAIZ, "cliente", "acervo-dropbox", "extraido", "open-fotos")
f = os.path.join(OPEN, "Foto 3-7-26, 11 17 09.jpg")
if os.path.exists(f):
    from PIL import ImageOps
    im = ImageOps.exif_transpose(Image.open(f)).convert("RGB")
    h = int(im.width * 10 / 16)
    y0 = int(0.28 * (im.height - h))
    salvar(acerto(im.crop((0, y0, im.width, y0 + h))), "prensa-madrid", [330, 660], q=72)

# "Dos formas de contratarla": foto no alto de cada cartão (16:10; 640 e 1000)
# Evento: quadro f26 do vídeo de Cheste (arco Dunlop com a equipe e o público) · Instalación fija: foto 9874
if os.environ.get("QUADROS_CHESTE"):
    q = Image.open(os.path.join(os.environ["QUADROS_CHESTE"], "f26.jpg")).convert("RGB")
    y0 = int(0.15 * (q.height - 675))
    salvar(acerto(q.crop((0, y0, 1080, y0 + 675))), "forma-evento", [640, 1000], q=72)
im = abrir("9874")
y0 = int(0.30 * (im.height - 2500))
salvar(acerto(im.crop((0, y0, im.width, y0 + 2500))), "forma-instalacion", [640, 1000], q=72)

# contacto: pórtico aceso, escurecido para ficar de fundo
im = acerto(recorte(abrir("9877"), (0, 0.0, 1, 0.85)))
im = ImageEnhance.Brightness(im).enhance(0.55)
salvar(im, "contacto-fondo", [960, 1600], q=62)

# clipe de pista (poster do vídeo): quadro do vídeo de Cheste é tratado à parte pelo ffmpeg
print("ok")
