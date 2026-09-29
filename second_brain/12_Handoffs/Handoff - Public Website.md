---
project: B_RealEstate
title: "Handoff - Public Website"
type: handoff
deliverable: "Public marketing website (pre-login)"
target_output: "Responsive website"
target_tool: "AI site builder (Framer AI, Webflow, v0, Lovable) or Figma → build"
source_notes: ["10_Brand_and_Web/Public Site Wireframe.md (v0.6)", "10_Brand_and_Web/Public Site Copy - ES Master.md (v1.0)"]
version: 1.1
status: "RE-SCOPED 2026-08-03 — this is now the DPROPERTY BRAND site (consumer/investor), not the company site. Build after the ecosystem site."
owner: Esteban
last_updated: 2026-09-29
tags: [handoff, production, website, brand, marketing]
---

> [!NOTE] Verified against canon 2026-09-23
> **Regenerate before external use.** Handoffs are self-contained snapshots, so this file may still inline pre-reconciliation naming, pricing or product boundaries. Check against canon: BluePrint oversees management outcomes across the commercial lifecycle without executing the sale · Building Blocks (not Academy) · B_ Partner (not White-Label) · $399/$799 + $1,500 setup · $950k raise · no “one database” or “CRM propio” claims. If a handoff and its source note disagree, **the source note wins**.
>
> Precedence: [[../01_Canon/00 - Precedence and Canonical Reconciliation|Canonical Reconciliation and Precedence]]

# HANDOFF — Public Website (Dproperty brand site)

> **Live-site/naming update (2026-08-16):** B_RealEstate and BluePrint are the active names; https://bfranchising.com is live. This handoff remains production history. Before further build work, use [[../10_Brand_and_Web/Website Audit - bfranchising.com - 2026-08-16|the live-site audit]] and [[../01_Canon/09 - Unit Economics Registry|the economics registry]] as the correction list.

> ⚠️ **RE-SCOPED 2026-08-03 — read before building.**
> The brand architecture changed: we are **not** Dproperty. Dproperty is the **flagship brand** of a parent company that operates a franchising ecosystem (Mercure : Accor). See [[../10_Brand_and_Web/Brand Architecture]].
>
> **This handoff is still valid**, but only as the **Dproperty consumer/investor brand site** (`dproperty.com`) — buyers, sellers, investors, Select. It is no longer the company's main site.
>
> **Two changes required before building this one:**
> 1. **PAGE 7 (Franquicias) is removed** from this site. Franchise/white-label/developer recruitment now lives on the parent site → [[Handoff - Ecosystem Website]]. Replace with a single banner + footer line: *"Dproperty es parte de B_RealEstate"* → link out.
> 2. Add a *"Dproperty es parte de B_RealEstate"* line to the footer.
>
> **Build order:** the ecosystem site first (that's where the revenue conversation is). This one after.

---

> **Self-contained package** to generate the public **Dproperty site (pre-login)**. Production language is **Spanish** (EN translated from it). External name = **"Dproperty Select."** Tone: calm, prestigious, human — *"we are the best, but we are reachable."* `[MOCK]` = replace before publish. Team section intentionally private for now.

## 0. Production Brief
- **Deliverable:** responsive marketing site, ~10 pages, Spanish-first + EN toggle.
- **Target tool:** AI site builder (Framer AI / Webflow / v0 / Lovable), or Figma high-fidelity then build.
- **Fidelity goal:** boutique, editorial, calm — few high-quality images, generous whitespace.
- **Integrations:** GoHighLevel (calendar embed + two CRM pipelines: client vs. franchise), SSO-ready login to the OS.

## 1. Design & Brand Direction
- **Palette:** background off-white `#F6F3ED`; text charcoal `#161616`; accent deep blue `#1F4E79`; secondary champagne `#B89B5E`.
- **Type:** editorial **serif** headlines; clean **sans-serif** body.
- **Feel:** boutique, calm, editorial; generous whitespace; few, high-quality images; champagne accents on line-art diagrams.
- **Header:** sticky, minimal — logo · Nosotros · Visión · Servicios · Select · Franquicias · ES/EN · [Iniciar sesión] (ghost) · [Agendar llamada] (champagne, primary).
- **Footer:** tagline *"Más amigos de la matemática que de la arquitectura."* · Compañía / Trabaja con nosotros / Contacto columns · © Dproperty · Privacidad · Términos · Aviso de inversión.

## 2. Assets Required
| Asset | Purpose | Source | Status |
|---|---|---|---|
| Logo (light/dark) | Header/footer | Brand | need |
| Hero + section imagery (curated Panama RE) | Home, About, Vision | Drive | need |
| Project photos (Bioma, Mova, Cavarrosa, Nayamara, Playa Escondida, La Maison by Fendi) | Proof, Select | Drive | need |
| Fonts (serif + sans) | Whole site | Brand kit | need |
| GHL calendar + form embeds | Contact, Select, Franchise | GoHighLevel | config |
| Real contact details | Replace `[MOCK]` | Esteban | need |
| Public franchise numbers | Franchise page | [[../06_Finance/Pricing Model]]/[[../06_Finance/Unit Economics]] | pull |

## 3. Tool Instructions (the prompt)
> "Build a **responsive, Spanish-first marketing website** from the page specs and copy in *Section 4*. Use the exact Spanish copy provided (add an EN toggle translated from it). Apply the palette, serif/sans typography, and boutique editorial feel from *Section 1*. Implement the sticky header and footer as specified. Wire: **[Agendar llamada]** → GoHighLevel calendar; **Dproperty Select 'Solicitar acceso'** → investor CRM pipeline; **Franquicias 'Agendar/Descargar'** → separate franchise-recruitment CRM pipeline (triggers Prep Pack). Keep `[MOCK]` placeholders visible until real data is supplied. No public prices/units on Select (teaser cards show region/type only). Include an Investment Disclaimer (no guaranteed returns) on Legal. Make it fast, accessible, SEO-clean. Output production code (or Framer/Webflow project)."

## 4. Final Content (self-contained) — Spanish production copy

### Sitemap
`Inicio · Nosotros · Visión/Ecosistema · Servicios · Dproperty Select · Proyectos (opcional) · Franquicias · Contacto · Iniciar sesión · Legal`

### 1. Inicio
- **Titular:** *Los especialistas en inversión inmobiliaria.*
- **Subtítulo:** *Oportunidades curadas y fuera de mercado, con asesoría honesta y basada en números. Acercamos la inversión inmobiliaria seria a más personas. Desde Panamá, para la región.*
- **CTAs:** [ Explorar oportunidades ] · [ Ser franquiciado ]
- **Frase de marca:** *Somos más amigos de la matemática que de la arquitectura.*
- **Franja de confianza:** *Desde 2017 · +$200M transaccionados en Panamá · +700 operaciones · +99% de nuestros clientes nunca perdió capital · +80% vuelve a invertir con nosotros.*
- **Quiénes somos (3 líneas):** *Dproperty es una firma boutique especializada en inversión inmobiliaria. Desde 2017 curamos oportunidades que la mayoría nunca ve: validadas, resguardadas y ofrecidas en condiciones preferenciales. Inversión inmobiliaria de nivel, con trato humano.*
- **Secciones:** Qué hacemos · Dproperty Select (teaser) · Nuestra visión · Conviértete en franquiciado.

### 2. Nosotros
- **Encabezado:** *Quiénes somos.*
- **Nuestra historia (4 bloques):**
  - *2017 — Una firma diferente.* Nació para cerrar la brecha entre las verdaderas oportunidades de inversión y los asesores que entendían sus complejidades — ser la firma especializada en inversión inmobiliaria, sin convertirse en un fondo, y acercar ese mundo a las personas de a pie.
  - *Construyendo el método.* Portafolio curado: validado por el mercado, respaldado por desarrolladores con trayectoria, resguardado por debida diligencia y transparencia → condiciones preferenciales para nuevos inversionistas.
  - *Ganándonos el nombre.* Voz reconocida en Panamá y la región (SIMA Madrid, ELDI Panamá, Gran Salón Inmobiliario Bogotá); CEO en la junta de la Lonja de Bogotá. Preventas fuera de mercado convertidas en referentes: Bioma, Mova, Cavarrosa, Nayamara, Playa Escondida, La Maison by Fendi.
  - *El punto de inflexión — un paso generacional.* La siguiente generación lleva el conocimiento más allá de Panamá. *BluePrint es solo el software que permite que este ecosistema exista; no es el producto. El producto es el ecosistema, y el conocimiento detrás de él.*
- **Misión:** *Conectar a quienes tienen los medios para construir con quienes tienen la visión para liderar, para que el talento nunca dependa de los recursos o los contactos, y los mejores bienes raíces se vuelvan inevitables.*
- **Visión:** *Convertirnos en la casa del talento, el capital y las ideas de los bienes raíces en Latinoamérica e Iberia, concentrando la cadena de valor en un solo lugar curado, para que mejores edificios creen mejores vidas.*
- **Valores (6):** Confianza por encima de la transacción · Curaduría por encima del volumen · Números por encima del ruido · Oficio boutique · Excelencia sistematizada · Mentalidad de ecosistema.
- **Reconocimiento:** SIMA · ELDI · Gran Salón Inmobiliario · Lonja de Bogotá.

### 3. Visión / El Ecosistema
- **Hero:** *Construyendo la casa de los bienes raíces en Latinoamérica e Iberia.*
- **En lo que no transigimos (6):** Boutique, siempre · Confianza y números · La inversión primero · Calidad sin concesiones · Talento por encima del tamaño · Más grande que nosotros.
- **El ecosistema:** *Usar nuestro conocimiento, experiencia y red para potenciar la visión de quienes pueden mover los bienes raíces en sus regiones… los mejores reunidos como maestros artesanos en un gran taller. El alma de un lugar como 19M, aplicada a los bienes raíces.*
- **Diagrama:** Talento · Capital · Ideas → [ Hub curado ] → mejores bienes raíces + nuevos proyectos.
- **¿Por qué Panamá? (6):** economía dolarizada · cruce de las Américas · destino estable y amigable con la inversión · puente LATAM–Iberia · donde nació Dproperty · mercado que premia la curaduría. *Ciudad de Panamá es el primer hogar natural del hub.*
- **Cómo llegamos:** Fase 1 — Franquicia y BluePrint (hoy) · Fase 2 — El ecosistema (estrella polar, financiado por la Fase 1). **CTA:** Súmate a la visión.

### 4. Servicios
- **Encabezado:** *Cómo ayudamos.*
- **Compradores:** *…opciones curadas, guía honesta y cero presión.*
- **Vendedores:** *…equipo boutique y red calificada de compradores e inversionistas serios.*
- **Inversionistas:** *…oportunidades fuera de mercado y en preventa… Inversión inmobiliaria, sin necesidad de ser un experto.* (→ Dproperty Select)
- **Desarrolladores:** *…operación de ventas profesional: demanda calificada, pipeline disciplinado, cuida tu marca y tus números.*
- **Cómo funciona:** 1. Conversamos · 2. Entendemos tu objetivo · 3. Curamos las opciones · 4. Te acompañamos hasta el cierre. **CTA:** Agendar una llamada.

### 5. Dproperty Select
- **Hero:** *Dproperty Select — oportunidades curadas, fuera de mercado.*
- **Qué es:** *Colección curada de oportunidades fuera de mercado y en preventa… validamos, negociamos y aseguramos en condiciones exclusivas antes del mercado abierto… en condiciones preferenciales. Oportunidades pasadas se han convertido en referentes.*
- **Para quién:** *Inversionistas serios que buscan bienes raíces validados y de nivel de inversión, ya sea tu primera inversión o la décima.*
- **CTA:** Solicitar acceso (→ formulario: nombre, correo, perfil de inversión). Sin precios/unidades públicas; teasers solo región/tipo.

### 6. Proyectos *(opcional, fase posterior)*
Filtros (Ubicación · Tipo · Presupuesto · Estado); tarjeta (imagen · nombre · ciudad · desde $ · [Consultar]).

### 7. Franquicias
- **Hero:** *Ten tu propia Dproperty. Lleva la inversión inmobiliaria boutique a tu mercado, con nuestra marca, sistema, formación y red detrás de ti.*
- **CTAs:** [ Agendar una llamada ] · [ Descargar información ].
- **Por qué Dproperty:** *Todo lo que nos tomó construir desde 2017… listo para operar en tu mercado desde el primer día.*
- **Tu camino:** Descubre → Aplica → Firma → Onboarding → Lanzamiento.
- **Qué incluye:** BluePrint · CRM white-label · la Academia · marca y manuales · acompañamiento de lanzamiento · agentes de IA incluidos.
- **Inversión y retorno:** `[pull from Pricing Model / Unit Economics: $30k→$40k, 7.5%, etc.]`.
- **Territorios:** mapa. **Prueba:** *Testimonios muy pronto: podrías ser parte de nuestra primera generación.* **FAQ:** financiamiento · riesgo · tiempos · exclusividad. **CTA:** Agendar una llamada.

### 8. Contacto
- **Encabezado:** *Hablemos.* Izquierda: calendario GoHighLevel ("Soy cliente" / "Quiero una franquicia"). Derecha: formulario breve + `[MOCK]` Oficina: Ciudad de Panamá · hola@dproperty.— · +507 …-…. · Instagram · LinkedIn.

### 9. Iniciar sesión
Branded login → OS (Layer 2). *"¿Nuevo franquiciado? Escríbenos." · "¿Olvidaste tu contraseña?"* SSO-ready.

### 10. Legal
Privacidad · Términos · **Aviso de inversión** (rentabilidades no garantizadas; ties to compliance). Claro y accesible.

## 5. Build & QA Checklist
- [ ] All 10 pages; Spanish copy verbatim; EN toggle.
- [ ] Sticky header + footer per spec; ES/EN works.
- [ ] Palette + serif/sans; boutique editorial feel; responsive + accessible.
- [ ] CTAs wired to correct GHL pipelines (client vs. franchise); calendar embed.
- [ ] Select shows no public prices/units.
- [ ] Investment Disclaimer on Legal.
- [ ] `[MOCK]` placeholders visible until replaced; franchise numbers pulled from Pricing Model.
- [ ] Team section omitted (private for now).

## 6. Source & Change Log
- **Source:** [[../10_Brand_and_Web/Public Site Wireframe]] v0.6 + [[../10_Brand_and_Web/Public Site Copy - ES Master]] v1.0.
- **Change log:** 1.0 (2026-07-21) — handoff created; ES production copy inlined.

## Product architecture acceptance — 2026-09-29 [D]

BlankCRM executes lead capture, legal workflow, commercial approvals, contracts, payment milestones, closing, commissions and post-sale, with communications, automation and commercial dashboards. BluePrint provides CRM-agnostic financial health, expected-vs-actual cash, expense/budget/variance control, KPI/CRM oversight, Glitches, policies, management audit and executive AI recommendations. Commercial execution screens belong in BlankCRM; BluePrint screens show evidence, verification and management intervention. BlankCRM must operate without BluePrint. A BluePrint management decision does not execute a sales action.

Spanish production copy: BlankCRM ejecuta todo el ciclo comercial: captación, calificación, gestión legal, aprobaciones, contratos, hitos de pago, cierre, comisiones y postventa; comunicaciones, automatización y tableros comerciales. Puede operar sin BluePrint. BluePrint es la capa de gestión interna, gobierno e inteligencia, independiente del CRM: salud financiera, caja esperada frente a real, gastos, presupuestos, desviaciones, KPI, supervisión del CRM, procesos y Glitches, auditoría, políticas y roles ejecutivos de IA. Observa, verifica y recomienda; no ejecuta ventas.
