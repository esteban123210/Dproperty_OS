---
project: B_RealEstate
title: "Handoff Index"
type: handoff_index
status: Active
owner: Esteban
last_updated: 2026-09-29
tags: [handoff, production, source-of-truth]
---

> [!NOTE] Verified against canon 2026-09-23
> **Regenerate before external use.** Handoffs are self-contained snapshots, so this file may still inline pre-reconciliation naming, pricing or product boundaries. Check against canon: BluePrint oversees management outcomes across the commercial lifecycle without executing the sale · Building Blocks (not Academy) · B_ Partner (not White-Label) · $399/$799 + $1,500 setup · $950k raise · no “one database” or “CRM propio” claims. If a handoff and its source note disagree, **the source note wins**.
>
> Precedence: [[../01_Canon/00 - Precedence and Canonical Reconciliation|Canonical Reconciliation and Precedence]]

# Handoff Index

> [!IMPORTANT] How to produce files
> **[[00 - Production Pipeline]]** — markdown → presentable PDF. Tier 1 Obsidian export · Tier 2 Claude artifact (default for proposals) · Tier 3 ChatGPT/Canva.
> Reusable design prompt: [[CLAUDE DESIGN - Offer One-Pager Template]]


> **What a handoff file is.** A **single, self-contained Markdown file** that carries *everything an external tool needs* to generate the final, highest-fidelity version of a deliverable — content **plus** design direction, assets list, and copy-paste tool instructions. It is a **build artifact**: you hand this one file to an AI presentation tool, a website builder, or a book/PDF generator and get the finished product.
>
> **Self-contained by design.** External tools can't read the vault or follow wikilinks, so a handoff **inlines the actual final content** (not links). Duplication with the source note is intentional and is kept in sync by the update rule below.

## The standing rule (Decision 2026-07-21)
1. **Every deliverable we work on gets a handoff file** here in `12_Handoffs/`.
2. **On every session close**, the handoff file for each deliverable touched this session is **created or updated** so it always reflects the latest final content. (Now part of Close Session Mode in `CLAUDE.md`.)
3. A handoff always contains: **Production Brief · Design/Brand Direction · Assets Required · Tool Instructions (the prompt) · Final Content (self-contained) · Build & QA Checklist · Source & Change Log.** Template: [[_Handoff Template]].
4. Naming: `Handoff - <Deliverable> [<id>].md`.

## Registry

| Deliverable | Handoff file | Target output | Tool type | Status |
|---|---|---|---|---|
| Sales Playbook (M4) | [[Handoff - Sales Playbook (M4)]] | Printable book (PDF) | Book/PDF generator | 🟢 v0.5 |
| Franchise Operations Manual (M2) | [[Handoff - Franchise Operations Manual (M2)]] | Printable book (PDF) | Book/PDF generator | 🟢 v0.5 |
| Compliance Manual (M5) | [[Handoff - Compliance Manual (M5)]] | Printable book (PDF) | Book/PDF generator | 🟢 v0.5 |
| Franchise Onboarding (M1) | [[Handoff - Franchise Onboarding (M1)]] | Printable book (PDF) | Book/PDF generator | 🟢 v0.5 |
| Launch Plan (M3) | [[Handoff - Launch Plan (M3)]] | Printable book (PDF) | Book/PDF generator | 🟢 v0.5 |
| Pitch Deck (Deck 1) | [[Handoff - Pitch Deck (Deck 1)]] | Slide deck (.pptx) | AI presentation tool | 🟢 v1.1 |
| Ecosystem Deck (Deck 2) | [[Handoff - Ecosystem Deck (Deck 2)]] | Slide deck (.pptx) | AI presentation tool | 🟢 v0.6 |
| **Ecosystem Website — DESIGN PROMPT** | [[CLAUDE DESIGN - Ecosystem Website Design Prompt]] | **Full visual + motion design** | Claude Design | 🟢 v1.0 |
| **Ecosystem Website — BUILD BRIEF** | [[LOVABLE - Ecosystem Website Build Brief]] | **Paste-ready ES/EN brief for Lovable** | Lovable | 🟢 v1.0 |
| Ecosystem Website (spec/source) | [[Handoff - Ecosystem Website]] | Website (B2B, 3 service lines) | Lovable / AI site builder | 🟢 v1.0 |
| Public Website (Dproperty brand site) | [[Handoff - Public Website]] | Website (consumer/investor) | Website/AI site builder | 🟡 v1.1 — re-scoped 2026-08-03 |
| Brand Manual | [[Handoff - Brand Manual]] | Brand book + kit | Design tool | 🟢 v0.5 |
| Welcome Kit | [[Handoff - Welcome Kit]] | Print + physical spec | Design/print | 🟢 v0.5 |
| Financial Model | [[Handoff - Financial Model]] | Spreadsheet | Excel/Sheets | 🟢 v0.7 |
| **BluePrint app — Release 1 (Back Office OS)** | [[../02_Offers/01_BluePrint/20 - Wireframe - Back Office OS]] | **Working web application** | Developers / AI code generator | 🟢 v1.0 |
| **BluePrint app — DESIGN PROMPT** | [[CLAUDE DESIGN - BluePrint App Design Prompt]] | **Functional clickable app prototype** | Claude Design | 🟢 v1.0 |

*(Add a row whenever a new deliverable begins. HQ manual M0 and white-label/developer overlays get handoffs once drafted.)*

> **Exception — BluePrint app handoff lives in `02_Offers/01_BluePrint/`, not here.** It is self-contained and tool-ready in the required sense (design tokens, screens, primitives, permissions, build order and acceptance criteria in one file), but it is also the *canonical product specification* under [[../98_Archive/Superseded Product/BluePrint Product Map]]. Copying it into `12_Handoffs/` would create exactly the source-vs-handoff drift the standing rule exists to prevent, on the vault's most load-bearing spec. It is therefore registered here and maintained in place. Decision 2026-08-26.

## Coverage note
All current major deliverables now have a handoff (11 files). **Not yet built** (deliverable itself not ready): M0 HQ manual, white-label overlay, developer overlay, and the Phase-2 ecosystem financial model — each gets a handoff once its source exists.

## Notes
- Handoffs are **generated from the source notes**; if a handoff and its source ever disagree, the **source note wins** and the handoff is regenerated.
- Keep `[local-market variable]` tags in handoffs so the production tool knows what is market-specific.

## Product architecture acceptance — 2026-09-29 [D]

BlankCRM executes lead capture, legal workflow, commercial approvals, contracts, payment milestones, closing, commissions and post-sale, with communications, automation and commercial dashboards. BluePrint provides CRM-agnostic financial health, expected-vs-actual cash, expense/budget/variance control, KPI/CRM oversight, Glitches, policies, management audit and executive AI recommendations. Commercial execution screens belong in BlankCRM; BluePrint screens show evidence, verification and management intervention. BlankCRM must operate without BluePrint. A BluePrint management decision does not execute a sales action.

Spanish production copy: BlankCRM ejecuta todo el ciclo comercial: captación, calificación, gestión legal, aprobaciones, contratos, hitos de pago, cierre, comisiones y postventa; comunicaciones, automatización y tableros comerciales. Puede operar sin BluePrint. BluePrint es la capa de gestión interna, gobierno e inteligencia, independiente del CRM: salud financiera, caja esperada frente a real, gastos, presupuestos, desviaciones, KPI, supervisión del CRM, procesos y Glitches, auditoría, políticas y roles ejecutivos de IA. Observa, verifica y recomienda; no ejecuta ventas.
