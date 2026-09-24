---
project: B_RealEstate
title: "Handoff - Financial Model"
type: handoff
deliverable: "Financial Model (Phase 1 franchise)"
target_output: "Spreadsheet (.xlsx / Google Sheets)"
target_tool: "Excel / Google Sheets (or an AI that builds formula-driven models)"
source_notes: ["07_Finance/Financial Model Summary.md", "00_Index/Decision Log.md (waterfall, pricing)", "03_Pitch/Pitch Deck Outline.md (S14–S15)"]
version: 0.7
status: Model exists (v0.7); handoff documents its logic for rebuild/extension. Phase-2 NOT built.
owner: Esteban
last_updated: 2026-07-21
tags: [handoff, production, finance, model]
---

> [!NOTE] Verified against canon 2026-09-23
> **Regenerate before external use.** Handoffs are self-contained snapshots, so this file may still inline pre-reconciliation naming, pricing or product boundaries. Check against canon: BluePrint owns the deal from qualified opportunity · Academy (not Building Blocks) · B_ Partner (not White-Label) · $399/$799 + $1,500 setup · $950k raise · no “one database” or “CRM propio” claims. If a handoff and its source note disagree, **the source note wins**.
>
> Precedence: [[../18_Ecosystem/18 - Canonical Reconciliation and Precedence|Canonical Reconciliation and Precedence]]

# HANDOFF — Financial Model (Phase 1)

> **Self-contained package** to (re)build or extend the **Phase-1 franchise financial model** as a formula-driven spreadsheet. The current source of truth is `09_Exports/Dproperty_OS_Financial_Model.xlsx v0.7`; this handoff documents its **logic, inputs, and outputs** so it can be regenerated, audited, or extended. Currency **USD**. ⚠️ OPEX/staffing rows need owner validation; a **Phase-2 (ecosystem) model does not exist yet.**

## 0. Production Brief
- **Deliverable:** conservative 5-year Phase-1 P&L for the franchise venture (HQ view).
- **Output:** **.xlsx / Google Sheets**, formula-driven, with an Assumptions tab that drives everything.
- **Target tool:** Excel/Sheets, or an AI that builds linked-formula models.
- **Fidelity goal:** every output cell traceable to an assumption; no hardcoded results.

## 1. Design & Structure
- Tabs: **README/Assumptions · Local Unit Economics · Dproperty Select · Franchise Fees · White-Label · Developer · 5-Year P&L · Charts.**
- Convention: inputs in one color, formulas locked; no magic numbers in P&L.

## 2. Inputs Required (Assumptions tab)
| Input | Value / status |
|---|---|
| Avg unit price | $300,000 (editable) |
| Local sale commission | 5% `[local-market variable]` |
| External co-broke split | 50/50 (editable input) |
| Internal split of into-company | seller 35% / director 10% / franchise net 55% |
| Royalty + Network & Brand Fund | 6% + 1.5% = **7.5% on collected GCI (gross-into-company)** |
| OS/platform fee | $1,000/month |
| Min royalty floor | $500/month, creditable, from month 7 |
| Launch fee | $30,000 → $40,000 after 5 successful franchises |
| Dproperty Select payout | 2.5% branded / 1.5% white-label of sale price (external-partner-broker terms, revised 2026-08-03 from 2.0%); HQ retains balance; model at 5% total |
| White-label | Starter setup ~$10k + ~$1,500/mo; Growth setup ~$20k + ~$2,500/mo |
| Developer Sales OS | 0.5% dev-team sales / 2.5–3% Dproperty-sourced; $3–5k/mo desk min |
| 5-yr targets | 5 branded · 20 white-label · 15 developer |
| Sales mix, ramp curve, deferral lag (18–30 mo) | **OPEN — needs owner input** |
| HQ support cost per franchise, OPEX/staffing | **OPEN — needs owner validation (BLOCKS accuracy)** |

## 3. Tool Instructions (the prompt)
> "Build a **formula-driven 5-year financial model** in the tab structure of *Section 1*, driven entirely by the Assumptions tab (*Section 2*). Implement: (a) the **local commission waterfall** (5% → 50/50 co-broke → 2.5% into company → 35/10/55; royalty 7.5% on the into-company 2.5%); (b) **Dproperty Select** economics (franchisee 2.5% branded / 1.5% white-label, HQ retains balance); (c) the **franchise-fees bundle** (launch + OS + royalty/fund + floor + CRM margin); (d) white-label and developer lines; (e) a consolidated **5-Year P&L** with revenue by line and EBITDA. No hardcoded outputs — every result is a formula referencing assumptions. Add charts for revenue-by-line and EBITDA. Flag OPEX/staffing rows as 'owner-validation required'."

## 4. Reference Outputs (from v0.7 — must reconcile)
- **Per $300k local unit:** GCI into company $7,500; **HQ royalty ~$562**; franchise net 55% ($4,125).
- **Dproperty Select per $300k:** franchisee $7,500; **HQ retains ~$7,500** (white-label: partner $4,500, HQ ~$10,500).
- **Revenue:** Y1 ~$87k → Y3 ~$660k → **Y5 ~$1.59M.**
- **EBITDA:** negative Y1–2 → +$15k Y3 → **+$630k Y5.**
- **Y5 revenue mix:** Select (HQ-retained) ~$360k · franchise-fees bundle ~$197k · white-label ~$438k · developer ~$600k.

## 5. Build & QA Checklist
- [ ] Assumptions tab drives all outputs; no hardcoded results.
- [ ] Waterfall + royalty base = gross-into-company (un-gameable).
- [ ] Three-flow firewall respected (income ≠ agent payout ≠ HQ royalty).
- [ ] Outputs reconcile to §4 reference figures.
- [ ] OPEX/staffing flagged for owner validation.
- [ ] Currency USD throughout.
- [ ] **Phase-2 (ecosystem) model:** separate build — space/membership, events, matchmaking, equity fund, franchise pull-through, data, hub capex. NOT in this file.

## 6. Source & Change Log
- **Source:** [[Financial Model Summary]] + Decision Log (2026-07-04/05 pricing & waterfall) + Pitch S14–S15. SoT = `Dproperty_OS_Financial_Model.xlsx v0.7`.
- **Change log:** 0.7 (2026-07-21) — handoff created documenting v0.7 logic. Open: commission-rate confirmation (5% vs 0.75%), OPEX/staffing validation, Phase-2 model.
