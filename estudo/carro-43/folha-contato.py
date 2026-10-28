"""Monta folhas de contato das filmagens do carro (estudo/carro-43/_filme). Uso: python -I folha-contato.py [pc|celular]"""
import glob
import json
import os
import sys
from PIL import Image, ImageDraw

AQUI = os.path.dirname(os.path.abspath(__file__))
PASTA = os.path.join(AQUI, "_filme")
tela = sys.argv[1] if len(sys.argv) > 1 else "pc"
for cena in ("A-descendo", "B-subindo-depois-de-sair", "C-subindo-no-meio"):
    dados = json.load(open(os.path.join(PASTA, f"{tela}-{cena}.json"), encoding="utf-8"))
    arqs = sorted(glob.glob(os.path.join(PASTA, f"{tela}-{cena}-*.png")))
    # so quadros em que o carro aparece ou esta perto de aparecer
    idx = [i for i, d in enumerate(dados) if d["vis"]]
    if len(idx) > 14:
        passo = len(idx) / 14
        idx = [idx[int(k * passo)] for k in range(14)]
    cel = []
    for i in idx:
        im = Image.open(arqs[i]).convert("RGB")
        w, h = im.size
        box = (int(w * 0.55), 0, w, h) if tela == "pc" else (int(w * 0.45), 0, w, h)
        im = im.crop(box)
        im.thumbnail((250, 380))
        d = dados[i]
        dr = ImageDraw.Draw(im)
        dr.rectangle((0, 0, im.width, 26), fill=(0, 0, 0))
        dr.text((4, 2), f"{i} {d['estado']} rot{d['rot'].replace('deg','')}", fill=(255, 255, 255))
        dr.text((4, 13), f"top {d['carTop']}{' parado' if d.get('parado') else ''}", fill=(255, 220, 0))
        cel.append(im)
    cols = 7
    lin = (len(cel) + cols - 1) // cols
    cw, ch = cel[0].size
    folha = Image.new("RGB", (cols * cw, lin * ch), (20, 20, 20))
    for k, im in enumerate(cel):
        folha.paste(im, ((k % cols) * cw, (k // cols) * ch))
    destino = os.path.join(PASTA, f"folha-{tela}-{cena}.png")
    folha.save(destino)
    print(destino, len(cel))
