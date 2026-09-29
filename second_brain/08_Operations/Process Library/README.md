---
project: B_RealEstate
title: "Process Library"
type: folder_readme
status: Active
owner: Esteban
last_updated: 2026-09-29
tags: [readme, operations, process, roles]
---

> Precedence: [[../../01_Canon/00 - Precedence and Canonical Reconciliation]] · Architecture: [[../../00_Start_Here/Vault Architecture Map]]

# Process Library

**The question this folder answers:** *How does a real-estate transaction actually get done, step by step, by which role?*

This is the operating core of the business and the **canonical role taxonomy for the entire vault**.

## The seven processes

| # | Process | Covers |
|---|---|---|
| [[00 - Process Library Index]] | **Index + role taxonomy** | Start here. Defines every role code used across the vault. |
| [[01 - Leads]] | Lead intake and qualification | Capture → qualification handoff |
| [[02 - Preventa (Lista Cero)]] | Pre-sale / Lista Cero | New-development pre-sale allocation |
| [[03 - Secondary Market Sale]] | Resale | Standard secondary-market transaction |
| [[04 - Assignment (Cesion)]] | Assignment / cesión | Contract assignment before completion |
| [[05 - Long-Stay Rental]] | Long-stay rental | Rental placement and contract |
| [[06 - Property Management]] | Property management | Ongoing management service |
| [[07 - Commissions]] | Commissions | Calculation, splits, payout |

## Why this folder is shared, not per-offer

These processes are used by **Dproperty Franchise**, **B_ Partner** and the **BluePrint product specification** alike. Duplicating them per offer would guarantee drift. They live here once.

- Franchise-specific packaging → `02_Offers/05_Dproperty_Franchise/`
- Execution configuration → `02_Offers/02_BlankCRM/`; management oversight → `02_Offers/01_BluePrint/` and [[../Golden Transaction Workflow]]

## Binding standard — roles, never names

Every process uses **abstract role codes**. Never personal names, never a single office's headcount. *(Decision 2026-07-21.)*

Any office-, country- or currency-specific value — commission percentages, ACOBIR rules, Panama-specific requirements, amounts — is marked a **local-market variable**, not hard-coded policy. See [[../Localization Framework]].

## Relationship to BluePrint

The Process Library describes **how the business operates**. BluePrint is **the software that governs it**.

Commercial processes 01–05 and 07 execute in **BlankCRM/chosen CRM**, including legal, approvals, closing, commission and post-sale. Process 06 property-management service delivery remains with the designated property-management system; its commercial communications and milestones can be coordinated in CRM. **BluePrint** reads outcomes to verify finances, monitor Glitches and govern processes; it executes none of these sales processes.

**When the process and the product spec disagree, the operating reality wins** and the product spec is updated — not the other way around.
