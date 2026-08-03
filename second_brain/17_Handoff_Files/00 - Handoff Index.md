---
project: Dproperty OS
title: "Handoff Index"
type: handoff_index
status: Active
owner: Esteban
last_updated: 2026-07-21
tags: [handoff, production, source-of-truth]
---

# Handoff Index

> **What a handoff file is.** A **single, self-contained Markdown file** that carries *everything an external tool needs* to generate the final, highest-fidelity version of a deliverable — content **plus** design direction, assets list, and copy-paste tool instructions. It is a **build artifact**: you hand this one file to an AI presentation tool, a website builder, or a book/PDF generator and get the finished product.
>
> **Self-contained by design.** External tools can't read the vault or follow wikilinks, so a handoff **inlines the actual final content** (not links). Duplication with the source note is intentional and is kept in sync by the update rule below.

## The standing rule (Decision 2026-07-21)
1. **Every deliverable we work on gets a handoff file** here in `17_Handoff_Files/`.
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
| **Ecosystem Website — BUILD BRIEF** | [[LOVABLE - Ecosystem Website Build Brief]] | **Paste-ready ES/EN brief for Lovable** | Lovable | 🟢 v1.0 |
| Ecosystem Website (spec/source) | [[Handoff - Ecosystem Website]] | Website (B2B, 3 service lines) | Lovable / AI site builder | 🟢 v1.0 |
| Public Website (Dproperty brand site) | [[Handoff - Public Website]] | Website (consumer/investor) | Website/AI site builder | 🟡 v1.1 — re-scoped 2026-08-03 |
| Brand Manual | [[Handoff - Brand Manual]] | Brand book + kit | Design tool | 🟢 v0.5 |
| Welcome Kit | [[Handoff - Welcome Kit]] | Print + physical spec | Design/print | 🟢 v0.5 |
| Financial Model | [[Handoff - Financial Model]] | Spreadsheet | Excel/Sheets | 🟢 v0.7 |

*(Add a row whenever a new deliverable begins. HQ manual M0 and white-label/developer overlays get handoffs once drafted.)*

## Coverage note
All current major deliverables now have a handoff (11 files). **Not yet built** (deliverable itself not ready): M0 HQ manual, white-label overlay, developer overlay, and the Phase-2 ecosystem financial model — each gets a handoff once its source exists.

## Notes
- Handoffs are **generated from the source notes**; if a handoff and its source ever disagree, the **source note wins** and the handoff is regenerated.
- Keep `[local-market variable]` tags in handoffs so the production tool knows what is market-specific.
