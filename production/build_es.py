# -*- coding: utf-8 -*-
"""Genera todos los documentos imprimibles en español."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from brand import doc, rebalance
from products_es import P
from products_es2 import P2
from products_es3 import P3
from products_es4 import P4

ALL = {}
ALL.update(P); ALL.update(P2); ALL.update(P3); ALL.update(P4)

OUT = "es"
os.makedirs(OUT, exist_ok=True)

order = ["01_BluePrint", "02_BlankCRM", "03_VAULTED", "04_Building_Blocks",
         "05_Dproperty_Franchise", "06_B_Partner", "07_Developer_Partnerships",
         "08_Dproperty_Select"]

written = []
for i, key in enumerate(order, 1):
    d = ALL[key]
    p1, p2 = rebalance(d["p1"], d["p2"])
    pages = [p1, p2] + ([d["p3"]] if d.get("p3") else [])
    html = doc(f"B_RealEstate — {d['file']}", pages)
    label = {2: "Dos Paginas", 3: "Tres Paginas"}.get(len(pages), f"{len(pages)} Paginas")
    name = f"{i:02d} - B_RealEstate - {d['file']} - {label} - 2026-09-25.html"
    path = os.path.join(OUT, name)
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(html)
    written.append(name)
    print("OK ", name)

# ---- extra documents registered by other modules ----
try:
    from ecosystem_es import ECO
    html = doc("B_RealEstate — Ecosistema", ECO)
    name = "09 - B_RealEstate - Ecosistema - Dos Paginas - 2026-09-24.html"
    with open(os.path.join(OUT, name), "w", encoding="utf-8", newline="") as fh:
        fh.write(html)
    written.append(name); print("OK ", name)
except ImportError:
    print("-- ecosystem_es not yet written")

try:
    from roadmap_es import ROADMAP
    html = doc("B_RealEstate — Ruta de Desarrollo", ROADMAP)
    name = "10 - B_RealEstate - Ruta de Desarrollo - 2026-09-24.html"
    with open(os.path.join(OUT, name), "w", encoding="utf-8", newline="") as fh:
        fh.write(html)
    written.append(name); print("OK ", name)
except ImportError:
    print("-- roadmap_es not yet written")

print(f"\n{len(written)} documentos generados en production/{OUT}/")
