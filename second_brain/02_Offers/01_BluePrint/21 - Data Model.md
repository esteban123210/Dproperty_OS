---
project: B_RealEstate
title: "BluePrint Data Model — Legacy Entry"
type: redirect
status: Partially revived 2026-09-23 — recover from git
owner: Esteban
last_updated: 2026-09-20
tags: [blueprint, data, legacy]
---

> [!TIP] Partially revived 2026-09-23 — recoverable design work
> The 2026-09-23 reconciliation **reinstated BluePrint's transaction and commission spine** (beginning at qualified opportunity). The pre-reset content of this note was transaction-spine design work and is **relevant again**.
>
> It was replaced by this stub on 2026-09-20 (commit `ff84d37`). Recover the full 77-line version with:
>
> ```bash
> git show "ff84d37^:second_brain/02_Offers/01_BluePrint/21 - Data Model.md" > "recovered - Data Model.md"
> ```
>
> **Review before reuse.** The pre-reset version may also contain *property/project/unit inventory, listing and MLS* scope, which remains **permanently retired**. Keep the transaction/commission/compliance/approval/closing design; discard the inventory design.
>
> Controlling note: [[../../01_Canon/00 - Precedence and Canonical Reconciliation]]

# BluePrint Data Model

The old transaction/inventory data model is not canonical.

Use:
- [[11 - Architecture and System Boundaries]]
- [[13 - Data Trust Audit and Process Assurance]]
- [[14 - Chat First AI Operating Model]]

Current core concepts include tenant/user/role, source/provenance, verification state, budget, management metric, process/SOP/control, incident, corrective action, management action, knowledge artifact, approval, report period, integration exception and audit event.
