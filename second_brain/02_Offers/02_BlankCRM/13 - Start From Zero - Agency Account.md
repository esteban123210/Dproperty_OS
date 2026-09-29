---
project: B_RealEstate
title: "BlankCRM — Start From Zero: Agency Account"
type: founder_runbook
status: Ready for founder — account not yet created
owner: Esteban
last_updated: 2026-09-29
tags: [blankcrm, gohighlevel, beginner, setup]
---

# BlankCRM — Start From Zero: Agency Account

Precedence: [[../../01_Canon/00 - Precedence and Canonical Reconciliation]] · next: [[10 - Snapshot Release and Client Onboarding]].

**Current fact:** Esteban confirmed on 2026-09-29 that there is no GoHighLevel account yet. The first pilot is **Dproperty**, a Panama presale franchise with several projects and developer-direct reservation payments. Nothing in GoHighLevel has been built or tested. This page is the founder's first action list.

## Understand the three layers

1. **Agency account:** your BlankCRM business control panel. It owns the HighLevel subscription and lets you manage sub-accounts and snapshots.
2. **MASTER sub-account:** the clean product template we build once. It uses synthetic examples only.
3. **TEST and client sub-accounts:** TEST proves each snapshot release; each franchise office gets its own isolated client sub-account.

HighLevel may also offer a designated **Agency Sub-Account** for your own billing/SaaS operations. This is distinct from the agency account and must not be confused with the clean MASTER. Do not connect your client or agency payment provider to MASTER. [HighLevel account types](https://help.gohighlevel.com/support/solutions/articles/155000007979-what-is-an-agency-sub-account-in-highlevel-).

## Before starting a trial

- Decide who legally owns the subscription and who will be the permanent agency owner. Use a business-controlled email address that will remain accessible; do not use a freelancer's account.
- Have the agency business name, billing address and payment method ready. Keep passwords, codes and card details out of chat and the repository.
- Block time for the first two weeks of setup. HighLevel currently advertises a **14-day trial** on Agency Pro and says billing begins automatically afterward unless cancelled; usage charges may occur during the trial. Check the terms and total shown at checkout. [Official pricing](https://www.gohighlevel.com/pricing).
- Keep the first pilot details at hand: Dproperty, Panama, presale, two representative projects/developers and the sales/legal/finance decision owners. Other local rules can be completed while the master is being built, but must be approved before live contracts or payment messages.

## Founder signup steps

1. Open the [official HighLevel pricing page](https://www.gohighlevel.com/pricing).
2. Select **Agency Pro, monthly** as the working plan. The published price checked on 2026-09-29 is **$497/month after the trial**; it includes SaaS Mode, automated sub-account creation and rebilling with markup. The $297 Unlimited plan supports unlimited sub-accounts but not SaaS Mode. Verify the live checkout before accepting it. [Official pricing](https://www.gohighlevel.com/pricing).
3. Start the trial when ready to work on the master immediately. Enter agency identity, billing and login information yourself; review and accept any legal terms and payment commitment yourself.
4. Complete email verification and any multi-factor setup. Sign in and make sure you are in **Agency View**, not a client sub-account.
5. In Agency View, confirm that `Agency Pro` is the active plan and that `Sub-Accounts` and `Account Snapshots` are available. Note the trial end/renewal date and billing settings in your private business records.
6. Tell me only: **“I am in Agency View on Agency Pro.”** Do not send a password, code, card number or API key. I can then guide and verify the first live configuration steps.

## What we do together immediately after signup

1. Create `BlankCRM MASTER` as the clean configuration source and `BlankCRM TEST` as a separate disposable test location. If HighLevel asks whether a new location is your own Agency Sub-Account or a client's account, inspect the choice carefully; the designated billing account is **not** the snapshot source.
2. Create the fields, three associated custom objects, one transaction pipeline, work queues and workflows from [[12 - GoHighLevel Build Manifest]]. Keep external sends disabled until synthetic tests pass.
3. Create a snapshot from MASTER, load it into a fresh TEST location, run [[09 - Configuration Acceptance Tests]], then connect the Panama pilot's real channels and people in its own office sub-account.

**Do not buy add-ons or connect WhatsApp, AI, phone numbers, payment processors or client domains just because an onboarding wizard suggests them.** Each has an owner, use case, cost and test later in the runbook. The first successful milestone is a clean MASTER and TEST, not a live marketing campaign.
