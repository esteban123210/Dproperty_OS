---
type: operating-standard
updated: 2026-07-16
---

# Universal Private Collection Project Architecture

Replicate this exact structure for every new project.

```text
Project Name/
├── 00_Project Control/
│   ├── Executive Summary.md
│   ├── Missing Information.md
│   ├── Source Register.md
│   └── Update Log.md
├── 01_Project & Developer/
│   └── README.md
├── 02_Location & Market/
│   └── README.md
├── 03_Product & Architecture/
│   └── README.md
├── 04_Inventory & Pricing/
│   └── Availability & Prices.md
├── 05_Payment & Financing/
│   └── Payment Plan.md
├── 06_Amenities & Lifestyle/
│   └── Amenities Register.md
├── 07_Legal & Compliance/
│   └── README.md
├── 08_Sales Enablement/
│   └── README.md
├── 09_Marketing Assets/
│   └── README.md
├── 10_Dproperty Commercial/
│   └── Commercial Terms.md
├── 11_Construction & Handover/
│   └── README.md
├── 12_Documents & Media/
│   └── Document Index.md
└── 99_Archive/
    └── README.md
```

## Folder purpose

| Folder | Required content |
|---|---|
| `00_Project Control` | Executive truth, missing-data control, source register and update history |
| `01_Project & Developer` | Project facts, promoter/legal entity, team, contacts, track record, stage and timeline |
| `02_Location & Market` | Exact address, coordinates, connectivity, neighborhood, comparable projects, rents and demand thesis |
| `03_Product & Architecture` | Models, unit plans, areas, views, building specifications, finishes, AC, appliances, parking and storage |
| `04_Inventory & Pricing` | Current unit-level stack, prices, status definitions, price history and validity |
| `05_Payment & Financing` | Reservation, official payment plan, mortgages, closing costs and internal cash-flow scenarios |
| `06_Amenities & Lifestyle` | Amenity register by level, operating rules, access, fees and commercial relevance |
| `07_Legal & Compliance` | Contracts, permits, land/title notes, escrow, PH rules, rental rules, taxes and due diligence |
| `08_Sales Enablement` | Buyer profiles, approved narrative, FAQs, objections, comparison sheets and sales scripts |
| `09_Marketing Assets` | Campaign plans, approved copy, renders, videos, social assets and asset usage rights |
| `10_Dproperty Commercial` | Developer commission, collection flow, franchise payout, co-broker rules, lead attribution and receivable milestones |
| `11_Construction & Handover` | Progress, site visits, delivery, inspections, punch list, warranties and property management |
| `12_Documents & Media` | Index and links to official brochures, plans, lists, contracts, photos and Drive/SharePoint originals |
| `99_Archive` | Superseded price lists, withdrawn materials and historical versions |

## Update workflow

1. Add the source to `12_Documents & Media/Document Index.md`.
2. Update unit status and prices in `04_Inventory & Pricing` first.
3. Update the project `Executive Summary.md`.
4. Resolve the project and portfolio missing-information trackers.
5. Move replaced material to `99_Archive`; preserve date and source.
6. Update `Source Register.md` and `Update Log.md`.

## Default construction payment scenario — internal assumption only

Where an under-construction project has no official plan, model:

- 5% at contract signing.
- 15% in monthly installments over the construction period.
- 10% as negotiable extraordinary payments or incorporated into monthly installments.
- 70% at delivery through cash or mortgage.

This is not a developer commitment. Replace it immediately when official terms are received.

## Private Collection commercial rule

The `10_Dproperty Commercial` folder must document who collects gross commission, the developer payment milestone, Dproperty’s retained economics and any franchise/co-broker payout. Do not mix client purchase installments with Dproperty commission cash flow.