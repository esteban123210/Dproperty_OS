---
project: B_RealEstate
title: "Handoff - Compliance Manual (M5)"
type: handoff
deliverable: "Compliance Manual (M5)"
target_output: "Printable book (PDF)"
target_tool: "Markdown-to-PDF book generator or AI document tool"
source_notes: ["05_Franchise_Package/Compliance/Compliance Package.md", "05_Franchise_Package/Localization/Localization Framework.md"]
version: 0.5
status: Ready to generate (DRAFT — needs legal sign-off before publishing)
owner: Esteban
last_updated: 2026-07-21
tags: [handoff, production, compliance, manual, legal]
---

> [!NOTE] Verified against canon 2026-09-23
> **Regenerate before external use.** Handoffs are self-contained snapshots, so this file may still inline pre-reconciliation naming, pricing or product boundaries. Check against canon: BluePrint owns the deal from qualified opportunity · Academy (not Building Blocks) · B_ Partner (not White-Label) · $399/$799 + $1,500 setup · $950k raise · no “one database” or “CRM propio” claims. If a handoff and its source note disagree, **the source note wins**.
>
> Precedence: [[../18_Ecosystem/18 - Canonical Reconciliation and Precedence|Canonical Reconciliation and Precedence]]

# HANDOFF — Compliance Manual (M5)

> **One-file, self-contained package** to generate the final **printable Compliance Manual book (PDF)**. ⚠️ **This is a draft, not legal advice** — the generated book is for internal review until counsel signs off per market. `[local]` marks market-specific values from the market pack.

## 0. Production Brief
- **Deliverable:** Dproperty Compliance Manual — cross-cutting rules for owner (PRIN) and all staff; HQ-owned.
- **Output:** print-ready **PDF book**, ~15–25 pages.
- **Target tool:** Markdown→PDF book generator or AI doc tool.
- **Fidelity goal:** serious, authoritative, clean — reads like a governance document.
- **Audience:** franchisee owner + all staff; referenced by HQ audits.
- **Language:** EN master; ES edition per market `[local]`.

## 1. Design & Brand Direction
- Tone: authoritative and clear (still on-brand, less "marketing"). Restrained use of the accent color.
- Prominent **"Draft — not legal advice"** banner on the cover and page 1 until signed off.
- Layout: cover → legal-status banner → TOC → numbered domains → MUST / MUST NOT pages → breach/incident flow → review cadence. Running header "Dproperty · Compliance Manual"; page numbers.
- Style the MUST / MUST NOT lists as two contrasting boxed panels.

## 2. Assets Required
| Asset | Purpose | Source | Status |
|---|---|---|---|
| Logo | Cover, header | Drive/Brand | need |
| Brand color hex + fonts | Whole book | Brand kit | need |
| Market pack values `[local]` | Resolve legal specifics | [[Localization Framework]] | partial |
| Counsel sign-off block | Approval page | Legal | need |

## 3. Tool Instructions (the prompt)
> "Generate a **print-ready PDF governance manual** from the Markdown in *Section 4*. Requirements: (1) cover with logo, title *Compliance Manual*, and a visible **'DRAFT — not legal advice'** banner; (2) auto TOC; (3) authoritative, highly readable typography per *Section 1*; (4) render tables cleanly; (5) style the **MUST** and **MUST NOT** lists as two contrasting boxed panels; (6) add running headers + page numbers; (7) US-Letter + A4. Do not add or soften any rule. Keep every `[local]` tag visible as a placeholder unless a specific market pack is supplied."

## 4. Final Content (self-contained)

### Cover
**Dproperty — Compliance Manual** · HQ-owned · Version 0.5 · **DRAFT — not legal advice** · Confidential

### Why compliance is a system, not a checklist
Dproperty operates across borders in a regulated industry (real estate, money movement, personal data). A breach can be a licensing, AML, privacy, or franchise-law event — not just brand damage. Compliance protects the client, franchisee, HQ, and network. **The Principal (PRIN) is accountable; every role complies; HQ owns and enforces.**

### How it works
Global core (this manual) + local pack (per-market legal specifics from the Localization Framework). Every franchisee completes **compliance certification** before go-live and **recertifies** on cadence. Incidents route through the OS **Cases** engine; no-blame process issues through **Glitch Report** (never person-attributed).

### Compliance domains
1. **Franchise law & disclosure `[local]`** — some jurisdictions require a disclosure document/registration before a franchise may be *sold*. HQ confirms the regime per market first.
2. **Real-estate licensing `[local]`** — confirm who may legally broker and under whose licence; no unlicensed regulated acts.
3. **AML/KYC & sanctions `[local]`** — client due diligence, source-of-funds where required, sanctions/PEP screening; no deal proceeds without KYC; escalate concerns.
4. **Data privacy & the CRM `[local]`** — lawful basis, marketing consent, data-subject rights, retention, cross-border transfer controls; approved systems only; no exporting client lists.
5. **Advertising, marketing & projections** — **no guaranteed-return claims, ever**; HQ-approved assumptions only; no unapproved/edited materials; obey local advertising/consumer rules `[local]`.
6. **Anti-bribery & developer relationships** — no improper payments/kickbacks; modest gift/hospitality threshold; log anything material.
7. **Fair dealing & anti-discrimination** — serve without unlawful discrimination `[local]`; honest representation; disclose known material facts.
8. **Contracts & document control** — approved templates only; single approved contract version signed by all parties; retain executed documents in approved systems.
9. **Dproperty Select controls** — HQ-controlled; present under rules for the fixed payout `[local]`; no direct developer negotiation, no unapproved projections, no edited materials, no bypassing HQ.
10. **Commission & financial integrity** — respect the three-flow firewall (income ≠ agent payout ≠ HQ royalty); report collected GCI accurately; royalty on gross-into-company; accurate invoicing/tax `[local]`.
11. **Insurance `[local]`** — maintain required cover (professional indemnity / E&O, general liability) at defined minimums before go-live.

### Every franchisee MUST
Register every client/deal and keep it current · complete KYC & sanctions screening before proceeding · use approved materials, templates, and projection assumptions · follow Dproperty Select and commission-reporting rules · hold required licences and insurance · complete and maintain compliance certification.

### Every franchisee MUST NOT
Make guaranteed-return or misleading claims · modify Dproperty Select materials or bypass HQ · hide deals, misreport GCI, or game the royalty base · export or misuse client personal data · pay or accept bribes/kickbacks · operate without required licence/insurance.

### Breaches & incidents
Client/legal/financial issues → OS **Cases** engine (confidential, routed, SLA-bound). No-blame process failures/near-misses → **Glitch Report** (never person-attributed). Serious breaches (AML, privacy, licensing, brand-damaging conduct) → immediate HQ escalation; may trigger agreement remedies.

### Review rhythm
Monthly during first 90 days; quarterly thereafter. Immediate review for any Dproperty Select, AML, or data-privacy issue. Annual recertification + refresh when a market pack or law changes.

### Localization & sign-off
All `[local]` items resolve from the market pack. **No market goes live until its compliance column is complete and signed off by local counsel.** [Counsel sign-off block: market / firm / date / signature.]

## 5. Build & QA Checklist
- [ ] "DRAFT — not legal advice" banner on cover + page 1.
- [ ] TOC + numbered domains render.
- [ ] MUST / MUST NOT panels styled distinctly.
- [ ] All `[local]` tags visible (or resolved for a market edition).
- [ ] Counsel sign-off page included.
- [ ] Content matches source ([[Compliance Package]] M5 v0.5) — no softened rules.
- [ ] US-Letter + A4 exported.

## 6. Source & Change Log
- **Source:** [[Compliance Package]] (M5 v0.5) + [[Localization Framework]].
- **Change log:** 0.5 (2026-07-21) — created from M5 v0.5. *Do not publish externally until legal sign-off.*
