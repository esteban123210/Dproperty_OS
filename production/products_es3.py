# -*- coding: utf-8 -*-
"""Contenido en español — ofertas 5 y 6 (canales de franquicia)."""

from brand import masthead, simple, table, glance, canvas

M = "B_RealEstate<br>29 sept 2026<br>v3.0"
P3 = {}

# ══════════════════════════════════════════════════════════ 5 · FRANQUICIA DPROPERTY
P3["05_Dproperty_Franchise"] = dict(
 file="Franquicia Dproperty",
 p1=masthead("Canal — Franquicia de marca", "Franquicia Dproperty",
   "El modelo operativo completo bajo la marca Dproperty: identidad, plataformas, estándares, "
   "formación y acceso a inventario curado.", M)
 + '<div class="cols"><div>'
 + '<h3>La idea</h3>'
 + '<p>Dproperty es la marca insignia de inversión inmobiliaria y el laboratorio donde el modelo se '
   'prueba todos los días. La franquicia lleva ese modelo completo a un operador local.</p>'
 + '<p>Quien toma una franquicia recibe el modelo operativo entero: identidad Dproperty, las '
   'plataformas configuradas (<strong>BluePrint + BlankCRM + Building Blocks</strong>), estándares y '
   'formación, acceso a Dproperty Select, implementación acompañada y participación en la red.</p>'
 + '<h3 class="mt">Qué problema le resuelve al operador</h3>'
 + '<p class="small">Un buen corredor independiente enfrenta siempre el mismo techo: es excelente '
   'vendiendo, pero <strong>crecer le exige convertirse en administrador, en gerente de procesos y en '
   'director financiero</strong> — trabajos distintos al que eligió y en los que no necesariamente '
   'quiere invertir su tiempo.</p>'
 + '<p class="small">La franquicia le entrega esa estructura ya construida. Sigue haciendo lo que sabe '
   'hacer, y la empresa a su alrededor funciona a un estándar que por su cuenta le tomaría años armar.</p>'
 + '<h3 class="mt">Lo que aporta cada parte</h3>'
 + '<p class="small"><strong>El operador aporta</strong> el conocimiento del mercado local, la relación '
   'con sus clientes y la ejecución comercial. <strong>Nosotros aportamos</strong> la marca, las '
   'plataformas, el método, la formación, el acceso a inventario curado y el acompañamiento continuo. '
   'Cada uno hace aquello en lo que es mejor.</p>'
 + '<h3 class="mt">El modelo económico, en concepto</h3>'
 + '<p class="small">Una cuota de incorporación que cubre la implementación y el lanzamiento, y luego '
   'una <strong>regalía calculada sobre la comisión efectivamente cobrada</strong> — de modo que crece '
   'cuando al operador le va bien y baja cuando no. Se suma un <strong>aporte a un fondo de marca</strong>, '
   'que no es utilidad nuestra: se reinvierte en construir la marca que todos usan. Los términos '
   'específicos se detallan en propuesta aparte.</p>'
 + '</div>'
 + glance([("Tipo","Canal. No es un producto de software separado."),
           ("Trabajo","Llevar el modelo operativo completo de marca a un operador local."),
           ("Modelo","Cuota de incorporación, regalía sobre comisión cobrada y aporte a fondo de marca."),
           ("Incluye","Marca · plataformas · estándares · formación · Dproperty Select · acompañamiento."),
           ("Alineación","La regalía se calcula sobre lo cobrado: si al operador le va bien, a todos "
                         "les va bien.")],
          [("Marca","Reputación en inversión inmobiliaria"),("Método","Procesos y manuales probados"),
           ("Select","Acceso a inventario curado"),("Red","Participación en el ecosistema")])
 + '</div>'
 + '<h2 style="margin-top:4mm"><span class="snum">01</span>Qué recibe una oficina nueva</h2>'
 + table(["Componente","Qué significa en la práctica"], [
     ["<strong>Marca e identidad</strong>",
      "Una marca con historial y reputación en inversión inmobiliaria, con su manual y sus materiales "
      "listos para usar."],
     ["<strong>Las plataformas configuradas</strong>",
      "El front office comercial y el back office de gestión, ya armados para el modelo — no un "
      "software genérico que hay que configurar desde cero."],
     ["<strong>Procesos y manuales</strong>",
      "La biblioteca de procesos del negocio: captación, preventa, mercado secundario, cesión, alquiler, "
      "administración y comisiones. Documentada y probada."],
     ["<strong>Formación y certificación</strong>",
      "El equipo llega al estándar en semanas a través de Building Blocks, con certificación por rol."],
     ["<strong>Dproperty Select</strong>",
      "Acceso a oportunidades curadas por la casa matriz — producto que la competencia local no tiene."],
     ["<strong>Acompañamiento</strong>",
      "Implementación de la apertura, soporte continuo y revisión periódica de estándares con la "
      "casa matriz."]], None, 99)
 + simple([
     "Una franquicia Dproperty es <strong>un negocio inmobiliario completo, listo para operar</strong>: "
     "marca, plataformas, procesos, formación y acceso a inventario curado.",
     "Resuelve el techo del buen corredor independiente: <strong>para crecer tendría que volverse "
     "administrador y gerente</strong>, y esos son trabajos distintos al que eligió.",
     "El costo tiene dos partes: una <strong>cuota de incorporación</strong> que paga el arranque, y "
     "una <strong>regalía sobre la comisión que efectivamente cobra</strong>. Si vende, paga; si no "
     "vende, baja.",
     "Hay además un <strong>aporte al fondo de marca</strong>. Ese dinero no es ganancia nuestra: se "
     "reinvierte en la marca que usan todas las oficinas.",
     "Lo que hay que mirar con honestidad antes de firmar: <strong>cuánto más necesita vender la "
     "oficina para que la franquicia le convenga frente a seguir independiente.</strong> Ese número "
     "existe, se calcula y se conversa abiertamente en la propuesta."]),
 p2=masthead("Franquicia Dproperty", "Modelo de Negocio", None, "B_RealEstate<br>29 sept 2026", small=True)
 + canvas(dict(
   kp=["Operadores locales","Asesores legales por jurisdicción","Desarrolladores para inventario",
       "Cuerpos locales del sector inmobiliario"],
   ka=["Selección y acompañamiento de operadores","Implementación y apertura",
       "Formación y certificación","Soporte continuo y revisión de estándares"],
   vp=["Un modelo operativo probado — no hay que inventarlo",
       "Las plataformas configuradas desde el primer día",
       "Una marca con reputación en inversión inmobiliaria",
       "Acceso a <strong>Dproperty Select</strong> — inventario curado",
       "Participación en la red del ecosistema",
       "<strong>Una empresa ordenada y transferible</strong> desde el inicio"],
   cr=["Acompañamiento intensivo en la apertura","Soporte recurrente",
       "Plan estratégico anual con la casa matriz"],
   cs=["Corredores establecidos que quieren estructura",
       "Profesionales con cartera que quieren una marca",
       "Inversionistas que buscan operar un negocio inmobiliario"],
   kr=["<strong>La marca Dproperty</strong> y su historial","Biblioteca de procesos y manuales",
       "Las plataformas propias","Relaciones con desarrolladores","Programa Dproperty Select"],
   ch=["Referidos de la red existente","Relación directa","Eventos del sector"],
   cost=["Apertura y acompañamiento en sitio","Desarrollo del canal","Legal y contratación",
         "Soporte continuo","Plataformas"],
   rev=["Cuota de incorporación",
        "Regalía sobre la comisión efectivamente cobrada",
        "Plataformas después del período incluido",
        "<strong>Fondo de marca — reinvertido en la marca, no es utilidad</strong>"]))
 + '<h2 style="margin-top:5mm"><span class="snum">02</span>Franquicia de marca o marca propia</h2>'
 + '<p class="small">Existen dos caminos, y la diferencia es deliberada:</p>'
 + table(["","Franquicia Dproperty","B_ Partner"], [
     ["Marca frente al cliente","<strong>Dproperty</strong>","<strong>La del operador</strong>"],
     ["Fondo de marca","Sí — se reinvierte en la marca compartida","No aplica: promociona su propia marca"],
     ["Regalía","Mayor — incluye el valor de la marca","Menor — sin el componente de marca"],
     ["Para quién","Quien quiere una marca con reputación ya construida",
      "Quien ya tiene marca propia y reputación local"]], None, 99)
 + '<div class="callout gold">La diferencia en la regalía <strong>es exactamente el valor de la marca</strong>. '
   'Quien usa su propia marca no recibe ese beneficio y por eso aporta menos. Es la lógica que hace que '
   'los dos caminos tengan sentido y no compitan entre sí.</div>'
 + '<p class="note"><strong>En construcción:</strong> el diseño de contrato y la asesoría legal por '
   'jurisdicción están en proceso — nada se firma sin eso · el modelo económico del operador se validará '
   'con las primeras oficinas · el acompañamiento por oficina se está midiendo, porque de eso depende '
   'cuántas podemos atender bien a la vez.</p>'
 + simple("En una frase: <strong>es la forma de crecer sin que cada oficina tenga que inventar la "
   "empresa de nuevo.</strong> El operador pone el mercado local y la ejecución comercial; nosotros "
   "ponemos la marca, las plataformas y el método. Nos deja ingreso recurrente y, más importante, casos "
   "reales que demuestran que el modelo funciona."),
)

# ══════════════════════════════════════════════════════════ 6 · B_ PARTNER
P3["06_B_Partner"] = dict(
 file="B_ Partner",
 p1=masthead("Canal — Marca propia acompañada", "B_ Partner",
   "La inmobiliaria conserva su marca y su identidad, y suma la infraestructura y los estándares de "
   "operación de B_.", M)
 + '<div class="cols"><div>'
 + '<h3>La idea</h3>'
 + '<p>Hay inmobiliarias con marca propia, reputación local y clientela construida durante años. '
   '<strong>Pedirles que cambien de marca sería pedirles que renuncien a su activo más valioso.</strong></p>'
 + '<p>B_ Partner existe para ellas: conservan su nombre frente al cliente y suman por detrás la '
   'infraestructura, los procesos y el acompañamiento del ecosistema.</p>'
 + '<h3 class="mt">Qué problema resuelve</h3>'
 + '<p class="small">Una firma establecida suele tener un buen nombre y una operación que creció de '
   'forma orgánica: procesos en la cabeza de las personas, información repartida entre planillas y '
   'correos, y una administración que funciona porque alguien la sostiene a pulso. '
   '<strong>Quiere profesionalizarse sin perder lo que la hizo buena.</strong></p>'
 + '<h3 class="mt">Qué incluye realmente</h3>'
 + '<p class="small">Implementación y migración · armado del modelo operativo · paquetes de procesos y '
   'manuales adaptados · configuración del front office comercial · incorporación a Building Blocks · '
   'soporte de integración · acompañamiento operativo continuo · participación en la red y acceso '
   'elegible a Dproperty Select y VAULTED.</p>'
 + '<div class="callout">Es un modelo <strong>de servicio, no solo de licencia</strong>. Eso es lo que '
   'lo distingue de simplemente contratar el software: el valor está en el acompañamiento y en el '
   'modelo operativo, no únicamente en el acceso a la plataforma.</div>'
 + '<h3 class="mt">Una regla clara sobre los datos</h3>'
 + '<p class="small">El socio es dueño de su marca y de la información de su operación. '
   '<strong>B_RealEstate no trata esa información como un activo compartido.</strong> Los socios corren '
   'sobre la misma plataforma, pero su información es suya y está separada.</p>'
 + '</div>'
 + glance([("Tipo","Canal. Modelo de servicio, no un producto de software aparte."),
           ("Trabajo","Entregar la infraestructura y el método bajo la marca del socio."),
           ("Modelo","Cuota de incorporación y regalía sobre comisión cobrada. Sin fondo de marca."),
           ("Conserva","Su marca, su identidad, su clientela y su información."),
           ("Diferencia","Aporta menos que una franquicia de marca, porque promociona su propia marca.")],
          [("Su marca","Se conserva intacta"),("Sus datos","Le pertenecen y están separados"),
           ("Método","Procesos y manuales adaptados"),("Red","Acceso según elegibilidad")])
 + '</div>'
 + '<h2 style="margin-top:4mm"><span class="snum">01</span>Por qué no es simplemente licenciar el software</h2>'
 + table(["Componente","Qué aporta"], [
     ["<strong>Implementación y migración</strong>",
      "Traer la información histórica de forma ordenada, sin perder lo que ya existe y sin frenar la "
      "operación."],
     ["<strong>Armado del modelo operativo</strong>",
      "Traducir la forma de trabajar de la firma a procesos documentados, en lugar de imponer un molde ajeno."],
     ["<strong>Procesos y manuales adaptados</strong>",
      "La biblioteca de procesos ajustada al mercado y a la realidad local del socio."],
     ["<strong>Formación del equipo</strong>",
      "Incorporación a Building Blocks para que el equipo alcance el estándar sin depender de quién le enseñó."],
     ["<strong>Acompañamiento continuo</strong>",
      "Una relación de trabajo permanente, no una licencia y un manual de usuario."],
     ["<strong>Participación en la red</strong>",
      "Acceso elegible a inventario curado y a la red — un beneficio que su competencia local no tiene."]], None, 99)
 + '<p class="note">Si lo que la firma quiere es únicamente la plataforma, <strong>lo correcto es '
   'ofrecerle el software directo</strong>. Este modelo tiene sentido cuando busca el acompañamiento y '
   'el método, no solo el acceso.</p>'
 + simple([
     "B_ Partner es para la inmobiliaria que <strong>ya tiene su marca y no la quiere cambiar</strong>, "
     "pero quiere la maquinaria por detrás.",
     "Conserva su nombre, su clientela y su información. Suma nuestros procesos, nuestras plataformas "
     "y nuestro acompañamiento.",
     "Aporta <strong>menos que una franquicia de marca</strong> — y eso es a propósito: no está usando "
     "nuestra marca ni recibiendo ese beneficio, así que no contribuye al fondo que la construye.",
     "Es un modelo <strong>de servicio</strong>: el valor está en la implementación, el método y el "
     "acompañamiento. Si alguien solo quiere la plataforma, le ofrecemos la plataforma directa.",
     "Una regla que no se negocia: <strong>sus datos son suyos.</strong> Corremos sobre la misma "
     "plataforma pero su información está separada y le pertenece."]),
 p2=masthead("B_ Partner", "Modelo de Negocio", None, "B_RealEstate<br>29 sept 2026", small=True)
 + canvas(dict(
   kp=["Inmobiliarias establecidas con marca propia","Asesores legales por jurisdicción",
       "Proveedores de las plataformas","Consultores de implementación"],
   ka=["Implementación y migración","Armado del modelo operativo","Configuración de las plataformas",
       "Acompañamiento operativo continuo","Configuración de marca y permisos"],
   vp=["<strong>Conserva tu marca, suma nuestra infraestructura</strong>",
       "El modelo operativo armado, no hay que diseñarlo",
       "Las plataformas configuradas y acompañadas",
       "Aporta menos que una franquicia de marca",
       "Acceso elegible a inventario curado y a la red",
       "<strong>Tus datos son tuyos</strong> — garantía contractual"],
   cr=["Implementación de alto contacto","Acompañamiento operativo recurrente",
       "Relación de socio, no de franquiciado"],
   cs=["Inmobiliarias con marca establecida y reputación local",
       "Firmas que no quieren franquiciar su nombre",
       "Operaciones que buscan estructura sin perder identidad"],
   kr=["Misma plataforma para todos, con configuración por socio",
       "Motor de permisos y personalización de marca",
       "Paquetes de procesos y manuales","Capacidad de implementación del equipo"],
   ch=["Relación directa","Referidos del sector",
       "Conversión desde clientes que ya usan las plataformas"],
   cost=["<strong>Implementación — el componente principal</strong>",
         "Acompañamiento operativo continuo","Desarrollo del canal",
         "Legal y contratación","Plataformas"],
   rev=["Cuota de incorporación",
        "Regalía sobre la comisión efectivamente cobrada",
        "Plataformas después del período incluido",
        "Migraciones complejas y oficinas adicionales, a la medida",
        "<strong>Sin fondo de marca</strong>"]))
 + '<h2 style="margin-top:5mm"><span class="snum">02</span>La restricción real: capacidad de acompañar</h2>'
 + '<p class="small">Este modelo es <strong>intensivo en acompañamiento</strong>. Cada socio consume '
   'tiempo de implementación y de asesoría que de otro modo atendería a otros clientes.</p>'
 + '<div class="callout gold">Por eso incorporamos <strong>pocos socios a la vez y de forma deliberada</strong>. '
   'Un socio bien implementado se convierte en referencia; un socio mal acompañado daña justamente la '
   'confianza que el modelo necesita para crecer. <strong>Preferimos ir despacio y hacerlo bien.</strong></div>'
 + '<h2 style="margin-top:3mm"><span class="snum">03</span>Lo que está en construcción</h2>'
 + '<p class="small soft">El costo real de acompañamiento por socio se está midiendo con los primeros '
   'casos · la estructura de regalía requiere diseño de contrato y asesoría legal local antes de firmar · '
   'y hay una conversación honesta pendiente: <strong>cómo garantizar a una firma independiente que la '
   'plataforma es neutral</strong>, siendo que el mismo grupo opera una marca de franquicia. La respuesta '
   'está en la separación técnica y contractual de la información, y se documenta explícitamente.</p>'
 + simple("En una frase: <strong>es para la inmobiliaria que quiere nuestra maquinaria sin dejar de ser "
   "ella misma.</strong> Aporta menos que una franquicia porque no usa nuestra marca. Nos permite llegar "
   "a firmas buenas y establecidas que nunca aceptarían franquiciarse — y por eso mismo vamos despacio: "
   "cada socio requiere acompañamiento real."),
)
