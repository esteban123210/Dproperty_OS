---
project: B_RealEstate
title: "System of Record and Integration Matrix"
type: data_governance
status: Canonical v1.0
owner: Esteban
last_updated: 2026-08-16
tags: [ecosystem, integrations, data-governance]
---

# System of Record and Integration Matrix

## Non-negotiable rule

Each business object has one writable system of record. Other systems may display, cache or receive selected fields, but they do not become competing editable masters.

## Ownership matrix

| Object | Writable source of truth | Referenced by | Key handoff |
|---|---|---|---|
| Lead/contact/conversation | GoHighLevel | BluePrint | Qualified contact ID and snapshot to BluePrint |
| Appointment/campaign/source attribution | GoHighLevel | BluePrint reports | Aggregated KPI sync |
| Tenant, user, role, permission | BluePrint / identity provider | GHL, Open edX, VAULTED | Provision/deprovision events |
| Developer/project/unit intelligence | BluePrint | VAULTED, GHL, reports | Approved publication fields only |
| Dproperty Select approval/terms | BluePrint under HQ Select governance | VAULTED, partner views | Access and commercial-term version |
| Marketplace listing/invitation/engagement | VAULTED | BluePrint | Listing reference and qualified match |
| Operational transaction | BluePrint | GHL, accounting, e-sign | Milestones written outward |
| Course/lesson/assessment activity | Open edX | BluePrint | Completion/certification result |
| Certification/readiness gate | BluePrint | Open edX, permissions | Role access decision |
| Binary file | Drive/SharePoint or legal archive | BluePrint | Stable link, version and metadata |
| Template/clause governance | BluePrint template control with approved binary source | Document generator | Approved version only |
| Signature envelope/evidence | E-signature provider | BluePrint | Status, timestamp and signed-file link |
| Projection inputs/results | BluePrint | Documents/reports | Deterministic calculation and version |
| Commission/royalty calculation | BluePrint | Accounting/payment provider | Approved payable/invoice instruction |
| Bank/payment/accounting movement | Accounting/payment provider | BluePrint | Paid/reconciled status |
| Audit event | BluePrint | HQ/compliance | Immutable log |

## Integration principles

1. Use stable external IDs on every linked record.
2. Define one-way or event-specific field ownership, never blind bidirectional sync.
3. Log integration failures and provide a repair queue.
4. Show source and last-sync time for externally sourced metrics.
5. Deprovision access across all connected systems from one tenant-lifecycle action.
6. Restrict personal and confidential data to the minimum required fields.
7. Do not expose private VAULTED or Select terms through public APIs/pages.

## Golden transaction handoff

1. GHL opportunity becomes qualified.
2. User creates/accepts a BluePrint transaction linked to the GHL IDs.
3. Project/unit is selected from BluePrint or linked from VAULTED.
4. BluePrint controls projection, documents, approvals and closing checklist.
5. E-signature/accounting providers return evidence and settlement status.
6. BluePrint returns reserved/closed/lost milestones to GHL.

## Security and tenancy

Tenant isolation applies at the record level. HQ cross-tenant access is role-specific and audit-logged. Confidentiality is a property of a record. Legal, financial, deletion and access-change actions always require human authorization and an audit event.

