---
project: B_RealEstate
title: "BluePrint Architecture and System Boundaries"
type: architecture
status: Canonical v2.0
owner: Esteban
last_updated: 2026-09-29
tags: [blueprint, architecture, integrations, system-of-record]
---

> [!IMPORTANT] Architecture corrected 2026-09-29 [D]
> BlankCRM owns full commercial execution through post-sale. BluePrint owns back-office management, financial verification, governance and intelligence; it observes the CRM without executing sales actions. See [[00 - Precedence and Canonical Reconciliation|Canonical Reconciliation and Precedence]].
>
> **Boundary in one line:** BluePrint owns the management verification record, policies and oversight; the CRM owns deal execution and commercial records.

# Architecture and System Boundaries

## Core architecture

```text
BlankCRM / chosen CRM: lead -> legal -> approval -> contract -> payment milestones
                      -> closing -> commission -> post-sale
         | authorized read events / evidence references
         v
BluePrint: observations -> verification -> cash/expense/budget reconciliation
           -> KPIs / CRM audit / Glitches -> recommendations -> management review
         ^
         | bank / accounting / signature / legal-archive evidence
```

Commercial corrections are performed by authorized teams in the CRM. BluePrint has no outbound sales-execution commands. Manual imports support CRM-independent management work.

## System ownership

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

## Authority boundary

BlankCRM executes the full commercial lifecycle: lead capture, qualification, legal workflow, approvals, contracts, payment milestones, closing, commissions, post-sale, communications, automation and commercial dashboards. BluePrint is the CRM-agnostic back-office management, governance and intelligence layer: financial health, expected vs actual cash, expenses, budgets, variance, KPI and CRM-usage oversight, process/Glitch monitoring, audit, policies, AI executive roles and management intervention. BlankCRM operates standalone. When connected, BluePrint observes, verifies, governs and recommends; authorized teams execute sales actions in BlankCRM or their chosen CRM.

## Integration rule

Never blindly synchronize two editable masters. Every field/data class has a declared authority. BluePrint can derive management interpretations but must preserve the source record and timestamp.

## GHL boundary

GHL is an excellent default front office for B_ customers. BluePrint must still work with another CRM or with limited manual imports. BluePrint should not depend on GHL-specific concepts for its internal management model.

## Accounting boundary

BluePrint must not invent accounting policy. Financial statements and statutory truth remain with the accountant/ledger. BluePrint translates verified financial data into management control: budget, variance, cash health, forecast, receivables, commission liabilities and management reporting.

## Data isolation

Independent customer tenants are isolated. B_Franchising/B_RealEstate must not gain competitive access to independent-agency customer data merely because it owns the software. Cross-tenant benchmarking must be aggregated/anonymized and contractually governed.
