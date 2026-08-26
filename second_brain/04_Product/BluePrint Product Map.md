---
project: B_RealEstate
title: "BluePrint Product Map"
type: product_index
status: "Canonical v2.0"
version: 2.0
owner: Esteban
created: 2026-08-16
last_updated: 2026-08-26
tags: [blueprint, product, index, navigation, source-of-truth]
---

# BluePrint Product Map

This is the entry point for BluePrint product work. It separates binding product decisions from supporting and historical specifications.

> **v2.0 — 2026-08-26.** BluePrint is the back-office brain for administrative staff; sales works in GoHighLevel. Scope is delivered in sequenced releases: **Release 1 = Back Office Brain**, **Release 2 = Transaction Spine**. See [[BluePrint Product Constitution]] §9.

## Read first

1. [[BluePrint Product Constitution]] — binding promise, boundaries, ownership, release sequencing, service-recovery rules and Copilot authority. **Start here.**
2. [[BluePrint Wireframe - Back Office OS (Developer Handoff)]] — **Release 1 build specification**: design system, screens, primitives, permissions, build order and acceptance criteria.
3. [[BluePrint Golden Workflow - Wireframe and Validation]] — **Release 2 specification**: transaction journey, screens, three-mode desk-test and acceptance criteria.
4. [[../18_Ecosystem/02 - BluePrint|Ecosystem component definition]] — BluePrint's role inside B_RealEstate.
5. [[../18_Ecosystem/12 - System of Record and Integration Matrix|System of Record Matrix]] — wider ecosystem data ownership.

## Supporting product specifications

| File | Role | Precedence note |
|---|---|---|
| [[Platform Information Architecture]] | Wider public/logged-in information architecture and integration patterns | Constitution controls; the Release 1 shell is in the Wireframe |
| [[Data Model]] | Detailed data-model exploration | Core entity boundaries in the Constitution are binding |
| [[Roles and Access Matrix]] | Role hierarchy and permission detail | Back-office-only access (§3.11) and AI authority in the Constitution are binding |
| [[MVP Scope]] | Short implementation summary | Constitution §9 defines the release boundary |
| [[Product Modules]] | Capability inventory | A module appearing here does not automatically place it in a release |
| [[Prototype Spec]] | Prior screen/prototype specification | Reconcile against the Golden Workflow before implementation |
| [[Prototype Control Note]] | Prototype governance | Use the canonical routes and scenarios in the Golden Workflow |
| [[Figma Handoff Notes]] | Design handoff support | Product behavior remains controlled by Constitution/workflow |
| [[AI Layer Notes]] | AI implementation exploration | Copilot permission levels and guardrails in the Constitution control |
| [[Platform Scenario Playbook]] | Wider scenario catalogue | Add Golden Workflow tests as the required regression spine |

## Product decision hierarchy

1. [[../00_Index/Decision Log|Decision Log]] — approved dated decisions.
2. [[BluePrint Product Constitution]] — current binding product contract.
3. [[BluePrint Wireframe - Back Office OS (Developer Handoff)]] — binding Release 1 build spec.
4. [[BluePrint Golden Workflow - Wireframe and Validation]] — binding Release 2 journey/test.
5. Supporting specifications — implementation detail.
6. Historical handoffs/prototypes — useful context, not authority where they conflict.

## Current product gate

**Release 1 — Back Office Brain.** Build the foundation at full strength, then the Registry and Ticket primitives, then the Glitch Report daily ritual, then the registries, performance and Copilot. Per [[BluePrint Wireframe - Back Office OS (Developer Handoff)]] §9.

The gate is behavioural, not feature-based: **a real Dproperty back office runs its morning meeting from the Daily Review screen for four consecutive weeks, and no renewal is discovered late in that period.**

Do not begin Release 2 (transaction spine) until Release 1 is in daily use. Do not shortcut the shared foundation to get there faster — that converts Release 2 into a rewrite.
