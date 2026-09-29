---
project: B_RealEstate
title: "BluePrint Lovable MVP Build Brief"
type: developer_handoff
status: Active prototype brief
owner: Esteban
last_updated: 2026-09-29
tags: [blueprint, lovable, prototype, handoff]
---

> [!IMPORTANT] Architecture corrected 2026-09-29 [D]
> BlankCRM owns full commercial execution through post-sale. BluePrint owns back-office management, financial verification, governance and intelligence; it observes the CRM without executing sales actions. See [[00 - Precedence and Canonical Reconciliation|Canonical Reconciliation and Precedence]].
>
> **Boundary in one line:** BluePrint owns the management verification record, policies and oversight; the CRM owns deal execution and commercial records.

# Lovable MVP Build Brief

Build a working prototype of **BluePrint**, an AI-native, chat-first management operating system for small real-estate agencies.

## Product outcome

A potential owner should immediately think:

> “I can hire one competent administrator, give them BluePrint, and run a much more professional back office without building a large management team.”

## Demo company

Use a fictional **Atria Real Estate**:
- 2 founders;
- 15 sales agents;
- 1 administrator;
- 1 marketing manager;
- external accountant.

## Main experience

Home opens as a management cockpit with:
- verified revenue;
- reported revenue;
- cash received;
- expenses;
- budget variance;
- runway;
- unresolved glitches;
- process-health warnings;
- overdue management actions;
- management budget/policy approvals needing attention (not commercial sign-off);
- prominent “Ask BluePrint” input.

The administrator’s main screen is conversational: **“What do you need?”**

## Mandatory prototype flows

1. Upload an invoice in chat → extract → classify → budget check → variance/approval → record/audit.
2. “We forgot water bottles at the event” → classify glitch → map process/SOP/control → detect recurrence → recommend action.
3. CRM says deal won → Reported; admin evidence → Operationally verified; accounting evidence → Financially verified.
4. CEO: “Why are we over budget?” → sourced management explanation.
5. “Prepare September management report” → financial/commercial/operational/process/action/risk report + executive commentary.

## Pages

Home · Assistant · Company · CRM Oversight · Finance · Processes · Glitches · Actions · Knowledge · Reports · Integrations · Audit · Settings.

## Roles

Owner/CEO; Administrator/Secretary; Finance/Accountant; Manager; Sales Agent (minimal/no full app access).

## Integrations shown in prototype

GoHighLevel, QuickBooks, Xero, Google Drive, Microsoft 365, HubSpot, Salesforce, Bank — mocked where necessary.

## Do not build

Commercial execution at any stage: legal workflow, transaction approvals, contracts/signatures, payment collection, closing, commissions or post-sale; CRM, lead marketing, funnels, property/project/unit inventory, MLS, accounting ledger, payroll, tax, property management, generic agent task management, marketplace.

## Design

Premium, calm, institutional, high-trust. Modern private-bank/consulting dashboard rather than gamified startup UI. The product should communicate: **“My company is under control.”**

## Acceptance boundary

No CRM write scopes or commands. Show expected vs actual cash and expenses separately; a pending expectation is not verified cash. CEO/CFO/COO/CMO agents propose and cite evidence. A manager requests remediation; the responsible team acts in BlankCRM/chosen CRM. Demonstrate BlankCRM functioning with BluePrint disconnected.
