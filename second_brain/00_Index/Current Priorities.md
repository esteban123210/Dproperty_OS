---
project: B_RealEstate
title: "Current Priorities"
type: priorities
status: Active
owner: Esteban
last_updated: 2026-08-16
source: Merged canonical (00_Index + AI Handoff Pack synced 2026-07-14)
tags: [priorities, next-actions, execution]
---

# Current Priorities

> **Canonical note (2026-08-16):** This file is the single source of truth. The AI Handoff Pack copy is a pointer.

## Session Update (2026-08-17) — Vault Consistency Audit

Ran a full propagation audit across `second_brain/` before starting BluePrint product work (see [[Decision Log]] 2026-08-17). Headline: the **2026-08-03 white-label Dproperty Select revision (2.0% → 1.5%, access no longer excluded) had not propagated into ~20 live files**, including the pitch deck, sales playbook, and three tool-ready handoff files — all fixed. Also fixed: EUR→USD in the Franchisee Acquisition Playbook, a stale LMS-vendor question in Roles and Access Matrix, and two resolved-but-still-open-looking items in Open Questions.

**Known remaining staleness (not fixed, flagged for a deliberate pass):**
- `16_Task_Management/Deliverables Tracker - Compact MD.md` — last real content update 2026-07-21; does not list the `18_Ecosystem/` folder (17 files), `17_Handoff_Files/` (14 files), or the BluePrint Product Map/Constitution/Golden Workflow. Needs an Excel-tracker regen, not a text patch.
- `03_Pitch/Pitch_Deck_Content.md` (v0.9, 2026-07-02) — predates the pricing restructure entirely; recommend regenerating from [[../03_Pitch/Pitch Deck Outline|Pitch Deck Outline]] or archiving rather than patching.
- Esteban's EUR salary figures (Compensation Package, Founder Pitch) — untouched; USD restatement is an owner decision, not a copy fix (see Open Questions).

**Next first action:** proceed to BluePrint product work — see the 2026-08-16 session update below, which is now the live work queue.

## Session Update (2026-08-16) — BluePrint Constitution + Golden Workflow

Completed the product-definition gate:

- [[../04_Product/BluePrint Product Constitution|Product Constitution]] is canonical for promise, boundaries, data ownership, three CRM modes, core entities, MVP and Copilot authority.
- [[../04_Product/BluePrint Golden Workflow - Wireframe and Validation|Golden Workflow]] defines the screen journey and passes an architecture desk-test for GoHighLevel, another CRM and BluePrint Direct without separate product variants.
- [[../04_Product/BluePrint Product Map|Product Map]] is the new entry point for all BluePrint work.

**Next product actions:**

1. Build the clickable Golden Workflow prototype using the canonical routes and acceptance criteria.
2. Create the controlled Copilot proof of concept with approved templates, SOPs, anonymized transactions and governed KPIs.
3. Implement/mock the canonical Intake contract: GoHighLevel adapter, standard webhook/API and guided manual/CSV intake.
4. Run the five-participant usability test and record time, errors, terminology confusion and Copilot trust.
5. Do not expand secondary modules until all three intake modes complete the same workflow.

## Session Update (2026-08-16) — B_RealEstate Ecosystem + BluePrint

Canonical architecture and naming are now documented in [[../18_Ecosystem/README|18_Ecosystem]]. Immediate order of work:

1. **Approve one commercial economics baseline** across the live website, contracts, pitch materials, and finance model.
2. **Correct the live-site P0 claims and routes** documented in [[../18_Ecosystem/15 - Website Audit - bfranchising.com - 2026-08-16|Website Audit]]—especially the BluePrint name, GoHighLevel disclosure, source-of-truth language, Dproperty Select governance, forms, and legal pages.
3. ~~**Define BluePrint's golden back-office workflow.**~~ Completed at product-architecture level in [[../04_Product/BluePrint Golden Workflow - Wireframe and Validation|Golden Workflow]]; clickable implementation/usability validation is next.
4. **Decide DpropertyLiving's status** before presenting it as a fourth ecosystem door.
5. **Define VAULTED's access, monetization, compliance, and integration rules** before implementation.

**Decision rule:** BluePrint complements GoHighLevel; it does not replace the CRM. Open edX remains the Academy delivery engine. Each system has one declared source-of-truth responsibility.

## Session Update (2026-07-21) — Manuals System + Process Library

Built the **manuals architecture** and executed the first real pass. Outcomes:
- **6-manual / 3-audience system** defined ([[../05_Franchise_Package/Manuals System Index|Manuals System Index]]); M0 HQ manual deferred.
- **Process Library** — agency's 7 commercial processes **abstracted to role-agnostic, market-flagged** files (crown-jewel content).
- **Roles, never names** is now a **project-wide standing rule** (Decision 2026-07-21; also in CLAUDE.md).
- **Rebuilt to v0.5:** Sales Playbook (M4), Franchise Operations Manual (M2), Compliance Manual (M5). **Fixed:** First Franchisee Launch Playbook → v0.2 (standards).
- **New frameworks:** Localization (process-global/values-local) + Multi-Line (shared core + overlays).
- **Audit:** multinational-hub readiness ~30% → **~55%**; two P0 gates remain — **compliance legal sign-off** and **localization packs**.

**Next first action:** start the **Colombia market pack** in [[../05_Franchise_Package/Localization/Localization Framework|Localization Framework]] (or book the **M5 legal review**), then upgrade **M1 Onboarding + M3 30-60-90** on the Process Library. Full path in [[../05_Franchise_Package/Manuals Audit and Gap Analysis|Manuals Audit]] (P0→P2).

## Session Update (2026-07-14) — Pitch Deck Content + Ecosystem Reframe

Worked the **pitch deck content layer** (Pitch Sprint Week 1). Outcomes:
- **[[Pitch Deck Outline]] → v1.1** — 20 slides. Opens on the ecosystem vision; adds a franchise **Problem → Solution → Proof-of-Concept** sequence (accelerator thesis); unit economics split into 3 revenue sections; bridges back to the vision before the ask. Full back-pocket strategic analysis.
- **[[Ecosystem Deck Outline]] → v0.6 (Deck 2)** — audience now owners + major investors + potentially government; first hub city = **Panama City**.
- **Strategic reframe logged:** franchising = Phase 1 of an ecosystem play (19M soul / Station F model). Propagated to Strategy, Business Plan (§20), Finance, Legal, Research.
- **Decisions logged (2026-07-14):** currency = USD; royalty floor = $500/mo; JV contributions defined (owners as investors incl. Simon's TheVelopers + projects); Miguel salary $0; equity held at 35/35/15/15 with an operator earn-in mechanism under exploration.
- **Vault hygiene:** 00_Index duplicate copies (Decision Log, Open Questions, Current Priorities, Vault Manifest) synced to the AI Handoff Pack versions.

**Next first action:** resolve remaining flags (track-record numbers, Esteban USD salary, TAM/SAM $), then hand Deck 1 to the branding/design session; queue the Phase-2 (ecosystem) financial model.

## Current Phase (Updated Jul 6)

**Execution Phase: Build first-franchise launch-ready package (Sept 15 deadline)**

Changed from "prepare internal owner pitch" to "deliver complete, turnkey franchisee package" by Sept 15.

## Scope Change (Jul 6)

- **Scope cut:** From 264 deliverables to 37 MVP items (first-franchise only)
- **Timeline:** 10.5 weeks (Jul 6 – Sept 15)
- **Team:** Esteban (full-time, 40 hrs/week) + Miguel (1–2 hrs/day, ~8 hrs/week)
- **Total capacity:** ~420–500 hours
- **Owner pitch timing:** No early pitch. Entire focus: Sept 15 launch-ready. Owner feedback comes after if needed.

## Immediate Goal (Next 10 Weeks)

Create a complete, professional, launch-ready first-franchise package that includes:

1. **Legal agreements** (6 contracts, lawyer-approved, ready to sign)
2. **Operations manuals** (250+ pages, step-by-step guidance)
3. **CRM setup** (GoHighLevel account, live, automated)
4. **Training** (Compliance certification module complete)
5. **Financial templates** (working calculators, P&L, earnings projections)
6. **Brand assets** (logo, colors, fonts, templates, 80+ page brand manual)
7. **Launch support** (30/60/90 plan, weekly coaching, success metrics)
8. **Welcome experience** (letter, video, box, QR code to data room)

## Weekly Breakdown

### Weeks 1–4 (Jul 6 – Aug 2): Pitch Sprint
- Use existing [[16_Task_Management/Pitch Sprint Roadmap - July 2026.md]] (already locked)
- Output: Pitch deck, brochure, FAQ, software mock, 4 roadmaps, rehearsal on Jul 31
- Transition to franchise build on Aug 2

### Weeks 5–11 (Aug 3 – Sept 15): Franchise Build-Out
- Week 5: Legal kickoff + brand direction lock + financial model finalize
- Weeks 6–8: Legal agreements draft + all manuals draft + CRM setup
- Weeks 9–10: Legal revisions + final polish + integration + QA
- Week 11: Final review + production + launch

## Critical Path (Do This First)

1. **Week 5 (Aug 3–9):**
   - Engage lawyer (franchise agreement strategy, timeline, cost)
   - Finalize franchisee profile (who are we selling to?)
   - Lock brand direction (existing Dproperty brand vs. new approach?)
   - Finalize financial model v1.0 (all agreements reference this)

2. **Weeks 6–7 (Aug 10–23):**
   - Draft all 6 legal agreements (Franchise Agreement, Brand License, NDA, Commission Agreement, OS License, Select Participation)
   - Draft Master Operations Manual (outline + sample chapters)
   - Draft Sales Playbook (scripts + objection handling)
   - Begin Brand Manual design (Chapters 1–4)

3. **Weeks 8–9 (Aug 24 – Sept 6):**
   - Finalize all manuals (operations, sales, compliance)
   - Get legal agreements revised by lawyer (v0.2)
   - Complete GoHighLevel CRM setup
   - Complete Brand Manual (Chapter 5, all templates)

4. **Week 10 (Sept 7–13):**
   - Integrate entire franchisee onboarding sequence (no gaps, logical flow)
   - Organize data room + create index
   - QA all documents (links, cross-references, consistency)
   - Final review + production prep

5. **Sept 15:**
   - Deliver complete package to first franchisee

## Key Decisions LOCKED (Jul 7, GTM Session)

✅ **GO-TO-MARKET STRATEGY FINALIZED**

- [x] **Franchisee profile CONFIRMED:** Agents Seeking Independence (PRIMARY) + Sales Professionals from other sectors (SECONDARY) + Youth Entrepreneurs (VOLUME)
- [x] **Target markets CONFIRMED:** Panama (local market), Bogotá, Medellín
- [x] **GTM Strategy LOCKED:** 3-persona approach, minimal budget (€2-5k organic), Week 5-12 execution
- [x] **Pricing FROZEN:** $30k launch, $1k/month, 6% + 1.5% royalty, 55% commission split *(currency confirmed USD 2026-07-14)*

## Current Risks (Updated)

| Risk | Mitigation |
|---|---|
| Legal agreements take longer | Start Week 5 early; prioritize 3 agreements first |
| Brand manual design iterations | Lock design direction Week 5; max 2 revision rounds |
| GoHighLevel complexity | Start simple Week 8; enhance post-launch if needed |
| Manuals need major rework | Approve content flow early; lock 70% by end of Week 7 |
| Franchisee profile not locked | Confirmed Jul 7 |

## Next Checkpoint

**Post-pitch-sprint:** resolve remaining pitch flags → branding/design session for Deck 1 → Phase-2 (ecosystem) financial model → legal kickoff (Week 5).
