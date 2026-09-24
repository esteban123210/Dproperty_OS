---
project: B_RealEstate
title: "Localization Framework & Market Variables"
type: framework
status: Active Draft
version: 0.5
owner: Esteban
last_updated: 2026-07-21
tags: [franchise, localization, multi-market, compliance, source-of-truth]
---

> [!INFO] Channel-scoped — verified 2026-09-23
> This folder describes the **Dproperty Franchise** channel, not the company and not a product. B_RealEstate is a product-led software company; this is one route to market.
>
> **Canonical name:** Dproperty Franchise — “the company itself” is a legacy alias.
> This is **valuable operating source material** — the process library and manuals feed BluePrint's SOP/process model and Academy. Franchise royalty/launch economics are channel-specific and require contract design plus local legal advice before external use.
>
> Precedence: [[../01_Canon/00 - Precedence and Canonical Reconciliation|Canonical Reconciliation and Precedence]]

# Localization Framework & Market Variables

> **Principle (Decision 2026-07-21): process is global, values are local.** Every manual holds the *process* once, market-agnostic. Every currency, %, legal step, licensing body, tax rule, deposit norm, and language that changes by country lives **here**, in a per-market pack. In manuals these appear tagged `[local-market variable]` and resolve from the matrix below.
>
> **Governing rule:** a new market may not sell franchises, onboard a franchisee, or take a white-label client until its column below is **complete and legally signed off.** This is a P0 gate (see [[Manuals Audit and Gap Analysis]]).

## 1. How it works

1. Manuals + the [[Process Library/00 - Process Library Index|Process Library]] describe the process using role codes and `[local]` tags.
2. This framework defines the **variable categories** (rows) that any market must specify.
3. Each market gets a **completed column** (a "market pack"). Panama is the reference pack below.
4. HQ + local counsel sign off the pack before go-live. Packs are versioned and dated.

## 2. Market Variables Matrix

> ✅ = confirmed · ⚠️ = needs local legal confirmation · ▫️ = template/not started. Panama values are drawn from the source Commercial Process Manual v002-26 and **still need legal reconfirmation** where marked.

| # | Variable | 🇵🇦 Panama (reference) | 🇨🇴 Colombia (Bogotá/Medellín) | [Template — any new market] |
|---|---|---|---|---|
| 1 | **Currency** | USD ✅ | COP ⚠️ | Set + FX handling for reporting |
| 2 | **Language(s)** | Spanish ✅ | Spanish ✅ | Primary + client-facing |
| 3 | **Sale commission norm** | ~5% of price ⚠️ | Confirm ▫️ | % + who pays |
| 4 | **Co-broke custom** | 50/50 external advisor ⚠️ | Confirm ▫️ | Split convention |
| 5 | **Reservation norm (preventa)** | ~USD 1,000 ⚠️ | Confirm ▫️ | Amount + refundability |
| 6 | **Down-payment norm** | ~5% to developer ⚠️ | Confirm ▫️ | % + schedule |
| 7 | **Rental deposit rule** | 2 deposits + first month (furnished) ⚠️ | Confirm ▫️ | Standard terms |
| 8 | **Real-estate licensing** | Assoc. body (e.g. ACOBIR); confirm mandatory license ⚠️ | Confirm (Lonja / local rules) ▫️ | Who may broker + under whose licence |
| 9 | **Franchise disclosure / registration law** | Confirm regime ⚠️ | Confirm regime ⚠️ | Disclosure doc? registration? cooling-off? |
| 10 | **AML/KYC regime & regulator** | RE is AML-regulated; define KYC set + reporting ⚠️ | Confirm (UIAF) ⚠️ | KYC docs + SAR obligations |
| 11 | **Sanctions screening** | Required ⚠️ | Required ⚠️ | List(s) + tooling |
| 12 | **Data privacy law** | Law 81 of 2019 ⚠️ | Ley 1581 of 2012 ⚠️ | Law + cross-border transfer rules |
| 13 | **Tax on commissions / withholding** | Confirm ⚠️ | Confirm ▫️ | VAT/ITBMS, withholding, invoicing |
| 14 | **Contract & closing steps** | Promise contract, notary, protocol, deed ⚠️ | Confirm ▫️ | Legal closing chain |
| 15 | **Advertising / consumer rules** | No guaranteed returns; confirm ad law ⚠️ | Confirm (SIC) ▫️ | Claims rules |
| 16 | **Insurance minimums** | E&O / PI — define ▫️ | Define ▫️ | Required cover + limits |
| 17 | **Business cadence / holidays** | PA calendar ✅ | CO calendar ▫️ | Working-week + holidays |
| 18 | **Maintenance/repair thresholds** | e.g. > USD 200 needs approval ⚠️ | Confirm ▫️ | Approval threshold |

## 3. Per-market pack template

Each new market produces a note `Localization/Market Pack - <Country>.md` filling all 18 rows, plus:
- Local legal counsel name + sign-off date.
- Licensing pathway for the franchisee (how they get legally able to broker).
- Any market-specific process deviations (must be logged, not improvised).
- Language/translation status of each manual.

## 4. What must NOT be localized (global invariants)
- The 7 processes' **structure**, RACI logic, and control points.
- The **role taxonomy** (Role Map).
- **Dproperty Select** HQ-control rules and the **commission-layer firewall**.
- Brand voice and boutique positioning.
- The franchise **royalty model** (7.5% on collected GCI, gross-into-company basis) — the *base* is global; only the underlying local commission % is a local input.

## 5. Status & next steps
- Panama pack: **partially filled from source, pending legal reconfirmation** (P0).
- Colombia (Bogotá, Medellín): **to build** — first-target markets per strategy.
- Every `⚠️`/`▫️` is an open localization item feeding [[../00_Start_Here/Open Questions]] (Legal / Franchise Package).
