---
project: B_RealEstate
title: "BluePrint"
type: ecosystem_component
status: Canonical v1.1
owner: Esteban
last_updated: 2026-08-16
tags: [ecosystem, platform, product]
---

# BluePrint

> **Controlling product documents:** [[../04_Product/BluePrint Product Map|Product Map]] · [[../04_Product/BluePrint Product Constitution|Product Constitution]] · [[../04_Product/BluePrint Golden Workflow - Wireframe and Validation|Golden Workflow]]


## Naming and lockup

**BluePrint** is the back-office platform formerly described as Dproperty OS and later given the working name Plano. In the visual wordmark, `B_` is the brand anchor and `luePrint` is underlined to continue the `B_` concept. In prose, databases, URLs and legal documents, write **BluePrint** without improvised underscore placement.

## Product definition

BluePrint is a CRM-neutral, multi-tenant back-office operating platform that converts qualified real-estate opportunities into controlled, documented and financially visible transactions while coordinating—not replacing—the specialist systems an agency already uses.

## What it is

- Operational system of record after a lead becomes a qualified opportunity or a direct intake is validated.
- Source of truth for operational intake, transactions, compliance status, document/template lineage, tasks, approvals, commission control, reports and audit events.
- Role and permission layer for HQ, branded franchises, white-label partners and developer teams.
- Launcher and coordination layer for the ecosystem's external engines.

## What it is not

- Not a CRM or marketing automation system.
- Not an LMS.
- Not an off-market marketplace.
- Not a file warehouse, e-signature provider, bank or accounting ledger.
- Not an autonomous legal or investment adviser.
- Not a generic project-management or HR suite in the MVP.

## Purpose

Remove the back-office burden that prevents a strong seller from running a reliable agency, while giving HQ enough visibility and governance to scale a multi-brand network.

## Core personas

- Franchise principal: business health, approvals, money and risk.
- Sales advisor: assigned transactions, projects, documents and next actions.
- Operations coordinator: data quality, legal checklist and closing execution.
- HQ: network governance, tenants, templates, economics and Select.
- Developer manager: project-specific sales and reporting, later phase.

## Core MVP jobs

1. Accept and normalize a qualified opportunity from GoHighLevel, another CRM, guided manual entry or CSV import.
2. Create one transaction workspace with accountable owner, next action and audit history.
3. Match the transaction to an approved/customer project or unit reference.
4. Apply compliance requirements and human-controlled gates.
5. Generate governed document drafts from approved versioned templates.
6. Coordinate human approval, external signature and closing evidence.
7. Calculate deterministic commissions, royalties and payouts.
8. Produce agency and HQ operating reports.
9. Provide the permission-aware BluePrint Copilot from MVP.

## Information architecture

Primary navigation: Home · Transactions · Projects & Inventory · Documents · Tasks & Approvals · Finance · Reports · Knowledge · Integrations · Administration. The Copilot is available globally and contextually. CRM, Academy and VAULTED remain connected products/services, not duplicated modules.

## Core data objects

Canonical entities are defined in [[../04_Product/BluePrint Product Constitution|BluePrint Product Constitution]] §7 and include tenancy/security, parties, intake, transactions, inventory, compliance, documents, work, finance, knowledge, reporting, integrations, AI and audit.

## Unit economics

BluePrint is included in the branded franchise package and bundled into white-label and developer service plans. The underlying economics must distinguish:

- recurring platform/service revenue;
- third-party per-seat or per-tenant costs;
- integration and implementation cost;
- AI usage where enabled;
- support and localization cost.

Do not publish a standalone BluePrint price until the commercial decision is recorded. See [[14 - Unit Economics Registry]].

## Success metrics

- Time to open a transaction.
- Time to generate an NDA and approved projection.
- Percentage of complete transaction files.
- Duplicate-entry rate across systems.
- Qualified-to-reserved and reserved-to-closed conversion.
- Commission forecast accuracy and ageing.
- Weekly active users by role.
- Time spent producing weekly/monthly reports.

## Build boundary

Build tenant isolation, permissions, auditability, integration IDs and the governed Copilot foundation from the beginning. Defer full HR/payroll, native CRM, native LMS, native marketplace, full accounting, advanced AI autonomy, offline mode and client portals until the transaction spine is proven.


## Three operating modes

- **Ecosystem Connected:** configured GoHighLevel handoff and optional B_RealEstate entitlements.
- **External CRM Connected:** standard API/webhook connector while the customer's CRM remains front-office source of truth.
- **BluePrint Direct:** guided form or CSV intake without adding CRM/marketing automation.

All three modes use the same Intake, Transaction, workflow states, screens, permissions and Copilot contract. See the Product Constitution §6 and Golden Workflow desk-test.

## Copilot MVP

The Copilot is included from MVP as a hyperfocused, permission-aware BluePrint assistant. It may explain/retrieve, summarize/analyze, draft from approved templates and prepare confirmed low-risk actions. It may not approve compliance, sign, pay, publish templates, waive controls or make regulated decisions.
