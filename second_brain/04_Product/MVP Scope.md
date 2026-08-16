---
project: B_RealEstate
title: "MVP Scope"
type: product_note
status: "Canonical summary v1.0"
owner: Esteban
last_updated: 2026-08-16
source: BluePrint Product Constitution and Golden Workflow
tags: [product, blueprint, mvp]
---

# BluePrint MVP Scope

> **Control:** Full boundary: [[BluePrint Product Constitution]] §9. Build/test gate: [[BluePrint Golden Workflow - Wireframe and Validation]]. This file is the compact implementation summary.

## MVP outcome

All three intake modes must complete one operational spine without separate product variants:

**qualified CRM/manual intake → transaction workspace → compliance → document generation → human approval/signature handoff → closing → commission → report**

## Included

- Multi-tenant workspace, roles, record permissions and audit foundation.
- GoHighLevel handoff, standard webhook/API, manual intake and CSV import.
- Intake validation, external IDs, field ownership and duplicate protection.
- Transaction workspace with owner, stage, next action, blockers and timeline.
- Project/unit operational references required by the transaction.
- Configurable compliance requirements, evidence, review and approval gates.
- Approved template/version registry and small governed document set.
- Tasks, checklists, approvals, deadlines and escalations.
- External e-signature handoff/status/reference.
- Deterministic commission calculation, human approval and reconciliation status.
- Operational dashboard and weekly management snapshot.
- Company knowledge registry.
- Permission-aware Copilot: retrieval/explanation, summaries/analysis, drafts and confirmed low-risk prepared actions.
- Integration event/error administration.

## Outside MVP

- Native CRM/marketing automation.
- Full accounting, invoicing, tax, banking, escrow or payment product.
- Course delivery, marketplace implementation or full Select curation.
- Native file storage or e-signature infrastructure.
- Unsupervised AI actions or AI legal/compliance/financial approval.
- General workflow builder, cross-tenant benchmarks, client portals and mobile-native apps.
- Secondary modules that do not prove the Golden Workflow.

## Success gate

The architecture is defined. The MVP is not validated until a clickable/working prototype passes the cross-mode, workflow, Copilot and usability criteria in the Golden Workflow document with no hidden mode-specific product fork.
