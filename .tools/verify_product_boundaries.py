"""Regression check for the 2026-09-29 commercial/management architecture decision.

This checks known contradictory claims and canonical acceptance requirements.
It complements human review; it is not a semantic proof of all prose.
Run from any directory: python .tools/verify_product_boundaries.py
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
VAULT = ROOT / "second_brain"
RETIRED = [
    r"BlankCRM owns demand (?:until|up to).*qualification",
    r"BluePrint owns everything after",
    r"BluePrint becomes authoritative at (?:the accepted qualified|the qualified)",
    r"BluePrint owns transaction stage",
    r"BluePrint execution",
    r"transaction execution[^\n]{0,55}(?:→|->)\s*\*?\*?BluePrint",
    r"BluePrint transaction (?:spine|workspace|workflows)",
    r"BluePrint.*tomará el control",
    r"previo a la calificación",
    r"ingreso calificado.*expediente de transacción",
]


def historical(path, text):
    return (
        "98_Archive" in path.parts
        or "Meeting Notes" in path.parts
        or path.name in {"Decision Log.md", "18 - Decision Record - 2026-09-20.md"}
        or "Superseded — historical evidence only" in text[:2000]
    )


errors = []
reviewed = 0
preserved = 0
paths = list(VAULT.rglob("*.md")) + list((ROOT / "production").rglob("*.html")) + list((ROOT / "production").glob("*.py"))
for path in paths:
    text = path.read_text(encoding="utf-8")
    if historical(path, text):
        preserved += 1
        continue
    reviewed += 1
    for pattern in RETIRED:
        for match in re.finditer(pattern, text, re.I):
            line = text.count("\n", 0, match.start()) + 1
            errors.append(f"{path.relative_to(ROOT)}:{line}: retired boundary: {match.group()}")

requirements = {
    "01_Canon/00 - Precedence and Canonical Reconciliation.md": [
        "standalone", "CRM-agnostic", "post-sale", "legal workflow", "expected vs actual cash", "commissions", "does not execute",
    ],
    "02_Offers/02_BlankCRM/01 - Definition and Boundaries.md": [
        "without BluePrint", "legal", "approvals", "contracts", "payment milestones", "closing", "commission", "post-sale", "dashboards",
    ],
    "02_Offers/01_BluePrint/15 - MVP and Validation Plan.md": [
        "BluePrint disconnected", "non-GHL", "expected vs actual cash", "Glitch", "management intervention",
    ],
    "09_Data_and_AI/Data Architecture and Canonical Entities.md": [
        "never BluePrint-owned", "ReconciliationException", "Budget", "Policy", "Glitch", "ManagementDecision",
    ],
}
for rel, phrases in requirements.items():
    text = (VAULT / rel).read_text(encoding="utf-8").lower()
    for phrase in phrases:
        if phrase.lower() not in text:
            errors.append(f"{rel}: missing acceptance concept: {phrase}")

for error in errors:
    print(error)
print(f"{'FAIL' if errors else 'PASS'}: {reviewed} active text files checked; {preserved} historical records excluded; {len(errors)} boundary findings.")
sys.exit(bool(errors))
