---
project: B_RealEstate
title: "Prototype Control Note"
type: product_note
status: Baseline Created
owner: Esteban
last_updated: 2026-08-16
source: ChatGPT baseline vault package
tags: [product]
---

# Prototype Control Note

> **⚠ Superseded for build purposes (2026-08-26):** The prototype to build is the **Release 1 Back Office OS**, specified end-to-end in [[BluePrint Wireframe - Back Office OS (Developer Handoff)]] — screens, design tokens, primitives, permissions, build order and acceptance criteria. Use that file's §9 build order in place of any sequencing below.

> **Naming and scope update (2026-08-16):** The platform is **BluePrint**, part of **B_RealEstate**. GoHighLevel remains the CRM, Open edX the Academy technology, and VAULTED the off-market marketplace. The canonical boundaries live in [[../18_Ecosystem/00 - Ecosystem Master Map]] and [[../18_Ecosystem/12 - System of Record and Integration Matrix]].

## Purpose

This note prepares the BluePrint product for Figma and build planning.

## Product Vision

BluePrint is the operating system for HQ, franchises, white-label agencies, and developer sales projects.

## Main User Types

- HQ admin.
- Venture lead.
- Franchise owner.
- Franchise agent.
- White-label agency admin.
- Developer sales manager.
- Broker partner.
- Client/investor viewer, later optional.
- External legal/finance reviewer, later optional.

## Main Modules

- HQ Dashboard.
- Franchise Workspace.
- Client Module.
- Broker Module.
- Developer Module.
- Project Module.
- Unit Module.
- Deal Pipeline.
- Document Generator.
- Projection Generator.
- Commission Tracker.
- Training Academy.
- Private Collection.
- Developer Sales OS.
- Reporting.
- Support.

## MVP Scope

MVP should include:

- Client records.
- Broker records.
- Project records.
- Unit records.
- Deal pipeline.
- Basic document generation/indexing.
- Projection template.
- Commission logic.
- Franchise dashboard.
- Private Collection access/request workflow.
- Training checklist.
- Reporting dashboard.

## Figma To-Do

1. Create information architecture.
2. Create dashboard wireframes.
3. Create client/project/deal screens.
4. Create Private Collection flow.
5. Create franchise onboarding flow.
6. Create projection generator flow.
7. Create reporting dashboard.

## 2026-07-18 Update — Platform Architecture

The information architecture (Figma To-Do #1) is now defined in [[Platform Information Architecture]] (public site + logged-in OS + back-office systems + embedding strategy + cost model), with [[Platform Scenario Playbook]] (72+ scenarios) and [[Roles and Access Matrix]]. Wireframe the priority screens first: Public Home, Franchise Workspace Home, Deal Detail, Resource Library, Command Bar, Glitch Report — not all 25 modules at once.
