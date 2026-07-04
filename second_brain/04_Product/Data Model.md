---
project: Dproperty OS
title: "Data Model"
type: product_note
status: Baseline Created
owner: Esteban
last_updated: 2026-07-01
source: ChatGPT baseline vault package
tags: [product]
---

# Data Model

## Core Objects

- Organization.
- User.
- Franchise.
- White-label client.
- Developer.
- Project.
- Unit.
- Client.
- Broker.
- Deal.
- Document.
- Projection.
- Commission.
- Training module.
- Support ticket.
- Private Collection request.
- Developer Sales OS project.

## Relationship Logic

- A franchise has many users, clients, brokers, deals, and reports.
- A project has one developer and many units.
- A deal connects a client, project/unit, franchise/agency, broker, and commission record.
- A Private Collection deal requires HQ approval.
- A projection is linked to a project, client, and assumptions.
- A document is linked to an object and a template.

## MVP Required Fields

Each object should have:

- Name.
- Owner.
- Status.
- Created date.
- Last updated.
- Responsible person.
- Notes.
- Related links.
