# -*- coding: utf-8 -*-
"""Contenido en español — ofertas 3 a 8."""

from brand import masthead, simple, table, glance, canvas

M = "B_RealEstate<br>24 sept 2026<br>v1.0"
P2 = {}

# ══════════════════════════════════════════════════════════ 3 · VAULTED
P2["03_VAULTED"] = dict(
 file="VAULTED",
 p1=masthead("Producto — Red / Marketplace", "VAULTED",
   "El mercado privado de oportunidades: acceso controlado, coincidencias atribuibles y una comisión "
   "de éxito sobre transacciones completadas.", M)
 + '<div class="cols"><div>'
 + '<h3>La idea</h3>'
 + '<p>VAULTED es el marketplace privado de B_ para oferta inmobiliaria elegible, demanda calificada, '
   'presentaciones y transacciones atribuibles. Es la apuesta de <strong>efecto de red</strong> del '
   'portafolio: mientras BluePrint es el motor de software, VAULTED es el motor potencial de red.</p>'
 + '<h3 class="mt">Estado honesto</h3>'
 + '<p><strong>Hipótesis, no negocio.</strong> Cero transacciones, cero listados, cero participantes '
   'firmados. Está deliberadamente <strong>bloqueado</strong> detrás de la estabilidad de BluePrint. '
   'Este documento existe para poder razonar y refutar la economía, no para citarla.</p>'
 + '<h3 class="mt">Qué controlaría</h3>'
 + '<p class="small">Listados y oportunidades · reglas de acceso · identidad de participantes · '
   'coincidencias y presentaciones · <strong>atribución</strong> · registros de transacciones '
   'completadas · volumen transado (GMV) y comisiones del marketplace.</p>'
 + '<h3 class="mt">Qué NO controla</h3>'
 + '<p class="small soft">Conversaciones del CRM · procesos de gestión y ejecución de transacciones '
   'de BluePrint · contabilidad · decisiones de curaduría de Dproperty Select · '
   '<strong>custodia, fideicomiso, cambio de divisas o vehículos de inversión</strong> — '
   'explícitamente fuera de alcance.</p>'
 + '</div>'
 + glance([("Tipo","Producto — red. Máximo potencial, mínima evidencia."),
           ("Trabajo","Dar acceso y conectar oferta con demanda."),
           ("Precio",'<strong>0.35%</strong> del valor de la transacción atribuible '
                     '<span class="chip">[A]</span>'),
           ("Estado","<strong>Bloqueado.</strong> Sin producto, sin economía validada."),
           ("Próxima meta","Prueba de liquidez en un nicho estrecho con relaciones existentes")],
          [("$1,050","Ingreso por transacción de $300k"),("5 de 7","Etapas del embudo sin base"),
           ("100+","Transacciones/año para ser relevante"),("0","Transacciones hoy")])
 + '</div>'
 + '<div class="callout"><strong>Regla de modelado obligatoria:</strong> nunca estimar el ingreso de '
   'VAULTED como «todos los clientes de BluePrint × un GMV arbitrario». Hay que modelar el embudo '
   'completo, donde <strong>cada etapa se prueba por separado</strong>.</div>'
 + '<h2 style="margin-top:4mm"><span class="snum">01</span>El embudo — siete etapas</h2>'
 + table(["Etapa","Supuesto","Base","Confianza"], [
     ["Valor promedio de transacción","$300,000","Modelo de portafolio","Baja-media"],
     ["Comisión efectiva","0.35%","Modelo de portafolio","<strong>Baja</strong>"],
     ["Tasa de activación","?","<strong>ninguna</strong>","<strong>Sin base</strong>"],
     ["Tasa de publicación de oferta","?","<strong>ninguna</strong>","<strong>Sin base</strong>"],
     ["Tasa de coincidencia","?","<strong>ninguna</strong>","<strong>Sin base</strong>"],
     ["Supervivencia de atribución","?","<strong>ninguna</strong>","<strong>Sin base — la crítica</strong>"],
     ["Fuga / elusión","?","<strong>ninguna</strong>","<strong>Sin base</strong>"]], None, 3)
 + '<p class="note">El ingreso es el producto de <strong>siete</strong> factores inciertos. Si cada uno '
   'se equivoca por la mitad, el ingreso se equivoca por ~100×. Por eso está bloqueado.</p>'
 + '<h2 style="margin-top:3mm"><span class="snum">02</span>Escala requerida</h2>'
 + table(["Transacciones atribuibles/año","GMV","Ingreso a 0.35%"], [
     ["10","$3.0M","$10,500"],["50","$15.0M","$52,500"],
     ["200","$60.0M","$210,000"],["500","$150.0M","$525,000"]])
 + '<p class="note">Para contexto: toda la historia de Dproperty se cita en ~700 operaciones. VAULTED '
   'necesita <strong>cientos de transacciones atribuibles al año</strong> para ser una línea de ingreso '
   'relevante. No es una historia de ingreso cercano — es una <strong>opción de red</strong>.</p>'
 + simple([
     "Cobraríamos <strong>0.35%</strong> de cada operación cerrada por la plataforma. En una propiedad "
     "de $300,000 son <strong>$1,050</strong>.",
     "Para que esto sea un negocio real necesitamos <strong>cientos de operaciones al año</strong>. "
     "Hoy tenemos <strong>cero</strong>.",
     "La pregunta que decide si esto existe: <strong>si presentamos al comprador y al vendedor, ¿qué "
     "impide que cierren por fuera y no nos paguen?</strong> Hasta que eso tenga respuesta de contrato, "
     "ningún otro número importa.",
     "Ojo con algo incómodo: <strong>$1,050 puede ser menos de lo que cuesta pelear un caso dudoso</strong>. "
     "Tal vez conviene cobrar más en menos operaciones mejor documentadas.",
     "Por eso está <strong>detenido a propósito</strong> hasta que BluePrint esté estable. Es la apuesta "
     "de mayor potencial y la de menor evidencia."]),
 p2=masthead("VAULTED", "Modelo de Negocio", None, "B_RealEstate<br>24 sept 2026", small=True)
 + canvas(dict(
   kp=["Desarrolladores — siembran oferta","Red de corredores","Inversionistas existentes",
       "Asesoría legal por jurisdicción","Proveedores de identidad y KYC"],
   ka=["Diseño de atribución","Curaduría y verificación de acceso","Emparejamiento",
       "Gestión de disputas","Cumplimiento por jurisdicción"],
   vp=["Acceso a oportunidades fuera de mercado",
       "Demanda calificada para quien tiene oferta",
       "Presentaciones con atribución documentada",
       "Reglas de acceso claras — no es un portal abierto",
       "<strong>Potencial de efecto de red</strong>: más participantes, más valor"],
   cr=["Acceso por invitación","Curaduría activa de participantes","Gestión de relación por acuerdo"],
   cs=["Desarrolladores con inventario","Corredores con compradores",
       "Inversionistas buscando oportunidad","Franquicias y socios elegibles"],
   kr=["<strong>La red de relaciones existente</strong> — ventaja de arranque en frío",
       "Motor de atribución","Reglas de acceso y elegibilidad","Registro de transacciones"],
   ch=["Relaciones existentes de Dproperty","Canal de desarrolladores",
       "Franquicias y socios B_ Partner","BlankCRM aporta demanda autorizada"],
   cost=["Construcción de producto","<strong>Atribución y disputas — intensivo en trabajo</strong>",
         "Verificación de participantes","Legal por jurisdicción","Siembra de red"],
   rev=["Comisión de éxito sobre transacciones atribuibles — 0.35% efectivo hipotético",
        "Posible después: membresía o acceso premium",
        "Posible después: servicios de datos agregados con consentimiento",
        "<strong>Sin ingreso hoy</strong> — producto no construido"]))
 + '<h2 style="margin-top:5mm"><span class="snum">03</span>Secuencia obligatoria</h2>'
 + '<p class="small">Probar en este orden, y <strong>detenerse si una falla</strong>: '
   '<strong>1)</strong> liquidez de oferta en un nicho estrecho donde ya tenemos relaciones · '
   '<strong>2)</strong> liquidez de demanda calificada · <strong>3)</strong> atribución evidenciable · '
   '<strong>4)</strong> control de fuga · <strong>5)</strong> disposición a pagar la comisión · '
   '<strong>6)</strong> estructura legal por jurisdicción con abogado.</p>'
 + '<div class="callout gold"><strong>Sin automatización del marketplace ni expansión geográfica</strong> '
   'antes de la revisión de meta a 90 días.</div>'
 + simple("En una frase: <strong>es la apuesta grande que todavía no hemos hecho.</strong> Si funciona, "
   "deja de ser software con crecimiento lineal y se convierte en una red que se vuelve más valiosa "
   "sola. Si no funciona, no perdimos casi nada porque está detenido a propósito. Nuestra ventaja real "
   "es que ya conocemos a los desarrolladores y corredores — eso es lo difícil de copiar."),
)

# ══════════════════════════════════════════════════════════ 4 · BUILDING BLOCKS
P2["04_Building_Blocks"] = dict(
 file="Building Blocks",
 p1=masthead("Producto — Formación y certificación", "Building Blocks",
   "Convierte los estándares de operación en capacidad transferible: currículos por rol, evaluación "
   "y certificación con evidencia.", M)
 + '<div class="cols"><div>'
 + '<h3>La idea</h3>'
 + '<p>Building Blocks es el producto independiente de formación, incorporación y certificación. '
   'Convierte los estándares de operación en currículos por rol y preserva la asignación, la '
   'finalización, la certificación, el vencimiento y la evidencia de competencia.</p>'
 + '<p>Funciona sobre <strong>Open edX</strong> como infraestructura. Open edX es el motor; Building '
   'Blocks es el producto.</p>'
 + '<h3 class="mt">Por qué es un producto independiente</h3>'
 + '<p>Cada producto del portafolio se define, se cotiza y se vende por separado — para que el paquete '
   'de franquicia sea una <strong>composición de productos con nombre</strong>, no un monolito. '
   'Cuatro productos fuertes se venden mejor que un producto que «lo tiene todo».</p>'
 + '<h3 class="mt">El diferenciador — el ciclo cerrado</h3>'
 + '<p class="small">Procedimiento aprobado → ejecución → <strong>BluePrint detecta una falla de '
   'proceso</strong> → se identifica la brecha de capacidad → módulo o cohorte de Building Blocks → '
   'evaluación y certificación → <strong>BluePrint habilita o bloquea el privilegio</strong> → '
   'resultado medido en BluePrint.</p>'
 + '<p class="small"><strong>El ciclo es la ventaja, no el contenido.</strong> El contenido es un '
   'commodity; hay material gratuito de sobra. Ningún competidor de formación tiene la señal de falla '
   'operativa que genera la inscripción, y ningún competidor de gestión tiene la ruta de remediación.</p>'
 + '</div>'
 + glance([("Tipo","Producto independiente de formación. No es donde está la ventaja competitiva."),
           ("Trabajo","Hacer transferible la capacidad."),
           ("Precio",'<strong>$199</strong> por inscripción (promedio) · certificación $199–$349 · '
                     'cohortes empresariales cotizadas <span class="chip">[A]</span>'),
           ("Estado","Arquitectura definida. <strong>Año 1 pierde dinero</strong> en todos los escenarios."),
           ("Próxima meta","Cotizar el LMS y demostrar enganche vía señales de BluePrint")],
          [("$199","Inscripción promedio"),("40–126","Inscripciones/año para equilibrio"),
           ("~95%","Margen de la inscripción marginal"),("$8k–25k","Costo anual de plataforma")])
 + '</div>'
 + '<h2 style="margin-top:4mm"><span class="snum">01</span>Economía</h2>'
 + '<div class="cols2">'
 + table(["Opción de plataforma","Costo anual","Por usuario/mes"], [
     ["Gestionada compartida (≤1,500 usuarios)","$8,000","~$0.44"],
     ["Autogestionada + soporte","~$16,200","variable"],
     ["Instancia dedicada, ilimitada","$25,000","—"]], "Costo de plataforma [F] tarifas de mercado")
 + table(["Base de costo anual","Inscripciones para equilibrio"], [
     ["$8,000 plataforma","~40"],
     ["$16,000 plataforma","~80"],
     ["$8,000 + $6,667 contenido","~74"],
     ["$16,000 + $6,667 contenido","~114"]], "Punto de equilibrio")
 + '</div>'
 + '<div class="callout"><strong>Verificación contra el modelo.</strong> La proyección muestra '
   '<strong>$8.6k de ingreso en año 1</strong> — unas <strong>43 inscripciones</strong>. Eso está '
   '<strong>por debajo del equilibrio</strong> en cualquier escenario que incluya amortización de '
   'contenido. Building Blocks <strong>pierde dinero en el año 1 en todos los escenarios modelados</strong>, '
   'alcanza el equilibrio en el año 2, y los <strong>$84.2k proyectados al año 3</strong> (~423 '
   'inscripciones) sí son cómodamente rentables.</div>'
 + '<p class="note"><strong>El riesgo económico real: el contenido es un costo fijo que se comporta '
   'como una suscripción.</strong> Siete procesos × varios roles × varios mercados, más localización. '
   'Cada cambio de proceso deja un módulo obsoleto. La carga de mantenimiento crece con el '
   '<strong>número de mercados</strong>, no con el ingreso.</p>'
 + simple([
     "Cobramos <strong>$199 por curso</strong> a cada persona. No es una suscripción mensual: "
     "es un pago cada vez que alguien se inscribe.",
     "La plataforma nos cuesta entre <strong>$8,000 y $25,000 al año</strong>. Necesitamos entre "
     "<strong>40 y 126 inscripciones al año</strong> solo para pagarla.",
     "<strong>El año 1 pierde dinero. Sin excepción.</strong> Empieza a ganar en el año 2 y al año 3 "
     "ya es claramente rentable. Es normal en este tipo de producto, pero hay que decirlo.",
     "El peligro escondido: <strong>mantener el contenido actualizado</strong>. Cada vez que cambiamos "
     "un proceso, hay que rehacer un curso. Eso cuesta todos los años, no una sola vez.",
     "Para la franquicia vale muchísimo aunque gane poco: es lo que hace que <strong>una oficina nueva "
     "opere igual que las demás</strong>."]),
 p2=masthead("Building Blocks", "Modelo de Negocio", None, "B_RealEstate<br>24 sept 2026", small=True)
 + canvas(dict(
   kp=["<strong>Open edX</strong> — plataforma","Proveedor de hosting gestionado",
       "Expertos de contenido por materia","Cuerpos de certificación locales donde aplique"],
   ka=["Producción de currículo","<strong>Mantenimiento de contenido</strong> — recurrente",
       "Diseño de evaluaciones","Administración de certificación","Entrega de cohortes"],
   vp=["Una oficina nueva opera al estándar <strong>en semanas</strong>",
       "Certificación que <strong>habilita privilegios</strong> en BluePrint",
       "Cierra brechas detectadas por fallas reales de proceso",
       "Evidencia de competencia auditable",
       "Consistencia entre oficinas — el problema central de una franquicia"],
   cr=["Currículo asignado por rol","Cohortes con instructor para empresas","Autoservicio para cursos sueltos"],
   cs=["Equipos nuevos de franquicia y socios","Clientes de BluePrint con rotación o ascensos",
       "Equipos de venta de desarrolladores","Profesionales independientes del sector"],
   kr=["<strong>La Biblioteca de Procesos</strong> como fuente del contenido",
       "Currículos por rol","Registro de certificación y vencimientos","Integración con BluePrint"],
   ch=["Incluido en incorporación de franquicia y socios",
       "<strong>Enganche disparado por señales de BluePrint</strong>",
       "Cohortes para desarrolladores","Venta directa de cursos"],
   cost=["Plataforma LMS — $8k–$25k/año","<strong>Producción de contenido</strong> — fijo, grande",
         "<strong>Mantenimiento de contenido</strong> — 15–30% del costo de construcción al año",
         "Administración de certificación","Entrega de cohortes","Soporte al alumno"],
   rev=["Incorporación base — incluida en paquetes, valorizada a precio de lista",
        "Cursos especializados — $199 por inscripción (promedio)",
        "Certificación — $199–$349 por programa",
        "Cohortes empresariales y de desarrolladores — licencia cotizada",
        "Supuesto de volumen: 1.5 inscripciones pagadas por cliente al año"]))
 + '<h2 style="margin-top:5mm"><span class="snum">02</span>Meta — no gastar antes de esto</h2>'
 + '<p class="small"><strong>No invertir en producción de contenido más allá de la incorporación base '
   'de franquicia hasta que:</strong> 1) el currículo base esté <strong>dimensionado</strong> — el rango '
   'de $7k–$48k debe estrecharse; 2) exista una <strong>cotización formal del LMS</strong>; 3) se '
   'demuestre el <strong>enganche</strong> con inscripciones disparadas por señales reales de BluePrint.</p>'
 + '<p class="note">La formación incluida se justifica por consistencia de franquicia y retención por sí '
   'sola. <strong>El ingreso independiente tiene que ganarse su propia inversión.</strong></p>'
 + '<h2 style="margin-top:3mm"><span class="snum">03</span>Límites que no se cruzan</h2>'
 + '<p class="small soft">No emite <strong>títulos acreditados</strong> y nunca debe insinuarlo · no '
   'reemplaza formación legal o de cumplimiento donde la regulación exige un proveedor acreditado · '
   'nunca se convierte en el sistema de registro de procesos — eso es BluePrint · no almacena '
   'expedientes de transacciones.</p>'
 + simple("En una frase: <strong>es lo que hace que una franquicia nueva trabaje como las demás.</strong> "
   "Gana poco dinero al principio y hay que ser honestos con eso. Su valor está en que una oficina nueva "
   "llegue al estándar rápido, y en que cuando BluePrint detecta que alguien está fallando, exista "
   "un lugar concreto a dónde mandarlo."),
)
