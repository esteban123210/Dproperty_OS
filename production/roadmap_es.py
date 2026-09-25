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
  "B_RealEstate<br>24 sept 2026<br>v1.0")

+ '<h2><span class="snum">00</span>Por qué este orden y no otro</h2>'
+ '<div class="cols2">'
+ '<div><p class="small">La secuencia no es arbitraria. Empezamos por GoHighLevel por cinco razones '
  'que se refuerzan:</p>'
+ '<p class="small"><strong>1 · Es lo más barato y lo más rápido.</strong> Semanas, no meses. '
  'Miles, no cientos de miles.</p>'
+ '<p class="small"><strong>2 · Resuelve dolor de hoy.</strong> El equipo comercial gana velocidad de '
  'respuesta y deja de perder prospectos esta misma semana.</p>'
+ '<p class="small"><strong>3 · Genera el dato que BluePrint necesita.</strong> No se puede construir '
  'un sistema de gestión sin saber cómo se comporta la operación real.</p>'
+ '<p class="small"><strong>4 · Valida la Biblioteca de Procesos antes de codificarla.</strong> '
  'Corregir un proceso en GoHighLevel cuesta una tarde. Corregirlo en software construido cuesta '
  'decenas de miles.</p></div>'
+ '<div><p class="small"><strong>5 · Reduce el riesgo de BluePrint.</strong> Aprendemos el flujo '
  'verdadero antes de pagar por construirlo. Esta es la razón más importante.</p>'
+ '<div class="callout gold" style="margin-top:2mm"><strong>El principio:</strong> aprender barato '
  'antes de construir caro. Cada fase compra información que hace más segura la siguiente.</div>'
+ '<p class="small" style="margin-top:2mm"><strong>La franquicia arranca en paralelo desde el mes 2</strong> '
  'porque el trabajo legal y de marca tiene plazos largos y <strong>no depende del software</strong>. '
  'Si esperamos a tener BluePrint, perdemos seis meses de reloj legal.</p>'
+ '<p class="small"><strong>VAULTED va al final y bloqueado.</strong> Es la apuesta de mayor potencial '
  'y menor evidencia; no consume capital hasta que BluePrint esté estable.</p></div>'
+ '</div>'

+ '<h2 style="margin-top:4mm"><span class="snum">01</span>Vista general</h2>'
+ '<div class="bar"><i class="on" style="width:17%"></i><i class="next" style="width:50%"></i>'
  '<i class="later" style="width:33%"></i></div>'
+ table(["Fase","Qué","Cuándo","Capital"], [
    ["<strong>1</strong>","GoHighLevel — Dproperty + DpropertyLiving","Semana 1–10","<strong>$12k–22k</strong>"],
    ["<strong>2A</strong>","BluePrint — descubrimiento, prototipo, cotizaciones","Mes 3–4","$15k–35k"],
    ["<strong>2B</strong>","BluePrint — MVP núcleo","Mes 5–8","$90k–180k"],
    ["<strong>2C</strong>","BluePrint — cumplimiento, comisiones, Copiloto","Mes 9–12","$70k–140k"],
    ["<strong>2D</strong>","Building Blocks — plataforma y dimensionamiento","Mes 4–6","$10k–20k"],
    ["<strong>2E</strong>","Building Blocks — currículo base y certificación","Mes 6–10","$15k–35k"],
    ["<strong>3</strong>","Franquicia — legal, marca, estructura (paralelo)","Mes 2–12","$69k–180k"],
    ["<strong>4</strong>","VAULTED — bloqueado hasta meta de 90 días","Mes 13+","por definir"],
    ["","<strong>Total de proyecto directo</strong>","18 meses","<strong>$281k–612k</strong>"]], None, 3)
+ '<p class="note">Contra el sobre de <strong>$950k de capitalización</strong> y el plan operativo de '
  '<strong>$800k a 18 meses</strong>. La diferencia entre el costo directo de proyecto y el plan '
  'operativo es equipo, nómina y capital de trabajo.</p>'

+ '<h2 style="margin-top:4mm"><span class="snum">02</span>Fase 1 — GoHighLevel · Semanas 1 a 10</h2>'
+ '<p class="small"><strong>Dos sub-cuentas, un solo motor.</strong> Dproperty habla de rendimiento e '
  'inversión. DpropertyLiving habla de estilo de vida y hogar. <strong>Mismo inventario, dos '
  'narrativas.</strong> Se construyen a la vez porque comparten configuración base.</p>'

+ '<div class="tl">'
+ phase("Sem 1–2","Fundaciones","Cuentas, dominios y el camino crítico",
  '<p class="small">Cuenta <strong>Agency Pro</strong> ($497/mes) con SaaS Mode · dos sub-cuentas · '
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
         "B_RealEstate<br>24 sept 2026", small=True)

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

+ '<h2 style="margin-top:3mm"><span class="snum">03</span>Capital de la Fase 1</h2>'
+ table(["Concepto","Monto"], [
    ["GoHighLevel Agency Pro — 3 meses","$1,491"],
    ["Números telefónicos y mensajería — 3 meses","~$900"],
    ["Implementación especializada en GoHighLevel","$6,000–12,000"],
    ["Producción de contenido inicial — 30 días × 2 marcas","$2,500–5,000"],
    ["Diseño de páginas de aterrizaje","$1,000–2,500"],
    ["Dominios y correo","~$300"],
    ["<strong>Total Fase 1</strong>","<strong>$12,000–22,000</strong>"]], None, 1)
+ '<p class="note">Si la implementación se hace internamente en lugar de contratar un especialista, baja '
  'a <strong>$5,000–9,000</strong> — pero cuesta entre 6 y 8 semanas de tiempo propio. Recomendación: '
  '<strong>contratar al especialista</strong>. El tiempo del fundador vale más en la conversación de '
  'franquicia y de capital.</p>'

+ '<h2 style="margin-top:3mm"><span class="snum">04</span>Fase 2 — BluePrint y Building Blocks</h2>'
+ '<div class="tl">'
+ phase("Mes 3–4","2A · $15k–35k","Descubrimiento, prototipo y dos cotizaciones",
  '<p class="small">Mapas de recorrido, datos y permisos · prototipo clickeable del '
  '<strong>flujo dorado</strong>: ingreso calificado → expediente → documentos y cumplimiento → '
  'aprobación → cierre → cálculo de comisión → reporte de gestión · arquitectura técnica · '
  '<strong>dos propuestas de desarrollo independientes</strong> con equipo nombrado, hitos, derechos de '
  'propiedad intelectual, soporte y exclusiones.</p>'
  '<div class="callout" style="margin:1.5mm 0"><strong>Meta de la etapa:</strong> no se libera capital de '
  'construcción hasta tener <strong>dos cotizaciones comparables</strong>. Es una brecha de evidencia '
  'declarada hoy.</div>')
+ phase("Mes 5–8","2B · $90k–180k","MVP núcleo",
  '<p class="small">Onboarding y roles · ingreso de oportunidad calificada · expediente de transacción · '
  'tareas · documentos y versiones · auditoría · reportes base. <strong>Piloto interno en Dproperty '
  'primero</strong>, después socios de diseño externos.</p>'
  '<p class="small"><strong>Condición de aprobación:</strong> un flujo corre de punta a punta '
  '<strong>sin que una hoja de cálculo paralela sea la autoridad</strong>.</p>')
+ phase("Mes 9–12","2C · $70k–140k","Cumplimiento, comisiones y Copiloto",
  '<p class="small">Motor de cumplimiento y aprobaciones · <strong>snapshots de cálculo de comisión</strong> · '
  'conector con GoHighLevel (aquí se cierra el traspaso definido en la Fase 1) · Copiloto con permisos '
  'para consulta y borradores · endurecimiento para producción y pruebas de seguridad.</p>'
  '<p class="small"><strong>Meta:</strong> 5 socios de diseño y 3 conversiones pagadas.</p>')
+ phase("Mes 4–6","2D · $10k–20k","Building Blocks — plataforma",
  '<p class="small"><strong>Cotización formal del LMS</strong> (mercado: $8k–$25k/año) · '
  '<strong>dimensionar el currículo base</strong> — hoy el rango de construcción es de $7k a $48k, '
  'siete veces de amplitud, porque nunca se contó cuántos módulos son · montaje de plataforma e '
  'integración con BluePrint.</p>')
+ phase("Mes 6–10","2E · $15k–35k","Building Blocks — currículo y certificación",
  '<p class="small">Producción del currículo base de incorporación (12–20 módulos estimados) · '
  'evaluaciones · certificación con vencimiento y renovación · la <strong>habilitación de permisos</strong> '
  'desde BluePrint según certificación vigente.</p>'
  '<div class="callout gold" style="margin:1.5mm 0"><strong>No expandir el catálogo</strong> más allá de '
  'la incorporación base hasta demostrar enganche real disparado por señales de BluePrint. El año 1 de '
  'Building Blocks pierde dinero en todos los escenarios; no agravarlo produciendo contenido que nadie '
  'pidió.</div>')
+ '</div>',

# ═══════════════════════════════ PÁGINA 3 — FASE 3 ASESORES Y CAPITAL
masthead("Ruta de Desarrollo", "Fase 3 · Franquicia, asesores y tramos de capital", None,
         "B_RealEstate<br>24 sept 2026", small=True)

+ '<h2><span class="snum">05</span>Fase 3 — Franquiciar la empresa · en paralelo desde el mes 2</h2>'
+ '<p class="small">Arranca <strong>antes</strong> de que BluePrint esté listo porque el reloj legal y de '
  'marca es largo y no depende del software. Cada frente necesita un especialista distinto — '
  '<strong>ningún abogado generalista cubre todo esto</strong>.</p>'
+ table(["Frente","Quién lo debe ver","Cuándo","Costo estimado"], [
    ["<strong>Estructura y contrato de franquicia</strong><br><span class='soft'>Documento de divulgación, "
     "contrato maestro, derechos territoriales, terminación, piso de regalía</span>",
     "Abogado <strong>especialista en franquicias</strong> — Panamá y cada mercado objetivo","Mes 2–5","$15k–40k"],
    ["<strong>Registro de marca</strong><br><span class='soft'>Dproperty, DpropertyLiving, BluePrint, "
     "BlankCRM, Building Blocks, VAULTED, B_</span>",
     "Abogado de <strong>propiedad intelectual</strong> con alcance multi-jurisdicción","Mes 2–4","$5k–15k"],
    ["<strong>Estructura fiscal y corporativa</strong><br><span class='soft'>Entidad, regalías "
     "transfronterizas, precios de transferencia, retenciones</span>",
     "<strong>Fiscalista internacional</strong> + contador","Mes 3–5","$8k–20k"],
    ["<strong>Licencias de corretaje</strong><br><span class='soft'>Quién puede cobrar comisión y bajo "
     "qué licencia en cada mercado</span>",
     "Abogado local por mercado · <strong>ACOBIR</strong> en Panamá","Mes 3–6","$3k–10k"],
    ["<strong>Protección de datos</strong><br><span class='soft'>Ley 81 de Panamá, Ley 1581 de Colombia, "
     "acuerdos de tratamiento, datos entre inquilinos</span>",
     "Abogado de <strong>privacidad y datos</strong>","Mes 4–6","$5k–12k"],
    ["<strong>Modelo financiero</strong><br><span class='soft'>Revisión independiente antes de mostrarlo "
     "a inversionistas o franquiciados</span>",
     "<strong>Consultor financiero</strong> independiente","Mes 3–4","$5k–15k"],
    ["<strong>Desarrollo de franquicia</strong><br><span class='soft'>Perfil del franquiciado, proceso de "
     "reclutamiento, materiales de venta, validación del paquete</span>",
     "<strong>Consultor de desarrollo de franquicias</strong>","Mes 5–8","$10k–25k"],
    ["<strong>Auditoría de manuales</strong><br><span class='soft'>Los manuales resisten un estándar "
     "multinacional</span>","Auditor de <strong>operaciones y calidad</strong>","Mes 6–8","$4k–10k"],
    ["<strong>Seguridad de la información</strong><br><span class='soft'>Obligatorio antes de que "
     "BluePrint toque datos de clientes en producción</span>",
     "<strong>Auditor de seguridad</strong> / pentest","Mes 9–11","$8k–18k"],
    ["<strong>PLD / AML</strong><br><span class='soft'>Solo si VAULTED avanza o si hay flujo de fondos</span>",
     "Consultor de <strong>cumplimiento PLD</strong>","Mes 8–12","$6k–15k"],
    ["","","<strong>Total Fase 3</strong>","<strong>$69k–180k</strong>"]], None, 3)
+ '<div class="callout gold"><strong>Prioridad absoluta dentro de la Fase 3:</strong> el '
  '<strong>registro de marca</strong> arranca primero. Es lo más barato, lo más rápido y lo único '
  'irreversible si alguien más registra los nombres antes. Hoy la posición de marca está '
  '<strong>sin verificar</strong> <span class="chip">[R]</span> para todos los nombres del portafolio.</div>'

+ '<h2 style="margin-top:4mm"><span class="snum">06</span>Tramos de capital atados a metas</h2>'
+ '<p class="small">El capital se libera contra evidencia, no contra calendario. Sobre de '
  '<strong>$950k</strong>; plan operativo de <strong>$800k a 18 meses</strong>.</p>'
+ table(["Tramo","Monto","Qué financia","Meta para liberar el siguiente"], [
    ["<strong>1</strong>","<strong>$120k</strong>",
     "Fase 1 completa · descubrimiento y prototipo de BluePrint · inicio de marca y legal de franquicia",
     "GoHighLevel en producción con el equipo usándolo · prototipo validado · <strong>dos cotizaciones "
     "de desarrollo</strong> · marcas presentadas"],
    ["<strong>2</strong>","<strong>$280k</strong>",
     "MVP núcleo de BluePrint · plataforma de Building Blocks · contrato de franquicia redactado",
     "Un flujo completo <strong>sin hoja de cálculo paralela</strong> · piloto interno en Dproperty "
     "funcionando · contrato listo para firma"],
    ["<strong>3</strong>","<strong>$250k</strong>",
     "Cumplimiento, comisiones y Copiloto · currículo base · auditoría de seguridad · primeros socios",
     "<strong>5 socios de diseño y 3 conversiones pagadas</strong> · sin hallazgo de seguridad crítico · "
     "primer franquiciado o socio firmado y pagado"],
    ["<strong>4</strong>","<strong>$150k</strong>",
     "Escala de canales · segundo mercado · evaluación de VAULTED",
     "Economía unitaria observada por cohorte, no modelada"]], None, 1)
+ '<p class="note"><strong>Regla de la meta a 90 días:</strong> sin automatización de marketplace ni '
  'expansión geográfica antes de la revisión. Y <strong>ser un producto con nombre no otorga '
  'presupuesto</strong> — BluePrint recibe el capital de ingeniería; los demás se lo ganan demostrando '
  'enganche o demanda propia.</p>'

+ simple([
  "<strong>Primero GoHighLevel</strong> (2 meses y medio, $12k–22k). Montamos el CRM y las redes de "
  "Dproperty y DpropertyLiving, con todo automatizado para que el equipo de ventas deje de perder "
  "prospectos. Es barato, rápido y nos enseña cómo opera el negocio de verdad.",
  "<strong>Con eso andando, empezamos BluePrint</strong> (mes 3 al 12, $175k–355k). Se construye en tres "
  "pedazos y cada pedazo se paga solo si el anterior funcionó.",
  "<strong>Building Blocks va al lado de BluePrint</strong> (mes 4 al 10, $25k–55k). Primero cotizamos la "
  "plataforma y contamos cuántos cursos son — hoy no lo sabemos y por eso el presupuesto varía 7 veces.",
  "<strong>La franquicia arranca desde el mes 2, en paralelo.</strong> No hay que esperar el software: "
  "los abogados y el registro de marca toman meses. <strong>Lo primero de todo es registrar las marcas</strong> "
  "— es barato y es lo único que no se puede deshacer si alguien nos gana el nombre.",
  "<strong>VAULTED se queda para el final y a propósito.</strong> Es la apuesta grande pero no gastamos "
  "en ella hasta que BluePrint esté estable.",
  "<strong>El dinero entra en cuatro tramos</strong> ($120k, $280k, $250k, $150k) y cada tramo se libera "
  "solo cuando el anterior demostró algo concreto. Si algo no funciona, nos detenemos ahí y no perdimos "
  "el resto."]),
]
