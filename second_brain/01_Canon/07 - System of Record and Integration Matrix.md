---
project: B_RealEstate
title: "System of Record and Integration Matrix"
type: data_governance
status: Canonical v2.0
owner: Esteban
last_updated: 2026-09-29
tags: [ecosystem, integrations, data-governance, blueprint]
---

> [!IMPORTANT] Reconciled 2026-09-23
> Precedence: [[00 - Precedence and Canonical Reconciliation]] controls this note.

# System of Record and Integration Matrix

## Rule

Each datum has a declared authority. BluePrint is not a universal writable master; it is the **management control and reconciliation layer**.

| Domain / object | Writable authority | BluePrint role |
|---|---|---|
| Leads, contacts, consent, campaigns, messages, appointments | BlankCRM / chosen CRM | Read authorized data; assess CRM usage |
| Qualification, deal stages, commercial tasks and dashboards | BlankCRM / chosen CRM | Observe completion, freshness and exceptions |
| Legal workflow, commercial compliance review, documents and approvals | BlankCRM / chosen CRM with legal/document integrations | Verify evidence; flag gaps; no execution or sign-off |
| Contracts, reservation, payment milestones, collection follow-up, closing, post-sale | BlankCRM / chosen CRM with signature/payment services | Read status and reconcile evidence; no signing, collection or closing |
| Commission rules, calculations, splits, adjustments and commercial approval | BlankCRM / chosen CRM | Verify sourced liabilities and discrepancies; no calculation authority or payout |
| Settlement / movement of funds | Bank / payment provider | Compare expected vs actual cash with provenance |
| Statutory ledger, tax and payroll | Accounting / payroll system | Read actuals and prepare management views |
| Signature evidence / immutable legal files | E-sign provider / secure legal archive | Permissioned metadata and evidence references |
| Management financial health, expected cash, expenses, budgets, forecasts and variance | BluePrint | Maintain evidence-backed management records; do not replace statutory books |
| Management KPI definitions, CRM-usage oversight, processes, Glitches | BluePrint | Observe, diagnose, govern and recommend |
| Policies, management decisions, corrective actions and executive AI recommendations | BluePrint | Govern internal management work; commercial remediation occurs in CRM |
| Verification, provenance, management audit and period close | BluePrint | Own management record; period close is not a sales closing |
| Property/project/unit inventory and listings | Developer / inventory service / authorized marketplace | Read references only |
| Marketplace access, matches, attribution and fees | VAULTED | Read permitted outcomes |
| Learning and certification activity | Building Blocks / LMS | Read evidence for management policy oversight |

## Verification hierarchy

Reported → Operationally verified → Financially verified → Closed-period/final.

## Integration principles

1. Stable external IDs.
2. No blind bidirectional sync.
3. Source and last-sync visible.
4. Discrepancies create repair/exception work.
5. Important management facts preserve evidence and provenance.
6. Independent customer tenants remain isolated from B_Franchising commercial operations.
