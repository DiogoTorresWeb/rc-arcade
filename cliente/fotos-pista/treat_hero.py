"""
Tratamento de imagem pra hero do RC Arcade — técnica em teste (ver DESIGN-DIRECTION.md,
seção "Tratamento de imagem pra stills"). Parte de foto real do cliente (DSC09861.jpg),
sem gerar nada por IA: só duotone, grain e blur direcional/radial em cima de pixel real.
"""
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

SRC = "DSC09861.jpg"

# Tokens de marca (DESIGN-DIRECTION.md)
RC_BLACK = (10, 11, 13)      # #0A0B0D
RC_RED = (227, 27, 35)       # #E31B23
RC_SILVER = (177, 176, 171)  # #B1B0AB

# Crop 16:9 a partir da foto retrato (4000x5000), enquadrando o carro nítido em primeiro
# plano + o pórtico Red Bull, cortando o excesso de chão vazio embaixo.
CROP_Y_START = 1300
CROP_HEIGHT_RATIO = 9 / 16


def duotone(gray_img: Image.Image, dark: tuple, light: tuple) -> Image.Image:
    lut_r = [int(dark[0] + (light[0] - dark[0]) * i / 255) for i in range(256)]
    lut_g = [int(dark[1] + (light[1] - dark[1]) * i / 255) for i in range(256)]
    lut_b = [int(dark[2] + (light[2] - dark[2]) * i / 255) for i in range(256)]
    r = gray_img.point(lut_r)
    g = gray_img.point(lut_g)
    b = gray_img.point(lut_b)
    return Image.merge("RGB", (r, g, b))


def add_grain(img: Image.Image, amount: float = 10.0) -> Image.Image:
    arr = np.array(img).astype(np.int16)
    noise = np.random.normal(0, amount, arr.shape[:2])[:, :, None]
    arr = np.clip(arr + noise, 0, 255).astype(np.uint8)
    return Image.fromarray(arr)


def radial_speed_blur(img: Image.Image, center: tuple, sharp_radius: int, feather: int) -> Image.Image:
    """Mantém nítido um círculo ao redor do carro em primeiro plano; o resto ganha blur
    direcional (motion blur horizontal, simulando velocidade) crescente até a borda."""
    w, h = img.size
    blurred = img.filter(ImageFilter.GaussianBlur(2))
    # motion blur horizontal: média de cópias deslocadas
    motion = np.array(img).astype(np.float32)
    shifts = [-24, -16, -8, 0, 8, 16, 24]
    acc = np.zeros_like(motion)
    for s in shifts:
        acc += np.roll(motion, s, axis=1)
    acc /= len(shifts)
    motion_img = Image.fromarray(np.clip(acc, 0, 255).astype(np.uint8))

    mask = Image.new("L", (w, h), 0)
    draw = ImageDraw.Draw(mask)
    cx, cy = center
    draw.ellipse(
        [cx - sharp_radius, cy - sharp_radius, cx + sharp_radius, cy + sharp_radius],
        fill=255,
    )
    mask = mask.filter(ImageFilter.GaussianBlur(feather))
    return Image.composite(img, motion_img, mask)


def process(dark, light, out_name, blur_center_ratio=(0.72, 0.70)):
    im = Image.open(SRC).convert("RGB")
    w, h = im.size
    crop_h = int(w * CROP_HEIGHT_RATIO)
    box = (0, CROP_Y_START, w, CROP_Y_START + crop_h)
    im = im.crop(box)
    w, h = im.size

    cx, cy = int(w * blur_center_ratio[0]), int(h * blur_center_ratio[1])
    im = radial_speed_blur(im, (cx, cy), sharp_radius=int(min(w, h) * 0.30), feather=90)

    gray = im.convert("L")
    im = duotone(gray, dark, light)
    im = add_grain(im, amount=9.0)

    # resize pra peso web
    target_w = 1920
    target_h = int(target_w * h / w)
    im = im.resize((target_w, target_h), Image.LANCZOS)
    im.save(out_name, quality=88)
    print(f"saved {out_name} ({target_w}x{target_h})")


if __name__ == "__main__":
    process(RC_BLACK, RC_SILVER, "hero-duotone-preto-prata.jpg")
    process(RC_BLACK, RC_RED, "hero-duotone-preto-vermelho.jpg")
