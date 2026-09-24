---
project: B_RealEstate
title: "BluePrint — Offer README"
type: offer_readme
status: Canonical — build priority
owner: Esteban
last_updated: 2026-09-23
tags: [offer, readme, blueprint]
---

> [!IMPORTANT] Start here
> Precedence: [[../../01_Canon/00 - Precedence and Canonical Reconciliation]] · Portfolio: [[../../01_Canon/04 - Offer Portfolio Map]] · Architecture: [[../../00_Start_Here/Vault Architecture Map]]

# BluePrint

**Type:** **Product** — proprietary core SaaS/IP. This is where the moat is.
**Job:** Run and control the company.
**Price:** Core **$399**/mo · Growth **$799**/mo · **$1,500** setup, per organization/office (never per agent seat). Scale tier quoted, undefined. `[A]`
**Status:** Specification complete. **Current build priority.** No paid external validation yet.

BluePrint is a chat-first, AI-native management operating system for small and growing real-estate agencies, **whose system of record is the verified transaction, commission and management-control record, beginning at qualified opportunity.**

The 2026-09-23 reconciliation merged two competing definitions: the management-control layer (2026-09-20) and the transaction spine (2026-09-23). Both are now true. The *property/unit inventory and MLS* ambition stays permanently retired.

**Boundary in one line:** BluePrint owns *the deal as a governed management object*; it does not own *the property as inventory*.

## What it owns

**Transaction spine — the wedge, from qualified opportunity onward**
qualified-opportunity intake · transaction file · parties/assets as transaction participants · documents, compliance checklists, retention · approval policies and e-signature evidence · reservation/contract milestones and closing · commission rules, calculation snapshots, adjustments, receivable/payout status

**Management control**
management truth and verification · budgets, forecast, variance · KPIs and reports · processes/SOPs/controls and process health · Glitches, root causes, corrective actions · management actions, approvals, decisions · governed company knowledge · reconciliation/exception queues · period close · long-term audit trail · permission-grounded Copilot

## What it does NOT own

Leads, marketing automation and the **pre-qualification** pipeline (→ BlankCRM) · property/project/unit **inventory**, listings, MLS · general ledger, tax, payroll (→ accounting) · property management · LMS delivery (→ Academy) · marketplace listings and matching (→ VAULTED) · escrow, custody, money movement, FX · sales-agent prospecting workspace

## Files in this folder

| File | What it is |
|---|---|
| `01 - Definition and Boundaries` | Canonical definition and hard boundaries |
| `02 - ICP and Jobs To Be Done` | Who buys, who operates, the economic job |
| `03 - Offer and Pricing` | Tiers, setup fee, value logic, metrics to validate |
| `04 - Product Record` | Modules, BMC, MVP acceptance, roadmap |
| `07 - Investor Two-Pager` | Comparable investor summary |
| `10 - Product Constitution` | Binding promise, non-goals, principles |
| `11 - Architecture and System Boundaries` | CRM vs accounting vs BluePrint; integration rules |
| `12 - Core Modules` | What the product contains |
| `13 - Data Trust Audit and Process Assurance` | Verification states, audit, Glitches, process health |
| `14 - Chat First AI Operating Model` | Conversational UX over structured records |
| `15 - MVP and Validation Plan` | What to build first; what must be proven |
| `16 - Competitive Positioning - GHL Odoo SAP` | Why this is not another CRM/ERP |
| `17 - Lovable MVP Build Brief` | Prototype/developer handoff |
| `18 - Decision Record - 2026-09-20` | Why the product was redefined (now amended) |
| `19 - Golden Workflow Wireframe and Validation` | The wedge workflow |
| `20 - Wireframe - Back Office OS` | Developer handoff wireframe |
| `21 - Data Model` | Entities and relationships |
| `22 - Platform Information Architecture` | Navigation and IA |
| `23 - Platform Scenario Playbook` | Worked operating scenarios |
| `24 - Prototype Control Note` | Prototype status and control |

## Gaps — genuine, not placeholders

- **`05 - Economics.md` missing.** BluePrint COGS (AI/integration/support per tenant) and gross margin are not modelled here. Summary lives in `06_Finance/Pricing Unit Economics and Revenue Policy.md`.
- **`06 - Legal.md` missing.** No SaaS terms, DPA, SLA or IP-ownership note exists yet. `[R]` Required before any paid pilot.
- **Transaction-spine module spec not yet written into `12 - Core Modules`** at the same depth as the management modules. The reconciliation reinstated it; the module detail is still thin.
- No paid external validation. Willingness to pay at $399/$799 is `[A]`.

## Product test

**If BluePrint does not deliver material value to an agency that already has a good CRM and competent accounting software, the product thesis fails.**

That is the sentence to re-read whenever scope creeps toward rebuilding a CRM or an ERP.

## Next gate

Prototype the golden workflow — **qualified intake → transaction file → documents/compliance → approval → closing → commission snapshot → management report** — then 5 design partners and 3 paid conversions.

**Pass condition:** the workflow runs with **no shadow spreadsheet acting as the authority**.

**Kill condition:** target agencies consistently prefer a configured Odoo/GHL/accounting stack and will not pay materially for the opinionated management/control layer.
