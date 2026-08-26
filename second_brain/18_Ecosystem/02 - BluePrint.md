---
project: B_RealEstate
title: "BluePrint"
type: ecosystem_component
status: Canonical v2.0
owner: Esteban
last_updated: 2026-08-26
tags: [ecosystem, platform, product, backoffice, glitch-report]
---

# BluePrint

> **Controlling product documents:** [[../04_Product/BluePrint Product Map|Product Map]] · [[../04_Product/BluePrint Product Constitution|Product Constitution]] · [[../04_Product/BluePrint Wireframe - Back Office OS (Developer Handoff)|Release 1 Wireframe]] · [[../04_Product/BluePrint Golden Workflow - Wireframe and Validation|Release 2 Golden Workflow]]

> **v2.0 — 2026-08-26.** BluePrint is the back-office brain for administrative staff only; the sales team works in GoHighLevel. Delivery is sequenced: **Release 1 = Back Office Brain**, **Release 2 = Transaction Spine**. See Product Constitution §9.


## Naming and lockup

**BluePrint** is the back-office platform formerly described as Dproperty OS and later given the working name Plano. In the visual wordmark, `B_` is the brand anchor and `luePrint` is underlined to continue the `B_` concept. In prose, databases, URLs and legal documents, write **BluePrint** without improvised underscore placement.

## Product definition

BluePrint is a CRM-neutral, multi-tenant platform that acts as the **operating brain of a lean real-estate back office** — the place where the office's institutional knowledge, daily operating rhythm, obligations, people records, approved materials and honest performance information live — while coordinating, never replacing, the specialist systems the agency already uses. From Release 2 it also converts qualified opportunities into controlled, documented and financially visible transactions.

## What it is

- The daily operating rhythm of the office, anchored by the Glitch Report service-recovery review.
- The tracked register of everything with an owner and an expiry: contracts, corporate and software licences, tax obligations, professional licences, people records.
- The governed library of approved templates and operating manuals, and the directory of external parties the office depends on.
- The confidential engine for HR cases and internal tickets.
- The honest performance layer: personal and team KPIs, satisfaction results, management reports, each with declared provenance.
- Role and permission layer for HQ, branded franchises, white-label partners and developer teams.
- Launcher and coordination layer for the ecosystem's external engines.
- From Release 2: operational system of record for intake, transactions, compliance, documents, approvals and commission control.

## What it is not

- Not a CRM or marketing automation system.
- **Not a tool for the sales team.** Sales advisors work in GoHighLevel and receive no BluePrint seat; a salesperson may exist in BluePrint as a *record* without a login.
- Not an LMS.
- Not an off-market marketplace.
- Not a file warehouse, e-signature provider, bank, payroll processor or accounting ledger.
- Not the legal archive — it tracks status, expiry and ownership; signed documents live in the secure archive.
- Not an autonomous legal or investment adviser.

## Purpose

Ensure nothing important lives only in one person's head or one person's inbox — removing the back-office burden that prevents a strong seller from running a reliable agency, while giving HQ enough visibility and governance to scale a multi-brand network and hold a measurable service standard across it.

## Core personas

- **Coordinator / secretary:** the daily driver — glitch logging, tasks, registries, library, directory.
- **Operations or office manager:** data quality, obligations, team performance, glitch review.
- **Franchise principal / C-suite:** business health, approvals, confidential HR, money and risk.
- **HQ:** network governance, tenants, templates, economics, Select, and cross-office service quality.
- Sales advisor and developer manager appear as *records and metrics*, not as BluePrint users.

## Core Release 1 jobs

1. Report a service glitch from anywhere in under twenty seconds, no blame attached.
2. Run the daily service-recovery review; roll unrecovered items forward until they are put right.
3. Surface patterns across glitches so root causes get fixed, not just incidents.
4. Track every contract, licence, permit and tax obligation with owner, expiry and automatic renewal alerts.
5. Hold team records, professional licence expiry, employment terms and document links.
6. Route confidential HR cases and complaints, including anonymous submission.
7. Govern approved templates and operating manuals with version, owner and review date.
8. Keep the directory of accountants, lawyers, authorities, suppliers and wellbeing services.
9. Report personal and team performance with declared provenance for every number.
10. Provide the permission-aware BluePrint Copilot across all of the above.

Release 2 adds intake, transaction workspace, compliance gates, document generation, signature handoff, commissions and transaction reporting.

## Information architecture

Release 1 navigation: **Today · Glitches · Tasks · Performance · People · Legal · Library · Directory · Administration.** Command Bar, Report a Glitch and the Copilot are present on every screen. Release 2 adds Transactions, Documents and Finance to the same shell.

CRM, Academy and VAULTED appear only as marked launch links (SSO, new tab). They are never rendered inside BluePrint — see the non-duplication rendering rule in Product Constitution §2.

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

**Release 1**
- Daily Review held on consecutive working days — the adoption measure.
- Glitch recovery rate and median time to recovery.
- Glitch reporting rate per person, watched for a healthy floor and never penalised.
- Renewals discovered late: target zero.
- Registry currency — records with a valid owner and review date.
- Time to find an approved template, manual section or contact.
- Weekly active users by role.

**Release 2**
- Time to open a transaction · time to generate an NDA and approved projection · percentage of complete transaction files · duplicate-entry rate across systems · qualified-to-reserved and reserved-to-closed conversion · commission forecast accuracy and ageing · time spent producing weekly/monthly reports.

## Build boundary

Build tenant isolation, permissions, record-level confidentiality, auditability, integration IDs and the governed Copilot foundation from the beginning, **at full strength in Release 1** — this foundation is shared with Release 2 and shortcutting it converts Release 2 into a rewrite.

Build the two primitives once: **Registry** (tracked record with owner, status, expiry, renewal rules, external links) and **Ticket** (reported item with routing, SLA, confidentiality, resolution). Most Release 1 surfaces are configurations of these.

Defer payroll processing, native CRM, native LMS, native marketplace, full accounting, clinical/EAP content, advanced AI autonomy, offline mode, mobile-native apps and client portals indefinitely. Defer the transaction spine to Release 2 and the GoHighLevel metrics connector to Release 1.5.


## Three operating modes *(Release 2 — designed into the Release 1 foundation, not built in it)*

- **Ecosystem Connected:** configured GoHighLevel handoff and optional B_RealEstate entitlements.
- **External CRM Connected:** standard API/webhook connector while the customer's CRM remains front-office source of truth.
- **BluePrint Direct:** guided form or CSV intake without adding CRM/marketing automation.

All three modes use the same Intake, Transaction, workflow states, screens, permissions and Copilot contract. See the Product Constitution §6 and Golden Workflow desk-test.

## Copilot

The Copilot is included from Release 1 as a hyperfocused, permission-aware BluePrint assistant over manuals, registries, people records and metrics. It may explain/retrieve, summarize/analyze, draft from approved templates and prepare confirmed low-risk actions. It may not approve compliance, sign, pay, publish templates, waive controls or make regulated decisions.
