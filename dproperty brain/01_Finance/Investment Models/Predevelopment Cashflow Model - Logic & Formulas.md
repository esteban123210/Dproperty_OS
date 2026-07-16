---
type: finance-model
status: v0.9 - ready for review
market: Panama
currency: USD
updated: 2026-07-16
owner: Esteban
---

# 🧮 Pre-Development Cashflow Model — Logic & Formulas

> Master specification for the client-facing pre-construction cashflow + returns model.
> **This note = the brain (logic, formulas, assumptions). The calculator itself = Excel.**
> Per-client outputs → Drive/SharePoint, linked from the deal note in `02_Projects`.

---

## 1. Core architecture — one monthly grid, superposition

The whole model is a single **master monthly timeline** (`month 0 → T`). Each property produces its own cashflow vector on that grid, **offset by its signing month**. The portfolio is just the **sum of the vectors**.

```
Global month:      0    1    2  ...   6  ...  36  ...  42
Property A (t0):   ▼sign, quotas ......▶ delivery/exit
Property B (t+6):           ▼sign, quotas ......▶ delivery/exit
PORTFOLIO      =   A + B + ... + Reserve-account interest
```

This is why staggered signing "just works": align every property to the global calendar, then add columns.

---

## 2. Inputs (per property)

| Symbol | Input | Typical | Notes |
|--------|-------|---------|-------|
| `P` | Contract price | — | USD |
| `t0` | Signing month (global) | 0, 6, ... | Enables staggering |
| `d` | Signing % | ~5% | Paid at `t0` |
| `q` | Construction-phase % | 15–25% | Spread across `N` |
| `N` | Construction months | 36–42 | To delivery |
| `a` | Total appreciation at delivery | flat % | e.g. +25–30% (per decision: flat uplift, not compounding) |
| `a2` | Post-delivery annual appreciation | opt. | Only for keep-and-hold-then-sell |
| Exit | Sell / Keep-cash / Keep-mortgage | — | Per property |

**Portfolio input:** `L` = client's available capital, `i` = reserve savings rate (~4% annual).

---

## 3. Single-property formulas

**Signing:** `S = d · P`

**Monthly construction quota:** `Q = (q · P) / N`

**Balance due at delivery:** `B = P − S − (Q·N) = P · (1 − d − q)`   *(~70–80% of P)*

**Cash-out schedule (before exit):**
```
Month t0:            −S
Months t0+1 .. t0+N: −Q  each
Month t0+N:          exit-dependent (below)
```

**Appreciated value at delivery (flat uplift):**
```
V_sell = P · (1 + a)
```

---

## 4. Exit scenarios (at delivery, month t0+N)

### A) SELL (flip / assignment)
```
SellCost = commission%·V_sell            (your sales commission)
         + material_increment            (developer charge — % or fixed, TBC)
         + assignment_cost               (cesión fee)
         + CGT                           (Panama: min(3%·V_sell, 10%·gain))
         + transfer_tax                  (Panama 2%, if borne by client — usually seller)

gain     = V_sell − P
CashIn   = V_sell − B − SellCost         (outstanding balance settled from proceeds)
```
**Reconciliation (matches how we pitch it to clients):**
```
Profit = CashIn − equity_in = (V_sell − P) − SellCost = appreciation − selling costs ✓
```
➡️ Client never funds the 70–80% balance — it comes out of the sale.

### B) KEEP with mortgage
```
principal = B (− extra cash down, if any)
M = principal · (r/12) / (1 − (1 + r/12)^(−12·T))     amortized monthly payment
   r = mortgage rate (check Ley de Interés Preferencial for qualifying new homes)
   T = term in years

R_net = gross_rent · (1 − vacancy% − mgmt%) − recurring_expenses
Monthly cashflow from delivery = R_net − M
```

### C) KEEP with cash
```
Month t0+N: −B  (large outflow)
From delivery onward: + R_net
```

**Later sale (B or C) in month H:**
```
Terminal = V_sell(H) − remaining_mortgage_balance(H) − SellCost
V_sell(H) = V_sell · (1 + a2)^((H − delivery)/12)
```

---

## 5. Reserve account (the "smart money" engine)

Runs in parallel; funds the outflows the client hasn't paid yet.
```
Reserve_0 = L − (all signings due at month 0)
Reserve_t = Reserve_{t−1} · (1 + i/12) − (payments drawn this month)
```
- `i/12` = monthly interest on idle capital (~4% annual).
- Purpose: makes time-value tangible + proves liquidity/safety.
- **Per decision: show BOTH** — `Project IRR` (pure property flows) and `Strategy IRR` (property + reserve interest) side by side.

> Conceptual note: XIRR already rewards later payments via timing. The reserve account is how the client *realizes* that time value in cash, and demonstrates they keep a safety buffer the whole time.

---

## 6. Multi-project portfolio

For each property `j`, build its vector aligned to the global calendar (shift by `t0_j`), then:
```
Portfolio_cashflow[t] = Σ_j  property_j_cashflow[t]
Portfolio_reserve[t]  = single reserve account funding ALL properties' due payments
```
Staggered signings, staggered deliveries, and sequential exits (sell A first, keep paying B) all fall out automatically from the superposition.

---

## 7. Summary / returns table (second sheet)

| Metric | Scope | Formula |
|--------|-------|---------|
| **XIRR** (headline) | Whole portfolio | `XIRR(net_flows, dates)` — use XIRR, not IRR, for staggered dates |
| **Project IRR** | Property flows only | XIRR excl. reserve interest |
| **Strategy IRR** | Property + reserve | XIRR incl. reserve interest |
| **Equity Multiple (MOIC)** | Portfolio | `Σ inflows / Σ outflows` |
| **ROI** | Portfolio | `total profit / total equity invested` |
| **Cash-on-Cash** | Keep-and-rent only | `annual R_net / equity invested` |
| **Net rental yield** | Keep-and-rent only | `annual R_net / V_sell` |
| **NPV** | Portfolio | discount net flows at client's opportunity rate |
| **Payback month** | Portfolio | first `t` where cumulative cashflow ≥ 0 |

Headline = **XIRR + MOIC + ROI**; rental metrics appear only in keep scenarios.

Also surface: total buying costs, total selling costs, total invested (out of pocket), expected appreciation $, expected annual rent, total profit.

---

## 8. Panama-specific parameters (defaults — override per deal)

| Item | Default | Notes |
|------|---------|-------|
| Buyer closing costs (pre-construction) | Legal ~1% + registration/notary ~0.3–0.5% | Developer usually absorbs the 2% transfer tax on first sale |
| Transfer tax (resale by client) | 2% of higher of price / cadastral value | Normally the seller |
| Capital gains (resale) | `min(3%·V_sell, 10%·gain)` | 3% withheld as advance; 10% of gain is definitive; can elect 3% as final |
| Mortgage — Ley de Interés Preferencial | Subsidized rate, qualifying new homes, first years | Materially lowers `M` early on |
| FECI | ~1% annual on qualifying loans | Add to effective mortgage cost where applicable |
| ITBMS (VAT 7%) | Not on the property transfer | Real estate transfers exempt |

---

## 9. Excel build blueprint

**Tabs:**
1. `Inputs` — one block per property + portfolio inputs (`L`, `i`, appreciation, rates).
2. `Property A`, `Property B`, ... — monthly engine per property (signing, quotas, balance, exit, rent).
3. `Reserve` — the savings-account drawdown.
4. `Portfolio` — sums property vectors + reserve; the master monthly cashflow.
5. `Summary` — the returns table (XIRR, MOIC, ROI, etc.) + deal projections.
6. `Client Output` — clean, branded, printable view (2 tables: cashflow + summary).

**Portfolio monthly columns:** `Month | Date | Signing | Quotas | Balance/Mortgage | Rent | Sale proceeds | Net cashflow | Cumulative | Reserve balance | Reserve interest`

Use `XIRR` (needs a Date column). Toggle exit per property with a dropdown driving IF logic.

---

## 10. Open items to confirm before final build
- [ ] **Material increment charge** — is it a % of price/sale, or a fixed developer fee? Formula placeholder until confirmed.
- [ ] **Assignment (cesión) cost** — typical value / whether developer charges it.
- [ ] Default **appreciation %** to use at delivery (e.g. 25% vs 30%).
- [ ] Default **rent assumptions** — gross yield %, vacancy %, management %.
- [ ] Default **mortgage** rate/term (and whether to model Interés Preferencial subsidy explicitly).
- [ ] Confirm client bears any transfer tax on exit, or seller-only.

---

## Version
- **v0.9** (2026-07-16) — Logic settled with Esteban: flat appreciation, 4-part selling costs, dual IRR view, Panama parameters. Ready to build Excel.
- Source of truth for the *logic*. Excel = source of truth for the *numbers*.
