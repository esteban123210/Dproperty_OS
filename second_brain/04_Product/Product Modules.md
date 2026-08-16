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
