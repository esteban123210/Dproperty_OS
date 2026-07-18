---
project: Dproperty OS
title: "Roles and Access Matrix"
type: product_spec
status: Draft v0.5
version: 0.5
owner: Esteban
last_updated: 2026-07-18
source: Claude working session 2026-07-18
tags: [product, architecture, roles, permissions, hr, ai-agents, pricing]
---

# Roles and Access Matrix

> Defines the platform hierarchy, the minimum roles a franchise office must have, which roles are human vs AI, the confidentiality rules, and how AI agents are priced into the plan. Companion to [[Platform Information Architecture]] and [[Platform Scenario Playbook]].
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

## Human vs AI agent map

| Role / Function | Human or AI | Notes |
|---|---|---|
| Franchise Principal | **Human** | Accountability, legal signatory |
| Sales Advisor (closing) | **Human** | Relationship + legal duty; AI assists, doesn't replace |
| Ops / Compliance sign-off | **Human** | Final checks, heavily AI-assisted |
| SDR / Lead qualifier | **AI agent (T1)** | First response, qualify, book calls (via GHL) |
| Nurture / follow-up | **AI agent (T1)** | Sequences, reminders, re-engagement |
| Document drafter | **AI agent (T1)** | Fills approved templates → human approves |
| Projection drafter | **AI agent (T1)** | Within HQ-locked assumptions → human approves |
| Meeting summarizer / CRM updater | **AI agent (T1)** | Notes, data entry, next-actions |
| Reporting analyst | **AI agent (T1)** | Weekly dashboards, alerts |
| Training coach | **AI agent (T1)** | Onboarding Q&A, role-play partner |
| Receipt reader (reimbursements) | **AI agent (T1)** | Extraction only; human approves payment |
| Ticket categorizer / glitch clustering | **AI agent (T1)** | Routing only; humans resolve |

**The pattern:** AI does the volume work up to the approval line; a human crosses it. Consistent with [[AI Layer Notes]]: AI drafts and operates; humans approve anything legal, financial, or client-facing. **AI never calculates, approves, pays, deletes, files, or routes.**

---

## Human vs AI — required-approval actions (always human + audit-logged)
- Approving payments, reimbursements, refunds
- Resolving disputes / grievances
- Final compliance / legal sign-off
- Hiring / firing
- Deleting data / data-governance actions
- Signing contracts

---

## How AI agents are priced into the plan

Three models — recommended hybrid:

1. **Seats + bundled agents (base):** each plan tier includes always-on agents (SDR, Nurture, Doc drafter). Priced into the monthly franchise/software fee. Simple, predictable.
2. **Agent add-ons:** premium agents (advanced analyst, custom sales coach) sold as monthly upsells.
3. **Usage/credit-based:** monthly AI credit pool; overage billed. Protects margin.

**Recommendation:** Base plan includes **2–3 core agents** (positioned as "a virtual team member included — worth one salary, included in your license"), premium agents as add-ons, and a **credit cap** to protect margin.

Because ~85% of platform work is T0 (free automation) and T1 runs on cheap/local models (DeepSeek local), **AI is a sales weapon, not a feared cost line.** Flows into [[Pricing Model]] and [[Unit Economics]].

---

## Open items (see [[Open Questions]])
- Final default agent bundle per plan tier
- Credit cap sizing to protect margin
- Whether Sales Manager is required above N advisors
- LMS choice (LearnWorlds vs edX) affects Academy role provisioning

## Related
- [[Platform Information Architecture]] · [[Platform Scenario Playbook]] · [[AI Layer Notes]] · [[Prototype Spec]] · [[Pricing Model]] · [[Unit Economics]]
