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

# BlankCRM — Standalone Product Record

## Executive summary

BlankCRM is a managed real-estate front-office package built on GoHighLevel. It provides standardized lead capture, marketing automation, communication, appointment scheduling, full commercial pipeline, templates, and integration to BluePrint. Its purpose is speed and adoption—not rebuilding a commodity CRM.

BlankCRM owns the full commercial lifecycle and works standalone. BluePrint optionally reads authorized evidence for management verification; secure legal archives retain authoritative originals and least-privilege access.

## Offer

- Workspace/sub-account setup, pipeline, fields, calendars, forms, templates and baseline automations.
- Integration mapping, signed webhooks, retries/reconciliation, lead/opportunity deduplication and read-only management ingestion.
- Defined managed support and template updates.
- Optional campaign setup, custom automation and migration quoted separately.
- SMS, WhatsApp, email, phone and premium AI usage prepaid or passed through to the customer.

## Economics hypothesis

| Item | Hypothesis |
|---|---:|
| Setup | $750 |
| Monthly managed package | $249/office |
| Underlying vendor reference | $497/month platform plus usage, shared across subaccounts where contract permits |
| Standalone base attach rate | 35% of B_ customers |
| Base COGS | 35% subscription and 35% setup |

The standalone base model estimates expected BlankCRM ARR/customer of **$1,045.80** across the whole B_ base after attach rate. Base year-5 BlankCRM revenue is **$342,102**. Actual margin depends on vendor terms, account volume, support, usage passthrough, taxes, and failure/abuse risk.

## Business model canvas

| Block | Design |
|---|---|
| Customer | Small agencies/franchises wanting fast, managed CRM operations |
| Value | Preconfigured full commercial workflows, standalone operation and optional management oversight |
| Channel | BluePrint implementation and franchise/partner launch |
| Revenue | Setup, monthly management, custom services; usage passed through |
| Partners | GoHighLevel, messaging/email/telephony providers |
| Costs | Platform license, usage, configuration, support, deliverability/compliance |

## Data and system boundary

Field ownership must be explicit. CRM owns contact marketing state, source/campaign, appointments, communication summaries, and commercial opportunity. BlankCRM owns transaction stages, legal workflow, documents, commercial approvals, payment milestones, closing, commissions and post-sale. BluePrint reads evidence and recommends management intervention; no sales-execution writeback. Deletions/merges, consent, opt-out, duplicate identities, expired credentials and failed webhooks require reconciliation.

## Risk and contingency

Vendor dependency, price changes, API limits, messaging policy, deliverability, number portability, data export, account suspension, and customer misuse. Maintain export procedures, configuration-as-code where practical, connector abstraction, account ownership terms, and an exit/migration playbook. Never represent the underlying platform as proprietary technology.

## Gates

Validate 10 managed accounts, <4 hours standard setup after templates mature, support burden within margin, standalone lead-to-post-sale completion and read-only management evidence ingestion, customer retention, and positive contribution after vendor/usage/support. If not, treat BlankCRM as optional referral/integration rather than a managed product.

