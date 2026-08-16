---
project: B_RealEstate
title: "BluePrint Product Map"
type: product_index
status: "Canonical v1.0"
version: 1.0
owner: Esteban
created: 2026-08-16
last_updated: 2026-08-16
tags: [blueprint, product, index, navigation, source-of-truth]
---

# BluePrint Product Map

This is the entry point for BluePrint product work. It separates binding product decisions from supporting and historical specifications.

## Read first

1. [[BluePrint Product Constitution]] — binding promise, boundaries, ownership, CRM modes, entities, MVP and Copilot authority.
2. [[BluePrint Golden Workflow - Wireframe and Validation]] — canonical MVP journey, screen wireframes, three-mode desk-test and acceptance criteria.
3. [[../18_Ecosystem/02 - BluePrint|Ecosystem component definition]] — BluePrint's role inside B_RealEstate.
4. [[../18_Ecosystem/12 - System of Record and Integration Matrix|System of Record Matrix]] — wider ecosystem data ownership.

## Supporting product specifications

| File | Role | Precedence note |
|---|---|---|
| [[Platform Information Architecture]] | Wider public/logged-in information architecture and integration patterns | Constitution and Golden Workflow control when older scope conflicts |
| [[Data Model]] | Detailed data-model exploration | Core entity boundaries in the Constitution are binding |
| [[Roles and Access Matrix]] | Role hierarchy and permission detail | AI authority and need-to-know rules in the Constitution are binding |
| [[MVP Scope]] | Short implementation summary | Golden Workflow acceptance criteria define the MVP gate |
| [[Product Modules]] | Capability inventory | A module appearing here does not automatically place it in MVP |
| [[Prototype Spec]] | Prior screen/prototype specification | Reconcile against the Golden Workflow before implementation |
| [[Prototype Control Note]] | Prototype governance | Use the canonical routes and scenarios in the Golden Workflow |
| [[Figma Handoff Notes]] | Design handoff support | Product behavior remains controlled by Constitution/workflow |
| [[AI Layer Notes]] | AI implementation exploration | Copilot permission levels and guardrails in the Constitution control |
| [[Platform Scenario Playbook]] | Wider scenario catalogue | Add Golden Workflow tests as the required regression spine |

## Product decision hierarchy

1. [[../00_Index/Decision Log|Decision Log]] — approved dated decisions.
2. [[BluePrint Product Constitution]] — current binding product contract.
3. [[BluePrint Golden Workflow - Wireframe and Validation]] — current binding MVP journey/test.
4. Supporting specifications — implementation detail.
5. Historical handoffs/prototypes — useful context, not authority where they conflict.

## Current product gate

Build one clickable prototype of the Golden Workflow and validate it with the five participant roles listed in the workflow document. Do not expand secondary modules until the same core flow works for GoHighLevel, an external CRM and BluePrint Direct.
