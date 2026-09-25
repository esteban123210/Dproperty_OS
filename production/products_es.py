# -*- coding: utf-8 -*-
"""Contenido en español de los ocho dos-páginas de oferta."""

from brand import masthead, simple, table, glance, canvas

M = "B_RealEstate<br>24 sept 2026<br>v1.0"

P = {}

# ══════════════════════════════════════════════════════════ 1 · BLUEPRINT
P["01_BluePrint"] = dict(
 file="BluePrint",
 p1=masthead("Producto — Núcleo propietario", "BluePrint",
   "El sistema operativo de gestión que controla el negocio desde la oportunidad calificada "
   "hasta la comisión y la auditoría.", M)
 + '<div class="cols"><div>'
 + '<h3>La idea</h3>'
 + '<p>BluePrint es el sistema operativo de back-office y transacciones para inmobiliarias '
   'pequeñas y medianas. Toma autoridad en el momento en que un prospecto se convierte en '
   '<strong>oportunidad calificada</strong>, y controla todo lo necesario para llevarla a un '
   'cierre documentado: partes, evidencia de cumplimiento, documentos, aprobaciones, hitos '
   'contractuales, comisiones, reportes e historial de auditoría.</p>'
 + '<p>Está construido para inmobiliarias dirigidas por buenos vendedores que no tienen tiempo '
   'ni vocación para la administración. <strong>Un coordinador capaz más BluePrint</strong> debería '
   'reemplazar la estructura de gestión que una agencia en crecimiento tendría que contratar.</p>'
 + '<p>Es conversacional: lenguaje natural de entrada, registros estructurados y auditables de salida.</p>'
 + '<h3 class="mt">El problema</h3>'
 + '<p>La información crítica está dispersa en chats, drives, hojas de cálculo, CRMs y la memoria '
   'de cada persona. Los traspasos fallan, faltan documentos, las aprobaciones son invisibles, las '
   'comisiones se disputan, y el reporte de gestión se reconstruye a mano cada mes.</p>'
 + '<h3 class="mt">Qué controla</h3>'
 + '<p class="small">Ingreso de oportunidad calificada · el expediente de la transacción · documentos, '
   'listas de cumplimiento y evidencia · políticas de aprobación y firma electrónica · hitos de '
   'contrato y cierre · <strong>reglas de comisión, cálculos y estado de pago</strong> · presupuestos, '
   'variaciones e indicadores · aseguramiento de procesos e incidencias · cierre de período · '
   'auditoría de largo plazo · Copiloto con permisos.</p>'
 + '<h3 class="mt">Qué NO controla</h3>'
 + '<p class="small soft">Prospectos, automatización de marketing y el embudo previo a la calificación '
   '(BlankCRM) · <strong>inventario</strong> de propiedades, proyectos y unidades, listados o MLS · '
   'contabilidad, impuestos y nómina · administración de propiedades · entrega de cursos '
   '(Building Blocks) · listados del marketplace (VAULTED) · fideicomiso, custodia y movimiento de dinero.</p>'
 + '</div>'
 + glance([("Tipo","Producto — núcleo propietario. Aquí está la ventaja competitiva."),
           ("Trabajo","Operar y controlar la empresa."),
           ("Precio",'$1,500 implementación · Core <strong>$399</strong>/mes · Growth '
                     '<strong>$799</strong>/mes, por organización <span class="chip">[A]</span>'),
           ("Estado","Especificación completa. Prioridad de construcción. Sin validación pagada."),
           ("Próxima meta","5 socios de diseño → 3 conversiones pagadas")],
          [("$4,788","Valor anual contrato Core"),("$9,588","Valor anual contrato Growth"),
           ("3.3 meses","Recuperación de CAC"),("3–50","Tamaño objetivo, personas")])
 + '</div>'
 + '<div class="callout"><strong>El límite en una línea:</strong> BluePrint es dueño de '
   '<em>el negocio como objeto de gestión gobernado</em>. No es dueño de '
   '<em>la propiedad como inventario</em>.</div>'
 + '<h2 style="margin-top:4mm"><span class="snum">01</span>Economía</h2>'
 + '<div class="cols2">'
 + table(["Concepto","Cifra"], [
     ["Costo anual, Core","$4,788 + $1,500"],
     ["Costo anual, Growth","$9,588 + $1,500"],
     ['Contratación de back-office que evita <span class="chip">[A]</span>',"$18k–$35k"],
     ['Esfuerzo de implementación <span class="chip">[T]</span>',"&lt;40 → &lt;20 h"],
     ['Tiempo a producción <span class="chip">[T]</span>',"&lt;21 días"]], "Para el cliente")
 + table(["Concepto","Cifra"], [
     ['ARR de software por cliente <span class="chip">[M]</span>',"$4,645.80"],
     ['Contribución de margen bruto <span class="chip">[M]</span>',"$3,600.40"],
     ['CAC <span class="chip">[M]</span>',"$1,000"],
     ['Recuperación de CAC <span class="chip">[M]</span>',"3.33 meses"],
     ['Parte del ingreso año 5 <span class="chip">[M]</span>',"$1.285M / $1.844M"]], "Para B_RealEstate")
 + '</div>'
 + '<p class="note"><strong>Advertencias explícitas.</strong> Son resultados de modelo sobre supuestos '
   'sin validar, no resultados reales. La retención se modela con 8% de abandono anual sin evidencia de '
   'cohortes, por lo que <strong>el LTV no se reporta deliberadamente</strong>. El costo propio de '
   'BluePrint —IA, integraciones y soporte por cliente— <strong>aún no está modelado</strong> '
   '<span class="chip">[R]</span>.</p>'
 + simple([
     "Cobramos <strong>$399 o $799 al mes</strong> por empresa, más <strong>$1,500</strong> de arranque. "
     "No cobramos por vendedor.",
     "Cada cliente deja alrededor de <strong>$3,600 al año</strong> de margen y nos cuesta unos "
     "<strong>$1,000</strong> conseguirlo. Se paga solo en <strong>poco más de tres meses</strong>.",
     "Para el cliente la cuenta es sencilla: si le evita contratar <strong>una sola persona</strong> "
     "de administración, ya salió ganando.",
     "Lo que todavía no sabemos: cuánto nos cuesta <strong>atender</strong> a cada cliente. Sin eso, "
     "el margen real está por confirmarse.",
     "Aquí está el <strong>valor de la empresa</strong>. Es lo único que puede convertirse en una "
     "compañía de software valiosa por sí sola."]),
 p2=masthead("BluePrint", "Modelo de Negocio", None, "B_RealEstate<br>24 sept 2026", small=True)
 + canvas(dict(
   kp=["GoHighLevel — motor de BlankCRM","Open edX — Building Blocks","Nube y proveedores de IA",
       "Firma electrónica","Almacenamiento documental","Asesores contables y legales"],
   ka=["Ingeniería de producto y seguridad","Diseño de flujos de trabajo","Integraciones",
       "Implementación","Soporte","Analítica"],
   vp=["Transacciones controladas de la calificación al cierre","Menos traspasos fallidos y "
       "documentos perdidos","Comisiones exactas y auditables",
       "Visibilidad de gestión <strong>sin contratar un gerente</strong>",
       "Una sola fuente de verdad operativa",
       "Jerarquía de verificación: reportado → verificado operativamente → verificado "
       "financieramente → cerrado"],
   cr=["Implementación de alto contacto","Migración a onboarding estandarizado","Éxito en producto y Copiloto"],
   cs=["Inmobiliarias boutique, 3–50 personas","Equipos de venta de desarrolladores",
       "Franquicias Dproperty","Socios de marca propia B_ Partner"],
   kr=["Modelo de datos y motor de flujos","Biblioteca de plantillas","Historial de auditoría",
       "Propiedad intelectual de implementación","Equipo"],
   ch=["Venta directa del fundador","Socios de diseño","Canal de franquicia y socios",
       "Relaciones con desarrolladores","Building Blocks"],
   cost=["Ingeniería y producto","Nube, API e inferencia de IA","Seguridad y cumplimiento",
         "Trabajo de implementación","Soporte","Ventas y marketing"],
   rev=["Implementación y migración — $1,500, más si la migración es compleja",
        "Suscripción Core — $399/mes por organización",
        "Suscripción Growth — $799/mes por organización",
        "Consumo: IA, almacenamiento y mensajes sobre el límite incluido",
        "Integraciones e implementación premium, cotizadas",
        "Nivel Scale — cotizado, deliberadamente sin definir"]))
 + '<h2 style="margin-top:5mm"><span class="snum">02</span>Qué hay que demostrar</h2>'
 + '<p class="small">Cinco socios de diseño y tres conversiones pagadas · una transacción completa '
   'corrida <strong>sin que una hoja de cálculo paralela sea la autoridad</strong> · pruebas de '
   'aislamiento entre clientes, permisos y auditoría · implementación bajo 40 horas y luego bajo 20 · '
   'usuarios activos semanales sobre 60% · finalización de flujos críticos sobre 70% al mes 9 · '
   'margen bruto, recuperación y retención observados por cohorte.</p>'
 + '<div class="callout gold"><strong>Condición de abandono.</strong> Si las inmobiliarias objetivo '
   'prefieren consistentemente un stack configurado de Odoo / GoHighLevel / contabilidad y no pagan '
   'de forma material por la capa de gestión, detener o reposicionar antes de un gasto grande de '
   'desarrollo.</div>'
 + '<h2 style="margin-top:4mm"><span class="snum">03</span>Por qué se puede defender</h2>'
 + '<p class="small">Profundidad de ajuste al flujo de trabajo, plantillas y paquetes de configuración '
   'acumulados, confiabilidad de integraciones, historial de transacciones y auditoría acumulado, '
   'velocidad de implementación, y alto costo de cambio una vez que BluePrint es el sistema de registro.</p>'
 + '<p class="note">El competidor a vencer no es SkySlope ni Dotloop — es <strong>CRM más hojas de '
   'cálculo más drives compartidos más WhatsApp más el conocimiento del personal</strong>.</p>'
 + simple("En una frase: <strong>es el cerebro operativo de la inmobiliaria.</strong> El CRM consigue "
   "clientes; BluePrint se encarga de que el negocio se cierre bien, que los papeles estén, que la "
   "comisión salga exacta y que el dueño pueda ver la verdad sin pedirle un reporte a nadie."),
)

# ══════════════════════════════════════════════════════════ 2 · BLANKCRM
P["02_BlankCRM"] = dict(
 file="BlankCRM",
 p1=masthead("Producto — Producto de enganche", "BlankCRM",
   "El front-office inmobiliario configurado, impulsado por GoHighLevel. Consigue clientes y no "
   "pierde oportunidades.", M)
 + '<div class="cols"><div>'
 + '<h3>La idea</h3>'
 + '<p>BlankCRM es el producto de front-office de B_ configurado para el sector inmobiliario, '
   '<strong>impulsado por GoHighLevel</strong>. Se vende como un ambiente práctico de operación '
   'comercial, no como tecnología propietaria de CRM.</p>'
 + '<p>Somos transparentes sobre el motor. B_ evita deliberadamente gastar capital de ingeniería '
   'propio en reconstruir infraestructura de CRM que ya es un commodity — ese capital va a BluePrint '
   'y VAULTED.</p>'
 + '<h3 class="mt">El hallazgo que cambia la economía</h3>'
 + '<p>GoHighLevel Agency Pro cuesta <strong>$497 al mes fijos</strong> e incluye <strong>sub-cuentas '
   'ilimitadas</strong> y la posibilidad de <strong>refacturar el consumo con margen</strong>. Eso '
   'significa que cada cliente adicional cuesta <strong>$0</strong> en plataforma.</p>'
 + '<h3 class="mt">Qué controla</h3>'
 + '<p class="small">Gestión de prospectos y contactos · flujos de WhatsApp, correo y SMS · '
   'formularios, páginas de aterrizaje y calendarios · seguimiento y maduración · embudo comercial '
   '<strong>previo a la calificación</strong> y actividad de vendedores · atribución de campañas · '
   'automatizaciones del equipo comercial.</p>'
 + '<h3 class="mt">Qué NO controla</h3>'
 + '<p class="small soft">Todo lo posterior a la calificación — expediente de transacción, '
   'cumplimiento, aprobaciones, cierre, comisión (BluePrint) · presupuestos y control financiero · '
   'la verdad oficial de gestión · contabilidad · listados del marketplace (VAULTED) · auditoría '
   'de gestión de largo plazo.</p>'
 + '</div>'
 + glance([("Tipo","Producto de enganche. Deliberadamente <em>no</em> es la ventaja competitiva."),
           ("Trabajo","Vender más y perder menos oportunidades."),
           ("Precio",'$750 configuración · <strong>$249</strong>/mes por oficina · consumo '
                     'refacturado con margen <span class="chip">[A]</span>'),
           ("Estado","Precio respaldado en costos desde 2026-09-24."),
           ("Próxima meta","Probar venta directa y enganche a BluePrint por separado")],
          [("$497","Costo fijo mensual total de plataforma"),("$0","Costo marginal por cliente"),
           ("2–3","Clientes para punto de equilibrio"),("65–91%","Margen bruto según escala")])
 + '</div>'
 + '<h2 style="margin-top:4mm"><span class="snum">01</span>Economía</h2>'
 + '<div class="cols2">'
 + table(["Clientes","Plataforma","Margen bruto","MB %"], [
     ["5","$99.40","$112–$137","45–55%"],
     ["10","$49.70","$162–$187","65–75%"],
     ["25","$19.88","$192–$217","77–87%"],
     ["50","$9.94","$202–$227","81–91%"]], "Margen mejora con la escala")
 + table(["Concepto","Cifra"], [
     ["Cuota de configuración","$750"],
     ['Trabajo de onboarding, 8–12 h <span class="chip">[A]</span>',"$200–$480"],
     ["<strong>Contribución</strong>","<strong>$270–$550</strong>"],
     ['Soporte mensual, 0.5–1.5 h <span class="chip">[A]</span>',"$12.50–$37.50"],
     ["Plataforma GHL Agency Pro","$497/mes fijo"]], "Configuración y soporte")
 + '</div>'
 + '<p class="note"><strong>El margen es un problema de disciplina de soporte, no de precio.</strong> '
   'Cada hora de soporte no planificado cuesta $25–40 contra un ticket mensual de $249. Si el '
   'onboarding pasa de 15 horas, la cuota de configuración se vuelve pérdida.</p>'
 + simple([
     "Cobramos <strong>$750</strong> de arranque y <strong>$249 al mes</strong> por oficina.",
     "La plataforma nos cuesta <strong>$497 al mes en total</strong>, sin importar si tenemos 3 o "
     "300 clientes. Con <strong>2 o 3 clientes ya la pagamos</strong>; a partir de ahí casi todo es margen.",
     "El consumo de mensajes y llamadas <strong>se lo refacturamos al cliente con margen</strong>. "
     "No lo absorbemos.",
     "El riesgo real no es el precio: es <strong>cuánto soporte pide cada cliente</strong>. Si pide "
     "más de hora y media al mes, el margen se come.",
     "El otro riesgo es que <strong>todo depende de GoHighLevel</strong>. Si ellos cambian precios o "
     "condiciones, nos afecta a todos los clientes a la vez. Lo aceptamos a cambio de no gastar "
     "nuestro dinero construyendo un CRM."]),
 p2=masthead("BlankCRM", "Modelo de Negocio", None, "B_RealEstate<br>24 sept 2026", small=True)
 + canvas(dict(
   kp=["<strong>GoHighLevel</strong> — el motor completo","Proveedores de mensajería y voz",
       "Meta / WhatsApp Business API","Proveedores de IA"],
   ka=["Configuración vertical inmobiliaria","Construcción de embudos y automatizaciones",
       "Onboarding de clientes","Soporte","Integración con BluePrint"],
   vp=["Front-office listo para inmobiliaria, no genérico",
       "Configurado en días, no semanas de auto-armado",
       "<strong>Traspaso a BluePrint</strong> en la oportunidad calificada",
       "Una sola relación de soporte para CRM y back-office",
       "Consumo refacturado de forma transparente"],
   cr=["Configuración hecha por nosotros","Soporte compartido con BluePrint","Autoservicio en producto"],
   cs=["Inmobiliarias que necesitan CRM y aún no están listas para BluePrint",
       "Clientes de BluePrint como enganche","Franquicias y socios B_ Partner",
       "Equipos de desarrolladores"],
   kr=["Plantillas de configuración vertical","Cuenta Agency Pro con sub-cuentas ilimitadas",
       "Biblioteca de automatizaciones","Conector a BluePrint"],
   ch=["Enganche a BluePrint","Venta directa como producto de entrada",
       "Incluido en paquetes de franquicia y socios"],
   cost=["GHL Agency Pro — $497/mes fijo","Trabajo de onboarding","Trabajo de soporte",
         "Consumo de mensajería (refacturado)"],
   rev=["Configuración — $750 por oficina","Suscripción — $249/mes por oficina",
        "Refacturación de mensajería, voz e IA con margen",
        "Complemento AI Employee — $97/mes por sub-cuenta, refacturado",
        "Migración compleja y oficinas adicionales, cotizadas"]))
 + '<h2 style="margin-top:5mm"><span class="snum">02</span>Riesgos que importan</h2>'
 + table(["Riesgo","Severidad","Nota"], [
     ["<strong>Dependencia de un solo proveedor</strong>","<strong>Alta</strong>",
      "Todo el producto es GoHighLevel. Un cambio de precio, condiciones o una caída afecta a todos los clientes a la vez. No hay segunda fuente."],
     ["Soporte sobre 1.5 h/cliente/mes","<strong>Alta</strong>","El principal destructor de margen. Medir desde el primer cliente."],
     ["Onboarding sobre 15 horas","Media","Convierte la cuota de configuración en pérdida."],
     ["GHL cambia condiciones de refacturación","Media","Convertiría el consumo de margen en costo."],
     ["El cliente descubre que puede comprar GHL directo","Media",
      "Se mitiga con la configuración vertical, la integración y el soporte — <strong>nunca</strong> ocultando el motor."]], None, 1)
 + simple("En una frase: <strong>es nuestro producto de entrada, y es rentable casi desde el primer "
   "cliente.</strong> No es donde está nuestro valor como empresa —eso es BluePrint— pero nos permite "
   "entrar barato a una inmobiliaria, y después subirla a BluePrint. Lo honesto es decirlo: el motor "
   "es GoHighLevel y nosotros lo configuramos, lo integramos y lo soportamos."),
)
