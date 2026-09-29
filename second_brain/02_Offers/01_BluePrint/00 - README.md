---
project: B_RealEstate
title: "BluePrint — Offer README"
type: offer_readme
status: Canonical — build priority
owner: Esteban
last_updated: 2026-09-29
tags: [offer, readme, blueprint]
---

> [!IMPORTANT] Start here
> Precedence: [[../../01_Canon/00 - Precedence and Canonical Reconciliation]] · Portfolio: [[../../01_Canon/04 - Offer Portfolio Map]] · Architecture: [[../../00_Start_Here/Vault Architecture Map]]

# BluePrint

**Type:** **Product** — proprietary core SaaS/IP. This is where the moat is.
**Job:** Be the whole back office of a company that has no management layer.
**Price:** Core **$399**/mo · Growth **$799**/mo · **$1,500** setup, per organization/office (never per agent seat). Scale tier quoted, undefined. `[A]`
**Status:** Specification complete. **Current build priority.** The agentic C-suite is the product **thesis, not built software** — all `[T]`.

> **BluePrint is an agentic back office. It gives a small, sales-led company a CEO, CFO, COO and CMO in one place — without the cost of hiring an actual C-suite.**

**The problem, precisely.** A CRM standardizes pipelines, computes commission splits and holds documents — it does those well. But its output is only as good as the discipline of the people feeding it, and those are the same people paid on what it reports. Deals get marked Won early or misclassified, so **CRM revenue does not reconcile with what accounting processed, nor with real receivables.** Good CRM usage is the CRM's own main dependency.

**BluePrint depends on no one's discipline.** Two rules define it:

1. **Nothing is recorded without evidence** — no receipt, invoice, contract or bank proof, no record.
2. **Agents manage, not just report** — they detect, explain, suggest and escalate.

**Repositioned 2026-09-25.** The earlier "transaction spine from qualified opportunity" framing claimed a differentiator a CRM already provides. See [[../../01_Canon/22 - BluePrint Repositioned - Agentic Back Office]].

**Boundary in one line:** BluePrint owns the **evidence-backed record and the management intelligence on top of it**. It does not own the deal workflow, and it does not own the property as inventory.

## What it owns

**The agentic C-suite**

| Agent | What it does |
|---|---|
| **CFO** | Evidence-backed entries only. Classifies invoices to P&L and budget line, applies accounting treatment, can push to the accounting system. Cash, receivables, variance. |
| **COO** | The **Glitch Report**. Finds which process step always fails and who fails most. Suggests process, team and training changes. Operating KPIs. |
| **CEO** | Verified company position — what needs attention, what decision is pending, and why. |
| **CMO** | **Reads the CRM** and reports whether sales execution matches management goals. |
| **Auditor** | Continuous audit trail, period close, due-diligence ready. |

**Verified financial truth** — evidence-backed records, classification, cash, receivables, commission liability, variance, period close.

**Process intelligence** — process/SOP registry, Glitch Report, root cause, recurrence, corrective actions, process health.

**Management layer** — actions, approvals, decisions, KPI definitions, reporting, long-term audit.

**Company knowledge** — governed manuals, policies, templates, contacts, institutional memory.

**The CRM audit** — reads the front office and reports alignment to management goals.

## What it does NOT own

Leads, marketing automation and the **full commercial lifecycle** (→ BlankCRM) · property/project/unit **inventory**, listings, MLS · **the general ledger of record**, tax filing, payroll (→ accounting) · property management · course delivery (→ Building Blocks) · marketplace listings (→ VAULTED) · escrow, custody, money movement, FX · the sales-agent prospecting workspace.

**CRM-agnostic by design** — must work with GoHighLevel, HubSpot, Salesforce or manual intake.

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
- Validate CRM Oversight and Evidence, expected-vs-actual cash and Glitch management against the corrected module and MVP specifications.
- No paid external validation. Willingness to pay at $399/$799 is `[A]`.
- **The ICP floor moved to two people, but pricing was modelled on a ~30-person agency.** Whether a two-person team supports $399/month is `[R]` unvalidated.
- **The Glitch Report is the adoption risk.** People do not enjoy logging their own failures, and it is the dataset every agent depends on.
- **How much accounting treatment can BluePrint apply before it needs a licensed accountant?** `[R]`

## It makes the business sellable

If the operator ever wants to sell the business or the franchise, BluePrint hands over an **ongoing managed operation** — current financial reporting, clean accounting, documented processes, audit trail, management history. A two-person agency with that is worth materially more than one whose records live in the founder's head.

**This is an exit-value argument, not only an efficiency argument** — and it is the strongest argument in a franchise sale.

## Product test

**If BluePrint does not deliver material value to an agency that already has a good CRM and competent accounting software, the product thesis fails.**

Re-read that whenever scope creeps toward rebuilding a CRM or an ERP.

## Next gate

Prototype the two golden flows — **(a) glitch reported by chat → process match → recurrence detected → suggested fix**, and **(b) invoice sent by chat → classified to P&L and budget → management report** — then 5 design partners and 3 paid conversions.

**Pass condition:** the workflow runs with **no shadow spreadsheet acting as the authority**.

**Kill condition:** target agencies consistently prefer a configured Odoo/GHL/accounting stack and will not pay materially for the opinionated management/control layer.
