---
project: Dproperty OS
title: "LOVABLE - Ecosystem Website Build Brief"
type: build_brief
deliverable: "Cantera ecosystem website — bilingual ES/EN"
target_tool: Lovable
version: 1.0
status: "Ready to paste into Lovable"
owner: Esteban
created: 2026-08-03
tags: [handoff, lovable, website, bilingual, production]
---

# BUILD BRIEF — Cantera Ecosystem Website

**Paste this entire document into Lovable as the project brief.**

This is a **fully bilingual (Spanish + English) B2B marketing website**. Every string appears below in both languages. Build with a real i18n layer — not duplicated pages.

---

# 0. WHAT WE ARE BUILDING

A marketing website for a company that operates **a franchising ecosystem for real estate**.

## The single most important framing rule

**The company is NOT "Dproperty."** Dproperty is its **flagship brand** — exactly the relationship **Mercure has to Accor**, or Ritz-Carlton to Marriott.

The company sells **three partnership products to three different buyers**:

| Product | Buyer | What they get |
|---|---|---|
| **Dproperty Franchise** | Agents/entrepreneurs who want to sell investment real estate | Our brand, our system, our recognition |
| **White-Label Franchise** | Operators who want their own brand | Our system, their brand, our endorsement |
| **Developer Sales Partner** | Property developers | A dedicated sales team across their portfolio |

Never write copy implying the company *is* Dproperty. Dproperty appears as **proof** and as **one option**.

## Names

- **Cantera** — the parent company. In Spanish both *quarry* (the source of the stone a building is made from) and *la cantera*, the academy that develops homegrown talent. A company that supplies both the material and the people.
- **Plano** — the platform (formerly "Dproperty OS"). *Blueprint*: the system as a drawing others can build from. Brand-neutral, so white-label partners can run on it under their own name.
- `[MOCK]` — remaining placeholder data (contact details only). Keep visible.

**Trademark clearance is not yet complete.** Implement both names as **variables in one config file** so a single edit updates the whole site.

---

# 1. NON-NEGOTIABLE TONE RULES

1. **We are the ecosystem; Dproperty is our flagship brand.**
2. **Sell the experience, not a logo.** "Join everything our experience built" — never "buy our brand."
3. **Two franchise doors, no consolation prize.** Branded and white-label are **equal, different choices**. White-label must never look like the budget tier.
4. **The difference is brand + focus, not price tier.**
5. **Premium but reachable.** *"We are the best, but we are reachable."*
6. **Numbers over hype.** Signature phrase stays in Spanish in both language versions: *"Somos más amigos de la matemática que de la arquitectura."*
7. No stock-photo handshakes. No franchise-expo energy. No exclamation marks.

---

# 2. DESIGN SYSTEM

```
Background     #F6F3ED   (warm off-white)
Text           #161616   (charcoal)
Accent         #1F4E79   (deep blue)
Secondary      #B89B5E   (champagne)
```

- **Typography:** editorial **serif** for headlines, clean **sans-serif** for body. Large headline sizes, generous line-height.
- **Feel:** boutique, calm, editorial, credible. Generous whitespace. Few, high-quality images. Champagne accents on line-art diagrams and key data rows.
- **Buttons:** primary = champagne fill, charcoal text. Secondary = ghost/outline.
- **Motion:** minimal. Subtle fade-up on scroll. Nothing bouncy.
- **Responsive:** mobile-first, fully responsive. Tables must degrade to stacked cards on mobile.
- **Accessibility:** WCAG AA contrast, semantic HTML, keyboard navigable, alt text on all images.

---

# 3. BILINGUAL REQUIREMENTS

- **Spanish is the primary/default language.** English is a full peer, not an afterthought.
- Language toggle in the header: `ES | EN`. Persist choice in localStorage.
- Use route-based i18n: `/es/...` and `/en/...`, with `/` redirecting to `/es`.
- Store all strings in **two locale files** (`es.json`, `en.json`) with identical key structures.
- `<html lang>` must update with the active locale.
- Add `hreflang` alternate tags for SEO.
- Meta titles/descriptions translated per page.
- The signature phrase *"Somos más amigos de la matemática que de la arquitectura."* stays **in Spanish in both locales**, with an English gloss beneath it in EN only: *"We're better friends with math than with architecture."*

---

# 4. SITEMAP & ROUTES

| Route (ES) | Route (EN) | Page |
|---|---|---|
| `/es` | `/en` | Home |
| `/es/ecosistema` | `/en/ecosystem` | The Ecosystem |
| `/es/franquicia-dproperty` | `/en/dproperty-franchise` | Dproperty Franchise |
| `/es/white-label` | `/en/white-label` | White-Label |
| `/es/desarrolladores` | `/en/developers` | Developers |
| `/es/plataforma` | `/en/platform` | The Platform |
| `/es/nosotros` | `/en/about` | About |
| `/es/contacto` | `/en/contact` | Contact |
| `/es/legal` | `/en/legal` | Legal |
| `/login` | `/login` | Login (→ Plano) |

## Header (sticky, minimal)

`Cantera` logo · nav · `ES|EN` · `[Iniciar sesión / Log in]` (ghost) · `[Agendar llamada / Book a call]` (champagne, primary)

**Nav ES:** Ecosistema · Franquicias ▾ (Franquicia Dproperty, White-Label) · Desarrolladores · Plataforma · Nosotros
**Nav EN:** Ecosystem · Franchising ▾ (Dproperty Franchise, White-Label) · Developers · Platform · About

## Footer

**ES:** *Un ecosistema de franquicias para el sector inmobiliario.*
**EN:** *A real estate franchising ecosystem.*

Columns — **ES:** Marcas (Dproperty) · Compañía · Contacto · © Cantera · Privacidad · Términos · Aviso de inversión
**EN:** Brands (Dproperty) · Company · Contact · © Cantera · Privacy · Terms · Investment Disclaimer

---

# 5. PAGE CONTENT

> Format below: **ES** first, **EN** second. Use verbatim.

## PAGE 1 — HOME

### Hero

**ES**
- H1: *Un ecosistema de franquicias para el sector inmobiliario.*
- Sub: *Te damos el método, la tecnología, la formación y la red que construimos desde 2017 — y tú decides cuánto de nuestra marca quieres usar.*
- CTAs: `[ Agendar una llamada ]` · `[ Ver las tres vías ]`

**EN**
- H1: *A real estate franchising ecosystem.*
- Sub: *We give you the method, the technology, the training and the network we've built since 2017 — and you decide how much of our brand you want to use.*
- CTAs: `[ Book a call ]` · `[ See the three routes ]`

**Signature phrase (both locales, under hero):** *Somos más amigos de la matemática que de la arquitectura.*
*(EN only, small, beneath: "We're better friends with math than with architecture.")*

### Trust strip

**ES:** *Desde 2017 · +$200M transaccionados · +700 operaciones · +99% de nuestros clientes nunca perdió capital · +80% vuelve a invertir.*
**EN:** *Since 2017 · $200M+ transacted · 700+ operations · 99%+ of our clients never lost capital · 80%+ invest with us again.*

**Attribution line directly beneath (required — these are the flagship's numbers, not the parent's):**
**ES:** *Los números de Dproperty, nuestra marca insignia.*
**EN:** *Dproperty's numbers — our flagship brand.*

### THE THREE DOORS — the most important block on the site

Three cards, **equal height, equal visual weight**. No card is highlighted, badged, "most popular," or visually promoted above the others.

| | Card 1 | Card 2 | Card 3 |
|---|---|---|---|
| **Title ES** | Franquicia Dproperty | White-Label | Desarrolladores |
| **Title EN** | Dproperty Franchise | White-Label | Developers |
| **Tagline ES** | *Opera bajo nuestra marca.* | *Opera bajo la tuya.* | *Tu equipo comercial, sin construirlo.* |
| **Tagline EN** | *Operate under our brand.* | *Operate under yours.* | *Your sales team, without building one.* |
| **Focus ES** | *Inversión, exclusivamente.* | *Tu mercado, tus reglas.* | *Tu producto, nuestro equipo.* |
| **Focus EN** | *Investment, exclusively.* | *Your market, your rules.* | *Your product, our team.* |
| **Body ES** | Para quien quiere vender inversión inmobiliaria con la credibilidad de una marca con más de una década de trayectoria. | Para quien ya tiene marca — o quiere construir la suya — con nuestro sistema detrás y libertad de enfoque. | Para desarrolladores que tienen el producto, pero no el equipo. |
| **Body EN** | For those who want to sell investment real estate with the credibility of a brand with over a decade of track record. | For those who already have a brand — or want to build their own — with our system behind them and freedom of focus. | For developers who have the product, but not the team. |
| **CTA ES** | Conocer la franquicia | Conocer white-label | Hablar con nosotros |
| **CTA EN** | Explore the franchise | Explore white-label | Talk to us |

### The Four Pillars

**ES**
1. **La promesa boutique.** *Todo se apoya en la forma de trabajar de Dproperty: curaduría sobre volumen, números sobre ruido, confianza sobre transacción.*
2. **Franquicia a tu manera.** *Damos las herramientas y acompañamos el proceso — la marca puede seguir siendo tuya.*
3. **Las herramientas ya existen.** *Plataforma Plano, CRM white-label, agentes de IA, academia, eventos de networking, acceso a Dproperty Select, plantillas y manuales.*
4. **Es un modelo probado.** *Llevamos desde 2017 operándolo. Cada operación de Dproperty Select es inventario que no tuviste que conseguir, con una comisión que no tuviste que negociar.*

**EN**
1. **The boutique promise.** *Everything rests on the Dproperty way of working: curation over volume, numbers over noise, trust over transactions.*
2. **Franchise your way.** *We provide the tools and walk beside you — the brand can still be yours.*
3. **The tools already exist.** *Plano platform, white-label CRM, AI agents, academy, networking events, Dproperty Select access, templates and manuals.*
4. **It's a proven model.** *We've been running it since 2017. Every Dproperty Select transaction is inventory you didn't have to source, at a commission you didn't have to negotiate.*

> **Pillar 4 makes no unverifiable claim.** It states the mechanism (sourced inventory, pre-negotiated commission) plus a real operating history — both defensible. Do **not** add a "partners increased profit by X%" statistic: with zero franchisees there is no such figure, and an unsourced number is the first thing a sceptical buyer will probe. Add a genuine case study when one exists.

### Proof block

**ES:** *No vendemos un brochure. Vendemos la entrada a todo lo que la experiencia de Dproperty construyó.*
**EN:** *We're not selling a brochure. We're selling entry into everything Dproperty's experience has built.*

Flagship card — Dproperty, since 2017, Panama. Landmark projects: **Bioma · Mova · Cavarrosa · Nayamara · Playa Escondida · La Maison by Fendi.**

### Tools grid (8 items)

**ES:** Plataforma Plano · CRM white-label · Agentes de IA · Academia · Eventos y red · Dproperty Select · Manuales y plantillas · Acompañamiento de lanzamiento
**EN:** Plano platform · White-label CRM · AI agents · Academy · Events & network · Dproperty Select · Manuals & templates · Launch support

### Vision strip → Ecosystem page

**ES:** *Esto es solo la Fase 1.* → Conocer la visión
**EN:** *This is only Phase 1.* → See the vision

---

## PAGE 2 — THE ECOSYSTEM

**Hero ES:** *No estás comprando una marca. Estás entrando a un ecosistema.*
**Hero EN:** *You're not buying a brand. You're joining an ecosystem.*

### House-of-brands diagram

Render as a clean line-art diagram with champagne accents:

```
                    Cantera
                        │
    ┌───────────┬───────┴───────┬──────────────┐
 DPROPERTY   WHITE-LABEL    DESARROLLADORES  Plano
 (marca       (marcas        (alianzas)      (la plataforma
  insignia)    propias)                       que lo conecta)
```

**Caption ES:** *Dproperty es nuestra marca insignia — la prueba de que el modelo funciona, y una de las formas en que puedes operar. No es quiénes somos; es lo que construimos.*
**Caption EN:** *Dproperty is our flagship brand — proof the model works, and one of the ways you can operate. It isn't who we are; it's what we built.*

### What we don't compromise on (6)

**ES:** Boutique, siempre · Confianza y números · La inversión primero · Calidad sin concesiones · Talento por encima del tamaño · Más grande que nosotros
**EN:** Boutique, always · Trust and numbers · Investment first · Quality without compromise · Talent over size · Bigger than us

### The north star

**ES:** *Usar nuestro conocimiento, experiencia y red para potenciar la visión de quienes pueden mover los bienes raíces en sus regiones — los mejores reunidos como maestros artesanos en un gran taller. El alma de un lugar como 19M, aplicada a los bienes raíces.*
**EN:** *Using our knowledge, experience and network to amplify the vision of those who can move real estate in their regions — the best gathered like master craftsmen in a great workshop. The soul of a place like 19M, applied to real estate.*

**Phases ES:** Fase 1 — El ecosistema de franquicias (hoy) · Fase 2 — El hub físico (estrella polar, financiado por la Fase 1)
**Phases EN:** Phase 1 — The franchising ecosystem (today) · Phase 2 — The physical hub (north star, funded by Phase 1)

### Why Panama (6)

**ES:** Economía dolarizada · Cruce de las Américas · Destino estable y amigable con la inversión · Puente LATAM–Iberia · Donde nació Dproperty · Un mercado que premia la curaduría
**EN:** Dollarized economy · Crossroads of the Americas · Stable, investment-friendly destination · LATAM–Iberia bridge · Where Dproperty was born · A market that rewards curation

### Founding members

**ES:** *Cada socio de esta primera generación es miembro fundador del ecosistema.*
**EN:** *Every partner in this first generation is a founding member of the ecosystem.*

**CTA ES:** Súmate al ecosistema · **CTA EN:** Join the ecosystem

---

## PAGE 3 — DPROPERTY FRANCHISE

**Hero ES:** *Ten tu propia Dproperty.*
Sub: *Lleva la inversión inmobiliaria boutique a tu mercado — con nuestra marca, nuestro sistema, nuestra formación y nuestra red detrás de ti.*
**Hero EN:** *Own your own Dproperty.*
Sub: *Bring boutique investment real estate to your market — with our brand, our system, our training and our network behind you.*

**CTAs ES:** `[ Agendar una llamada ]` · `[ Descargar información ]`
**CTAs EN:** `[ Book a call ]` · `[ Download the info pack ]`

### BLOCK: The investment brand — place this high, immediately after the hero

**ES**
> **Dproperty no es una marca inmobiliaria general. Es una marca de inversión.**
>
> Nuestros clientes no compran para vivir: compran para rentabilizar. Un inversionista que llega con $50,000 puede comprar una o dos propiedades sin la presión de una hipoteca, porque la unidad es revendible — y si toma hipoteca, es para alquilar.
>
> Por eso una franquicia Dproperty busca producto **rentable y confiable**, no necesariamente bonito y habitable. Entre dos edificios comparables, el de mejores acabados suele ser el producto equivocado para nosotros: mejores materiales significan un punto de entrada más alto, y un punto de entrada más alto significa menor retorno.
>
> Vendemos y alquilamos a usuario final cuando hace falta — dentro de nuestros círculos o con brokers aliados — pero la identidad y el enfoque siempre miran al inversionista.

**EN**
> **Dproperty is not a general real estate brand. It's an investment brand.**
>
> Our clients don't buy to live — they buy to profit. An investor arriving with $50,000 can buy one or two properties without mortgage pressure, because the unit is resellable — and if they do take a mortgage, it's so the unit can be rented.
>
> That's why a Dproperty franchise hunts for product that is **profitable and reliable**, not necessarily pretty and livable. Between two comparable buildings, the one with better finishes is usually the wrong product for us: better materials mean a higher entry point, and a higher entry point means a lower return.
>
> We do sell and rent to end users when needed — within our own circles or with partner brokers — but the identity and the focus always face the investor.

### Who it's for

**ES:** Agentes que quieren independizarse y especializarse en inversión · Profesionales de ventas de otros sectores · Jóvenes emprendedores.
*Si tu mercado es el comprador de vivienda para habitar, tu camino probablemente es white-label — y te lo diremos.*

**EN:** Agents who want independence and to specialize in investment · Sales professionals from other sectors · Young entrepreneurs.
*If your market is the buyer looking for a home to live in, your route is probably white-label — and we'll tell you so.*

### What's included

**ES:** Marca Dproperty y manuales · Plataforma Plano · CRM white-label · Academia · Agentes de IA · **Acceso completo a Dproperty Select** · Plantillas legales y comerciales · Plan de lanzamiento 30/60/90 · Acompañamiento y reporting de HQ · Prioridad de inversión y red internacional
**EN:** Dproperty brand and manuals · Plano platform · White-label CRM · Academy · AI agents · **Full Dproperty Select access** · Legal and commercial templates · 30/60/90 launch plan · HQ support and reporting · Investment priority and international network

### Your path

**ES:** Descubre → Aplica → Firma → Onboarding → Lanzamiento
**EN:** Discover → Apply → Sign → Onboarding → Launch

### Investment & returns

**ES:** Desde **$30,000** · **$1,000/mes** · 6% royalty + 1.5% Fondo de Marca y Red sobre GCI **cobrado** · Dproperty Select al **2.5% del valor de venta**
**EN:** From **$30,000** · **$1,000/month** · 6% royalty + 1.5% Network & Brand Fund on **collected** GCI · Dproperty Select at **2.5% of sale value**

> Default display: show *"desde $30,000 / from $30,000"* prominently; put the detailed fee breakdown behind the info-pack download.

### THE PAYBACK BLOCK — the most persuasive block on the site. Give it room.

**ES**
> **¿Por qué la franquicia Dproperty cuesta más?**
>
> Porque no compras solo el conocimiento y las herramientas — eso también está en white-label. Compras **una marca con más de una década de trayectoria**, y **un punto completo más en Dproperty Select**.

**EN**
> **Why does the Dproperty franchise cost more?**
>
> Because you're not only buying the know-how and the tools — white-label has those too. You're buying **a brand with over a decade of track record**, and **a full extra point on Dproperty Select**.

| ES | Franquicia Dproperty | White-label |
|---|---|---|
| Comisión Select | **2.5%** | 1.5% |
| En una unidad de $300,000 | **$7,500** | $4,500 |
| Diferencia | **+$3,000 por unidad** | |

| EN | Dproperty Franchise | White-label |
|---|---|---|
| Select commission | **2.5%** | 1.5% |
| On a $300,000 unit | **$7,500** | $4,500 |
| Difference | **+$3,000 per unit** | |

**ES:** *La diferencia en la inversión inicial se recupera en aproximadamente **siete operaciones Select**. A partir de ahí, la marca se paga sola.*
**EN:** *The difference in upfront investment is recovered in roughly **seven Select transactions**. After that, the brand pays for itself.*

**Design:** clean editorial table, champagne accent on the difference row. On mobile, stack as two labelled cards.

### Territories

Map. **ES:** Panamá · Bogotá · Medellín abiertos · **EN:** Panama · Bogotá · Medellín open

### Proof

**ES:** *Testimonios muy pronto — podrías ser parte de nuestra primera generación.*
**EN:** *Testimonials coming soon — you could be part of our founding generation.*

### FAQ

**ES:** ¿Hay financiamiento disponible? · ¿Necesito experiencia previa en bienes raíces? · ¿Por qué no hacerlo por mi cuenta? · ¿Cuánto tarda el lanzamiento? · ¿La exclusividad territorial está garantizada? · ¿Qué pasa si no funciona?
**EN:** Is financing available? · Do I need prior real estate experience? · Why not do it on my own? · How long does launch take? · Is territorial exclusivity guaranteed? · What if it doesn't work?

---

## PAGE 4 — WHITE-LABEL

**This page must feel as premium as Page 3.** Same layout quality, same photography quality, same typographic scale. Different door — not lesser door.

**Hero ES:** *Tu marca. Nuestro sistema.*
Sub: *Construye tu agencia a tu manera — con la tecnología, el método, la formación y la red que nos tomó años construir. La marca que crezcas es tuya.*
**Hero EN:** *Your brand. Our system.*
Sub: *Build your agency your way — with the technology, method, training and network it took us years to build. The brand you grow is yours.*

### The idea

**ES:** *No todos quieren operar bajo otra marca, y está bien. Te damos las herramientas y te acompañamos en el proceso; tú decides cómo se llama, cómo se ve y hacia dónde va.*
**EN:** *Not everyone wants to operate under someone else's brand, and that's fine. We give you the tools and walk beside you; you decide what it's called, how it looks, and where it goes.*

### BLOCK: Your focus, your rules

**ES**
> La franquicia Dproperty opera con un mandato estricto: inversión, exclusivamente. **White-label no tiene ese límite.**
>
> Si tu mercado son familias comprando su casa, producto de mejores acabados, o desarrollo pensado para habitar — eso es perfectamente válido, y con white-label puedes perseguirlo. Recibes el mismo sistema, la misma tecnología y la misma formación, aplicados al mercado que tú elijas.

**EN**
> The Dproperty franchise operates under a strict mandate: investment, exclusively. **White-label has no such limit.**
>
> If your market is families buying a home, higher-finish product, or development designed to be lived in — that's entirely valid, and with white-label you can pursue it. You get the same system, the same technology and the same training, applied to whatever market you choose.

### BLOCK: Backed, not absorbed

**ES:** *Te acompañamos y te respaldamos públicamente: puedes decir **"powered by Dproperty."** Es respaldo, no identidad. La marca que construyas es tuya, y el valor que le agregues se queda contigo.*
**EN:** *We support and publicly back you: you can say **"powered by Dproperty."** That's endorsement, not identity. The brand you build is yours, and the value you add to it stays with you.*

### What's included

**ES:** Plataforma Plano · CRM white-label bajo tu marca · Academia · Agentes de IA · Flujos, manuales y plantillas · Dashboards y lógica de proyección · **Acceso a Dproperty Select como broker aliado (1.5% del valor de venta)** · Respaldo "powered by Dproperty" · Implementación acompañada · Eventos y red
**EN:** Plano platform · White-label CRM under your brand · Academy · AI agents · Workflows, manuals and templates · Dashboards and projection logic · **Dproperty Select access as a partner broker (1.5% of sale value)** · "Powered by Dproperty" endorsement · Guided implementation · Events and network

### What's not included

**ES:** La marca Dproperty ni su trayectoria · Prioridad de inversión · Relaciones directas con desarrolladores del grupo · El payout preferente de Select (2.5%)
**EN:** The Dproperty brand or its track record · Investment priority · Direct relationships with group developers · The preferential Select payout (2.5%)

### Honest comparison table

| ES | Franquicia Dproperty | White-Label |
|---|---|---|
| Marca | Dproperty | **La tuya** |
| Reconocimiento | +10 años de trayectoria | Respaldo *"powered by Dproperty"* |
| Enfoque | Inversión, exclusivamente | **Tú decides** |
| Plataforma, CRM, IA, Academia | ✓ | ✓ |
| Dproperty Select | **2.5%** del valor de venta | 1.5% (broker aliado) |
| Prioridad de inversión | ✓ | — |
| Equity de marca | De Dproperty | **Tuyo** |
| Inversión inicial | desde $30,000 | desde $10,000 |

| EN | Dproperty Franchise | White-Label |
|---|---|---|
| Brand | Dproperty | **Yours** |
| Recognition | 10+ years of track record | *"Powered by Dproperty"* endorsement |
| Focus | Investment, exclusively | **You decide** |
| Platform, CRM, AI, Academy | ✓ | ✓ |
| Dproperty Select | **2.5%** of sale value | 1.5% (partner broker) |
| Investment priority | ✓ | — |
| Brand equity | Dproperty's | **Yours** |
| Upfront investment | from $30,000 | from $10,000 |

> **Design instruction:** bold the *win* cells in **both** columns (shown above). The white-label column must visibly win on "brand," "focus" and "brand equity." This is the block that proves white-label isn't the cheap tier.

### Plans

**ES:** **Starter** — $10,000 setup / $1,500 al mes · **Growth** — $20,000 setup / $2,500 al mes
Add-ons: formación a medida · implementación extra · dashboards avanzados · integraciones · plantillas legales localizadas
**EN:** **Starter** — $10,000 setup / $1,500 per month · **Growth** — $20,000 setup / $2,500 per month
Add-ons: custom training · extra implementation · advanced dashboards · integrations · localized legal templates

---

## PAGE 5 — DEVELOPERS

**Hero ES:** *Tu equipo comercial, sin construirlo desde cero.*
Sub: *Un equipo dedicado que aprende el alma de tu producto y te acompaña proyecto tras proyecto — con nuestro método, nuestra tecnología y nuestra red detrás.*
**Hero EN:** *Your sales team, without building one from scratch.*
Sub: *A dedicated team that learns the soul of your product and stays with you project after project — with our method, our technology and our network behind it.*

### The problem

**ES:** *Tienes el producto. Construir una operación de ventas profesional — contratar, formar, sistematizar, controlar el pipeline, reportar — es otro negocio completamente distinto. Y hacerlo mal te cuesta la marca y el margen.*
**EN:** *You have the product. Building a professional sales operation — hiring, training, systematizing, controlling the pipeline, reporting — is an entirely different business. And doing it badly costs you the brand and the margin.*

### Our proposal

**ES:** *No te damos un equipo genérico. Te damos un equipo que se queda contigo: que entiende tu producto, tu comprador y tus estándares, y que lleva ese conocimiento de un proyecto al siguiente.*
**EN:** *We don't give you a generic team. We give you a team that stays with you: one that understands your product, your buyer and your standards, and carries that knowledge from one project to the next.*

### Why it's different (4 — the core block)

**ES**
1. **Continuidad, no rotación.** *El mismo equipo te acompaña en todos tus proyectos. Lo que aprenden no se pierde.*
2. **Entienden el alma del producto.** *No vendemos con un brochure en la mano. Entendemos qué estás construyendo y por qué.*
3. **Cuidamos tu marca y tus números.** *Sin proyecciones no aprobadas, sin descontar tu producto para cerrar rápido.*
4. **No somos una agencia más.** *Es una alianza, más cerca de un white-label que de un contrato de comercialización.*

**EN**
1. **Continuity, not turnover.** *The same team accompanies you across every project. What they learn isn't lost.*
2. **They understand the soul of the product.** *We don't sell with a brochure in hand. We understand what you're building and why.*
3. **We protect your brand and your numbers.** *No unapproved projections, no discounting your product to close fast.*
4. **We're not another agency.** *This is a partnership — closer to a white-label than to a sales contract.*

### What we do

**ES:** CRM y pipeline · Proceso comercial · Formación del equipo · Activación y disciplina de brokers · Scripts y presentación de proyecto · Reporting para dirección e inversionistas · Soporte de proyecciones · **Demanda calificada desde nuestra red y nuestra base de inversionistas**
**EN:** CRM and pipeline · Commercial process · Team training · Broker activation and discipline · Scripts and project presentation · Reporting for leadership and investors · Projection support · **Qualified demand from our network and investor base**

### Levels

**ES:** Sales Enablement · Managed Sales Desk · Socio Comercial Exclusivo del Proyecto
**EN:** Sales Enablement · Managed Sales Desk · Exclusive Project Sales Partner

### Commercial model

**ES:** 0.5% sobre venta bruta en ventas del equipo propio · 2.5%–3% en ventas originadas por nuestra red · Desk gestionado desde $3,000–$5,000/mes, potencialmente acreditable
**EN:** 0.5% of gross sale value on in-house team sales · 2.5%–3% on sales originated by our network · Managed desk from $3,000–$5,000/month, potentially creditable

### Proof

**ES/EN:** Bioma · Mova · Cavarrosa · Nayamara · Playa Escondida · La Maison by Fendi

**CTA ES:** Hablemos de tu proyecto · **CTA EN:** Let's talk about your project

---

## PAGE 6 — THE PLATFORM (Plano)

**Hero ES:** *La plataforma que hace que todo esto funcione.*
**Hero EN:** *The platform that makes all of this work.*

**Modules ES:** CRM · Pipeline · Portafolio Dproperty Select · Proyecciones · Dashboards y reporting · Academia · Agentes de IA · Plantillas y documentos · Cumplimiento
**Modules EN:** CRM · Pipeline · Dproperty Select portfolio · Projections · Dashboards and reporting · Academy · AI agents · Templates and documents · Compliance

**Framing ES:** *Plano no es el producto. Es el software que permite que el ecosistema exista.*
**Framing EN:** *Plano isn't the product. It's the software that lets the ecosystem exist.*

**White-label note ES:** *Se adapta a tu marca.* · **EN:** *It adapts to your brand.*
**CTA ES:** Ver una demo · **EN:** See a demo

---

## PAGE 7 — ABOUT

### Our history — four blocks

**ES**
- **2017 — Una firma diferente.** Nació para cerrar la brecha entre las verdaderas oportunidades de inversión y los asesores que entendían sus complejidades — ser la firma especializada en inversión inmobiliaria, sin convertirse en un fondo, y acercar ese mundo a las personas de a pie.
- **Construyendo el método.** Un portafolio curado: validado por el mercado, respaldado por desarrolladores con trayectoria, resguardado por debida diligencia y transparencia — lo que permitió ofrecer condiciones preferenciales a nuevos inversionistas.
- **Ganándonos el nombre.** Voz reconocida en Panamá y la región: SIMA Madrid, ELDI Panamá, Gran Salón Inmobiliario Bogotá; nuestra CEO en la junta de la Lonja de Bogotá. Preventas fuera de mercado convertidas en referentes.
- **El punto de inflexión.** La siguiente generación lleva ese conocimiento más allá de Panamá — convirtiendo una carrera de experiencia en un sistema sobre el que otros pueden construir.

**EN**
- **2017 — A different kind of firm.** Founded to close the gap between real investment opportunities and advisors who genuinely understood their intricacies — to be the firm specialized in real estate investment, without becoming a fund, and to bring that world closer to everyday people.
- **Building the method.** A curated portfolio: validated by the market, backed by developers with proven track records, safeguarded by due diligence and transparency — which let us offer preferential terms to new investors.
- **Earning our name.** A recognized voice in Panama and the region: SIMA Madrid, ELDI Panama, Gran Salón Inmobiliario Bogotá; our CEO on the board of the Lonja de Bogotá. Off-market pre-sales that became landmarks.
- **The turning point.** The next generation is taking that knowledge beyond Panama — turning a career's worth of experience into a system others can build on.

### Mission

**ES:** *Conectar a quienes tienen los medios para construir con quienes tienen la visión para liderar, para que el talento nunca dependa de los recursos o los contactos, y los mejores bienes raíces se vuelvan inevitables.*
**EN:** *To connect those with the means to build with those with the vision to lead — so talent is never gated by resources or network, and better real estate becomes inevitable.*

### Vision

**ES:** *Convertirnos en la casa del talento, el capital y las ideas de los bienes raíces en Latinoamérica e Iberia, concentrando la cadena de valor en un solo lugar curado, para que mejores edificios creen mejores vidas.*
**EN:** *To become the home of real estate talent, capital and ideas in LATAM and Iberia — concentrating the value chain in one curated place, so that better buildings create better lives.*

### Values (6)

**ES:** Confianza por encima de la transacción · Curaduría por encima del volumen · Números por encima del ruido · Oficio boutique · Excelencia sistematizada · Mentalidad de ecosistema
**EN:** Trust over transactions · Curation over volume · Numbers over noise · Boutique craft · Systematized excellence · Ecosystem-minded

### Recognition

SIMA · ELDI · Gran Salón Inmobiliario · Lonja de Bogotá

> Team section intentionally omitted for now.

---

## PAGE 8 — CONTACT

**Heading ES:** *Hablemos.* · **EN:** *Let's talk.*

**Left:** GoHighLevel calendar embed with **three self-selection routes**:

**ES:** "Quiero una franquicia Dproperty" · "Quiero white-label" · "Soy desarrollador"
**EN:** "I want a Dproperty franchise" · "I want white-label" · "I'm a developer"

**Right:** short form (name, email, country, which route, message) + `[MOCK]` Office: Panama City · hello@Cantera.— · +507 …-…. · Instagram · LinkedIn

---

## PAGE 9 — LOGIN

Branded login → Plano. SSO-ready.
**ES:** *¿Nuevo socio? Escríbenos.* · *¿Olvidaste tu contraseña?*
**EN:** *New partner? Get in touch.* · *Forgot your password?*

---

## PAGE 10 — LEGAL

**ES:** Privacidad · Términos · **Aviso de inversión** (las rentabilidades no están garantizadas) · **Aviso de franquicia**
**EN:** Privacy · Terms · **Investment Disclaimer** (returns are not guaranteed) · **Franchise Disclosure**

---

# 6. CRM WIRING (GoHighLevel)

**Three completely separate pipelines.** Never merge them.

| Source | Pipeline |
|---|---|
| Dproperty Franchise page CTAs, "franchise" calendar route | **Branded franchise pipeline** |
| White-Label page CTAs, "white-label" calendar route | **White-label pipeline** |
| Developers page CTAs, "developer" calendar route | **Developer pipeline** |

- Booking on the franchise pipeline triggers the **Prep Pack** automation.
- "Download the info pack" is a gated form → branded franchise pipeline.
- Pass locale (`es`/`en`) as a field on every submission.

---

# 7. TECHNICAL REQUIREMENTS

- Responsive, mobile-first.
- Fast: lazy-load images, optimize fonts, target Lighthouse 90+.
- SEO: per-page translated meta titles/descriptions, Open Graph tags, `hreflang`, sitemap.xml, semantic headings.
- Accessible: WCAG AA, keyboard navigation, alt text, visible focus states.
- All copy in locale files — no hardcoded strings.
- `Cantera`, `Plano`, `[MOCK]` as config variables, single source.

---

# 8. QA CHECKLIST

- [ ] Every page exists in both `/es` and `/en`; no untranslated strings.
- [ ] Language toggle works everywhere and persists.
- [ ] The company is **never** presented as "Dproperty."
- [ ] Trust-strip numbers explicitly attributed to Dproperty as flagship brand.
- [ ] Three-door block: equal height, equal weight, no "recommended" badge.
- [ ] White-label page reads as premium; its comparison-table wins are visually bold.
- [ ] Developers page leads with continuity and product understanding, not headcount.
- [ ] Payback block renders correctly and stacks well on mobile.
- [ ] Three CRM pipelines wired separately; locale passed through.
- [ ] `Cantera`, `Plano`, `[MOCK]` still visible and centrally editable.
- [ ] Signature Spanish phrase present in both locales.
- [ ] Investment + franchise disclaimers on Legal.
- [ ] Lighthouse ≥ 90 on performance and accessibility.

---

# 9. KNOWN PLACEHOLDERS — NOT LAUNCH-READY UNTIL RESOLVED

1. Contact details (office, email, phone, social).
2. Territory map data.
3. Photography and logos.
4. Product videos for the Platform / CRM / Academy showcases.

**Names (Cantera, Plano) are resolved but pending trademark clearance — keep them as config variables.**
