---
type: index
updated: 2026-07-16
---

# 📁 Dproperty Brain — Architecture Guide

The operating system for running Dproperty day-to-day. Start at [[Home]].

> **This vault vs `second_brain`:**
> `second_brain` = *building* the Dproperty OS / franchise system.
> `dproperty brain` (here) = *running* the actual agency day-to-day.
> Ask yourself: "Am I building the system, or running my agency today?"

## Folder Map

| Folder | What goes here |
|--------|----------------|
| `00_Dashboard` | Home hub, Weekly Review, Quick Capture inbox |
| `01_Finance` | Accounting, commissions, expenses, invoices, taxes, payroll, reports — **finances tracked in-vault**, heavy models linked to Excel |
| `02_Projects` | Every deal. Sub-tracks: **Resale · Developments · Rentals · Private Collection**, each with Active / Pipeline / Closed. Copy from `_Templates/` |
| `03_Templates` | Reusable documents, emails, checklists, social/marketing |
| `04_Branding` | Live brand system: guidelines, logos, colors, fonts, imagery, assets |
| `05_Operations` | SOPs, team & roles, onboarding, hiring, tools, vendors (built out for a growing team) |
| `06_Marketing & Sales` | Campaigns, listing copy, content calendar, lead snapshot (GHL is source of truth) |
| `07_Legal & Compliance` | Signed contracts, licenses, compliance, insurance (notes + links; originals in legal archive) |
| `08_Meetings & Notes` | Dated meeting notes: `YYYY-MM-DD - Topic.md` |
| `99_Archive` | Dead/old files kept out of the way but searchable |

## Rules of the road
1. **Contacts live in GoHighLevel**, not this vault. Notes reference people, don't duplicate the CRM.
2. **Obsidian = thinking & tracking. Heavy/final files → Drive/SharePoint. Design → Canva/Figma. Models → Excel.**
3. **Signed legal docs → secure legal archive**; keep a note + link here.
4. New deal? Duplicate the matching template from `02_Projects/_Templates/` into the right sub-track.
5. Run the [[Weekly Review]] to keep everything trustworthy.

## Conventions
- Folders numbered for deliberate order.
- `_` prefix = templates / meta (sort to top).
- Dates as `YYYY-MM-DD`.
- Use frontmatter (`status:`, `deal_type:`, `value:`) so Dataview can build live dashboards later.
