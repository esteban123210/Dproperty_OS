# -*- coding: utf-8 -*-
"""Ruta de desarrollo: secuencia, tiempos, capital y asesores."""

from brand import masthead, simple, table

def phase(when, sub, title, body):
    return (f'<div class="phase"><div class="when"><b>{when}</b>{sub}</div>'
            f'<div><h4>{title}</h4>{body}</div></div>')

ROADMAP = [

# ═══════════════════════════════ PÁGINA 1 — ESTRATEGIA Y FASE 1
masthead("Ruta de Desarrollo", "De dónde partimos y en qué orden",
  "Secuencia, tiempos, capital por etapa y qué especialista se necesita en cada frente.",
  "B_RealEstate<br>25 sept 2026<br>v3.0")

+ '<h2><span class="snum">00</span>Por qué este orden y no otro</h2>'
+ '<div class="cols2">'
+ '<div><p class="small">La secuencia no es arbitraria. Empezamos por GoHighLevel por cinco razones '
  'que se refuerzan:</p>'
+ '<p class="small"><strong>1 · Es lo más rápido de poner en marcha.</strong> Se mide en semanas, no '
  'en trimestres, y con una inversión modesta frente al resto del plan.</p>'
+ '<p class="small"><strong>2 · Resuelve dolor de hoy.</strong> El equipo comercial gana velocidad de '
  'respuesta y deja de perder prospectos esta misma semana.</p>'
+ '<p class="small"><strong>3 · Genera el dato que BluePrint necesita.</strong> No se puede construir '
  'un sistema de gestión sin conocer primero cómo se comporta la operación real.</p>'
+ '<p class="small"><strong>4 · Valida la Biblioteca de Procesos antes de codificarla.</strong> '
  'Ajustar un proceso en GoHighLevel toma una tarde. Ajustarlo en software ya construido cuesta '
  'mucho más, en dinero y en tiempo.</p></div>'
+ '<div><p class="small"><strong>5 · Reduce el riesgo de BluePrint.</strong> Aprendemos el flujo '
  'verdadero antes de pagar por construirlo. Esta es la razón más importante.</p>'
+ '<div class="callout gold" style="margin-top:2mm"><strong>El principio:</strong> aprender barato '
  'antes de construir. Cada fase entrega información que hace más segura la siguiente.</div>'
+ '<p class="small" style="margin-top:2mm"><strong>La franquicia arranca en paralelo desde el mes 2</strong> '
  'porque el trabajo legal y de marca tiene plazos largos y <strong>no depende del software</strong>. '
  'Si esperamos a tener BluePrint, perdemos seis meses de reloj legal.</p>'
+ '<p class="small"><strong>VAULTED va al final y bloqueado.</strong> Es la apuesta de mayor potencial '
  'y menor evidencia; no consume capital hasta que BluePrint esté estable.</p></div>'
+ '</div>'

+ '<h2 style="margin-top:4mm"><span class="snum">01</span>Vista general</h2>'
+ '<div class="bar"><i class="on" style="width:17%"></i><i class="next" style="width:50%"></i>'
  '<i class="later" style="width:33%"></i></div>'
+ table(["Fase","Qué","Cuándo","Inversión relativa"], [
    ["<strong>1</strong>","GoHighLevel — Dproperty + DpropertyLiving","Semana 1–10","Baja"],
    ["<strong>2A</strong>","BluePrint — descubrimiento, prototipo y cotizaciones","Mes 3–4","Baja"],
    ["<strong>2B</strong>","BluePrint — núcleo del producto","Mes 5–8","<strong>Alta</strong>"],
    ["<strong>2C</strong>","BluePrint — finanzas, procesos y roles agénticos","Mes 9–12","<strong>Alta</strong>"],
    ["<strong>2D</strong>","Building Blocks — plataforma y alcance del currículo","Mes 4–6","Baja"],
    ["<strong>2E</strong>","Building Blocks — currículo base y certificación","Mes 6–10","Media"],
    ["<strong>3</strong>","Franquicia — legal, marca y estructura (en paralelo)","Mes 2–12","Media"],
    ["<strong>4</strong>","VAULTED — en pausa hasta consolidar BluePrint","Mes 13+","Por definir"]], None, 3)
+ '<p class="note">El detalle de la inversión por etapa y el calendario de desembolsos se presentan en el modelo financiero, en documento aparte. <strong>Cada etapa se financia contra el resultado de la anterior</strong>, no contra el calendario.</p>'


,

# ═══════════════════════════════ PÁGINA 2 — FASE 1 ARRANQUE
masthead("Ruta de Desarrollo", "Fase 1 · GoHighLevel", None,
         "B_RealEstate<br>25 sept 2026", small=True)
+ '<h2><span class="snum">02</span>Fase 1 — GoHighLevel · Semanas 1 a 10</h2>'
+ '<p class="small"><strong>Dos sub-cuentas, un solo motor.</strong> Dproperty habla de rendimiento e '
  'inversión. DpropertyLiving habla de estilo de vida y hogar. <strong>Mismo inventario, dos '
  'narrativas.</strong> Se construyen a la vez porque comparten configuración base.</p>'

+ '<div class="tl">'
+ phase("Sem 1–2","Fundaciones","Cuentas, dominios y el camino crítico",
  '<p class="small">Cuenta de agencia con modo de reventa habilitado · dos sub-cuentas · '
  'dominios y subdominios · <strong>autenticación de correo SPF, DKIM y DMARC</strong> (sin esto, todo '
  'lo demás cae en spam) · números telefónicos y registro A2P donde aplique · conexión de Instagram, '
  'Facebook, LinkedIn y Google Business Profile.</p>'
  '<div class="callout" style="margin:1.5mm 0"><strong>Camino crítico — empezar el día 1:</strong> la '
  'verificación de <strong>WhatsApp Business API</strong> con Meta toma entre <strong>1 y 3 semanas</strong> '
  'y no se puede acelerar. Si arranca tarde, retrasa todo el lanzamiento.</div>')
+ phase("Sem 2–4","CRM núcleo","Taxonomía, pipelines y la definición del traspaso",
  '<p class="small"><strong>Campos personalizados:</strong> presupuesto, zona, tipo de operación, moneda, '
  'financiamiento, horizonte de compra, fuente, idioma. <strong>Etiquetas y segmentación</strong> por '
  'marca e intención.</p>'
  '<p class="small"><strong>Un pipeline por proceso de la Biblioteca:</strong> Prospectos · Preventa '
  '(Lista Cero) · Venta mercado secundario · Cesión · Alquiler larga estadía · Administración de '
  'propiedades. Cada etapa con <strong>criterio de salida explícito</strong>, no subjetivo.</p>'
  '<p class="small"><strong>Asignación:</strong> round-robin, por zona o por especialidad, con reasignación '
  'automática si no hay contacto.</p>'
  '<div class="callout gold" style="margin:1.5mm 0"><strong>Definir aquí la «oportunidad calificada».</strong> '
  'Es el punto exacto donde después BluePrint tomará el control. Definirlo ahora, aunque BluePrint no '
  'exista, evita rehacer todo el embudo el año que viene.</div>')
+ phase("Sem 3–5","Automatización","Quitarle trabajo operativo al equipo comercial",
  '<p class="small"><strong>Velocidad de respuesta:</strong> contacto automático en menos de 5 minutos, '
  'asignación inmediata, notificación al asesor por WhatsApp y push. Es la automatización con mayor '
  'retorno demostrado en venta inmobiliaria.</p>'
  '<p class="small"><strong>Secuencias de maduración</strong> distintas por marca: inversión (rendimiento, '
  'absorción, salida) vs vivienda (zona, espacio, escuelas, comunidad).</p>'
  '<p class="small"><strong>Además:</strong> reactivación de fríos a 30/60/90 días · recordatorios de '
  'seguimiento con escalamiento al supervisor · solicitud automática de documentos · confirmación y '
  'recordatorio de citas · encuesta y reseña post-visita y post-cierre · alerta interna por oportunidad '
  'estancada · <strong>reporte semanal automático a la dirección comercial</strong>.</p>')
+ '</div>',

# ═══════════════════════════════ PÁGINA 2 — FASE 1 (cont.) Y FASE 2
masthead("Ruta de Desarrollo", "Fase 1 continuación y Fase 2", None,
         "B_RealEstate<br>25 sept 2026", small=True)

+ '<div class="tl">'
+ phase("Sem 4–6","Contenido y redes","Dos calendarios, dos tonos de voz",
  '<p class="small"><strong>Calendario editorial por marca.</strong> Programación nativa desde '
  'GoHighLevel a <strong>Instagram</strong> (feed, stories, reels), <strong>Facebook</strong>, '
  '<strong>LinkedIn</strong> y <strong>estados de WhatsApp</strong>.</p>'
  + table(["Marca","Canales prioritarios","Cadencia sugerida","Tono"], [
      ["<strong>Dproperty</strong>","LinkedIn · Instagram feed","4–5 por semana",
       "Rendimiento, datos, análisis de mercado, casos de inversión"],
      ["<strong>DpropertyLiving</strong>","Instagram (feed + stories) · Facebook · WhatsApp",
       "6–7 por semana + stories diarios","Estilo de vida, zona, espacios, comunidad, recorridos"]], None, 99)
  + '<p class="small"><strong>Plantillas por tipo de publicación:</strong> inventario nuevo, avance de '
  'obra, testimonio, contenido educativo, cierre celebrado, recorrido de propiedad, comparativo de zona. '
  'Biblioteca de activos con flujo de aprobación.</p>')
+ phase("Sem 5–7","Captación","Formularios, páginas y agenda",
  '<p class="small">Formularios de calificación (los campos alimentan directamente la definición de '
  'oportunidad calificada) · páginas de aterrizaje por proyecto e inventario · '
  '<strong>catálogo de inventario para usuario final</strong> en DpropertyLiving · calendarios de cita '
  'por asesor con confirmación automática · widget de chat y WhatsApp click-to-chat · atribución de '
  'campaña de punta a punta.</p>')
+ phase("Sem 6–8","Datos y equipo","Migración, tableros y capacitación",
  '<p class="small">Migración de la base existente con <strong>limpieza y deduplicación</strong> '
  '(no migrar basura) · tableros de embudo, velocidad, fuente y desempeño por asesor · '
  'dos sesiones de capacitación más manual de uso · certificación básica obligatoria antes de dar acceso.</p>')
+ phase("Sem 8–10","Piloto y lanzamiento","Primero dos asesores, luego todos",
  '<p class="small">Piloto con 2–3 asesores durante dos semanas · corrección de fricciones reales · '
  'lanzamiento completo. <strong>Nunca lanzar a todo el equipo de golpe:</strong> una mala primera '
  'experiencia cuesta meses de adopción.</p>')
+ '</div>'

,

# ═══════════════════════════════ PÁGINA 4 — CAPITAL F1 Y FASE 2
masthead("Ruta de Desarrollo", "Qué hace falta para la Fase 1", None,
         "B_RealEstate<br>25 sept 2026", small=True)
+ '<h2><span class="snum">03</span>Qué hace falta para la Fase 1</h2>'
+ table(["Componente","Qué implica"], [
    ["Licencia de la plataforma","Una sola cuenta de agencia, con sub-cuentas para ambas marcas."],
    ["Números y mensajería","Líneas telefónicas y verificación de WhatsApp Business."],
    ["Implementación especializada","Un especialista en GoHighLevel que arme la configuración completa."],
    ["Producción de contenido inicial","Plantillas y primer mes de calendario editorial para cada marca."],
    ["Páginas de aterrizaje","Diseño de las páginas por proyecto e inventario."],
    ["Dominios y correo","Configuración técnica y autenticación de envío."]], None, 99)
+ '<p class="note">Es la fase de menor inversión de todo el plan y la que más rápido se nota en el día a día del equipo comercial. <strong>Recomendación: contratar al especialista</strong> en lugar de hacerlo internamente — el tiempo del fundador rinde más en la conversación de franquicia y de capital que configurando embudos.</p>',

# ═══════════════════════════════ PÁGINA 5 — FASE 2 DETALLE
masthead("Ruta de Desarrollo", "Fase 2 · BluePrint y Building Blocks", None,
         "B_RealEstate<br>25 sept 2026", small=True)
+ '<h2><span class="snum">04</span>Fase 2 — BluePrint y Building Blocks</h2>'
+ '<div class="tl">'
+ phase("Mes 3–4","2A · Diseño","Descubrimiento, prototipo y dos cotizaciones",
  '<p class="small">Mapas de recorrido, datos y permisos · prototipo clickeable del '
  '<strong>flujo dorado</strong>: ingreso calificado → expediente → documentos y cumplimiento → '
  'aprobación → cierre → cálculo de comisión → reporte de gestión · arquitectura técnica · '
  '<strong>dos propuestas de desarrollo independientes</strong> con equipo nombrado, hitos, derechos de '
  'propiedad intelectual, soporte y exclusiones.</p>'
  '<div class="callout" style="margin:1.5mm 0"><strong>Meta de la etapa:</strong> no se libera capital de '
  'construcción hasta tener <strong>dos cotizaciones comparables</strong>. Es una brecha de evidencia '
  'declarada hoy.</div>')
+ phase("Mes 5–8","2B · Núcleo","MVP núcleo",
  '<p class="small">Onboarding y roles · ingreso de oportunidad calificada · expediente de transacción · '
  'tareas · documentos y versiones · auditoría · reportes base. <strong>Piloto interno en Dproperty '
  'primero</strong>, después socios de diseño externos.</p>'
  '<p class="small"><strong>Condición de aprobación:</strong> un flujo corre de punta a punta '
  '<strong>sin que una hoja de cálculo paralela sea la autoridad</strong>.</p>')
+ phase("Mes 9–12","2C · Gerencia","Cumplimiento, comisiones y Copiloto",
  '<p class="small">Motor de cumplimiento y aprobaciones · <strong>snapshots de cálculo de comisión</strong> · '
  'conector con GoHighLevel (aquí se cierra el traspaso definido en la Fase 1) · Copiloto con permisos '
  'para consulta y borradores · endurecimiento para producción y pruebas de seguridad.</p>'
  '<p class="small"><strong>Meta:</strong> 5 socios de diseño y 3 conversiones pagadas.</p>')
+ phase("Mes 4–6","2D · Plataforma","Building Blocks — plataforma",
  '<p class="small"><strong>Cotización formal de la plataforma de formación</strong> · '
  '<strong>definir el alcance del currículo base</strong> — cuántos módulos, para qué roles y '
  'con qué profundidad; hoy es la variable más abierta del plan · montaje de plataforma e '
  'integración con BluePrint.</p>')
+ phase("Mes 6–10","2E · Currículo","Building Blocks — currículo y certificación",
  '<p class="small">Producción del currículo base de incorporación (12–20 módulos estimados) · '
  'evaluaciones · certificación con vencimiento y renovación · la <strong>habilitación de permisos</strong> '
  'desde BluePrint según certificación vigente.</p>'
  '<div class="callout gold" style="margin:1.5mm 0"><strong>No expandir el catálogo</strong> más allá de '
  'la incorporación base hasta ver demanda real derivada desde BluePrint. Es un producto que madura '
  'despacio: conviene construir lo que se va a usar y ampliar después.</div>')
+ '</div>',

# ═══════════════════════════════ PÁGINA 3 — FASE 3 ASESORES Y CAPITAL
masthead("Ruta de Desarrollo", "Fase 3 · Franquicia, asesores y tramos de capital", None,
         "B_RealEstate<br>25 sept 2026", small=True)

+ '<h2><span class="snum">05</span>Fase 3 — Franquiciar la empresa · en paralelo desde el mes 2</h2>'
+ '<p class="small">Arranca <strong>antes</strong> de que BluePrint esté listo porque el reloj legal y de '
  'marca es largo y no depende del software. Cada frente necesita un especialista distinto — '
  '<strong>ningún abogado generalista cubre todo esto</strong>.</p>'
+ table(["Frente","Quién lo debe ver","Cuándo"], [
    ["<strong>Estructura y contrato de franquicia</strong><br><span class='soft'>Documento de divulgación, "
     "contrato maestro, derechos territoriales, terminación, piso de regalía</span>",
     "Abogado <strong>especialista en franquicias</strong> — Panamá y cada mercado objetivo","Mes 2–5"],
    ["<strong>Registro de marca</strong><br><span class='soft'>Dproperty, DpropertyLiving, BluePrint, "
     "BlankCRM, Building Blocks, VAULTED, B_</span>",
     "Abogado de <strong>propiedad intelectual</strong> con alcance multi-jurisdicción","Mes 2–4"],
    ["<strong>Estructura fiscal y corporativa</strong><br><span class='soft'>Entidad, regalías "
     "transfronterizas, precios de transferencia, retenciones</span>",
     "<strong>Fiscalista internacional</strong> + contador","Mes 3–5"],
    ["<strong>Licencias de corretaje</strong><br><span class='soft'>Quién puede cobrar comisión y bajo "
     "qué licencia en cada mercado</span>",
     "Abogado local por mercado · <strong>ACOBIR</strong> en Panamá","Mes 3–6"],
    ["<strong>Protección de datos</strong><br><span class='soft'>Ley 81 de Panamá, Ley 1581 de Colombia, "
     "acuerdos de tratamiento, datos entre inquilinos</span>",
     "Abogado de <strong>privacidad y datos</strong>","Mes 4–6"],
    ["<strong>Modelo financiero</strong><br><span class='soft'>Revisión independiente antes de mostrarlo "
     "a inversionistas o franquiciados</span>",
     "<strong>Consultor financiero</strong> independiente","Mes 3–4"],
    ["<strong>Desarrollo de franquicia</strong><br><span class='soft'>Perfil del franquiciado, proceso de "
     "reclutamiento, materiales de venta, validación del paquete</span>",
     "<strong>Consultor de desarrollo de franquicias</strong>","Mes 5–8"],
    ["<strong>Auditoría de manuales</strong><br><span class='soft'>Los manuales resisten un estándar "
     "multinacional</span>","Auditor de <strong>operaciones y calidad</strong>","Mes 6–8"],
    ["<strong>Seguridad de la información</strong><br><span class='soft'>Obligatorio antes de que "
     "BluePrint toque datos de clientes en producción</span>",
     "<strong>Auditor de seguridad</strong> / pentest","Mes 9–11"],
    ["<strong>PLD / AML</strong><br><span class='soft'>Solo si VAULTED avanza o si hay flujo de fondos</span>",
     "Consultor de <strong>cumplimiento PLD</strong>","Mes 8–12"],], None, 99)
+ '<div class="callout gold"><strong>Prioridad absoluta dentro de la Fase 3:</strong> el '
  '<strong>registro de marca</strong> arranca primero. Es lo más barato, lo más rápido y lo único '
  'irreversible si alguien más registra los nombres antes. Hoy la posición de marca está '
  '<strong>pendiente de verificar</strong> para todos los nombres del portafolio.</div>'

,

# ═══════════════════════════════ PÁGINA 7 — TRAMOS DE CAPITAL
masthead("Ruta de Desarrollo", "Tramos de capital atados a metas", None,
         "B_RealEstate<br>25 sept 2026", small=True)
+ '<h2><span class="snum">06</span>Etapas de financiamiento atadas a resultados</h2>'
+ '<p class="small">El financiamiento se libera <strong>contra evidencia, no contra calendario</strong>. Cada etapa tiene una condición concreta que debe cumplirse antes de abrir la siguiente. Los montos se detallan en el modelo financiero.</p>'
+ table(["Etapa","Qué financia","Qué debe demostrarse para abrir la siguiente"], [
    ["<strong>1</strong>","Fase 1 completa · descubrimiento y prototipo de BluePrint · inicio de marca y legal de franquicia",
     "GoHighLevel en producción con el equipo usándolo a diario · prototipo validado con usuarios reales · <strong>dos cotizaciones de desarrollo comparables</strong> · marcas presentadas a registro"],
    ["<strong>2</strong>","Núcleo de BluePrint · plataforma de Building Blocks · contrato de franquicia redactado",
     "Un proceso completo corriendo dentro de BluePrint · piloto interno en Dproperty en uso real · contrato listo para firma con revisión legal"],
    ["<strong>3</strong>","Finanzas, procesos y roles agénticos · currículo base · auditoría de seguridad · primeros socios",
     "Socios de diseño activos y primeras conversiones pagadas · sin hallazgos críticos de seguridad · primer operador de franquicia o socio firmado"],
    ["<strong>4</strong>","Escala de canales · segundo mercado · evaluación de VAULTED",
     "Economía unitaria observada con clientes reales, no modelada"]], None, 99)
+ '<p class="note"><strong>Regla de la revisión a 90 días:</strong> sin automatización de la red ni expansión geográfica antes de esa revisión. Y una disciplina que nos protege: <strong>que un producto exista en el mapa no le otorga presupuesto</strong> — BluePrint concentra la inversión de ingeniería, y los demás la reciben cuando demuestran demanda.</p>'

+ simple([
  "<strong>Primero GoHighLevel</strong> (unas diez semanas). Montamos el CRM y las redes de Dproperty "
  "y DpropertyLiving, con todo automatizado para que el equipo comercial deje de perder oportunidades. "
  "Es rápido, es la inversión más baja del plan y nos enseña cómo opera el negocio de verdad.",
  "<strong>Con eso andando, empezamos BluePrint</strong> (del mes 3 al 12). Se construye en tres etapas "
  "y cada etapa se financia solo si la anterior funcionó.",
  "<strong>Building Blocks va al lado de BluePrint</strong> (del mes 4 al 10). Primero cotizamos la "
  "plataforma y definimos cuántos cursos son — hoy esa es la variable más abierta del plan.",
  "<strong>La franquicia arranca desde el mes 2, en paralelo.</strong> No hay que esperar el software: "
  "los abogados y el registro de marca toman meses. <strong>Lo primero de todo es registrar las "
  "marcas</strong> — es lo más rápido y lo único que no se puede deshacer si alguien más las registra.",
  "<strong>VAULTED se queda para el final, a propósito.</strong> Es la apuesta de mayor potencial y no "
  "consume recursos hasta que BluePrint esté consolidado.",
  "<strong>El financiamiento entra por etapas</strong>, y cada una se abre solo cuando la anterior "
  "demostró algo concreto. Si algo no funciona, nos detenemos ahí sin haber comprometido el resto."]),
]
