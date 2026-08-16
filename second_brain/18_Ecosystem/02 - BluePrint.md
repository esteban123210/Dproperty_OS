---
project: B_RealEstate
title: "BluePrint"
type: ecosystem_component
status: Canonical v1.0
owner: Esteban
last_updated: 2026-08-16
tags: [ecosystem, platform, product]
---

# BluePrint

## Naming and lockup

**BluePrint** is the back-office platform formerly described as Dproperty OS and later given the working name Plano. In the visual wordmark, `B_` is the brand anchor and `luePrint` is underlined to continue the `B_` concept. In prose, databases, URLs and legal documents, write **BluePrint** without improvised underscore placement.

## Product definition

BluePrint is the multi-tenant back-office control plane that converts qualified real-estate opportunities into compliant, documented and financially controlled transactions while coordinating GoHighLevel, Open edX, VAULTED, Drive/SharePoint, e-signature and accounting systems.

## What it is

- Operational system of record after a lead becomes a qualified opportunity.
- Source of truth for project intelligence, units, transactions, document status, approved assumptions, projections, commissions, approvals and operational reporting.
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

1. Accept a qualified opportunity from GoHighLevel.
2. Match it to an approved project/unit or VAULTED listing.
3. Generate an approved investment projection.
4. Generate, approve, sign and index required documents.
5. Manage reservation-to-close checklists and exceptions.
6. Calculate deterministic commissions, royalties and payouts.
7. Produce agency and HQ operating reports.

## Information architecture

Primary navigation: Home · Transactions · Projects & Inventory · Documents & Compliance · Projections · Finance · Reports · Library. Team, permissions and integrations live in Settings. CRM, Academy and VAULTED are persistent launchers, not duplicated modules.

## Core data objects

Tenant, user, role, contact reference, developer, project, unit, transaction, document, template, projection, assumption set, commission, payout, approval, task, file link, integration reference and audit event.

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

Build tenant isolation, permissions, auditability and integration IDs from the beginning. Defer full HR/payroll, native CRM, native LMS, native marketplace, full accounting, advanced AI, offline mode and client portals until the transaction spine is proven.

