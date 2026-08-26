---
project: B_RealEstate
title: "Roles and Access Matrix"
type: product_spec
status: Draft v0.5
version: 0.5
owner: Esteban
last_updated: 2026-08-16
source: Claude working session 2026-07-18
tags: [product, architecture, roles, permissions, hr, ai-agents, pricing]
---

# Roles and Access Matrix

> **Precedence update (2026-08-16):** Role names remain abstract/configurable. Need-to-know access and AI-0–AI-4 authority are controlled by [[BluePrint Product Constitution]]; Golden Workflow actors and separation rules are in [[BluePrint Golden Workflow - Wireframe and Validation]].

> ## ⚠ Access boundary update — 2026-08-26 (read before using the tables below)
>
> **BluePrint is licensed and designed for administrative staff only.** Sales advisors work in GoHighLevel and **do not receive BluePrint seats**. Their time belongs with clients, not behind an internal system. This is a product boundary, not a configuration preference ([[BluePrint Product Constitution]] §3.11), and it governs seat design and pricing.
>
> A sales advisor may exist in BluePrint **as a record** — appearing in People, in team KPIs and in licence tracking — without ever having a login.
>
> The Release 1 access tiers are:
>
> | Tier | Who | Scope |
> |---|---|---|
> | **T4 — HQ / Network Admin** | HQ operations, franchise oversight | All tenants; cross-office glitch, recovery and performance patterns; template governance; tenant provisioning |
> | **T3 — Principal / C-Suite** | Office owner, director | Everything in own tenant, including confidential HR and full financial visibility |
> | **T2 — Manager** | Operations, sales or office manager | Own tenant operations; team KPIs for their team; glitch review; tasks; registries. **Not** confidential HR cases about themselves or peers |
> | **T1 — Coordinator / Secretary** | Admin coordinator, receptionist, assistant | Day-to-day: glitch logging, tasks, registries, library, directory, own personal KPIs. No team-wide financials, no HR case detail |
>
> The **Sales Advisor** row in the tables below therefore describes a **CRM** user and a BluePrint *record*, not a BluePrint login. The **Marketing Lead** row likewise describes a GoHighLevel user.
>
> Full permission matrix per surface: [[BluePrint Wireframe - Back Office OS (Developer Handoff)]] §8.


> Defines the platform hierarchy, the minimum roles a franchise office must have, where the Copilot may support human roles, the confidentiality rules, and how AI usage is priced into the plan. Companion to [[Platform Information Architecture]] and [[Platform Scenario Playbook]].
>
> **Key insight:** the roles defined here become BOTH the permission tiers in the software AND the minimum staffing requirement in the franchise agreement.

---

## Hierarchy

```
HQ (Dproperty)
├── HQ Admin / Super Admin ........... everything, all tenants
├── HQ Legal / Compliance ............ approves templates, clauses, signed docs
├── HQ Finance ....................... royalties, network fees, splits
└── HQ Private Collection Manager .... curates & assigns curated inventory
        │
        ▼  (each franchise is a tenant)
FRANCHISE OFFICE
├── Franchise Principal / Owner ...... 1 required — accountable, legal signatory
├── Sales Manager .................... optional early (Principal can wear this hat)
├── Sales Advisor / Agent ............ 1+ required — client-facing, closes deals
├── Operations / Admin Coordinator ... 1 required — documents, compliance, data hygiene
└── Marketing Lead ................... optional (can be AI + GHL)
```

**Minimum viable franchise office = 3 humans:** Principal + one Sales Advisor + one Operations Coordinator. Everything else starts as AI + HQ-shared services and is added as the office grows.

> Franchise-agreement line: *"To operate a Dproperty franchise you must maintain at minimum a Principal, a licensed Sales Advisor, and an Operations Coordinator."*

---

## Role → access summary (what each role sees)

| Role | Sees | Cannot see |
|------|------|-----------|
| HQ Admin | All tenants, all modules, all dashboards | — |
| HQ Legal/Compliance | Templates, clauses, signed docs, cases (compliance), audit log | Personal HR grievances unrelated to compliance |
| HQ Finance | Royalties, splits, invoices, payouts across network | HR grievances |
| HQ Private Collection Mgr | Curated inventory, authorized franchises, PC deals | Unrelated franchise internal data |
| Franchise Principal | Own tenant: team, clients, brokers, deals, finance, reporting, PC (approved) | Other tenants; HR grievances *about themselves* |
| Sales Manager | Team pipeline, team performance, own-tenant reporting | HQ-wide data, other tenants |
| Sales Advisor | Assigned clients, deals, tasks, docs, projections | Other advisors' private clients (unless shared), finance internals |
| Operations Coordinator | Documents, compliance checklist, data hygiene, back-office | Commission internals (unless granted) |
| Marketing Lead | CRM & Marketing, campaigns, public-site leads | Deal financials |

**Confidentiality is a property of the *case/record*, not a separate app.** An HR grievance about a Principal must hide from that Principal — visibility rules live at the record level. Build once, reuse everywhere.

---

## Human roles and AI support map

| Role / Function | Human or AI | Notes |
|---|---|---|
| Franchise Principal | **Human** | Accountability, legal signatory |
| Sales Advisor (closing) | **Human** | Relationship + legal duty; AI assists, doesn't replace |
| Ops / Compliance sign-off | **Human** | Final checks, heavily AI-assisted |
| SDR / lead qualifier | **GoHighLevel automation / human** | Front-office function outside the BluePrint Copilot; qualified handoff enters BluePrint |
| Nurture / follow-up | **GoHighLevel automation / human** | Front-office function outside the BluePrint Copilot |
| Document drafting support | **Copilot AI-2** | Uses approved versioned templates and structured inputs; output remains draft |
| Projection support | **Deterministic service + Copilot AI-1/2** | Service calculates; Copilot explains or drafts narrative; human approves where required |
| Meeting/transaction summarizer | **Copilot AI-1/3** | Summarizes immediately; proposed record actions require confirmation |
| Reporting support | **Deterministic metrics + Copilot AI-1/2** | Metrics are governed; Copilot explains and drafts narrative |
| Knowledge/training support | **Copilot AI-0/1** | Answers from authorized BluePrint/company/Academy sources with citations |
| Receipt/evidence extraction | **Copilot AI-1** | Extraction only; human validates and approves financial action |
| Ticket/glitch assistance | **Rules + Copilot AI-1/3** | Rules route; Copilot summarizes/clusters or prepares confirmed changes; humans resolve |

**The pattern:** deterministic services calculate, gate, file and route; the Copilot retrieves, explains, summarizes, drafts and prepares confirmed low-risk actions. Authorized humans approve, sign, pay, publish templates, waive controls and make regulated decisions. See [[BluePrint Product Constitution]] §11.

---

## Human vs AI — required-approval actions (always human + audit-logged)
- Approving payments, reimbursements, refunds
- Resolving disputes / grievances
- Final compliance / legal sign-off
- Hiring / firing
- Deleting data / data-governance actions
- Signing contracts

---

## How Copilot usage is priced into the plan

Three models — recommended hybrid:

1. **Seats + bundled agents (base):** each plan tier includes always-on agents (SDR, Nurture, Doc drafter). Priced into the monthly franchise/software fee. Simple, predictable.
2. **Agent add-ons:** premium agents (advanced analyst, custom sales coach) sold as monthly upsells.
3. **Usage/credit-based:** monthly AI credit pool; overage billed. Protects margin.

**Recommendation:** Base plan includes **2–3 core agents** (positioned as "a virtual team member included — worth one salary, included in your license"), premium agents as add-ons, and a **credit cap** to protect margin.

Most workflow remains deterministic. Copilot usage runs through cost-aware approved GPT routing, tenant allowances and priced overage, so assistance can increase product value without silently eroding margin. See [[BluePrint Product Constitution]] §11 and the financial model.

---

## Open items (see [[Open Questions]])
- Final default agent bundle per plan tier
- Credit cap sizing to protect margin
- Whether Sales Manager is required above N advisors
- ~~LMS choice (LearnWorlds vs edX)~~ Resolved 2026-08-16: Open edX. Hosting, SSO and role-provisioning implementation still affects Academy role setup.

## Related
- [[Platform Information Architecture]] · [[Platform Scenario Playbook]] · [[AI Layer Notes]] · [[Prototype Spec]] · [[Pricing Model]] · [[Unit Economics]]
