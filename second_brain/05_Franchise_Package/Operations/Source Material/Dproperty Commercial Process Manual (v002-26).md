---
title: "Dproperty — Manual de Procesos Comerciales"
document_type: "Ground floor documental, borrador operativo y especificación de evolución hacia el sistema modular"
status: "Base de trabajo — no definitivo, no constituye por sí solo política vigente"
version: "002-26"
last_updated: "2026-06-14"
source_html: "dproperty_procesos_diagrama_ajustado_comite_002-26.html"
source_minutes: "Acta 002-26 — Comité de Ventas Dproperty"
owner: "Dproperty"
output_html: "dproperty_procesos_diagrama.html"
authority_level: "Documento base de construcción; las decisiones aprobadas prevalecen sobre este consolidado"
migration_target: "Arquitectura modular en Commercial Processes"
vault_role: "SOURCE MATERIAL — imported verbatim 2026-07-21. Do not edit. Abstract into the Process Library and manuals per [[../../Manuals System Index]]."
---

# Dproperty — Manual de Procesos Comerciales

> [!IMPORTANT] Naturaleza del documento
> Este archivo es el **ground floor** del futuro sistema documental del Manual de Procesos Comerciales de Dproperty. Reúne en un solo lugar la estructura propuesta, el contenido actualmente disponible, las decisiones conocidas y las instrucciones para construir la versión modular y el HTML final.  
>
> **No es una fuente definitiva de verdad, no reemplaza las actas, aprobaciones escritas, contratos, políticas formalmente aprobadas ni los módulos operativos que se crearán posteriormente.**

> [!NOTE] Cómo debe interpretarse
> El documento puede contener simultáneamente:
> - decisiones formalmente aprobadas;
> - contenido heredado pendiente de reconfirmación;
> - supuestos de trabajo;
> - propuestas estructurales;
> - instrucciones técnicas todavía no implementadas.
>
> Cada elemento deberá clasificarse y validarse durante la migración. Cuando exista conflicto, prevalece siempre la evidencia formal más reciente: acta aprobada, correo de aprobación, contrato, política vigente o decisión registrada.

> [!SUCCESS] Qué sí representa
> Este archivo constituye una base común desde la cual se puede:
> - entender el estado actual del manual;
> - identificar vacíos, inconsistencias y dependencias;
> - separar los procesos en módulos;
> - construir el generador del HTML;
> - validar cada proceso con sus responsables;
> - publicar futuras versiones controladas y reproducibles.

> **Estado de validación parcial:** los ajustes de Alquiler y Administración incorporan los acuerdos del Comité de Ventas documentados en el Acta 002-26, celebrada el 14 de junio de 2026. Esto no implica que todo el resto del manual haya sido validado con el mismo nivel de formalidad.

---

# 0. Sistema de mantenimiento y generación del HTML

## 0.0 Dictamen estructural del Board of Advisors

El Board of Advisors revisó la **estructura**, no la validez del contenido operativo. Participaron cuatro perspectivas:

- **Pragmatic Operator:** prioriza que el sistema pueda implementarse y mantenerse con el equipo y los recursos actuales.
- **Long-Term Strategist:** evalúa escalabilidad, reutilización, versionado y crecimiento futuro.
- **Blunt Skeptic:** identifica contradicciones, duplicaciones, fragilidad técnica y falsas sensaciones de completitud.
- **Wise Mentor:** protege la claridad para los usuarios y separa la experiencia operativa de la experiencia técnica.

### Decisión del board

La arquitectura conceptual queda **aprobada como punto de partida**, pero el archivo monolítico no debe considerarse la estructura final.

El documento actual debe entenderse como:

1. un inventario consolidado del estado actual;
2. un documento de migración;
3. una guía para construir la arquitectura definitiva;
4. una referencia temporal mientras se crean los módulos;
5. una base de discusión para validar cada proceso con sus responsables.

No debe entenderse como:

1. una política corporativa completa y definitivamente aprobada;
2. la versión final del manual;
3. un sustituto de las evidencias de aprobación;
4. el archivo que se editará indefinidamente después de la modularización;
5. una licencia para publicar en el HTML contenido todavía no validado.

### Observaciones estructurales del board

#### 1. El documento mezcla tres capas diferentes

Actualmente conviven:

- la guía para mantener y compilar el sistema;
- el contenido operativo del manual;
- el registro de versión y las decisiones incorporadas.

Estas tres capas deberán separarse progresivamente para evitar duplicaciones y contradicciones.

#### 2. La arquitectura propuesta todavía no equivale a una implementación

El archivo describe carpetas, un manifiesto, scripts y validaciones, pero esas piezas solo serán operativas cuando existan físicamente y puedan producir un HTML reproducible.

Hasta ese momento, toda referencia a automatización debe entenderse como una **especificación de construcción**, no como una capacidad ya disponible.

#### 3. Debe existir una sola ubicación autoritativa para cada dato

Al completar la migración:

- los metadatos vivirán únicamente en el front matter;
- cada proceso vivirá en un solo módulo;
- cada decisión tendrá una sola entrada en el Decision Log;
- el HTML será exclusivamente un producto generado;
- el archivo monolítico será archivado.

#### 4. El manual operativo y la guía técnica deben tener recorridos separados

El equipo comercial debe poder entrar directamente a los procesos, roles y responsabilidades.

La persona que mantiene el sistema debe tener un README independiente con arquitectura, compilación, validaciones y publicación.

#### 5. La consistencia de los módulos es obligatoria

Todos los procesos deberán usar el mismo esquema, incluso cuando una sección no aplique. Esto permitirá:

- comparar procesos;
- detectar vacíos;
- validar automáticamente;
- evitar excepciones innecesarias en el generador;
- construir diferentes salidas desde una misma base.

#### 6. El sistema necesita metadatos legibles por máquinas

No se debe depender exclusivamente de títulos escritos en lenguaje natural para identificar secciones. Los módulos deberán utilizar campos estables como:

```yaml
---
schema_version: 1
id: process5
order: 70
status: draft
content_version: "002-26"
depends_on:
  - process1
triggers:
  - process6
---
```

#### 7. Debe versionarse tanto el contenido como el esquema

La versión del manual indica qué contenido se publicó. La versión del esquema indica cómo debe interpretar los archivos el generador.

Ambas deben mantenerse separadas:

```yaml
schema_version: 1
content_version: "002-26"
```

#### 8. Las relaciones entre procesos deben ser explícitas

Las conexiones no deben depender únicamente de párrafos narrativos. Cada módulo deberá declarar:

- procesos de los que depende;
- procesos que activa;
- entradas necesarias;
- entregables o salidas;
- evidencias que produce.

#### 9. El archivo actual es temporal

Una vez que los módulos, el manifiesto y el generador funcionen y hayan sido validados, este documento deberá trasladarse a:

```text
99_Archive/
└── 2026-06-14_Manual_Migration_Source_002-26.md
```

Su función histórica será demostrar desde qué base se construyó la arquitectura, no seguir compitiendo con los módulos como fuente operativa.

### Pregunta rectora

Antes de convertir cualquier sección en política publicada, se debe responder:

> **¿Este elemento está formalmente aprobado, está pendiente de validación o es solamente un supuesto utilizado para construir el sistema?**

### Acción estructural recomendada

Dividir este documento sin reescribir inicialmente el contenido:

1. mover las instrucciones técnicas a `README.md` y `90_HTML_System/README_BUILD.md`;
2. extraer introducción, leyenda y resumen a `01_Foundation`;
3. extraer cada proceso a su archivo en `02_Processes`;
4. registrar evidencias en `03_Evidence`;
5. crear el manifiesto y el esquema;
6. construir y probar el generador;
7. comparar el HTML generado con el HTML de referencia;
8. validar proceso por proceso;
9. publicar una release;
10. archivar este ground floor.

## 0.1 Principio de trabajo

La carpeta modular de procesos está diseñada para convertirse en la **fuente operativa controlada** una vez construida, validada y aprobada. Este archivo monolítico no cumple todavía esa función: es la base desde la cual se construirá dicha carpeta.

Cuando la migración esté completa, cada proceso se mantendrá en Markdown y el archivo HTML se regenerará cuando cambie cualquier módulo. No se harán cambios permanentes directamente sobre el HTML de salida, porque esos cambios se perderían en la siguiente compilación y crearían una versión paralela no controlada.

La separación recomendada es:

```text
dproperty brain/
└── 05_Operations/
    └── Commercial Processes/
        ├── README.md
        ├── 00_Control/
        │   ├── 00_Manifest.md
        │   ├── 01_Decision_Log.md
        │   ├── 02_Change_Log.md
        │   ├── 03_Missing_Information.md
        │   ├── 04_Release_Log.md
        │   └── 05_Structure_Schema.md
        ├── 01_Foundation/
        │   ├── 01_Introduction.md
        │   ├── 02_Roles_and_RACI.md
        │   ├── 03_Approval_Hierarchy.md
        │   └── 04_Responsibility_Summary.md
        ├── 02_Processes/
        │   ├── 01_Leads.md
        │   ├── 02_Lista_Cero.md
        │   ├── 03_Mercado_Secundario.md
        │   ├── 04_Cesiones.md
        │   ├── 05_Alquiler.md
        │   ├── 06_Administracion_de_Propiedades.md
        │   └── 07_Comisiones.md
        ├── 03_Evidence/
        │   ├── Committee_Minutes/
        │   ├── Written_Approvals/
        │   └── Supporting_Documents/
        ├── 90_HTML_System/
        │   ├── template.html
        │   ├── styles.css
        │   ├── app.js
        │   ├── build_manual.py
        │   ├── validate_manual.py
        │   ├── README_BUILD.md
        │   └── tests/
        ├── 98_Releases/
        │   └── 002-26/
        │       ├── manual_002-26.html
        │       └── release_notes.md
        ├── 99_Output/
        │   └── dproperty_procesos_diagrama.html
        └── 99_Archive/
            └── 2026-06-14_Manual_Migration_Source_002-26.md
```

## 0.2 Función de cada carpeta

| Carpeta o archivo | Función |
|---|---|
| `README.md` | Explica cómo mantener, validar y publicar el sistema; no contiene copias completas de los procesos. |
| `00_Control` | Controla el orden, esquema, decisiones, cambios, releases y vacíos de información. |
| `01_Foundation` | Contiene introducción, definiciones RACI, jerarquía de aprobaciones y resumen de responsabilidades. |
| `02_Processes` | Contiene un archivo Markdown autoritativo por proceso o pestaña del HTML. |
| `03_Evidence` | Conserva actas, aprobaciones escritas y documentos que justifican las decisiones. |
| `90_HTML_System` | Contiene plantilla, estilos, JavaScript, generador, validador y pruebas. |
| `98_Releases` | Conserva cada versión publicada junto con sus notas de release. |
| `99_Output` | Contiene únicamente la compilación vigente para distribución interna. |
| `99_Archive` | Conserva documentos de migración y versiones históricas que ya no deben editarse. |

## 0.3 Regla de actualización

Cada cambio operativo debe seguir esta secuencia:

1. Guardar el acta, correo o decisión que origina el cambio en `03_Committee Minutes` o en la carpeta documental correspondiente.
2. Registrar la decisión en `00_Control/01_Decision_Log.md`.
3. Modificar el archivo del proceso correspondiente en `02_Processes`.
4. Actualizar la matriz RACI, el flujo y los KPIs dentro del mismo módulo; no dejar solo una nota narrativa.
5. Registrar el cambio en `00_Control/02_Change_Log.md`.
6. Actualizar `00_Control/00_Manifest.md` si se creó, eliminó, renombró o reordenó una pestaña.
7. Ejecutar el generador del HTML.
8. Revisar el resultado en escritorio, móvil e impresión/PDF.
9. Publicar únicamente el archivo de `99_Output`.

## 0.4 Formato obligatorio para cada módulo de proceso

Cada archivo de `02_Processes` debe empezar con metadatos consistentes:

```yaml
---
id: process5
nav_label: "5. Alquiler"
order: 50
title: "Proceso 5: Alquiler (Estancias Largas)"
status: active
last_updated: "2026-06-14"
source_decisions:
  - "Acta 002-26 — Comité de Ventas — 2026-06-14"
owner: "Dirección de Operaciones"
---
```

El cuerpo debe usar siempre este orden:

```markdown
# Título del proceso

## Objetivo

## Reglas críticas y excepciones

## Roles específicos del proceso

## Decisiones operativas obligatorias

## Diagrama de flujo
| Paso | Acción | Rol responsable | Descripción / resultado esperado |

## Matriz RACI
| Tarea | R | A | C | I |

## KPIs del proceso
| KPI | Meta / frecuencia |

## Documentos y evidencias obligatorias

## Fuentes y decisiones relacionadas
```

Si una sección no aplica, debe mantenerse con la indicación `No aplica actualmente`, en lugar de eliminarla. Esto facilita comparar procesos y detectar información faltante.

## 0.5 Reglas de identificación

- El campo `id` es permanente. No debe modificarse después de publicar el proceso, porque el JavaScript y los enlaces internos dependen de él.
- `nav_label` controla el texto de la pestaña.
- `order` controla el orden de aparición.
- Los códigos de rol deben coincidir exactamente con la leyenda del manual.
- Cada actividad debe tener un solo **A — Aprobador**. Puede tener varios responsables, consultados o informados.
- Toda excepción debe indicar quién la aprueba y cuál es la evidencia escrita requerida.
- Los montos, porcentajes, SLAs y fechas deben expresarse de forma inequívoca.

## 0.6 Cómo generar el HTML final

El archivo `90_HTML_System/template.html` conserva el diseño actual: encabezado, colores, tarjetas, pestañas, diagramas, tablas RACI, KPIs, diseño responsivo y estilos de impresión. Debe tener dos marcadores:

```html
<!-- NAV_TABS -->
<!-- PROCESS_SECTIONS -->
```

El generador `build_manual.py` debe:

1. Leer `00_Control/00_Manifest.md` para obtener los módulos activos y su orden.
2. Leer el front matter YAML de cada archivo Markdown.
3. Convertir el contenido Markdown a HTML.
4. Convertir la tabla de `Diagrama de flujo` en tarjetas `.flow-step`.
5. Convertir la tabla `Matriz RACI` en `.raci-table` y aplicar las clases de color según los códigos de rol.
6. Convertir la tabla de KPIs en tarjetas `.kpi-card`.
7. Crear un botón `.nav-tab` por módulo usando `nav_label` e `id`.
8. Insertar los botones en `<!-- NAV_TABS -->`.
9. Insertar las secciones en `<!-- PROCESS_SECTIONS -->`.
10. Mantener el CSS y JavaScript del template sin duplicarlos.
11. Escribir un único archivo autocontenido en `99_Output/dproperty_procesos_diagrama.html`.
12. Fallar la compilación si encuentra IDs duplicados, una matriz RACI sin aprobador o columnas obligatorias ausentes.

### Dependencias recomendadas

```bash
python -m pip install markdown pyyaml beautifulsoup4
```

### Comando de compilación

Desde la raíz de `Commercial Processes`:

```bash
python 90_HTML_System/build_manual.py
```

### Resultado esperado

```text
99_Output/dproperty_procesos_diagrama.html
```

El HTML final debe ser autocontenido: estilos y JavaScript incluidos en el mismo archivo, sin depender de rutas locales que puedan romperse al enviarlo por correo o abrirlo en otra computadora.

## 0.7 Controles automáticos mínimos del generador

Antes de crear el HTML, el generador debe comprobar:

- IDs únicos.
- Orden sin duplicados.
- Título y objetivo presentes.
- Flujo con numeración consecutiva.
- Cada fila RACI tiene exactamente un aprobador o un rol aprobador claramente definido.
- Todos los códigos de rol existen en la leyenda.
- Cada KPI tiene una meta, frecuencia o estado explícito.
- Los enlaces a fuentes existen.
- No hay procesos marcados como `draft` incluidos accidentalmente en producción.

## 0.8 Revisión humana obligatoria después de compilar

- Abrir todas las pestañas y confirmar que navegan correctamente.
- Revisar que ningún texto quede cortado.
- Revisar tablas largas en pantalla de 1366 px y en móvil.
- Confirmar que los colores de roles sean consistentes.
- Probar `Ctrl+P` y revisar saltos de página.
- Confirmar que cifras, nombres y responsabilidades coincidan con la última decisión aprobada.
- Comparar la fecha de generación con el último cambio registrado.

## 0.9 Cómo añadir un nuevo proceso

1. Duplicar el módulo más parecido dentro de `02_Processes`.
2. Asignar un `id` nuevo e inmutable, por ejemplo `process8`.
3. Definir `nav_label`, `order`, título, responsable y fuente.
4. Completar todas las secciones obligatorias.
5. Añadir el archivo al manifiesto.
6. Registrar la decisión y el cambio.
7. Ejecutar el generador.
8. Validar la nueva pestaña y las demás pestañas existentes.

## 0.10 Cómo modificar un proceso existente

- Cambiar únicamente el módulo afectado.
- Mantener el mismo `id`.
- Actualizar `last_updated` y `source_decisions`.
- Revisar impacto sobre otros procesos conectados. Por ejemplo, una regla creada en Alquiler puede requerir nuevas alertas en Administración de Propiedades.
- Regenerar el HTML completo, no una sola sección aislada.

## 0.11 Convención para decisiones aún no confirmadas

Usar etiquetas explícitas:

- `APROBADO`: decisión formalmente validada.
- `PENDIENTE DE VALIDACIÓN`: propuesta operativa aún no aprobada.
- `SUPUESTO DE TRABAJO`: criterio temporal utilizado para diseñar el flujo.
- `NO APLICA`: sección evaluada y descartada.

Las propuestas pendientes no deben presentarse en el HTML final como políticas vigentes, salvo que el diseño las muestre claramente como pendientes.

## 0.12 Manifiesto recomendado

`00_Control/00_Manifest.md` debe contener una tabla como esta:

| Orden | ID | Archivo | Pestaña | Estado | Última actualización |
|---:|---|---|---|---|---|
| 10 | intro | `01_Foundation/01_Introduction.md` | Introducción | active | 2026-06-14 |
| 20 | legend | `01_Foundation/02_Roles_and_RACI.md` | Leyenda | active | 2026-06-14 |
| 30 | process1 | `02_Processes/01_Leads.md` | 1. Leads | active | 2026-06-14 |
| 40 | process2 | `02_Processes/02_Lista_Cero.md` | 2. Lista Cero | active | 2026-06-14 |
| 50 | process3 | `02_Processes/03_Mercado_Secundario.md` | 3. Secundario | active | 2026-06-14 |
| 60 | process4 | `02_Processes/04_Cesiones.md` | 4. Cesiones | active | 2026-06-14 |
| 70 | process5 | `02_Processes/05_Alquiler.md` | 5. Alquiler | active | 2026-06-14 |
| 80 | process6 | `02_Processes/06_Administracion_de_Propiedades.md` | 6. Administración | active | 2026-06-14 |
| 90 | process7 | `02_Processes/07_Comisiones.md` | 7. Comisiones | active | 2026-06-14 |
| 100 | summary | `01_Foundation/04_Responsibility_Summary.md` | Resumen | active | 2026-06-14 |

## 0.13 Regla de transición desde este ground floor

Mientras la migración no haya terminado:

- este archivo puede utilizarse para consulta y diseño;
- cualquier dato que vaya a convertirse en política debe validarse primero;
- las nuevas decisiones deben registrarse con su evidencia;
- no se debe asumir que una frase es vigente solo porque aparece aquí;
- no se deben crear copias paralelas del contenido sin registrar su relación con este archivo.

La migración se considerará terminada únicamente cuando:

- [ ] Exista un módulo por cada proceso.
- [ ] Cada módulo tenga front matter válido.
- [ ] Exista un manifiesto sin duplicados.
- [ ] Todas las decisiones vigentes estén vinculadas a una evidencia.
- [ ] El validador se ejecute sin errores.
- [ ] El generador produzca el HTML completo.
- [ ] El HTML haya sido revisado visualmente.
- [ ] Los responsables hayan validado sus procesos.
- [ ] Exista una release publicada.
- [ ] Este documento haya sido archivado.

---



# 1. Contenido operativo consolidado — base de trabajo

> [!WARNING] Alcance de esta sección
> El contenido siguiente representa el material operativo consolidado disponible al momento de crear este ground floor. No todo tiene el mismo nivel de validación. Las secciones respaldadas por decisiones formales deben conservar su evidencia; las demás deben revisarse con sus responsables antes de publicarse como política definitiva.



## Índice de pestañas del HTML

| Pestaña | ID interno |
| --- | --- |
| 📖 Introducción | intro |
| 👥 Leyenda | legend |
| 1. Leads | process1 |
| 2. Lista Cero | process2 |
| 3. Secundario | process3 |
| 4. Cesiones | process4 |
| 5. Alquiler | process5 |
| 6. Administración | process6 |
| 7. Comisiones | process7 |
| 📋 Resumen | summary |


---

# Cómo Leer Este Documento

`ID HTML: intro`


> **Nota de proceso:** Versión ajustada según Acta de Reunión #002-26 — Comité de Ventas Dproperty, 14 de junio de 2026. Los cambios se concentran en el Proceso 5: Alquiler y su conexión con el Proceso 6: Administración de Propiedades. Se incorporan trazabilidad formal de ofertas, diferenciación de roles, aprobación reforzada de perfiles especiales, control de versiones contractuales, condiciones para inmuebles amoblados, garantías de promotora y alertas de vencimientos y mantenimientos.


Este manual está diseñado para que cualquier miembro del equipo pueda entender rápidamente cómo funcionan los procesos comerciales de Dproperty y cuál es su rol en cada uno de ellos.


## Estructura de cada proceso


Cada proceso comercial se presenta en tres partes:


1. DIAGRAMA DE FLUJO: Una secuencia visual que muestra paso a paso cómo se ejecuta el proceso. Cada paso indica quién lo realiza (codificado por color) y qué resultado se espera.


2. MATRIZ RACI: Una tabla que define claramente los roles de cada persona en cada tarea. Esto elimina la ambigüedad sobre quién debe hacer qué.


3. KPIs: Indicadores clave de desempeño que nos permiten medir si el proceso está funcionando correctamente.


## ¿Qué es la Matriz RACI?


RACI es un modelo de asignación de responsabilidades que usamos para definir exactamente quién hace qué en cada tarea:


| Código | Significado | Definición |
| --- | --- | --- |
| R | RESPONSABLE | Quien EJECUTA la tarea. Hace el trabajo. Puede haber más de uno. |
| A | APROBADOR | Quien RINDE CUENTAS y tiene la última palabra. Solo puede haber UNO. |
| C | CONSULTADO | A quien se PIDE OPINIÓN antes de actuar. Comunicación bidireccional. |
| I | INFORMADO | A quien se NOTIFICA después. Comunicación unidireccional. |


## Ejemplo Práctico


Para la tarea "Presentar oferta al vendedor":


- R (Responsable) = AG → El agente redacta y presenta la oferta.


- A (Aprobador) = DC → La Directora Comercial debe aprobar antes de enviarla.


- C (Consultado) = ADM → Se consulta a Administración si hay dudas legales.


- I (Informado) = CBI → Se notifica a Coordinación para registro.


---

# Leyenda del Equipo

`ID HTML: legend`


El equipo de Dproperty está compuesto por 14 personas. Cada rol tiene un código y color único:


> **Nota de proceso:** Nota para el Proceso 5: el rol general AG se divide operativamente en ATI (Asesor del Inquilino) y ACO (Asesor Consignador). Asimismo, se distinguen DO (Dirección de Operaciones), LA (Luz Adriana) y PYE (Preparación y Entrega) para reflejar los acuerdos del Comité 002-26.


| Código | Rol | Responsabilidad principal |
| --- | --- | --- |
| DC | Directora Comercial (1) | Dirige agentes, aprueba ofertas y contratos, supervisa cierres |
| AG | Agentes Inmobiliarios (9) | Captación, visitas, negociación, cierre de ventas y alquileres |
| ADM | Administración (1) | Legal, contabilidad, contratos, comunicación post-cierre, comisiones |
| CBI | Coordinación/BI — Esteban (1) | Estrategia, analytics, coordinación, supervisión de procesos, CRM |
| SEC | Secretaria (1) | Documentación, archivo, comunicaciones internas, agendas |
| MAN | Mensajero/Mantenimiento (1) | Entregas, reparaciones, preparación de apartamentos, inventarios |


## Jerarquía de Aprobaciones


- Ofertas y negociaciones → Aprueba: DC


- Contratos y términos legales → Aprueba: DC con apoyo de ADM


- Procesos y flujos operativos → Supervisa: CBI


- Pagos y comisiones → Aprueba: DC, ejecuta: ADM


- Asignación de leads → Coordina: CBI (Automatico en CRM), valida: DC


---

# Proceso 1: Registro y Gestión de Leads

`ID HTML: process1`


Objetivo: Estandarizar la captación, calificación y seguimiento de leads desde ferias, canales digitales y referidos.


## Diagrama de Flujo


| Paso | Acción | Rol responsable | Descripción / resultado esperado |
| --- | --- | --- | --- |
| 1 | Captación del Lead | AG | Recoger datos en feria/web: nombre, correo, teléfono, país, tipo de inversor |
| 2 | Registro en CRM | AG | Ingresar lead en HubSpot con información completa (<1 hora) |
| 3 | Verificación de datos | SEC | Validar que la información esté completa y sin duplicados |
| 4 | Calificación | AG | Clasificar: Hot (<30 días), Warm (1-6 meses), Cold (>6 meses) |
| 5 | Propuesta de Asignación | CBI | Proponer asignación según reglas (Hot→Senior, Cold→Prospección) |
| 6 | Validación Asignación | DC | Aprobar o reasignar lead según criterio comercial |
| 7 | Primer Contacto | AG | Contactar en <24h con guion y material inicial (brochure) |
| 8 | Seguimiento | AG | Día 1: WhatsApp / Día 3: Brochure / Día 7: Dudas / Día 14: Oferta |
| 9 | Supervisión Pipeline | DC | Revisar avance semanal de leads por agente |
| 10 | Nutrición Automática | CBI | Si no responde en 30 días → Flujo automático en HubSpot |
| 11 | Reporte Semanal | CBI | Dashboard de leads, conversiones y ROI por fuente |


## Matriz RACI


| Tarea | R | A | C | I |
| --- | --- | --- | --- | --- |
| Captación en feria/digital | AG | DC | — | CBI |
| Registro en CRM | AG | CBI | SEC | DC |
| Verificación de datos | SEC | CBI | AG | — |
| Calificación del lead | AG | DC | CBI | — |
| Propuesta de asignación | CBI | DC | — | AG |
| Aprobación de asignación | DC | DC | CBI | AG |
| Primer contacto (<24h) | AG | DC | — | CBI |
| Seguimiento estructurado | AG | DC | — | CBI |
| Supervisión semanal pipeline | DC | DC | CBI | AG |
| Configurar flujos automáticos | CBI | CBI | DC | AG |
| Reporte semanal de leads | CBI | CBI | DC | AG, ADM |


## KPIs del Proceso


| KPI | Meta / frecuencia |
| --- | --- |
| Tiempo primer contacto | < 24 horas |
| Leads registrados en <1h | > 90% |
| Conversión Lead → Reunión | > 25% |
| ROI por fuente | Mensual |


---

# Proceso 2: Venta Lista Cero (Preventa)

`ID HTML: process2`


Objetivo: Gestionar la venta de propiedades en planos directamente con promotoras, desde la reserva hasta el cobro de comisión.


## Diagrama de Flujo


| Paso | Acción | Rol responsable | Descripción / resultado esperado |
| --- | --- | --- | --- |
| 1 | Reunión Inicial | AG | Levantar perfil: presupuesto total, disponible, mensual, motivación |
| 2 | Presentación Proyecto | AG | Mostrar proyectos + cuadro ROI. Registrar feedback en CRM |
| 3 | Validar Interés | DC | Revisar que el proyecto se ajuste al perfil del cliente |
| 4 | Reserva (USD 1,000) | AG | Recibir pago reserva + completar hoja de negocio |
| 5 | Aprobación de Reserva | DC | Validar términos y autorizar envío a promotora |
| 6 | Comunicación Promotora | ADM | Enviar a promotora: proyecto, unidad, cliente, precio, ID |
| 7 | Solicitud Documentos | ADM | Pedir al cliente: debida diligencia, estados cuenta, carta laboral |
| 8 | Elaboración Contrato | ADM | Redactar contrato (formato Dproperty) o recibir de promotora |
| 9 | Aprobación Contrato | DC | Validar términos y aprobar versión final |
| 10 | Firma Contrato | ADM | Coordinar firma (digital o presencial) con todas las partes |
| 11 | Pago 5% Inicial | ADM | Cliente paga 5% a promotora. Confirmar y archivar |
| 12 | Cobro Comisión | ADM | Emitir factura proforma a promotora. Gestionar cobro |
| 13 | Actualización CRM | SEC | Registrar en CRM y cuadro de control interno |
| 14 | Postventa | ADM | Seguimiento a pagos, consultas y comunicación con cliente |


## Matriz RACI


| Tarea | R | A | C | I |
| --- | --- | --- | --- | --- |
| Reunión inicial + perfil | AG | DC | — | CBI |
| Presentación proyecto + ROI | AG | DC | — | — |
| Validación de interés | DC | DC | AG | CBI |
| Recepción de reserva | AG | DC | — | ADM, SEC |
| Aprobación de reserva | DC | DC | AG | ADM |
| Envío a promotora | ADM | ADM | DC | AG |
| Solicitud docs al cliente | ADM | ADM | AG | — |
| Elaboración de contrato | ADM | DC | AG | CBI |
| Aprobación de contrato | DC | DC | ADM | AG |
| Coordinación de firma | ADM | DC | — | AG |
| Confirmación pago 5% | ADM | ADM | DC | AG, CBI |
| Gestión cobro comisión | ADM | DC | — | AG |
| Actualización CRM | SEC | CBI | ADM | DC |
| Seguimiento postventa | ADM | DC | AG | CBI |


## KPIs del Proceso


| KPI | Meta / frecuencia |
| --- | --- |
| Conversión Reunión → Reserva | > 30% |
| Tiempo Reserva → Contrato | < 15 días |
| Expedientes completos | 100% |
| ROI real vs proyectado | ±10% |


---

# Proceso 3: Venta Mercado Secundario

`ID HTML: process3`


Objetivo: Gestionar la venta de propiedades existentes a usuario final, desde la perfilación hasta la entrega.


## Diagrama de Flujo


| Paso | Acción | Rol responsable | Descripción / resultado esperado |
| --- | --- | --- | --- |
| 1 | Reunión Inicial | AG | Perfil: presupuesto, tamaño, zona, edificios, crédito, especiales |
| 2 | Elaborar Agenda Visitas | AG | Seleccionar propiedades según perfil. Registrar en CRM |
| 3 | Realizar Visitas | AG | Mostrar propiedades. Registrar feedback detallado en CRM |
| 4 | Preparar Oferta | AG | Estructurar oferta con estrategia de negociación |
| 5 | Aprobación Oferta | DC | Aprobar estrategia y términos antes de presentar |
| 6 | Presentar al Vendedor | AG | Enviar oferta formal. Gestionar contraoferta si aplica |
| 7 | Negociación | AG + DC | DC supervisa y aprueba contraofertas hasta acuerdo |
| 8 | Proceso de Reserva | ADM | Hoja de negocio + acuerdo reserva + docs ID + pago |
| 9 | Elaborar Contrato | ADM | Redactar contrato de promesa con términos acordados |
| 10 | Validaciones Paralelas | ADM | Impuesto inmueble, crédito comprador, hipoteca vendedor |
| 11 | Aprobación Final | DC | Validar contrato final antes de firma |
| 12 | Firma + Cobro 50% | ADM | Coordinar firma. Cobrar 50% comisión |
| 13 | Cierre Legal | ADM | Carta saldo, promesa pago, protocolo, escritura |
| 14 | Entrega Unidad | AG + MAN | Entrega física + inventario detallado |
| 15 | Seguimiento 30 días | AG | Llamada de satisfacción al mes de la entrega |


## Matriz RACI


| Tarea | R | A | C | I |
| --- | --- | --- | --- | --- |
| Reunión inicial + perfil | AG | DC | — | CBI |
| Agenda y visitas | AG | DC | — | — |
| Registro feedback CRM | AG | CBI | — | DC |
| Preparación de oferta | AG | DC | ADM | — |
| Aprobación de oferta | DC | DC | AG | CBI |
| Negociación con vendedor | AG | DC | ADM | CBI |
| Proceso de reserva | ADM | DC | AG | SEC |
| Elaboración contrato | ADM | DC | AG | CBI |
| Validaciones legales | ADM | ADM | DC | AG |
| Aprobación final contrato | DC | DC | ADM | AG |
| Entrega física | AG | DC | MAN | ADM |
| Seguimiento postventa | AG | DC | ADM | CBI |


## KPIs del Proceso


| KPI | Meta / frecuencia |
| --- | --- |
| Conversión Visitas → Ofertas | > 20% |
| Conversión Ofertas → Reservas | > 40% |
| Tiempo Reserva → Contrato | < 10 días |
| Satisfacción (NPS) | > 80 |


---

# Proceso 4: Venta por Cesión

`ID HTML: process4`


Objetivo: Gestionar la cesión de propiedades de inversionistas a clientes finales, maximizando la rentabilidad del inversionista original.


> **ALERTA / REGLA:** ⚠️ NOTA IMPORTANTE: Este proceso requiere validación dual cuando el agente que vende al cliente final es diferente al asesor de inversión original. En caso de conflicto, la Directora Comercial tiene la decisión final.


## Diagrama de Flujo


| Paso | Acción | Rol responsable | Descripción / resultado esperado |
| --- | --- | --- | --- |
| 1 | Reunión Inicial | AG | Perfil del comprador final: presupuesto, zona, edificios, crédito |
| 2 | Agenda y Visitas | AG | Seleccionar y mostrar propiedades en cesión |
| 3 | Validación Interna | DC | Si agente ≠ asesor original: validar con asesor de inversión |
| 4 | Preparar Oferta | AG | Estructurar oferta maximizando utilidad del inversionista |
| 5 | Doble Aprobación | DC | Aprobar estrategia. Si hay conflicto entre agentes: DC decide |
| 6 | Presentar al Cedente | AG | Enviar oferta al inversionista/cedente |
| 7 | Negociación | AG + DC | DC supervisa que se maximice rentabilidad del inversionista |
| 8 | Proceso de Reserva | ADM | Hoja de negocio + acuerdo + documentos + pago |
| 9 | Contrato de Cesión | ADM | Elaborar contrato específico de cesión |
| 10 | Aprobación Final | DC | Validar contrato de cesión antes de firma |
| 11 | Firma + Cobro | ADM | Coordinar firma tripartita. Cobrar comisiones |
| 12 | Cierre y Entrega | AG + MAN | Proceso legal + entrega física + inventario |
| 13 | Reporte Rentabilidad | CBI | Comparar ROI real vs. proyectado del inversionista |


## Matriz RACI


| Tarea | R | A | C | I |
| --- | --- | --- | --- | --- |
| Reunión inicial cliente final | AG | DC | — | CBI |
| Validación con asesor original | DC | DC | AG (orig) | AG, CBI |
| Preparación de oferta | AG | DC | AG (orig) | — |
| Doble aprobación | DC | DC | AG, AG (orig) | CBI |
| Negociación con inversionista | AG | DC | AG (orig) | CBI |
| Proceso de reserva | ADM | DC | AG | SEC |
| Contrato de cesión | ADM | DC | AG | CBI |
| Aprobación final | DC | DC | ADM | AG |
| Entrega física | AG | DC | MAN | ADM |
| Reporte de rentabilidad | CBI | CBI | DC | AG (orig) |


## KPIs del Proceso


| KPI | Meta / frecuencia |
| --- | --- |
| Validación con asesor original | 100% |
| Rentabilidad vs proyectada | ≥ Proyección |
| Tiempo total de cesión | < 30 días |


---

# Proceso 5: Alquiler (Estancias Largas)

`ID HTML: process5`


Objetivo: Gestionar el arrendamiento de propiedades con trazabilidad completa desde la visita y la presentación de la oferta hasta la firma, entrega, seguimiento y activación de alertas administrativas.


> **ALERTA / REGLA:** ⚠️ REGLA DE TRAZABILIDAD: La llamada al propietario no sustituye el respaldo formal. Toda oferta deberá quedar documentada por correo con el resumen del perfil, condiciones del negocio, documentación de respaldo y resultado de la llamada. No se avanza a firma sin que ambas partes hayan aprobado la misma versión del contrato.


## Roles específicos de este proceso


| Código | Rol | Responsabilidad principal |
| --- | --- | --- |
| ATI | Asesor del Inquilino | Capta, perfila, visita, presenta la oferta, documenta la gestión y acompaña la entrega. |
| ACO | Asesor Consignador | Conoce la relación con el propietario y apoya en la presentación del perfil o negociación cuando sea necesario. |
| ADM | Administración | Silvia y/o Maria Isabel: documentación, oferta formal, contrato, firma, alertas y mantenimiento. |
| DO | Dirección de Operaciones | Controla el procedimiento, la trazabilidad, las excepciones operativas y la versión contractual. |
| LA | Luz Adriana | Aprueba el perfil del cliente y emite visto bueno escrito para perfiles especiales o excepciones relevantes. |
| PYE | Preparación y Entrega | Inspección, reparaciones autorizadas, inventario, acta de entrega y registro de pendientes. |


## Decisiones operativas obligatorias


| Decisión / caso | Regla operativa |
| --- | --- |
| Inmuebles amoblados | Durante la visita se informa la condición general de dos depósitos de garantía más el primer mes. Un solo depósito requiere autorización previa de Administración. |
| Perfiles especiales | Abogados, influencers u otros perfiles de validación reforzada requieren documentación adicional y visto bueno escrito de Luz Adriana antes de la firma. |
| Revisión contractual | Ruta ordinaria: propietario y luego inquilino. Ruta rápida: inquilino y luego propietario. Ambas partes deben aprobar exactamente la misma versión. |
| Garantías de promotora | Los pendientes bajo garantía se explican desde la visita, se reiteran en la entrega y se registran sin intervenir cuando ello pueda anular la garantía. |


## Diagrama de Flujo


| Paso | Acción | Rol responsable | Descripción / resultado esperado |
| --- | --- | --- | --- |
| 1 | Recepción y Registro del Lead | ATI | Registrar en CRM: cliente, inmueble, presupuesto, fechas, fuente, asesor consignador y necesidades especiales. |
| 2 | Calificación y Documentación Inicial | ATI | Validar plazo, ingresos, fecha de mudanza, referencias y documentación. Marcar perfiles que requieran validación reforzada. |
| 3 | Visita y Divulgaciones Obligatorias | ATI | Mostrar el inmueble. En amoblados, informar dos depósitos + primer mes. En unidades nuevas, explicar posibles pendientes bajo garantía de la promotora. |
| 4 | Recibir y Estructurar Oferta | ATI | Documentar monto, plazo, inicio, depósitos, mobiliario, solicitudes especiales y condiciones del cliente. |
| 5 | Presentación Telefónica al Propietario | ATI | Presentar verbalmente la oferta y registrar el resultado de la llamada, observaciones y posibles contraofertas. |
| 6 | Informar al Asesor Consignador | ATI → ACO | Notificar la gestión para que conozca el caso y apoye en la presentación del perfil o la negociación cuando sea necesario. |
| 7 | Correo Formal de Trazabilidad | ATI | Enviar a Silvia, con copia a Luz Adriana, Maria Isabel y ACO: documentos, perfil, condiciones, resultado de llamada y observaciones. |
| 8 | Aprobación del Perfil | LA | Aprobar o rechazar el perfil. Para abogados, influencers u otros casos especiales, emitir visto bueno escrito y solicitar documentación adicional. |
| 9 | Oferta Formal al Propietario | ADM | Silvia y/o Maria Isabel envían la oferta formal, resumen del perfil, documentación de respaldo y borrador del contrato para revisión. |
| 10 | Definir Ruta de Revisión | DO + ADM | Ruta ordinaria: propietario primero, luego inquilino. Ruta rápida: inquilino primero, incorporar comentarios y después propietario. |
| 11 | Control de Versión Contractual | ADM | Consolidar comentarios y confirmar que propietario e inquilino aprueban la misma versión final antes de firmar. |
| 12 | Firma y Pagos | ADM | Coordinar firma. Confirmar primer mes y depósitos. En amoblados, cualquier excepción a los dos depósitos debe estar autorizada previamente. |
| 13 | Acta de Remodelación de Terceros | ADM | Cuando aplique, solicitar acta con pisos, acabados, equipos, mobiliario fijo, decoración, mejoras, garantías y proveedores. |
| 14 | Preparación, Inspección e Inventario | PYE | Preparar el inmueble y elaborar inventario tomando como base el acta de remodelación, fotografías y estado real de equipos y mobiliario. |
| 15 | Registro de Garantías y Pendientes | PYE + ADM | Registrar trabajos pendientes de promotora en inventario o acta. No intervenir si puede anular la garantía; informar que los tiempos dependen de la promotora. |
| 16 | Entrega del Inmueble | ATI + PYE | Entregar llaves, inventario y acta firmada. Reiterar pendientes de garantía, responsables y canales de seguimiento. |
| 17 | Activar Alertas Administrativas | ADM | Crear alertas de contrato a 45 o 60 días y calendario de mantenimiento de aires y línea blanca según contrato. Conectar con Proceso 6. |
| 18 | Seguimiento Post-entrega | ATI + ADM | Contacto a los 7 y 30 días, registro de incidencias y traspaso formal de la administración recurrente. |


## Matriz RACI


| Tarea | R | A | C | I |
| --- | --- | --- | --- | --- |
| Recepción, registro y calificación | ATI | DO | ADM | LA |
| Visita y divulgaciones obligatorias | ATI | DO | ACO | ADM |
| Presentación telefónica de oferta | ATI | DO | ACO | ADM |
| Informar al asesor consignador | ATI | DO | ACO | ADM |
| Correo formal con respaldo | ATI | DO | ADM, ACO | LA |
| Aprobación del perfil | ADM | LA | ATI, DO | ACO |
| Perfiles especiales / documentación reforzada | ADM | LA | ATI, DO | ACO |
| Excepción a dos depósitos en amoblados | ADM | DO | ATI, LA | ACO |
| Envío de oferta formal y borrador | ADM | DO | LA, ATI, ACO | — |
| Definir ruta de revisión contractual | ADM | DO | ATI, ACO | LA |
| Control de versión y aprobación bilateral | ADM | DO | ATI | ACO, LA |
| Firma y confirmación de pagos | ADM | DO | ATI | ACO, LA |
| Solicitud de acta de remodelación | ADM | DO | ACO, PYE | ATI |
| Preparación e inventario | PYE | ADM | ATI, ACO | DO |
| Registro de garantías y pendientes | PYE | DO | ADM, ATI | ACO, LA |
| Entrega del inmueble | ATI + PYE | DO | ADM | ACO, LA |
| Alertas de contrato y mantenimientos | ADM | DO | PYE | ATI, ACO, LA |
| Seguimiento post-entrega | ATI | DO | ADM | ACO, LA |


## KPIs del Proceso


| KPI | Meta / frecuencia |
| --- | --- |
| Ofertas con respaldo formal | 100% |
| Perfiles especiales con aprobación escrita | 100% |
| Contratos con misma versión aprobada | 100% |
| Entregas con inventario firmado | 100% |
| Alertas creadas al cierre | 100% |
| Seguimiento 7 y 30 días | ≥ 95% |


---

# Proceso 6: Administración de Propiedades

`ID HTML: process6`


Objetivo: Gestionar propiedades arrendadas garantizando pagos, conservación del inmueble, trazabilidad de incidencias y cumplimiento anticipado de vencimientos y mantenimientos contractuales.


> **Nota de proceso:** Conexión obligatoria con Proceso 5: al cerrar cada alquiler, Administración deberá recibir el expediente final, inventario, acta de entrega, pendientes de garantía, fecha de vencimiento, condiciones de renovación y frecuencias de mantenimiento para crear las alertas correspondientes.


## Diagrama de Flujo


| Paso | Acción | Rol responsable | Descripción / resultado esperado |
| --- | --- | --- | --- |
| 1 | Recibir Expediente del Alquiler | ADM | Validar contrato final, inventario, acta, depósitos, pendientes de garantía, vencimiento y obligaciones de mantenimiento. |
| 2 | Generar Facturación | ADM | Emitir factura mensual según contrato. |
| 3 | Recordatorio de Pago | ADM | Enviar recordatorio cinco días antes del vencimiento. |
| 4 | Recibir y Registrar Pago | ADM | Confirmar pago en sistema y actualizar CRM o cuadro de control. |
| 5 | Calcular Deducciones | ADM | Aplicar gastos comunes, administración y mantenimientos autorizados. |
| 6 | Validar Liquidación | DC / DO | Aprobar la liquidación antes de transferir al propietario. |
| 7 | Transferir al Propietario | ADM | Transferir el pago neto y archivar comprobante. |
| 8 | Recibir Incidencias | ADM | Registrar reportes del inquilino, propietario, inspecciones o pendientes de garantía. |
| 9 | Autorizar Reparación | DC / DO | Aprobar gastos mayores a USD 200 o cualquier intervención que requiera autorización especial. |
| 10 | Coordinar Reparación | PYE / MAN | Coordinar proveedor autorizado. No intervenir en pendientes de promotora cuando pueda afectarse la garantía. |
| 11 | Documentar Trabajo | PYE / MAN | Registrar fotos, costo, proveedor, fecha, garantía y resultado. Subir evidencia al expediente. |
| 12 | Reporte Mensual | ADM | Enviar al propietario: renta, deducciones, incidencias, mantenimientos y estado del inmueble. |
| 13 | Inspección Semestral | PYE / MAN | Realizar visita programada, actualizar fotografías e identificar necesidades preventivas. |
| 14 | Alerta de Vencimiento | ADM | Mantener alerta en calendario 45 o 60 días antes del vencimiento, según contrato y complejidad del caso. |
| 15 | Gestionar Renovación o Entrega | ADM | Contactar a propietario e inquilino, confirmar intención, condiciones, ajustes o cronograma de salida. |
| 16 | Calendario de Mantenimientos | ADM | Mantener cuadro y calendario de aires acondicionados y línea blanca conforme a la frecuencia indicada en cada contrato. |
| 17 | Correo y Coordinación de Proveedor | ADM | Enviar recordatorio al inquilino, coordinar proveedor recomendado y confirmar fecha de atención. |
| 18 | Archivar Evidencia y Reprogramar | ADM | Archivar factura, fotos o constancia del servicio y programar la siguiente alerta. |


## Matriz RACI


| Tarea | R | A | C | I |
| --- | --- | --- | --- | --- |
| Recepción y validación de expediente | ADM | DO | ATI, PYE | ACO, LA |
| Facturación mensual | ADM | ADM | CBI | DC |
| Registro de pagos | ADM | ADM | — | CBI |
| Cálculo de deducciones | ADM | DO | — | CBI |
| Validación y liquidación al propietario | ADM | DO | DC | CBI |
| Gestión de incidencias | ADM | ADM | PYE | DO |
| Autorización de gastos mayores | DO | DO | ADM | DC |
| Ejecución y documentación de reparaciones | PYE | ADM | — | DO |
| Reporte mensual al propietario | ADM | DO | CBI | — |
| Inspección semestral | PYE | ADM | — | DO, CBI |
| Crear alerta 45/60 días | ADM | DO | ATI, ACO | LA |
| Gestionar renovación o entrega | ADM | DO | ATI, ACO | LA |
| Actualizar calendario de mantenimientos | ADM | DO | PYE | ATI, ACO |
| Correo al inquilino y coordinación de proveedor | ADM | ADM | PYE | DO |
| Archivo de evidencia y nueva alerta | ADM | DO | PYE | CBI |


## KPIs del Proceso


| KPI | Meta / frecuencia |
| --- | --- |
| Pagos en fecha | > 95% |
| Tiempo de atención de incidencias | < 48 horas |
| Contratos con alerta 45/60 días | 100% |
| Mantenimientos programados según contrato | 100% |
| Servicios con evidencia archivada | 100% |
| Renovación de contratos | > 70% |


---

# Proceso 7: Pago de Comisiones

`ID HTML: process7`


Objetivo: Estandarizar el cobro, liquidación y pago de comisiones garantizando trazabilidad y cumplimiento de plazos.


## Diagrama de Flujo


| Paso | Acción | Rol responsable | Descripción / resultado esperado |
| --- | --- | --- | --- |
| 1 | Confirmar Pago Cliente | ADM | Verificar que cliente pagó 5% inicial a promotora |
| 2 | Factura Proforma | ADM | Crear factura con datos de unidad y promotora |
| 3 | Enviar a Promotora | ADM | Enviar proforma + documentación de cobro |
| 4 | Recibir ACH | ADM | Confirmar transferencia de promotora |
| 5 | Factura Electrónica | ADM | Emitir factura electrónica formal |
| 6 | Notificar a Agentes | ADM | Informar que comisión fue pagada |
| 7 | Cuentas de Cobro | AG | Agentes envían cuenta + factura (MARTES 12:00) |
| 8 | Calcular Comisiones | ADM | Aplicar política: Junior 35%/70%, Senior 40%/45% |
| 9 | Validar Cálculos | DC | Revisar montos y aprobar liquidación |
| 10 | Validar Documentos | CBI | Revisar RUC, documentación completa |
| 11 | Armar Carpetas | SEC | Imprimir y organizar por unidad (MIÉRCOLES 12:00) |
| 12 | Autorizar Pagos | DC | Dar visto bueno final para transferencias |
| 13 | Procesar Pagos | ADM | Ejecutar transferencias (VIERNES o LUNES) |
| 14 | Archivar | SEC | Digital y físico en carpeta de unidad |


## Política de Comisiones


| Categoría | Ventas | Alquileres | Consignación |
| --- | --- | --- | --- |
| Broker Junior | 35% | 70% | +5% prop / +5% cliente |
| Broker Senior (ACOBIR) | 40% | 45% | +5% prop / +5% cliente |
| Broker Externo | 1.5% del valor | — | — |


Nota: Las comisiones se calculan sobre el monto que ingresa a Dproperty, no sobre el valor total de la propiedad.


## Matriz RACI


| Tarea | R | A | C | I |
| --- | --- | --- | --- | --- |
| Confirmar pago 5% | ADM | ADM | — | DC |
| Gestión cobro promotora | ADM | DC | — | CBI |
| Envío cuentas de cobro | AG | ADM | — | SEC |
| Cálculo de comisiones | ADM | DC | — | CBI |
| Validación de cálculos | DC | DC | ADM | — |
| Validación documentos | CBI | CBI | ADM | — |
| Armado de carpetas | SEC | ADM | — | — |
| Autorización de pagos | DC | DC | ADM | CBI |
| Procesamiento pago | ADM | DC | — | AG |
| Archivo final | SEC | ADM | — | CBI |


## KPIs del Proceso


| KPI | Meta / frecuencia |
| --- | --- |
| Tiempo 5% → pago agente | < 10 días |
| Carpetas completas | 100% |
| Errores documentales | 0 |


---

# Resumen de Responsabilidades

`ID HTML: summary`


## Directora Comercial (DC)


- Supervisión y dirección del equipo de 9 agentes


- Aprobación de todas las ofertas y estrategias de negociación


- Validación y aprobación de contratos


- Decisión final en conflictos (especialmente cesiones)


- Supervisión semanal del pipeline


- Autorización de gastos de mantenimiento mayores


- Aprobación final de liquidaciones y pagos de comisiones


## Agentes Inmobiliarios (AG)


- Captación, calificación y seguimiento de leads


- Reuniones iniciales y perfilación de clientes


- Agenda, preparación y ejecución de visitas


- Preparación de ofertas (requieren aprobación de DC)


- Negociación bajo supervisión de DC


- Participación en entregas físicas


- Seguimiento postventa (7 y 30 días)


## Administración (ADM)


- Comunicación con promotoras y propietarios post-cierre


- Elaboración y gestión de contratos


- Solicitud y validación de documentos


- Coordinación de firmas


- Gestión de cobro y pago de comisiones


- Facturación mensual y liquidaciones


## Coordinación/BI (CBI)


- Propuesta de asignación de leads


- Supervisión de cumplimiento de procesos


- Validación documental en comisiones


- Configuración de flujos automáticos en CRM


- Generación de reportes y dashboards


- Coordinación interdepartamental


## Secretaria (SEC)


- Verificación de datos y duplicados en CRM


- Impresión y armado de carpetas documentales


- Entrega de documentación a contabilidad


- Archivo físico y digital


## Mensajero/Mantenimiento (MAN)


- Pre-inspección de propiedades


- Ejecución de reparaciones menores


- Limpieza profunda pre-entrega


- Elaboración de inventarios


- Inspecciones semestrales


Preparación y Entrega (PYE): inspecciona, prepara, documenta inventario, registra pendientes de garantía y participa en la entrega física.


Luz Adriana (LA): aprueba el perfil del cliente y debe dar visto bueno escrito a perfiles especiales antes de la firma.


Dirección de Operaciones (DO): asegura que se cumpla la ruta aprobada, valida excepciones operativas y supervisa trazabilidad, contrato, entrega y seguimiento administrativo.


Administración (ADM): recibe el expediente, gestiona aprobaciones, envía la oferta formal y el borrador, controla la versión contractual, coordina firma, activa alertas y administra mantenimientos.


Asesor Consignador (ACO): debe ser informado después de la presentación telefónica al propietario y participa como apoyo en el perfil o la negociación cuando sea necesario.


Asesor del Inquilino (ATI): perfila al cliente, realiza la visita, explica depósitos y garantías, presenta la oferta por teléfono, informa al asesor consignador, envía el correo formal de trazabilidad y acompaña la entrega.


## Roles específicos en Alquiler — Comité 002-26


## Tiempos Críticos (SLAs)


| Acción | Tiempo Máximo |
| --- | --- |
| Registro de lead en CRM | < 1 hora |
| Primer contacto con lead | < 24 horas |
| Aprobación de oferta por DC | < 24 horas |
| Revisión de contrato (cada parte) | 48 horas |
| Envío cuentas de cobro (agentes) | Martes 12:00 |
| Entrega carpetas a contabilidad | Miércoles 12:00 |
| Procesamiento de pagos | Viernes o Lunes |
| Resolución de incidencias | < 48 horas |
| Alerta de vencimiento / renovación | 45 o 60 días antes |
| Correo formal de oferta y respaldo | Mismo día de la llamada |
| Aprobación de perfil especial | Antes de emitir versión final |
| Activación de alertas post-firma | < 2 días hábiles |
| Archivo de mantenimiento realizado | < 2 días hábiles |



---

# 2. Registro de esta versión

| Campo | Valor |
|---|---|
| Versión base | 002-26 |
| Fecha de decisión principal | 14 de junio de 2026 |
| Procesos modificados por el comité | Proceso 5: Alquiler; Proceso 6: Administración de Propiedades |
| Fuente de diseño | HTML ajustado del Manual de Procesos Comerciales |
| Fuente operativa validada para los cambios de Alquiler y Administración | Acta 002-26 del Comité de Ventas Dproperty |
| Próxima acción recomendada | Utilizar este ground floor para crear los módulos, validar cada proceso, construir el generador determinístico y después archivar este consolidado. |

## 2.1 Cambios principales incorporados por el Comité 002-26

- Participación obligatoria del asesor consignador después de la presentación telefónica de la oferta.
- Correo formal de trazabilidad con perfil, documentos, condiciones y resultado de la llamada.
- Aprobación escrita de Luz Adriana para perfiles especiales.
- Ruta ordinaria y ruta rápida para revisión del contrato.
- Control de una única versión contractual aprobada por propietario e inquilino.
- Dos depósitos de garantía más primer mes como condición general para inmuebles amoblados, salvo excepción autorizada.
- Acta de entrega de remodelaciones realizadas por terceros.
- Registro de garantías y pendientes de promotora sin intervenciones que puedan anularlas.
- Alertas de vencimiento con 45 o 60 días de anticipación.
- Calendario de mantenimiento de aires acondicionados y línea blanca.
- Conexión formal entre el cierre del proceso de Alquiler y la Administración recurrente de la propiedad.

## 2.2 Criterio de gobernanza documental

Este ground floor no determina por sí solo cuál regla es definitiva.

Cuando exista contradicción:

1. prevalece la decisión formal más reciente que pueda demostrarse;
2. la evidencia debe conservarse en `03_Evidence`;
3. la decisión debe registrarse en el Decision Log;
4. el módulo afectado debe actualizarse;
5. deben actualizarse también la matriz RACI, el flujo, los controles y los documentos asociados;
6. debe generarse una nueva release;
7. el HTML debe regenerarse desde los módulos aprobados.

La jerarquía provisional de autoridad será:

| Prioridad | Fuente |
|---:|---|
| 1 | Ley, contrato firmado, política corporativa formal o instrucción legal vigente |
| 2 | Decisión escrita y aprobada por la autoridad competente |
| 3 | Acta de comité aprobada |
| 4 | Módulo de proceso validado y publicado en una release |
| 5 | Correo o instrucción operativa documentada pendiente de incorporación |
| 6 | Contenido consolidado en este ground floor |
| 7 | Supuesto de trabajo o propuesta no aprobada |

## 2.3 Estado estructural de esta versión

| Elemento | Estado actual |
|---|---|
| Consolidación del contenido disponible | Completada como base inicial |
| Validación integral de todos los procesos | Pendiente |
| Separación en módulos | Pendiente |
| Manifiesto operativo | Especificado, pendiente de implementación |
| Esquema versionado | Recomendado, pendiente de implementación |
| Generador HTML | Especificado, pendiente de implementación |
| Validador automático | Especificado, pendiente de implementación |
| Release reproducible | Pendiente |
| Archivo del ground floor | Se archivará al completar la migración |

## 2.4 Criterio para usar este documento

Este archivo puede utilizarse para:

- orientar sesiones de trabajo;
- identificar qué debe validarse;
- preparar entrevistas con responsables;
- diseñar la arquitectura definitiva;
- construir los módulos iniciales;
- comparar el HTML actual con el futuro HTML generado.

No debe utilizarse por sí solo para:

- imponer una regla no aprobada;
- sustituir una evidencia formal;
- comunicar externamente políticas no validadas;
- resolver una contradicción sin revisar la fuente;
- mantener indefinidamente dos versiones paralelas del mismo proceso.
