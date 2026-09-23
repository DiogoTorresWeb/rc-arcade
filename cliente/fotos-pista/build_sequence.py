"""
Protótipo real do canvas image sequence — a partir de vídeo real do cliente
(VID-20260909-WA00791.mp4, WhatsApp, 1024x576). Janela usada: ~39.5-42.5s do
vídeo, onde um carro (liga verde-água/preto, pista "DriftStation") acelera e
passa raspando por uma câmera baixa e fixa no chão — a única sequência de
vários frames consecutivos do material recebido com blur de movimento real.

Frames de origem: C:\\Users\\DIOGOT~1\\AppData\\Local\\Temp\\rc-b\\b_0NN.jpg (25fps nativo)
"""
import glob
import os
from PIL import Image, ImageEnhance, ImageFilter

SRC_DIR = r"C:\Users\DIOGOT~1\AppData\Local\Temp\rc-b"
OUT_DIR = os.path.join(os.path.dirname(__file__), "sequence-launch")
os.makedirs(OUT_DIR, exist_ok=True)

# faixa com o lançamento + passagem (estático antes, sai de quadro depois)
START, END = 52, 76

RC_BLACK = (10, 11, 13)
RC_SILVER = (177, 176, 171)


def duotone(gray_img, dark, light):
    lut_r = [int(dark[0] + (light[0] - dark[0]) * i / 255) for i in range(256)]
    lut_g = [int(dark[1] + (light[1] - dark[1]) * i / 255) for i in range(256)]
    lut_b = [int(dark[2] + (light[2] - dark[2]) * i / 255) for i in range(256)]
    return Image.merge("RGB", (gray_img.point(lut_r), gray_img.point(lut_g), gray_img.point(lut_b)))


count = 0
for i in range(START, END + 1):
    path = os.path.join(SRC_DIR, f"b_{i:03d}.jpg")
    if not os.path.exists(path):
        continue
    im = Image.open(path).convert("RGB")
    w, h = im.size
    # corta a faixa de cima (onde fica o letreiro "DriftStation") — mantém carro + chão
    crop_top = int(h * 0.34)
    im = im.crop((0, crop_top, w, h))
    # nitidez + contraste leve pra compensar a compressão do WhatsApp
    im = im.filter(ImageFilter.UnsharpMask(radius=2, percent=120, threshold=2))
    im = ImageEnhance.Contrast(im).enhance(1.12)
    im = ImageEnhance.Color(im).enhance(0.85)
    count += 1
    im.save(os.path.join(OUT_DIR, f"frame_{count:03d}.jpg"), quality=90)

print(f"{count} frames salvos em {OUT_DIR}")
