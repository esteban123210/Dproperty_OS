> [!IMPORTANT] Reconciled 2026-09-23 — read the precedence note first
> [[../../01_Canon/00 - Precedence and Canonical Reconciliation|18 - Canonical Reconciliation and Precedence]] controls the vault. This folder is **one of three canonical layers**, not the sole authority:
>
> - `01_Canon/` — what the company **is**
> - `02_Offers/01_BluePrint/` — what the product **is**
> - `01_Canon/` — **this folder**: how it is **proven and financed** (finance models, data/AI architecture, operations, compliance, KPIs/gates, investor diligence)
>
> **Naming corrections that override this folder:** **Building Blocks** (not *Academy* / *B_Academy*) · **B_ Partner** (not *White-Label*) · **Dproperty Select** (not *Private Collection*) · **Developer Partnerships** (not *Developer Sales OS*).
>
> **Architecture decision — 2026-09-29 [D]:** BlankCRM owns full commercial execution through post-sale. BluePrint owns back-office management, financial verification, governance and intelligence; it observes the CRM without executing sales actions.

# BlankCRM — Investor Two-Pager

## 1. The idea in plain English

BlankCRM is a managed front-office package for small real-estate agencies, built on GoHighLevel rather than as a new proprietary CRM. B_ configures the workspace, lead capture, forms, calendars, pipeline, templates, baseline automations, communications, and the full commercial lifecycle, with optional read-only BluePrint oversight.

The strategic logic is speed: do not spend capital rebuilding commodity CRM features. Package a proven external platform around real-estate workflows and make full commercial execution repeatable and management observations reliable.

## 2. Customer, problem, and value

**Buyer:** small agency or franchise office that lacks a disciplined CRM or does not want to configure and manage one.

**Problem:** leads arrive through many channels, follow-up is inconsistent, and sales, legal, approvals, contracts, payments, closing and commissions are fragmented across people and tools.

**Value proposition:** a ready-to-use, managed real-estate acquisition stack with a clean boundary: BlankCRM owns full commercial execution through post-sale; BluePrint owns back-office management, verification, governance and intelligence.

## 3. Offer and boundaries

Included: sub-account/workspace setup, pipeline, fields, calendars, forms, legal/approval/contract/payment/closing/commission/post-sale configuration, baseline automations, optional read-only BluePrint feed with retries/deduplication/reconciliation, and defined support. The pilot must verify which actions are native, integrated or human-confirmed.

Separately priced or passed through: custom campaigns, complex migration, custom automation, WhatsApp/SMS/email/phone charges, premium AI use, advertising, and non-standard integrations.

BlankCRM must always be represented honestly as a managed package built on a third-party platform. B_ does not own the underlying CRM technology.

## 4. Revenue model and unit economics

| Economic item | Current hypothesis |
|---|---:|
| Setup fee | $750 per office |
| Managed subscription | $249/month per office |
| Annual recurring revenue per attached office | $2,988 |
| Underlying vendor reference | $497/month platform plus usage, shared where contract permits |
| Base attach rate | 35% of B_ customers |
| Modeled direct COGS | 35% of setup and subscription |

This historical model predates the full-lifecycle build. The pilot must measure legal, contract, payment and commission setup plus integrations and support before these prices or margins are treated as sale-ready. See [[03 - Offer and Pricing]].

At 35% COGS, one attached office generates modeled annual subscription gross profit of **$1,942.20** and setup gross profit of **$487.50**, before allocated sales, product, and corporate costs. Across the whole B_ customer base, a 35% attach rate yields expected BlankCRM ARR of **$1,045.80 per B_ customer**. Base year-5 BlankCRM revenue is modeled at **$342,102**.

These margins remain highly sensitive to vendor pricing, messaging usage, support tickets, account suspension, migration effort, taxes, and whether usage can be passed through. A managed account that consumes several hours of monthly support may be unprofitable even if software COGS looks acceptable.

## 5. Expanded business model canvas

| Block | Model |
|---|---|
| Customer segments | Small agencies, franchise offices, own-brand partners |
| Value proposition | Managed full-lifecycle CRM execution, standalone operation and optional BluePrint oversight |
| Channels | BluePrint implementation, franchise launch, partner bundles, direct referrals |
| Relationship | Setup, managed support, template updates, usage monitoring |
| Revenue | Setup, monthly management, custom services; vendor usage passed through |
| Key activities | Configuration, automation, integration, deliverability, support, reconciliation |
| Key resources | Templates, connector, implementation playbook, vendor expertise, support process |
| Key partners | GoHighLevel, messaging/email/telephony providers, ad platforms |
| Cost structure | Vendor license, usage, setup labor, support, deliverability/compliance, integration maintenance |

## 6. Competitive landscape

Customers can buy GoHighLevel directly or choose real-estate CRMs such as Follow Up Boss, Lofty, kvCORE, and Propertybase. HubSpot and Salesforce compete for customers willing to configure broader platforms. Agencies can also hire a marketing-automation freelancer.

BlankCRM does not have a credible standalone technology moat. Its differentiation is packaging: fast setup, real-estate templates, managed support, and an optional evidence feed into BluePrint. If that implementation advantage is not measurable, customers should buy the underlying tool directly.

## 7. Defensibility and risks

Limited defensibility comes from configuration IP, support knowledge, integration reliability, and bundled distribution. Vendor dependence is structural.

Main risks: vendor price/API changes; account suspension; deliverability; customer misuse; number portability; privacy/consent failures; thin support margin; configuration drift; and confusion that B_ owns the platform.

Mitigation requires exports, configuration-as-code where practical, connector abstraction, usage prepayment/passthrough, support limits, account-ownership terms, and a migration playbook.

## 8. What must be proven

- Ten active managed accounts.
- Measure whether standard setup can fall below four hours after templates mature; do not assume the pilot achieves it.
- Standalone full commercial lifecycle and read-only evidence reconciliation under failure conditions.
- Positive contribution after actual vendor, usage, setup, and support costs.
- Retention and attach rate by customer type.
- An exit path if the underlying vendor changes terms.

## Investor conclusion

**Useful attach product; not a standalone venture thesis.** BlankCRM can increase revenue per customer and reduce activation friction, but it should remain disciplined, transparent, and optional. If support burden destroys margin, switch to integration/referral rather than subsidizing a managed service.

## Competitive references

- Follow Up Boss: https://www.followupboss.com/
- Lofty CRM: https://lofty.com/real-estate/crm
- Propertybase: https://propertybase.lwolf.com/
