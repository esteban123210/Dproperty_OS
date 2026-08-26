---
project: B_RealEstate
title: "Product Modules"
type: product_note
status: Baseline Created
owner: Esteban
last_updated: 2026-08-16
source: ChatGPT baseline vault package
tags: [product]
---

# Product Modules

> **Scope control (2026-08-16):** [[BluePrint Product Constitution]] controls the product/MVP boundary and [[BluePrint Golden Workflow - Wireframe and Validation]] controls the build gate. A capability listed here is not automatically included in MVP.

## HQ Dashboard

Tracks franchises, white-label clients, developer projects, revenue, deal flow, compliance, and Private Collection.

## Franchise Workspace

Workspace for each franchise to manage clients, projects, brokers, local deals, Private Collection opportunities, training, and reporting.

## Client Module

Stores buyer/investor profiles, contact details, preferences, budget, qualification, status, and related deals.

## Broker Module

Tracks broker partners, agreements, referrals, performance, communication, and commission sharing.

## Project Module

Stores project data, developer information, location, pricing, availability, materials, target buyer, and approved assumptions.

## Unit Module

Stores inventory-level details: unit, price, size, view, floor, availability, reservation status.

## Deal Pipeline

Tracks leads from initial contact to qualification, project match, reservation, contract, closing, and post-sale.

## Document Generator

Creates approved documents from structured data and templates.

## Projection Generator

Creates investment projections from approved assumptions.

## Commission Tracker

Calculates commissions, splits, royalties, network fees, and Private Collection economics.

## Training Academy

Tracks franchisee training modules, certifications, and completion.

## Private Collection

Controls access, client registration, deal workflow, and HQ approval for curated inventory.

## Developer Sales OS

Tracks developer projects, sales team pipeline, broker network, reporting, and success fees.

---

## 2026-07-18 Update — Platform Architecture Expansion

The modules above are the operating core. The full platform architecture (public site + logged-in OS + back-office systems) is defined in [[Platform Information Architecture]], with scenarios in [[Platform Scenario Playbook]] and roles in [[Roles and Access Matrix]]. New modules/systems added this session:

### New OS modules
- **Command Bar** — persistent universal search + command palette on every screen ("three clicks to anything").
- **Report a Glitch** — persistent no-blame improvement button on every screen.
- **Resource Library** — templates, brochures, brand assets surfaced from Drive (not re-hosted).
- **Learning / Academy** — embedded LMS (Open edX) via white-label + SSO.
- **CRM & Marketing** — embedded, white-labeled GoHighLevel via SSO.
- **AI Assistant** — the T1 agent layer.
- **Support / Help Desk** — tickets to HQ, knowledge base.
- **Field Mode (mobile)** — stripped in-meeting/offline view (inventory, prices, media, contacts, NDA).
- **Franchise Sales Room** (HQ) — full pitch package in one place for closing franchises.
- **Data Room generator** — per-prospect shareable personalized microsite.

### Six back-office systems
- **Finance / Back Office** — commissions, royalties, invoices, payments, reimbursements, refunds, reconciliation, close.
- **People / HR** — users, roles, contracts, leave, payslips, reviews, on/offboarding, self-service "My Profile."
- **Cases / Ticketing** — one engine for complaints, grievances, claims, disputes, escalations, whistleblower; case type controls visibility + routing + SLA.
- **Tenant Lifecycle** (in HQ Control Center) — provision → audit → wind-down a franchise.
- **Audit Log & Data Governance** — immutable trail, data requests, security flags.
- **Glitch Report** — no-blame, transparent, continuous-improvement reporting (Four Seasons model); glitches never person-attributed.

---

## 2026-08-26 Update — Scope redirection and module consolidation

[[BluePrint Product Constitution]] v2.0 confirms BluePrint as the **back-office brain for administrative staff only**, and re-sequences delivery into Release 1 (Back Office Brain) and Release 2 (Transaction Spine). This section supersedes the module inventory above where they conflict.

**Note on history:** the 2026-07-18 additions above (Glitch Report, People/HR, Cases, Resource Library, Command Bar, Support) were correct and are now formally restored to canonical scope. Constitution v1.0 had narrowed them away; v2.0 reinstates them.

### Modules are now instantiations of two primitives

Do not build these as separate systems. Build the primitive once and configure it. See [[BluePrint Wireframe - Back Office OS (Developer Handoff)]] §5.

| Primitive | Instantiated as |
|---|---|
| **Registry** — tracked record with owner, status, expiry, renewal rules, external links | Legal contracts · corporate licences · software licences · tax obligations · person records · templates · manuals · directory entries |
| **Ticket** — reported item with routing, SLA, confidentiality, resolution | Glitch reports · HR cases and complaints · internal requests |

Supporting engines: Task (with provenance links), Alert/renewal, Metric definition, Copilot.

### Release 1 modules

Today · Glitches (report, daily review, dashboard) · Tasks · Performance (personal KPIs, team KPIs, satisfaction, reports) · People (records, licences, HR cases, wellbeing) · Legal (contracts, licences, software, taxes, calendar) · Library (templates, manuals, Academy links) · Directory · Copilot · Administration. Global: Command Bar · Report a Glitch.

### Modules moved to Release 2

Deal Pipeline (as transaction workspace) · Document Generator · Projection Generator · Commission Tracker · Client Module · Project Module · Unit Module · Broker Module. These remain valid; they are not built in Release 1.

### Modules removed from BluePrint scope

| Module | Reason |
|---|---|
| **CRM & Marketing (embedded GHL)** | Duplicates GoHighLevel. Replaced by a launch link + inbound performance metrics. Sales advisors do not receive BluePrint seats (Constitution §3.11) |
| **Learning / Academy (embedded LMS)** | Duplicates B_Academy. Replaced by a launch link + completion status only |
| **Field Mode (mobile)** | Was designed for sales advisors in meetings — that user is now a CRM user. Deferred pending a genuine back-office mobile need |
| **Training Academy module** | Superseded by the Library → Formación link-out |
| **Support / Help Desk** | Absorbed into the Ticket primitive as `internal_request` |
| **Cases / Ticketing** (as a distinct system) | Absorbed into the Ticket primitive as `hr_case` |
| **Resource Library** (as a distinct system) | Absorbed into the Registry primitive as Library + Directory |

### Unchanged and still in scope

HQ Control Center (T4 cross-tenant views, now including cross-office glitch and recovery patterns) · Tenant Lifecycle · Audit Log & Data Governance · Private Collection and Developer Sales OS (governed by their own workstream notes) · Franchise Sales Room and Data Room generator (HQ commercial tooling, unscheduled).
