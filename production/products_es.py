# -*- coding: utf-8 -*-
"""Contenido en español — ofertas 1 y 2."""

from brand import masthead, simple, table, glance, canvas

M = "B_RealEstate<br>29 sept 2026<br>v3.0"

P = {}

# ══════════════════════════════════════════════════════════ 1 · BLUEPRINT
P["01_BluePrint"] = dict(
 file="BluePrint",
 p1=masthead("Producto — Núcleo propietario", "BluePrint",
   "Un back office agéntico: una gerencia profesional completa — CEO, CFO, COO y CMO — al alcance de "
   "una empresa que no necesita ni puede sostener esa estructura.", M)
 + '<div class="cols"><div>'
 + '<h3>Dónde está realmente el problema</h3>'
 + '<p>El problema del CRM no es el CRM. Son las personas que lo alimentan: en su mayoría '
   '<strong>agentes inmobiliarios cuyo valor principal está en el contacto con el cliente</strong>, '
   'no detrás de un computador haciendo trabajo administrativo. Si el CRM no se alimenta con rigor, '
   'su información pierde valor y veracidad.</p>'
 + '<p>Y aquí está el punto importante: <strong>culpar al equipo comercial por preferir hacer aquello '
   'en lo que es excelente</strong>, en lugar de llenar formularios, es contraproducente. Es un error '
   'gerencial — es no maximizar el potencial humano de la empresa.</p>'
 + '<div class="callout gold">BluePrint busca ser precisamente <strong>ese vínculo que optimiza todo el '
   'ecosistema empresarial</strong>: el comercial sigue vendiendo, y la administración alcanza un '
   'estándar profesional sin pedirle al vendedor que se convierta en administrador.</div>'
 + '<h3 class="mt">La separación que lo hace posible</h3>'
 + '<p class="small">El equipo comercial puede seguir usando el CRM y ajustarlo a su medida — nuestro '
   'equipo facilita esa implementación. <strong>BluePrint opera de forma independiente</strong> para '
   'llevar el manejo interno: una gerencia de alto nivel, auditoría de procesos, manejo financiero y '
   'reportería — mientras acompaña el uso del CRM.</p>'
 + '<p class="small">En un mundo ideal ambas plataformas funcionan de forma óptima. Pero <strong>al '
   'separar la parte administrativa de la parte comercial</strong>, la empresa es seria desde el día '
   'cero y deja de ser vulnerable a depender de una sola fuente de verdad.</p>'
 + '<h3 class="mt">La meta</h3>'
 + '<p><strong>Potenciar la capacidad humana de cada agente de la compañía, usando inteligencia '
   'artificial para hacerlo posible.</strong></p>'
 + '<h3 class="mt">La interfaz</h3>'
 + '<p class="small">Todo ocurre por detrás. <strong>Al frente solo hay una conversación.</strong> '
   'Debajo están los manuales, los procesos, la biblioteca de conocimiento de la empresa, las '
   'plantillas, los contactos y los registros. El producto es ultracompleto; la experiencia es tan '
   'simple o tan profunda como cada persona quiera.</p>'
 + '</div>'
 + glance([("Tipo","Producto — núcleo propietario. Aquí está la ventaja competitiva."),
           ("Trabajo","Ser el back office completo de una empresa sin estructura gerencial."),
           ("Modelo","Suscripción por organización, no por vendedor. Implementación acompañada."),
           ("Para quién","Equipos <strong>desde dos personas</strong>, liderados por su fuerza comercial."),
           ("Principio","Todo registro nace de un documento que lo respalda.")],
          [("5","Roles de gerencia incluidos"),("2","Personas: desde donde tiene sentido"),
           ("1","Conversación: toda la interfaz"),("0","Registros sin respaldo")])
 + '</div>'
 + '<h2 style="margin-top:4mm"><span class="snum">01</span>La gerencia agéntica</h2>'
 + table(["Rol","Qué aporta"], [
     ["<strong>CFO</strong>",
      "Cada registro nace de un documento que lo respalda. Le compartes una factura y le dices qué es: "
      "la clasifica en el estado de resultados y en la línea de presupuesto que corresponde, aplica el "
      "tratamiento contable adecuado, genera el registro y puede integrarlo al sistema contable. "
      "Acompaña el flujo de caja, la cobranza y el cumplimiento del presupuesto."],
     ["<strong>COO</strong>",
      "Opera el <strong>Glitch Report</strong>. Identifica <em>en qué paso un proceso necesita "
      "rediseño</em> y <em>dónde una persona necesita apoyo o formación</em>. Propone mejoras de "
      "proceso, de organización y de capacitación. Construye los indicadores operativos."],
     ["<strong>CEO</strong>",
      "La vista de empresa: qué requiere atención, qué se está desviando del plan y qué decisión está "
      "pendiente — sobre información respaldada, no sobre percepciones."],
     ["<strong>CMO</strong>",
      "Acompaña el uso del CRM y reporta si las campañas, el embudo y la actividad comercial están "
      "alineados con los objetivos de la empresa. Es la mirada que conecta lo comercial con lo gerencial."],
     ["<strong>Auditor / Consultor</strong>",
      "Trazabilidad continua, cierre de período y una empresa <strong>lista para una revisión "
      "externa</strong> en cualquier momento."]], None, 99)
 + simple([
     "Un CRM ayuda a vender. <strong>BluePrint hace la gerencia.</strong>",
     "El punto de partida es simple y humano: <strong>un buen agente inmobiliario es bueno con las "
     "personas, no llenando formularios.</strong> Pedirle que sea administrador desperdicia su mejor "
     "cualidad — y deja la información de la empresa incompleta.",
     "BluePrint resuelve eso por otro camino: <strong>cada registro nace de un documento que lo "
     "respalda</strong>. Así la información de la empresa se sostiene sola.",
     "Le compartes una factura por chat, le dices qué es, y queda donde debe quedar: resultados, "
     "presupuesto, flujo de caja, contabilidad.",
     "Con el <strong>Glitch Report</strong> se registra cada tropiezo, grande o pequeño. Con el tiempo "
     "el sistema muestra <strong>en qué paso el proceso necesita ayuda y dónde el equipo necesita "
     "formación</strong> — y qué hacer al respecto.",
     "<strong>La meta de fondo:</strong> que cada persona dedique su tiempo a lo que mejor sabe hacer, "
     "y que la tecnología se encargue del resto."]),
 p2=masthead("BluePrint", "El Glitch Report y por qué el valor crece con el tiempo", None,
             "B_RealEstate<br>29 sept 2026", small=True)
 + '<h2><span class="snum">02</span>El Glitch Report — inspirado en Four Seasons</h2>'
 + '<p class="small">Tomado del reporte de glitches del hotel <strong>Four Seasons</strong>: '
   '<strong>cualquier tropiezo, por pequeño que sea, se registra.</strong> El propósito no es señalar a '
   'nadie — es tener una medida real de la eficiencia y la eficacia de los procesos, para poder '
   'mejorarlos con evidencia en lugar de con intuición.</p>'
 + '<p class="small">Produce algo que ningún CRM tiene: <strong>el mapa de dónde la operación necesita '
   'ayuda.</strong> Es lo que permite al rol de COO <em>recomendar</em> en vez de solo <em>mostrar</em>, '
   'y la razón por la que <strong>el producto vale más mientras más tiempo lleva acompañando a la '
   'empresa</strong>. Es un software que crece con la compañía.</p>'
 + '<h3 class="mt">Los manuales: qué hace el CRM con ellos y qué hace BluePrint</h3>'
 + table(["","CRM","BluePrint"], [
     ["Papel del manual","<strong>Una guía</strong> — indica al equipo el debido proceso",
      "<strong>Un proceso instrumentado</strong>"],
     ["Qué se aprende","Que el proceso está documentado",
      "<strong>Dónde se traba, con qué frecuencia y qué lo causa</strong>"],
     ["Resultado","El equipo sabe qué debe hacer",
      "Tropiezo → diagnóstico → mejora propuesta → resultado medido"]], None, 99)
 + '<p class="note">Ambas plataformas pueden tener los mismos manuales. <strong>BluePrint además indica '
   'si están funcionando.</strong></p>'
 + '<h2 style="margin-top:3mm"><span class="snum">03</span>Construye una empresa transferible</h2>'
 + '<p class="small">Si algún día el dueño quiere crecer, incorporar un socio o vender su operación, '
   'con BluePrint entrega <strong>una empresa en marcha y ordenada</strong>: reportería financiera al '
   'día, contabilidad consistente, procesos y manuales documentados, trazabilidad e historial de '
   'gestión.</p>'
 + '<div class="callout gold">Una operación pequeña con todo eso en orden <strong>vale bastante más</strong> '
   'que una donde el conocimiento vive en la cabeza de una sola persona. BluePrint construye '
   '<strong>valor patrimonial</strong>, no solo eficiencia del día a día — y es el argumento más sólido '
   'en una conversación de franquicia: se adquiere un negocio que <em>va a valer algo</em> el día que se deje.</div>'
 + '<h2 style="margin-top:3mm"><span class="snum">04</span>Qué acompaña y qué deja en manos de otros</h2>'
 + '<div class="cols2">'
 + '<div><h3>Acompaña</h3><p class="small">La información financiera respaldada y su clasificación · '
   'la inteligencia de procesos y el Glitch Report · las decisiones, aprobaciones e indicadores de '
   'gestión · el cierre de período y la trazabilidad de largo plazo · la biblioteca de conocimiento de '
   'la empresa: manuales, políticas, plantillas y contactos · y <strong>la mirada sobre el uso del '
   'CRM</strong>.</p></div>'
 + '<div><h3>Deja en manos de otros</h3><p class="small soft">La captación y el seguimiento comercial '
   'hasta postventa, incluida gestión legal, contratos, pagos, cierre y comisiones — eso es del CRM · el inventario de propiedades y proyectos · el libro '
   'contable oficial, los impuestos y la nómina — eso es del contador · la administración de '
   'propiedades · la entrega de cursos, que corresponde a Building Blocks · el marketplace, que '
   'corresponde a VAULTED · y el movimiento de fondos, que corresponde a la banca.</p>'
 + '<p class="small"><strong>Funciona con cualquier CRM</strong> — GoHighLevel, HubSpot, Salesforce o '
   'carga manual.</p></div>'
 + '</div>',
 p3=masthead("BluePrint", "Modelo de Negocio", None, "B_RealEstate<br>29 sept 2026", small=True)
 + canvas(dict(
   kp=["CRM del cliente — la fuente que se acompaña","Sistemas contables",
       "Nube y proveedores de inteligencia artificial","Firma electrónica"],
   ka=["Ingeniería de los roles agénticos","Diseño del Glitch Report",
       "Reglas de clasificación contable","Implementación y acompañamiento"],
   vp=["<strong>Una gerencia profesional sin la estructura de una gerencia</strong>",
       "Información que se sostiene sola: todo registro tiene respaldo",
       "El Glitch Report muestra dónde ayudar",
       "<strong>Una empresa transferible</strong> y lista para revisión externa",
       "Una conversación al frente, toda la complejidad por detrás"],
   cr=["Implementación acompañada","Incorporación estandarizada",
       "Los roles agénticos como relación cotidiana"],
   cs=["<strong>Equipos desde dos personas, liderados por ventas</strong>",
       "Franquicias Dproperty","Socios de marca propia B_ Partner",
       "Inmobiliarias boutique sin estructura gerencial"],
   kr=["<strong>El histórico de procesos y tropiezos</strong> — crece y no se copia",
       "Modelo de datos y reglas de respaldo","Biblioteca de procesos y plantillas",
       "Trazabilidad acumulada"],
   ch=["Relación directa","Socios de diseño","Canal de franquicia y socios","Building Blocks"],
   cost=["Ingeniería y producto","Nube e inteligencia artificial",
         "Seguridad y cumplimiento","Implementación y acompañamiento"],
   rev=["Implementación inicial acompañada",
        "Suscripción recurrente por organización — niveles según complejidad operativa",
        "Nivel superior para operaciones multi-oficina, a la medida",
        "Consumo de inteligencia artificial y almacenamiento por encima de lo incluido",
        "Integraciones específicas, a la medida"]))
 + '<p class="note"><strong>Estado honesto:</strong> los roles agénticos son la <strong>tesis del '
   'producto y están en desarrollo</strong>. Lo que existe hoy es la especificación y el diseño. '
   'El principal reto de adopción es el Glitch Report: requiere una cultura donde registrar un '
   'tropiezo se vea como mejora y no como falta — y es justamente la información de la que depende '
   'todo lo demás.</p>',
)

# ══════════════════════════════════════════════════════════ 2 · BLANKCRM
P["02_BlankCRM"] = dict(
 file="BlankCRM",
 p1=masthead("Producto — Front office comercial", "BlankCRM",
   "El front office inmobiliario configurado, impulsado por GoHighLevel: que el equipo comercial "
   "dedique su tiempo a vender y no a administrar.", M)
 + '<div class="cols"><div>'
 + '<h3>La idea</h3>'
 + '<p>BlankCRM es el front office de B_ configurado para el sector inmobiliario, '
   '<strong>impulsado por GoHighLevel</strong>. Se ofrece como un ambiente práctico de trabajo '
   'comercial, no como tecnología propietaria de CRM.</p>'
 + '<p>Somos transparentes sobre el motor. B_ prefiere no invertir capital de ingeniería en '
   'reconstruir una infraestructura de CRM que ya existe y funciona bien — ese esfuerzo se concentra '
   'en BluePrint y VAULTED, donde sí construimos algo propio.</p>'
 + '<h3 class="mt">Para qué sirve de verdad</h3>'
 + '<p class="small">Un buen CRM le quita fricción al vendedor: responde al prospecto en minutos, '
   'ordena el seguimiento, recuerda la próxima conversación, publica el contenido y deja registro de '
   'la actividad. <strong>Bien configurado, el equipo comercial vende más y pierde menos '
   'oportunidades.</strong> Incluye gestión legal, aprobaciones, contratos, hitos de pago, cierre, comisiones y postventa.</p>'
 + '<h3 class="mt">Su límite natural, dicho con honestidad</h3>'
 + '<p class="small">Lo que el CRM muestra refleja lo que el equipo alcanzó a registrar. No porque el '
   'equipo falle, sino porque <strong>su mejor tiempo está con el cliente</strong>, no llenando campos. '
   'Por eso existe BluePrint: para que la información de la empresa no dependa de eso. Los dos '
   'productos se complementan, y cada uno hace lo que mejor hace.</p>'
 + '<h3 class="mt">Qué acompaña</h3>'
 + '<p class="small">Prospectos y contactos · conversaciones por WhatsApp, correo y SMS · formularios, '
   'páginas y calendarios · seguimiento y maduración · el embudo comercial y la actividad del equipo · '
   'atribución · gestión legal · aprobaciones · contratos · hitos de pago · cierre · comisiones · postventa · automatización y tableros comerciales.</p>'
 + '</div>'
 + glance([("Tipo","Front office comercial. Deliberadamente <em>no</em> es tecnología propia."),
           ("Trabajo","Que el equipo venda más y pierda menos oportunidades."),
           ("Modelo","Configuración inicial y suscripción por oficina. El consumo de mensajería se "
                     "traslada de forma transparente."),
           ("Motor","GoHighLevel, declarado abiertamente."),
           ("Complemento","BluePrint es opcional: observa, verifica y recomienda; BlankCRM funciona solo.")],
          [("Días","Listo para operar, no semanas"),("1","Relación de soporte para todo el stack"),
           ("Fijo","El costo de plataforma no crece por cliente"),("+","Se integra con BluePrint")])
 + '</div>'
 + '<h2 style="margin-top:4mm"><span class="snum">01</span>Por qué el modelo funciona</h2>'
 + table(["Característica del modelo","Qué significa para el negocio"], [
     ["<strong>Costo de plataforma fijo</strong>",
      "La licencia de la plataforma es una sola, independientemente de cuántos clientes atendamos. "
      "Cada cliente adicional no agrega costo de plataforma."],
     ["<strong>Sub-cuentas sin límite</strong>",
      "Podemos abrir una cuenta por marca, por oficina o por franquicia sin penalización de costo."],
     ["<strong>Consumo trasladable con margen</strong>",
      "La mensajería, la voz y la inteligencia artificial se facturan al cliente de forma transparente, "
      "en lugar de absorberse como costo."],
     ["<strong>El margen depende del acompañamiento</strong>",
      "El verdadero costo no es la plataforma: es el tiempo de implementación y soporte. Medirlo desde "
      "el primer cliente es la disciplina que sostiene el modelo."]], None, 99)
 + simple([
     "El CRM es la herramienta del equipo comercial. <strong>Su trabajo es que vendan más y con menos "
     "esfuerzo administrativo.</strong>",
     "No construimos el motor: usamos <strong>GoHighLevel</strong> y lo decimos abiertamente. Lo que "
     "aportamos es la configuración inmobiliaria, la integración con BluePrint y el acompañamiento.",
     "El modelo funciona porque <strong>la plataforma se paga una sola vez y sirve para todos los "
     "clientes</strong>. Crecer no encarece la operación.",
     "Lo que sí cuidamos es el <strong>tiempo de soporte</strong>: ahí está el verdadero costo, y ahí "
     "está la disciplina que hace sano el negocio.",
     "Y lo importante: <strong>el CRM y BluePrint no compiten</strong>. Uno ayuda a vender, el otro "
     "ordena la empresa. Juntos, el vendedor vende y la administración funciona sola."]),
 p2=masthead("BlankCRM", "Modelo de Negocio", None, "B_RealEstate<br>29 sept 2026", small=True)
 + canvas(dict(
   kp=["<strong>GoHighLevel</strong> — el motor","Proveedores de mensajería y voz",
       "Meta / WhatsApp Business","Proveedores de inteligencia artificial"],
   ka=["Configuración vertical inmobiliaria","Construcción de embudos y automatizaciones",
       "Incorporación del cliente","Acompañamiento","Integración con BluePrint"],
   vp=["Front office listo para inmobiliaria, no genérico",
       "Operativo en días, sin semanas de auto-configuración",
       "Respuesta al prospecto en minutos y seguimiento que no se olvida",
       "<strong>BluePrint acompaña su uso</strong> y cierra el círculo con la gerencia",
       "Una sola relación de soporte para todo el stack"],
   cr=["Configuración hecha por nosotros","Soporte compartido con BluePrint",
       "Autoservicio dentro del producto"],
   cs=["Inmobiliarias que necesitan ordenar su fuerza comercial",
       "Clientes de BluePrint que suman el front office",
       "Franquicias y socios B_ Partner","Equipos de venta de desarrolladores"],
   kr=["Plantillas de configuración vertical","Cuenta de agencia con sub-cuentas sin límite",
       "Biblioteca de automatizaciones","Conector con BluePrint"],
   ch=["Complemento de BluePrint","Puerta de entrada al ecosistema",
       "Incluido en paquetes de franquicia y socios"],
   cost=["Licencia de plataforma — fija, no por cliente","Implementación inicial",
         "Acompañamiento y soporte","Consumo de mensajería, trasladado"],
   rev=["Configuración inicial por oficina",
        "Suscripción recurrente por oficina",
        "Traslado de mensajería, voz e inteligencia artificial con margen",
        "Complementos de automatización avanzada",
        "Migraciones complejas y oficinas adicionales, a la medida"]))
 + '<h2 style="margin-top:5mm"><span class="snum">02</span>Lo que hay que cuidar</h2>'
 + table(["Tema","Por qué importa","Cómo se maneja"], [
     ["<strong>Dependencia del proveedor</strong>",
      "Todo el producto corre sobre GoHighLevel. Un cambio de condiciones nos afecta de forma amplia.",
      "Se acepta a cambio de no invertir capital propio en infraestructura de CRM. Se revisa cada año."],
     ["<strong>Tiempo de acompañamiento</strong>",
      "Es el costo real del producto y el que define su salud.",
      "Se mide por cliente desde el primer día y se estandariza la implementación."],
     ["<strong>Transparencia del motor</strong>",
      "El cliente puede descubrir que la plataforma existe por separado.",
      "Se declara siempre. El valor está en la configuración inmobiliaria, la integración con BluePrint "
      "y el acompañamiento — <strong>nunca</strong> en ocultar el motor."]], None, 99)
 + simple("En una frase: <strong>es la herramienta que le facilita la vida al equipo comercial.</strong> "
   "Hace bien una cosa: ayudar a vender. Lo que no puede hacer es garantizar que toda la información de "
   "la empresa quede completa — porque eso exigiría convertir a los vendedores en administradores. "
   "Para eso está BluePrint. Por eso los dos se ofrecen juntos."),
)
