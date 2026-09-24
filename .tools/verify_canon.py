# -*- coding: utf-8 -*-
import io, os, re, glob, collections

ROOT = r"C:\Users\esteb\Desktop\Dproperty_OS\second_brain"
os.chdir(ROOT)

files = sorted(glob.glob("**/*.md", recursive=True))
print("total md files:", len(files))

# ---------------------------------------------------------------- 1. coverage
missing = [f for f in files
           if "Canonical Reconciliation and Precedence" not in io.open(f, encoding="utf-8").read()]
print("\n1. COVERAGE -- files with no precedence reference:", len(missing))
for f in missing:
    print("   ", f)

# ------------------------------------------------------- 2. frontmatter sanity
bad_fm = []
for f in files:
    s = io.open(f, encoding="utf-8").read()
    if s.lstrip().startswith("---"):
        if not s.startswith("---"):
            bad_fm.append((f, "leading whitespace before frontmatter"))
        elif not re.match(r"^---\r?\n.*?\r?\n---\r?\n", s, re.S):
            bad_fm.append((f, "unterminated frontmatter"))
    elif re.search(r"^---\r?\nproject:", s, re.M):
        bad_fm.append((f, "frontmatter is NOT at top of file (breaks YAML)"))
print("\n2. FRONTMATTER -- malformed:", len(bad_fm))
for f, why in bad_fm:
    print("   ", f, "->", why)

# ----------------------------------------------------- 3. banner-before-YAML
banner_first = [f for f in files
                if io.open(f, encoding="utf-8").read().startswith(">")
                and re.search(r"^---\r?\nproject:", io.open(f, encoding="utf-8").read(), re.M)]
print("\n3. banner placed above frontmatter:", len(banner_first))
for f in banner_first:
    print("   ", f)

# --------------------------------------------------------- 4. broken wikilinks
stems = {}
for f in files:
    stems.setdefault(os.path.basename(f)[:-3], []).append(f)
for f in glob.glob("**/*", recursive=True):
    if os.path.isfile(f) and not f.endswith(".md"):
        stems.setdefault(os.path.basename(f), []).append(f)

broken = collections.defaultdict(list)
LINK = re.compile(r"\[\[([^\]\|#]+?)(?:#[^\]\|]*)?(?:\|[^\]]*)?\]\]")
for f in files:
    d = os.path.dirname(f)
    for target in LINK.findall(io.open(f, encoding="utf-8").read()):
        t = target.strip()
        if not t or t.startswith(("http", "$")):
            continue
        base = os.path.basename(t)
        # resolve relative path form
        cand = os.path.normpath(os.path.join(d, t))
        ok = (os.path.exists(cand) or os.path.exists(cand + ".md")
              or base in stems or (base[:-3] if base.endswith(".md") else base) in stems)
        if not ok:
            broken[f].append(t)

nb = sum(len(v) for v in broken.values())
print("\n4. BROKEN WIKILINKS:", nb, "in", len(broken), "files")
for f, ts in sorted(broken.items()):
    print("   ", f)
    for t in sorted(set(ts)):
        print("        ->", t)

# ------------------------------------------------- 5. retired-claim regression
RETIRED = {
 r"\$299\s*/\s*\$599\s*/\s*\$999": "retired BluePrint tiers",
 r"\$650[kK]": "retired funding ask",
 r"\bone database\b|una sola base de datos|misma base de datos": "'one database' claim",
 r"CRM propio": "'CRM propio' claim",
 r"Building Blocks": "legacy product name (needs Academy alias note)",
}
print("\n5. RETIRED CLAIMS still present (excluding files that mark them as retired):")
for pat, label in RETIRED.items():
    hits = []
    for f in files:
        s = io.open(f, encoding="utf-8").read()
        if re.search(pat, s, re.I):
            marked = re.search(r"retired|superseded|legacy|historical|Reconcil|not current|RESOLVED",
                               s, re.I) is not None
            hits.append((f, marked))
    unmarked = [f for f, m in hits if not m]
    print("   {:<50} total {:>3}  unmarked {:>3}".format(label, len(hits), len(unmarked)))
    for f in unmarked:
        print("        !!", f)
print("\nDONE")
