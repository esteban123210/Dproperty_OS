---
project: B_RealEstate
title: "Figma Handoff Notes"
type: product_note
status: Baseline Created
owner: Esteban
last_updated: 2026-08-16
source: ChatGPT baseline vault package
tags: [product]
---

# Figma Handoff Notes

> **Naming and scope update (2026-08-16):** The platform is **BluePrint**, part of **B_RealEstate**. GoHighLevel remains the CRM, Open edX the Academy technology, and VAULTED the off-market marketplace. The canonical boundaries live in [[../18_Ecosystem/00 - Ecosystem Master Map]] and [[../18_Ecosystem/12 - System of Record and Integration Matrix]].

## Goal

Translate the product specs into a clickable Figma prototype.

## First Screens

1. Login / workspace selector.
2. HQ Dashboard.
3. Franchise Dashboard.
4. Client List.
5. Client Profile.
6. Project List.
7. Project Profile.
8. Deal Pipeline.
9. Deal Detail.
10. Private Collection Request.
11. Projection Generator.
12. Commission Tracker.
13. Training Dashboard.

## Design Principles

- Clean, premium, quiet.
- Not too many colors.
- Strong hierarchy.
- Simple tables.
- Clear status pills.
- Good mobile/tablet readability.
- Real estate visuals should be curated, not cluttered.

## Claude/Figma Prompt Use

Use Claude for long UX copy and Figma prompt drafting. Use ChatGPT for product logic and data model.

## 2026-07-18 Update — Platform Architecture & Priority Screens

Full platform architecture is now in [[Platform Information Architecture]]. Before the OS screens above, the wireframe also needs the **public site** (Home, About, Services, Become-a-Franchise hub) and two **always-on top-bar elements** (Command Bar + Report a Glitch) present on every OS screen.

**Recommended first wireframe set (priority, not all at once):**
1. Public Home (dual CTA: client vs franchise)
2. "Become a Franchise" hub page
3. Login / workspace selector
4. Franchise Workspace Home (with Command Bar + Glitch button)
5. Deal Detail
6. Resource Library
7. Glitch Report + Glitch Feed

Then extend to the remaining OS modules and back-office systems. See [[Platform Scenario Playbook]] for the flows each screen must support and [[Roles and Access Matrix]] for what each role sees.
