---
project: B_RealEstate
title: "Handoff - Ecosystem Website"
type: handoff
deliverable: "B_RealEstate company website — the franchising ecosystem (B2B)"
target_output: "Responsive marketing site, Lovable build"
target_tool: "Lovable (primary) — Framer/Webflow/v0 acceptable"
source_notes: ["01_Strategy/Brand Architecture.md (v0.1)", "04_Product/Public Site Wireframe.md (v0.6)", "05_Franchise_Package/Pre-Signing/Franchisee Acquisition Playbook.md"]
version: 1.0
status: "Live at bfranchising.com — audit corrections required"
owner: Esteban
created: 2026-08-03
last_updated: 2026-08-16
tags: [handoff, production, website, franchise, ecosystem, lovable]
---

# HANDOFF — Ecosystem Website (B_RealEstate)

> **Live-site/naming update (2026-08-16):** B_RealEstate and BluePrint are the active names; https://bfranchising.com is live. This handoff remains production history. Before further build work, use [[../18_Ecosystem/15 - Website Audit - bfranchising.com - 2026-08-16|the live-site audit]] and [[../18_Ecosystem/14 - Unit Economics Registry|the economics registry]] as the correction list.

> **Self-contained package** to build the **parent company's B2B site**: the franchising ecosystem for real estate. This site sells **three service lines** to partners. It is **not** the Dproperty consumer site — that is a separate build ([[Handoff - Public Website]]).
>
> `B_RealEstate` = parent ecosystem. `BluePrint` = platform. `[MOCK]` = replace before publication.
> **Language:** Spanish-first, EN toggle. **Audience:** agents, agency owners, developers — not homebuyers.

## 0. Production Brief

- **Deliverable:** responsive B2B marketing site, ~8 pages, Spanish-first + EN toggle.
- **Audience:** three distinct buyers. The site's central job is to **route them fast** without making any of the three feel like the afterthought.
- **Core message:** *Join a real estate ecosystem — and decide how much of our brand you want.*
- **Non-goal:** this site does not sell property. Property/investor traffic goes to the Dproperty brand site.
- **Fidelity:** boutique, editorial, calm, credible. Fewer, better images. Generous whitespace.
- **Integrations:** GoHighLevel — **three separate CRM pipelines** (branded franchise · white-label · developer).

## 1. The Two-Site Architecture (read first)

| Site | Brand | Audience | Sells | Status |
|---|---|---|---|---|
| **bfranchising.com** | Parent | Agents, agency owners, developers | The three partnership lines | **This handoff — build now** |
| **dproperty.com** | Dproperty (flagship) | Buyers, sellers, investors | Property, advisory, Select | [[Handoff - Public Website]] v1.0 — re-scoped, build later |

Cross-links: Dproperty site keeps a *"Dproperty is part of B_RealEstate"* footer line and a "Become a partner" banner → this site. This site references Dproperty as **proof and as an option**, and links out to it as a live showcase.

## 2. Design & Brand Direction

Inherits the Dproperty visual system for now (a deliberate choice — the parent should feel like the source of the boutique standard, not a different company). Revisit at naming.

- **Palette:** background off-white `#F6F3ED` · text charcoal `#161616` · accent deep blue `#1F4E79` · secondary champagne `#B89B5E`.
- **Type:** editorial **serif** headlines · clean **sans-serif** body.
- **Feel:** boutique, calm, editorial, credible. Champagne accents on line-art diagrams. No stock-photo handshakes, no franchise-expo energy.
- **Header (sticky, minimal):** `B_RealEstate` · Ecosistema · Franquicias · White-Label · Desarrolladores · BluePrint · Nosotros · ES/EN · [Iniciar sesión] (ghost) · [Agendar llamada] (champagne, primary).
- **Footer:** *"Un ecosistema de franquicias para el sector inmobiliario."* · Marcas (Dproperty) / Compañía / Contacto · © · Privacidad · Términos · Aviso de inversión.

## 3. Tone Rules (non-negotiable)

1. **We are the ecosystem; Dproperty is our flagship brand.** Never write as if the company is Dproperty.
2. **Sell experience, not a logo.** *"Join everything our experience built"* — not *"buy our brand."*
3. **Two doors, no consolation prize.** Branded and white-label are presented as **equal, different choices**. White-label must never read as the cheap tier.
4. **Freedom is the differentiator.** *We provide the tools and walk beside you — the brand can still be yours.*
5. **Premium but reachable.** *"We are the best, but we are reachable."*
6. **Numbers over hype.** *Somos más amigos de la matemática que de la arquitectura.*

## 4. Sitemap

```
INICIO · EL ECOSISTEMA · FRANQUICIA DPROPERTY · WHITE-LABEL ·
DESARROLLADORES · LA PLATAFORMA (BluePrint) · NOSOTROS · CONTACTO · LEGAL · LOGIN
```

---

## 5. Page Specs

### PAGE 1 — INICIO

```
┌──────────────────────────────────────────────────────────┐
│ HERO — headline + subhead + primary CTA                  │
├──────────────────────────────────────────────────────────┤
│ TRUST STRIP — 2017 · $200M+ · 700+ ops · 99%+ · 80%+     │
├──────────────────────────────────────────────────────────┤
│ THE THREE DOORS (3 cards — the core routing block)       │
├──────────────────────────────────────────────────────────┤
│ THE FOUR PILLARS (why us)                                │
├──────────────────────────────────────────────────────────┤
│ PROOF — the Select uplift + Dproperty as flagship        │
├──────────────────────────────────────────────────────────┤
│ WHAT'S IN THE ECOSYSTEM (tools grid)                     │
├──────────────────────────────────────────────────────────┤
│ THE VISION strip (hub / north-star) → Ecosistema         │
├──────────────────────────────────────────────────────────┤
│ CTA — Agendar una llamada                                │
└──────────────────────────────────────────────────────────┘
```

**Hero headline:** *Un ecosistema de franquicias para el sector inmobiliario.*
**Subhead:** *Te damos el método, la tecnología, la formación y la red que construimos desde 2017 — y tú decides cuánto de nuestra marca quieres usar.*
**CTAs:** `[ Agendar una llamada ]` · `[ Ver las tres vías ]`
**Tagline:** *Somos más amigos de la matemática que de la arquitectura.*

**Trust strip:** *Desde 2017 · +$200M transaccionados · +700 operaciones · +99% de nuestros clientes nunca perdió capital · +80% vuelve a invertir.*
> Framing note: these are **Dproperty's** numbers. Label them honestly — *"Los números de Dproperty, nuestra marca insignia."* Do not present them as the parent's franchise track record.

**THE THREE DOORS** — the most important block on the site. Three equal cards, same height, same weight:

| | **Franquicia Dproperty** | **White-Label** | **Desarrolladores** |
|---|---|---|---|
| Line | *Opera bajo nuestra marca.* | *Opera bajo la tuya.* | *Tu equipo comercial, sin construirlo.* |
| Focus | *Inversión, exclusivamente.* | *Tu mercado, tus reglas.* | *Tu producto, nuestro equipo.* |
| For | Quien quiere vender inversión inmobiliaria con la credibilidad de una marca con más de una década de trayectoria. | Quien ya tiene marca — o quiere construir la suya — con nuestro sistema detrás, y libertad de enfoque. | Desarrolladores que tienen el producto, no el equipo. |
| CTA | Conocer la franquicia | Conocer white-label | Hablar con nosotros |

> **Copy rule for this block:** the difference is **not** price tiers. It is **brand + focus**. Dproperty = investment-only, under our name, with our recognition. White-label = your name, your focus, our system. Never imply one is the entry-level version of the other.

**THE FOUR PILLARS:**
1. **La promesa boutique.** *Todo se apoya en la forma de trabajar de Dproperty: curaduría sobre volumen, números sobre ruido, confianza sobre transacción.*
2. **Franquicia a tu manera.** *Damos las herramientas y acompañamos el proceso — la marca puede seguir siendo tuya.*
3. **Las herramientas ya existen.** *Plataforma BluePrint, CRM white-label, agentes de IA, academia, eventos de networking, acceso a Dproperty Select, plantillas y manuales.*
4. **Es un modelo probado.** *Nuestros socios han aumentado su rentabilidad simplemente sumando Dproperty Select a lo que ya ofrecían a sus clientes.*

**PROOF block:** *No vendemos un brochure. Vendemos la entrada a todo lo que la experiencia de Dproperty construyó.* + Dproperty flagship card (2017, Panama, landmarks: Bioma · Mova · Cavarrosa · Nayamara · Playa Escondida · La Maison by Fendi) + `[MOCK — pending substantiation]` one partner uplift stat.

**TOOLS GRID (8):** Plataforma BluePrint · CRM white-label · Agentes de IA · Academia · Eventos y red · Dproperty Select · Manuales y plantillas · Acompañamiento de lanzamiento.

---

### PAGE 2 — EL ECOSISTEMA

Hero: *No estás comprando una marca. Estás entrando a un ecosistema.*
- **The house-of-brands diagram:** `B_RealEstate` → Dproperty (marca insignia) · White-label partners · Desarrolladores · BluePrint (la plataforma que lo conecta).
- **Explicit framing:** *Dproperty es nuestra marca insignia — la prueba de que el modelo funciona, y una de las formas en que puedes operar. No es quiénes somos; es lo que construimos.*
- **En lo que no transigimos (6):** Boutique siempre · Confianza y números · La inversión primero · Calidad sin concesiones · Talento por encima del tamaño · Más grande que nosotros.
- **The north star:** the curated physical hub — *el alma de un lugar como 19M, aplicada a los bienes raíces.* Fase 1 — el ecosistema de franquicias (hoy) · Fase 2 — el hub. **¿Por qué Panamá?** (6 reasons).
- **Founding-member framing:** *Cada socio de esta primera generación es miembro fundador del ecosistema.*
- CTA: Súmate al ecosistema.

---

### PAGE 3 — FRANQUICIA DPROPERTY

```
HERO → LA MARCA DE INVERSIÓN → PARA QUIÉN ES → QUÉ INCLUYE → TU CAMINO →
INVERSIÓN Y RETORNO → DPROPERTY SELECT → TERRITORIOS → FAQ → CTA
```
**Hero:** *Ten tu propia Dproperty. Lleva la inversión inmobiliaria boutique a tu mercado — con nuestra marca, nuestro sistema, nuestra formación y nuestra red detrás de ti.*
**CTAs:** `[ Agendar una llamada ]` · `[ Descargar información ]`

**LA MARCA DE INVERSIÓN (new block — the identity of the brand, must sit high on the page):**
> **Dproperty no es una marca inmobiliaria general. Es una marca de inversión.**
>
> *Nuestros clientes no compran para vivir: compran para rentabilizar. Un inversionista que llega con $50,000 puede comprar una o dos propiedades sin la presión de una hipoteca, porque la unidad es revendible — y si toma hipoteca, es para alquilar.*
>
> *Por eso una franquicia Dproperty busca producto **rentable y confiable**, no necesariamente bonito y habitable. Entre dos edificios comparables, el de mejores acabados suele ser el producto equivocado para nosotros: mejores materiales significan un punto de entrada más alto, y un punto de entrada más alto significa menor retorno.*
>
> *Vendemos y alquilamos a usuario final cuando hace falta — dentro de nuestros círculos o con brokers aliados — pero la identidad y el enfoque siempre miran al inversionista.*

**Para quién:** agentes que quieren independizarse y **especializarse en inversión** (primario) · profesionales de ventas de otros sectores (secundario) · jóvenes emprendedores. *Si tu mercado es el comprador de vivienda para habitar, tu camino probablemente es white-label — y te lo diremos.*
**Qué incluye:** marca Dproperty y manuales · Plataforma BluePrint · CRM white-label · Academia · agentes de IA · **acceso completo a Dproperty Select** · plantillas legales y comerciales · plan de lanzamiento 30/60/90 · acompañamiento y reporting de HQ · prioridad de inversión y red internacional.
**Tu camino:** Descubre → Aplica → Firma → Onboarding → Lanzamiento.
**Inversión y retorno:** `[pull from Pricing Model / Unit Economics — DO NOT retype]` · $30,000 fundador → $40,000 · $1,000/mes · 6% royalty + 1.5% Network & Brand Fund sobre GCI **cobrado** · Dproperty Select **2.5% del precio de venta**.
> ⚠️ Publication decision pending — see §8. Default: show *"desde $30,000"* and gate the detail behind the info pack.
**Select block:** *Acceso a oportunidades curadas y fuera de mercado que la mayoría nunca ve — la ventaja que más rápido cambia la rentabilidad de un socio.* **Las franquicias Dproperty transaccionan Select al 2.5% del valor de venta** — frente al 1.5% de un broker aliado externo.

**THE PAYBACK BLOCK (new — put this immediately after Inversión y Retorno):**
> *¿Por qué la franquicia Dproperty cuesta más?*
>
> *Porque no compras solo el conocimiento y las herramientas — eso también está en white-label. Compras **una marca con más de una década de trayectoria**, y **un punto completo más en Dproperty Select**.*
>
> | | Franquicia Dproperty | White-label |
> |---|---|---|
> | Comisión Select | **2.5%** | 1.5% |
> | En una unidad de $300,000 | **$7,500** | $4,500 |
> | Diferencia | **+$3,000 por unidad** | |
>
> *La diferencia en la inversión inicial se recupera en aproximadamente **siete operaciones Select**. A partir de ahí, la marca se paga sola.*
>
> **Design note:** render as a clean editorial table, champagne accent on the delta row. This is the single most persuasive block on the site — give it room. It is the *más amigos de la matemática* argument made literal.
**Territorios:** map. Panamá · Bogotá · Medellín abiertos. **Prueba:** *Testimonios muy pronto — podrías ser parte de nuestra primera generación.*
**FAQ (source: [[../05_Franchise_Package/Pre-Signing/Franchisee Acquisition Playbook]] objection scripts):** financiamiento · experiencia previa · por qué no hacerlo solo · tiempos · exclusividad territorial · qué pasa si no funciona.

---

### PAGE 4 — WHITE-LABEL

**This page must feel as premium as Page 3.** Different door, not lesser door.

```
HERO → LA IDEA → PARA QUIÉN → QUÉ INCLUYE (y qué no) →
CÓMO SE COMPARA → PLANES → TU CAMINO → FAQ → CTA
```
**Hero:** *Tu marca. Nuestro sistema.*
**Subhead:** *Construye tu agencia a tu manera — con la tecnología, el método, la formación y la red que nos tomó años construir. La marca que crezcas es tuya.*
**La idea:** *No todos quieren operar bajo otra marca, y está bien. Te damos las herramientas y te acompañamos en el proceso; tú decides cómo se llama, cómo se ve y hacia dónde va.*

**TU ENFOQUE, TUS REGLAS (new block — the real freedom):**
> *La franquicia Dproperty opera con un mandato estricto: inversión, exclusivamente. White-label no tiene ese límite.*
>
> *Si tu mercado son familias comprando su casa, producto de mejores acabados, o desarrollo pensado para habitar — eso es perfectamente válido, y con white-label puedes perseguirlo. Recibes el mismo sistema, la misma tecnología y la misma formación, aplicados al mercado que tú elijas.*

**RESPALDADOS, NO ABSORBIDOS:**
> *Te acompañamos y te respaldamos públicamente: puedes decir **"powered by Dproperty."** Es respaldo, no identidad. La marca que construyas es tuya, y el valor que le agregues se queda contigo.*

**Para quién:** agencias boutique que quieren profesionalizarse · operadores con marca propia y red local · quien quiere construir algo suyo sin empezar de cero · **quien quiere servir a usuario final, no solo a inversionistas**.
**Qué incluye:** Plataforma BluePrint · CRM white-label bajo tu marca · Academia · agentes de IA · flujos, manuales y plantillas · dashboards y lógica de proyección · **acceso a Dproperty Select como broker aliado (1.5% del valor de venta)** · respaldo "powered by Dproperty" · implementación acompañada · eventos y red.
**Qué no incluye:** la marca Dproperty ni su trayectoria · prioridad de inversión · relaciones directas con desarrolladores del grupo · el payout preferente de Select (2.5%).

**Comparación honesta (side-by-side table — build this, don't hide it):**

| | Franquicia Dproperty | White-Label |
|---|---|---|
| Marca | Dproperty | La tuya |
| Reconocimiento | +10 años de trayectoria | Respaldo *"powered by Dproperty"* |
| Enfoque | Inversión, exclusivamente | Tú decides |
| Plataforma, CRM, IA, Academia | ✓ | ✓ |
| Dproperty Select | **2.5%** del valor de venta | 1.5% (broker aliado) |
| Prioridad de inversión | ✓ | — |
| Equity de marca | De Dproperty | **Tuyo** |
| Inversión inicial | desde $30,000 | desde $10,000 |

> Honest comparison builds more trust than hiding the trade-off — and the "brand equity is **yours**" row is genuinely a *win* column for white-label. Make sure it reads that way visually.
**Planes:** Starter — $10,000 setup / $1,500 mes · Growth — $20,000 setup / $2,500 mes. Add-ons: formación a medida, implementación extra, dashboards avanzados, integraciones, plantillas legales localizadas.
**CTA:** Agendar una llamada → **white-label CRM pipeline**.

---

### PAGE 5 — DESARROLLADORES

**Repositioned — this is the biggest content change on the site.** Not an outsourced sales desk. A **dedicated team that stays with the developer across all their projects.**

```
HERO → EL PROBLEMA → NUESTRA PROPUESTA → POR QUÉ ES DIFERENTE →
QUÉ HACEMOS → NIVELES → CÓMO TRABAJAMOS → PRUEBA → CTA
```
**Hero:** *Tu equipo comercial, sin construirlo desde cero.*
**Subhead:** *Un equipo dedicado que aprende el alma de tu producto y te acompaña proyecto tras proyecto — con nuestro método, nuestra tecnología y nuestra red detrás.*

**El problema:** *Tienes el producto. Construir una operación de ventas profesional — contratar, formar, sistematizar, controlar el pipeline, reportar — es otro negocio completamente distinto. Y hacerlo mal te cuesta la marca y el margen.*

**Nuestra propuesta:** *No te damos un equipo genérico. Te damos un equipo que se queda contigo: que entiende tu producto, tu comprador y tus estándares, y que lleva ese conocimiento de un proyecto al siguiente.*

**Por qué es diferente (the core differentiator block — 4 points):**
1. **Continuidad, no rotación.** *El mismo equipo te acompaña en todos tus proyectos. Lo que aprenden no se pierde.*
2. **Entienden el alma del producto.** *No vendemos con un brochure en la mano. Entendemos qué estás construyendo y por qué.*
3. **Cuidamos tu marca y tus números.** *Sin proyecciones no aprobadas, sin descontar tu producto para cerrar rápido.*
4. **No somos una agencia más.** *Es una alianza, más cerca de un white-label que de un contrato de comercialización.*

**Qué hacemos:** CRM y pipeline · proceso comercial · formación del equipo · activación y disciplina de brokers · scripts y presentación de proyecto · reporting para dirección e inversionistas · soporte de proyecciones · **demanda calificada desde nuestra red y nuestra base de inversionistas**.
**Niveles (3):** Sales Enablement · Managed Sales Desk · Socio Comercial Exclusivo del Proyecto.
**Modelo comercial:** `[pull from Developer Pricing Model]` — 0.5% sobre venta bruta en ventas del equipo propio · 2.5–3% en ventas originadas por nuestra red · desk gestionado desde $3,000–$5,000/mes, potencialmente acreditable.
**Prueba:** landmark projects — Bioma · Mova · Cavarrosa · Nayamara · Playa Escondida · La Maison by Fendi.
**CTA:** Hablemos de tu proyecto → **developer CRM pipeline**.

---

### PAGE 6 — LA PLATAFORMA (BluePrint)

Hero: *La plataforma que hace que todo esto funcione.*
Modules: CRM · pipeline · Dproperty Select portfolio · proyecciones · dashboards y reporting · Academia · agentes de IA · plantillas y documentos · cumplimiento.
Framing: *BluePrint no es el producto. Es el software que permite que el ecosistema exista.*
White-label note: *Se adapta a tu marca.* · CTA: Ver una demo.

### PAGE 7 — NOSOTROS
Origin story (2017 → today, from [[../04_Product/Public Site Wireframe]] PAGE 2, **rewritten in parent voice**) · Mission · Vision · the 6 values · Recognition (SIMA · ELDI · Gran Salón · Lonja de Bogotá) · *"BluePrint es solo el software que permite que este ecosistema exista; el producto es el ecosistema y el conocimiento detrás."* · Team intentionally private for now.

### PAGE 8 — CONTACTO
GoHighLevel calendar with **three routes**: *"Quiero una franquicia Dproperty"* · *"Quiero white-label"* · *"Soy desarrollador"* → three separate pipelines. Short form + `[MOCK]` office/email/phone/social.

### PAGE 9 — LOGIN
Branded login → BluePrint. SSO-ready. *"¿Nuevo socio? Escríbenos."*

### PAGE 10 — LEGAL
Privacidad · Términos · **Aviso de inversión** (rentabilidades no garantizadas) · **Aviso de franquicia** (franchise-disclosure per market — see [[../05_Franchise_Package/Localization/Localization Framework]]).

---

## 6. The Lovable Prompt (paste this)

> Build a **responsive, Spanish-first B2B marketing website** (with an EN toggle) for a company that operates **a franchising ecosystem for real estate**. Use the page specs and Spanish copy in Section 5 of this document verbatim.
>
> **Critical framing:** the company is **not** "Dproperty." Dproperty is its **flagship brand** — the relationship Mercure has to Accor. The site sells **three distinct partnership lines to three distinct buyers**: (1) a branded Dproperty franchise, (2) a white-label franchise where the partner keeps their own brand, and (3) a dedicated sales-team partnership for property developers. The homepage's most important job is a **three-door routing block** where all three options are visually equal — white-label must never look like a cheaper tier.
>
> Use `B_RealEstate` wherever the company name goes and `BluePrint` wherever the platform name goes — both are active names and remain configuration-driven. Keep all `[MOCK]` placeholders visible.
>
> **Design:** boutique, editorial, calm, credible. Background `#F6F3ED`, text `#161616`, accent deep blue `#1F4E79`, secondary champagne `#B89B5E`. Editorial serif headlines, clean sans body, generous whitespace, few high-quality images, champagne accents on line-art diagrams. No stock handshakes, no franchise-expo energy. Sticky minimal header, primary CTA in champagne, ghost login button, ES/EN toggle.
>
> **Wire:** every CTA to GoHighLevel, into **three separate CRM pipelines** (branded franchise / white-label / developer). The contact page calendar must let the visitor self-select which of the three they are.
>
> Fast, accessible, SEO-clean. Output production code.

## 7. Assets Required

| Asset | Purpose | Status |
|---|---|---|
| **Parent company name** | Everything | **BLOCKER for launch** |
| **Platform name** | Everything | **BLOCKER for launch** |
| Parent logo (light/dark) | Header/footer | need |
| Dproperty logo (as flagship brand card) | Proof blocks | have |
| Fonts (serif + sans) | Site-wide | need |
| Project photography (6 landmarks) | Proof, developers page | Drive |
| Partner uplift stat (Select proof point) | Pillar 4 | **need — substantiate** |
| GHL calendar + 3 pipeline embeds | CTAs | config |
| Territory map data | Franchise page | need |
| Real contact details | Replace `[MOCK]` | need |

## 8. Open Decisions Blocking Publish

1. **Parent brand name** and **platform name**.
2. ~~Does white-label get Dproperty Select access?~~ ✅ **RESOLVED 2026-08-03** — yes, at **1.5%** (external-partner-broker terms) vs. **2.5%** branded. Propagation to the `dproperty brain` operational project files still pending.
3. **How much economics to publish** — exact figures vs. *"desde $30,000"* vs. fully gated. Default: gated.
4. **Substantiate the "proven model" claim** — need a real, defensible number.
5. **Does Dproperty Select keep the Dproperty name** under the parent architecture?
6. **Currency consistency** — Acquisition Playbook says €30k, everything else USD $30k. Fix before public.

## 9. Build & QA Checklist
- [ ] All pages built; Spanish copy verbatim; EN toggle works.
- [ ] Company is never presented as "Dproperty"; Dproperty always framed as flagship brand.
- [ ] Three-door block: equal visual weight, all three.
- [ ] White-label page reads as premium, not budget.
- [ ] Developers page leads with **continuity + understanding the product**, not headcount.
- [ ] `B_RealEstate` / `BluePrint` / `[MOCK]` all still visible and find-replaceable.
- [ ] Three CRM pipelines wired correctly and separately.
- [ ] Trust-strip numbers honestly attributed to Dproperty.
- [ ] Franchise numbers pulled from Pricing Model / Unit Economics, not retyped.
- [ ] Investment + franchise disclaimers on Legal.
- [ ] Responsive + accessible + SEO-clean.

## 10. Source & Change Log
- **Source:** [[../01_Strategy/Brand Architecture]] v0.1 · [[../04_Product/Public Site Wireframe]] v0.6 · [[../05_Franchise_Package/Pre-Signing/Franchisee Acquisition Playbook]] · [[../13_White_Label/White-Label Pricing]] · [[../11_Developer_Sales_OS/Developer Sales OS Guide]].
- **1.0 (2026-08-03)** — created. Parent-brand restructure; three service lines; developer line repositioned to dedicated embedded team; Lovable prompt written.
