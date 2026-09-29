---
project: B_RealEstate
title: "BlankCRM — Offer README"
type: offer_readme
status: Canonical — price unmodelled
owner: Esteban
last_updated: 2026-09-29
tags: [offer, readme, blankcrm]
---

> [!IMPORTANT] Start here
> Precedence: [[../../01_Canon/00 - Precedence and Canonical Reconciliation]] · Portfolio: [[../../01_Canon/04 - Offer Portfolio Map]] · Architecture: [[../../00_Start_Here/Vault Architecture Map]]

# BlankCRM

**Type:** **Product** — attach/acquisition. Deliberately *not* the moat.
**Job:** Help the agency sell more and lose fewer opportunities.
**Price:** **Open.** Must be built from GHL plan/sub-account cost + messaging/AI usage + onboarding/support + target margin. `[R]` Do not publish a number before the economics are approved.
**Status:** Full-lifecycle product designed; live configuration and acceptance tests pending. Pricing requires pilot delivery-cost validation.

BlankCRM is B_'s configured real-estate front-office product, **powered by GoHighLevel**. It is sold as a practical sales operating environment, not as proprietary CRM technology.

Be transparent about the engine. B_ deliberately avoids spending proprietary engineering capital rebuilding commodity CRM infrastructure — that capital goes to BluePrint and VAULTED.

**Never claim "CRM propio" or a proprietary CRM.**

## What it owns

Lead and contact management · WhatsApp/email/SMS workflows · forms, landing pages, calendars · follow-up and nurture · full commercial sales pipeline and agent activity · campaign and source attribution · sales, legal and administration automations · legal workflow · commercial approvals · contracts · payment milestones · closing · commissions · post-sale · commercial dashboards

## What it does NOT own

management budgets and finance control · official management truth · process assurance and Glitches · accounting · marketplace listings (→ VAULTED) · long-term management audit

## Files in this folder

| File | What it is |
|---|---|
| `01 - Definition and Boundaries` | Canonical definition; relationship to BluePrint and VAULTED |
| `04 - Product Record` | Product record and commercial framing |
| `04A - Delivery - GoHighLevel Setup Checklist` | Implementation checklist |
| `08 - Master Product Specification` | Full product architecture, fields, roles, workflows and clone boundary |
| `09 - Configuration Acceptance Tests` | End-to-end and failure-path tests; live results still pending |
| `10 - Snapshot Release and Client Onboarding` | Build sequence, release gates and repeatable client setup |
| `11 - Pilot Office Intake Worksheet` | Fill-in decisions and ownership for the first office |
| `12 - GoHighLevel Build Manifest` | Exact records, fields, pipeline, queues, workflows and snapshot inventory |
| `13 - Start From Zero - Agency Account` | Founder guide to open the agency account before live build/testing |
| `05 - GoHighLevel Engine` | What GHL owns and does not own |
| `05A - GoHighLevel Role` | Role of GHL in the ecosystem |
| `07 - Investor Two-Pager` | Comparable investor summary |

## Gaps — genuine, not placeholders

- **`00`/`02 - ICP and Jobs To Be Done` missing.** The ICP is assumed to be the same as BluePrint's; that has never been tested separately. Smaller agencies may be a CRM-first gateway segment.
- **Full-lifecycle delivery economics unvalidated.** The existing $750 setup/$249 monthly list and cost model predate the expanded legal, payment, closing and commission implementation. Measure actual pilot onboarding/support hours and integrations before confirming this price for the full package. `[R]`
- **`06 - Legal.md` missing.** Reseller/sub-account terms with GoHighLevel not documented. Vendor-dependency risk is unassessed. `[R]`
- **Trademark availability for the name "BlankCRM" unverified.** `[R]`

## Next gate

Build and test the master in a fresh GoHighLevel TEST sub-account, pilot one new-development transaction path, measure COGS, then test **standalone acquisition** separately from **attach to BluePrint**.

**Guardrail:** do not let CRM customization consume core engineering resources.
