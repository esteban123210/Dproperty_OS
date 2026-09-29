---
project: B_RealEstate
title: "Ecosystem Master Map"
type: ecosystem_architecture
status: Canonical v4.0
owner: Esteban
last_updated: 2026-09-29
tags: [ecosystem, architecture, map]
---

> [!IMPORTANT] Reconciled 2026-09-23
> Read [[00 - Precedence and Canonical Reconciliation]] first. It merges this map with the `19_Canonical_B_RealEstate` baseline and controls the vault.

# B_RealEstate — Ecosystem Master Map

## One-sentence definition

**B_ is operating infrastructure for real-estate businesses: BlankCRM helps the team sell, BluePrint helps management understand, verify and govern the company using financial and operational evidence, and VAULTED connects the company to a transaction network.**

## The handoff line

**BlankCRM executes the commercial process through post-sale. BluePrint verifies evidence and supports back-office management; data completeness and human review remain essential. VAULTED owns network supply and access. Building Blocks owns capability. Accounting remains the ledger.**

## Core architecture

```mermaid
flowchart LR
    C["Clients / Leads"] --> CRM["BlankCRM
powered by GoHighLevel
lead → legal → contract → closing → commission → post-sale"]
    CRM -->|"authorized lifecycle observations"| BP["BluePrint
Management OS
financial health · governance · intelligence · audit"]
    EXT["Accounting · Bank · Drive · E-sign"] --> BP
    CRM <--> VA["VAULTED
Private marketplace/network"]
    VA --> BP
    AC["Building Blocks
Learning & certification"] --> BP

    FR["Dproperty Franchise"] --> CRM
    FR --> BP
    FR --> VA

    PT["B_ Partner"] --> CRM
    PT --> BP
    PT --> VA

    DEV["Developer Partnerships"] --> VA
    DEV --> CRM
```

## Product hierarchy

| Product | Core job | Owns | Strategic role |
|---|---|---|---|
| **BluePrint** | Manage/govern the company | Evidence-backed financial health, expected vs actual cash, expenses, budgets and variance; KPI and CRM-usage oversight; process/Glitch monitoring; policies, management interventions, audit and AI executive support | Proprietary SaaS/IP |
| **BlankCRM** | Generate, organize and convert demand | Leads, contacts, messaging, forms/calendars, nurture, full commercial pipeline through post-sale, campaign attribution | Attach/acquisition product; third-party engine |
| **VAULTED** | Access/match network supply and demand | Gated listings, access rules, matches, introductions, attribution, GMV, fees | Network effect + GMV/take-rate upside |
| **Building Blocks** | Teach standards and close capability gaps | Learning content, assessments, certification evidence | Retention/quality/enablement (legacy alias: Building Blocks) |

### What BluePrint does **not** own

Property/project/unit inventory · listing management/MLS · full commercial workflow and marketing automation · general ledger, tax, payroll · property management · LMS delivery · marketplace listings and matching.

## Distribution and monetization channels

| Channel | Role |
|---|---|
| **Dproperty Franchise** | Branded, vertically integrated deployment of the stack |
| **B_ Partner** | Managed stack/operating model under customer's own brand |
| **Developer Partnerships** | Revenue + supply + distribution + product learning |
| **Direct SaaS** | BluePrint and/or BlankCRM sold to independent agencies |
| **VAULTED network** | Marketplace participation independent of franchise status where eligible |

## Strategic assets

- **Dproperty** — flagship investment brand/testbed/distribution.
- **Dproperty Select** — HQ-curated opportunities; may appear as a curated collection inside VAULTED.
- Existing developer/broker/investor relationships — cold-start advantage.
- Second Brain/process library — internal institutional knowledge; feeds product and Building Blocks curricula but is not itself a customer product.

## Long-term option

A physical real-estate innovation hub may remain a future expression of the network, but the software/network business must be valuable and defensible without it.
