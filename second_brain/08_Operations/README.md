---
project: B_RealEstate
title: "08_Operations — How Work Is Actually Done"
type: folder_readme
status: Active
owner: Esteban
last_updated: 2026-09-23
tags: [readme, navigation]
---

> Precedence: [[../01_Canon/00 - Precedence and Canonical Reconciliation]] · Architecture: [[../00_Start_Here/Vault Architecture Map]]

# 08_Operations — How Work Is Actually Done

**The question this folder answers:** *How is work actually done?* Shared operating standards.

These are **shared** standards, used by Dproperty Franchise, B_ Partner and the BluePrint product spec alike. They are deliberately not duplicated inside each offer folder.

## What lives here

| File / folder | Purpose |
|---|---|
| `Process Library/` | **The role-based process library** — the operating core |
| `Operations Manual` | Franchise/office operations manual |
| `Golden Transaction Workflow` | The end-to-end transaction workflow BluePrint must support |
| `Shared Operating Model` | What all channels share |
| `Onboarding Support and QA` | Onboarding, support and quality standards |
| `Reporting and Management Cadence` | Weekly/monthly/quarterly rhythm |
| `Localization Framework` | How market-specific variables are handled |
| `Manuals System Index` | The manual architecture (M1–M5) |
| `Manuals Audit and Gap Analysis` | Audit against a multinational standard |
| `Multi-Line Manual Strategy` | Shared-core + overlays model |
| `Source Material/` | The original commercial process manual |

## Process Library

`00 - Process Library Index` · `01 - Leads` · `02 - Preventa (Lista Cero)` · `03 - Secondary Market Sale` · `04 - Assignment (Cesion)` · `05 - Long-Stay Rental` · `06 - Property Management` · `07 - Commissions`

This library is also the **canonical role taxonomy** for the whole vault.

## Binding standard — roles, never names

Every deliverable uses **abstract role codes**, never personal names or single-office headcounts. Any office-, country- or currency-specific value (amounts, ACOBIR, Panama rules) is marked a **local-market variable**, not hard-coded policy. *(Decision 2026-07-21.)*

## Relationship to BluePrint

`Golden Transaction Workflow` and the Process Library describe **how the business operates**. `02_Offers/01_BluePrint/` describes **the software that governs it**. When they disagree, the operating reality wins and the product spec is updated.
