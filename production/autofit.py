# -*- coding: utf-8 -*-
"""Mide cada pagina y aplica un zoom por pagina para que quepa exactamente."""
import glob, os, re, subprocess, pathlib, tempfile, sys

EDGE = r"C:\Program Files (x86)\Microsoft\EdgeCore\154.0.4258.37\msedge.exe"
LIMIT = 255.0     # mm utiles por pagina impresa
FLOOR = 0.85      # no reducir mas alla de esto (legibilidad)

PROBE = """<script>window.addEventListener('load',function(){setTimeout(function(){
var o=[];document.querySelectorAll('.page').forEach(function(p,i){
o.push(Math.round(p.getBoundingClientRect().height/3.7795));});
var d=document.createElement('div');d.id='MEAS';d.textContent='H='+o.join(',');
document.body.appendChild(d);},1500);});</script>"""

def heights(path):
    html = open(path, encoding="utf-8").read()
    html = re.sub(r'<section class="page"[^>]*>', '<section class="page">', html)
    html = html.replace("</body>", PROBE + "</body>")
    tmp = os.path.join(tempfile.gettempdir(), "af_" + os.path.basename(path))
    open(tmp, "w", encoding="utf-8").write(html)
    r = subprocess.run([EDGE, "--headless=new", "--disable-gpu", "--no-sandbox",
                        "--virtual-time-budget=9000", "--dump-dom",
                        pathlib.Path(tmp).as_uri()],
                       capture_output=True, text=True, encoding="utf-8",
                       errors="replace", timeout=150)
    m = re.search(r"H=([\d,]+)", r.stdout or "")
    return [int(x) for x in m.group(1).split(",")] if m else None

problems = []
for f in sorted(glob.glob("es/*.html")):
    hs = heights(f)
    name = os.path.basename(f)[:44]
    if not hs:
        print(f"?? no medido  {name}"); continue
    html = open(f, encoding="utf-8").read()
    html = re.sub(r'<section class="page"[^>]*>', '<section class="page">', html)
    parts = html.split('<section class="page">')
    out, zooms = [parts[0]], []
    for i, seg in enumerate(parts[1:]):
        h = hs[i] if i < len(hs) else 0
        z = 1.0 if h <= LIMIT else round(LIMIT / h, 3)
        if z < FLOOR:
            problems.append((name, i + 1, h, z)); z = FLOOR
        zooms.append(z)
        tag = '<section class="page">' if z == 1.0 else f'<section class="page" style="zoom:{z}">'
        out.append(tag + seg)
    open(f, "w", encoding="utf-8", newline="").write("".join(out))
    print(f"{name:46s} " + "  ".join(f"p{i+1}:{h}mm z={z}" for i, (h, z) in enumerate(zip(hs, zooms))))

if problems:
    print("\n!! Paginas con demasiado contenido (necesitan dividirse, no reducirse):")
    for n, p, h, z in problems:
        print(f"   {n} pagina {p}: {h}mm requiere zoom {z}")
