---
project: B_RealEstate
title: "System of Record and Integration Matrix"
type: data_governance
status: Canonical v2.0
owner: Esteban
last_updated: 2026-09-23
tags: [ecosystem, integrations, data-governance, blueprint]
---

> [!IMPORTANT] Reconciled 2026-09-23
> Precedence: [[00 - Precedence and Canonical Reconciliation]] controls this note.

# System of Record and Integration Matrix

## Rule

Each datum has a declared authority. BluePrint is not a universal writable master; it is the **management control and reconciliation layer**.

| Domain/object | Writable authority | BluePrint role |
|---|---|---|
| Leads/contacts/conversations | CRM | Reference for management |
| Campaign/source/appointments | CRM | Aggregate/interpret |
| Pre-qualification pipeline status | CRM | Treat as reported until verified |
| **Qualified opportunity acceptance** | **BluePrint** | System of record from qualification onward |
| **Transaction file / deal record** | **BluePrint** | System of record |
| **Compliance checklists and evidence** | **BluePrint** | System of record |
| **Approvals and approval policy** | **BluePrint** | System of record |
| **Closing milestones** | **BluePrint** | System of record |
| **Commission rules and calculation snapshots** | **BluePrint** | System of record |
| Property/project/unit inventory and listings | Developer system / portal / VAULTED | **Not BluePrint** — reference only |
| Escrow/custody/money movement | Bank / escrow provider | **Not BluePrint** — read evidence only |
| Accounting ledger/statutory books | Accounting platform | Read authoritative finance data |
| Bank/payment settlement | Bank/payment/accounting | Reconcile/read evidence |
| Binary documents | Drive/SharePoint/legal archive | Govern metadata/evidence/link |
| E-signature evidence | E-sign provider | Read status/timestamp/link |
| Marketplace inventory/engagement | VAULTED | Separate system |
| Course activity | Open edX/LMS | Read relevant completion |
| Management budgets | **BluePrint** | System of record |
| Management forecast/KPI definitions | **BluePrint** | System of record |
| Verification state/provenance | **BluePrint** | System of record |
| Processes/SOP/control graph | **BluePrint** | System of record |
| Operational incidents/Glitches | **BluePrint** | System of record |
| Corrective/preventive actions | **BluePrint** | System of record |
| Management actions/decisions | **BluePrint** | System of record |
| Management period snapshots/close | **BluePrint** | System of record |
| Integration discrepancies/exceptions | **BluePrint** | System of record |
| Management audit events | **BluePrint** | Long-term system of record |

## Verification hierarchy

Reported → Operationally verified → Financially verified → Closed-period/final.

## Integration principles

1. Stable external IDs.
2. No blind bidirectional sync.
3. Source and last-sync visible.
4. Discrepancies create repair/exception work.
5. Important management facts preserve evidence and provenance.
6. Independent customer tenants remain isolated from B_Franchising commercial operations.
