"""Receita do carro 43 visto de cima (o 'carro que desce' de Cómo trabajamos).
Origem: estudo/carro-43/carro-43-recorte.png (gerado por estudo/carro-43/recortar-carro.py a partir de
ia-43-original.png, imagem feita por IA a partir das fotos reais DSC09882 e DSC09884 do carro nº 43).
Saida: assets/fotos/carro-43-300.webp e carro-43-532.webp (com transparencia).

Tratamento para o carro conversar com o resto do site (o recorte cru parecia 'colado'):
 1. borda: o alfa perde 1,5 px e as cores da faixa de borda vem de dentro do carro (tira o farelo cinza do fundo);
 2. o mesmo acerto de cor das fotos do site (contraste em S, sombras frias, vermelho vivo, saturacao 1,06, grao leve);
 3. luz de estudio mais baixa: exposicao -7 %, brancos comprimidos e vinheta leve nas pontas, como as fotos escuras do site;
 4. paleta do site: verde neon e laranja com menos saturacao; silhueta arredondada (sem farelos brancos soltos);
 5. luz vermelha de contorno cozida na imagem (22 px de margem transparente com halo), como o escudo aceso da marca.
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
# silhueta mais limpa: tira os farelos brancos soltos das laterais (abertura) e arredonda mordidas (fechamento)
from skimage import morphology
duro = ndi.binary_opening(duro, structure=morphology.disk(5))
duro = ndi.binary_closing(np.pad(duro, 20), structure=morphology.disk(9))[20:-20, 20:-20]
duro = ndi.binary_fill_holes(duro)
alfa = ndi.gaussian_filter(duro.astype(np.float32), 1.1)

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
# paleta do site (preto, prata, vermelho): o verde neon e o laranja gritavam; baixo a saturacao so deles
import colorsys
hsv = np.stack(np.vectorize(colorsys.rgb_to_hsv)(a[..., 0], a[..., 1], a[..., 2]), axis=-1)
hh = hsv[..., 0] * 360
verde = np.exp(-((hh - 118) / 38) ** 2)
laranja = np.exp(-((hh - 30) / 16) ** 2)
hsv[..., 1] *= 1 - 0.28 * verde - 0.16 * laranja
hsv[..., 2] *= 1 - 0.12 * verde
a = np.stack(np.vectorize(colorsys.hsv_to_rgb)(hsv[..., 0], hsv[..., 1], hsv[..., 2]), axis=-1).astype(np.float32)
tratado = ImageEnhance.Color(Image.fromarray((a * 255).astype(np.uint8))).enhance(1.06)
MARGEM = 22
rgb8 = np.pad(np.asarray(tratado).astype(np.float32), ((MARGEM, MARGEM), (MARGEM, MARGEM), (0, 0)), mode="edge")
al = np.pad(np.clip(alfa, 0, 1), MARGEM)
# luz de contorno: 2 halos vermelhos (perto e largo) so FORA do carro; a cor do carro nao muda
halo = np.clip(ndi.gaussian_filter(al, 5) * 0.55 + ndi.gaussian_filter(al, 12) * 0.35, 0, 1) * (1 - al)
vermelho = np.array([227, 27, 35], np.float32)
alfa_out = al + halo
rgb_out = (rgb8 * al[..., None] + vermelho * halo[..., None]) / np.maximum(alfa_out, 1e-4)[..., None]
out_rgba = Image.fromarray(np.dstack([np.clip(rgb_out, 0, 255), np.clip(alfa_out, 0, 1) * 255]).astype(np.uint8), "RGBA")
out_rgba.save(os.path.join(RAIZ, "estudo", "carro-43", "carro-43-tratado.png"))

for largura in (300, 532):
    alt = round(out_rgba.height * largura / out_rgba.width)
    im = out_rgba if largura >= out_rgba.width else out_rgba.resize((largura, alt), Image.LANCZOS)
    destino = os.path.join(RAIZ, "assets", "fotos", f"carro-43-{largura}.webp")
    im.save(destino, "WEBP", quality=82, method=6, alpha_quality=90)
    print(destino, im.size, os.path.getsize(destino) // 1024, "KB")
