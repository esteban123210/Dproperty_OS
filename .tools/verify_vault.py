# -*- coding: utf-8 -*-
"""Vault integrity check: broken wikilinks, stale paths, retired vocabulary, README coverage."""
import os, re, sys, posixpath, collections
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BS = chr(92)
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "second_brain"))

files = {}
for r, d, f in os.walk(ROOT):
    if ".obsidian" in r or ".claudian" in r:
        continue
    for x in f:
        p = os.path.relpath(os.path.join(r, x), ROOT).replace(BS, "/")
        files[p] = os.path.join(r, x)

md = {p: v for p, v in files.items() if p.endswith(".md")}
stems = collections.defaultdict(list)
for p in md:
    stems[posixpath.basename(p)[:-3]].append(p)

WIKI = re.compile(r"\[\[([^\]\|#]+)(?:#[^\]\|]*)?(?:\|([^\]]*))?\]\]")

OLD_FOLDERS = ["00_Index/", "01_Strategy/", "02_Business_Plan/", "03_Pitch/", "04_Product/",
               "05_Franchise_Package/", "06_Legal/", "07_Finance/", "08_Research/", "09_Exports/",
               "10_Templates/", "11_Developer_Sales_OS/", "12_Private_Collection/", "13_White_Label/",
               "14_CRM_GoHighLevel/", "15_Brand_Assets_Index/", "16_Task_Management/",
               "17_Handoff_Files/", "18_Ecosystem/", "19_Canonical_B_RealEstate/"]

FUNDING_CTX = r"seed|ask|raise|fund|budget|tranche|capital|investor|ROI|return|equity|proceeds|cash need"

RETIRED = {
    r"\$299\s*/\s*\$599\s*/\s*\$999": "retired BluePrint tiers",
    r"\$650k": "retired funding ask",
    r"one shared database|una sola base de datos": "forbidden claim",
    r"CRM propio": "forbidden claim",
}

# A prohibition ("never claim X", "do not say X") is correct usage, not a violation.
PROHIBITION = re.compile(
    r"(never|avoid|do not|don't|remove|replace|reemplaz|prohibit|forbidden|incorrect|calls it)"
    r"[^\n]{0,80}$", re.I)

broken = []
stale = []
retired_hits = []

for p, full in sorted(md.items()):
    cur = posixpath.dirname(p)
    txt = open(full, encoding="utf-8", errors="replace").read()

    # ---- wikilinks
    for m in WIKI.finditer(txt):
        t = m.group(1).strip().rstrip(BS)   # tables escape the alias pipe as \|
        if not t or t.startswith(("http://", "https://", "mailto:")):
            continue
        cands = [t] if "." in posixpath.basename(t) else []
        cands.append(t + ".md")
        resolved = False
        # relative / absolute path
        for cand in cands:
            for base in ([cur] if cur else []) + [""]:
                probe = posixpath.normpath(posixpath.join(base, cand)) if base else posixpath.normpath(cand)
                if probe in md or probe in files:
                    resolved = True
                    break
            if resolved:
                break
        # bare stem
        if not resolved and posixpath.basename(t) == t and t in stems:
            resolved = True
        if not resolved:
            broken.append((p, t))

    # ---- stale folder paths (ignore the two notes that document history)
    if posixpath.basename(p) not in ("Vault Architecture Map.md", "verify_vault.py"):
        for old in OLD_FOLDERS:
            for mm in re.finditer(re.escape(old), txt):
                # allow when clearly marked historical on the same line
                line_start = txt.rfind("\n", 0, mm.start()) + 1
                line_end = txt.find("\n", mm.end())
                line = txt[line_start: line_end if line_end != -1 else len(txt)]
                if re.search(r"old |former|legacy|was |history|historical|superseded|no longer|dissolved|→|->", line, re.I):
                    continue
                stale.append((p, old, line.strip()[:100]))

    # ---- retired vocabulary (98_Archive is evidence by design; banners mark known-stale live notes)
    if p.startswith("98_Archive/") or "Stale figures" in txt or "Do not produce from this file yet" in txt:
        continue
    for pat, label in RETIRED.items():
        for mm in re.finditer(pat, txt, re.I):
            line_start = txt.rfind("\n", 0, mm.start()) + 1
            line_end = txt.find("\n", mm.end())
            line = txt[line_start: line_end if line_end != -1 else len(txt)]
            before = line[: mm.start() - line_start]
            if PROHIBITION.search(before):
                continue
            # $650k is only a problem in a funding/return context, not as a random cost figure
            if label == "retired funding ask" and not re.search(FUNDING_CTX, line, re.I):
                continue
            ctx = txt[max(0, mm.start()-400): mm.end()+200]
            if re.search(r"retired|never use|forbidden|do not use|don't use|superseded|not current|no longer|legacy|instead of|replaced|historical|was |RESOLVED|Reason:|reconcil", ctx, re.I):
                continue
            retired_hits.append((p, label, line.strip()[:100]))

# ---- README coverage
dirs = sorted({posixpath.dirname(p) for p in md if posixpath.dirname(p)})
missing_readme = []
for d in dirs:
    if d.startswith("98_Archive") and d != "98_Archive":
        continue
    if d.endswith("Meeting Notes") or d.endswith("AI Handoff Pack") or d.endswith("Source Material") or d.endswith("Model Data"):
        continue
    has = (d + "/README.md") in md or (d + "/00 - README.md") in md
    if not has:
        missing_readme.append(d)

def section(name, items, fmt):
    print("\n" + "=" * 70)
    print(f"{name}: {len(items)}")
    print("=" * 70)
    for it in items[:200]:
        print("  " + fmt(it))
    if len(items) > 200:
        print(f"  ... and {len(items)-200} more")

print(f"markdown files: {len(md)}")
section("BROKEN WIKILINKS", broken, lambda i: f"{i[0]}  ->  [[{i[1]}]]")
section("STALE OLD-FOLDER PATHS", stale, lambda i: f"{i[0]}  ({i[1]})  {i[2]}")
section("RETIRED VOCABULARY", retired_hits, lambda i: f"{i[0]}  [{i[1]}]  {i[2]}")
section("FOLDERS MISSING README", missing_readme, lambda i: i)

total = len(broken) + len(stale) + len(retired_hits) + len(missing_readme)
print("\n" + ("PASS - vault is coherent" if total == 0 else f"ISSUES: {total}"))
sys.exit(0 if total == 0 else 1)
