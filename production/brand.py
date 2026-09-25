# -*- coding: utf-8 -*-
"""B_RealEstate brand system for print-ready HTML documents.
Palette and typography per 12_Handoffs/CLAUDE DESIGN - Ecosystem Website Design Prompt.md
"""
import re

CSS = """
:root{
  --bone:#F7F4ED; --bone-deep:#EFEAE0; --bone-warm:#FAF8F3;
  --charcoal:#1A1A1A; --soft:#55514C; --champagne:#B89B5E;
  --blue:#1F4E79; --rule:rgba(26,26,26,.25);
}
*{box-sizing:border-box;margin:0;padding:0}
@page{size:letter;margin:11mm 13mm}
html,body{background:var(--bone);color:var(--charcoal);
  font-family:'Inter',system-ui,sans-serif;font-size:9pt;line-height:1.43;
  -webkit-print-color-adjust:exact;print-color-adjust:exact}
.page{width:190mm;min-height:234mm;margin:0 auto;background:var(--bone);
  position:relative;padding-bottom:10mm}
.page+.page{page-break-before:always}

.eyebrow{font-family:'JetBrains Mono',monospace;font-size:7pt;text-transform:uppercase;
  letter-spacing:.09em;color:var(--soft)}
.masthead{display:flex;justify-content:space-between;align-items:flex-start}
.brandmark{font-family:'JetBrains Mono',monospace;font-size:6.8pt;letter-spacing:.09em;
  color:var(--soft);text-align:right;line-height:1.7}
h1{font-family:'Playfair Display',Georgia,serif;font-weight:500;font-size:22pt;
  line-height:1.05;letter-spacing:-.022em;margin:1.5mm 0}
h1.sm{font-size:17pt}
.positioning{font-size:9.4pt;color:var(--soft);max-width:134mm;line-height:1.4}
.hrule{border-top:1.4pt solid var(--charcoal);margin:3mm 0 3.5mm}
.hrule.thin{border-top:.4pt solid var(--rule);margin:3mm 0 4mm}

h2{font-family:'Playfair Display',Georgia,serif;font-weight:500;font-size:11.5pt;
  letter-spacing:-.012em;margin:0 0 1.5mm;break-after:avoid}
.snum{font-family:'JetBrains Mono',monospace;font-size:7pt;letter-spacing:.09em;
  color:var(--champagne);display:block;margin-bottom:.8mm}
h3{font-family:'JetBrains Mono',monospace;font-size:7pt;font-weight:500;
  text-transform:uppercase;letter-spacing:.09em;color:var(--soft);
  margin:0 0 1.5mm;break-after:avoid}
h3.mt{margin-top:2.8mm}
p{margin:0 0 1.8mm}
strong{font-weight:600}
em{font-family:'Playfair Display',serif;font-style:italic}
.small{font-size:8.3pt}
.soft{color:var(--soft)}

.cols{display:grid;grid-template-columns:1fr 62mm;gap:5.5mm;align-items:start}
.cols3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:5mm}
.cols2{display:grid;grid-template-columns:1fr 1fr;gap:6mm}

.panel{background:var(--bone-warm);border-left:2.6pt solid var(--champagne);
  padding:3mm 3.5mm;break-inside:avoid}
.panel.blue{border-left-color:var(--blue)}
.panel.dark{border-left-color:var(--charcoal);background:var(--bone-deep)}
.dl div{display:flex;gap:2.5mm;padding:1mm 0;border-bottom:.4pt solid var(--rule);font-size:7.8pt}
.dl div:last-of-type{border-bottom:none}
.dl dt{font-family:'JetBrains Mono',monospace;font-size:6.5pt;text-transform:uppercase;
  letter-spacing:.07em;color:var(--soft);min-width:16mm;padding-top:.5mm}
.dl dd{flex:1}
.figs{display:grid;grid-template-columns:1fr 1fr;gap:2.2mm;margin-top:3mm;
  padding-top:2.5mm;border-top:.9pt solid var(--charcoal)}
.fig .n{font-family:'Playfair Display',serif;font-weight:500;font-size:13.5pt;
  line-height:1;color:var(--champagne)}
.fig .l{font-family:'JetBrains Mono',monospace;font-size:6pt;text-transform:uppercase;
  letter-spacing:.07em;color:var(--soft);margin-top:1mm;line-height:1.35}

table{width:100%;border-collapse:collapse;font-size:8pt;margin:1.2mm 0 2.2mm;break-inside:avoid}
th{background:var(--bone-deep);font-family:'JetBrains Mono',monospace;font-size:6.5pt;
  font-weight:500;text-transform:uppercase;letter-spacing:.07em;color:var(--soft);
  text-align:left;padding:1.2mm 1.8mm;border-bottom:.9pt solid var(--charcoal)}
td{padding:1mm 1.8mm;border-bottom:.4pt solid var(--rule);vertical-align:top}
tr:nth-child(even) td{background:var(--bone-warm)}
.num{text-align:right;white-space:nowrap}
caption{font-family:'JetBrains Mono',monospace;font-size:6.5pt;text-transform:uppercase;
  letter-spacing:.07em;color:var(--soft);text-align:left;padding-bottom:1.4mm}

.chip{font-family:'JetBrains Mono',monospace;font-size:6.3pt;background:var(--bone-deep);
  color:var(--blue);padding:.3mm 1.1mm;border-radius:1pt;white-space:nowrap;font-weight:500}

.note{font-size:7.6pt;color:var(--soft);border-left:2pt solid var(--rule);
  padding-left:3.5mm;margin:1.5mm 0 2.2mm}
.callout{background:var(--bone-deep);padding:2.2mm 3mm;font-size:8.1pt;margin:1.8mm 0;
  border-left:2.6pt solid var(--charcoal)}
.callout.gold{border-left-color:var(--champagne);background:var(--bone-warm)}

/* SIMPLE-READING BLOCK — the plain-language conclusion */
.simple{background:var(--bone-warm);border:.5pt solid var(--champagne);
  border-left:3.2pt solid var(--champagne);padding:3mm 3.5mm;margin:2.5mm 0;break-inside:avoid}
.simple h3{color:var(--champagne);font-size:7.4pt;margin-bottom:2mm}
.simple p{font-size:8.6pt;margin-bottom:1.5mm}
.simple p:last-child{margin-bottom:0}
.simple ul{list-style:none;font-size:8.6pt}
.simple li{padding-left:3.5mm;position:relative;margin-bottom:1mm}
.simple li::before{content:"→";position:absolute;left:0;color:var(--champagne);font-weight:600}

/* canvas */
.canvas{display:grid;grid-template-columns:repeat(5,1fr);gap:1.2mm;margin-top:1.5mm}
.cell{background:var(--bone-deep);border:.4pt solid var(--rule);padding:2mm 2.2mm;break-inside:avoid}
.cell h4{font-family:'JetBrains Mono',monospace;font-size:6pt;font-weight:500;
  text-transform:uppercase;letter-spacing:.07em;color:var(--soft);margin-bottom:1.4mm}
.cell ul{list-style:none;font-size:6.9pt;line-height:1.35}
.cell li{padding-left:2.5mm;position:relative;margin-bottom:.6mm}
.cell li::before{content:"·";position:absolute;left:.6mm;color:var(--champagne);font-weight:700}
.vp{background:var(--bone-warm);border-left:2.6pt solid var(--champagne);grid-column:3;grid-row:1/span 2}
.vp h4{color:var(--charcoal)}
.kp{grid-column:1;grid-row:1/span 2}
.cseg{grid-column:5;grid-row:1/span 2}
.wide-l{grid-column:1/span 2}
.wide-r{grid-column:3/span 3}

/* timeline / roadmap */
.tl{position:relative;margin:2.5mm 0}
.phase{display:grid;grid-template-columns:20mm 1fr;gap:3mm;padding:2.4mm 0;
  border-top:.5pt solid var(--rule);break-inside:avoid}
.phase:first-child{border-top:1.2pt solid var(--charcoal)}
.phase .when{font-family:'JetBrains Mono',monospace;font-size:6.8pt;text-transform:uppercase;
  letter-spacing:.07em;color:var(--champagne);line-height:1.5;padding-top:.5mm}
.phase .when b{display:block;color:var(--charcoal);font-size:8.5pt;letter-spacing:0;
  font-family:'Playfair Display',serif;font-weight:500;margin-bottom:.8mm}
.phase h4{font-family:'Playfair Display',serif;font-size:9.8pt;font-weight:500;margin-bottom:1mm}
.bar{height:3.4mm;background:var(--bone-deep);display:flex;margin:2mm 0 3mm;border:.4pt solid var(--rule)}
.bar i{display:block;height:100%}
.bar i.on{background:var(--champagne)}
.bar i.next{background:rgba(184,155,94,.35)}
.bar i.later{background:transparent}
.gridnote{display:grid;grid-template-columns:1fr 1fr;gap:4mm;font-size:8.2pt}
.cap{font-family:'JetBrains Mono',monospace;font-size:8pt;color:var(--charcoal);font-weight:500}

.foot{position:absolute;bottom:0;left:0;right:0;border-top:.4pt solid var(--rule);
  padding-top:2mm;display:flex;justify-content:space-between;
  font-family:'JetBrains Mono',monospace;font-size:6pt;letter-spacing:.05em;color:var(--soft)}
.foot span{max-width:152mm;line-height:1.5}
"""

FONTS = ("https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400"
         "&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap")

DISCLAIMER_ES = ("Las cifras marcadas [A] son supuestos sin validar · [M] resultado de modelo · "
                 "[T] objetivo · [R] evidencia pendiente. No constituye una oferta ni una "
                 "solicitud de inversión.")


def doc(title, pages, disclaimer=DISCLAIMER_ES, lang="es"):
    """Wrap page HTML fragments into a complete printable document."""
    body = []
    total = len(pages)
    for i, content in enumerate(pages, 1):
        body.append(
            f'<section class="page">{content}'
            f'<div class="foot"><span>{disclaimer}</span><span>{i} / {total}</span></div>'
            f'</section>'
        )
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<title>{title}</title>
<link href="{FONTS}" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
{''.join(body)}
</body>
</html>"""



def rebalance(p1, p2):
    """Move page 1's 'Como leerlo en simple' block to the end of page 2, and drop
    page 2's redundant one-line version. Keeps exactly one simplified conclusion."""
    blocks = list(re.finditer(r'<div class="simple">.*?</div>\s*(?=<|$)', p1, re.S))
    moved = ""
    if blocks:
        b = blocks[-1]
        moved = b.group(0)
        p1 = p1[:b.start()] + p1[b.end():]
    p2 = re.sub(r'<div class="simple">.*?</div>\s*$', "", p2, flags=re.S)
    return p1, p2 + moved


def masthead(eyebrow, title, positioning=None, meta="B_RealEstate", small=False):
    cls = "sm" if small else ""
    pos = f'<p class="positioning">{positioning}</p>' if positioning else ""
    return (f'<div class="masthead"><div><div class="eyebrow">{eyebrow}</div>'
            f'<h1 class="{cls}">{title}</h1></div>'
            f'<div class="brandmark">{meta}</div></div>{pos}<div class="hrule"></div>')


def simple(items, heading="Cómo leerlo en simple"):
    """The plain-language conclusion block required on every document."""
    if isinstance(items, str):
        inner = f"<p>{items}</p>"
    else:
        inner = "<ul>" + "".join(f"<li>{x}</li>" for x in items) + "</ul>"
    return f'<div class="simple"><h3>{heading}</h3>{inner}</div>'


def table(headers, rows, caption=None, numeric_from=1):
    cap = f"<caption>{caption}</caption>" if caption else ""
    th = "".join(
        f'<th class="num">{h}</th>' if i >= numeric_from and i > 0 else f"<th>{h}</th>"
        for i, h in enumerate(headers))
    tr = ""
    for r in rows:
        tds = "".join(
            f'<td class="num">{c}</td>' if i >= numeric_from and i > 0 else f"<td>{c}</td>"
            for i, c in enumerate(r))
        tr += f"<tr>{tds}</tr>"
    return f"<table>{cap}<thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>"


def glance(rows, figures=None, heading="En resumen"):
    dl = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in rows)
    figs = ""
    if figures:
        figs = '<div class="figs">' + "".join(
            f'<div class="fig"><div class="n">{n}</div><div class="l">{l}</div></div>'
            for n, l in figures) + "</div>"
    return f'<aside class="panel"><h3 style="margin-bottom:2.5mm">{heading}</h3><div class="dl">{dl}</div>{figs}</aside>'


def canvas(blocks):
    """blocks: dict with keys kp, ka, vp, cr, cs, kr, ch, cost, rev — each a list of strings."""
    def cell(key, label, extra=""):
        items = "".join(f"<li>{x}</li>" for x in blocks.get(key, []))
        return f'<div class="cell {extra}"><h4>{label}</h4><ul>{items}</ul></div>'
    return ('<div class="canvas">'
            + cell("kp", "Socios clave", "kp")
            + cell("ka", "Actividades clave")
            + cell("vp", "Propuesta de valor", "vp")
            + cell("cr", "Relación con clientes")
            + cell("cs", "Segmentos de clientes", "cseg")
            + cell("kr", "Recursos clave")
            + cell("ch", "Canales")
            + cell("cost", "Estructura de costos", "wide-l")
            + cell("rev", "Fuentes de ingreso", "wide-r")
            + "</div>")
