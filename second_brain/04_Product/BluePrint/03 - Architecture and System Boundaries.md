---
project: B_RealEstate
title: "BluePrint Architecture and System Boundaries"
type: architecture
status: Canonical v1.0
owner: Esteban
last_updated: 2026-09-20
tags: [blueprint, architecture, integrations, system-of-record]
---

# Architecture and System Boundaries

## Core architecture

```
FRONT OFFICE                    AUTHORITATIVE SYSTEMS
GHL / HubSpot / Salesforce      Accounting / Bank / E-sign / Drive
          \                         /
           \                       /
            ---> BLUEPRINT <-------
                 management control layer
                       |
              verified management truth
                       |
        reports · processes · actions · AI
```

## System ownership

| Domain | Primary system | BluePrint role |
|---|---|---|
| Leads, contacts, conversations, campaigns | CRM | Read selected data; reconcile for management |
| Sales pipeline / agent-entered opportunity state | CRM | Treat as reported, not automatically verified |
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

## Integration rule

Never blindly synchronize two editable masters. Every field/data class has a declared authority. BluePrint can derive management interpretations but must preserve the source record and timestamp.

## GHL boundary

GHL is an excellent default front office for B_ customers. BluePrint must still work with another CRM or with limited manual imports. BluePrint should not depend on GHL-specific concepts for its internal management model.

## Accounting boundary

BluePrint must not invent accounting policy. Financial statements and statutory truth remain with the accountant/ledger. BluePrint translates verified financial data into management control: budget, variance, cash health, forecast, receivables, commission liabilities and management reporting.

## Data isolation

Independent customer tenants are isolated. B_Franchising/B_RealEstate must not gain competitive access to independent-agency customer data merely because it owns the software. Cross-tenant benchmarking must be aggregated/anonymized and contractually governed.
