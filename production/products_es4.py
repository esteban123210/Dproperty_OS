# -*- coding: utf-8 -*-
"""Contenido en español — ofertas 7 y 8."""

from brand import masthead, simple, table, glance, canvas

M = "B_RealEstate<br>24 sept 2026<br>v1.0"
P4 = {}

# ══════════════════════════════════════════════════════════ 7 · DESARROLLADORES
P4["07_Developer_Partnerships"] = dict(
 file="Alianzas con Desarrolladores",
 p1=masthead("Canal — Ingreso, oferta y distribución", "Alianzas con Desarrolladores",
   "Servicio comercial a equipos de venta de desarrolladores: proceso, formación, reporte y "
   "distribución en red.", M)
 + '<div class="cols"><div>'
 + '<h3>La idea</h3>'
 + '<p>Las alianzas con desarrolladores son un canal de <strong>ingreso + oferta + distribución + '
   'aprendizaje de producto</strong>. No son un quinto producto.</p>'
 + '<p>B_ puede aportar: armado de CRM y proceso comercial, formación, activación de corredores, '
   'reporte, mesa de ventas gestionada, distribución en red y servicios operativos seleccionados.</p>'
 + '<h3 class="mt">Por qué importan más allá de la comisión</h3>'
 + '<p class="small"><strong>1)</strong> Ingreso directo de servicio y desempeño · <strong>2)</strong> '
   '<strong>siembran la oferta de VAULTED</strong> — la ventaja de arranque en frío · '
   '<strong>3)</strong> oportunidades potenciales para Dproperty Select · <strong>4)</strong> '
   'aprendizaje de producto con organizaciones de venta complejas · <strong>5)</strong> distribución '
   'hacia los equipos de venta del desarrollador.</p>'
 + '<p class="small">Las razones 2 a 5 son por las que este canal existe a pesar de una contribución '
   'delgada en el retainer. Internamente hay que ser honestos: <strong>el retainer está cerca de ser '
   'un mecanismo de recuperación de costos</strong>, no de margen.</p>'
 + '<h3 class="mt">La ambigüedad que se corrigió</h3>'
 + '<p class="small">Los porcentajes históricos se citaban <strong>sin decir sobre qué base</strong>. '
   '0.5% del valor de la transacción en una unidad de $300,000 son <strong>$1,500</strong>; 0.5% de '
   'una bolsa de comisión del 3% son <strong>$45</strong>. Una diferencia de <strong>33 veces</strong>. '
   'Regla nueva: <strong>todo porcentaje declara su denominador, siempre</strong>.</p>'
 + '</div>'
 + glance([("Tipo","Canal. Alianza comercial y de distribución, no consultoría de desarrollo."),
           ("Trabajo","Servir al equipo comercial del desarrollador y sembrar oferta de red."),
           ("Mesa gestionada","<strong>$3,000–$5,000</strong>/mes — retainer fijo"),
           ("Equipo propio","<strong>0.5%</strong> del <strong>valor de la transacción</strong>"),
           ("Originado en red","<strong>2.5–3.0%</strong> del <strong>valor de la transacción</strong>")],
          [("$1,500","Equipo propio, unidad de $300k"),("$7,500","Originado en red, 2.5%"),
           ("$500–2,500","Contribución mensual de la mesa"),("33×","La ambigüedad corregida")])
 + '</div>'
 + '<h2 style="margin-top:4mm"><span class="snum">01</span>Ejemplos sobre una unidad de $300,000</h2>'
 + '<div class="cols2">'
 + table(["Escenario","Comisión","B_ recibe"], [
     ["Equipo propio del desarrollador, B_ opera proceso y reporte","0.5% del valor","$1,500"],
     ["Originado en red — B_ trae al comprador","2.5% del valor","$7,500"],
     ["Originado en red, banda alta","3.0% del valor","$9,000"],
     ["Mesa de ventas gestionada","fijo","$3,000–$5,000/mes"]], "Tarifas con base explícita")
 + table(["Caso","B_ recibe","Queda para los demás"], [
     ["Equipo propio 0.5%","$1,500","$10,500"],
     ["Originado en red 2.5%","$7,500","$4,500"],
     ["Originado en red 3.0%","$9,000","$3,000"]], "Sobre una bolsa del 4% = $12,000")
 + '</div>'
 + '<div class="callout"><strong>Aquí es donde el precio se prueba en la realidad.</strong> Al 3% del '
   'valor de la transacción, B_ toma tres cuartas partes de una bolsa del 4%. Eso solo se defiende '
   'cuando B_ realmente consiguió un comprador que el desarrollador no podía alcanzar. '
   '<strong>Si la bolsa del desarrollador es del 3%, una tarifa de red del 3% se la consume completa '
   'y el negocio es imposible.</strong> Cada cotización debe verificarse contra la bolsa real de ese '
   'proyecto antes de ofrecerse.</div>'
 + '<p class="note"><strong>Por qué la brecha de 5–6× entre equipo propio y originado en red es '
   'correcta:</strong> en el primer caso B_ aporta <em>proceso e infraestructura</em> mientras los '
   'corredores del desarrollador son dueños de la relación y de la venta. En el segundo, B_ aporta '
   '<em>el comprador</em> — que es el insumo escaso y carga el costo de adquisición.</p>'
 + simple([
     "Hay <strong>tres formas</strong> de cobrar: una mesa de ventas fija ($3,000–$5,000 al mes), "
     "un <strong>0.5%</strong> si el desarrollador vende con su propio equipo y nosotros ponemos el "
     "proceso, o un <strong>2.5–3%</strong> si nosotros traemos al comprador.",
     "Todos esos porcentajes son <strong>sobre el precio de la propiedad</strong>, no sobre la comisión. "
     "Antes esto estaba confuso y la diferencia era de <strong>33 veces</strong>.",
     "Traducido: en una propiedad de $300,000 cobramos <strong>$1,500</strong> si es su equipo, o "
     "<strong>$7,500</strong> si nosotros conseguimos al comprador.",
     "<strong>Advertencia importante:</strong> nuestra comisión sale de la bolsa que el desarrollador "
     "ya tenía asignada, no se suma. Si el desarrollador solo tiene 3% para repartir y nosotros "
     "pedimos 3%, <strong>el negocio no se puede hacer</strong>. Hay que revisar proyecto por proyecto.",
     "La mesa de ventas <strong>casi no deja margen</strong>. La hacemos porque nos da relación, "
     "inventario para VAULTED y aprendizaje — no porque sea rentable."]),
 p2=masthead("Alianzas con Desarrolladores", "Modelo de Negocio", None,
             "B_RealEstate<br>24 sept 2026", small=True)
 + canvas(dict(
   kp=["Desarrolladores inmobiliarios","Red de corredores externos",
       "Asesores legales para comisiones y licencias","Proveedores de marketing de proyecto"],
   ka=["Armado de CRM y proceso comercial","Activación y formación de corredores",
       "Operación de mesa de ventas","Reporte al desarrollador","Distribución en red"],
   vp=["Proceso comercial armado sin contratar estructura",
       "Corredores activados y formados rápido",
       "Reporte confiable del avance de ventas",
       "<strong>Acceso a nuestra red de compradores</strong>",
       "Formación específica del proyecto vía Building Blocks"],
   cr=["Relación directa con la dirección comercial","Reporte periódico de desempeño",
       "Mesa gestionada como servicio continuo"],
   cs=["Desarrolladores con equipo de venta interno",
       "Desarrolladores que venden vía corredores externos",
       "Proyectos de preventa y nueva construcción"],
   kr=["<strong>La red de compradores e inversionistas</strong>","Proceso comercial documentado",
       "Capacidad de mesa de ventas","Stack de software configurable"],
   ch=["Relaciones existentes de Dproperty","Referidos del sector",
       "Presentaciones directas a desarrolladores"],
   cost=["<strong>Personal de mesa de ventas — intensivo en headcount</strong>",
         "Gestión de cuenta y reporte","Armado inicial de proceso","Formación de corredores"],
   rev=["Mesa de ventas gestionada — $3,000–$5,000/mes",
        "Equipo propio — 0.5% del <strong>valor de la transacción</strong>",
        "Originado en red — 2.5–3.0% del <strong>valor de la transacción</strong>",
        "Software para el equipo del desarrollador — precio de lista",
        "Cohortes de Building Blocks — licencia cotizada",
        "<strong>Componente de éxito — bloqueado hasta revisión legal</strong>"]))
 + '<h2 style="margin-top:5mm"><span class="snum">02</span>Límite que no debe desplazarse</h2>'
 + '<p class="small">B_RealEstate <strong>no es dueño</strong> del inventario de proyectos ni unidades '
   'del desarrollador, y <strong>BluePrint no se convierte</strong> en el sistema de registro del '
   'inventario. La ejecución de reservas queda en el sistema propio del desarrollador. Disciplina de '
   'alcance: esto es una <strong>alianza de ventas y distribución de inventario</strong>, no consultoría '
   'amplia de desarrollo.</p>'
 + '<h2 style="margin-top:3mm"><span class="snum">03</span>Pendientes críticos</h2>'
 + '<p class="small soft"><span class="chip">[R]</span> Las <strong>comisiones de éxito requieren '
   'abogado</strong> antes de ofrecerse en cualquier jurisdicción — las licencias de corretaje y las '
   'reglas de reparto de comisión las gobiernan · <span class="chip">[R]</span> el acceso al inventario '
   'del desarrollador es una <strong>dependencia crítica sin base contractual documentada</strong> · '
   '<span class="chip">[R]</span> las cohortes de Building Blocks no tienen estructura de precio — '
   'riesgo real de que se absorban gratis en el retainer · <span class="chip">[R]</span> los acuerdos '
   'firmados existentes deben revisarse contra estas bases antes de reutilizar cualquier cifra.</p>'
 + simple("En una frase: <strong>servimos al desarrollador para conseguir dos cosas que no se compran "
   "con dinero: inventario y aprendizaje.</strong> La mesa de ventas casi no deja margen, pero nos pone "
   "adentro de proyectos grandes, nos da producto para vender y para VAULTED, y nos enseña cómo opera "
   "una fuerza de ventas compleja. Hay que ser muy cuidadosos con los porcentajes: salen de la bolsa "
   "que el desarrollador ya tenía, no se suman."),
)

# ══════════════════════════════════════════════════════════ 8 · DPROPERTY SELECT
P4["08_Dproperty_Select"] = dict(
 file="Dproperty Select",
 p1=masthead("Activo estratégico — Inventario curado", "Dproperty Select",
   "El programa de oportunidades de inversión curadas por HQ: flujo de negocio diferenciado que la "
   "competencia no puede replicar comprando software.", M)
 + '<div class="cols"><div>'
 + '<h3>La idea</h3>'
 + '<p>Dproperty Select es el programa de oportunidades de inversión <strong>curadas por HQ</strong>. '
   'Aporta flujo de negocio diferenciado, relaciones negociadas, prueba de expertise en el dominio y '
   'economía de transacción.</p>'
 + '<p><strong>No es un producto de software.</strong> Es un activo estratégico — y es la parte del '
   'ecosistema que un competidor no puede replicar comprando tecnología.</p>'
 + '<h3 class="mt">La distinción crítica con VAULTED</h3>'
 + '<p><strong>Dproperty Select = curado por nosotros.</strong> HQ decide qué califica.<br>'
   '<strong>VAULTED = marketplace de red.</strong> Participar no implica respaldo.</p>'
 + '<p class="small">Select puede aparecer dentro de VAULTED como una colección claramente identificada, '
   'pero <strong>VAULTED nunca confiere aprobación Select</strong>.</p>'
 + '<h3 class="mt">Gobierno — no negociable</h3>'
 + '<p class="small">HQ controla la curaduría, los supuestos aprobados, los materiales, el acceso y los '
   'términos comerciales. Los socios <strong>pueden proponer</strong> oportunidades pero '
   '<strong>no pueden auto-aprobar</strong> el estatus Select. Cualquier afirmación pública de que los '
   'franquiciados curan el portafolio es <strong>incorrecta</strong> y debe corregirse.</p>'
 + '</div>'
 + glance([("Tipo","Activo estratégico. No es producto de software ni canal de franquicia."),
           ("Trabajo","Proveer flujo de oportunidad de inversión curada."),
           ("Economía","Comisión de transacción retenida"),
           ("Pago histórico",'<strong>2.5%</strong> a socio de marca · <strong>1.5%</strong> a socio '
                             'de marca propia elegible <span class="chip">[A]</span>'),
           ("Estado","Activo y operando. <strong>Verificar acuerdos firmados</strong> antes de uso externo.")],
          [("HQ","Única autoridad de curaduría"),("2.5% / 1.5%","Pago a socio, por verificar"),
           ("≠ VAULTED","Curado, no marketplace"),("Difícil","De replicar por un competidor")])
 + '</div>'
 + '<h2 style="margin-top:4mm"><span class="snum">01</span>Qué controla y qué no</h2>'
 + '<div class="cols2">'
 + table(["Controla"], [["Decisiones de curaduría y aprobación"],
     ["Supuestos aprobados y materiales"],["Derechos de acceso y niveles"],
     ["Términos comerciales"],["Estructura de pago a socios"]], None, 99)
 + table(["NO controla"], [["Inventario de proyectos como sistema (sistema del desarrollador)"],
     ["Ejecución de la transacción (BluePrint)"],["Mecánica de marketplace (VAULTED)"],
     ["El libro contable"],["Aprobación de estatus Select por parte de socios"]], None, 99)
 + '</div>'
 + '<p class="note">BluePrint puede recibir resultados financieros y operativos verificados a nivel '
   'empresa relacionados con Select. <strong>No administra el inventario ni ejecuta la transacción.</strong></p>'
 + '<h2 style="margin-top:3mm"><span class="snum">02</span>Por qué es valioso estratégicamente</h2>'
 + '<p class="small">Un competidor puede comprar un CRM, licenciar un LMS y construir un software de '
   'transacciones. <strong>No puede comprar quince años de relaciones con desarrolladores ni la '
   'capacidad de negociar condiciones preferentes.</strong> Select es la prueba de que B_RealEstate '
   'entiende el negocio inmobiliario y no solo el software — y es lo que hace creíble la promesa de '
   'franquicia y de red.</p>'
 + '<p class="small">También es el <strong>combustible inicial de VAULTED</strong>: la primera oferta '
   'de calidad que puede sembrar el marketplace viene de aquí y de las alianzas con desarrolladores.</p>'
 + simple([
     "Select es <strong>nuestra lista de oportunidades escogidas a mano</strong>. Nosotros decidimos "
     "qué entra y qué no. Punto.",
     "Al socio que vende una de estas oportunidades le pagamos <strong>2.5%</strong> si usa nuestra "
     "marca, o <strong>1.5%</strong> si usa su propia marca. <strong>Hay que verificar esto contra los "
     "contratos firmados</strong> antes de decirlo por fuera.",
     "No confundir con VAULTED: <strong>Select lo escogemos nosotros; VAULTED es un mercado abierto a "
     "la red.</strong> Que algo esté en VAULTED no significa que lo aprobamos.",
     "Un franquiciado <strong>puede proponer</strong> una oportunidad, pero <strong>nunca puede "
     "aprobarla él mismo</strong>. Si en algún lugar dice lo contrario, está mal y hay que corregirlo.",
     "Por qué importa aunque no sea software: <strong>un competidor puede copiar nuestra tecnología, "
     "pero no puede copiar quince años de relaciones con desarrolladores.</strong>"]),
 p2=masthead("Dproperty Select", "Modelo de Negocio", None, "B_RealEstate<br>24 sept 2026", small=True)
 + canvas(dict(
   kp=["Desarrolladores con proyectos de calidad","Vendedores de inmuebles de inversión",
       "Asesores legales y fiscales","Socios de marca y marca propia como distribuidores"],
   ka=["<strong>Curaduría y aprobación</strong>","Negociación de condiciones preferentes",
       "Producción de materiales y supuestos","Control de acceso por nivel",
       "Supervisión del cumplimiento de términos"],
   vp=["Oportunidades filtradas por quien conoce el mercado",
       "Condiciones negociadas mejores que las de mercado abierto",
       "Supuestos y materiales preparados y aprobados",
       "<strong>Ahorro de tiempo y reducción de riesgo</strong> para el inversionista",
       "Para el socio: producto diferenciado que su competencia no tiene"],
   cr=["Acceso por nivel y elegibilidad","Relación directa con HQ para aprobaciones",
       "Acompañamiento en la presentación al inversionista"],
   cs=["Inversionistas inmobiliarios","Franquicias Dproperty como distribuidores",
       "Socios B_ Partner elegibles","Clientes de banca privada y asesores patrimoniales"],
   kr=["<strong>Las relaciones con desarrolladores</strong> — el activo real",
       "Criterio y método de curaduría","Historial de operaciones",
       "Reputación de la marca Dproperty"],
   ch=["Franquicias y socios como fuerza de distribución",
       "Relaciones directas con inversionistas",
       "Posible colección identificada dentro de VAULTED"],
   cost=["Tiempo de análisis y curaduría","Negociación y relación con desarrolladores",
         "Producción de materiales","Pago de comisión a socios distribuidores",
         "Revisión legal de cada oportunidad"],
   rev=["Comisión de transacción retenida por HQ",
        "Pago al socio de marca — 2.5% histórico, por verificar",
        "Pago al socio de marca propia elegible — 1.5% histórico, por verificar",
        "<strong>Economía separada del software y de las regalías</strong>"]))
 + '<h2 style="margin-top:5mm"><span class="snum">03</span>Pendientes críticos</h2>'
 + '<p class="small soft"><span class="chip">[R]</span> <strong>Economía sin verificar contra acuerdos '
   'firmados.</strong> La base de 2.5%/1.5% es histórica · <span class="chip">[R]</span> '
   '<strong>no existe nota legal</strong> — responsabilidad de curaduría, idoneidad del inversionista, '
   'descargos de inversión y límites de afirmaciones de marketing están sin documentar. Esto es un '
   'programa de <strong>inversión</strong>, así que es una exposición real · '
   '<span class="chip">[R]</span> no existe perfil definido del inversionista Select.</p>'
 + '<div class="callout gold"><strong>Regla de comunicación:</strong> nunca insinuar disponibilidad '
   'amplia en la red ni autoridad de curaduría por parte de los franquiciados.</div>'
 + simple("En una frase: <strong>es la razón por la que un corredor querría nuestra franquicia en vez "
   "de cualquier otra.</strong> No es software y no se puede copiar. Es el acceso a oportunidades que "
   "nosotros escogimos y negociamos. Nos falta ponerle orden legal y verificar los porcentajes contra "
   "los contratos, pero estratégicamente es lo que hace creíble todo lo demás."),
)
