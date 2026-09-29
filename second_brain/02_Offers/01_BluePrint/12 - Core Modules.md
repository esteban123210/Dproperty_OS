---
project: B_RealEstate
title: "BluePrint Core Modules"
type: capability_map
status: Canonical v2.0
owner: Esteban
last_updated: 2026-09-29
tags: [blueprint, modules, product]
---

> [!IMPORTANT] Architecture corrected 2026-09-29 [D]
> BlankCRM owns full commercial execution through post-sale. BluePrint owns back-office management, financial verification, governance and intelligence; it observes the CRM without executing sales actions. See [[00 - Precedence and Canonical Reconciliation|Canonical Reconciliation and Precedence]].
>
> **Boundary in one line:** BluePrint owns the management verification record, policies and oversight; the CRM owns deal execution and commercial records.

# Core Modules

BluePrint is organized around management jobs, not generic ERP modules.

## 1. Assistant
Primary chat-first interface. Search, upload, classify, create, ask, prepare, report and initiate governed actions.

## 2. Company / Management Cockpit
Company health, verified vs reported numbers, attention queue, risks, approvals and decisions.

## 3. CRM Oversight and Evidence

Read authorized lifecycle events from BlankCRM or another CRM. Keep source IDs, timestamps, evidence links and reported/verified status. Detect stale stages, missing approvals, incomplete legal evidence and commission/payment discrepancies. Recommend corrective action to the responsible team; execution remains in the CRM. No transaction workspace, sales stage editor, signing, closing or commission execution.

## 4. Finance Control
Budgets, actual vs budget, management forecast, cash overview, verified revenue/receivables, recurring costs, commission liabilities and management P&L views. No statutory ledger.

## 5. Processes
Process registry, SOPs, controls, owners, KPIs, checklists, versions, evidence and process health.

## 6. Glitches
Operational incidents, severity, root cause, process link, recurrence, financial/time impact, corrective/preventive actions and closure evidence.

## 7. Management Actions
Executive/operations tasks, strategic initiatives, corrective actions, board commitments, approvals and decisions. Not sales-agent follow-up.

## 8. Knowledge
Governed manuals, policies, template metadata, employee/company records and links to binary files.

## 9. Reports
Weekly operating report, monthly management report, financial-health report, process-health report, glitch analysis and QBR.

## 10. Integrations & Reconciliation
Connection status, last sync, discrepancy queue, source authority and repair workflow.

## 11. Audit & Period Close
Change history, approvals, evidence, immutable/snapshot reporting and period adjustments.

## Navigation

**Home · Assistant · Company · CRM Oversight · Finance · Processes · Glitches · Actions · Knowledge · Reports · Integrations · Audit · Settings**

## Executive intelligence roles [T]

CEO: priorities, company health and management intervention. CFO: expected vs actual cash, expenses, budgets, variance and liability reconciliation. COO: process health, Glitches, corrective actions and recurrence. CMO: campaign and CRM-usage oversight. Each cites evidence, marks uncertainty and proposes management action. Commercial approval, signature, collection, closing and commission execution remain outside BluePrint.
