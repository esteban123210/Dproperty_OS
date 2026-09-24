---
project: B_RealEstate
title: "BluePrint Architecture and System Boundaries"
type: architecture
status: Canonical v2.0
owner: Esteban
last_updated: 2026-09-23
tags: [blueprint, architecture, integrations, system-of-record]
---

> [!IMPORTANT] Amended 2026-09-23 — transaction spine reinstated
> [[../../18_Ecosystem/18 - Canonical Reconciliation and Precedence]] controls this folder. BluePrint's system of record now **begins at qualified opportunity** and includes the transaction file, compliance evidence, approvals, closing and **commission calculation**. The *property/project/unit inventory, listing and MLS* retirement from 2026-09-20 **stands permanently**.
>
> **Boundary in one line:** BluePrint owns *the deal as a governed management object*; it does not own *the property as inventory*.

# Architecture and System Boundaries

## Core architecture

```
FRONT OFFICE                    AUTHORITATIVE SYSTEMS
GHL / HubSpot / Salesforce      Accounting / Bank / E-sign / Drive
demand -> qualification         ledger / settlement / evidence
          \                         /
  qualified \                      /
 opportunity \                    /
            ---> BLUEPRINT <-------
        transaction spine + management control
                       |
        transaction file -> compliance -> approval
             -> closing -> commission snapshot
                       |
              verified management truth
                       |
        reports · processes · actions · audit · AI

NOT BluePrint: inventory / listings / MLS / escrow / custody / GL / payroll
```

## System ownership

| Domain | Primary system | BluePrint role |
|---|---|---|
| Leads, contacts, conversations, campaigns | CRM | Read selected data; reconcile for management |
| Pre-qualification pipeline / agent-entered opportunity state | CRM | Treat as reported, not automatically verified |
| **Qualified opportunity acceptance** | **BluePrint** | Own — authority begins here |
| **Transaction file / deal record** | **BluePrint** | Own |
| **Compliance checklists and evidence** | **BluePrint** | Own |
| **Approvals and approval policy** | **BluePrint** | Own |
| **Closing milestones** | **BluePrint** | Own |
| **Commission rules and calculation snapshots** | **BluePrint** | Own |
| Property/project/unit inventory, listings, MLS | Developer system / portal / VAULTED | **Not BluePrint** — reference only |
| Escrow/custody/money movement/FX | Bank / escrow provider | **Not BluePrint** — read evidence only |
| General ledger, statutory accounting | Accounting platform | Read authoritative financial events |
| Bank/payment settlement | Bank/payment provider/accounting | Read/reconcile evidence |
| Binary documents | Drive/SharePoint/legal archive | Govern metadata, location, evidence and status |
| E-signature | E-sign provider | Read envelope/signature evidence |
| Management budgets and forecast | BluePrint | Own |
| Management KPI definitions | BluePrint | Own |
| Management actions/decisions | BluePrint | Own |
| Glitches/incidents | BluePrint | Own |
| Processes/SOP/control relationships | BluePrint | Own |
| Verification state/provenance | BluePrint | Own |
| Management period close/snapshots | BluePrint | Own |
| Audit events | BluePrint | Own long-term record |
| Academy learning activity | LMS | Read relevant completion/certification |
| VAULTED marketplace | VAULTED | Separate network/GMV system |

## Authority boundary

BluePrint's authority **begins at qualified opportunity**. Everything before that belongs to the CRM. Inventory, listings and MLS never belong to BluePrint at any stage — BluePrint references the asset as a transaction participant, not as sellable stock.

## Integration rule

Never blindly synchronize two editable masters. Every field/data class has a declared authority. BluePrint can derive management interpretations but must preserve the source record and timestamp.

## GHL boundary

GHL is an excellent default front office for B_ customers. BluePrint must still work with another CRM or with limited manual imports. BluePrint should not depend on GHL-specific concepts for its internal management model.

## Accounting boundary

BluePrint must not invent accounting policy. Financial statements and statutory truth remain with the accountant/ledger. BluePrint translates verified financial data into management control: budget, variance, cash health, forecast, receivables, commission liabilities and management reporting.

## Data isolation

Independent customer tenants are isolated. B_Franchising/B_RealEstate must not gain competitive access to independent-agency customer data merely because it owns the software. Cross-tenant benchmarking must be aggregated/anonymized and contractually governed.
