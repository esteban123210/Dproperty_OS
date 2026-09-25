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
+ '<div class="callout gold" style="margin-top:1mm"><strong>BlankCRM ayuda al equipo a vender y '
  'depende de su disciplina. BluePrint opera el back office y depende únicamente de la evidencia.</strong> '
  'VAULTED es dueño de la oferta y el acceso de red. Building Blocks es dueño de la capacidad. La '
  'contabilidad sigue siendo el libro mayor.</div>'
+ '<p class="note">Y algo más: <strong>BluePrint lee el CRM</strong> para auditar si la ejecución '
  'comercial cumple los objetivos de la gerencia. No es solo el siguiente paso del flujo — también es '
  'el control sobre el paso anterior.</p>'

+ '<h2 style="margin-top:4mm"><span class="snum">01</span>El flujo</h2>'
+ '<pre style="font-family:\'JetBrains Mono\',monospace;font-size:6.2pt;line-height:1.26;'
  'background:var(--bone-deep);padding:3mm;border-left:2.6pt solid var(--champagne);'
  'white-space:pre;overflow:hidden">'
+ """  Dproperty (inversionista)        DpropertyLiving (usuario final)
            └──────────────┬──────────────┘
                           ▼
            ┌──────────────────────────────┐
            │  BlankCRM  (GoHighLevel)     │  dos sub-cuentas, un motor
            └──────────────┬───────────────┘
                     │     ▲ BluePrint AUDITA el CRM
   Contabilidad ──► ┌┴─────┴──────┐ ◄── Building Blocks (certifica permisos)
   Banco · Firma    │  BluePrint  │  CEO · CFO · COO · CMO agénticos
                    │  sin comprobante NO hay registro
                    │  Glitch Report · P&L · auditoría
                    └──────┬──────┘
                           ▼
                    ┌─────────────┐ ◄── Dproperty Select (oferta curada)
                    │   VAULTED   │ ◄── Desarrolladores (oferta de proyecto)
                    └─────────────┘

  CANALES: Franquicia Dproperty · B_ Partner · Alianzas con Desarrolladores"""
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
    ["Libro mayor · fideicomiso · custodia","Contabilidad / banco","BluePrint solo lee evidencia"]], None, 99)
+ '<p class="note"><strong>Una sola autoridad por clase de dato.</strong> Nunca decimos «una sola base '
  'de datos» — es un ecosistema conectado con fuentes de verdad definidas. Jerarquía de confianza: '
  '<strong>reportado → verificado operativamente → verificado financieramente → cerrado</strong>.</p>'

+ simple([
  "Piénsalo como una <strong>fábrica con estaciones</strong>. Cada estación hace una cosa y le pasa "
  "el trabajo a la siguiente.",
  "<strong>BlankCRM</strong> consigue y persigue clientes — pero lo que muestra depende de lo que el "
  "vendedor escribió.",
  "<strong>BluePrint</strong> es la gerencia: solo registra lo que tiene comprobante, clasifica las "
  "facturas, lleva el P&amp;L, anota los errores con el Glitch Report y <strong>revisa el CRM para ver "
  "si lo reportado cuadra con lo cobrado</strong>.",
  "<strong>Building Blocks</strong> entrena a la gente. <strong>VAULTED</strong> conecta con la red "
  "para conseguir más producto y más compradores.",
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
     "A <strong>BlankCRM</strong>: lo <strong>audita</strong> — detecta cuando lo reportado no cuadra con "
     "lo cobrado. A <strong>Building Blocks</strong>: su motor de demanda — el Glitch Report dice a quién "
     "entrenar y en qué. A <strong>VAULTED</strong>: transacciones verificadas y atribución confiable. A los "
     "<strong>canales</strong>: la consistencia que hace posible franquiciar, y un negocio "
     "<strong>vendible</strong> al final."],
    ["<strong>BlankCRM</strong>",
     "A <strong>BluePrint</strong>: oportunidades calificadas — sin esto no tiene materia prima. A "
     "<strong>VAULTED</strong>: señales de demanda autorizada. A los <strong>canales</strong>: un producto "
     "de entrada barato. A <strong>Dproperty y DpropertyLiving</strong>: la maquinaria de contenido. Su límite: <strong>depende de que el equipo lo use bien</strong>."],
    ["<strong>VAULTED</strong>",
     "A <strong>BluePrint</strong>: más transacciones. A los <strong>canales</strong>: un beneficio que "
     "ningún competidor local ofrece. A <strong>Select</strong>: distribución. "
     "<strong>Hoy da poco: está bloqueado a propósito.</strong>"],
    ["<strong>Building Blocks</strong>",
     "A <strong>BluePrint</strong>: usuarios que saben usarlo — la causa nº1 de fracaso en software B2B "
     "es que nadie aprendió. A la <strong>franquicia</strong>: consistencia entre oficinas. A "
     "<strong>desarrolladores</strong>: corredores certificados por proyecto."],
    ["<strong>Franquicia Dproperty</strong>",
     "A <strong>BluePrint</strong>: los casos reales que prueban el producto y los primeros ingresos. A "
     "<strong>VAULTED</strong>: participantes y oferta. A <strong>Select</strong>: fuerza de distribución. "
     "A la empresa: credibilidad — operamos lo que vendemos."],
    ["<strong>B_ Partner</strong>",
     "A <strong>BluePrint</strong>: clientes que <em>no</em> son Dproperty — la prueba de que la "
     "plataforma es neutral. A <strong>VAULTED</strong>: oferta y demanda independientes."],
    ["<strong>Desarrolladores</strong>",
     "A <strong>VAULTED</strong>: la oferta inicial — resuelve el arranque en frío. A <strong>Select</strong>: "
     "oportunidades candidatas. A <strong>BluePrint</strong>: aprendizaje de ventas complejas."],
    ["<strong>Dproperty Select</strong>",
     "A la <strong>franquicia</strong>: la razón para elegirnos sobre otra marca. A <strong>VAULTED</strong>: "
     "su primera oferta de calidad. A la empresa: la prueba de que entendemos inmobiliaria, no solo software."]], None, 99)

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
