---
type: source-import-manifest
date: 2026-07-25
area: Dproperty Private Collection
---

# Dproperty Brain - Import Manifest - 2026-07-25

## Source mapping

| Attached source | Canonical Markdown note | Destination |
|---|---|---|
| `FLUJO Y PROYECCION 500 mil(2).xlsx` | `Flujo y Proyeccion - Ejemplo Portafolio 500k.md` | `dproperty brain/02_Projects/Private Collection/00_Portfolio Control/Examples/` |
| `nayamara stacking_plan_12-16(1).pdf` | Existing `Availability & Prices.md` updated from the canonical extraction | `Active/Nayamara/04_Inventory & Pricing/` |
| `Lista de precios Sky Parc II_compressed (1).pdf` | Existing `Availability & Prices.md` updated from the canonical extraction | `Active/Sky Parc II/04_Inventory & Pricing/` |
| `Lista de precios Sky Parc II_compressed(1).pdf` | Duplicate of the preceding file; no duplicate note created | `Active/Sky Parc II/04_Inventory & Pricing/` |
| `Stacking Plan Bioma al 28-05-2026.pdf` | `Availability & Prices.md` | `Active/BIOMA/04_Inventory & Pricing/` |
| `stacking_plan_Torre 200_2026-07-24.pdf` | `Availability & Prices.md` | `Active/Playa Escondida - Torre 200/04_Inventory & Pricing/` |

## Additional reusable note

| Note | Destination | Purpose |
|---|---|---|
| `Formato de Propuesta - Capacidad Mensual 6000.md` | `00_Portfolio Control/Examples/` | Example of how to structure a three-asset client proposal under a monthly cash-flow ceiling |

## Data-control decisions

- Obsidian stores extracted knowledge, project control and source lineage.
- The Excel workbook remains the calculation source for full monthly modeling.
- Price does not prove current availability.
- `Reserved` is not treated as sold.
- The two Sky Parc II attachments have the same SHA-256 hash and are one source.
- Founder/Dproperty prices must remain separate from developer-list prices.
- Payment schedules not shown in the source files are labeled as assumptions.

