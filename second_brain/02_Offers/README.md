---
project: B_RealEstate
title: "02_Offers — What We Sell"
type: folder_readme
status: Active
owner: Esteban
last_updated: 2026-09-23
tags: [readme, navigation]
---

> Precedence: [[../01_Canon/00 - Precedence and Canonical Reconciliation]] · Architecture: [[../00_Start_Here/Vault Architecture Map]]

# 02_Offers — What We Sell

**The question this folder answers:** *What do we SELL?* One folder per sellable thing.

An **offer** is anything a customer can buy. Full portfolio view with prices, boundaries and maturity: [[../01_Canon/04 - Offer Portfolio Map]].

## The eight offers

| Folder | Offer | Type | Job |
|---|---|---|---|
| [[01_BluePrint/00 - README\|01_BluePrint]] | **BluePrint** | Product — proprietary core | Run and control the company |
| [[02_BlankCRM/00 - README\|02_BlankCRM]] | **BlankCRM** | Product — attach | Sell |
| [[03_VAULTED/00 - README\|03_VAULTED]] | **VAULTED** | Product — network | Access the network |
| [[04_Academy/00 - README\|04_Academy]] | **Academy** | Product — enablement | Operate better |
| [[05_Dproperty_Franchise/00 - README\|05_Dproperty_Franchise]] | **Dproperty Franchise** | Channel | Full branded operating model |
| [[06_B_Partner/00 - README\|06_B_Partner]] | **B_ Partner** | Channel | Managed stack, own brand |
| [[07_Developer_Partnerships/00 - README\|07_Developer_Partnerships]] | **Developer Partnerships** | Channel | Developer sales and supply |
| [[08_Dproperty_Select/00 - README\|08_Dproperty_Select]] | **Dproperty Select** | Strategic asset | Curated deal flow |

## The handoff line

**BlankCRM owns demand until qualification. BluePrint owns everything after qualification. VAULTED owns network supply and access. Academy owns capability. Accounting remains the ledger.**

## Standard skeleton

```
0X_Offer_Name/
├── 00 - README.md                     what it is · status · what exists · what is missing
├── 01 - Definition and Boundaries.md  canonical definition; owns / does NOT own
├── 02 - ICP and Jobs To Be Done.md    who buys, who uses, the job
├── 03 - Offer and Pricing.md          what is sold, at what price, with a truth label
├── 04 - Delivery and Operations.md    implementation, onboarding, support
├── 05 - Economics.md                  unit economics, COGS, margin
├── 06 - Legal.md                      agreement notes, commission rules, jurisdiction flags
├── 07 - Investor Two-Pager.md         comparable investor summary
└── …                                  offer-specific files
```

**Not every offer has every file.** Each `00 - README.md` lists what exists and what is a genuine gap — a named gap is more useful than an empty placeholder.

## Rules

- Start every offer folder with `01 - Definition and Boundaries.md`, and state **what it does not own**.
- Channels are never pitched as separate software products.
- Shared operating standards live in `08_Operations/`, not duplicated per offer.
- Adding an offer? Create the skeleton and register it in [[../01_Canon/04 - Offer Portfolio Map]] and [[../01_Canon/03 - Product and Channel Hierarchy]].
