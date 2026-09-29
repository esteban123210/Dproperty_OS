> [!IMPORTANT] Reconciled 2026-09-23 — read the precedence note first
> [[00 - Precedence and Canonical Reconciliation|18 - Canonical Reconciliation and Precedence]] controls the vault. This folder is **one of three canonical layers**, not the sole authority:
>
> - `01_Canon/` — what the company **is**
> - `02_Offers/01_BluePrint/` — what the product **is**
> - `01_Canon/` — **this folder**: how it is **proven and financed** (finance models, data/AI architecture, operations, compliance, KPIs/gates, investor diligence)
>
> **Naming corrections that override this folder:** **Building Blocks** (not *Academy* / *B_Academy*) · **B_ Partner** (not *White-Label*) · **Dproperty Select** (not *Private Collection*) · **Developer Partnerships** (not *Developer Sales OS*).
>
> **Architecture decision — 2026-09-29 [D]:** BlankCRM owns full commercial execution through post-sale. BluePrint owns back-office management, financial verification, governance and intelligence; it observes the CRM without executing sales actions.

# Ecosystem Customer Journeys and Handoffs

## Agency/partner journey

Discover → qualify → commercial proposal → agreement/payment → organization setup → identity/roles → CRM/data connection → Building Blocks assignments → template/workflow configuration → test transaction → production activation → weekly use/support → business review → renewal/expansion.

Critical handoff: commercial promise to implementation. The signed order form, entitlements, scope, exclusions, data migration, owners, dates and acceptance criteria become a structured onboarding record. Sales notes alone are not authority.

## Lead-to-close journey

1. CRM captures source, consent, contact and commercial opportunity.
2. The CRM continues qualification, legal workflow, commercial approvals, contracts, payment milestones, closing, commissions and post-sale.
3. If BluePrint is enabled, authorized events and evidence are read throughout the lifecycle, independently of stage.
4. BluePrint verifies management observations, reconciles expected vs actual cash, monitors usage and Glitches, and recommends intervention.
5. Authorized teams perform commercial corrections in the CRM. BluePrint reads the result and re-verifies; it does not change source transaction status.
6. BlankCRM-only customers complete the same commercial lifecycle without BluePrint.

## VAULTED journey

Teaser → registration → profile/qualification → NDA → deal room → interest → agency/developer response → inventory validation → BlankCRM/chosen-CRM transaction → close → attribution. Status returned to VAULTED is minimized by participant permissions.

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

