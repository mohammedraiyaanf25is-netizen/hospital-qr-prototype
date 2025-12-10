import csv
import os
import qrcode
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.getcwd()     # <-- safe, works anywhere you run it
OUT_DIR = os.path.join(BASE_DIR, "qr_output")
os.makedirs(OUT_DIR, exist_ok=True)

def make_qr(url, filename):
    qr = qrcode.make(url)
    qr.save(os.path.join(OUT_DIR, filename))
    print("Saved:", filename)

with open("links.csv", newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        label, url = row[0], row[1]
        make_qr(url, f"{label}.png")