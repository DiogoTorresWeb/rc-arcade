"""Recorta o carro 43 (ia-43-original.png) do fundo cinza e gera previa sobre preto.
Rodar: python -I recortar-carro.py"""
import os
import numpy as np
from PIL import Image
from scipy import ndimage as ndi
from skimage import color, morphology

AQUI = os.path.dirname(os.path.abspath(__file__))
im = Image.open(os.path.join(AQUI, "ia-43-original.png")).convert("RGB")
rgb = np.asarray(im).astype(np.float32) / 255
lab = color.rgb2lab(rgb)
h, w = lab.shape[:2]

# cor do fundo: mediana das bordas; o fundo tem leve degrade, entao uso o fundo suavizado por regiao
borda = np.concatenate([lab[:12].reshape(-1, 3), lab[-12:].reshape(-1, 3),
                        lab[:, :12].reshape(-1, 3), lab[:, -12:].reshape(-1, 3)])
bg = np.median(borda, axis=0)
dist = np.linalg.norm(lab - bg, axis=2)
print("fundo Lab", bg, "dist p5/p50", np.percentile(dist, [5, 50]))

# Segmentacao por bacia (watershed) sobre o gradiente: o fundo tem sombra suave que chega perto do branco do
# carro (paralama branco em sombra ~ mesma luminosidade do fundo), entao limiar de cor nao basta.
# Marcadores seguros: carro = escuro, colorido ou mais claro que o fundo; fundo = liso, neutro, ligado a borda.
from skimage import filters, segmentation
L = lab[..., 0]
croma = np.hypot(lab[..., 1], lab[..., 2])
Ls = filters.gaussian(L, 1.0)
grad = filters.sobel(Ls) + 0.5 * filters.sobel(filters.gaussian(croma, 1.0))
carro_certo = (L < 70) | (croma > 12) | (L > bg[0] + 3.0)
carro_certo = ndi.binary_erosion(carro_certo, iterations=2)
fundo_liso = (L > 70) & (L < bg[0] + 3.0) & (croma < 5) & (grad < 0.6)
rot, n = ndi.label(fundo_liso)
ids = set(np.unique(np.concatenate([rot[0], rot[-1], rot[:, 0], rot[:, -1]]))) - {0}
fundo_certo = ndi.binary_erosion(np.isin(rot, list(ids)), iterations=3)
marc = np.zeros(L.shape, np.int32)
marc[fundo_certo] = 1
marc[carro_certo] = 2
seg = segmentation.watershed(grad, marc)
carro = seg == 2
rot2, n2 = ndi.label(carro)
tam = ndi.sum(carro, rot2, range(1, n2 + 1))
carro = rot2 == (1 + int(np.argmax(tam)))
carro = ndi.binary_fill_holes(carro)
carro = ndi.binary_opening(carro, structure=morphology.disk(2))
# o contorno do carro e liso: fecha as mordidas deixadas pelo branco em sombra e alisa a borda
pad = 40
cp = np.pad(carro, pad)
cp = ndi.binary_closing(cp, structure=morphology.disk(26))
cp = ndi.binary_fill_holes(cp)
cp = ndi.binary_opening(cp, structure=morphology.disk(6))
carro = cp[pad:-pad, pad:-pad]

# borda suave: 1 px de desfoque no alfa
alfa = ndi.gaussian_filter(carro.astype(np.float32), 1.0)
rgba = np.dstack([np.asarray(im), (alfa * 255).astype(np.uint8)])
out = Image.fromarray(rgba, "RGBA")
ys, xs = np.where(carro)
box = (max(xs.min() - 6, 0), max(ys.min() - 6, 0), min(xs.max() + 7, w), min(ys.max() + 7, h))
out = out.crop(box)
out.save(os.path.join(AQUI, "carro-43-recorte.png"))
print("recorte", out.size, "caixa", box)

for nome, cor in (("preto", (10, 11, 13)), ("magenta", (255, 0, 255))):
    base = Image.new("RGBA", out.size, cor + (255,))
    base.alpha_composite(out)
    base.convert("RGB").save(os.path.join(AQUI, f"_previa-{nome}.png"))
