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
+ '<div class="callout gold" style="margin-top:1mm"><strong>El CRM ayuda al equipo a vender. '
  'BluePrint hace la gerencia. Building Blocks forma a las personas. VAULTED amplía el alcance.</strong> '
  'Cada pieza hace aquello en lo que es mejor, y ninguna le pide a otra que haga su trabajo.</div>'
+ '<p class="note">La idea central: <strong>el vendedor vende, y la empresa se ordena por detrás.</strong> '
  'BluePrint además acompaña el uso del CRM y reporta si la actividad comercial está alineada con los '
  'objetivos de la empresa — no es solo el siguiente paso, también es la mirada sobre el anterior.</p>'

+ '<h2 style="margin-top:4mm"><span class="snum">01</span>El flujo</h2>'
+ '<pre style="font-family:\'JetBrains Mono\',monospace;font-size:6.2pt;line-height:1.26;'
  'background:var(--bone-deep);padding:3mm;border-left:2.6pt solid var(--champagne);'
  'white-space:pre;overflow:hidden">'
+ """  Dproperty (inversionista)        DpropertyLiving (usuario final)
            └──────────────┬──────────────┘
                           ▼
            ┌──────────────────────────────┐
            │  BlankCRM  (GoHighLevel)     │  el equipo comercial vende
            └──────────────┬───────────────┘
                     │     ▲ BluePrint acompaña el uso del CRM
   Contabilidad ──► ┌┴─────┴──────┐ ◄── Building Blocks (forma y certifica)
   Banco · Firma    │  BluePrint  │  CEO · CFO · COO · CMO agénticos
                    │  la gerencia profesional de la empresa
                    │  Glitch Report · finanzas · trazabilidad
                    └──────┬──────┘
                           ▼
                    ┌─────────────┐ ◄── Dproperty Select (oferta curada)
                    │   VAULTED   │ ◄── Desarrolladores (oferta de proyecto)
                    └─────────────┘

  CANALES: Franquicia Dproperty · B_ Partner · Alianzas con Desarrolladores"""
+ '</pre>'

+ '<h2 style="margin-top:4mm"><span class="snum">02</span>Quién se encarga de qué</h2>'
+ table(["Ámbito","Se encarga","Por qué ahí"], [
    ["Prospectos, contactos, conversaciones y campañas","<strong>BlankCRM</strong>",
     "Es la herramienta del equipo comercial"],
    ["Todo el ciclo comercial, de captación a postventa","<strong>BlankCRM</strong>",
     "Es donde el vendedor trabaja"],
    ["La información financiera respaldada y su clasificación","<strong>BluePrint</strong>",
     "Nace de un documento, no de un campo llenado"],
    ["Procesos, Glitch Report, indicadores y trazabilidad","<strong>BluePrint</strong>",
     "Es la mirada gerencial de la empresa"],
    ["Inventario de propiedades y proyectos","Sistema del desarrollador o la red",
     "Es de quien lo tiene"],
    ["Oferta de red, conexiones y reconocimiento del aporte","<strong>VAULTED</strong>",
     "Es una red, no un sistema interno"],
    ["Contenido, evaluación y certificación","<strong>Building Blocks</strong>",
     "Es formación, con su propia plataforma"],
    ["Libro contable, impuestos y movimiento de fondos","Contador y banca",
     "Corresponde a profesionales y entidades reguladas"]], None, 99)
+ '<p class="note"><strong>Una sola responsable por ámbito.</strong> No hablamos de «una sola base de '
  'datos»: es un ecosistema conectado donde cada pieza sabe cuál es su trabajo. Por eso nada se duplica '
  'y nadie se pisa.</p>'
+ simple([
  "Piénsalo como <strong>un equipo donde cada uno hace lo que mejor sabe hacer</strong>.",
  "<strong>BlankCRM</strong> es del vendedor: le facilita conseguir y atender clientes.",
  "<strong>BluePrint</strong> es la gerencia: ordena las finanzas, documenta los procesos, anota los "
  "tropiezos y acompaña el uso del CRM. Así <strong>el vendedor no tiene que volverse administrador</strong>.",
  "<strong>Building Blocks</strong> forma al equipo. <strong>VAULTED</strong> amplía el alcance con la red.",
  "Y los <strong>canales</strong> — franquicia, socio de marca propia y desarrolladores — son las tres "
  "formas de llevar todo el paquete a distintos tipos de operador.",
  "<strong>Lo importante:</strong> ninguna pieza le pide a otra que haga su trabajo. Eso es lo que "
  "permite que una empresa pequeña opere con el orden de una grande."]),

# ═══════════════════════════════ PÁGINA 2
masthead("Ecosistema", "Cómo cada bloque crea valor para los demás", None,
         "B_RealEstate<br>24 sept 2026", small=True)

+ '<h2><span class="snum">03</span>Matriz de intercambio de valor</h2>'
+ '<p class="small soft" style="margin-bottom:2mm">Lee cada fila así: «este bloque <strong>le da</strong> '
  'esto a los demás». Donde una fila está vacía, el bloque todavía no aporta — y eso también es información.</p>'
+ table(["Bloque","Qué le da al resto del ecosistema"], [
    ["<strong>BluePrint</strong>",
     "Al <strong>CRM</strong>: lo acompaña y avisa cuando algo no está cuadrando, sin pedirle al equipo "
     "más trabajo administrativo. A <strong>Building Blocks</strong>: le indica qué formación hace falta "
     "y para quién. A <strong>VAULTED</strong>: operaciones respaldadas y reconocimiento confiable del "
     "aporte. A los <strong>canales</strong>: la consistencia que hace posible franquiciar, y una empresa "
     "<strong>ordenada y transferible</strong>."],
    ["<strong>BlankCRM</strong>",
     "A <strong>BluePrint</strong>: evidencia autorizada del ciclo comercial; también admite otros CRM. A "
     "<strong>VAULTED</strong>: señales de demanda autorizada. A los <strong>canales</strong>: un producto "
     "de entrada barato. A <strong>Dproperty y DpropertyLiving</strong>: la maquinaria de contenido. Su límite: <strong>depende de que el equipo lo use bien</strong>."],
    ["<strong>VAULTED</strong>",
     "A <strong>BluePrint</strong>: evidencia para supervisión gerencial. A los <strong>canales</strong>: un beneficio que "
     "ningún competidor local ofrece. A <strong>Select</strong>: distribución. "
     "<strong>Hoy da poco: está bloqueado a propósito.</strong>"],
    ["<strong>Building Blocks</strong>",
     "A <strong>BluePrint</strong> y al <strong>CRM</strong>: equipos que saben aprovecharlos — la razón "
     "más común por la que un buen software no rinde es que nadie tuvo tiempo de aprenderlo. A la "
     "<strong>franquicia</strong>: consistencia entre oficinas. A <strong>desarrolladores</strong>: "
     "corredores formados y certificados por proyecto."],
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
+ '<div class="panel"><h3>1 · Círculo de mejora</h3><p class="small">BluePrint identifica dónde el proceso '
  'necesita apoyo → Building Blocks forma a quien lo necesita → BluePrint reconoce la certificación → '
  'la operación mejora → hay más información para seguir mejorando. <strong>Cada vuelta hace la '
  'herramienta más útil y la formación más pertinente.</strong></p></div>'
+ '<div class="panel"><h3>2 · Circuito de red</h3><p class="small">Más oficinas y socios → más oferta y '
  'demanda en VAULTED → más transacciones atribuibles → la red vale más → ser franquicia o socio vale '
  'más. <strong>Es el único circuito con potencial de efecto de red real.</strong></p></div>'
+ '<div class="panel"><h3>3 · Círculo de prueba</h3><p class="small">Dproperty opera con las plataformas '
  'todos los días → genera casos y aprendizajes reales → el producto mejora y se vuelve ofrecible a '
  'terceros → más operadores → más aprendizaje. <strong>Es la ventaja de haber construido esto desde '
  'dentro de una inmobiliaria que opera.</strong></p></div>'
+ '</div>'


+ simple([
  "La pregunta real es: <strong>¿por qué esto es una empresa y no cuatro productos sueltos?</strong> "
  "Porque cada pieza hace más valiosa a la siguiente.",
  "Ejemplo concreto: <strong>BluePrint nota que en una oficina siempre se traba el mismo paso. Building "
  "Blocks forma a esa persona. BluePrint verifica que quedó resuelto.</strong> Ninguna plataforma de "
  "formación tiene la señal, y ninguna de gestión tiene el curso.",
  "Otro: <strong>los desarrolladores aportan inventario. Ese inventario da valor a la red. La red hace "
  "más atractivo pertenecer al ecosistema. Más participantes traen más inventario.</strong>",
  "Y el más importante: <strong>Dproperty usa todo esto todos los días.</strong> No es un producto "
  "diseñado en teoría — se construyó desde dentro de una inmobiliaria que opera.",
  "Siendo honestos sobre la madurez: <strong>hoy el corazón es BluePrint.</strong> VAULTED es la apuesta "
  "grande y está en pausa a propósito. Los canales llevan el paquete al mercado. Y Select es lo único "
  "que un competidor definitivamente no puede copiar."]),
]
