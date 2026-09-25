# -*- coding: utf-8 -*-
"""Contenido en español — ofertas 5 a 8 (canales y activo estratégico)."""

from brand import masthead, simple, table, glance, canvas

M = "B_RealEstate<br>24 sept 2026<br>v1.0"
P3 = {}

# ══════════════════════════════════════════════════════════ 5 · FRANQUICIA DPROPERTY
P3["05_Dproperty_Franchise"] = dict(
 file="Franquicia Dproperty",
 p1=masthead("Canal — Franquicia de marca", "Franquicia Dproperty",
   "El modelo operativo completo bajo la marca Dproperty: identidad, stack de software, estándares, "
   "formación y acceso a inventario curado.", M)
 + '<div class="cols"><div>'
 + '<h3>La idea</h3>'
 + '<p>Dproperty es la marca insignia de inversión, el laboratorio de operación y un canal de '
   'distribución verticalmente integrado del stack de B_.</p>'
 + '<p>Una franquicia recibe el modelo operativo completo: identidad Dproperty, stack configurado '
   '(<strong>BluePrint + BlankCRM + Building Blocks + VAULTED</strong>), estándares y formación, '
   'acceso a Dproperty Select, implementación y participación en la red.</p>'
 + '<p><strong>No es la definición de la empresa.</strong> B_RealEstate es una compañía de software '
   'e infraestructura; la franquicia es <em>un canal</em>. Es una ventaja de salida al mercado que '
   'la mayoría de las startups de software no tiene — no es la tecnología propietaria en sí.</p>'
 + '<h3 class="mt">Estructura de regalía — resuelta</h3>'
 + '<p class="small">Existían tres estructuras en conflicto. La estructura <strong>diferenciada</strong> '
   'es la canónica: Dproperty <strong>6% + 1%</strong> de fondo de marca restringido; marca propia '
   '<strong>4% sin fondo</strong>. La diferencia de 3 puntos <strong>es el precio de la marca</strong>. '
   'Si se elimina, uno de los dos canales queda redundante.</p>'
 + '<h3 class="mt">Definición que importa</h3>'
 + '<p class="small soft">La regalía se calcula sobre <strong>GCI cobrado</strong> — comisión '
   'efectivamente cobrada y retenida después de compartir con corredores externos y devoluciones, '
   'sin impuesto indirecto, antes de pagos a agentes internos. El <strong>fondo de 1% no es ingreso '
   'ni utilidad</strong>: está segregado y excluido del EBITDA.</p>'
 + '</div>'
 + glance([("Tipo","Canal. No es un producto de software separado."),
           ("Trabajo","Desplegar el modelo operativo completo de marca."),
           ("Entrada",'<strong>$50,000</strong> lista · <strong>$40,000</strong> para las dos '
                      'primeras aperturas fundadoras <span class="chip">[A]</span>'),
           ("Regalía","<strong>6%</strong> del GCI cobrado + piso de $750/mes desde el mes 13"),
           ("Fondo de marca","<strong>1%</strong> del GCI cobrado — restringido, excluido del EBITDA")],
          [("$58,224","Utilidad operativa modelada"),("16.2%","Utilidad sobre GCI"),
           ("37 meses","Recuperación de inversión"),("~$98,000","Capital recomendado para abrir")])
 + '</div>'
 + '<h2 style="margin-top:4mm"><span class="snum">01</span>Economía</h2>'
 + '<div class="cols2">'
 + table(["Concepto","Anual"], [
     ["GCI cobrado","$360,000"],
     ["Pagos a agentes","($198,000)"],
     ["Costo fijo local + sueldo del dueño","($72,000)"],
     ["Regalía 6%","($21,600)"],
     ["Fondo de marca 1%","($3,600)"],
     ["BluePrint después del año 1","(~$4,788)"],
     ["<strong>Utilidad operativa modelada</strong>","<strong>~$58,224</strong>"]],
     "Para el franquiciado — oficina madura [A]")
 + table(["Concepto","Anual"], [
     ["Regalía 6%","$21,600"],
     ["BluePrint tras el año gratis","~$4,788"],
     ["BlankCRM si se engancha","~$2,988"],
     ["<strong>Ingreso recurrente bruto</strong>","<strong>~$29,376</strong>"],
     ["Fondo de marca 1%","$3,600 — <strong>no es ingreso</strong>"],
     ['Costo de soporte por oficina <span class="chip">[R]</span>',"<strong>sin medir</strong>"]],
     "Para B_RealEstate — por oficina madura")
 + '</div>'
 + '<div class="callout gold"><strong>La pregunta que realmente hace un prospecto:</strong> «¿Cuánto '
   'tengo que ganar de más para justificar el costo de la franquicia frente a seguir independiente?» '
   '— Aproximadamente <strong>$92,632 de GCI adicional al año, unos 9.3 cierres más</strong> '
   '<span class="chip">[A]</span>. Es una barra real, y decirlo con claridad convence más que cualquier '
   'proyección.</div>'
 + simple([
     "El franquiciado paga <strong>$40,000–$50,000</strong> de entrada y necesita unos "
     "<strong>$98,000</strong> en total para abrir, contando remodelación y capital de trabajo.",
     "Después paga <strong>6% de la comisión que cobra</strong>, más <strong>1%</strong> que va a un "
     "fondo de marca (ese 1% no es nuestra ganancia, se gasta en marca).",
     "En una oficina que funciona bien, al franquiciado le quedan unos <strong>$58,000 al año</strong> "
     "y recupera su inversión en <strong>poco más de 3 años</strong>.",
     "Lo honesto: para que le convenga frente a seguir solo, tiene que vender "
     "<strong>unos 9 inmuebles más al año</strong>. Si no los vende, no le conviene.",
     "A nosotros nos deja unos <strong>$29,000 al año por oficina</strong> — pero todavía "
     "<strong>no sabemos cuánto nos cuesta atenderla</strong>. Eso falta medir."]),
 p2=masthead("Franquicia Dproperty", "Modelo de Negocio", None, "B_RealEstate<br>24 sept 2026", small=True)
 + canvas(dict(
   kp=["Franquiciados locales","Asesores legales por jurisdicción","Desarrolladores para inventario",
       "ACOBIR y cuerpos locales del sector"],
   ka=["Reclutamiento y selección de franquiciados","Implementación y apertura",
       "Formación y certificación","Soporte de campo continuo"],
   vp=["Modelo operativo probado, no hay que inventarlo",
       "Stack completo de software incluido el primer año",
       "Marca con reputación en inversión inmobiliaria",
       "Acceso a <strong>Dproperty Select</strong> — inventario curado",
       "Participación en la red y en VAULTED cuando sea elegible"],
   cr=["Acompañamiento intensivo en la apertura","Soporte de campo recurrente",
       "Plan estratégico anual con HQ"],
   cs=["Corredores establecidos que quieren estructura",
       "Profesionales con cartera que quieren marca",
       "Inversionistas que buscan operar un negocio inmobiliario"],
   kr=["<strong>La marca Dproperty</strong> y su historial","Biblioteca de procesos y manuales",
       "Stack de software propio","Relaciones con desarrolladores","Programa Dproperty Select"],
   ch=["Referidos de la red existente","Venta directa del fundador","Eventos del sector"],
   cost=["Apertura y viajes","Comisión de venta","Legal y contratación",
         "Soporte de campo","Plataforma de software"],
   rev=["Cuota de entrada — $50,000 lista, $40,000 fundadora",
        "Regalía — 6% del GCI cobrado",
        "Piso mínimo de regalía — $750/mes desde el mes 13",
        "Software tras el año gratis — valorizado a precio de lista",
        "<strong>Fondo de marca 1% — restringido, NO es ingreso</strong>"]))
 + '<h2 style="margin-top:5mm"><span class="snum">02</span>Comparación con B_ Partner</h2>'
 + table(["Concepto","Franquicia Dproperty","B_ Partner"], [
     ["Cuota de entrada","$50,000 ($40k fundadora)","$30,000 ($25k fundadora)"],
     ["Regalía","6% del GCI cobrado","4% del GCI cobrado"],
     ["Piso mínimo","$750/mes","$400/mes"],
     ["Fondo de marca","1% restringido","ninguno"],
     ["Marca al consumidor","Dproperty","la del socio"],
     ["Recurrente a $360k de GCI","~$29,376","~$22,176"]])
 + '<h2 style="margin-top:3mm"><span class="snum">03</span>Pendientes críticos</h2>'
 + '<p class="small soft"><span class="chip">[R]</span> Diseño de contrato y asesoría legal local por '
   'jurisdicción — nada aquí está revisado legalmente · <span class="chip">[R]</span> '
   '<strong>no existe pipeline firmado ni pagado</strong>; toda la economía del franquiciado es '
   'modelada, no observada · <span class="chip">[R]</span> costo de soporte y campo por oficina sin '
   'medir, por lo que la contribución neta es desconocida · <span class="chip">[R]</span> mecánica '
   'contractual del piso de regalía ante bajo desempeño y terminación.</p>'
 + simple("En una frase: <strong>es nuestra forma de crecer rápido sin poner todo el capital.</strong> "
   "El franquiciado pone la inversión y la operación local; nosotros ponemos la marca, el software y "
   "el método. Nos deja ingreso recurrente y, más importante, nos da <strong>casos reales que prueban "
   "que el software funciona</strong>. Pero es un canal, no es la empresa."),
)

# ══════════════════════════════════════════════════════════ 6 · B_ PARTNER
P3["06_B_Partner"] = dict(
 file="B_ Partner",
 p1=masthead("Canal — Marca propia gestionada", "B_ Partner",
   "La inmobiliaria conserva su marca y compra una implementación gestionada de la infraestructura y "
   "los estándares de B_.", M)
 + '<div class="cols"><div>'
 + '<h3>La idea</h3>'
 + '<p>Una inmobiliaria mantiene su propia marca frente al consumidor, pero compra una implementación '
   'gestionada más profunda de la infraestructura y los estándares de operación de B_.</p>'
 + '<p>Los socios de marca propia corren sobre <strong>el mismo código y el mismo modelo de datos</strong>. '
   'La marca y los permisos son <strong>configuración</strong>, nunca una bifurcación del código.</p>'
 + '<h3 class="mt">Por qué no es «BluePrint más caro»</h3>'
 + '<p>BluePrint solo cuesta $399–$799 al mes con $1,500 de arranque. B_ Partner justifica una entrada '
   'de $30,000 y una regalía <strong>únicamente porque incluye servicios reales</strong>: implementación '
   'y migración, armado del modelo operativo, paquetes de proceso y manuales, configuración de BlankCRM, '
   'incorporación de Building Blocks, soporte de integración, acompañamiento operativo continuo, '
   'participación en la red y acceso elegible a Dproperty Select y VAULTED.</p>'
 + '<div class="callout" style="margin-top:2mm"><strong>Si el prospecto solo quiere el software, '
   'véndele BluePrint.</strong> Forzar un modelo de regalía a un comprador de software es la forma en '
   'que este canal se come la venta directa. Regla canónica: si los socios prefieren SaaS, '
   '<strong>cambia el modelo</strong> en lugar de forzar la regalía.</div>'
 + '<h3 class="mt">Regla de datos y marca</h3>'
 + '<p class="small soft">El cliente es dueño de su marca y de los datos de su instancia. B_RealEstate '
   '<strong>no puede</strong> tratar los datos de un B_ Partner como un conjunto competitivo compartido.</p>'
 + '</div>'
 + glance([("Tipo","Canal. No es un producto de software separado."),
           ("Trabajo","Entregar el stack gestionado bajo la marca del cliente."),
           ("Entrada",'<strong>$30,000</strong> lista · <strong>$25,000</strong> para los dos '
                      'primeros socios fundadores <span class="chip">[A]</span>'),
           ("Regalía","<strong>4%</strong> del GCI cobrado + piso de $400/mes"),
           ("Fondo de marca","<strong>Ninguno</strong> — es la diferencia deliberada con Dproperty")],
          [("$22,176","Recurrente por socio maduro"),("$15.3k–33k","Costo real de lanzamiento"),
           ("4% vs 6%","El precio de la marca"),("2","Socios fundadores máximo sugerido")])
 + '</div>'
 + '<h2 style="margin-top:4mm"><span class="snum">01</span>Economía</h2>'
 + '<div class="cols2">'
 + table(["Componente del lanzamiento","Estimado"], [
     ["Implementación y migración de datos","$4,000–$8,000"],
     ["Modelo operativo y paquete de procesos","$3,000–$6,000"],
     ["Configuración e incorporación de BluePrint","$2,000–$4,000"],
     ["Configuración de BlankCRM","$750–$1,500"],
     ["Building Blocks base (valorizado)","$1,500–$3,000"],
     ["Soporte de integración","$1,000–$3,000"],
     ["Costo de venta del socio","$2,000–$5,000"],
     ["Legal y contratación","$1,000–$2,500"],
     ["<strong>Costo total de lanzamiento</strong>","<strong>$15,250–$33,000</strong>"]],
     "Qué debe cubrir la cuota de entrada [A]")
 + table(["Concepto","Anual"], [
     ["Regalía 4% sobre $360k de GCI","$14,400"],
     ["Piso mínimo (si GCI &lt; $360k)","$4,800"],
     ["BluePrint tras el año 1","~$4,788"],
     ["BlankCRM si se engancha","~$2,988"],
     ["<strong>Recurrente bruto por socio maduro</strong>","<strong>~$22,176</strong>"],
     ['Costo de soporte por socio <span class="chip">[R]</span>',"<strong>sin medir</strong>"]],
     "Para B_RealEstate")
 + '</div>'
 + '<p class="note"><strong>A $30,000 de lista la cuota de entrada apenas cubre el costo de '
   'lanzamiento</strong> —y en el extremo alto del rango, casi sin margen. Al precio fundador de '
   '$25,000 probablemente está <strong>por debajo del costo</strong>. Es aceptable para los dos '
   'primeros socios como una <strong>inversión declarada en referencias</strong>, pero debe registrarse '
   'así y nunca modelarse como utilidad de la cuota de entrada.</p>'
 + simple([
     "El socio conserva <strong>su propia marca</strong>. Nosotros le ponemos el software, los procesos "
     "y el acompañamiento por detrás.",
     "Paga <strong>$25,000–$30,000</strong> de entrada y <strong>4% de la comisión que cobra</strong>. "
     "No paga fondo de marca porque promociona su marca, no la nuestra.",
     "¿Por qué 4% y no 6% como Dproperty? Porque <strong>esos 3 puntos de diferencia son el precio de "
     "usar la marca Dproperty</strong>. Si cobramos igual, uno de los dos modelos no tiene sentido.",
     "Cuidado con esto: <strong>lanzar un socio nos cuesta entre $15,000 y $33,000</strong>. La cuota "
     "de entrada apenas lo cubre. No es donde ganamos — ganamos en la regalía a lo largo del tiempo.",
     "El límite real no es el dinero, es <strong>nuestra capacidad de atender</strong>. Sugerimos "
     "máximo <strong>2 socios fundadores</strong> antes de comprometer más."]),
 p2=masthead("B_ Partner", "Modelo de Negocio", None, "B_RealEstate<br>24 sept 2026", small=True)
 + canvas(dict(
   kp=["Inmobiliarias establecidas con marca propia","Asesores legales por jurisdicción",
       "Proveedores de software del stack","Consultores de implementación"],
   ka=["Implementación y migración","Armado del modelo operativo","Configuración del stack",
       "Acompañamiento operativo continuo","Gestión de permisos y configuración de marca"],
   vp=["Conserva tu marca, gana nuestra infraestructura",
       "Modelo operativo armado, no hay que diseñarlo",
       "Stack completo configurado y soportado",
       "Menor regalía que una franquicia de marca",
       "Participación en la red y acceso elegible a Select y VAULTED",
       "<strong>Tus datos son tuyos</strong> — garantía contractual"],
   cr=["Implementación de alto contacto","Acompañamiento operativo recurrente",
       "Relación de socio, no de franquiciado"],
   cs=["Inmobiliarias con marca establecida y reputación local",
       "Firmas que rechazan franquiciar su marca",
       "Operaciones que necesitan estructura sin perder identidad"],
   kr=["Mismo código y modelo de datos que todos","Motor de configuración y permisos",
       "Paquetes de proceso y manuales","Capacidad de implementación del equipo"],
   ch=["Venta directa del fundador","Referidos del sector",
       "Conversión desde clientes de BluePrint que quieren más servicio"],
   cost=["<strong>Trabajo de implementación — intensivo</strong>","Acompañamiento operativo continuo",
         "Costo de venta del socio","Legal y contratación","Plataforma de software"],
   rev=["Cuota de entrada — $30,000 lista, $25,000 fundadora",
        "Regalía — 4% del GCI cobrado",
        "Piso mínimo — $400/mes desde el mes 13",
        "Software valorizado a precio de lista tras el año 1",
        "Migración compleja y oficinas adicionales, cotizadas",
        "<strong>Sin fondo de marca</strong>"]))
 + '<h2 style="margin-top:5mm"><span class="snum">02</span>El riesgo de capacidad — la restricción real</h2>'
 + '<p class="small">B_ Partner es <strong>intensivo en servicio</strong>. Cada socio consume capacidad '
   'de implementación y acompañamiento que de otro modo atendería clientes de venta directa. '
   '<strong>Límite sugerido:</strong> tope de socios fundadores en el número que el equipo realmente '
   'puede implementar (se sugiere <strong>dos</strong>, igual al número de descuentos fundadores) antes '
   'de comprometer más. Un socio firmado que no se puede implementar a tiempo destruye justamente el '
   'valor de referencia por el que se dio el descuento.</p>'
 + '<h2 style="margin-top:3mm"><span class="snum">03</span>Pendientes críticos</h2>'
 + '<p class="small soft"><span class="chip">[R]</span> Costo de soporte y gestión de cuenta por socio '
   'sin medir — la contribución neta es desconocida · <span class="chip">[R]</span> la estructura de '
   'regalía requiere diseño de contrato y asesoría legal local · <span class="chip">[R]</span> '
   '<strong>¿confiarán las firmas ajenas a Dproperty</strong> en una plataforma cuyo dueño también '
   'opera una marca de franquicia competidora? Requiere una historia de separación legal y técnica · '
   '<span class="chip">[A]</span> el GCI de $360k es un escenario modelado, no un resultado observado.</p>'
 + simple("En una frase: <strong>es para la inmobiliaria que quiere nuestra maquinaria pero no quiere "
   "dejar de ser ella misma.</strong> Paga menos regalía que una franquicia porque no usa nuestra marca. "
   "Nos sirve para llegar a firmas buenas y establecidas que jamás aceptarían franquiciarse — pero "
   "consume mucho tiempo de nuestro equipo, así que hay que ir despacio."),
)
