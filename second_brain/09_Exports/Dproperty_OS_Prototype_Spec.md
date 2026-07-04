# Dproperty OS — Prototype Specification for Figma

## Prototype goal
Create a premium, calm, boutique real estate operating platform. The product should feel like a private investment office crossed with a modern operating system: elegant, structured, and extremely clear.

The Figma prototype should show three experiences:
1. **HQ Control Center** — Dproperty headquarters manages franchises, white-label clients, developer projects, templates, Private Collection, and performance.
2. **Franchise / Agency Workspace** — a local operator manages clients, brokers, projects, deals, documents, projections, and follow-ups.
3. **Developer Sales Dashboard** — a developer sees project sales performance, team activity, broker network activity, and Dproperty-managed process quality.

## Visual identity
- Background: warm off-white (#F6F3ED).
- Text: charcoal (#161616).
- Accent: muted deep blue (#1F4E79).
- Secondary accent: champagne/gold (#B89B5E).
- Success: muted green (#4C7A5A).
- Warning: soft amber (#C58A2A).
- Error: muted red (#A94B4B).
- Typography: editorial serif for major headings; clean sans-serif for UI text.
- Avoid a generic SaaS look. The interface should feel like a boutique operating desk, not a tech dashboard template.

## Global navigation
Left sidebar:
- Home
- Clients
- Brokers
- Developers
- Projects
- Units
- Deals
- Documents
- Projections
- Private Collection
- Training Academy
- Dashboards
- Settings

Top bar:
- Global search: “Search client, project, document, deal…”
- Create button: “New” with menu for Client, Broker, Project, Deal, Document, Projection
- Notifications
- User profile
- Tenant switcher for HQ users

## User roles

### HQ Admin
Can manage all tenants, templates, pricing rules, Private Collection, global dashboards, and franchise compliance.

### Franchise Principal
Can manage local team, local clients, local brokers, local deals, local reporting, and access approved Private Collection opportunities.

### Sales Advisor
Can manage assigned clients, deals, tasks, documents, and projections.

### Developer Manager
Can view developer project sales dashboards, pipeline, broker activity, and Dproperty recommendations.

### Legal / Compliance
Can approve templates, clauses, signed documents, broker agreements, and jurisdiction-specific variations.

### Finance
Can see commissions, royalties, splits, payments, and projected fees.

## Core data model

### Client
Fields: name, email, phone, country, nationality, budget, preferred market, investment objective, risk profile, assigned advisor, NDA status, client agreement status, notes, documents.

### Broker
Fields: broker name, company, country, agreement type, NDA status, commission split, authorized projects, deals introduced, payment status, performance score.

### Developer
Fields: developer name, country, contact person, active projects, sales model, Dproperty package, agreement status, dashboard access.

### Project
Fields: project name, developer, country, city, status, project type, average unit price, total units, available units, payment plan, commission pool, marketing assets, legal documents, investment thesis, risk notes.

### Unit
Fields: unit number, floor, size, price, availability, payment plan, expected rent, projected yield, status, linked project.

### Deal
Fields: client, project, unit, advisor, broker, deal source, stage, expected commission, commission split, Private Collection flag, reservation status, payment status, approval status, signed documents.

### Document
Fields: document type, template version, linked client/deal/broker/project, status, approver, signature status, signed file, expiry date.

### Projection
Fields: project, unit, purchase price, rental assumptions, occupancy, operating costs, appreciation, exit year, conservative/base/optimistic outputs, disclaimer status.

## Main screens

### 1. HQ Home Dashboard
Purpose: show overall company performance.

Blocks:
- KPI strip: Active franchises, white-label agencies, developer projects, monthly recurring revenue, projected annual revenue.
- Revenue mix chart: Franchise, white-label, developer sales, Private Collection.
- Franchise map/list: country, status, revenue, compliance score.
- Alerts: expired templates, unsigned agreements, developer project at risk, franchise below activity threshold.
- Quick actions: Create franchise, approve template, onboard developer, publish Private Collection project.

### 2. Franchise Workspace Home
Purpose: daily operating screen for the franchise.

Blocks:
- My active deals.
- Follow-ups due today.
- Documents missing.
- Private Collection opportunities.
- Local pipeline by stage.
- Commission forecast.
- Training completion of team.

### 3. Client Profile
Tabs:
- Overview
- Preferences
- Deals
- Documents
- Projections
- Notes & activity

Important interactions:
- Generate NDA.
- Generate client agreement.
- Recommend projects.
- Create projection.
- Create deal.

### 4. Project Profile
Tabs:
- Overview
- Units
- Payment plan
- Documents
- Sales arguments
- Investment thesis
- FAQs
- Deals
- Brokers authorized

Important interactions:
- Update availability.
- Generate project memo.
- Add to Private Collection.
- Publish to franchise network.

### 5. Deal Detail
This is the core screen.

Header:
- Client name
- Project + unit
- Stage
- Expected commission
- Private Collection flag

Sections:
- Deal timeline
- Required documents checklist
- Projection summary
- Broker involvement
- Commission split
- Approvals
- Next actions

Primary actions:
- Generate document
- Generate projection
- Request approval
- Send for signature
- Move stage
- Mark as reserved / closed

### 6. Document Generator
Flow:
1. Select document type.
2. Select client/broker/project/deal.
3. Confirm variables.
4. Select jurisdiction.
5. Insert optional approved clauses.
6. Preview document.
7. Request approval.
8. Send for signature.
9. Archive signed version.

Design note: This should feel like a guided wizard, not a blank editor.

### 7. Projection Generator
Flow:
1. Select client + project + unit.
2. Pull price and payment plan automatically.
3. Show assumptions: rent, occupancy, operating costs, appreciation, exit year.
4. Show conservative/base/optimistic cases.
5. Generate client-friendly PDF.
6. Attach to deal.

Important UI details:
- Blue editable assumption fields.
- Locked HQ assumptions marked with lock icon.
- Warning if assumptions exceed approved range.

### 8. Private Collection
Purpose: controlled HQ-curated inventory.

Cards/list items:
- Project name
- Country/city
- Average unit price
- Commission pool
- Investment thesis
- Authorized franchises
- Senior HQ manager
- Status

Actions:
- Request access
- Create investor memo
- Create client projection
- Submit buyer lead to HQ

### 9. Developer Sales Dashboard
Purpose: developer can see sales without managing the whole process manually.

Blocks:
- Project overview: total units, sold, reserved, available.
- Pipeline funnel: leads, qualified leads, visits, offers, reservations, closed.
- Sales by source: internal team, Dproperty HQ, broker network, franchise network.
- Salesperson performance.
- Broker performance.
- Projected sell-out date.
- Dproperty fees payable.
- Recommendations from Dproperty.

### 10. Training Academy
Structure:
- Sales Advisor Certification
- Broker Manager Certification
- Projection Certification
- Developer Sales Certification
- Legal/Documents Certification

Each module should show:
- Progress
- Lessons completed
- Quiz/test status
- Certification status
- Required before user can perform certain actions

### 11. HQ Template Control
Purpose: legal/document governance.

Screens:
- Template library
- Clause library
- Jurisdiction variants
- Version history
- Approval status
- Usage analytics

Important interaction:
- HQ can push template updates to all tenants.
- Local adaptations require approval.

## Key user journeys to prototype

### Journey A: Franchise creates a new client and generates an NDA
1. Franchise user clicks New Client.
2. Completes client profile.
3. System creates client folder.
4. User clicks Generate NDA.
5. System fills approved template.
6. Legal approval if needed.
7. Send for signature.
8. Signed NDA archived and client status updated.

### Journey B: Franchise sells Private Collection project
1. Advisor opens Private Collection.
2. Selects Panama project.
3. Requests client match.
4. Creates deal.
5. HQ senior manager is automatically assigned.
6. Projection generated.
7. Deal commission split shows 50/50 HQ/franchise logic.
8. Deal moves to reservation.

### Journey C: Developer sees project sales performance
1. Developer logs in.
2. Opens Project X dashboard.
3. Sees units sold, pipeline, team activity, broker source performance.
4. Dproperty recommendations appear.
5. Developer downloads weekly sales report.

### Journey D: HQ monitors franchise network
1. HQ admin opens Control Center.
2. Sees all franchises and compliance score.
3. Flags franchise with missing broker agreements.
4. Pushes updated broker agreement template.
5. Dashboard updates after template adoption.

## Prototype screens list
Minimum Figma screens:
1. Login / tenant selector
2. HQ Control Center
3. Franchise Workspace Home
4. Client List
5. Client Profile
6. Project List
7. Project Profile
8. Private Collection
9. Deal Detail
10. Document Generator Wizard
11. Projection Generator
12. Developer Sales Dashboard
13. Training Academy
14. Template Control / Clause Library
15. Finance / Commission Dashboard
16. Settings / Permissions

## Figma prompt
Design a premium boutique real estate operating platform called Dproperty OS. The product is used by headquarters, franchisees, white-label agencies, and developers. It should feel calm, editorial, high-end, and operationally precise. Avoid a generic SaaS dashboard look. Use warm off-white backgrounds, charcoal text, muted deep blue, and champagne accents. Create screens for HQ Control Center, Franchise Workspace, Client Profile, Project Profile, Deal Detail, Document Generator, Projection Generator, Private Collection, Developer Sales Dashboard, Training Academy, and Template Control. The core experience should show how data becomes documents, documents move through approvals, signed files return to the archive, and dashboards update automatically.
