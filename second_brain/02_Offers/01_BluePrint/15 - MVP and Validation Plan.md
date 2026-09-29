---
project: B_RealEstate
title: "BluePrint MVP and Validation Plan"
type: mvp_spec
status: Canonical v2.0
owner: Esteban
last_updated: 2026-09-29
tags: [blueprint, mvp, validation]
---

> [!IMPORTANT] Architecture corrected 2026-09-29 [D]
> BlankCRM owns full commercial execution through post-sale. BluePrint owns back-office management, financial verification, governance and intelligence; it observes the CRM without executing sales actions. See [[00 - Precedence and Canonical Reconciliation|Canonical Reconciliation and Precedence]].
>
> **Boundary in one line:** BluePrint owns the management verification record, policies and oversight; the CRM owns deal execution and commercial records.

# MVP and Validation Plan

## Objective

Do not build a full ERP. Prove one economic thesis:

> **Can one capable administrator + BluePrint run a small agency’s back office with materially less founder/manager time and fewer control failures?**

## MVP integrations

Initially: CRM (GHL first), accounting source/mock, Drive/SharePoint or file repository. Banking can be mocked/manual until secure integration is justified.

## Primary gate — the golden workflow

**One workflow must execute from CRM evidence intake -> verification -> expected vs actual cash -> variance/Glitch -> recommendation -> review -> management report, with no shadow spreadsheet acting as the authority.**

This is the single most important MVP test. If the customer still keeps the real answer in Excel, the product has not landed.

## Six mandatory demo flows

### 0. Independent execution plus management verification

The pilot completes lead capture through legal, approvals, contract, payment milestones, closing, commission and post-sale in BlankCRM with BluePrint disconnected. Then BluePrint reads those events, compares reported outcomes with legal/bank/accounting evidence, reconciles expected vs actual cash and commissions payable, detects a discrepancy, and proposes a management intervention. The authorized team repairs the source in BlankCRM; BluePrint re-verifies. Repeat with a non-GHL import to prove CRM independence.

### 1. Invoice through chat
Upload → extract → classify → budget check → variance → approval if required → structured record → audit → dashboard update.

### 2. Glitch through chat
Free text → incident → process/SOP/control match → recurrence → corrective action → process-health update.

### 3. CRM claim vs verified truth
CRM reports deal won → BluePrint marks Reported → admin evidence → Operationally verified → accounting evidence → Financially verified.

### 4. CEO management question
“Why are we over budget?” → sourced explanation with underlying records and confidence/provenance.

### 5. Monthly management close/report
Finance + commercial + operations + process health + actions + risks + AI commentary → review → close period.

## MVP modules

Assistant, Home/Company cockpit, **CRM Oversight and Evidence**, Finance Control, Processes, Glitches, Actions, Knowledge, Reports, Integrations, Audit.

## Explicitly excluded

Commercial execution at every stage, property/project/unit **inventory**, listings, MLS, marketplace, escrow/custody/money movement, full accounting, payroll, sales-agent workspace, LMS, tax engine, generic project management.

## Validation gate before major custom build

Interview 10–20 agencies; recruit **5 design partners**; obtain **3 paid conversions**.

Also required: tenant isolation and permission tests pass; implementation under 40 hours initially, trending under 20; median calendar time under 21 days; weekly active target users above 60%; critical workflow completion above 70% by month 9; no severity-1 security issue.

Measure:
- founder management hours saved;
- admin training time;
- reporting preparation time;
- number of discrepancies detected;
- recurring glitches/process failures identified;
- time to find/record information;
- willingness to pay at $399/$799 + $1,500 setup;
- whether the reconciled management cash/liability view is traceable to CRM and accounting evidence;
- weekly usage by admin and owner.

## Kill condition

If target agencies consistently prefer a configured Odoo/GHL/accounting stack and will not pay materially for BluePrint’s opinionated management/control layer, stop or reposition before large development spend.
