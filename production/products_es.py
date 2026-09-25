# -*- coding: utf-8 -*-
"""Contenido en español de los dos-páginas de oferta — 1 y 2."""

from brand import masthead, simple, table, glance, canvas

M = "B_RealEstate<br>25 sept 2026<br>v2.0"

P = {}

# ══════════════════════════════════════════════════════════ 1 · BLUEPRINT
P["01_BluePrint"] = dict(
 file="BluePrint",
 p1=masthead("Producto — Núcleo propietario", "BluePrint",
   "Un back office agéntico: te da un CEO, CFO, COO y CMO en un solo lugar, sin el costo de "
   "contratar una gerencia completa.", M)
 + '<div class="cols"><div>'
 + '<h3>El problema, dicho con precisión</h3>'
 + '<p>Un CRM hace muchas cosas bien. Estandariza embudos, calcula divisiones de comisión, adjunta '
   'documentos y le dice al equipo comercial cuál es el debido proceso.</p>'
 + '<p><strong>Pero lo que sale de un CRM vale exactamente lo que vale la disciplina de quien lo '
   'alimenta — y esa es la misma gente a la que se le paga según lo que el CRM reporta.</strong></p>'
 + '<p class="small">Entonces un negocio se marca como cerrado antes de tiempo. O se mal clasifica: '
   'tipo equivocado, etapa equivocada, monto equivocado. Y el resultado es que '
   '<strong>las ventas del CRM no cuadran con lo que contabilidad realmente procesó, ni con las '
   'cuentas por cobrar reales</strong>. Nadie puede decir cuál número es el verdadero, y la gerencia '
   'termina operando por intuición.</p>'
 + '<div class="callout gold"><strong>El buen uso del CRM es, en sí mismo, la principal dependencia '
   'del CRM.</strong> Ese es el hueco que BluePrint existe para cerrar. BluePrint no depende de la '
   'disciplina de nadie: <strong>solo registra lo que tiene comprobante</strong>.</div>'
 + '<h3 class="mt">Las dos reglas que definen el producto</h3>'
 + '<p class="small"><strong>1 · Nada se registra sin evidencia.</strong> Una venta, una compra o un '
   'pago se registran únicamente cuando existe el adjunto válido — recibo, factura, contrato, '
   'comprobante bancario. Sin adjunto, no hay registro.</p>'
 + '<p class="small"><strong>2 · Los agentes gestionan, no solo reportan.</strong> No dibujan un tablero '
   'y esperan. Detectan, explican, sugieren y escalan.</p>'
 + '<h3 class="mt">La interfaz</h3>'
 + '<p class="small">Todo pasa por detrás. <strong>Al frente solo hay un chat.</strong> Debajo están los '
   'manuales, los procesos, la biblioteca de conocimiento de la empresa, las plantillas, los contactos '
   'y los registros. El producto es ultracompleto; la experiencia es tan simple o tan profunda como el '
   'usuario quiera. Reportar un glitch debe ser tan fácil como mandar un mensaje.</p>'
 + '</div>'
 + glance([("Tipo","Producto — núcleo propietario. Aquí está la ventaja competitiva."),
           ("Trabajo","Ser el back office completo de una empresa que no tiene gerencia."),
           ("Precio",'$1,500 implementación · Core <strong>$399</strong>/mes · Growth '
                     '<strong>$799</strong>/mes, por organización <span class="chip">[A]</span>'),
           ("Para quién","Equipos de <strong>2 personas en adelante</strong>, liderados por ventas, "
                         "sin gerencia y sin medios para contratarla."),
           ("Estado","Especificación completa. Los agentes son la tesis, no software construido "
                     '<span class="chip">[T]</span>')],
          [("$4,788","Valor anual contrato Core"),("2","Personas: el piso del cliente objetivo"),
           ("3.3 meses","Recuperación de CAC"),("0","Adjuntos faltantes permitidos")])
 + '</div>'
 + '<h2 style="margin-top:4mm"><span class="snum">01</span>La gerencia agéntica</h2>'
 + table(["Agente","Qué hace realmente"], [
     ["<strong>CFO</strong>",
      "Registra solo asientos con comprobante. Le mandas una factura y le dices qué es: la clasifica "
      "en P&amp;L y en la línea de presupuesto, aplica el tratamiento contable correcto, genera el "
      "registro y puede empujarlo al sistema contable. Controla caja, cuentas por cobrar y variación "
      "contra presupuesto. Produce reportería digna de un CFO."],
     ["<strong>COO</strong>",
      "Opera el <strong>Glitch Report</strong>. Detecta que <em>el mismo paso de un proceso siempre "
      "falla</em>, o que <em>una persona falla más seguido que el resto</em>. Sugiere cambios de "
      "proceso, de equipo o de capacitación. Produce KPIs operativos. Es consultor <strong>y</strong> "
      "gerente."],
     ["<strong>CEO</strong>",
      "La vista de empresa: qué requiere atención, qué está fuera de plan, qué decisión está pendiente "
      "y por qué — sobre la posición verificada, no la reportada."],
     ["<strong>CMO</strong>",
      "<strong>Lee el CRM</strong> y reporta si las campañas, el embudo y la ejecución comercial "
      "realmente cumplen los objetivos de la gerencia. Es la auditoría del front office."],
     ["<strong>Auditor / Consultor</strong>",
      "Rastro de auditoría continuo, cierre de período, y una empresa <strong>lista para due "
      "diligence</strong> en cualquier momento."]], None, 99)
 + simple([
     "Un CRM te ayuda a vender. <strong>BluePrint te hace la gerencia.</strong>",
     "El problema del CRM es simple: <strong>la información la mete el vendedor, y al vendedor le "
     "pagan por lo que reporta.</strong> Por eso las ventas del CRM casi nunca cuadran con lo que "
     "realmente entró al banco.",
     "BluePrint arregla eso con una regla dura: <strong>si no hay factura o recibo adjunto, no existe "
     "el registro.</strong> Así los números sí se pueden creer.",
     "Le mandas una foto de una factura por chat, le dices qué es, y él la mete donde va: P&amp;L, "
     "presupuesto, flujo de caja, contabilidad.",
     "Y con el <strong>Glitch Report</strong> anotas cada error, grande o chico. Con el tiempo el "
     "sistema te dice <strong>en qué paso siempre se traba el proceso y quién se equivoca más</strong> "
     "— y qué hacer al respecto.",
     "Es para el que vende bien pero no tiene ni quiere pagar un gerente financiero, un gerente de "
     "operaciones y un gerente de mercadeo. <strong>Desde 2 personas.</strong>"]),
 p2=masthead("BluePrint", "El Glitch Report, el modelo y por qué vale", None,
             "B_RealEstate<br>25 sept 2026", small=True)
 + '<h2><span class="snum">02</span>El Glitch Report — inspirado en Four Seasons</h2>'
 + '<p class="small">Tomado del reporte de glitches del hotel <strong>Four Seasons</strong>: '
   '<strong>cualquier falla, por pequeña que sea, se reporta y se registra.</strong> El propósito no es '
   'culpar a nadie — es tener un registro medible de la eficiencia y la eficacia de los procesos.</p>'
 + '<p class="small">Produce un dato que ningún CRM tiene: <strong>dónde se rompe la empresa de '
   'verdad.</strong> Es lo que permite al agente COO <em>recomendar</em> en vez de solo <em>mostrar</em>, '
   'y por qué <strong>el producto vale más mientras más lleva corriendo</strong>.</p>'
 + '<h3 class="mt">Los manuales: qué hace el CRM con ellos y qué hace BluePrint</h3>'
 + table(["","CRM","BluePrint"], [
     ["Papel del manual","<strong>Una guía</strong> — le dice al equipo el debido proceso",
      "<strong>Un proceso instrumentado</strong>"],
     ["Qué aprendes","Si alguien lo abrió",
      "<strong>Dónde falla, con qué frecuencia y quién</strong>"],
     ["Resultado","Cumplimiento, con suerte",
      "Glitch → diagnóstico → mejora sugerida → resultado medido"]], None, 99)
 + '<p class="note">Los dos pueden tener los mismos manuales. <strong>Solo BluePrint te dice si '
   'funcionan.</strong></p>'
 + '<h2 style="margin-top:3mm"><span class="snum">03</span>Hace que el negocio se pueda vender</h2>'
 + '<p class="small">Si el día de mañana el dueño quiere vender su negocio o su franquicia, con '
   'BluePrint entrega <strong>una operación gestionada y andando</strong>: reportería financiera al día, '
   'contabilidad limpia, procesos y manuales documentados, rastro de auditoría e historial de gestión.</p>'
 + '<div class="callout gold">Una inmobiliaria de dos personas con todo eso <strong>vale bastante más</strong> '
   'que una donde los registros viven en la cabeza del dueño y en una hoja de cálculo. BluePrint es un '
   'argumento de <strong>valor de salida</strong>, no solo de eficiencia — y es el argumento más fuerte '
   'en una venta de franquicia: el franquiciado compra un negocio que <em>va a valer algo</em> cuando lo deje.</div>'

,
 p3=masthead("BluePrint", "Modelo de Negocio", None, "B_RealEstate<br>25 sept 2026", small=True)
+ canvas(dict(
   kp=["CRM (GoHighLevel y otros) — fuente a auditar","Sistemas contables",
       "Nube y proveedores de IA","Firma electrónica"],
   ka=["Ingeniería de agentes","Diseño del Glitch Report",
       "Reglas de clasificación contable","Implementación y soporte"],
   vp=["<strong>Un CEO, CFO, COO y CMO sin nómina de gerencia</strong>",
       "Sin comprobante no hay registro: números confiables",
       "Glitch Report: dónde y quién falla",
       "<strong>Un negocio vendible</strong>, listo para due diligence"],
   cr=["Implementación de alto contacto","Onboarding estandarizado","Los agentes como relación diaria"],
   cs=["<strong>Equipos de 2+ personas liderados por ventas</strong>","Franquicias Dproperty",
       "Socios de marca propia B_ Partner","Inmobiliarias boutique sin gerencia"],
   kr=["<strong>El dataset de glitches</strong> — crece y no se copia",
       "Modelo de datos y reglas de evidencia","Biblioteca de procesos y plantillas",
       "Rastro de auditoría acumulado"],
   ch=["Venta directa del fundador","Socios de diseño","Canal de franquicia y socios",
       "Building Blocks"],
   cost=["Ingeniería y producto","Nube, API e inferencia de IA",
         "Seguridad y cumplimiento","Implementación y soporte"],
   rev=["Implementación — $1,500, más si la migración es compleja",
        "Core — $399/mes por organización",
        "Growth — $799/mes por organización",
        "Consumo de IA y almacenamiento sobre el límite incluido",
        "Nivel Scale — cotizado, sin definir"]))
 + '<p class="note"><strong>Estado honesto:</strong> la gerencia agéntica es la <strong>tesis del '
   'producto, no software construido</strong> <span class="chip">[T]</span>. El riesgo de adopción es el '
   'Glitch Report: a nadie le gusta registrar sus propios errores, y es el dato del que depende todo.</p>',
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
 + '<h3 class="mt">Su límite, dicho con honestidad</h3>'
 + '<p class="small">El CRM es excelente para vender, y <strong>depende de que el equipo lo use bien</strong>. '
   'Lo que reporta refleja lo que el vendedor escribió, no necesariamente lo que ocurrió. Esa es '
   'precisamente la razón por la que existe BluePrint — y por la que los dos se venden juntos.</p>'
 + '<h3 class="mt">Qué controla</h3>'
 + '<p class="small">Gestión de prospectos y contactos · flujos de WhatsApp, correo y SMS · '
   'formularios, páginas de aterrizaje y calendarios · seguimiento y maduración · embudo comercial '
   '<strong>previo a la calificación</strong> y actividad de vendedores · atribución de campañas · '
   'automatizaciones del equipo comercial.</p>'
 + '<h3 class="mt">Qué NO controla</h3>'
 + '<p class="small soft">La verdad financiera verificada y la gerencia (BluePrint) · presupuestos y '
   'control financiero · aseguramiento de procesos y Glitch Report · contabilidad · listados del '
   'marketplace (VAULTED) · auditoría de largo plazo.</p>'
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
     "El otro riesgo es que <strong>todo depende de GoHighLevel</strong>. Lo aceptamos a cambio de no "
     "gastar nuestro dinero construyendo un CRM."]),
 p2=masthead("BlankCRM", "Modelo de Negocio", None, "B_RealEstate<br>25 sept 2026", small=True)
 + canvas(dict(
   kp=["<strong>GoHighLevel</strong> — el motor completo","Proveedores de mensajería y voz",
       "Meta / WhatsApp Business API","Proveedores de IA"],
   ka=["Configuración vertical inmobiliaria","Construcción de embudos y automatizaciones",
       "Onboarding de clientes","Soporte","Integración con BluePrint"],
   vp=["Front-office listo para inmobiliaria, no genérico",
       "Configurado en días, no semanas de auto-armado",
       "<strong>BluePrint lo audita</strong> y detecta lo que no cuadra",
       "Una sola relación de soporte para CRM y back office",
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
      "Todo el producto es GoHighLevel. Un cambio de precio o condiciones afecta a todos los clientes a la vez."],
     ["Soporte sobre 1.5 h/cliente/mes","<strong>Alta</strong>","El principal destructor de margen."],
     ["Onboarding sobre 15 horas","Media","Convierte la cuota de configuración en pérdida."],
     ["El cliente descubre que puede comprar GHL directo","Media",
      "Se mitiga con la configuración vertical, la integración con BluePrint y el soporte — <strong>nunca</strong> ocultando el motor."]], None, 1)
 + simple("En una frase: <strong>es nuestro producto de entrada, y es rentable casi desde el primer "
   "cliente.</strong> Le facilita la venta al equipo comercial. Lo que no puede hacer es garantizar que "
   "lo que el equipo escribió sea cierto — para eso está BluePrint. Por eso se venden juntos."),
)
