---
type: data-standard
updated: 2026-07-16
---

# Private Collection Data Standards

## Required executive-summary fields

Project, location, exact address, developer, legal entity, stage, construction progress, delivery, total units, number of models, area range, available/reserved/sold counts, sold percentage, price range by model, parking, storage, amenities, official payment method, maintenance, rental rules, commercial terms, sources and verification date.

## Inventory status vocabulary

| Status | Definition |
|---|---|
| Available | Promoter confirms the unit may be reserved now |
| Reserved | Temporarily held; not automatically counted as sold |
| Sold | Binding sale confirmed by promoter |
| Blocked | Not offered commercially but not sold |
| Withdrawn | Previously offered and removed |
| Unknown | Source does not establish status |

## Data-quality labels

- **Verified:** current official source plus confirmation.
- **Good:** current official source with limited supporting fields missing.
- **Partial:** brochure, incomplete list or undated list.
- **Assumed:** internal Dproperty scenario; never presented as official.
- **Expired:** historical document retained only for audit.

## File naming

- Dates: `YYYY-MM-DD`.
- Price list: `YYYY-MM-DD - Price List - Project`.
- Stacking plan: `YYYY-MM-DD - Stacking Plan - Project`.
- Payment plan: `YYYY-MM-DD - Payment Plan - Project`.
- Every commercial source must record issuer, received date, validity and superseded status.

## Calculation rules

- Sold percentage = sold units ÷ confirmed total units.
- Reserved units remain separate from sold units.
- If the source lists only available units, do not infer that all omitted units are sold.
- Price per m² must state whether terrace area is included.
- Use USD unless an official source states another currency.