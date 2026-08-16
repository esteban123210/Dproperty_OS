---
project: B_RealEstate
title: "Web Presence and Funnel Architecture"
type: ecosystem_architecture
status: Canonical v1.0
owner: Esteban
last_updated: 2026-08-16
tags: [ecosystem, web, funnel, domains]
---

# Web Presence and Funnel Architecture

## Principle

Separate audiences and jobs. B_RealEstate sells partnerships; Dproperty serves investors; BluePrint operates the back office; VAULTED serves approved marketplace participants.

## Web properties

| Property | Audience | Primary job | Conversion |
|---|---|---|---|
| https://bfranchising.com | Agents, agencies, developers | Explain B_RealEstate and route to the correct commercial model | GoHighLevel model-specific pipeline / booked call |
| Dproperty consumer site | Investors and Dproperty clients | Explain the investment method and generate qualified investor demand | GoHighLevel investor pipeline |
| BluePrint portal | Contracted ecosystem users | Authenticate and operate the business | Role-based workspace |
| Open edX Academy | Provisioned learners | Deliver courses, assessments and certification | Completion status back to BluePrint |
| VAULTED | Invited buyers, brokers and sellers | Controlled off-market discovery and matching | Qualified marketplace introduction / BluePrint transaction |

## bfranchising.com sitemap

Recommended canonical navigation:

- Home
- Ecosystem
- Dproperty Franchise
- White-Label
- Developers
- BluePrint
- About
- Contact
- Log in
- Legal

The current `/franquicia` and `/franquicias` pair creates avoidable semantic and SEO confusion. Keep `/franquicia` for the branded model and rename `/franquicias` to `/modelos`, `/sistema` or another clearly different route with redirects.

## Funnel design

Every CTA must carry source page, model of interest, language, campaign attribution and consent into GoHighLevel. Maintain separate pipelines for branded, white-label and developer prospects. Booking and form completion should trigger model-specific information packs and internal assignment.

## Public claims policy

- Attribute Dproperty operating figures to Dproperty, not B_RealEstate.
- Do not imply that BluePrint, Academy, VAULTED or live integrations are complete unless demonstrable.
- Label demo data clearly.
- No payback, ROI, profit uplift or performance claim without a sourced model and disclaimer.
- Do not claim one shared database; describe a connected ecosystem with governed systems of record.

## Login principle

No public self-service BluePrint registration. Contracted users receive provisioned accounts, MFA and tenant/role-based access. White-label users should not be forced through a Dproperty-branded login experience.

## Naming on the web

Replace “La Plataforma” as a product name with **BluePrint**. The first mention may read “BluePrint, la plataforma de back office de B_RealEstate.” Replace “CRM propio” with “CRM white-label configurado sobre GoHighLevel.”

