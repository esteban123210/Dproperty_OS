# -*- coding: utf-8 -*-
"""Convierte los HTML a PDF usando Edge en modo headless."""
import os, glob, subprocess, pathlib, urllib.parse, sys, time

EDGE = r"C:\Program Files (x86)\Microsoft\EdgeCore\154.0.4258.37\msedge.exe"
BASE = os.path.dirname(os.path.abspath(__file__))
SRC  = os.path.join(BASE, "es")
OUT  = os.path.join(BASE, "pdf")
os.makedirs(OUT, exist_ok=True)

files = sorted(glob.glob(os.path.join(SRC, "*.html")))
print(f"{len(files)} archivos HTML encontrados\n")

ok = 0
for f in files:
    name = os.path.basename(f)[:-5]
    pdf  = os.path.join(OUT, name + ".pdf")
    url  = pathlib.Path(f).as_uri()
    cmd = [EDGE, "--headless=new", "--disable-gpu", "--no-sandbox",
           "--no-first-run", "--no-default-browser-check",
           "--virtual-time-budget=10000",
           "--no-pdf-header-footer",
           f"--print-to-pdf={pdf}", url]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    if os.path.exists(pdf) and os.path.getsize(pdf) > 2000:
        print(f"OK   {name}.pdf  ({os.path.getsize(pdf)//1024} KB)")
        ok += 1
    else:
        print(f"FALLO {name}")
        if r.stderr:
            print("      ", r.stderr.strip().splitlines()[:2])

print(f"\n{ok}/{len(files)} PDFs generados en production/pdf/")
