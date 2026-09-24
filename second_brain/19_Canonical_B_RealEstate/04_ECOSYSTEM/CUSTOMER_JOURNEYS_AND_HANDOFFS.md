> [!IMPORTANT] Reconciled 2026-09-23 — read the precedence note first
> [[../../18_Ecosystem/18 - Canonical Reconciliation and Precedence|18 - Canonical Reconciliation and Precedence]] controls the vault. This folder is **one of three canonical layers**, not the sole authority:
>
> - `18_Ecosystem/` — what the company **is**
> - `04_Product/BluePrint/` — what the product **is**
> - `19_Canonical_B_RealEstate/` — **this folder**: how it is **proven and financed** (finance models, data/AI architecture, operations, compliance, KPIs/gates, investor diligence)
>
> **Naming corrections that override this folder:** **Academy** (not *Building Blocks*) · **B_ Partner** (not *White-Label*) · **Dproperty Select** (not *Private Collection*) · **Developer Partnerships** (not *Developer Sales OS*).
>
> **BluePrint is both halves:** the transaction/commission spine from qualified opportunity **and** the management-control layer (budgets, variance, process assurance, Glitches, period close). It never owns property/unit inventory, listings or MLS.

# Ecosystem Customer Journeys and Handoffs

## Agency/partner journey

Discover → qualify → commercial proposal → agreement/payment → organization setup → identity/roles → CRM/data connection → Building Blocks assignments → template/workflow configuration → test transaction → production activation → weekly use/support → business review → renewal/expansion.

Critical handoff: commercial promise to implementation. The signed order form, entitlements, scope, exclusions, data migration, owners, dates and acceptance criteria become a structured onboarding record. Sales notes alone are not authority.

## Lead-to-close journey

1. CRM captures source, consent, contact and early opportunity.
2. Configured qualification trigger creates or proposes BluePrint intake.
3. Integration deduplicates and records external identifiers/idempotency.
4. BluePrint assigns owner and workflow; CRM remains engagement tool.
5. Transaction proceeds through evidence, documents, approvals, contracting, closing and commission.
6. Minimal stage/blocker/completion information returns to CRM.
7. Final outcome updates analytics and permitted attribution.

## VAULTED journey

Teaser → registration → profile/qualification → NDA → deal room → interest → agency/developer response → inventory validation → BluePrint transaction → close → attribution. Status returned to VAULTED is minimized by participant permissions.

## Learning journey

Role/entitlement creates assignment → LMS enrollment → learning/assessment → completion/certification webhook → reconciliation → BluePrint updates readiness → human/automation permits activation or access → expiry triggers reassignment.

## Developer journey

Due diligence → project agreement → data responsibility map → project/unit import → validation → distribution policy → agency enablement/training → inventory windows → demand → reservation/transaction → reporting and settlement.

## Handoff failure controls

| Failure | Control |
|---|---|
| Duplicate identity/opportunity | Namespaced external IDs, matching rules, merge audit |
| Lost webhook | Signed receipt, async queue, idempotency, retries, dead-letter and reconciliation |
| Stale inventory | Owner, timestamp, SLA, expiry, automatic visibility restriction |
| Wrong document version | Approved-current default, immutable prior bytes, invalidated approval on change |
| Unqualified access | Policy/state engine, evidence, expiry and revocation |
| Commission dispute | Effective rule version and calculation snapshot with inputs/approvals |
| AI creates unsafe change | Permission check, proposal preview, confirmation, audit and rollback |

