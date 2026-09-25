# -*- coding: utf-8 -*-
"""Dos páginas: cómo interactúa el ecosistema y cómo cada bloque crea valor para los demás."""

from brand import masthead, simple, table, canvas

ECO = [

# ═══════════════════════════════ PÁGINA 1
masthead("Ecosistema", "Cómo encaja todo",
  "Ocho ofertas, un solo negocio. Cada bloque hace algo que hace más valioso al siguiente — y esa "
  "es la diferencia entre un portafolio y una empresa.",
  "B_RealEstate<br>24 sept 2026<br>v1.0")
+ '<h3>La frase que ordena todo</h3>'
+ '<div class="callout gold" style="margin-top:1mm"><strong>BlankCRM es dueño de la demanda hasta la '
  'calificación. BluePrint es dueño de todo lo que pasa después. VAULTED es dueño de la oferta y el '
  'acceso de red. Building Blocks es dueño de la capacidad. La contabilidad sigue siendo el libro '
  'mayor.</strong></div>'

+ '<h2 style="margin-top:4mm"><span class="snum">01</span>El flujo</h2>'
+ '<pre style="font-family:\'JetBrains Mono\',monospace;font-size:7.2pt;line-height:1.55;'
  'background:var(--bone-deep);padding:4mm;border-left:2.6pt solid var(--champagne);'
  'white-space:pre;overflow:hidden">'
+ """  Dproperty (inversionista)        DpropertyLiving (usuario final)
            │                                  │
            └──────────────┬───────────────────┘
                           ▼
                   ┌───────────────┐
                   │   BlankCRM    │   prospectos · contenido · seguimiento
                   │ (GoHighLevel) │   dos sub-cuentas, un solo motor
                   └───────┬───────┘
                           │  ◄── OPORTUNIDAD CALIFICADA ──►  el único traspaso
                           ▼
   Contabilidad ─────► ┌───────────┐ ◄───── Building Blocks
   Banco · Firma       │ BluePrint │        certificación habilita permisos
   Drive               │           │
                       │ expediente · cumplimiento · aprobaciones
                       │ cierre · COMISIÓN · auditoría
                       └─────┬─────┘
                             │  resultados verificados
                             ▼
                       ┌───────────┐
                       │  VAULTED  │ ◄──── Dproperty Select (oferta curada)
                       │  red      │ ◄──── Desarrolladores (oferta de proyecto)
                       └───────────┘

   CANALES que despliegan el stack completo:
   Franquicia Dproperty · B_ Partner · Alianzas con Desarrolladores"""
+ '</pre>'

+ '<h2 style="margin-top:4mm"><span class="snum">02</span>Quién es dueño de qué dato</h2>'
+ table(["Dominio","Dueño","Nota"], [
    ["Prospectos, contactos, conversaciones, campañas","<strong>BlankCRM</strong>","Impulsado por GoHighLevel"],
    ["Embudo previo a la calificación","<strong>BlankCRM</strong>","Reportado, no verificado"],
    ["Desde la oportunidad calificada: expediente, cumplimiento, aprobaciones, cierre, comisión",
     "<strong>BluePrint</strong>","Sistema de registro"],
    ["Presupuestos, variaciones, indicadores, cierre de período, auditoría","<strong>BluePrint</strong>","Sistema de registro"],
    ["Inventario de propiedades, listados, MLS","Sistema del desarrollador / portal / VAULTED",
     "<strong>Nunca BluePrint</strong>"],
    ["Listados de red, coincidencias, atribución, GMV","<strong>VAULTED</strong>","Sistema separado"],
    ["Contenido, evaluaciones, certificación","<strong>Building Blocks</strong>","Open edX"],
    ["Libro mayor, impuestos, nómina","Plataforma contable","BluePrint solo lee"],
    ["Fideicomiso, custodia, movimiento de dinero","Banco / fiduciario","BluePrint solo lee evidencia"]], None, 99)
+ '<p class="note"><strong>Una sola autoridad por clase de dato.</strong> Nunca decimos «una sola base '
  'de datos» — es un ecosistema conectado con fuentes de verdad definidas. Jerarquía de confianza: '
  '<strong>reportado → verificado operativamente → verificado financieramente → cerrado</strong>.</p>'

+ simple([
  "Piénsalo como una <strong>fábrica con estaciones</strong>. Cada estación hace una cosa y le pasa "
  "el trabajo a la siguiente.",
  "<strong>BlankCRM</strong> consigue y persigue clientes. Cuando un cliente ya es serio, se lo pasa "
  "a <strong>BluePrint</strong>. Ese traspaso es el único punto de conexión que importa.",
  "<strong>BluePrint</strong> se encarga de que el negocio se cierre bien: papeles, aprobaciones, "
  "comisión exacta, y deja todo auditado.",
  "<strong>Building Blocks</strong> entrena a la gente. <strong>VAULTED</strong> conecta con la red "
  "para conseguir más producto y más compradores.",
  "Los <strong>canales</strong> (franquicia, socio de marca propia, desarrolladores) son las tres "
  "formas de vender todo el paquete junto.",
  "<strong>Lo importante:</strong> ninguna estación es dueña del trabajo de otra. Por eso nada se "
  "duplica y nadie se pisa."]),

# ═══════════════════════════════ PÁGINA 2
masthead("Ecosistema", "Cómo cada bloque crea valor para los demás", None,
         "B_RealEstate<br>24 sept 2026", small=True)

+ '<h2><span class="snum">03</span>Matriz de intercambio de valor</h2>'
+ '<p class="small soft" style="margin-bottom:2mm">Lee cada fila así: «este bloque <strong>le da</strong> '
  'esto a los demás». Donde una fila está vacía, el bloque todavía no aporta — y eso también es información.</p>'
+ table(["Bloque","Qué le da al resto del ecosistema"], [
    ["<strong>BluePrint</strong>",
     "Da a <strong>BlankCRM</strong> la razón para subir de precio (el CRM solo no cierra negocios). "
     "Da a <strong>Building Blocks</strong> su motor de demanda: detecta la falla de proceso y dice a "
     "quién hay que entrenar. Da a <strong>VAULTED</strong> transacciones verificadas y atribución "
     "confiable. Da a los <strong>canales</strong> la consistencia operativa que hace posible "
     "franquiciar. Da a <strong>Select</strong> resultados financieros verificados."],
    ["<strong>BlankCRM</strong>",
     "Da a <strong>BluePrint</strong> oportunidades ya calificadas — sin esto BluePrint no tiene "
     "materia prima. Da a <strong>VAULTED</strong> señales de demanda autorizada (qué busca cada "
     "comprador). Da a los <strong>canales</strong> un producto de entrada barato que abre la puerta. "
     "Da a <strong>Dproperty y DpropertyLiving</strong> la maquinaria de contenido y seguimiento."],
    ["<strong>VAULTED</strong>",
     "Da a <strong>BluePrint</strong> más transacciones que procesar. Da a los <strong>canales</strong> "
     "un beneficio que ningún competidor local ofrece (acceso a red). Da a <strong>Select</strong> un "
     "canal de distribución. Da a <strong>desarrolladores</strong> compradores. "
     "<strong>Hoy da poco: está bloqueado a propósito.</strong>"],
    ["<strong>Building Blocks</strong>",
     "Da a <strong>BluePrint</strong> usuarios que saben usarlo — la causa número uno de fracaso en "
     "software B2B es que nadie aprendió. Da a la <strong>franquicia</strong> consistencia entre "
     "oficinas, que es el problema central de franquiciar. Da a <strong>B_ Partner</strong> velocidad "
     "de arranque. Da a <strong>desarrolladores</strong> corredores certificados por proyecto."],
    ["<strong>Franquicia Dproperty</strong>",
     "Da a <strong>BluePrint</strong> los casos reales que prueban que el producto funciona — y los "
     "primeros ingresos. Da a <strong>VAULTED</strong> participantes y oferta. Da a <strong>Select</strong> "
     "una fuerza de distribución. Da a la <strong>empresa</strong> credibilidad: operamos lo que vendemos."],
    ["<strong>B_ Partner</strong>",
     "Da a <strong>BluePrint</strong> clientes que <em>no</em> son Dproperty — la prueba de que la "
     "plataforma es neutral y no un truco para franquiciar. Da a <strong>VAULTED</strong> oferta y "
     "demanda independientes. Da ingreso recurrente sin costo de marca."],
    ["<strong>Alianzas con Desarrolladores</strong>",
     "Da a <strong>VAULTED</strong> la oferta inicial — resuelve el arranque en frío del marketplace. "
     "Da a <strong>Select</strong> oportunidades candidatas. Da a <strong>BluePrint</strong> aprendizaje "
     "de organizaciones de venta complejas. Da a <strong>Building Blocks</strong> un comprador de "
     "cohortes empresariales."],
    ["<strong>Dproperty Select</strong>",
     "Da a la <strong>franquicia</strong> la razón para elegirnos sobre cualquier otra marca. Da a "
     "<strong>VAULTED</strong> su primera oferta de calidad. Da a <strong>B_ Partner</strong> un "
     "producto diferenciado que su competencia no tiene. Da a la <strong>empresa</strong> la prueba "
     "de que entendemos inmobiliaria, no solo software."]], None, 99)

+ '<h2 style="margin-top:4mm"><span class="snum">04</span>Los tres circuitos que se refuerzan</h2>'
+ '<div class="cols3">'
+ '<div class="panel"><h3>1 · Circuito de calidad</h3><p class="small">BluePrint detecta una falla de '
  'proceso → Building Blocks entrena → BluePrint habilita el permiso → la operación mejora → hay más '
  'datos de proceso. <strong>Cada vuelta hace al software más útil y a la formación más pertinente.</strong></p></div>'
+ '<div class="panel"><h3>2 · Circuito de red</h3><p class="small">Más oficinas y socios → más oferta y '
  'demanda en VAULTED → más transacciones atribuibles → la red vale más → ser franquicia o socio vale '
  'más. <strong>Es el único circuito con potencial de efecto de red real.</strong></p></div>'
+ '<div class="panel"><h3>3 · Circuito de prueba</h3><p class="small">Dproperty opera con el stack → '
  'genera casos y métricas reales → el software se vuelve vendible a terceros → más clientes → más '
  'aprendizaje de producto. <strong>Es la ventaja que la mayoría de startups de software no tiene.</strong></p></div>'
+ '</div>'

+ '<h2 style="margin-top:4mm"><span class="snum">05</span>Dónde está el valor de la empresa — sin adornos</h2>'
+ table(["Capa","Rol estratégico","Dónde está el valor"], [
    ["<strong>BluePrint</strong>","Núcleo propietario","<strong>Aquí</strong> — es lo único que puede ser una compañía de software valiosa por sí sola"],
    ["<strong>VAULTED</strong>","Opción de red","<strong>Potencial alto, evidencia cero</strong> — la apuesta grande"],
    ["BlankCRM","Producto de enganche","Asignación eficiente de capital, no ventaja competitiva"],
    ["Building Blocks","Formación y retención","Consistencia y enganche, no foso defensivo"],
    ["Canales","Distribución","Ventaja de salida al mercado, no tecnología"],
    ["Dproperty Select","Activo estratégico","<strong>No se puede copiar</strong> — relaciones, no software"]], None, 99)
+ '<div class="callout"><strong>Regla de presentación:</strong> nunca presentar todos los bloques como '
  'negocios iguales. La jerarquía es <strong>BluePrint como núcleo → VAULTED como potencial de red → '
  'BlankCRM como enganche → Building Blocks y canales como soporte.</strong></div>'

+ simple([
  "La pregunta real es: <strong>¿por qué esto es una empresa y no cuatro productos sueltos?</strong> "
  "Porque cada pieza hace más valiosa a la siguiente.",
  "Ejemplo concreto: <strong>BluePrint detecta que una oficina pierde documentos. Building Blocks "
  "entrena a esa persona. BluePrint verifica que se certificó y le devuelve el permiso.</strong> "
  "Ningún competidor de formación tiene la alarma, y ningún competidor de software tiene el curso.",
  "Otro ejemplo: <strong>los desarrolladores nos dan inventario. Ese inventario llena VAULTED. "
  "VAULTED hace que ser franquicia valga más. Más franquicias traen más inventario.</strong>",
  "Y el más importante: <strong>Dproperty usa el software todos los días.</strong> Eso nos da pruebas "
  "reales que casi ninguna startup de software tiene cuando sale a vender.",
  "Siendo honestos: <strong>hoy el valor está en BluePrint.</strong> VAULTED es la apuesta grande pero "
  "aún no existe. Los canales venden, no son la tecnología. Y Select es lo único que un competidor "
  "definitivamente no puede copiar."]),
]
