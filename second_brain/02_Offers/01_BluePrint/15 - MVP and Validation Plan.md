---
project: B_RealEstate
title: "BluePrint MVP and Validation Plan"
type: mvp_spec
status: Canonical v2.0
owner: Esteban
last_updated: 2026-09-23
tags: [blueprint, mvp, validation]
---

> [!IMPORTANT] Amended 2026-09-23 — transaction spine reinstated
> [[../../01_Canon/00 - Precedence and Canonical Reconciliation]] controls this folder. BluePrint's system of record now **begins at qualified opportunity** and includes the transaction file, compliance evidence, approvals, closing and **commission calculation**. The *property/project/unit inventory, listing and MLS* retirement from 2026-09-20 **stands permanently**.
>
> **Boundary in one line:** BluePrint owns *the deal as a governed management object*; it does not own *the property as inventory*.

# MVP and Validation Plan

## Objective

Do not build a full ERP. Prove one economic thesis:

> **Can one capable administrator + BluePrint run a small agency’s back office with materially less founder/manager time and fewer control failures?**

## MVP integrations

Initially: CRM (GHL first), accounting source/mock, Drive/SharePoint or file repository. Banking can be mocked/manual until secure integration is justified.

## Primary gate — the golden workflow

**One workflow must execute from qualified intake -> transaction file -> documents/compliance -> approval -> closing -> commission snapshot -> management report, with no shadow spreadsheet acting as the authority.**

This is the single most important MVP test. If the customer still keeps the real answer in Excel, the product has not landed.

## Six mandatory demo flows

### 0. Qualified deal through close and commission — **the golden workflow**
CRM marks opportunity qualified, BluePrint accepts and opens the transaction file, parties/assets attached, document and compliance checklist completed with evidence, approval policy satisfied, closing milestones recorded, commission calculated as an auditable snapshot with adjustments and payout status, flowing into the management report and audit trail.

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

Assistant, Home/Company cockpit, **Transaction Spine**, Finance Control, Processes, Glitches, Actions, Knowledge, Reports, Integrations, Audit.

## Explicitly excluded

CRM and the pre-qualification pipeline, property/project/unit **inventory**, listings, MLS, marketplace, escrow/custody/money movement, full accounting, payroll, sales-agent workspace, LMS, tax engine, generic project management.

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
- whether the commission snapshot is trusted over the spreadsheet;
- weekly usage by admin and owner.

## Kill condition

If target agencies consistently prefer a configured Odoo/GHL/accounting stack and will not pay materially for BluePrint’s opinionated management/control layer, stop or reposition before large development spend.
