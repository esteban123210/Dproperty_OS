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
| Franchise Onboarding (M1) | `Handoff - Franchise Onboarding (M1)` | Printable book / PDF | Book/PDF generator | ⬜ to build |
| Launch Plan (M3) | `Handoff - Launch Plan (M3)` | Printable book / PDF | Book/PDF generator | ⬜ to build |
| Pitch Deck (Deck 1) | `Handoff - Pitch Deck (Deck 1)` | Slide deck | AI presentation tool | ⬜ to build (source: [[Pitch Deck Outline]]) |
| Ecosystem Deck (Deck 2) | `Handoff - Ecosystem Deck (Deck 2)` | Slide deck | AI presentation tool | ⬜ to build |
| Public Website | `Handoff - Public Website` | Website | Website/AI site builder | ⬜ to build (source: [[Public Site Wireframe]], [[Public Site Copy - ES Master]]) |
| Brand Manual | `Handoff - Brand Manual` | Printable book / brand kit | Design tool | ⬜ to build |
| Welcome Kit | `Handoff - Welcome Kit` | Print + physical spec | Design/print | ⬜ to build |
| Financial Model | `Handoff - Financial Model` | Spreadsheet | Excel/Sheets | ⬜ to build |

*(Add a row whenever a new deliverable begins. HQ manual M0 and white-label/developer overlays get handoffs once drafted.)*

## Priority to build next
1. **Pitch Deck (Deck 1)** — named example; source outline is mature (v1.1).
2. **Public Website** — named example; wireframe + ES copy exist.
3. **M1 Onboarding + M3 Launch** — once upgraded to standards.

## Notes
- Handoffs are **generated from the source notes**; if a handoff and its source ever disagree, the **source note wins** and the handoff is regenerated.
- Keep `[local-market variable]` tags in handoffs so the production tool knows what is market-specific.
