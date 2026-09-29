> [!IMPORTANT] Reconciled 2026-09-23 — read the precedence note first
> [[../01_Canon/00 - Precedence and Canonical Reconciliation|18 - Canonical Reconciliation and Precedence]] controls the vault. This folder is **one of three canonical layers**, not the sole authority:
>
> - `01_Canon/` — what the company **is**
> - `02_Offers/01_BluePrint/` — what the product **is**
> - `01_Canon/` — **this folder**: how it is **proven and financed** (finance models, data/AI architecture, operations, compliance, KPIs/gates, investor diligence)
>
> **Naming corrections that override this folder:** **Building Blocks** (not *Academy* / *B_Academy*) · **B_ Partner** (not *White-Label*) · **Dproperty Select** (not *Private Collection*) · **Developer Partnerships** (not *Developer Sales OS*).
>
> **Architecture decision — 2026-09-29 [D]:** BlankCRM owns full commercial execution through post-sale. BluePrint owns back-office management, financial verification, governance and intelligence; it observes the CRM without executing sales actions.

# Onboarding, Support, and Quality Assurance

## Standard implementation workplan

1. Commercial handoff and scope lock.
2. Legal entity/data/brand/intake questionnaire.
3. Organization, identity, roles, entitlements and MFA.
4. CRM/integration and field-ownership map.
5. Workflow, jurisdiction, template and commission pack.
6. Data migration/import with preview, validation, error report and rollback.
7. Building Blocks assignments and completion.
8. Test transaction and reconciliation.
9. Production activation approval.
10. 30/60/90-day stabilization and outcome review.

Standardization target: initial external BluePrint onboarding 20 hours in integrated base year 1, falling to 18/16 in years 2/3. The strategic target is median calendar implementation under 21 days. Exceptions are separately scoped and priced.

## Support severity

| Severity | Example | Response target hypothesis |
|---|---|---|
| S1 | Cross-tenant exposure, system unavailable, lost binding workflow | Immediate incident route; continuous until contained |
| S2 | Major transaction blocker/no workaround | Same business hour/priority |
| S3 | Function impaired/workaround exists | One business day |
| S4 | Question/configuration/enhancement | Queue and published target |

Targets become contractual only after staffing and pilot measurement.

## QA layers

- Automated unit/integration/e2e, migration, permission and financial-calculation tests.
- Tenant-isolation and IDOR/adversarial authorization tests.
- Workflow acceptance with realistic transaction fixtures.
- Template/document version and merge-field tests.
- Integration failure, retry, duplicate and reconciliation tests.
- AI grounding, leakage, hallucination, action-safety and prompt-injection evaluations.
- Backup restore, incident tabletop and disaster-recovery exercise.
- Operational file audits and support trend/root-cause review.

## Release gates

No release with unresolved critical security issue, failed tenant isolation, unreconciled financial calculation, lost audit trail, missing rollback, or untrained support owner. Every release has scope, owner, tests, migration, monitoring, customer communication and post-release review.

