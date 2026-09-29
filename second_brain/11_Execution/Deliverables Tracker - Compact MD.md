---
project: B_RealEstate
title: "Deliverables Tracker - Compact MD"
type: tracker
status: Generated from Excel
owner: Esteban
last_updated: 2026-09-29
source: ChatGPT baseline vault package
tags: [deliverables, tracker]
---

> [!NOTE] Verified against canon 2026-09-23
> Active execution tracker. Deliverables affected by the 2026-09-23 reconciliation need status review — especially product specs, pitch decks and finance models.
>
> Precedence: [[../01_Canon/00 - Precedence and Canonical Reconciliation|Canonical Reconciliation and Precedence]]

# Deliverables Tracker - Compact MD

This is a lightweight Markdown version of the Excel Deliverables Tracker. Use it in AI chats when the XLSX would use too many tokens.

Last generated: 2026-07-01

## How To Use

- Use the Excel file as the editable execution tracker.
- Upload the latest Excel tracker to ChatGPT when you want this Markdown file regenerated.
- Use this compact MD file for AI context and quick searching.

## 2026-07-04 Update — Franchise Pricing Restructure & Financial Model

**Decision applied (see Decision Log 2026-07-04):** launch fee $30k/$40k; royalty 6% + Network & Brand Fund 1.5% on **collected** GCI; Private Collection renamed **Dproperty Select** with fixed-% payout (2.5% branded / 2.0% white-label of sale price).

**New deliverables created:**
- `98_Archive/Exports/Dproperty_OS_Financial_Model.xlsx` **v0.7** — formula-driven model (README/Assumptions/Model + commission-waterfall reference). Status: Draft, OPEX rows need owner validation. Outputs: Y1 $87k → Y5 **$1.59M** revenue; EBITDA positive Y3 (~$15k) → Y5 (~$630k). Local royalty now on gross-into-company after the 50/50 external-advisor split.
- `98_Archive/Superseded Execution/Pitch Sprint Roadmap - July 2026.md` **v1.0** — 4-week execution plan (Jul 6–Aug 2) to a rehearsal-ready investor pitch; 5 roadmaps + priority order + pitch table.

**Updated this session (Business Plan workstream):**
- DP-006 Business Plan → v0.9 (In Review). Pricing/Select/model aligned.
- Pricing Model, Unit Economics, Conservative 5-Year Plan, Funding Plan → v0.6.
- Strategy: Franchise / White-Label / Private Collection / Business Model Overview → updated.
- Dproperty Select notes (Guide, Commission Split, Deal Workflow) → v0.6.
- Franchise Onboarding PDF, Sales Playbook → updated.
- Decision Log, Open Questions → updated.

**Still needs update (next session):**
- DP-007 Pitch Deck / `98_Archive/Superseded Pitch/Pitch_Deck_Content.md` — pricing & revenue slides still show old numbers.
- AI Handoff Pack (01 Context Brief, 02 Decision Log, 03 Open Questions, 05 Current Priorities, 06 Tracker, 07 Closeout) — sync to 00_Index versions.
- `98_Archive/Exports/Dproperty_OS_Business_Plan.md` — regenerate from canonical (stale hand-copy).
- **New task:** validate financial model OPEX/staffing; confirm 5% vs 0.75% commission (Fernando/Ernesto).

## 2026-07-14 Update — Pitch Deck Content v1.0 + Ecosystem Reframe

**Session:** built the pitch deck content layer and reframed the venture as an ecosystem play (franchising = Phase 1). See [[../00_Start_Here/AI Handoff Pack/07_Latest Session Closeout|Latest Session Closeout]].

**Row changes:**
- **DP-007 Pitch Deck** → content outline advanced to **v1.0** (17 slides + back pocket, ecosystem reframe). Design/build still pending (branding session). Status effectively **In Progress (content ready, design pending)**.

**New deliverable created:**
- **Ecosystem Deck (Deck 2)** — `98_Archive/Superseded Pitch/Ecosystem Deck Outline.md` **v0.5**. 10–15 yr ecosystem/hub vision + capital-recycling bridge. Status: Structured Draft; NOT raise-ready until a Phase-2 P&L, hub capex, and location exist. *(Suggest new tracker ID DP-270 when the Excel tracker is next regenerated.)*

**Updated this session (ecosystem framing appended):**
- Strategy: Business Model Overview, Strategic Thesis, Moat and Positioning, Franchise Strategy, Ecosystem Workflow.
- Business Plan: Dproperty OS Business Plan (§20 + Validation 12–15), Conservative 5-Year Plan.
- Finance: Financial Model Summary (Phase-2 model flagged).
- Legal: Legal Architecture (Phase-2 legal needs).
- Research: Research Backlog (ecosystem research block).
- Handoff pack: Decision Log, Open Questions, Current Priorities, Vault Manifest, Latest Session Closeout.

**Still needs action (next session):**
- Resolve pitch flags: currency ($ vs €30k), equity (confirm 35/35/15/15), Simón contribution, track-record numbers, Miguel salary, royalty floor.
- Build Phase-2 (ecosystem) financial model; decide first-hub city/capex.
- Branding/design session for Deck 1.
- Sync 00_Index duplicate copies to Handoff Pack versions.

## 2026-07-18 Update — Platform Architecture (Product Workstream)

**Session:** defined the full Dproperty OS platform information architecture (public site + logged-in role-gated OS + 6 back-office systems), stress-tested with 72+ scenarios, and set the roles/human-vs-AI/agent-pricing model. See Decision Log 2026-07-18 and [[../00_Start_Here/Decision Log|Decision Log]].

**New deliverables created (Product / Phase 2 planning specs — not part of the 37 MVP-launch set):**
- **Platform Information Architecture** — `02_Offers/01_BluePrint/22 - Platform Information Architecture.md` **v0.5**. Two-layer architecture, ~14 public pages, ~25 OS modules, 6 back-office systems, T0/T1/T2 cost model, embedding strategy. *(Suggest tracker ID DP-270 at next Excel regen.)*
- **Platform Scenario Playbook** — `02_Offers/01_BluePrint/23 - Platform Scenario Playbook.md` **v0.5**. 72+ scenarios (agent, prospect, HQ, HR, complaints, finance, claims/edge, glitch). *(Suggest DP-271.)*
- **Roles and Access Matrix** — `09_Data_and_AI/Roles and Access Matrix.md` **v0.5**. Hierarchy, role→access, human/AI map, confidentiality rules, agent pricing. *(Suggest DP-272.)*

**Impact on existing software rows (DP-061–DP-080):** these now have a defined IA parent. New systems to fold into the software backlog at next Excel regen: Command Bar, Field Mode (mobile), Resource Library, embedded Academy (LMS), embedded CRM, Cases/Ticketing engine, Finance/Back-Office, People/HR, Tenant Lifecycle, Audit Log, **Glitch Report**, Franchise Sales Room, Data Room generator.

**Updated this session:** Product Modules, Data Model, Prototype Spec, Prototype Control Note, Figma Handoff Notes, Master Index, Decision Log, Open Questions, Vault Manifest.

**Still needs action:** wireframe priority screens in Figma; assign DP-270–272 IDs in the Excel tracker; sync AI Handoff Pack duplicate copies (02/03/04/06) to the 00_Index canonical versions.

## 2026-07-21 Update — Manuals System + Process Library + Multinational Readiness

**Session:** built the manuals architecture and executed the first real pass. See [[../98_Archive/Session Closeouts/2026-07-21 - Work Session Closeout|2026-07-21 Closeout]] and Decision Log (+4 decisions).

**Row changes (Manuals workstream):**
- **DP-094 Master Operations Manual** → M2 Franchise Operations Manual **v0.5** (rebuilt on the Process Library). Path: `08_Operations/Operations Manual.md`.
- **DP-097 Sales Playbook** → M4 **v0.5** (rebuilt on Process Library). Path: `02_Offers/05_Dproperty_Franchise/04D - Sales Playbook.md`.
- **DP-101 Compliance Manual** → M5 **v0.5** (multinational coverage; needs legal sign-off). Path: `07_Legal_and_Compliance/Compliance Package.md`.
- **DP-046 30/60/90 Launch Plan** — companion **First Franchisee Launch Playbook v0.2** fixed to standards (roles/USD/relative weeks/commission math). Path: `02_Offers/05_Dproperty_Franchise/Launch/`.
- **DP-044 Franchise Onboarding** — unchanged this session; flagged for standards upgrade next.

**New deliverables created (suggest new tracker IDs at next Excel regen):**
- **Manuals System Index** — `08_Operations/Manuals System Index.md` (architecture, 6 manuals / 3 audiences).
- **Process Library (8 files, 7/7 processes abstracted)** — `02_Offers/05_Dproperty_Franchise/Operations/Process Library/` (role-agnostic Leads, Preventa, Secondary, Assignment, Rental, Property Mgmt, Commissions + Index/Role Map).
- **Source Material** — `08_Operations/Source Material/Dproperty Commercial Process Manual (v002-26).md` (verbatim import, read-only).
- **Localization Framework** — `08_Operations/Localization Framework.md` (Market Variables Matrix).
- **Multi-Line Manual Strategy** — `08_Operations/Multi-Line Manual Strategy.md`.
- **Manuals Audit & Gap Analysis** — `08_Operations/Manuals Audit and Gap Analysis.md`.

**Path reconciliation:** the Excel tracker lists manuals under a single `02_Offers/05_Dproperty_Franchise/Manuals/` folder; actual files live under `Operations/`, `Sales/`, `Compliance/`, `Launch/`. Update the Excel paths at next regen.

**Still needs action (next session):** legal sign-off on M5 per market; build Colombia market pack + reconfirm Panama values; decide manual language; upgrade M1 Onboarding + M3 30-60-90 + Brand + Training to standards; write white-label & developer overlays.

## Status Summary

- Not Started: ~258
- Draft Created: 4
- In Progress: 1
- **Manuals v0.5 (Structured Draft): 3** *(M2 Operations, M4 Sales, M5 Compliance — 2026-07-21)*
- **Process Library (abstracted, role-agnostic): 7 processes + index** *(2026-07-21)*
- **New manuals frameworks: 4** *(Manuals Index, Localization, Multi-Line, Audit — 2026-07-21)*
- Product architecture specs (v0.5): 3 *(Platform IA, Scenario Playbook, Roles & Access — added 2026-07-18)*

## Priority Summary

- High: 194
- Critical: 50
- Medium: 22
- Low: 3

## Workstream Summary

- Software: 20
- Legal Signing: 15
- Sales Assets: 15
- Marketing: 14
- GoHighLevel / CRM: 13
- Training Academy: 13
- Pre-Signing: 12
- Project Onboarding: 12
- Finance: 12
- Brand: 11
- Manuals: 11
- Compliance: 11
- Launch Support: 11
- Legal Templates - Client: 10
- Legal Templates - Broker: 10
- Legal Templates - Developer: 10
- Internal Templates: 10
- Private Collection: 10
- HQ Readiness: 10
- Knowledge Base: 9
- Reporting: 9
- Broker Network: 8
- Welcome Experience: 7
- Onboarding: 6

## Tracker Table

| ID | Workstream | Deliverable | Priority | Status | MVP | First Franchise | Format | Obsidian Path | Link/File | Baseline Note Created |
|---|---|---|---|---|---|---|---|---|---|---|
| DP-001 | Knowledge Base | B_RealEstate Master Index | Critical | Not Started | Yes | Yes | MD | 00_Start_Here/Master Index.md |  | Yes |
| DP-002 | Knowledge Base | Decision Log | Critical | Not Started | Yes | Yes | MD | 00_Start_Here/Decision Log.md |  | Yes |
| DP-003 | Knowledge Base | Open Questions | High | Not Started | Yes | Yes | MD | 00_Start_Here/Open Questions.md |  | Yes |
| DP-004 | Knowledge Base | Source Map | High | Not Started | Yes | Yes | MD | 00_Start_Here/Source Map.md |  | Yes |
| DP-005 | Knowledge Base | Conversation Summary | Critical | Draft Created | Yes | Yes | DOCX/PDF/MD | 03_Strategy/Conversation Summaries/ | Dproperty_OS_Conversation_Summary.* |  |
| DP-006 | Knowledge Base | Business Plan | Critical | Draft Created | Yes | Yes | DOCX/PDF/MD | 04_Business_Plan/ | Dproperty_OS_Business_Plan.* | Yes |
| DP-007 | Knowledge Base | Pitch Deck | Critical | Draft Created | Yes | Yes | PPTX | 05_Pitch_and_Investor/Final Decks/ | Dproperty_OS_Pitch_Deck.pptx |  |
| DP-008 | Knowledge Base | Prototype Spec for Figma | Critical | Draft Created | Yes | Yes | MD | 98_Archive/Superseded Product/Prototype Spec.md | Dproperty_OS_Prototype_Spec.md | Yes |
| DP-009 | Knowledge Base | Deliverables Checklist Tracker | Critical | In Progress | Yes | Yes | XLSX | 00_Start_Here/Deliverables Tracker.xlsx |  |  |
| DP-010 | Pre-Signing | Franchise Opportunity Brochure | Critical | Not Started | Yes | Yes | PDF | 02_Offers/05_Dproperty_Franchise/Pre-Signing/ |  |  |
| DP-011 | Pre-Signing | Why Dproperty Presentation | High | Not Started | Yes | Yes | PPTX | 02_Offers/05_Dproperty_Franchise/Pre-Signing/ |  |  |
| DP-012 | Pre-Signing | Founder Letter | Medium | Not Started | Yes | Yes | DOCX/PDF | 02_Offers/05_Dproperty_Franchise/Pre-Signing/ |  |  |
| DP-013 | Pre-Signing | Brand Story Document | High | Not Started | Yes | Yes | PDF | 02_Offers/05_Dproperty_Franchise/Pre-Signing/ |  |  |
| DP-014 | Pre-Signing | Dproperty vs Mass-Market Agencies One-Pager | High | Not Started | Yes | Yes | PDF | 02_Offers/05_Dproperty_Franchise/Pre-Signing/ |  |  |
| DP-015 | Pre-Signing | Private Collection Explainer | Critical | Not Started | Yes | Yes | PDF | 02_Offers/05_Dproperty_Franchise/Private_Collection/ |  |  |
| DP-016 | Pre-Signing | Territory Model Explainer | High | Not Started | Yes | Yes | PDF | 07_Legal_and_Compliance/Franchise/ |  |  |
| DP-017 | Pre-Signing | Franchise Economics One-Pager | Critical | Not Started | Yes | Yes | PDF | 06_Finance/ |  | Yes |
| DP-018 | Pre-Signing | Franchise Candidate Self-Assessment | Medium | Not Started | Yes | Yes | PDF/Form | 02_Offers/05_Dproperty_Franchise/Pre-Signing/ |  |  |
| DP-019 | Pre-Signing | Franchise Candidate Evaluation Form | High | Not Started | Yes | Yes | XLSX/Form | 02_Offers/05_Dproperty_Franchise/Pre-Signing/ |  |  |
| DP-020 | Pre-Signing | Discovery Call Script | Medium | Not Started | Yes | Yes | MD/DOCX | 02_Offers/05_Dproperty_Franchise/Pre-Signing/ |  |  |
| DP-021 | Pre-Signing | Franchise FAQ | High | Not Started | Yes | Yes | MD/PDF | 02_Offers/05_Dproperty_Franchise/Pre-Signing/ |  |  |
| DP-022 | Legal Signing | Master Franchise Agreement | Critical | Not Started | Yes | Yes | Contract | 07_Legal_and_Compliance/Franchise/ |  |  |
| DP-023 | Legal Signing | Brand License Agreement | Critical | Not Started | Yes | Yes | Contract | 07_Legal_and_Compliance/Franchise/ |  |  |
| DP-024 | Legal Signing | Dproperty OS License Agreement | Critical | Not Started | Yes | Yes | Contract | 07_Legal_and_Compliance/Software/ |  |  |
| DP-025 | Legal Signing | Territory Agreement | High | Not Started | Yes | Yes | Contract | 07_Legal_and_Compliance/Franchise/ |  |  |
| DP-026 | Legal Signing | Franchisee NDA | Critical | Not Started | Yes | Yes | Contract | 07_Legal_and_Compliance/NDA/ |  |  |
| DP-027 | Legal Signing | Non-Circumvention Agreement | Critical | Not Started | Yes | Yes | Contract | 07_Legal_and_Compliance/Franchise/ |  |  |
| DP-028 | Legal Signing | Data Processing Agreement | High | Not Started | Yes | Yes | Contract | 07_Legal_and_Compliance/Data/ |  |  |
| DP-029 | Legal Signing | Commission & Royalty Agreement | Critical | Not Started | Yes | Yes | Contract | 06_Finance/ |  |  |
| DP-030 | Legal Signing | Private Collection Participation Agreement | Critical | Not Started | Yes | Yes | Contract | 07_Legal_and_Compliance/Private_Collection/ |  |  |
| DP-031 | Legal Signing | Broker Network Participation Agreement | Medium | Not Started | Yes | Yes | Contract | 07_Legal_and_Compliance/Broker_Network/ |  |  |
| DP-032 | Legal Signing | Operations Manual Acknowledgment | High | Not Started | Yes | Yes | Contract | 07_Legal_and_Compliance/Franchise/ |  |  |
| DP-033 | Legal Signing | Brand Manual Acknowledgment | Medium | Not Started | Yes | Yes | Contract | 07_Legal_and_Compliance/Brand/ |  |  |
| DP-034 | Legal Signing | Payment Authorization Form | High | Not Started | Yes | Yes | Form | 06_Finance/ |  |  |
| DP-035 | Legal Signing | Authorized Signatory Form | High | Not Started | Yes | Yes | Form | 02_Offers/05_Dproperty_Franchise/Admin/ |  |  |
| DP-036 | Legal Signing | Franchisee Company Info Form | High | Not Started | Yes | Yes | Form | 02_Offers/05_Dproperty_Franchise/Admin/ |  |  |
| DP-037 | Welcome Experience | Premium Welcome Box | Medium | Not Started | No | Yes | Physical Item | 02_Offers/05_Dproperty_Franchise/Welcome_Kit/ |  |  |
| DP-038 | Welcome Experience | Branded Wine or Champagne | Low | Not Started | No | Yes | Physical Item | 02_Offers/05_Dproperty_Franchise/Welcome_Kit/ |  |  |
| DP-039 | Welcome Experience | Printed Welcome Letter | Medium | Not Started | No | Yes | PDF/Physical | 02_Offers/05_Dproperty_Franchise/Welcome_Kit/ |  |  |
| DP-040 | Welcome Experience | Franchise Partner Certificate | Low | Not Started | No | Yes | Physical Item/PDF | 02_Offers/05_Dproperty_Franchise/Welcome_Kit/ |  |  |
| DP-041 | Welcome Experience | Branded Notebook and Pen | Low | Not Started | No | Yes | Physical Item | 02_Offers/05_Dproperty_Franchise/Welcome_Kit/ |  |  |
| DP-042 | Welcome Experience | QR Start Card | Medium | Not Started | Yes | Yes | Physical/Digital | 02_Offers/05_Dproperty_Franchise/Welcome_Kit/ |  |  |
| DP-043 | Welcome Experience | Founder Welcome Video | Medium | Not Started | Yes | Yes | Video | 02_Offers/05_Dproperty_Franchise/Welcome_Kit/ |  |  |
| DP-044 | Onboarding | Franchise Onboarding PDF | Critical | Not Started | Yes | Yes | PDF | 02_Offers/05_Dproperty_Franchise/Onboarding/ |  | Yes |
| DP-045 | Onboarding | Start Here Page | Critical | Not Started | Yes | Yes | MD/Web | 02_Offers/05_Dproperty_Franchise/Onboarding/ |  |  |
| DP-046 | Onboarding | 30/60/90-Day Launch Plan | Critical | Not Started | Yes | Yes | PDF/XLSX | 02_Offers/05_Dproperty_Franchise/Launch/ |  | Yes |
| DP-047 | Onboarding | Franchise Launch Checklist | Critical | Not Started | Yes | Yes | Checklist | 02_Offers/05_Dproperty_Franchise/Launch/ |  | Yes |
| DP-048 | Onboarding | HQ Contact Directory | High | Not Started | Yes | Yes | PDF/MD | 02_Offers/05_Dproperty_Franchise/Onboarding/ |  |  |
| DP-049 | Onboarding | Support Process Guide | Medium | Not Started | Yes | Yes | PDF/MD | 02_Offers/05_Dproperty_Franchise/Onboarding/ |  |  |
| DP-050 | Brand | Brand Manual | Critical | Not Started | Yes | Yes | PDF | 02_Offers/05_Dproperty_Franchise/Brand/ |  | Yes |
| DP-051 | Brand | Logo Asset Library | Critical | Not Started | Yes | Yes | Folder | 02_Offers/05_Dproperty_Franchise/Brand/Assets/ |  |  |
| DP-052 | Brand | Tone of Voice Guide | High | Not Started | Yes | Yes | PDF/MD | 02_Offers/05_Dproperty_Franchise/Brand/ |  |  |
| DP-053 | Brand | Email Signature Template | High | Not Started | Yes | Yes | Template | 02_Offers/05_Dproperty_Franchise/Brand/Templates/ |  |  |
| DP-054 | Brand | Business Card Template | Medium | Not Started | No | Yes | Template | 02_Offers/05_Dproperty_Franchise/Brand/Templates/ |  |  |
| DP-055 | Brand | Letterhead Template | Medium | Not Started | Yes | Yes | DOCX | 02_Offers/05_Dproperty_Franchise/Brand/Templates/ |  |  |
| DP-056 | Brand | Presentation Template | High | Not Started | Yes | Yes | PPTX | 02_Offers/05_Dproperty_Franchise/Brand/Templates/ |  |  |
| DP-057 | Brand | Proposal / Investment Memo Template | High | Not Started | Yes | Yes | DOCX/PDF | 02_Offers/05_Dproperty_Franchise/Brand/Templates/ |  |  |
| DP-058 | Brand | Social Media Template Pack | High | Not Started | Yes | Yes | Folder | 02_Offers/05_Dproperty_Franchise/Marketing/Templates/ |  |  |
| DP-059 | Brand | Office Signage Files | Medium | Not Started | No | Yes | Folder | 02_Offers/05_Dproperty_Franchise/Brand/Signage/ |  |  |
| DP-060 | Brand | Office Experience Standards | Medium | Not Started | No | Yes | PDF | 02_Offers/05_Dproperty_Franchise/Brand/ |  |  |
| DP-061 | Software | Franchise Workspace | High | Not Started | Yes | Yes | Software Module | 02_Offers/01_BluePrint/Modules/ |  |  |
| DP-062 | Software | HQ Admin Dashboard | High | Not Started | Yes | Yes | Software Module | 02_Offers/01_BluePrint/Modules/ |  |  |
| DP-063 | Software | Franchise Dashboard | Critical | Not Started | Yes | Yes | Software Module | 02_Offers/01_BluePrint/Modules/ |  |  |
| DP-064 | Software | Client Module | Critical | Not Started | Yes | Yes | Software Module | 02_Offers/01_BluePrint/Modules/ |  |  |
| DP-065 | Software | Broker Module | High | Not Started | Yes | Yes | Software Module | 02_Offers/01_BluePrint/Modules/ |  |  |
| DP-066 | Software | Developer Module | High | Not Started | Yes | Yes | Software Module | 02_Offers/01_BluePrint/Modules/ |  |  |
| DP-067 | Software | Project Module | Critical | Not Started | Yes | Yes | Software Module | 02_Offers/01_BluePrint/Modules/ |  |  |
| DP-068 | Software | Unit Inventory Module | High | Not Started | Yes | Yes | Software Module | 02_Offers/01_BluePrint/Modules/ |  |  |
| DP-069 | Software | Deal Pipeline Module | Critical | Not Started | Yes | Yes | Software Module | 02_Offers/01_BluePrint/Modules/ |  |  |
| DP-070 | Software | Document Generator | Critical | Not Started | Yes | Yes | Software Module | 02_Offers/01_BluePrint/Modules/ |  |  |
| DP-071 | Software | Projection Generator | Critical | Not Started | Yes | Yes | Software Module | 02_Offers/01_BluePrint/Modules/ |  |  |
| DP-072 | Software | Commission Tracker | High | Not Started | Yes | Yes | Software Module | 02_Offers/01_BluePrint/Modules/ |  |  |
| DP-073 | Software | Task & Approval Module | High | Not Started | Yes | Yes | Software Module | 02_Offers/01_BluePrint/Modules/ |  |  |
| DP-074 | Software | Training Academy Module | High | Not Started | Yes | Yes | Software Module | 02_Offers/01_BluePrint/Modules/ |  |  |
| DP-075 | Software | Support Ticket Module | High | Not Started | Yes | Yes | Software Module | 02_Offers/01_BluePrint/Modules/ |  |  |
| DP-076 | Software | Knowledge Base Search | High | Not Started | Yes | Yes | Software Module | 02_Offers/01_BluePrint/Modules/ |  |  |
| DP-077 | Software | Private Collection Access Control | High | Not Started | Yes | Yes | Software Module | 02_Offers/01_BluePrint/Modules/ |  |  |
| DP-078 | Software | Reporting Export Module | High | Not Started | Yes | Yes | Software Module | 02_Offers/01_BluePrint/Modules/ |  |  |
| DP-079 | Software | E-Signature Integration | High | Not Started | Yes | Yes | Software Module | 02_Offers/01_BluePrint/Modules/ |  |  |
| DP-080 | Software | GoHighLevel Integration | High | Not Started | Yes | Yes | Software Module | 02_Offers/01_BluePrint/Modules/ |  |  |
| DP-081 | GoHighLevel / CRM | GoHighLevel Account Setup | High | Not Started | Yes | Yes | Template/Automation | 02_Offers/01_BluePrint/CRM/ |  |  |
| DP-082 | GoHighLevel / CRM | CRM Branding Setup | High | Not Started | Yes | Yes | Template/Automation | 02_Offers/01_BluePrint/CRM/ |  |  |
| DP-083 | GoHighLevel / CRM | Lead Pipeline | High | Not Started | Yes | Yes | Template/Automation | 02_Offers/01_BluePrint/CRM/ |  |  |
| DP-084 | GoHighLevel / CRM | Contact Custom Fields | High | Not Started | Yes | Yes | Template/Automation | 02_Offers/01_BluePrint/CRM/ |  |  |
| DP-085 | GoHighLevel / CRM | Lead Capture Forms | High | Not Started | Yes | Yes | Template/Automation | 02_Offers/01_BluePrint/CRM/ |  |  |
| DP-086 | GoHighLevel / CRM | Appointment Calendar | High | Not Started | Yes | Yes | Template/Automation | 02_Offers/01_BluePrint/CRM/ |  |  |
| DP-087 | GoHighLevel / CRM | Automated First Response | High | Not Started | Yes | Yes | Template/Automation | 02_Offers/01_BluePrint/CRM/ |  |  |
| DP-088 | GoHighLevel / CRM | Client Nurture Campaign | High | Not Started | Yes | Yes | Template/Automation | 02_Offers/01_BluePrint/CRM/ |  |  |
| DP-089 | GoHighLevel / CRM | Broker Nurture Campaign | High | Not Started | Yes | Yes | Template/Automation | 02_Offers/01_BluePrint/CRM/ |  |  |
| DP-090 | GoHighLevel / CRM | Past Client Referral Campaign | High | Not Started | Yes | Yes | Template/Automation | 02_Offers/01_BluePrint/CRM/ |  |  |
| DP-091 | GoHighLevel / CRM | Meeting Reminder Automation | High | Not Started | Yes | Yes | Template/Automation | 02_Offers/01_BluePrint/CRM/ |  |  |
| DP-092 | GoHighLevel / CRM | Project Brochure Send Template | High | Not Started | Yes | Yes | Template/Automation | 02_Offers/01_BluePrint/CRM/ |  |  |
| DP-093 | GoHighLevel / CRM | Review Request Automation | High | Not Started | Yes | Yes | Template/Automation | 02_Offers/01_BluePrint/CRM/ |  |  |
| DP-094 | Manuals | Master Operations Manual | Critical | Not Started | Yes | Yes | MD/PDF | 02_Offers/05_Dproperty_Franchise/Manuals/ |  |  |
| DP-095 | Manuals | Office Launch Manual | High | Not Started | Yes | Yes | MD/PDF | 02_Offers/05_Dproperty_Franchise/Manuals/ |  |  |
| DP-096 | Manuals | Daily Operating Checklist | High | Not Started | Yes | Yes | MD/PDF | 02_Offers/05_Dproperty_Franchise/Manuals/ |  |  |
| DP-097 | Manuals | Sales Playbook | Critical | Not Started | Yes | Yes | MD/PDF | 02_Offers/05_Dproperty_Franchise/Manuals/ |  |  |
| DP-098 | Manuals | Broker Playbook | High | Not Started | Yes | Yes | MD/PDF | 02_Offers/05_Dproperty_Franchise/Manuals/ |  |  |
| DP-099 | Manuals | Project Onboarding Manual | High | Not Started | Yes | Yes | MD/PDF | 02_Offers/05_Dproperty_Franchise/Manuals/ |  |  |
| DP-100 | Manuals | Finance Manual | High | Not Started | Yes | Yes | MD/PDF | 02_Offers/05_Dproperty_Franchise/Manuals/ |  |  |
| DP-101 | Manuals | Compliance Manual | Critical | Not Started | Yes | Yes | MD/PDF | 02_Offers/05_Dproperty_Franchise/Manuals/ |  |  |
| DP-102 | Manuals | Reporting Manual | High | Not Started | Yes | Yes | MD/PDF | 02_Offers/05_Dproperty_Franchise/Manuals/ |  |  |
| DP-103 | Manuals | Private Collection Manual | High | Not Started | Yes | Yes | MD/PDF | 02_Offers/05_Dproperty_Franchise/Manuals/ |  |  |
| DP-104 | Manuals | Developer Sales OS Manual | High | Not Started | Yes | Yes | MD/PDF | 02_Offers/05_Dproperty_Franchise/Manuals/ |  |  |
| DP-105 | Sales Assets | First Call Script | High | Not Started | Yes | Yes | MD/PDF/Template | 02_Offers/05_Dproperty_Franchise/Sales/ |  |  |
| DP-106 | Sales Assets | WhatsApp First Message Templates | High | Not Started | Yes | Yes | MD/PDF/Template | 02_Offers/05_Dproperty_Franchise/Sales/ |  |  |
| DP-107 | Sales Assets | Referral Introduction Message | High | Not Started | Yes | Yes | MD/PDF/Template | 02_Offers/05_Dproperty_Franchise/Sales/ |  |  |
| DP-108 | Sales Assets | Buyer Qualification Script | High | Not Started | Yes | Yes | MD/PDF/Template | 02_Offers/05_Dproperty_Franchise/Sales/ |  |  |
| DP-109 | Sales Assets | Investor Qualification Script | High | Not Started | Yes | Yes | MD/PDF/Template | 02_Offers/05_Dproperty_Franchise/Sales/ |  |  |
| DP-110 | Sales Assets | Project Presentation Script | High | Not Started | Yes | Yes | MD/PDF/Template | 02_Offers/05_Dproperty_Franchise/Sales/ |  |  |
| DP-111 | Sales Assets | Private Collection Introduction Script | High | Not Started | Yes | Yes | MD/PDF/Template | 02_Offers/05_Dproperty_Franchise/Sales/ |  |  |
| DP-112 | Sales Assets | Objection Handling Guide | High | Not Started | Yes | Yes | MD/PDF/Template | 02_Offers/05_Dproperty_Franchise/Sales/ |  |  |
| DP-113 | Sales Assets | Follow-Up Sequence | High | Not Started | Yes | Yes | MD/PDF/Template | 02_Offers/05_Dproperty_Franchise/Sales/ |  |  |
| DP-114 | Sales Assets | Closing / Reservation Script | High | Not Started | Yes | Yes | MD/PDF/Template | 02_Offers/05_Dproperty_Franchise/Sales/ |  |  |
| DP-115 | Sales Assets | Referral Request Script | High | Not Started | Yes | Yes | MD/PDF/Template | 02_Offers/05_Dproperty_Franchise/Sales/ |  |  |
| DP-116 | Sales Assets | Client Discovery Questionnaire | High | Not Started | Yes | Yes | MD/PDF/Template | 02_Offers/05_Dproperty_Franchise/Sales/ |  |  |
| DP-117 | Sales Assets | Buyer Persona Guide | High | Not Started | Yes | Yes | MD/PDF/Template | 02_Offers/05_Dproperty_Franchise/Sales/ |  |  |
| DP-118 | Sales Assets | Buying Process Visual | High | Not Started | Yes | Yes | MD/PDF/Template | 02_Offers/05_Dproperty_Franchise/Sales/ |  |  |
| DP-119 | Sales Assets | Why Buy Through Dproperty One-Pager | High | Not Started | Yes | Yes | MD/PDF/Template | 02_Offers/05_Dproperty_Franchise/Sales/ |  |  |
| DP-120 | Marketing | Franchise Launch Announcement | High | Not Started | Yes | Yes | Template/Checklist | 02_Offers/05_Dproperty_Franchise/Marketing/ |  |  |
| DP-121 | Marketing | Press Release Template | High | Not Started | Yes | Yes | Template/Checklist | 02_Offers/05_Dproperty_Franchise/Marketing/ |  |  |
| DP-122 | Marketing | LinkedIn Launch Post | High | Not Started | Yes | Yes | Template/Checklist | 02_Offers/05_Dproperty_Franchise/Marketing/ |  |  |
| DP-123 | Marketing | Instagram Launch Post Pack | High | Not Started | Yes | Yes | Template/Checklist | 02_Offers/05_Dproperty_Franchise/Marketing/ |  |  |
| DP-124 | Marketing | WhatsApp Network Announcement | High | Not Started | Yes | Yes | Template/Checklist | 02_Offers/05_Dproperty_Franchise/Marketing/ |  |  |
| DP-125 | Marketing | Email Launch Announcement | High | Not Started | Yes | Yes | Template/Checklist | 02_Offers/05_Dproperty_Franchise/Marketing/ |  |  |
| DP-126 | Marketing | Launch Event Plan | High | Not Started | Yes | Yes | Template/Checklist | 02_Offers/05_Dproperty_Franchise/Marketing/ |  |  |
| DP-127 | Marketing | 90-Day Content Calendar | High | Not Started | Yes | Yes | Template/Checklist | 02_Offers/05_Dproperty_Franchise/Marketing/ |  |  |
| DP-128 | Marketing | Paid Ads Starter Plan | High | Not Started | Yes | Yes | Template/Checklist | 02_Offers/05_Dproperty_Franchise/Marketing/ |  |  |
| DP-129 | Marketing | Local PR Checklist | High | Not Started | Yes | Yes | Template/Checklist | 02_Offers/05_Dproperty_Franchise/Marketing/ |  |  |
| DP-130 | Marketing | Website Local Office Page | High | Not Started | Yes | Yes | Template/Checklist | 02_Offers/05_Dproperty_Franchise/Marketing/ |  |  |
| DP-131 | Marketing | Google Business Profile Setup Checklist | High | Not Started | Yes | Yes | Template/Checklist | 02_Offers/05_Dproperty_Franchise/Marketing/ |  |  |
| DP-132 | Marketing | Social Media Profile Setup Checklist | High | Not Started | Yes | Yes | Template/Checklist | 02_Offers/05_Dproperty_Franchise/Marketing/ |  |  |
| DP-133 | Marketing | Marketing Budget Template | High | Not Started | Yes | Yes | Template/Checklist | 02_Offers/05_Dproperty_Franchise/Marketing/ |  |  |
| DP-134 | Training Academy | Dproperty Brand & Culture Training | High | Not Started | Yes | Yes | Training Module | 02_Offers/05_Dproperty_Franchise/Training/ |  |  |
| DP-135 | Training Academy | Dproperty OS Basics Training | High | Not Started | Yes | Yes | Training Module | 02_Offers/05_Dproperty_Franchise/Training/ |  |  |
| DP-136 | Training Academy | Client Advisory Certification | High | Not Started | Yes | Yes | Training Module | 02_Offers/05_Dproperty_Franchise/Training/ |  |  |
| DP-137 | Training Academy | Projection Certification | High | Not Started | Yes | Yes | Training Module | 02_Offers/05_Dproperty_Franchise/Training/ |  |  |
| DP-138 | Training Academy | Private Collection Certification | High | Not Started | Yes | Yes | Training Module | 02_Offers/05_Dproperty_Franchise/Training/ |  |  |
| DP-139 | Training Academy | Broker Management Certification | High | Not Started | Yes | Yes | Training Module | 02_Offers/05_Dproperty_Franchise/Training/ |  |  |
| DP-140 | Training Academy | Compliance Certification | High | Not Started | Yes | Yes | Training Module | 02_Offers/05_Dproperty_Franchise/Training/ |  |  |
| DP-141 | Training Academy | Roleplay Sales Assessment | High | Not Started | Yes | Yes | Training Module | 02_Offers/05_Dproperty_Franchise/Training/ |  |  |
| DP-142 | Training Academy | Document Workflow Assessment | High | Not Started | Yes | Yes | Training Module | 02_Offers/05_Dproperty_Franchise/Training/ |  |  |
| DP-143 | Training Academy | CRM Usage Assessment | High | Not Started | Yes | Yes | Training Module | 02_Offers/05_Dproperty_Franchise/Training/ |  |  |
| DP-144 | Training Academy | Training Progress Dashboard | High | Not Started | Yes | Yes | Training Module | 02_Offers/05_Dproperty_Franchise/Training/ |  | Yes |
| DP-145 | Training Academy | Training Video Library | High | Not Started | Yes | Yes | Training Module | 02_Offers/05_Dproperty_Franchise/Training/ |  | Yes |
| DP-146 | Training Academy | Training Quiz Bank | High | Not Started | Yes | Yes | Training Module | 02_Offers/05_Dproperty_Franchise/Training/ |  | Yes |
| DP-147 | Legal Templates - Client | Client NDA Template | Critical | Not Started | Yes | Yes | Contract/Template | 07_Legal_and_Compliance/Client_Documents/ |  |  |
| DP-148 | Legal Templates - Client | Client Onboarding Form | High | Not Started | Yes | Yes | Contract/Template | 07_Legal_and_Compliance/Client_Documents/ |  |  |
| DP-149 | Legal Templates - Client | Buyer Representation Agreement | Critical | Not Started | Yes | Yes | Contract/Template | 07_Legal_and_Compliance/Client_Documents/ |  |  |
| DP-150 | Legal Templates - Client | Investment Profile Form | High | Not Started | Yes | Yes | Contract/Template | 07_Legal_and_Compliance/Client_Documents/ |  |  |
| DP-151 | Legal Templates - Client | Reservation Process Checklist | High | Not Started | Yes | Yes | Contract/Template | 07_Legal_and_Compliance/Client_Documents/ |  |  |
| DP-152 | Legal Templates - Client | Purchase Process Checklist | High | Not Started | Yes | Yes | Contract/Template | 07_Legal_and_Compliance/Client_Documents/ |  |  |
| DP-153 | Legal Templates - Client | Projection Disclaimer | High | Not Started | Yes | Yes | Contract/Template | 07_Legal_and_Compliance/Client_Documents/ |  |  |
| DP-154 | Legal Templates - Client | Client Meeting Summary Template | High | Not Started | Yes | Yes | Contract/Template | 07_Legal_and_Compliance/Client_Documents/ |  |  |
| DP-155 | Legal Templates - Client | Client Offer Letter Template | High | Not Started | Yes | Yes | Contract/Template | 07_Legal_and_Compliance/Client_Documents/ |  |  |
| DP-156 | Legal Templates - Client | Post-Sale Handover Checklist | High | Not Started | Yes | Yes | Contract/Template | 07_Legal_and_Compliance/Client_Documents/ |  |  |
| DP-157 | Legal Templates - Broker | Broker NDA Template | Critical | Not Started | Yes | Yes | Contract/Template | 07_Legal_and_Compliance/Broker_Documents/ |  |  |
| DP-158 | Legal Templates - Broker | Broker Onboarding Form | High | Not Started | Yes | Yes | Contract/Template | 07_Legal_and_Compliance/Broker_Documents/ |  |  |
| DP-159 | Legal Templates - Broker | Referral Agreement | Critical | Not Started | Yes | Yes | Contract/Template | 07_Legal_and_Compliance/Broker_Documents/ |  |  |
| DP-160 | Legal Templates - Broker | Co-Brokerage Agreement | Critical | Not Started | Yes | Yes | Contract/Template | 07_Legal_and_Compliance/Broker_Documents/ |  |  |
| DP-161 | Legal Templates - Broker | Commission Split Agreement | Critical | Not Started | Yes | Yes | Contract/Template | 07_Legal_and_Compliance/Broker_Documents/ |  |  |
| DP-162 | Legal Templates - Broker | Non-Circumvention Template | High | Not Started | Yes | Yes | Contract/Template | 07_Legal_and_Compliance/Broker_Documents/ |  |  |
| DP-163 | Legal Templates - Broker | Project-Specific Broker Authorization | High | Not Started | Yes | Yes | Contract/Template | 07_Legal_and_Compliance/Broker_Documents/ |  |  |
| DP-164 | Legal Templates - Broker | Broker Code of Conduct | High | Not Started | Yes | Yes | Contract/Template | 07_Legal_and_Compliance/Broker_Documents/ |  |  |
| DP-165 | Legal Templates - Broker | Broker Payment Instruction Form | High | Not Started | Yes | Yes | Contract/Template | 07_Legal_and_Compliance/Broker_Documents/ |  |  |
| DP-166 | Legal Templates - Broker | Broker Termination Form | High | Not Started | Yes | Yes | Contract/Template | 07_Legal_and_Compliance/Broker_Documents/ |  |  |
| DP-167 | Legal Templates - Developer | Developer Project Intake Form | High | Not Started | No | No | Contract/Template | 07_Legal_and_Compliance/Developer_Documents/ |  |  |
| DP-168 | Legal Templates - Developer | Developer Sales OS Agreement | High | Not Started | No | No | Contract/Template | 07_Legal_and_Compliance/Developer_Documents/ |  |  |
| DP-169 | Legal Templates - Developer | Project Sales Management Agreement | High | Not Started | No | No | Contract/Template | 07_Legal_and_Compliance/Developer_Documents/ |  |  |
| DP-170 | Legal Templates - Developer | Marketing Authorization Agreement | High | Not Started | No | No | Contract/Template | 07_Legal_and_Compliance/Developer_Documents/ |  |  |
| DP-171 | Legal Templates - Developer | Developer Commission Agreement | High | Not Started | No | No | Contract/Template | 07_Legal_and_Compliance/Developer_Documents/ |  |  |
| DP-172 | Legal Templates - Developer | Exclusivity / Semi-Exclusivity Agreement | High | Not Started | No | No | Contract/Template | 07_Legal_and_Compliance/Developer_Documents/ |  |  |
| DP-173 | Legal Templates - Developer | Unit Availability Update Template | High | Not Started | No | No | Contract/Template | 07_Legal_and_Compliance/Developer_Documents/ |  |  |
| DP-174 | Legal Templates - Developer | Developer Reporting Template | High | Not Started | No | No | Contract/Template | 07_Legal_and_Compliance/Developer_Documents/ |  |  |
| DP-175 | Legal Templates - Developer | Project Information Request Checklist | High | Not Started | No | No | Contract/Template | 07_Legal_and_Compliance/Developer_Documents/ |  |  |
| DP-176 | Legal Templates - Developer | Developer Sales Team Training Agreement | High | Not Started | No | No | Contract/Template | 07_Legal_and_Compliance/Developer_Documents/ |  |  |
| DP-177 | Internal Templates | Deal Approval Checklist | High | Not Started | Yes | Yes | Template/Checklist | 02_Offers/05_Dproperty_Franchise/Internal_Templates/ |  |  |
| DP-178 | Internal Templates | Commission Approval Form | High | Not Started | Yes | Yes | Template/Checklist | 02_Offers/05_Dproperty_Franchise/Internal_Templates/ |  |  |
| DP-179 | Internal Templates | Discount Approval Form | High | Not Started | Yes | Yes | Template/Checklist | 02_Offers/05_Dproperty_Franchise/Internal_Templates/ |  |  |
| DP-180 | Internal Templates | Legal Review Request | High | Not Started | Yes | Yes | Template/Checklist | 02_Offers/05_Dproperty_Franchise/Internal_Templates/ |  |  |
| DP-181 | Internal Templates | Private Collection Approval Form | High | Not Started | Yes | Yes | Template/Checklist | 02_Offers/05_Dproperty_Franchise/Internal_Templates/ |  |  |
| DP-182 | Internal Templates | Projection Approval Form | High | Not Started | Yes | Yes | Template/Checklist | 02_Offers/05_Dproperty_Franchise/Internal_Templates/ |  |  |
| DP-183 | Internal Templates | Project Launch Approval Checklist | High | Not Started | Yes | Yes | Template/Checklist | 02_Offers/05_Dproperty_Franchise/Internal_Templates/ |  |  |
| DP-184 | Internal Templates | Franchise Compliance Checklist | High | Not Started | Yes | Yes | Template/Checklist | 02_Offers/05_Dproperty_Franchise/Internal_Templates/ |  |  |
| DP-185 | Internal Templates | Incident Report Form | High | Not Started | Yes | Yes | Template/Checklist | 02_Offers/05_Dproperty_Franchise/Internal_Templates/ |  |  |
| DP-186 | Internal Templates | Exception Approval Form | High | Not Started | Yes | Yes | Template/Checklist | 02_Offers/05_Dproperty_Franchise/Internal_Templates/ |  |  |
| DP-187 | Private Collection | Private Collection Access Rules | Critical | Not Started | Yes | Yes | MD/PDF/Template | 02_Offers/05_Dproperty_Franchise/Private_Collection/ |  |  |
| DP-188 | Private Collection | Private Collection Client Submission Form | High | Not Started | Yes | Yes | MD/PDF/Template | 02_Offers/05_Dproperty_Franchise/Private_Collection/ |  |  |
| DP-189 | Private Collection | Private Collection Deal Registration Form | High | Not Started | Yes | Yes | MD/PDF/Template | 02_Offers/05_Dproperty_Franchise/Private_Collection/ |  |  |
| DP-190 | Private Collection | Private Collection Project Deck Template | High | Not Started | Yes | Yes | MD/PDF/Template | 02_Offers/05_Dproperty_Franchise/Private_Collection/ |  |  |
| DP-191 | Private Collection | Private Collection Investment Memo Template | High | Not Started | Yes | Yes | MD/PDF/Template | 02_Offers/05_Dproperty_Franchise/Private_Collection/ |  |  |
| DP-192 | Private Collection | Private Collection FAQ Template | High | Not Started | Yes | Yes | MD/PDF/Template | 02_Offers/05_Dproperty_Franchise/Private_Collection/ |  |  |
| DP-193 | Private Collection | Private Collection Risk Disclosure | High | Not Started | Yes | Yes | MD/PDF/Template | 02_Offers/05_Dproperty_Franchise/Private_Collection/ |  |  |
| DP-194 | Private Collection | Private Collection HQ Handoff Process | Critical | Not Started | Yes | Yes | MD/PDF/Template | 02_Offers/05_Dproperty_Franchise/Private_Collection/ |  |  |
| DP-195 | Private Collection | Private Collection Commission Payment Process | High | Not Started | Yes | Yes | MD/PDF/Template | 02_Offers/05_Dproperty_Franchise/Private_Collection/ |  |  |
| DP-196 | Private Collection | Private Collection Restrictions One-Pager | High | Not Started | Yes | Yes | MD/PDF/Template | 02_Offers/05_Dproperty_Franchise/Private_Collection/ |  |  |
| DP-197 | Broker Network | Broker Recruitment Guide | Medium | Not Started | Yes | Yes | MD/Template | 02_Offers/05_Dproperty_Franchise/Broker_Network/ |  |  |
| DP-198 | Broker Network | Broker Qualification Form | Medium | Not Started | Yes | Yes | MD/Template | 02_Offers/05_Dproperty_Franchise/Broker_Network/ |  |  |
| DP-199 | Broker Network | Broker Categories | Medium | Not Started | Yes | Yes | MD/Template | 02_Offers/05_Dproperty_Franchise/Broker_Network/ |  |  |
| DP-200 | Broker Network | Broker Communication Templates | Medium | Not Started | Yes | Yes | MD/Template | 02_Offers/05_Dproperty_Franchise/Broker_Network/ |  |  |
| DP-201 | Broker Network | Broker Performance Dashboard | Medium | Not Started | Yes | Yes | MD/Template | 02_Offers/05_Dproperty_Franchise/Broker_Network/ |  |  |
| DP-202 | Broker Network | Broker Conflict Resolution Rules | Medium | Not Started | Yes | Yes | MD/Template | 02_Offers/05_Dproperty_Franchise/Broker_Network/ |  |  |
| DP-203 | Broker Network | Broker Renewal Process | Medium | Not Started | Yes | Yes | MD/Template | 02_Offers/05_Dproperty_Franchise/Broker_Network/ |  |  |
| DP-204 | Broker Network | Broker Termination Process | Medium | Not Started | Yes | Yes | MD/Template | 02_Offers/05_Dproperty_Franchise/Broker_Network/ |  |  |
| DP-205 | Project Onboarding | Developer Intake Form | High | Not Started | Yes | Yes | Template/Checklist | 02_Offers/05_Dproperty_Franchise/Project_Onboarding/ |  |  |
| DP-206 | Project Onboarding | Project Due Diligence Checklist | High | Not Started | Yes | Yes | Template/Checklist | 02_Offers/05_Dproperty_Franchise/Project_Onboarding/ |  |  |
| DP-207 | Project Onboarding | Project Data Checklist | High | Not Started | Yes | Yes | Template/Checklist | 02_Offers/05_Dproperty_Franchise/Project_Onboarding/ |  |  |
| DP-208 | Project Onboarding | Unit Inventory Template | High | Not Started | Yes | Yes | Template/Checklist | 02_Offers/05_Dproperty_Franchise/Project_Onboarding/ |  |  |
| DP-209 | Project Onboarding | Price List Template | High | Not Started | Yes | Yes | Template/Checklist | 02_Offers/05_Dproperty_Franchise/Project_Onboarding/ |  |  |
| DP-210 | Project Onboarding | Payment Plan Template | High | Not Started | Yes | Yes | Template/Checklist | 02_Offers/05_Dproperty_Franchise/Project_Onboarding/ |  |  |
| DP-211 | Project Onboarding | Commission Terms Form | High | Not Started | Yes | Yes | Template/Checklist | 02_Offers/05_Dproperty_Franchise/Project_Onboarding/ |  |  |
| DP-212 | Project Onboarding | Marketing Assets Checklist | High | Not Started | Yes | Yes | Template/Checklist | 02_Offers/05_Dproperty_Franchise/Project_Onboarding/ |  |  |
| DP-213 | Project Onboarding | Project Risk Scoring Template | High | Not Started | Yes | Yes | Template/Checklist | 02_Offers/05_Dproperty_Franchise/Project_Onboarding/ |  |  |
| DP-214 | Project Onboarding | Project Sales Argument Template | High | Not Started | Yes | Yes | Template/Checklist | 02_Offers/05_Dproperty_Franchise/Project_Onboarding/ |  |  |
| DP-215 | Project Onboarding | Project FAQ Template | High | Not Started | Yes | Yes | Template/Checklist | 02_Offers/05_Dproperty_Franchise/Project_Onboarding/ |  |  |
| DP-216 | Project Onboarding | Project Comparison Matrix | High | Not Started | Yes | Yes | Template/Checklist | 02_Offers/05_Dproperty_Franchise/Project_Onboarding/ |  |  |
| DP-217 | Finance | Commission Calculator | High | Not Started | Yes | Yes | XLSX | 06_Finance/ |  |  |
| DP-218 | Finance | Royalty Calculation Template | High | Not Started | Yes | Yes | XLSX | 06_Finance/ |  |  |
| DP-219 | Finance | Private Collection Split Calculator | High | Not Started | Yes | Yes | XLSX | 06_Finance/ |  |  |
| DP-220 | Finance | Franchise P&L Template | High | Not Started | Yes | Yes | XLSX | 06_Finance/ |  | Yes |
| DP-221 | Finance | Cash Flow Template | High | Not Started | Yes | Yes | XLSX | 06_Finance/ |  |  |
| DP-222 | Finance | Marketing Budget Template | High | Not Started | Yes | Yes | XLSX | 06_Finance/ |  |  |
| DP-223 | Finance | Break-Even Calculator | High | Not Started | Yes | Yes | XLSX | 06_Finance/ |  |  |
| DP-224 | Finance | Sales Target Calculator | High | Not Started | Yes | Yes | XLSX | 06_Finance/ |  | Yes |
| DP-225 | Finance | Owner-Operator Earnings Calculator | High | Not Started | Yes | Yes | XLSX | 06_Finance/ |  |  |
| DP-226 | Finance | Annual Budget Template | High | Not Started | Yes | Yes | XLSX | 06_Finance/ |  |  |
| DP-227 | Finance | Invoice Template | High | Not Started | Yes | Yes | XLSX | 06_Finance/ |  |  |
| DP-228 | Finance | Payment Tracker | High | Not Started | Yes | Yes | XLSX | 06_Finance/ |  |  |
| DP-229 | Compliance | Client File Checklist | High | Not Started | Yes | Yes | Checklist/MD | 02_Offers/05_Dproperty_Franchise/Compliance/ |  |  |
| DP-230 | Compliance | Broker File Checklist | High | Not Started | Yes | Yes | Checklist/MD | 02_Offers/05_Dproperty_Franchise/Compliance/ |  |  |
| DP-231 | Compliance | Deal File Checklist | High | Not Started | Yes | Yes | Checklist/MD | 02_Offers/05_Dproperty_Franchise/Compliance/ |  |  |
| DP-232 | Compliance | Advertising Compliance Rules | High | Not Started | Yes | Yes | Checklist/MD | 02_Offers/05_Dproperty_Franchise/Compliance/ |  | Yes |
| DP-233 | Compliance | Social Media Compliance Rules | High | Not Started | Yes | Yes | Checklist/MD | 02_Offers/05_Dproperty_Franchise/Compliance/ |  | Yes |
| DP-234 | Compliance | Data Privacy Rules | High | Not Started | Yes | Yes | Checklist/MD | 02_Offers/05_Dproperty_Franchise/Compliance/ |  |  |
| DP-235 | Compliance | No-Guarantee Investment Language | High | Not Started | Yes | Yes | Checklist/MD | 02_Offers/05_Dproperty_Franchise/Compliance/ |  |  |
| DP-236 | Compliance | Complaint Handling Process | High | Not Started | Yes | Yes | Checklist/MD | 02_Offers/05_Dproperty_Franchise/Compliance/ |  |  |
| DP-237 | Compliance | Monthly Compliance Report | High | Not Started | Yes | Yes | Checklist/MD | 02_Offers/05_Dproperty_Franchise/Compliance/ |  | Yes |
| DP-238 | Compliance | Quarterly Compliance Review | High | Not Started | Yes | Yes | Checklist/MD | 02_Offers/05_Dproperty_Franchise/Compliance/ |  | Yes |
| DP-239 | Compliance | HQ Audit Checklist | High | Not Started | Yes | Yes | Checklist/MD | 02_Offers/05_Dproperty_Franchise/Compliance/ |  |  |
| DP-240 | Reporting | Weekly Franchise Report | High | Not Started | Yes | Yes | Dashboard/Template | 02_Offers/05_Dproperty_Franchise/Reporting/ |  |  |
| DP-241 | Reporting | Monthly Sales Report | High | Not Started | Yes | Yes | Dashboard/Template | 02_Offers/05_Dproperty_Franchise/Reporting/ |  |  |
| DP-242 | Reporting | Monthly Royalty Report | High | Not Started | Yes | Yes | Dashboard/Template | 02_Offers/05_Dproperty_Franchise/Reporting/ |  |  |
| DP-243 | Reporting | Broker Performance Report | High | Not Started | Yes | Yes | Dashboard/Template | 02_Offers/05_Dproperty_Franchise/Reporting/ |  |  |
| DP-244 | Reporting | Marketing Performance Report | High | Not Started | Yes | Yes | Dashboard/Template | 02_Offers/05_Dproperty_Franchise/Reporting/ |  |  |
| DP-245 | Reporting | Private Collection Report | High | Not Started | Yes | Yes | Dashboard/Template | 02_Offers/05_Dproperty_Franchise/Reporting/ |  |  |
| DP-246 | Reporting | Training Completion Report | High | Not Started | Yes | Yes | Dashboard/Template | 02_Offers/05_Dproperty_Franchise/Reporting/ |  |  |
| DP-247 | Reporting | Quarterly Business Review Deck | High | Not Started | Yes | Yes | Dashboard/Template | 02_Offers/05_Dproperty_Franchise/Reporting/ |  |  |
| DP-248 | Reporting | Franchise KPI Dashboard | High | Not Started | Yes | Yes | Dashboard/Template | 02_Offers/05_Dproperty_Franchise/Reporting/ |  |  |
| DP-249 | Launch Support | Kickoff Call Agenda | High | Not Started | Yes | Yes | Checklist/Template | 02_Offers/05_Dproperty_Franchise/Launch_Support/ |  |  |
| DP-250 | Launch Support | Legal Onboarding Call Agenda | High | Not Started | Yes | Yes | Checklist/Template | 02_Offers/05_Dproperty_Franchise/Launch_Support/ |  |  |
| DP-251 | Launch Support | Brand Onboarding Call Agenda | High | Not Started | Yes | Yes | Checklist/Template | 02_Offers/05_Dproperty_Franchise/Launch_Support/ |  |  |
| DP-252 | Launch Support | Software Setup Call Agenda | High | Not Started | Yes | Yes | Checklist/Template | 02_Offers/05_Dproperty_Franchise/Launch_Support/ |  |  |
| DP-253 | Launch Support | CRM Setup Call Agenda | High | Not Started | Yes | Yes | Checklist/Template | 02_Offers/05_Dproperty_Franchise/Launch_Support/ |  |  |
| DP-254 | Launch Support | Private Collection Training Call Agenda | High | Not Started | Yes | Yes | Checklist/Template | 02_Offers/05_Dproperty_Franchise/Launch_Support/ |  |  |
| DP-255 | Launch Support | First 90-Day Business Plan Session | High | Not Started | Yes | Yes | Checklist/Template | 02_Offers/05_Dproperty_Franchise/Launch_Support/ |  |  |
| DP-256 | Launch Support | Weekly Launch Check-In Template | High | Not Started | Yes | Yes | Checklist/Template | 02_Offers/05_Dproperty_Franchise/Launch_Support/ |  |  |
| DP-257 | Launch Support | Pipeline Review Template | High | Not Started | Yes | Yes | Checklist/Template | 02_Offers/05_Dproperty_Franchise/Launch_Support/ |  |  |
| DP-258 | Launch Support | System Usage Audit | High | Not Started | Yes | Yes | Checklist/Template | 02_Offers/05_Dproperty_Franchise/Launch_Support/ |  |  |
| DP-259 | Launch Support | Launch Readiness Scorecard | High | Not Started | Yes | Yes | Checklist/Template | 02_Offers/05_Dproperty_Franchise/Launch_Support/ |  |  |
| DP-260 | HQ Readiness | Final Franchise Model | Critical | Not Started | Yes | Yes | MD/PDF/XLSX | 00_Start_Here/HQ_Readiness/ |  |  |
| DP-261 | HQ Readiness | Final Pricing Model | Critical | Not Started | Yes | Yes | MD/PDF/XLSX | 00_Start_Here/HQ_Readiness/ |  |  |
| DP-262 | HQ Readiness | Final Territory Strategy | Critical | Not Started | Yes | Yes | MD/PDF/XLSX | 00_Start_Here/HQ_Readiness/ |  |  |
| DP-263 | HQ Readiness | Franchise Selection Criteria | Critical | Not Started | Yes | Yes | MD/PDF/XLSX | 00_Start_Here/HQ_Readiness/ |  |  |
| DP-264 | HQ Readiness | Franchise Scorecard | Critical | Not Started | Yes | Yes | MD/PDF/XLSX | 00_Start_Here/HQ_Readiness/ |  |  |
| DP-265 | HQ Readiness | HQ Support SOP | Critical | Not Started | Yes | Yes | MD/PDF/XLSX | 00_Start_Here/HQ_Readiness/ |  |  |
| DP-266 | HQ Readiness | Change Control Policy | Critical | Not Started | Yes | Yes | MD/PDF/XLSX | 00_Start_Here/HQ_Readiness/ |  |  |
| DP-267 | HQ Readiness | Template Version Control Register | Critical | Not Started | Yes | Yes | MD/PDF/XLSX | 00_Start_Here/HQ_Readiness/ |  |  |
| DP-268 | HQ Readiness | Product Roadmap | Critical | Not Started | Yes | Yes | MD/PDF/XLSX | 00_Start_Here/HQ_Readiness/ |  |  |
| DP-269 | HQ Readiness | Internal Governance Charter | Critical | Not Started | Yes | Yes | MD/PDF/XLSX | 00_Start_Here/HQ_Readiness/ |  |  |

---

## 2026-09-23 Update — Canonical Reconciliation Impact

The vault's two competing canonical layers were reconciled. See [[../01_Canon/00 - Precedence and Canonical Reconciliation]]. The following deliverables changed status as a direct result.

| Deliverable | Old Status | New Status | Priority | Next Action | File Location |
|---|---|---|---|---|---|
| Canonical Reconciliation & Precedence note | Did not exist | **Created v1.0** | Critical | Esteban to ratify the 4 open items | `01_Canon/00 - Precedence and Canonical Reconciliation.md` |
| BluePrint Product Canon (folder) | Canonical v3.0 | **Amended v4.0** | Critical | Build golden workflow from it | `02_Offers/01_BluePrint/` |
| BluePrint Pricing & Packaging | $299/$599/$999 hypothesis | **$399/$799 + $1,500 setup** | Critical | Validate with design partners | `02_Offers/01_BluePrint/03 - Offer and Pricing.md` |
| BluePrint CRM Oversight and Evidence | Architecture corrected 2026-09-29 | Management reconciliation MVP | Critical | Validate read-only intake, provenance, cash variance and Glitches | `02_Offers/01_BluePrint/12 - Core Modules.md` §3 |
| BluePrint Golden Workflow spec | Superseded | **Revived — recover from git `ff84d37^`** | Critical | Recover 432 lines, strip inventory scope | `02_Offers/01_BluePrint/19 - Golden Workflow Wireframe and Validation.md` |
| BluePrint Wireframe (Developer Handoff) | Superseded | **Revived — recover from git `ff84d37^`** | High | Recover 918 lines, strip inventory scope | `02_Offers/01_BluePrint/20 - Wireframe - Back Office OS.md` |
| BluePrint Data Model | Superseded | **Revived — recover from git `ff84d37^`** | High | Recover 77 lines, strip inventory scope | `02_Offers/01_BluePrint/21 - Data Model.md` |
| CLAUDE.md AI instructions | Pre-reconciliation | **Rebuilt v2.0** | Critical | None | `CLAUDE.md` |
| AI Handoff Pack | 7 files, no precedence | **Rebuilt + new file 00** | Critical | Use new starter prompt | `00_Start_Here/AI Handoff Pack/` |
| Project Context Brief | v3.0 | **v4.0 reconciled** | Critical | None | `00_Start_Here/Project Context Brief.md` |
| Vault Manifest | v1 | **v2.0 + folder status table** | High | None | `00_Start_Here/Vault Manifest.md` |
| Current Priorities | Pre-reconciliation | **v2.0** | High | Work P0 items | `00_Start_Here/Current Priorities.md` |
| Open Questions | 6 conflicts open | **6 resolved, 3 new** | High | Ratify open items | `00_Start_Here/Open Questions.md` |
| Decision Log | Through 2026-09-20 | **+6 entries for 2026-09-23** | High | None | `00_Start_Here/Decision Log.md` |
| Master Index | Legacy filename | **Renamed + 3-layer model** | Medium | None | `00_Start_Here/Master Index.md` |
| Academy product record | Named "Building Blocks" | **Renamed to Academy; downgraded to bundled layer** | Medium | Decide if ever standalone | `19_Canonical.../03_PRODUCTS/BUILDING_BLOCKS/PRODUCT_RECORD.md` |
| 20-Unit Franchise Projection | Presented as forecast | **Marked channel model, not company SOM** | High | Resolve royalty structure | `19_Canonical.../06_FINANCE/FRANCHISING_20_UNIT_PROJECTION.md` |
| All 17 handoff files | Ready to generate | **Regenerate before external use** | High | Regenerate against canon | `12_Handoffs/` |
| Pitch Deck (Deck 1 & 2) | Ready to generate | **Blocked on ratification** | Critical | Rebuild on reconciled hierarchy | `05_Pitch_and_Investor/`, `12_Handoffs/` |
| Financial Model | v0.7 | **Blocked — rebuild on $399/$799 + $950k** | Critical | Single integrated model | `19_Canonical.../06_FINANCE/` |
| Public Site Copy (ES) | Final v1.0 | **Needs correction before reuse** | High | Fix naming + claims + economics | `10_Brand_and_Web/Public Site Copy - ES Master.md` |

### Blocked pending Esteban's ratification

1. Reconciled BluePrint definition.
2. Scale tier: exists or not, contents and price.
3. $950k / $800k envelope as the single current position.
4. Academy over Building Blocks as the commercial name.

Pitch decks and the financial model should not be rebuilt until items 1-3 are ratified.
