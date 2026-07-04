import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

wb = openpyxl.Workbook()

H1 = Font(bold=True, size=14, color="FFFFFF")
H2 = Font(bold=True, size=11, color="FFFFFF")
BOLD = Font(bold=True)
ITAL = Font(italic=True, size=9, color="555555")
fill_dark = PatternFill("solid", fgColor="1F3B4D")
fill_mid = PatternFill("solid", fgColor="2E6E8E")
fill_light = PatternFill("solid", fgColor="D9E6EE")
fill_input = PatternFill("solid", fgColor="FFF6D9")
fill_total = PatternFill("solid", fgColor="EDEDED")
CUR = "#,##0;[Red](#,##0)"
PCT = "0.0%"
thin = Side(style="thin", color="BBBBBB")
border = Border(left=thin, right=thin, top=thin, bottom=thin)

cols = ["C", "D", "E", "F", "G"]
prev = [None, "C", "D", "E", "F"]
yhead = ["Year 1", "Year 2", "Year 3", "Year 4", "Year 5"]

# ================= README =================
ws = wb.active
ws.title = "README"
ws.column_dimensions["A"].width = 4
ws.column_dimensions["B"].width = 100
ws["B1"] = "DPROPERTY OS - FINANCIAL MODEL"
ws["B1"].font = Font(bold=True, size=16)
readme = [
    "",
    "Version: v0.6 (working)   Last built: 2026-07-04   Owner: Esteban",
    "Basis: collected-GCI royalty, 30k/40k staged launch fee, Dproperty Select fixed pct of sale price.",
    "",
    "HOW TO USE",
    "1. Edit only the yellow cells on 'Assumptions' and the yellow cost rows on 'Model'.",
    "2. Everything else on 'Model' is a live formula and recalculates when you open in Excel.",
    "3. Blue rows = section headers. Grey rows = totals.",
    "",
    "WHAT THIS MODEL IS / IS NOT",
    "- A transparent, adjustable operating model for the conservative 5-year plan (5 branded / 20 white-label / 15 developer).",
    "- NOT audited. Cost lines are planning estimates. Confirm with owners before pitch-final use.",
    "",
    "KEY LEVERS (Assumptions sheet)",
    "- local_comm_rate: set to 0.0075 to run the 0.75pct deferred-advisory sensitivity.",
    "- select_mix / local_mix: share of a franchise's volume that is Dproperty Select vs local.",
    "- ramp row (Model row 12): how fast new franchises reach full productivity.",
    "- dev_rev_per_project: conservative 40k blended assumption.",
    "",
    "OPEN VALIDATION ITEMS (mirror Business Plan Section 19)",
    "1. Commission rate 5pct vs 0.75pct (Fernando/Ernesto) - BLOCKS everything.",
    "2. Miguel salary amount (EUR 3,000/mo placeholder).",
    "3. Sales mix 70/30, ramp curve, developer per project.",
    "4. Minimum royalty floor amount (750/mo placeholder).",
    "5. Whether franchisee pays royalty on Dproperty Select earnings (default: no).",
]
r = 2
for line in readme:
    ws.cell(row=r, column=2, value=line)
    if line.isupper() and line.strip():
        ws.cell(row=r, column=2).font = BOLD
    r += 1

# ================= ASSUMPTIONS =================
wa = wb.create_sheet("Assumptions")
wa.column_dimensions["A"].width = 4
wa.column_dimensions["B"].width = 42
wa.column_dimensions["C"].width = 16
wa.column_dimensions["D"].width = 50
wa["B1"] = "ASSUMPTIONS - edit the yellow cells"
wa["B1"].font = H1
wa["B1"].fill = fill_dark
wa["C1"].fill = fill_dark
wa["D1"].fill = fill_dark

labels_order = [
    ("unit_price", "Unit price (USD)", 300000, CUR, "Average unit price", True),
    ("local_comm", "Local commission rate", 0.05, PCT, "Set 0.0075 to test the 0.75pct case", True),
    ("royalty", "Royalty rate", 0.06, PCT, "On collected local GCI", True),
    ("fund", "Network & Brand Fund", 0.015, PCT, "On collected local GCI", True),
    ("total_local", "Total local take", "=C5+C6", PCT, "Royalty + Fund", False),
    ("fee_found", "Launch fee - founding", 30000, CUR, "First 5 franchises", True),
    ("fee_mature", "Launch fee - mature", 40000, CUR, "After 5 successful franchises", True),
    ("os_month", "OS fee / month", 1000, CUR, "Per franchise", True),
    ("floor_month", "Min royalty floor / month", 750, CUR, "From month 7 (placeholder)", True),
    ("select_comm", "Dproperty Select commission (model)", 0.05, PCT, "Model at 5pct; upside kept by HQ", True),
    ("sel_branded", "Select payout - branded", 0.025, PCT, "pct of sale price to franchisee", True),
    ("sel_wl", "Select payout - white-label", 0.02, PCT, "pct of sale price to partner", True),
    ("units_fr", "Units per franchise / year", 50, "#,##0", "Full-productivity assumption", True),
    ("local_mix", "Local sales mix", 0.70, PCT, "Share of units that are local", True),
    ("select_mix", "Dproperty Select mix", 0.30, PCT, "Share of units that are Select", True),
    ("wl_setup", "White-label setup (avg)", 12000, CUR, "Blend of starter/growth", True),
    ("wl_month", "White-label monthly (avg)", 1800, CUR, "Blend of starter/growth", True),
    ("ghl_margin", "GHL resale margin / month", 100, CUR, "Per active account (placeholder)", True),
    ("dev_rev", "Developer revenue / project", 40000, CUR, "Conservative blended", True),
    ("eur_usd", "EUR to USD", 1.08, "0.00", "FX for salaries", True),
    ("gci_unit", "GCI per unit", "=C3*C4", CUR, "Price x commission", False),
    ("sel_hq_br", "Select HQ retained - branded", "=C3*C4-C3*C13", CUR, "Commission minus branded payout", False),
    ("sel_hq_wl", "Select HQ retained - white-label", "=C3*C4-C3*C14", CUR, "Commission minus WL payout", False),
]
r = 3
addr = {}
for key, label, val, fmt, note, is_in in labels_order:
    wa.cell(row=r, column=2, value=label)
    c = wa.cell(row=r, column=3, value=val)
    c.number_format = fmt
    c.border = border
    if is_in:
        c.fill = fill_input
    else:
        c.fill = fill_total
        c.font = BOLD
    wa.cell(row=r, column=4, value=note).font = ITAL
    addr[key] = f"$C${r}"
    r += 1

# ================= MODEL =================
wm = wb.create_sheet("Model")
wm.column_dimensions["A"].width = 4
wm.column_dimensions["B"].width = 42
for cl in cols:
    wm.column_dimensions[cl].width = 15


def setrow(row, label, values=None, formula_fn=None, fmt=CUR, bold=False,
           section=False, total=False, note=False, inputrow=False):
    cell = wm.cell(row=row, column=2, value=label)
    if section:
        cell.font = H2
        cell.fill = fill_mid
        for cl in cols:
            wm[f"{cl}{row}"].fill = fill_mid
        return
    if bold or total:
        cell.font = BOLD
    if note:
        cell.font = ITAL
    for i, cl in enumerate(cols):
        c = wm[f"{cl}{row}"]
        if formula_fn is not None:
            c.value = formula_fn(cl, prev[i], i)
        elif values is not None:
            c.value = values[i]
        c.number_format = fmt
        if total:
            c.fill = fill_total
            c.font = BOLD
        if inputrow:
            c.fill = fill_input
        c.border = border


wm["B1"] = "DPROPERTY OS - FINANCIAL MODEL v0.6 (blue=headers, grey=totals, yellow=editable)"
wm["B1"].font = H1
wm["B1"].fill = fill_dark
for cl in cols:
    wm[f"{cl}1"].fill = fill_dark
wm.cell(row=3, column=2, value="Line").font = BOLD
for i, cl in enumerate(cols):
    c = wm[f"{cl}3"]
    c.value = yhead[i]
    c.font = BOLD
    c.fill = fill_light
    c.alignment = Alignment(horizontal="center")

setrow(4, "COUNTS", section=True)
setrow(5, "Branded franchises (EOY)", values=[0, 1, 2, 3, 5], fmt="#,##0", inputrow=True)
setrow(6, "Branded - new this year",
       formula_fn=lambda cl, pv, i: (f"={cl}5" if pv is None else f"={cl}5-{pv}5"), fmt="#,##0")
setrow(7, "Branded - active (avg)",
       formula_fn=lambda cl, pv, i: (f"=(0+{cl}5)/2" if pv is None else f"=({pv}5+{cl}5)/2"), fmt="0.0")
setrow(8, "White-label (EOY)", values=[2, 5, 10, 15, 20], fmt="#,##0", inputrow=True)
setrow(9, "White-label - new this year",
       formula_fn=lambda cl, pv, i: (f"={cl}8" if pv is None else f"={cl}8-{pv}8"), fmt="#,##0")
setrow(10, "White-label - active (avg)",
       formula_fn=lambda cl, pv, i: (f"=(0+{cl}8)/2" if pv is None else f"=({pv}8+{cl}8)/2"), fmt="0.0")
setrow(11, "Developer projects / year", values=[1, 3, 6, 10, 15], fmt="#,##0", inputrow=True)
setrow(12, "Ramp factor (0-1)", values=[0.5, 0.6, 0.7, 0.75, 0.8], fmt="0.00", inputrow=True)

A_ = "Assumptions!"
setrow(14, "REVENUE (USD)", section=True)
setrow(15, "Franchise launch fees",
       formula_fn=lambda cl, pv, i: f"={cl}6*{A_}{addr['fee_found']}")
setrow(16, "Franchise OS fees",
       formula_fn=lambda cl, pv, i: f"={cl}7*{A_}{addr['os_month']}*12")
setrow(17, "Local royalty + Network & Brand Fund (collected)",
       formula_fn=lambda cl, pv, i: f"={cl}7*{A_}{addr['units_fr']}*{A_}{addr['local_mix']}*{A_}{addr['gci_unit']}*{A_}{addr['total_local']}*{cl}12")
setrow(18, "Dproperty Select - HQ retained",
       formula_fn=lambda cl, pv, i: f"={cl}7*{A_}{addr['units_fr']}*{A_}{addr['select_mix']}*{A_}{addr['sel_hq_br']}*{cl}12")
setrow(19, "White-label setup fees",
       formula_fn=lambda cl, pv, i: f"={cl}9*{A_}{addr['wl_setup']}")
setrow(20, "White-label recurring",
       formula_fn=lambda cl, pv, i: f"={cl}10*{A_}{addr['wl_month']}*12")
setrow(21, "GoHighLevel resale margin",
       formula_fn=lambda cl, pv, i: f"=({cl}7+{cl}10)*{A_}{addr['ghl_margin']}*12")
setrow(22, "Developer Sales OS",
       formula_fn=lambda cl, pv, i: f"={cl}11*{A_}{addr['dev_rev']}")
setrow(23, "TOTAL REVENUE",
       formula_fn=lambda cl, pv, i: f"=SUM({cl}15:{cl}22)", total=True)

setrow(25, "OPERATING COSTS (USD) - editable planning estimates", section=True)
setrow(26, "Salaries (founders + team)", values=[150000, 220000, 300000, 400000, 500000], inputrow=True)
setrow(27, "Product / technology", values=[80000, 70000, 80000, 90000, 100000], inputrow=True)
setrow(28, "Legal / compliance", values=[60000, 40000, 40000, 40000, 40000], inputrow=True)
setrow(29, "Training / content", values=[40000, 30000, 30000, 35000, 40000], inputrow=True)
setrow(30, "Customer success / implementation", values=[30000, 50000, 70000, 90000, 110000], inputrow=True)
setrow(31, "Sales / BD / travel", values=[40000, 50000, 60000, 70000, 80000], inputrow=True)
setrow(32, "Hosting / tools / admin", values=[30000, 35000, 45000, 55000, 65000], inputrow=True)
setrow(33, "Contingency", values=[15000, 15000, 20000, 25000, 30000], inputrow=True)
setrow(34, "TOTAL OPEX",
       formula_fn=lambda cl, pv, i: f"=SUM({cl}26:{cl}33)", total=True)

setrow(36, "EBITDA",
       formula_fn=lambda cl, pv, i: f"={cl}23-{cl}34", total=True)
setrow(37, "EBITDA margin",
       formula_fn=lambda cl, pv, i: f"=IFERROR({cl}36/{cl}23,0)", fmt=PCT, total=True)

wm.cell(row=39, column=2, value="Founder salary ref: Esteban EUR 4,000/mo (Y1) -> 5,500 (Tranche 2); Miguel EUR 3,000/mo placeholder. Inside 'Salaries'.").font = ITAL
wm.cell(row=40, column=2, value="At 5pct Select commission, branded HQ-retained = franchisee payout = 7,500 per 300k unit. Above 5pct, HQ keeps the upside.").font = ITAL

wb.save("second_brain/09_Exports/Dproperty_OS_Financial_Model.xlsx")
print("SAVED workbook.")

# ---- Parallel Python calc to print projected P&L ----
unit = 300000; comm = 0.05; roy = 0.06; fund = 0.015; tl = roy + fund
fee = 30000; osm = 1000; units = 50; lmix = 0.70; smix = 0.30
selhq = unit * comm - unit * 0.025
wl_setup = 12000; wl_m = 1800; ghl = 100; dev = 40000
gci = unit * comm
beoy = [0, 1, 2, 3, 5]; weoy = [2, 5, 10, 15, 20]; dproj = [1, 3, 6, 10, 15]
ramp = [0.5, 0.6, 0.7, 0.75, 0.8]
bprev = [0] + beoy[:-1]; wprev = [0] + weoy[:-1]
bnew = [beoy[i] - bprev[i] for i in range(5)]; wnew = [weoy[i] - wprev[i] for i in range(5)]
bavg = [(bprev[i] + beoy[i]) / 2 for i in range(5)]; wavg = [(wprev[i] + weoy[i]) / 2 for i in range(5)]
opex = [[150000, 220000, 300000, 400000, 500000], [80000, 70000, 80000, 90000, 100000],
        [60000, 40000, 40000, 40000, 40000], [40000, 30000, 30000, 35000, 40000],
        [30000, 50000, 70000, 90000, 110000], [40000, 50000, 60000, 70000, 80000],
        [30000, 35000, 45000, 55000, 65000], [15000, 15000, 20000, 25000, 30000]]
launch = [bnew[i] * fee for i in range(5)]
osf = [bavg[i] * osm * 12 for i in range(5)]
locr = [bavg[i] * units * lmix * gci * tl * ramp[i] for i in range(5)]
sel = [bavg[i] * units * smix * selhq * ramp[i] for i in range(5)]
wls = [wnew[i] * wl_setup for i in range(5)]
wlm = [wavg[i] * wl_m * 12 for i in range(5)]
ghlm = [(bavg[i] + wavg[i]) * ghl * 12 for i in range(5)]
devr = [dproj[i] * dev for i in range(5)]
rev = [launch[i] + osf[i] + locr[i] + sel[i] + wls[i] + wlm[i] + ghlm[i] + devr[i] for i in range(5)]
totopex = [sum(opex[j][i] for j in range(8)) for i in range(5)]
ebitda = [rev[i] - totopex[i] for i in range(5)]


def line(name, vals):
    print(f"{name:40}", *[f"{v:12,.0f}" for v in vals])


print(f"{'Line':40}", *[f"{'Y'+str(i+1):>12}" for i in range(5)])
line("Launch fees", launch)
line("OS fees", osf)
line("Local royalty+fund", locr)
line("Dproperty Select (HQ)", sel)
line("WL setup", wls)
line("WL recurring", wlm)
line("GHL margin", ghlm)
line("Developer", devr)
line("TOTAL REVENUE", rev)
line("TOTAL OPEX", totopex)
line("EBITDA", ebitda)
