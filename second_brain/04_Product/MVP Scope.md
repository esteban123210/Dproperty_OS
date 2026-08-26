---
project: B_RealEstate
title: "MVP Scope"
type: product_note
status: "Canonical summary v2.0"
version: 2.0
owner: Esteban
last_updated: 2026-08-26
source: BluePrint Product Constitution v2.0 §9
tags: [product, blueprint, mvp, release-plan]
---

# BluePrint Release Scope

> **Control:** Full boundary: [[BluePrint Product Constitution]] §9. Release 1 build spec and acceptance criteria: [[BluePrint Wireframe - Back Office OS (Developer Handoff)]]. Release 2 spec: [[BluePrint Golden Workflow - Wireframe and Validation]]. This file is the compact summary.

> **v2.0 change (2026-08-26).** v1.0 defined a single MVP built around the transaction spine. The founder pain assessment established that the office's real daily pain is back-office administration, not transaction control. Scope is now sequenced. **Nothing was cancelled — the order changed.**

## Release 1 — The Back Office Brain

**Outcome:** the office runs its day from BluePrint.

**Foundation (full strength, not deferrable):** multi-tenancy · authentication · roles · record-level access · confidentiality tiers · immutable audit · base entity conventions · design system.

**Two primitives, built once:**
- **Registry** — a tracked record with owner, status, expiry, renewal rules and links to files stored elsewhere.
- **Ticket** — a reported item with routing, SLA, confidentiality and resolution.

**Surfaces (mostly configurations of the two primitives):**

| Surface | Built from |
|---|---|
| Glitch Report — report, daily review, pattern dashboard | Ticket |
| Tasks with provenance back to the originating record | Task engine |
| Legal & assets — contracts, corporate licences, software licences, taxes, renewal calendar | Registry |
| People — team records, professional licences, employment terms; confidential HR cases; wellbeing links | Registry + Ticket |
| Library — approved templates and operating manuals, versioned and review-dated; Academy link-outs | Registry |
| Directory — accountants, lawyers, authorities, suppliers, useful sites | Registry |
| Performance — metric definitions, native metrics, surveys, personal and team dashboards, CSV bridge for CRM metrics | Metric engine |
| Copilot across all of the above | Constitution §11 |
| Administration — users, permissions, metric definitions, integrations, audit viewer | — |

## Release 1.5

GoHighLevel metrics connector replaces the CSV bridge, feeding the **same** metric definitions and dashboards. Satisfaction survey automation.

## Release 2 — The Transaction Spine

Intake across all three CRM modes → transaction workspace → compliance gates → governed document generation → approval → e-signature handoff → closing → deterministic commission → transaction reporting.

Constitution §6 (CRM modes) and §8 (state model) remain binding and unchanged. The connector contract and field-ownership model are designed into the Release 1 foundation so this is an extension, not a retrofit.

## Outside all current releases

Native CRM/marketing automation or any sales-team-facing surface · full accounting, invoicing, tax, banking, escrow, payment or payroll · course delivery · marketplace implementation · full Select curation · native file storage or e-signature infrastructure · clinical/medical/EAP case content · unsupervised AI actions or AI legal/compliance/financial approval · general workflow builder · cross-tenant benchmarks beyond HQ's own network view · client portals · native mobile apps.

## Success gate

Release 1 is not validated by shipping features. It is validated by **behaviour**: a real Dproperty back office runs its morning meeting from the Daily Review screen for four consecutive weeks, and no licence, contract or renewal is discovered late in that period.

Full acceptance criteria — functional, design and non-functional — are in [[BluePrint Wireframe - Back Office OS (Developer Handoff)]] §10.
