---
project: Dproperty OS
title: "Data Model"
type: product_note
status: Baseline Created
owner: Esteban
last_updated: 2026-07-01
source: ChatGPT baseline vault package
tags: [product]
---

# Data Model

## Core Objects

- Organization.
- User.
- Franchise.
- White-label client.
- Developer.
- Project.
- Unit.
- Client.
- Broker.
- Deal.
- Document.
- Projection.
- Commission.
- Training module.
- Support ticket.
- Private Collection request.
- Developer Sales OS project.

## Relationship Logic

- A franchise has many users, clients, brokers, deals, and reports.
- A project has one developer and many units.
- A deal connects a client, project/unit, franchise/agency, broker, and commission record.
- A Private Collection deal requires HQ approval.
- A projection is linked to a project, client, and assumptions.
- A document is linked to an object and a template.

## MVP Required Fields

Each object should have:

- Name.
- Owner.
- Status.
- Created date.
- Last updated.
- Responsible person.
- Notes.
- Related links.

## 2026-07-18 Update — New Objects (Platform Architecture)

Added to support the expanded platform (see [[Platform Information Architecture]]). Every object keeps the MVP required fields above; key new ones:

- **Listing** — property/unit intake record; links to Project/Unit; triggers T0 file-routing to Drive.
- **Shortlist / Share** — curated client-facing set of projects; shareable link.
- **Data Room** — per-prospect shareable microsite (franchise recruitment).
- **Case** — complaint / grievance / claim / dispute / escalation / whistleblower. Fields: case type, **confidentiality level**, routing target, SLA, status, resolution. *(Extends the existing Support ticket object.)*
- **Glitch** — no-blame improvement report. Fields: text, auto-context (page/module/role/tenant/time), tag (Product/Experience), severity, status (reported/in-progress/fixed), fix note. **No person-attribution field by design.**
- **Invoice / Payment** — client/developer/royalty billing; provider reference; paid/unpaid.
- **Payout** — commission/royalty distribution record; split lines; approval; reconciliation.
- **Reimbursement** — expense claim; receipt; approver; payment status.
- **Person (HR)** — employee record; role; contract; leave; payslip links; certification status.
- **Tenant** — franchise workspace; lifecycle state (provisioned/active/wind-down).
- **Audit Log entry** — immutable action trail (who/what/when); powers data-governance and security cases.

**Rule:** confidentiality is a property of the record (esp. Case), not a separate app. Money/legal objects are always deterministic (T0) and audit-logged.
