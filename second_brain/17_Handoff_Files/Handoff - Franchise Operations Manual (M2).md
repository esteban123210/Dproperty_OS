---
project: Dproperty OS
title: "Handoff - Franchise Operations Manual (M2)"
type: handoff
deliverable: "Franchise Operations Manual (M2)"
target_output: "Printable book (PDF)"
target_tool: "Markdown-to-PDF book generator or AI document tool"
source_notes: ["05_Franchise_Package/Operations/Operations Manual.md", "Process Library 01–07"]
version: 0.5
status: Ready to generate (tracks M2 v0.5)
owner: Esteban
last_updated: 2026-07-21
tags: [handoff, production, operations, manual]
---

# HANDOFF — Franchise Operations Manual (M2)

> **One-file, self-contained package** to generate the final **printable Franchise Operations Manual book (PDF)**. The owner-facing manual **plus** all seven processes are inlined so the book stands alone. `[local]` marks market-specific values.

## 0. Production Brief
- **Deliverable:** the owner-facing manual — how to run a Dproperty office day to day (Tier 1, for the Principal/PRIN).
- **Output:** print-ready **PDF book**, ~30–45 pages (largest of the manuals because it inlines the process library).
- **Target tool:** Markdown→PDF book generator or AI doc tool.
- **Fidelity goal:** the flagship operating manual — premium, structured, easy to navigate.
- **Audience:** franchisee owner; also HQ onboarding reference.
- **Language:** EN master; ES edition per market `[local]`.

## 1. Design & Brand Direction
- Premium, structured, navigable. Clear part/chapter hierarchy. Boutique but businesslike.
- Layout: cover → title → **detailed TOC** → Part A (running the office) → Part B (the seven processes, one chapter each) → KPI dashboard → governance page. Running header "Dproperty · Operations Manual"; page numbers.
- Style RACI tables and flow tables cleanly; use the accent color for table headers and the "firewall" callout.
- Each process chapter starts on a new page.

## 2. Assets Required
| Asset | Purpose | Source | Status |
|---|---|---|---|
| Logo | Cover, header | Drive/Brand | need |
| Brand color hex + fonts | Whole book | Brand kit | need |
| Process flow diagrams (optional) | Visualize each process | Generate from tables | optional |
| Market pack values `[local]` | Resolve amounts/thresholds | [[Localization Framework]] | partial |

## 3. Tool Instructions (the prompt)
> "Generate a **print-ready PDF operations manual** from the Markdown in *Section 4*. Requirements: (1) cover with logo + title *Franchise Operations Manual* + subtitle *For the Dproperty Principal*; (2) a **detailed multi-level TOC**; (3) premium structured typography per *Section 1*; (4) render all flow and RACI tables cleanly, avoiding mid-row page breaks; (5) start each of the seven process chapters on a new page; (6) style the **commission-layer firewall** as a prominent boxed callout; (7) optionally render a simple flow diagram per process from its step table; (8) running headers + page numbers; (9) US-Letter + A4. Use only the provided content; keep `[local]` tags visible."

## 4. Final Content (self-contained)

### Cover
**Dproperty — Franchise Operations Manual** · *For the Dproperty Principal* · Version 0.5 · Confidential

### PART A — Running your office

**Who this is for.** The franchisee owner (PRIN). Your salespeople use the Sales Playbook; you use this. Roles never names; USD unless your market pack overrides; `[local]` values from the market pack.

**1. How to use this manual.** This is the owner-facing view of the Process Library (Part B). Part B holds the authoritative step/RACI/KPI detail; Part A tells you how to run the office. If they differ, Part B + the Decision Log win.

**2. Your office at a glance.** Minimum staffing: **PRIN + Sales Advisor (SA) + Operations Coordinator (OC)**. Other roles (SD, OD, CA, BI, PH) start as HQ-shared services or AI, or are hats worn by the Principal, and split out as you grow. A role = a responsibility, not always a headcount.

**3. The operating system — seven processes.** Every commercial activity runs one of the seven in Part B: (1) Leads, (2) Preventa, (3) Secondary, (4) Assignment, (5) Rental, (6) Property Management, (7) Commissions.

**4. People & training.** Define who holds each role/hat; keep it current in the OS. Every advisor completes sales + compliance certification before client-facing work. Hiring follows HQ standards; brand and compliance are non-negotiable. Recertify on cadence and when a process/market pack changes.

**5. Finance & the commission firewall.** Three **separate** money flows — never merge:
> **① Income collection** (counterparties pay the office) · **② Agent payout** (you pay advisors on *your* office scheme `[local]`, not an HQ mandate) · **③ HQ royalty** (**7.5% = 6% + 1.5% on collected GCI**, computed on **gross-into-company**), plus the OS/platform fee and any minimum royalty floor.
Owner settlement for managed rentals (rent − deductions − management fee) is a **fourth, distinct** flow (Process 6). Report collected GCI accurately; the royalty base is un-gameable by design.

**6. Reporting rhythm.** Daily: keep CRM/OS current. Weekly: pipeline review (SD), report activity. Monthly: royalty/commission report on collected GCI, marketing + compliance, forecast. Quarterly: HQ business review.

**7. Systems & data.** Dproperty OS = operational source of truth. The CRM (white-labeled + SSO) = lead capture/follow-up. **Data first, documents second.** Approved templates only; files live in Drive and surface through the OS — never duplicated.

**8. Compliance.** Non-negotiable, HQ-enforced — see the Compliance Manual (M5): franchise law, licensing, AML/KYC & sanctions, data privacy, advertising/no-guarantees, anti-bribery, contracts, insurance. PRIN is accountable; certification required before go-live.

**9. Dproperty Select.** HQ-controlled inventory. Present under rules; earn the fixed originator payout `[local: 2.5% branded]`; never negotiate directly with developers or edit materials.

**10. Launch.** First 90 days follow the 30-60-90 Launch Plan and the First Franchisee Launch Playbook. Onboarding entry point: the Onboarding manual (M1).

**11. Governance.** Versioned; sections change only via HQ + the Decision Log. `[local]` values from your market pack; the process never changes locally without a logged deviation.

### PART B — The seven processes (authoritative detail)

> Each process below carries its flow, RACI, and KPIs. Roles: PRIN, SD, SA, OC, OD, CA, BI, PH (+ SA hats: Tenant Advisor, Listing Advisor, Originating Advisor).

**Chapter 1 — Leads.** Objective: standardize capture, qualification, follow-up.
Flow: capture (SA) → register CRM <1h `[local]` → verify (OC) → qualify Hot/Warm/Cold (SA) → propose assignment (BI) → validate (SD) → first contact <24h (SA) → structured follow-up D1/3/7/14 (SA) → weekly supervision (SD) → automated nurture (BI) → weekly report (BI).
KPIs: first contact <24h; leads registered <1h >90%; lead→meeting >25%.

**Chapter 2 — Preventa (Lista Cero).** Objective: off-plan sales with developers.
Flow: meeting/profile (SA) → present + ROI (SA) → validate (SD) → reservation `[local amount]` (SA) → approve (SD) → notify developer (OC) → KYC docs (OC) → draft contract (OC) → approve (SD) → sign (OC) → down-payment `[local %]` (OC) → collect commission (OC) → update CRM (OC) → post-sale (OC).
KPIs: meeting→reservation >30%; reservation→contract <15d; complete files 100%.

**Chapter 3 — Secondary Market Sale.** Objective: resale to end users.
Flow: profile (SA) → visit agenda (SA) → visits (SA) → prepare offer (SA) → **SD approves** → present to seller (SA) → negotiate (SA+SD) → reservation (OC) → contract (OC) → parallel legal validations `[local]` (OC) → final approval (SD) → sign + collect (OC) → legal closing `[local]` (OC) → handover + inventory (SA+PH) → 30-day follow-up (SA).
KPIs: visits→offers >20%; offers→reservations >40%; NPS >80.

**Chapter 4 — Assignment (Cesión).** Objective: assign an investor's contract to a new buyer, maximizing the investor's return.
Rule: **dual validation when the selling SA ≠ the Originating Advisor; SD decides conflicts.**
Flow: profile buyer (SA) → visits (SA) → internal validation (SD) → prepare offer (SA) → dual approval (SD) → present to assignor (SA) → negotiate (SA+SD) → reservation (OC) → assignment contract (OC) → final approval (SD) → tripartite signing (OC) → closing + handover (SA+PH) → ROI report (BI).
KPIs: validation with originating advisor 100%; return ≥ projection; total time <30d.

**Chapter 5 — Long-Stay Rental.** Objective: leasing with full traceability.
Rule: **the call never replaces the written record; no signing until both parties approve the same contract version.**
Flow: register (SA·Tenant Advisor) → qualify + flag special profiles → visit + mandatory disclosures (furnished: 2 deposits + first month `[local]`) → structure offer → phone owner → inform Listing Advisor → **formal traceability email** → **CA approves profile** → formal offer + draft (OC) → review route (OD) → **single version control** (OC) → sign + payments (OC) → renovation record (OC) → prep + inventory (PH) → log warranties (PH+OC) → handover (SA+PH) → activate 45/60-day alerts (OC) → 7 & 30-day follow-up.
KPIs: offers with formal backup 100%; special profiles with written approval 100%; handovers with signed inventory 100%.

**Chapter 6 — Property Management.** Objective: manage leased assets; guarantee payments, preserve the asset, stay ahead of renewals/maintenance.
Flow: receive rental file (OC) → billing (OC) → payment reminder `[local]` → record payment (OC) → calculate deductions (OC) → validate settlement (OD) → transfer to owner (OC) → incidents (OC) → authorize repair `[local threshold]` (OD) → coordinate repair (PH) → document (PH) → monthly owner report (OC) → semi-annual inspection (PH) → 45/60-day expiry alert (OC) → renewal/exit (OC) → maintenance calendar (OC) → supplier coordination (OC) → file + reschedule (OC).
KPIs: on-time payments >95%; incident response <48h; renewals >70%.

**Chapter 7 — Commissions.** Objective: collect, calculate, pay commissions with traceability.
> **Firewall (boxed callout):** three separate flows — ① income collection · ② agent payout (office scheme `[local]`, e.g. Junior 35/70, Senior 40/45) · ③ HQ franchise royalty (7.5% on collected GCI, gross-into-company). **Never merge.**
Flow: confirm client payment (OC) → proforma (OC) → send to counterparty (OC) → receive transfer (OC) → formal invoice (OC) → notify advisors (OC) → advisors submit accounts `[local cutoff]` (SA) → calculate `[local scheme]` (OC) → validate (SD) → validate docs (BI) → assemble folders (OC) → authorize (SD) → process payments `[local cycle]` (OC) → archive (OC).
KPIs: trigger→advisor paid <10d `[local]`; complete folders 100%; documentation errors 0.

### KPI dashboard (aggregate)
Lead→meeting >25% · Meeting→reservation >30% · Offers→reservations >40% · On-time rental payments >95% · Incident response <48h · Renewals >70% · Commission cycle accuracy 0 errors.

### Governance page
Versioned; changes via HQ + Decision Log. `[local]` values from the market pack; no local process change without a logged deviation.

## 5. Build & QA Checklist
- [ ] Cover + detailed multi-level TOC.
- [ ] Part A / Part B structure; each process chapter starts on a new page.
- [ ] All flow + RACI tables render cleanly.
- [ ] Firewall callout prominent in Ch. 7 and §5.
- [ ] `[local]` tags visible (or resolved for a market edition).
- [ ] Content matches source ([[Operations Manual]] M2 v0.5 + Process Library) — no invented material.
- [ ] US-Letter + A4 exported.

## 6. Source & Change Log
- **Source:** [[Operations Manual]] (M2 v0.5) + Process Library [[01 - Leads]]–[[07 - Commissions]].
- **Change log:** 0.5 (2026-07-21) — created from M2 v0.5 with inlined process appendix.
