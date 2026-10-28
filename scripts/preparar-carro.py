"""Receita do carro 43 visto de cima (o 'carro que desce' de Cómo trabajamos).
Origem: estudo/carro-43/carro-43-recorte.png (gerado por estudo/carro-43/recortar-carro.py a partir de
ia-43-original.png, imagem feita por IA a partir das fotos reais DSC09882 e DSC09884 do carro nº 43).
Saida: assets/fotos/carro-43-280.webp e carro-43-488.webp (com transparencia).
Rodar: python -I scripts/preparar-carro.py"""
import os
from PIL import Image

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = Image.open(os.path.join(RAIZ, "estudo", "carro-43", "carro-43-recorte.png")).convert("RGBA")
print("origem", src.size)
for largura in (280, 488):
    alt = round(src.height * largura / src.width)
    im = src if largura >= src.width else src.resize((largura, alt), Image.LANCZOS)
    destino = os.path.join(RAIZ, "assets", "fotos", f"carro-43-{largura}.webp")
    im.save(destino, "WEBP", quality=82, method=6, alpha_quality=90)
    print(destino, im.size, os.path.getsize(destino) // 1024, "KB")
