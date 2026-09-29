# -*- coding: utf-8 -*-
"""Contenido en español — ofertas 3 y 4."""

from brand import masthead, simple, table, glance, canvas

M = "B_RealEstate<br>29 sept 2026<br>v3.0"
P2 = {}

# ══════════════════════════════════════════════════════════ 3 · VAULTED
P2["03_VAULTED"] = dict(
 file="VAULTED",
 p1=masthead("Producto — Red / Marketplace", "VAULTED",
   "La red privada de oportunidades: que una operación pequeña tenga el alcance de una grande, sin "
   "dejar de ser pequeña.", M)
 + '<div class="cols"><div>'
 + '<h3>La idea</h3>'
 + '<p>VAULTED es la red privada de B_ para oferta inmobiliaria elegible, demanda calificada, '
   'presentaciones y operaciones atribuibles.</p>'
 + '<p>El problema que resuelve es de <strong>alcance</strong>. Una inmobiliaria boutique tiene buenos '
   'clientes y buen criterio, pero su inventario se limita a lo que consigue directamente. Y al '
   'contrario: quien tiene el inventario no siempre tiene el comprador adecuado. '
   '<strong>La red conecta las dos puntas sin que ninguna pierda su independencia.</strong></p>'
 + '<h3 class="mt">Nuestra ventaja de arranque</h3>'
 + '<p class="small">Un marketplace nuevo normalmente enfrenta el problema del arranque en frío: sin '
   'oferta no llegan compradores, y sin compradores nadie publica. <strong>Nosotros partimos con '
   'relaciones ya construidas</strong> con desarrolladores, corredores e inversionistas. Eso es lo '
   'difícil de conseguir y es lo que ya tenemos.</p>'
 + '<h3 class="mt">Estado — dicho con claridad</h3>'
 + '<p class="small">VAULTED es hoy una <strong>hipótesis bien definida, no un producto en operación</strong>. '
   'Está deliberadamente en pausa hasta que BluePrint esté consolidado. Preferimos concentrar el '
   'esfuerzo en lo que ya está probado y abrir la red cuando podamos sostenerla bien.</p>'
 + '<h3 class="mt">Lo que hay que resolver primero</h3>'
 + '<p class="small">La pregunta central es la <strong>atribución</strong>: cuando la red presenta a dos '
   'partes, el acuerdo tiene que reconocer ese aporte de forma natural y justa para todos. Resolver eso '
   'bien — en el contrato y en la experiencia — es lo que hace viable la red. Es un trabajo de diseño '
   'comercial y legal, y va antes que el desarrollo.</p>'
 + '</div>'
 + glance([("Tipo","Producto — red. Máximo potencial, en etapa temprana."),
           ("Trabajo","Conectar oferta elegible con demanda calificada."),
           ("Modelo","Comisión de éxito sobre operaciones concretadas a través de la red."),
           ("Estado","<strong>En pausa deliberada</strong> hasta consolidar BluePrint."),
           ("Primer paso","Prueba de liquidez en un nicho estrecho, con relaciones ya existentes.")],
          [("Red","La ventaja: relaciones ya construidas"),("Privada","Acceso curado, no portal abierto"),
           ("Éxito","Solo se cobra si la operación se concreta"),("Después","De BluePrint, por decisión")])
 + '</div>'
 + '<h2 style="margin-top:4mm"><span class="snum">01</span>Qué aporta a cada participante</h2>'
 + table(["Participante","Qué gana"], [
     ["<strong>Inmobiliaria boutique</strong>",
      "Acceso a inventario que no podría conseguir sola, y a oportunidades fuera del mercado abierto. "
      "Amplía lo que puede ofrecer a sus clientes sin crecer en estructura."],
     ["<strong>Quien tiene el inventario</strong>",
      "Demanda calificada y presentaciones con contexto, en lugar de publicidad masiva. Llega a "
      "compradores que ya están buscando algo así."],
     ["<strong>Desarrollador</strong>",
      "Distribución a través de una red de profesionales con criterio, complementaria a su propia "
      "fuerza de venta."],
     ["<strong>Franquicia o socio B_</strong>",
      "Un beneficio que su competencia local no tiene: pertenecer a una red que le trae producto y "
      "compradores."],
     ["<strong>Inversionista</strong>",
      "Oportunidades filtradas por quien conoce el mercado, con la información preparada."]], None, 99)
 + simple([
     "VAULTED es <strong>una red privada</strong> donde quien tiene una propiedad y quien busca una "
     "propiedad se encuentran, con nosotros como puente.",
     "El problema que resuelve es de tamaño: <strong>una inmobiliaria pequeña puede ofrecer mucho más "
     "de lo que consigue por su cuenta</strong> — y quien tiene inventario llega a compradores reales "
     "en lugar de publicar al aire.",
     "Solo se cobra <strong>si la operación se concreta</strong>. No hay cuota por participar.",
     "Nuestra ventaja de partida: <strong>ya conocemos a los desarrolladores, corredores e "
     "inversionistas.</strong> Eso es lo difícil de un mercado nuevo, y ya lo tenemos.",
     "Y lo honesto: <strong>todavía no está en operación, y es a propósito.</strong> Primero "
     "consolidamos BluePrint. Es la apuesta de mayor potencial y preferimos abrirla cuando podamos "
     "sostenerla bien."]),
 p2=masthead("VAULTED", "Modelo de Negocio", None, "B_RealEstate<br>29 sept 2026", small=True)
 + canvas(dict(
   kp=["Desarrolladores — aportan oferta","Red de corredores","Inversionistas de la red",
       "Asesoría legal por jurisdicción","Verificación de identidad"],
   ka=["Diseño de la atribución","Curaduría y verificación de participantes",
       "Emparejamiento de oferta y demanda","Acompañamiento de la operación",
       "Cumplimiento por jurisdicción"],
   vp=["Acceso a oportunidades fuera del mercado abierto",
       "Demanda calificada para quien tiene inventario",
       "Presentaciones con contexto y reconocimiento del aporte",
       "Acceso curado — no es un portal abierto",
       "<strong>Más participantes, más valor para todos</strong>"],
   cr=["Acceso por invitación","Curaduría activa de participantes",
       "Acompañamiento en cada operación"],
   cs=["Inmobiliarias boutique","Desarrolladores con inventario",
       "Corredores con compradores","Inversionistas","Franquicias y socios elegibles"],
   kr=["<strong>Las relaciones ya construidas</strong> — la ventaja de arranque",
       "Mecanismo de atribución","Reglas de elegibilidad y acceso","Historial de operaciones"],
   ch=["Relaciones existentes de Dproperty","Canal de desarrolladores",
       "Franquicias y socios B_ Partner","Demanda autorizada desde el CRM"],
   cost=["Construcción del producto","Acompañamiento de operaciones",
         "Verificación de participantes","Asesoría legal por mercado","Activación de la red"],
   rev=["Comisión de éxito sobre operaciones concretadas a través de la red",
        "Posible más adelante: acceso preferente o servicios premium",
        "<strong>Sin ingreso hoy</strong> — producto en pausa deliberada"]))
 + '<h2 style="margin-top:5mm"><span class="snum">02</span>La secuencia, en orden</h2>'
 + table(["Paso","Qué se prueba"], [
     ["<strong>1 · Oferta</strong>","Que en un nicho estrecho, donde ya tenemos relación, alguien quiera publicar."],
     ["<strong>2 · Demanda</strong>","Que haya compradores calificados interesados en esa oferta."],
     ["<strong>3 · Atribución</strong>","Que el aporte de la red quede reconocido de forma natural en el acuerdo."],
     ["<strong>4 · Experiencia</strong>","Que transaccionar en la red sea más cómodo que hacerlo por fuera."],
     ["<strong>5 · Modelo</strong>","Que la comisión de éxito se perciba justa por el valor recibido."],
     ["<strong>6 · Marco legal</strong>","Que la estructura funcione en cada jurisdicción, con asesoría."]], None, 99)
 + '<div class="callout gold">Se avanza <strong>un paso a la vez</strong>. Si uno no se sostiene, nos '
   'detenemos ahí — sin haber comprometido capital en los siguientes.</div>'
 + simple("En una frase: <strong>es la apuesta grande que todavía no hemos hecho.</strong> Si funciona, "
   "deja de ser software con crecimiento lineal y se convierte en una red que se vuelve más valiosa "
   "sola. Si no funciona, no perdimos casi nada porque está en pausa a propósito. Lo que sí tenemos ya "
   "es lo más difícil de construir: <strong>las relaciones</strong>."),
)

# ══════════════════════════════════════════════════════════ 4 · BUILDING BLOCKS
P2["04_Building_Blocks"] = dict(
 file="Building Blocks",
 p1=masthead("Producto — Formación y certificación", "Building Blocks",
   "Convierte la experiencia de la empresa en capacidad transferible: currículos por rol, evaluación y "
   "certificación con evidencia.", M)
 + '<div class="cols"><div>'
 + '<h3>La idea</h3>'
 + '<p>Building Blocks es el producto de formación, incorporación y certificación. Convierte los '
   'estándares de operación en currículos por rol y conserva la asignación, la finalización, la '
   'certificación, la vigencia y la evidencia de competencia.</p>'
 + '<p>Funciona sobre <strong>Open edX</strong> como infraestructura. Open edX es el motor; '
   'Building Blocks es el producto.</p>'
 + '<h3 class="mt">El problema que resuelve</h3>'
 + '<p>Un manual guardado en una carpeta no cambia el comportamiento de nadie. '
   '<strong>El conocimiento de una empresa suele vivir en la cabeza de dos o tres personas</strong>, y '
   'cada persona nueva lo aprende por imitación, con resultados distintos cada vez.</p>'
 + '<p class="small">Para una franquicia eso es el problema central: que una oficina nueva opere con el '
   'mismo estándar que las demás, desde el principio y sin depender de quién la acompañó.</p>'
 + '<h3 class="mt">El diferenciador — el ciclo cerrado</h3>'
 + '<p class="small">Proceso aprobado → ejecución → <strong>BluePrint identifica dónde el proceso '
   'necesita apoyo</strong> → se reconoce la brecha de capacidad → módulo o cohorte de Building '
   'Blocks → evaluación y certificación → <strong>BluePrint reconoce la certificación</strong> → '
   'resultado medido en la operación.</p>'
 + '<p class="small"><strong>El ciclo es la ventaja, no el contenido.</strong> Material formativo hay '
   'de sobra y gratis. Lo que no existe en otro lugar es la conexión entre <em>lo que la operación '
   'muestra que hace falta</em> y <em>la formación que lo resuelve</em>.</p>'
 + '</div>'
 + glance([("Tipo","Producto independiente de formación y certificación."),
           ("Trabajo","Hacer transferible la capacidad de la empresa."),
           ("Modelo","Por inscripción y por programa de certificación. Cohortes empresariales a la medida."),
           ("En paquetes","La incorporación base va incluida en franquicia y socios, valorizada aparte."),
           ("Estado","Arquitectura definida. Plataforma por contratar.")],
          [("Semanas","Para que un equipo nuevo llegue al estándar"),("Por rol","Currículos, no cursos genéricos"),
           ("Vigencia","Certificación con renovación"),("Ciclo","Conectado a la operación real")])
 + '</div>'
 + '<h2 style="margin-top:4mm"><span class="snum">01</span>Cómo está armado</h2>'
 + table(["Capa","Contenido","Cómo se ofrece"], [
     ["<strong>Incorporación base</strong>",
      "Estándares de marca y operación, uso de las plataformas, calificación, diligencia, documentos y "
      "cumplimiento, cierre y comisiones",
      "Incluida para los usuarios definidos de franquicia y socios"],
     ["<strong>Cursos especializados</strong>",
      "Inversión inmobiliaria, venta de proyecto, operación de cumplimiento, liderazgo, producto avanzado",
      "Por inscripción individual"],
     ["<strong>Certificación</strong>",
      "Evaluación, evidencia, vigencia y renovación, habilitación de rol",
      "Por programa"],
     ["<strong>Cohortes empresariales</strong>",
      "Grupo cerrado con marca propia, formación específica de proyecto, tablero para gerencia",
      "A la medida, para desarrolladores y operaciones grandes"]], None, 99)
 + simple([
     "Building Blocks es <strong>la escuela de la empresa</strong>. Toma lo que sabemos hacer y lo "
     "convierte en cursos por rol, con evaluación y certificado.",
     "Resuelve algo muy concreto: <strong>que una oficina nueva trabaje igual de bien que las demás</strong>, "
     "sin depender de quién la entrenó.",
     "Se cobra <strong>por inscripción</strong>, no como una suscripción mensual. Y en los paquetes de "
     "franquicia la formación base va incluida.",
     "Lo que lo hace distinto no es el contenido — de eso hay gratis en internet. Es que "
     "<strong>BluePrint detecta dónde la operación necesita ayuda y manda a la persona al curso "
     "correcto</strong>. Después verifica que se certificó.",
     "Lo honesto: <strong>al principio gana poco dinero.</strong> Su valor real está en que hace "
     "consistente la operación y en que retiene a los clientes del ecosistema."]),
 p2=masthead("Building Blocks", "Modelo de Negocio", None, "B_RealEstate<br>29 sept 2026", small=True)
 + canvas(dict(
   kp=["<strong>Open edX</strong> — la plataforma","Proveedor de alojamiento gestionado",
       "Especialistas de contenido por materia","Cuerpos de certificación locales donde aplique"],
   ka=["Producción de currículo","<strong>Mantenimiento del contenido</strong> — continuo",
       "Diseño de evaluaciones","Administración de certificación","Entrega de cohortes"],
   vp=["Una oficina nueva al estándar <strong>en semanas</strong>",
       "Certificación que <strong>habilita responsabilidades</strong> en BluePrint",
       "Cierra brechas detectadas en la operación real, no supuestas",
       "Evidencia de competencia verificable",
       "Consistencia entre oficinas — el problema central de una franquicia"],
   cr=["Currículo asignado por rol","Cohortes con instructor para empresas",
       "Autoservicio para cursos individuales"],
   cs=["Equipos nuevos de franquicia y socios","Clientes del ecosistema con rotación o ascensos",
       "Equipos de venta de desarrolladores","Profesionales independientes del sector"],
   kr=["<strong>La biblioteca de procesos</strong> como fuente del contenido",
       "Currículos por rol","Registro de certificación y vigencias","Integración con BluePrint"],
   ch=["Incluido en la incorporación de franquicia y socios",
       "<strong>Derivación desde BluePrint</strong> cuando detecta una brecha",
       "Cohortes para desarrolladores","Venta directa de cursos"],
   cost=["Plataforma de formación","<strong>Producción de contenido</strong> — el costo principal",
         "<strong>Mantenimiento del contenido</strong> — continuo, no único",
         "Administración de certificación","Entrega de cohortes y soporte al alumno"],
   rev=["Incorporación base — incluida en paquetes, valorizada a precio de referencia",
        "Cursos especializados — por inscripción",
        "Certificación — por programa, con renovación",
        "Cohortes empresariales y de desarrolladores — a la medida"]))
 + '<h2 style="margin-top:5mm"><span class="snum">02</span>Lo que hay que cuidar</h2>'
 + table(["Tema","Por qué importa","Cómo se maneja"], [
     ["<strong>El contenido se desactualiza</strong>",
      "Cada vez que un proceso cambia, el módulo que lo enseña queda viejo. Un curso desactualizado "
      "deja de convencer.",
      "La biblioteca de procesos es la fuente única. Un cambio de proceso dispara una lista concreta y "
      "acotada de módulos a revisar."],
     ["<strong>Madura despacio</strong>",
      "Es un producto con costo inicial de construcción y retorno gradual.",
      "Se construye solo la incorporación base primero. El catálogo se amplía cuando la demanda real "
      "lo justifique."],
     ["<strong>Lo importante es que se termine</strong>",
      "Un curso que nadie completa no cambia nada.",
      "Currículos cortos por rol, derivación desde la operación real y certificación con vigencia."]], None, 99)
 + '<h2 style="margin-top:3mm"><span class="snum">03</span>Límites que no se cruzan</h2>'
 + '<p class="small soft">No emite <strong>títulos acreditados</strong> y nunca debe insinuarlo · no '
   'reemplaza la formación legal o de cumplimiento donde la regulación exige un proveedor acreditado · '
   'no se convierte en el sistema de registro de procesos — eso corresponde a BluePrint · no almacena '
   'expedientes de operaciones.</p>'
 + simple("En una frase: <strong>es lo que hace que una franquicia nueva trabaje como las demás.</strong> "
   "Su valor está en que una oficina llegue al estándar rápido, y en que cuando la operación muestra "
   "que algo no está funcionando, exista un lugar concreto a dónde llevar a la persona — y una forma de "
   "verificar que quedó resuelto."),
)
