# -*- coding: utf-8 -*-
"""Mide la altura real de cada .page inyectando JS y volcando el DOM."""
import glob, os, re, subprocess, pathlib, tempfile

EDGE = r"C:\Program Files (x86)\Microsoft\EdgeCore\154.0.4258.37\msedge.exe"
PROBE = """<script>window.addEventListener('load',function(){setTimeout(function(){
var o=[];document.querySelectorAll('.page').forEach(function(p,i){
o.push((i+1)+':'+Math.round(p.getBoundingClientRect().height/3.7795));});
var d=document.createElement('div');d.id='MEAS';d.textContent='HEIGHTS='+o.join(',');
document.body.appendChild(d);},1200);});</script>"""
# 1mm = 3.7795px at 96dpi

LIMIT = 257  # mm available per printed page (letter 279.4 - 22mm margins)

for f in sorted(glob.glob("es/*.html")):
    html = open(f, encoding="utf-8").read().replace("</body>", PROBE + "</body>")
    tmp = os.path.join(tempfile.gettempdir(), "m_" + os.path.basename(f))
    open(tmp, "w", encoding="utf-8").write(html)
    r = subprocess.run([EDGE, "--headless=new", "--disable-gpu", "--no-sandbox",
                        "--virtual-time-budget=8000", "--dump-dom",
                        pathlib.Path(tmp).as_uri()],
                       capture_output=True, text=True, timeout=120)
    m = re.search(r"HEIGHTS=([\d:,]+)", r.stdout or "")
    name = os.path.basename(f)[:46]
    if not m:
        print(f"?? {name}"); continue
    parts = [x.split(":") for x in m.group(1).split(",")]
    out = []
    for idx, h in parts:
        h = int(h)
        over = h - LIMIT
        out.append(f"p{idx}={h}mm" + (f" (+{over})" if over > 0 else ""))
    print(f"{name:48s} " + "  ".join(out))
