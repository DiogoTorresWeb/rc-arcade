"""
Tratamento do hero — v2. Mesma técnica da v1 (duotone + grain + blur radial de
velocidade sobre pixel real, sem gerar nada por IA), mas com enquadramento
parametrizável, porque a v1 deixava dois carros na cena e nenhum centralizado.
"""
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

RC_BLACK = (10, 11, 13)
RC_SILVER = (177, 176, 171)


def duotone(gray, dark, light):
    luts = [[int(dark[c] + (light[c] - dark[c]) * i / 255) for i in range(256)] for c in range(3)]
    return Image.merge("RGB", [gray.point(lut) for lut in luts])


def add_grain(img, amount=9.0):
    arr = np.array(img).astype(np.int16)
    noise = np.random.normal(0, amount, arr.shape[:2])[:, :, None]
    return Image.fromarray(np.clip(arr + noise, 0, 255).astype(np.uint8))


def radial_speed_blur(img, center, sharp_ratio=(0.30, 0.33), feather=120, shift=110):
    """Zona nítida ELÍPTICA (o carro é largo, não redondo) colada no carro; fora dela,
    motion blur horizontal. Duas correções sobre a v1:
    - amostragem de 1 em 1 pixel, senão as cópias aparecem como listras fantasma;
    - borda replicada em vez de `np.roll`, que trazia o lado direito de volta na
      esquerda e sujava a margem."""
    w, h = img.size
    arr = np.array(img).astype(np.float32)
    padded = np.pad(arr, ((0, 0), (shift, shift), (0, 0)), mode="edge")
    acc = np.zeros_like(arr)
    offsets = range(-shift, shift + 1)
    for s in offsets:
        acc += padded[:, shift + s: shift + s + w, :]
    acc /= len(list(offsets))
    motion_img = Image.fromarray(np.clip(acc, 0, 255).astype(np.uint8))

    mask = Image.new("L", (w, h), 0)
    cx, cy = center
    rx, ry = int(w * sharp_ratio[0]), int(h * sharp_ratio[1])
    ImageDraw.Draw(mask).ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(feather))
    return Image.composite(img, motion_img, mask)


def vignette(img, center, strength=0.62, radius=0.78):
    """Escurece a periferia em direção ao preto de marca, centrada no carro. É o que
    faz o segundo veículo (canto superior direito) afundar no fundo em vez de
    competir como sujeito."""
    w, h = img.size
    cx, cy = center[0] * w, center[1] * h
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    d = np.sqrt(((xx - cx) / (w * radius)) ** 2 + ((yy - cy) / (h * radius)) ** 2)
    falloff = np.clip((d - 0.45) / 0.85, 0, 1) ** 1.6
    k = (1.0 - strength * falloff)[:, :, None]
    arr = np.array(img).astype(np.float32)
    base = np.array(RC_BLACK, dtype=np.float32)[None, None, :]
    out = base + (arr - base) * k
    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8))


def build(src, box, blur_center, out, target_w=2560, quality=86, shift=110):
    im = Image.open(src).convert("RGB").crop(box)
    w, h = im.size
    im = radial_speed_blur(im, (int(w * blur_center[0]), int(h * blur_center[1])), shift=shift)
    im = duotone(im.convert("L"), RC_BLACK, RC_SILVER)
    im = vignette(im, blur_center)
    im = add_grain(im)
    im = im.resize((target_w, int(target_w * h / w)), Image.LANCZOS)
    im.save(out, quality=quality, subsampling=0, progressive=True)
    print(f"{out}  {im.size}  origem={src}")


# Enquadramento final: carro #22 do DSC09864 centralizado no eixo horizontal.
# Bbox do carro no original (4000x5000): x[1600,3400] y[2150,3400] -> centro (2500, 2775).
# Corte 16:9 de 3000px de largura centrado nesse x; é a largura máxima possível
# mantendo o carro no meio (2500 + 1500 = 4000, a borda da foto).
BOX_HERO = (1000, 1931, 4000, 3619)
CAR_CENTER = (0.47, 0.54)

if __name__ == "__main__":
    import os, sys
    dest = os.path.join("..", "..", "assets")
    os.makedirs(dest, exist_ok=True)
    if "--preview" in sys.argv:
        build("DSC09864.jpg", BOX_HERO, CAR_CENTER, "cand-final.jpg", 1400, 80)
    else:
        build("DSC09864.jpg", BOX_HERO, CAR_CENTER, os.path.join(dest, "hero-2560.jpg"), 2560, 84)
        build("DSC09864.jpg", BOX_HERO, CAR_CENTER, os.path.join(dest, "hero-1280.jpg"), 1280, 82)
        # LQIP: versão minúscula e borrada pro primeiro paint, embutida como data URI
        build("DSC09864.jpg", BOX_HERO, CAR_CENTER, os.path.join(dest, "hero-lqip.jpg"), 32, 40)
