# -*- coding: utf-8 -*-
"""Contenido en español — ofertas 7 y 8."""

from brand import masthead, simple, table, glance, canvas

M = "B_RealEstate<br>25 sept 2026<br>v3.0"
P4 = {}

# ══════════════════════════════════════════════════════════ 7 · DESARROLLADORES
P4["07_Developer_Partnerships"] = dict(
 file="Alianzas con Desarrolladores",
 p1=masthead("Canal — Alianza comercial", "Alianzas con Desarrolladores",
   "Acompañamos al equipo comercial de un desarrollador: proceso, formación, activación de corredores, "
   "reportería y distribución en red.", M)
 + '<div class="cols"><div>'
 + '<h3>La idea</h3>'
 + '<p>Un desarrollador construye bien. Vender es otro oficio, y sostenerlo exige una estructura '
   'comercial que no siempre tiene sentido montar internamente para un solo proyecto.</p>'
 + '<p>Ahí entramos: aportamos el <strong>proceso comercial armado</strong>, la formación y activación '
   'de corredores, la reportería de avance y el acceso a nuestra red de compradores — sin que el '
   'desarrollador tenga que construir un área comercial desde cero.</p>'
 + '<h3 class="mt">Tres formas de trabajar juntos</h3>'
 + '<p class="small"><strong>1 · Mesa comercial gestionada.</strong> Operamos la mesa de ventas del '
   'proyecto: proceso, seguimiento, reportería y coordinación de corredores, con un honorario mensual '
   'definido.</p>'
 + '<p class="small"><strong>2 · Apoyo al equipo propio.</strong> El desarrollador vende con su gente; '
   'nosotros aportamos el proceso, las plataformas, la formación y la reportería. El reconocimiento es '
   'menor porque la relación con el cliente sigue siendo suya.</p>'
 + '<p class="small"><strong>3 · Originado en la red.</strong> Nosotros traemos al comprador. El '
   'reconocimiento es mayor porque aportamos el insumo más escaso: la demanda calificada.</p>'
 + '<h3 class="mt">Una claridad importante</h3>'
 + '<p class="small">Nuestro reconocimiento <strong>sale de la bolsa de comisión que el proyecto ya tiene '
   'asignada</strong> — no se suma por encima. Cada propuesta se revisa contra la estructura real de ese '
   'proyecto antes de presentarse, para que la operación sea viable para todas las partes. '
   '<strong>Un acuerdo que no le cierra al desarrollador no le sirve a nadie.</strong></p>'
 + '</div>'
 + glance([("Tipo","Canal. Alianza comercial y de distribución."),
           ("Trabajo","Acompañar al equipo comercial del desarrollador y sumar oferta a la red."),
           ("Modelo","Honorario mensual por mesa gestionada, o reconocimiento sobre la operación "
                     "concretada según quién aportó el comprador."),
           ("Base","El reconocimiento sale de la bolsa de comisión ya asignada del proyecto."),
           ("Alcance","Alianza de ventas y distribución — no consultoría de desarrollo.")],
          [("Proceso","Comercial armado, sin montar estructura"),("Corredores","Activados y formados"),
           ("Red","Acceso a compradores calificados"),("Reporte","Avance real de ventas")])
 + '</div>'
 + '<h2 style="margin-top:4mm"><span class="snum">01</span>Qué aporta cada modalidad</h2>'
 + table(["Modalidad","Qué aportamos","Qué reconoce el proyecto"], [
     ["<strong>Mesa comercial gestionada</strong>",
      "Operación completa de la mesa: proceso, seguimiento, coordinación de corredores, reportería a la "
      "dirección.",
      "Honorario mensual definido, independiente del resultado."],
     ["<strong>Apoyo al equipo propio</strong>",
      "Proceso comercial, plataformas configuradas, formación del equipo y reportería de avance. La "
      "relación con el cliente es del desarrollador.",
      "Reconocimiento menor sobre la operación — aportamos infraestructura, no la demanda."],
     ["<strong>Originado en la red</strong>",
      "El comprador. Calificado, acompañado y con la información preparada.",
      "Reconocimiento mayor — aportamos el insumo escaso y asumimos el costo de conseguirlo."]], None, 99)
 + '<p class="note">La diferencia entre las dos últimas modalidades es deliberada y se explica sola: '
   '<strong>traer el proceso y traer el comprador son aportes de valor muy distinto.</strong></p>'
 + simple([
     "Ayudamos al desarrollador a vender su proyecto sin que tenga que montar un área comercial completa.",
     "Hay <strong>tres formas</strong>: le operamos la mesa de ventas por un honorario mensual, le "
     "ponemos el proceso y la formación mientras vende con su equipo, o le traemos nosotros al comprador.",
     "Cuanto más aportamos, mayor es el reconocimiento. <strong>Traer al comprador vale más que traer "
     "el proceso</strong>, y así se refleja.",
     "Algo clave y muy concreto: <strong>lo que cobramos sale de la comisión que el proyecto ya tenía "
     "asignada, no se suma encima.</strong> Por eso revisamos cada proyecto antes de proponer: si no le "
     "cierra al desarrollador, no hay negocio para nadie.",
     "Para nosotros este canal vale por algo más que el honorario: <strong>nos da inventario para la red, "
     "relación con desarrolladores y aprendizaje real</strong> de cómo opera una fuerza de ventas grande."]),
 p2=masthead("Alianzas con Desarrolladores", "Modelo de Negocio", None,
             "B_RealEstate<br>25 sept 2026", small=True)
 + canvas(dict(
   kp=["Desarrolladores inmobiliarios","Red de corredores externos",
       "Asesores legales en materia de comisiones y licencias","Proveedores de marketing de proyecto"],
   ka=["Armado del proceso comercial","Activación y formación de corredores",
       "Operación de la mesa de ventas","Reportería a la dirección","Distribución en la red"],
   vp=["Proceso comercial armado sin montar estructura interna",
       "Corredores activados y formados con rapidez",
       "Reportería confiable del avance de ventas",
       "<strong>Acceso a una red de compradores calificados</strong>",
       "Formación específica del proyecto vía Building Blocks"],
   cr=["Relación directa con la dirección comercial","Reportería periódica de desempeño",
       "Mesa gestionada como servicio continuo"],
   cs=["Desarrolladores con equipo comercial interno",
       "Desarrolladores que venden a través de corredores externos",
       "Proyectos de preventa y obra nueva"],
   kr=["<strong>La red de compradores e inversionistas</strong>","Proceso comercial documentado",
       "Capacidad de operar una mesa de ventas","Plataformas configurables"],
   ch=["Relaciones existentes de Dproperty","Referidos del sector",
       "Presentación directa a desarrolladores"],
   cost=["<strong>Equipo de la mesa comercial</strong> — el componente principal",
         "Gestión de la relación y reportería","Armado inicial del proceso",
         "Formación de corredores"],
   rev=["Honorario mensual por mesa comercial gestionada",
        "Reconocimiento sobre operaciones con apoyo al equipo propio",
        "Reconocimiento mayor sobre operaciones originadas en la red",
        "Plataformas para el equipo del desarrollador",
        "Cohortes de formación específicas del proyecto"]))
 + '<h2 style="margin-top:5mm"><span class="snum">02</span>Por qué este canal importa más allá del honorario</h2>'
 + table(["Beneficio","Por qué cuenta"], [
     ["<strong>Oferta para la red</strong>",
      "Resuelve el arranque en frío de VAULTED. El inventario de proyecto es la primera oferta de "
      "calidad que puede activar la red."],
     ["<strong>Candidatos para Dproperty Select</strong>",
      "Las mejores oportunidades que pasan por aquí pueden entrar al programa curado."],
     ["<strong>Aprendizaje de producto</strong>",
      "Una fuerza de ventas de proyecto es más compleja que una inmobiliaria boutique. Lo que "
      "aprendemos ahí mejora las plataformas para todos."],
     ["<strong>Distribución</strong>",
      "Acceso a los equipos comerciales del desarrollador, que son usuarios potenciales del ecosistema."]], None, 99)
 + '<div class="callout">Internamente somos claros: <strong>la mesa gestionada no es el negocio de mayor '
   'margen.</strong> Se hace porque abre relación, inventario y aprendizaje — y esos tres no se compran.</div>'
 + '<h2 style="margin-top:3mm"><span class="snum">03</span>Límites y pendientes</h2>'
 + '<p class="small soft">No somos dueños del inventario del desarrollador ni de la ejecución de sus '
   'reservas — eso queda en sus sistemas · es una alianza de ventas y distribución, '
   '<strong>no consultoría amplia de desarrollo</strong> · los componentes de reconocimiento por '
   'desempeño requieren revisión legal en cada jurisdicción antes de ofrecerse, porque las reglas de '
   'licencia y reparto de comisión los gobiernan · el acceso al inventario debe quedar documentado '
   'contractualmente en cada alianza.</p>'
 + simple("En una frase: <strong>acompañamos al desarrollador para conseguir dos cosas que no se compran: "
   "inventario y aprendizaje.</strong> La mesa comercial deja margen modesto, pero nos pone dentro de "
   "proyectos grandes, nos da producto para la red y nos enseña cómo funciona una fuerza de ventas "
   "compleja. Y siempre revisamos que el acuerdo le cierre al desarrollador."),
)

# ══════════════════════════════════════════════════════════ 8 · DPROPERTY SELECT
P4["08_Dproperty_Select"] = dict(
 file="Dproperty Select",
 p1=masthead("Activo estratégico — Inventario curado", "Dproperty Select",
   "El programa de oportunidades de inversión seleccionadas por la casa matriz: lo que un competidor "
   "no puede replicar comprando tecnología.", M)
 + '<div class="cols"><div>'
 + '<h3>La idea</h3>'
 + '<p>Dproperty Select es el programa de oportunidades de inversión <strong>curadas por la casa '
   'matriz</strong>. Aporta flujo de negocio diferenciado, condiciones negociadas y la prueba de que '
   'entendemos el oficio inmobiliario, no solamente el software.</p>'
 + '<p><strong>No es un producto de tecnología.</strong> Es un activo construido con años de relación, '
   'y es la parte del ecosistema que no se puede copiar con presupuesto.</p>'
 + '<h3 class="mt">Qué aporta a quien lo distribuye</h3>'
 + '<p class="small">Una oficina o un socio de la red puede ofrecer a sus clientes oportunidades que su '
   'competencia local no tiene, con la información y los supuestos ya preparados. '
   '<strong>Amplía lo que puede ofrecer sin tener que salir a buscar y negociar cada oportunidad por su '
   'cuenta.</strong> Y recibe un reconocimiento por la operación que concreta.</p>'
 + '<h3 class="mt">Qué aporta al inversionista</h3>'
 + '<p class="small">Oportunidades filtradas por quien conoce el mercado, con supuestos preparados y '
   'condiciones negociadas. <strong>Ahorra tiempo de búsqueda y reduce el riesgo de evaluar solo.</strong></p>'
 + '<h3 class="mt">La distinción con VAULTED</h3>'
 + '<p><strong>Select lo seleccionamos nosotros.</strong> La casa matriz decide qué califica.<br>'
   '<strong>VAULTED es una red abierta a sus participantes.</strong> Estar en la red no implica respaldo.</p>'
 + '<p class="small">Select puede aparecer dentro de VAULTED como una colección claramente identificada, '
   'pero <strong>estar en VAULTED nunca otorga el estatus Select</strong>.</p>'
 + '</div>'
 + glance([("Tipo","Activo estratégico. No es producto de software ni canal de franquicia."),
           ("Trabajo","Proveer flujo de oportunidades de inversión curadas."),
           ("Modelo","Comisión de la operación, con un reconocimiento al socio que la concreta."),
           ("Gobierno","La casa matriz cura, aprueba y define los términos. Los socios proponen."),
           ("Por qué importa","Es lo que un competidor no puede replicar comprando tecnología.")],
          [("Curado","Seleccionado, no listado"),("Matriz","Única autoridad de aprobación"),
           ("≠ VAULTED","Curado, no red abierta"),("Años","De relación construida")])
 + '</div>'
 + '<h2 style="margin-top:4mm"><span class="snum">01</span>Gobierno del programa</h2>'
 + table(["Aspecto","Cómo funciona"], [
     ["<strong>Curaduría</strong>",
      "La casa matriz evalúa y decide qué oportunidad entra al programa. El criterio es explícito y "
      "consistente."],
     ["<strong>Materiales y supuestos</strong>",
      "Se preparan y aprueban centralmente, para que todos presenten la misma información verificada."],
     ["<strong>Propuestas de la red</strong>",
      "Los socios <strong>pueden proponer</strong> oportunidades y se les agradece que lo hagan — pero "
      "<strong>la aprobación siempre es de la casa matriz</strong>."],
     ["<strong>Acceso</strong>",
      "Definido por nivel y elegibilidad, según el tipo de relación con el ecosistema."],
     ["<strong>Términos comerciales</strong>",
      "Definidos centralmente, con un reconocimiento al socio que concreta la operación."]], None, 99)
 + '<div class="callout gold">Cualquier afirmación pública de que las oficinas de la red curan el '
   'portafolio <strong>es incorrecta y debe corregirse</strong>. La curaduría centralizada es justamente '
   'lo que le da valor al programa: si cualquiera pudiera aprobar, no sería un programa curado.</div>'
 + simple([
     "Select es <strong>nuestra lista de oportunidades escogidas a mano</strong>. La casa matriz decide "
     "qué entra y qué no, y prepara la información.",
     "Para una oficina de la red, esto significa <strong>poder ofrecerle a su cliente algo que la "
     "competencia local no tiene</strong>, sin tener que salir a buscar y negociar cada oportunidad "
     "por su cuenta.",
     "Para el inversionista significa oportunidades ya filtradas, con los supuestos preparados y las "
     "condiciones negociadas. <strong>Ahorra tiempo y reduce riesgo.</strong>",
     "No confundir con VAULTED: <strong>Select lo escogemos nosotros; VAULTED es una red.</strong> Que "
     "algo esté en la red no significa que lo respaldamos.",
     "Una oficina <strong>puede proponer</strong> una oportunidad — y se agradece — pero la aprobación "
     "es siempre de la casa matriz. Esa disciplina es precisamente lo que hace valioso el programa.",
     "Por qué importa aunque no sea software: <strong>un competidor puede copiar la tecnología, pero no "
     "puede copiar años de relación con los desarrolladores.</strong>"]),
 p2=masthead("Dproperty Select", "Modelo de Negocio", None, "B_RealEstate<br>25 sept 2026", small=True)
 + canvas(dict(
   kp=["Desarrolladores con proyectos de calidad","Propietarios de inmuebles de inversión",
       "Asesores legales y fiscales","Oficinas y socios de la red como distribuidores"],
   ka=["<strong>Curaduría y aprobación</strong>","Negociación de condiciones",
       "Preparación de materiales y supuestos","Control de acceso por nivel",
       "Acompañamiento en la presentación al inversionista"],
   vp=["Oportunidades filtradas por quien conoce el mercado",
       "Condiciones negociadas mejores que en el mercado abierto",
       "Supuestos y materiales preparados y verificados",
       "<strong>Ahorro de tiempo y menor riesgo</strong> para el inversionista",
       "Para el socio: producto diferenciado que su competencia no tiene"],
   cr=["Acceso por nivel y elegibilidad","Relación directa con la casa matriz para aprobaciones",
       "Acompañamiento en la presentación"],
   cs=["Inversionistas inmobiliarios","Franquicias Dproperty como distribuidores",
       "Socios B_ Partner elegibles","Asesores patrimoniales y banca privada"],
   kr=["<strong>Las relaciones con desarrolladores</strong> — el activo real",
       "El criterio y el método de curaduría","El historial de operaciones",
       "La reputación de la marca Dproperty"],
   ch=["Oficinas y socios como fuerza de distribución",
       "Relación directa con inversionistas",
       "Posible colección identificada dentro de VAULTED"],
   cost=["Tiempo de análisis y curaduría","Negociación y relación con desarrolladores",
         "Preparación de materiales","Reconocimiento al socio que concreta",
         "Revisión legal de cada oportunidad"],
   rev=["Comisión de la operación, retenida por la casa matriz",
        "Reconocimiento al socio distribuidor según su relación con el ecosistema",
        "<strong>Economía independiente del software y de las regalías</strong>"]))
 + '<h2 style="margin-top:5mm"><span class="snum">02</span>Qué acompaña y qué no</h2>'
 + '<div class="cols2">'
 + '<div><h3>Acompaña</h3><p class="small">La decisión de curaduría y aprobación · los supuestos y '
   'materiales aprobados · los derechos de acceso por nivel · los términos comerciales · la estructura '
   'de reconocimiento a los socios distribuidores.</p></div>'
 + '<div><h3>No acompaña</h3><p class="small soft">El inventario del proyecto como sistema — eso es del '
   'desarrollador · la ejecución de la operación — eso es de BluePrint · la mecánica de la red — eso es '
   'de VAULTED · el libro contable.</p></div>'
 + '</div>'
 + '<h2 style="margin-top:3mm"><span class="snum">03</span>Lo que está en construcción</h2>'
 + '<p class="small soft">La estructura de reconocimiento a los socios se está verificando contra los '
   'acuerdos firmados antes de publicarse · falta documentar el marco legal del programa: '
   'responsabilidad de la curaduría, idoneidad del inversionista y límites de las afirmaciones de '
   'marketing — <strong>es un programa de inversión y merece ese rigor</strong> · y falta definir con '
   'precisión el perfil del inversionista Select.</p>'
 + simple("En una frase: <strong>es la razón por la que un corredor querría nuestra red y no otra.</strong> "
   "No es software y no se puede copiar: es el acceso a oportunidades que nosotros seleccionamos y "
   "negociamos. Le falta orden legal y verificación de los términos, pero estratégicamente es lo que "
   "hace creíble todo lo demás."),
)
