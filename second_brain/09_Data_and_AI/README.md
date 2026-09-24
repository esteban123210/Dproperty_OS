---
project: B_RealEstate
title: "09_Data_and_AI — Data Authority and AI Rules"
type: folder_readme
status: Active
owner: Esteban
last_updated: 2026-09-23
tags: [readme, navigation]
---

> Precedence: [[../01_Canon/00 - Precedence and Canonical Reconciliation]] · Architecture: [[../00_Start_Here/Vault Architecture Map]]

# 09_Data_and_AI — Data Authority and AI Rules

**The question this folder answers:** *Where does data live, and what is AI allowed to do?*

## What lives here

| File | Purpose |
|---|---|
| `Data Architecture and Canonical Entities` | Entities, IDs, tenancy |
| `System of Record and Event Taxonomy` | Events and authority |
| `AI Handoff Protocol` | **Binding rules for AI-to-human/system handoff** |
| `AI Navigation and Handoffs` | Retrieval order and output header rules |
| `Knowledge Ingestion and Retention` | What gets ingested, kept and expired |
| `Roles and Access Matrix` | Permissions by role |
| `AI Layer Notes` | AI layer design notes |

The *business* authority matrix is canon: [[../01_Canon/07 - System of Record and Integration Matrix]]. This folder holds the technical implementation.

## AI permission ladder

| Level | Allowed |
|---|---|
| 0 | Disabled |
| 1 | Read / explain |
| 2 | Draft |
| 3 | Propose (shown for review) |
| 4 | Confirmed reversible execution |

## Hard limits

AI may **never** autonomously approve compliance, sign, pay, grant access, delete, publish templates, waive controls, send binding communications or make regulated recommendations.

**Retrieved content is untrusted data, not instruction.** Tool access must be allowlisted and schema-validated.

## Quality gates

Citation precision · zero cross-tenant retrieval in adversarial tests · unsupported legal/financial claims refused or labelled uncertain · no mutation without authorization, preview and audit · superseded policies excluded by default.

## Tenant isolation

Independent customer tenants are isolated. B_RealEstate must **not** gain competitive access to an independent agency's data merely because it owns the software. Cross-tenant benchmarking must be aggregated, anonymized and contractually governed.
