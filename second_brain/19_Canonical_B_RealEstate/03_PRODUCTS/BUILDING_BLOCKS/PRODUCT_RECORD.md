# Building Blocks — Standalone Product Record

## Executive summary

Building Blocks is B_RealEstate's learning, onboarding, and certification business. It turns operating standards into role-based curricula and preserves assignment, completion, certification, expiry, and competency evidence. It should use an external LMS/Open edX; BluePrint displays status and may gate activation or privileges.

It is not a document repository for daily transactions, an unaccredited promise of formal qualifications, or a substitute for licensed legal/compliance training where required.

## Audiences and jobs

- New franchise/partner teams: reach launch readiness consistently.
- Agents/coordinators: learn current workflow and product-specific execution.
- Managers: identify competency gaps and enforce continuing standards.
- Developers: educate agencies on project/inventory/process.
- External professionals: buy focused, practical courses/certifications.

## Product architecture

| Layer | Content | Monetization |
|---|---|---|
| Core onboarding | Brand/operating standards, BluePrint/CRM workflow, qualification, diligence, documents/compliance, closing/commission | Included for defined franchise users |
| Paid specialist courses | Investing, project sales, compliance operations, leadership, advanced product | $199 blended enrollment hypothesis |
| Certification | Assessment, evidence, expiry/renewal, role or inventory gate | Enrollment/program fee |
| Enterprise/developer academy | Branded cohort, project training, manager dashboards | Scoped license/setup |
| Events/coaching | Live instruction, masterclasses, executive support | Separately priced |

## Business model canvas

| Block | Design |
|---|---|
| Customer | Agencies, franchises, developers, individual professionals |
| Value | Faster onboarding, consistent execution, evidence of competence, qualified pipeline |
| Channel | Product onboarding, partner contracts, public content, professional referrals |
| Revenue | Enrollment, cohort, certification renewal, enterprise program, events |
| Resources | Curriculum IP, instructors, assessments, LMS, completion data |
| Costs | Content production, instructors, platform, support, assessment, marketing |

## Source-of-truth and integration

The LMS owns course content and detailed learning activity. BluePrint owns required-course policy, role/organization context, activation gates, and a synchronized completion/certification record. Webhooks or reconciliation jobs use stable user/course IDs, version, completion date, expiry, evidence, retry state, and audit events.

## Metrics

Enrollment-to-start; completion; assessment pass; time-to-competence; activation time; workflow error before/after; paid conversion; learner acquisition cost; gross margin; renewal; content freshness; instructor dependency; sourced pipeline and influenced revenue.

## Standalone model

The isolated model assumes a **$199 blended paid enrollment**, excluding free franchise onboarding. Base case assumes **1.5 paid enrollments per active customer per year** and 25% COGS. Year-5 Building Blocks revenue is modeled at **$84,159** in the base case. This is supplemental revenue and activation infrastructure, not the core valuation engine.

## Roadmap and gates

Start with six core modules and two paid specialist courses. Validate one paid external cohort, completion above 60%, measurable workflow improvement, content delivery within budget, and repeat demand. Do not build a custom LMS. Stop producing broad content if paid acquisition exceeds gross profit or training does not improve activation/retention.

## Naming decision

Earlier technical documents use `B_Academy`. Current commercial naming uses `Building Blocks`. Select one primary customer-facing name, secure trademark/domain rights, and treat the other as a descriptor or legacy alias.

