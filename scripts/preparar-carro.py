"""Receita do carro 43 visto de cima (o 'carro que desce' de Cómo trabajamos).
Origem: estudo/carro-43/carro-43-recorte.png (gerado por estudo/carro-43/recortar-carro.py a partir de
ia-43-original.png, imagem feita por IA a partir das fotos reais DSC09882 e DSC09884 do carro nº 43).
Saida: assets/fotos/carro-43-280.webp e carro-43-488.webp (com transparencia).

Tratamento para o carro conversar com o resto do site (o recorte cru parecia 'colado'):
 1. borda: o alfa perde 1,5 px e as cores da faixa de borda vem de dentro do carro (tira o farelo cinza do fundo);
 2. o mesmo acerto de cor das fotos do site (contraste em S, sombras frias, vermelho vivo, saturacao 1,06, grao leve);
 3. luz de estudio mais baixa: exposicao -7 %, brancos comprimidos e vinheta leve nas pontas, como as fotos escuras do site.
Rodar: python -I scripts/preparar-carro.py"""
import os
import numpy as np
from PIL import Image, ImageEnhance
from scipy import ndimage as ndi

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rng = np.random.default_rng(7)

src = Image.open(os.path.join(RAIZ, "estudo", "carro-43", "carro-43-recorte.png")).convert("RGBA")
print("origem", src.size)
rgb = np.asarray(src.convert("RGB")).astype(np.float32) / 255.0
alfa = np.asarray(src.split()[3]).astype(np.float32) / 255.0

# 1. borda limpa
miolo = alfa > 0.98
miolo_in = ndi.binary_erosion(miolo, iterations=4)
_, (iy, ix) = ndi.distance_transform_edt(~miolo_in, return_indices=True)
faixa = ndi.binary_dilation(miolo_in, iterations=0) ^ True  # tudo fora do miolo seguro
rgb = np.where(faixa[..., None], rgb[iy, ix], rgb)
duro = ndi.binary_erosion(alfa > 0.5, iterations=2)  # perde ~1,5 px
alfa = ndi.gaussian_filter(duro.astype(np.float32), 0.9)

# 2. acerto de cor do site
a = np.clip((rgb - 0.5) * 1.08 + 0.5, 0, 1)
lum = (a[..., 0] * 0.3 + a[..., 1] * 0.59 + a[..., 2] * 0.11)[..., None]
sombra = np.clip(1 - lum * 2.2, 0, 1)
a[..., 2] += sombra[..., 0] * 0.035
a[..., 0] -= sombra[..., 0] * 0.012
a[..., 0] = np.clip(a[..., 0] * 1.025, 0, 1)

# 3. menos luz de estudio: exposicao, brancos comprimidos, vinheta leve
a = a * 0.93
a = a / (1 + 0.16 * a * a)
a = a * 1.08
h, w = a.shape[:2]
yy, xx = np.mgrid[0:h, 0:w]
r2 = ((xx - w / 2) / (w / 2)) ** 2 * 0.55 + ((yy - h / 2) / (h / 2)) ** 2 * 0.45
a = a * (1 - 0.11 * np.clip(r2, 0, 1.2))[..., None]
a += rng.normal(0, 0.009, (h, w))[..., None]
a = np.clip(a, 0, 1)
tratado = ImageEnhance.Color(Image.fromarray((a * 255).astype(np.uint8))).enhance(1.06)
out_rgba = tratado.convert("RGBA")
out_rgba.putalpha(Image.fromarray((np.clip(alfa, 0, 1) * 255).astype(np.uint8)))
out_rgba.save(os.path.join(RAIZ, "estudo", "carro-43", "carro-43-tratado.png"))

for largura in (280, 488):
    alt = round(out_rgba.height * largura / out_rgba.width)
    im = out_rgba if largura >= out_rgba.width else out_rgba.resize((largura, alt), Image.LANCZOS)
    destino = os.path.join(RAIZ, "assets", "fotos", f"carro-43-{largura}.webp")
    im.save(destino, "WEBP", quality=82, method=6, alpha_quality=90)
    print(destino, im.size, os.path.getsize(destino) // 1024, "KB")
