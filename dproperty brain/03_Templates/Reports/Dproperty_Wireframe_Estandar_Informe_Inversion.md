# Dproperty — Wireframe maestro del informe de inversión

## 1. Propósito

Este documento define la estructura visual, narrativa y técnica estándar para los informes de **Flujo y Proyección** de Dproperty. Debe servir como instrucción directa para una IA, diseñador o analista que convierta el modelo financiero en un informe de *investment advisory* imprimible.

El informe se produce **primero en español**. Cualquier versión en otro idioma debe generarse posteriormente como una versión derivada, sin modificar la versión maestra en español.

El sistema debe funcionar con cualquier cantidad de proyectos y unidades:

- Las páginas estratégicas y financieras son módulos fijos.
- El índice visual, las fichas de proyectos y el calendario son módulos variables.
- Las unidades pertenecientes al mismo proyecto se agrupan bajo una sola ficha de proyecto.
- Se presentan como máximo **dos proyectos simples por página A4**.
- Un proyecto con más de dos unidades recibe una página completa y, si es necesario, páginas de continuación.
- El calendario se pagina por unidades y presenta como máximo cuatro líneas de tiempo por página.
- Todos los gráficos se alimentan de la misma fuente financiera validada.
- Las imágenes deben corresponder a los proyectos incluidos; no se deben utilizar fotografías inmobiliarias genéricas.

## Variables de escala

```text
P = cantidad de proyectos
U = cantidad total de unidades
S = cantidad de proyectos simples, con 1–2 unidades
C = conjunto de proyectos complejos, con más de 2 unidades
```

## Fórmula de paginación

```text
Páginas de índice visual
= techo(P ÷ 6)

Páginas de fichas
= techo(S ÷ 2)
+ suma[techo(unidades del proyecto complejo ÷ 6)]

Páginas de calendario
= techo(U ÷ 4)

Número total de páginas
= 8 módulos fijos
+ páginas de índice visual
+ páginas de fichas
+ páginas de calendario
```

Los ocho módulos fijos son: resumen ejecutivo, tesis, ventaja Dproperty, flujo y liquidez, financiamiento, contexto de Panamá, retornos y riesgos.

Para el portafolio de referencia de cinco proyectos y seis unidades:

```text
8 + techo(5 ÷ 6) + techo(5 ÷ 2) + techo(6 ÷ 4)
= 8 + 1 + 3 + 2
= 14 páginas
```

---

# 2. Sistema visual

## Formato

- Tamaño final: **A4 vertical, 210 × 297 mm**.
- El informe debe diseñarse directamente para A4; no se debe construir en 16:9 y escalar posteriormente.
- Márgenes exteriores: 14–16 mm.
- Retícula: 12 columnas.
- Espacio entre módulos: 10–14 pt.
- Fondo principal: blanco cálido.
- Cada página debe tener un solo mensaje central.
- La zona segura debe permitir impresión doméstica y profesional sin cortar pies, fuentes o numeración.

Referencia CSS para una versión HTML imprimible:

```css
@page {
  size: A4 portrait;
  margin: 15mm;
}

body {
  font-family: Helvetica, Arial, sans-serif;
  font-size: 12.5pt;
  line-height: 1.35;
}
```

## Paleta

| Uso | Color | Código |
|---|---|---|
| Color principal | Azul marino | `#0B1F33` |
| Azul secundario | Azul profundo | `#15344F` |
| Retorno positivo | Verde | `#12A67A` |
| Verde oscuro | Verde institucional | `#08785A` |
| Acento patrimonial | Dorado | `#C8A35A` |
| Comparación | Azul medio | `#4F7CAC` |
| Riesgo | Rojo | `#CF5A5A` |
| Texto principal | Grafito | `#17212B` |
| Texto secundario | Gris pizarra | `#637182` |
| Fondo de tarjetas | Gris muy claro | `#F4F7F8` |
| Líneas y retícula | Gris | `#DFE6EA` |

## Tipografía

- Familia principal: **Helvetica**.
- Fallback técnico: `Arial, sans-serif`.
- Números: usar cifras tabulares cuando la versión disponible de Helvetica lo permita.
- Título de portada o título principal de sección: 26–30 pt, bold.
- Título de página: 22–24 pt, bold.
- Kicker o antetítulo: 10–11 pt, bold, mayúsculas y espaciado amplio.
- Subtítulo: 12–13 pt, regular.
- KPI principal: 18–22 pt, bold.
- Etiqueta de KPI: 9–10 pt, bold.
- Texto de cuerpo: **12–13 pt**; estándar recomendado: 12.5 pt.
- Texto de tablas: 10.5–11.5 pt.
- Etiquetas, ejes y leyendas de gráficos: 9–10 pt.
- Fuente, nota metodológica breve y disclaimer: **9 pt**.
- No se permite ningún texto menor a 9 pt.
- Si el contenido no cabe, se crea una página adicional; nunca se reduce la tipografía por debajo de estas reglas.

## Cabecera y pie

Todas las páginas deben conservar:

1. Barra superior tricolor: azul marino, verde y dorado.
2. Kicker en mayúsculas.
3. Título que exprese una conclusión.
4. Subtítulo explicativo alineado a la derecha.
5. Pie izquierdo: `DPROPERTY · INVESTMENT ADVISORY`.
6. Pie derecho: fuente, fecha de corte y número de página.

Todo el contenido visible —títulos, ejes, leyendas, tooltips, notas y disclaimers— se redacta primero en español.

## Uso de fotografías

- Usar renders oficiales, fotografías oficiales del proyecto, avance de obra o planos suministrados por el promotor.
- Resolución mínima recomendada: 1,600 × 900 px.
- Relación preferida: 16:9.
- Evitar collages con más de tres imágenes por página.
- Mantener el punto focal libre de texto.
- Identificar proyecto, ubicación y tipo de imagen.
- Si es un render, incluir discretamente: `Render conceptual del promotor`.
- Si dos unidades pertenecen al mismo proyecto, combinar una imagen exterior con un plano, interior o amenidad para evitar duplicación visual.
- No alterar la apariencia arquitectónica mediante generación de imágenes.

## Reglas para los gráficos

- Usar **Plotly como estándar principal** para barras, líneas, waterfall, donut, Sankey, heatmaps, sensibilidad y gráficos de dispersión.
- Usar **D3** cuando se requiera una línea de tiempo de inflexiones altamente personalizada, resolución de colisiones entre anotaciones o interacción que Plotly no pueda representar con claridad.
- Para PDF, exportar los mismos gráficos como SVG; usar PNG de alta resolución solo cuando SVG no sea viable.
- El HTML interactivo y el PDF deben utilizar los mismos datos y producir las mismas cifras.
- No usar gráficos 3D.
- No utilizar más de cinco colores en un mismo gráfico.
- Mostrar cifras directamente cuando haya menos de ocho categorías.
- Para más de ocho activos, cambiar barras verticales por barras horizontales.
- Todos los textos dentro de gráficos deben respetar el mínimo de 9 pt.
- Incluir unidad de medida en título, eje o subtítulo.
- Indicar si el dato es:
  - Fuente del modelo.
  - Dato externo.
  - Recomendación Dproperty.
  - Supuesto pendiente de validación.
- Los tooltips interactivos deben mostrar valor, porcentaje, fecha y proyecto cuando corresponda.

---

# 3. Mapa completo del informe

Los números de página posteriores a la página 2 son dinámicos. Se conserva el siguiente orden:

| Orden | Tipo | Sección | Gráficos obligatorios | Imágenes |
|---:|---|---|---|---|
| 1 | Fijo | Resumen ejecutivo | Waterfall de valor + donut de estrategia | Ninguna; mantener el contenido exactamente aprobado |
| 2 | Fijo | Tesis de inversión | Sankey de arquitectura de retorno | Dos imágenes de proyectos patrimoniales |
| 3 | Variable | Portafolio en una mirada | Bubble chart + exposición geográfica | Hasta seis proyectos por página |
| 4 | Variable | Fichas de proyectos | Mini barras de precio/costo/valor | Una o dos imágenes oficiales por proyecto |
| 5 | Fijo | Ventaja Dproperty | Waterfall + barras de ventaja por proyecto/unidad | Detalle arquitectónico opcional |
| 6 | Variable | Calendario de inflexiones | Step chart de flujo mensual + hitos y pagos extraordinarios | Ninguna o avance de obra discreto |
| 7 | Fijo | Flujo y liquidez | Línea de caja + barras mensuales de flujo | Ninguna |
| 8 | Fijo | Financiamiento | Funding bridge + sensibilidad cuota/DSCR | Activos financiados |
| 9 | Fijo | Panamá y ubicación | Indicadores de mercado + exposición geográfica | Mapa e imágenes de ubicaciones |
| 10 | Fijo | Retornos y alternativas | Puente de riqueza + benchmark + sensibilidad | Ninguna |
| 11 | Fijo | Riesgos y decisión | Heatmap + plan de acciones | Imagen final sobria |

## Ejemplo de numeración para el portafolio de referencia

| Página | Contenido |
|---:|---|
| 1 | Resumen ejecutivo |
| 2 | Tesis de inversión |
| 3 | Portafolio en una mirada |
| 4–6 | Fichas de los cinco proyectos |
| 7 | Ventaja Dproperty |
| 8–9 | Calendario de las seis unidades |
| 10 | Flujo y liquidez |
| 11 | Financiamiento |
| 12 | Panamá y ubicación |
| 13 | Retornos y alternativas |
| 14 | Riesgos, controles y recomendación |

---

# 4. Wireframe detallado por módulo

## Página 1 — Resumen ejecutivo

### Regla principal

Esta página debe conservarse **exactamente como fue aprobada**. No añadir fotografías, nuevas métricas, nuevas notas ni cambiar el orden de los elementos.

### Distribución

| Zona | Ancho | Contenido |
|---|---:|---|
| Cabecera izquierda | 64% | Kicker y título |
| Cabecera derecha | 36% | Descripción del escenario |
| Franja de KPI | 100% | Seis tarjetas en retícula 3 × 2 |
| Gráfico principal | 68% | Puente de valor del portafolio |
| Gráfico secundario | 32% | Asignación por estrategia |
| Cierre | 100% | Tres bloques: tesis, retorno y riesgo |

La composición puede adaptarse a A4 vertical, pero el texto, las cifras, los seis KPI, los dos gráficos y el orden narrativo deben permanecer exactamente como fueron aprobados.

### Texto exacto

**Kicker**

`RESUMEN EJECUTIVO 01`

**Título**

`Portafolio y creación de valor`

**Subtítulo**

`Modelo híbrido de seis activos en preconstrucción: cuatro salidas por cesión y dos activos retenidos para renta. Cifras en USD; escenario base del archivo fuente.`

### Tarjetas KPI exactas

| Etiqueta | Valor | Línea secundaria |
|---|---:|---|
| ACTIVOS | 6 unidades | 560.91 m² |
| PRECIO PROMOTOR | $2,151,575 | $3,836/m² |
| VENTAJA DPROPERTY | $272,124 | 12.6% vs caso promotor |
| COSTO FINAL | $2,144,225 | $3,823/m² |
| VALOR PROYECTADO | $2,460,476 | 1.15x sobre costo |
| UTILIDAD FLIPPING | $200,964 | 35.8% sobre abonos |

### Gráfico 1 exacto

**Título:** `Puente de valor del portafolio`

**Tipo:** waterfall.

**Secuencia:**

| Paso | Valor |
|---|---:|
| Lista | $2,151,575 |
| Descuento | ($77,907) |
| Ajuste final | $70,556 |
| Valorización | $316,251 |
| Valor futuro | $2,460,476 |

### Gráfico 2 exacto

**Título:** `Asignación por estrategia · valor futuro`

**Tipo:** donut.

| Estrategia | Valor futuro | Participación |
|---|---:|---:|
| Cesión | $1,490,976 | 60.6% |
| Renta | $969,500 | 39.4% |

Centro del donut:

```text
Valor futuro
$2.5m
```

### Bloques inferiores exactos

**TESIS DE ENTRADA**

> El precio Founders reduce la base de compra en $77,907. Al incorporar diferencias de materiales, cesión y comisión, la ventaja comercial modelada alcanza $272,124.

**ARQUITECTURA DE RETORNO**

> Las cuatro cesiones modelan $434,814 de recuperaciones y $119,449 de utilidad; BIOMA y CDE quedan como núcleo patrimonial y de renta.

**LECTURA DE RIESGO**

> 80.4% del valor proyectado se concentra en Costa del Este. El resultado depende de valorización, liquidez de cesión, cumplimiento de obra y timing de entrega.

**Pie exacto**

```text
DPROPERTY · INVESTMENT ADVISORY
Fuente: FLUJO Y PROYECCION 500 mil · Página 1
```

---

## Página 2 — Tesis de inversión

Esta página conserva la estructura narrativa, pero su título, número de motores, imágenes y texto se adaptan a las estrategias realmente presentes. No se debe mencionar cesión, renta o financiamiento si esas funciones no existen en el portafolio analizado.

### Título

`Una estrategia con tres motores de creación de valor`

### Subtítulo

`La propuesta combina una entrada disciplinada, recuperación de capital mediante cesiones y construcción de patrimonio con renta.`

### Layout

| Zona | Ancho | Contenido |
|---|---:|---|
| Bloque narrativo | 40% | Dos párrafos de tesis |
| Imagen principal | 30% | BIOMA |
| Imagen secundaria | 30% | CDE The Velopers |
| Franja inferior | 100% | Sankey y cuatro conclusiones |

### Texto guía

> La propuesta utiliza $500,000 de capital inicial para construir un portafolio de seis unidades en preconstrucción. La estrategia no trata todos los activos de la misma manera: cuatro unidades están diseñadas para recuperar capital mediante cesión y dos se conservan para construir patrimonio y renta recurrente.

> Esta arquitectura reduce la dependencia de una sola fuente de retorno. La ventaja de entrada disminuye el punto de equilibrio; los pagos durante obra distribuyen el uso del capital; las cesiones aportan liquidez; y BIOMA y CDE permanecen como activos patrimoniales. El financiamiento se incorpora únicamente donde existe un activo retenido y una fuente de renta capaz de cubrir la deuda.

### Gráfico obligatorio

**Tipo:** Sankey Plotly.

```text
$500,000 de capital
├─ Pagos durante obra
│  ├─ 4 activos de cesión → $434,814 recuperado
│  └─ 2 activos retenidos → $969,500 de valor futuro
└─ $200,000 de financiamiento selectivo
   └─ BIOMA + CDE → $4,217/mes de renta neta antes de deuda
```

### Mensajes de cierre

- Entrada con ventaja comercial.
- Despliegue gradual del capital.
- Recuperación parcial antes de entrega.
- Patrimonio y renta al final del horizonte.

---

## Módulo variable — Portafolio en una mirada

### Título

`[U] unidades, [P] proyectos y [E] estrategias de inversión`

### Subtítulo

`La selección combina diferentes tickets, metrajes, fechas de entrega y estrategias de salida.`

### Layout

| Zona | Ancho | Contenido |
|---|---:|---|
| Mosaico visual | 58% | Hasta seis imágenes oficiales de proyectos |
| Resumen de cartera | 42% | Lista de proyectos, unidades y métricas |
| Franja inferior izquierda | 65% | Bubble chart |
| Franja inferior derecha | 35% | Donut geográfico |

### Mosaico de imágenes

- Máximo seis proyectos por página.
- Una imagen representativa por proyecto.
- Si existen más de seis proyectos, repetir este módulo como página de índice visual.
- El orden debe coincidir con el utilizado en las fichas y en el calendario.

Cada imagen debe incluir una etiqueta discreta con proyecto, ubicación y cantidad de unidades incluidas. Un proyecto ocupa una sola imagen aunque contenga varias unidades.

### Gráfico 1

**Tipo:** bubble chart.

- Eje X: área en m².
- Eje Y: precio Founders Dproperty.
- Tamaño de burbuja: valor futuro.
- Color: cesión o renta.
- Etiqueta: proyecto/unidad.
- Tooltip: recámaras, firma, entrega y precio por m².

### Gráfico 2

**Tipo:** donut geográfico.

| Ubicación | Valor futuro | Participación |
|---|---:|---:|
| Costa del Este | $1,978,400 | 80.41% |
| Playa | $482,076 | 19.59% |

### Takeaway

> La cartera diversifica tamaño, precio, plazo y estrategia en el grado que muestran los datos. Cuando exista concentración geográfica, temporal, por desarrollador o por estrategia, debe indicarse de forma explícita y cuantificada.

---

## Módulo variable — Fichas de proyectos y unidades

### Regla de agrupación

- La entidad visual principal es el **proyecto**.
- Dentro de cada proyecto se enumeran todas las unidades incluidas.
- Un proyecto simple con una o dos unidades ocupa media página.
- Dos proyectos simples pueden compartir una página.
- Un proyecto con tres a seis unidades ocupa una página completa.
- Un proyecto con más de seis unidades utiliza páginas de continuación.
- Nunca se separan unidades del mismo proyecto para llenar espacios de manera artificial.

### Layout de un proyecto simple

| Zona | Alto aproximado | Contenido |
|---|---:|---|
| Fotografía | 34% | Imagen principal oficial |
| Identificación | 12% | Proyecto, ubicación, desarrollador y estrategia |
| Unidades | 20% | Hasta dos unidades y sus datos esenciales |
| Finanzas | 22% | Compra, costo, valor futuro, capital y retorno |
| Mini gráfico | 12% | Promotor → Dproperty → costo final → valor futuro |

### Layout de un proyecto complejo

| Zona | Ancho | Contenido |
|---|---:|---|
| Columna visual | 38% | Imagen principal + plano, amenidad o avance |
| Columna analítica | 62% | Tesis del proyecto, métricas y tabla de unidades |
| Franja inferior | 100% | Comparativo de unidades y conclusión |

### Contenido obligatorio por proyecto

- Nombre oficial, ubicación y desarrollador.
- Cantidad de unidades seleccionadas.
- Estrategia o combinación de estrategias.
- Firma, entrega y horizonte.
- Precio promotor y precio Dproperty.
- Ventaja de entrada.
- Costo final y valor futuro.
- Capital requerido antes de entrega.
- Retorno aplicable: utilidad de cesión, yield de renta o ambos, claramente diferenciados.
- Una frase que explique la función del proyecto dentro del portafolio.

### Contenido obligatorio por unidad

| Campo | Formato |
|---|---|
| Unidad | Torre + número/letra o `Por confirmar` |
| Área | `0.00 m²` |
| Recámaras | Número |
| Equipamiento | Texto breve |
| Firma | `MMM-AAAA` |
| Entrega | `MMM-AAAA` |
| Precio Dproperty | `$0,000` |
| Costo final | `$0,000` |
| Valor futuro | `$0,000` |
| Estrategia | Cesión / renta / otra |

### Gráfico obligatorio

Cada proyecto incluye un mini gráfico Plotly:

1. Precio promotor.
2. Precio Dproperty.
3. Costo final.
4. Valor futuro.

Cuando haya varias unidades, usar barras agrupadas por unidad. Mantener una escala común dentro de cada página; si las diferencias de ticket hacen ilegible el gráfico, utilizar índice base 100 y mostrar los valores absolutos como etiquetas.

### Tratamiento fotográfico

- Proyecto simple: una imagen principal; segunda imagen opcional.
- Proyecto complejo: una imagen principal y una secundaria de plano, interior, amenidad o avance.
- Si varias unidades pertenecen al mismo proyecto, evitar repetir el mismo render.
- La imagen debe apoyar la tesis del proyecto y no sustituir información financiera.

### Ejemplo de datos del portafolio de referencia

| Proyecto | Unidades | Área total | Precio Dproperty | Costo final | Valor futuro | Estrategia |
|---|---:|---:|---:|---:|---:|---|
| BIOMA | 1 | 114.00 m² | $510,000 | $525,300 | $598,500 | Renta |
| CDE The Velopers | 1 | 70.00 m² | $308,000 | $317,240 | $371,000 | Renta |
| Sky Parc II | 1 | 85.00 m² | $294,350 | $303,181 | $348,500 | Cesión |
| Sky Parc 4 | 2 | 158.00 m² | $544,000 | $560,320 | $660,400 | Cesión |
| Playa Escondida Torre 100 | 1 | 133.91 m² | $417,318 | $438,184 | $482,076 | Cesión |

---

## Módulo fijo — Ventaja Dproperty

### Título

`La ventaja de entrada reduce la dependencia de valorización futura`

### Subtítulo

`La creación de valor comienza antes de la apreciación: precio Founders, materiales, cesión y comisión forman la ventaja comercial modelada.`

### Layout

| Zona | Ancho | Contenido |
|---|---:|---|
| Gráfico principal | 62% | Waterfall del portafolio |
| Gráfico secundario | 38% | Barras de ventaja por activo |
| Parte inferior | 100% | Párrafo descriptivo y tabla de componentes |

### Gráfico 1

**Tipo:** waterfall.

```text
Precio promotor
→ descuento Founders
→ materiales
→ cesión
→ comisión
→ ventaja comercial total
```

### Gráfico 2

**Tipo:** barras horizontales apiladas.

- Eje Y: activos.
- Eje X: ventaja en USD.
- Segmentos: descuento, materiales, cesión y comisión.
- Etiqueta final: ventaja total y porcentaje sobre precio promotor.

### Texto guía

> La ventaja comercial modelada asciende a $272,124, equivalente a 12.65% del precio promotor. Esta diferencia reduce el punto de equilibrio y proporciona un colchón antes de asumir valorización futura. BIOMA aporta la mayor ventaja absoluta y porcentual. No obstante, los componentes distintos al descuento directo deben vincularse a condiciones contractuales o comerciales verificables antes de presentarse como beneficio definitivo.

### Tabla de apoyo

| Proyecto | Ventaja total | Ventaja sobre precio promotor |
|---|---:|---:|
| BIOMA | $101,220 | 18.04% |
| CDE The Velopers | $43,680 | 13.57% |
| Sky Parc II | $27,575 | 9.37% |
| Sky Parc 4 · 63 m² | $21,168 | 9.41% |
| Sky Parc 4 · 95 m² | $30,120 | 9.44% |
| Playa Escondida | $48,362 | 11.24% |

---

## Módulo variable — Calendario de inflexiones del flujo

### Título

`El flujo cambia en hitos definidos y permanece estable entre cada inflexión`

### Subtítulo

`Cada segmento muestra la cuota o el flujo mensual vigente; cada punto marca un evento que cambia el compromiso financiero o la posición del activo.`

### Layout

| Zona | Ancho | Contenido |
|---|---:|---|
| Franja superior | 100% | Step chart agregado del flujo mensual del portafolio |
| Cuerpo | 100% | Hasta cuatro líneas de tiempo de unidades |
| Franja inferior | 100% | Leyenda, eventos críticos y lectura del periodo |

### Gráfico 1

**Tipo:** step chart Plotly del flujo mensual agregado.

- Eje X: fecha.
- Eje Y: flujo neto mensual recurrente del portafolio.
- Línea escalonada con `line.shape = "hv"`.
- Cada cambio de nivel coincide con una inflexión.
- Los pagos o ingresos extraordinarios se muestran como barras o marcadores verticales, sin confundirse con el flujo mensual recurrente.
- Tooltip: fecha, flujo mensual anterior, evento, monto extraordinario y nuevo flujo mensual.

### Gráfico 2

**Tipo:** línea de tiempo de inflexiones por unidad, preferiblemente D3; Plotly es válido si mantiene la legibilidad.

- Una fila por unidad.
- Máximo cuatro unidades por página.
- Cada punto representa un evento que cambia el flujo o constituye un hito material.
- Entre dos puntos existe un segmento horizontal que representa un período estable.
- Cada segmento debe incluir una nota visible con:

```text
[Mes inicial]–[Mes final]
Cuota mensual: $X/mes
Duración: N meses
Total del período: $Y
```

Si el activo ya genera renta:

```text
[Mes inicial]–[Mes final]
Renta neta: +$X/mes
Cuota hipotecaria: ($Y/mes)
Flujo neto mensual: +$Z/mes
```

Si no existe cuota ni flujo recurrente:

```text
Sin cuota mensual durante este período
```

### Eventos de inflexión

Registrar como punto cualquier evento que cambie el flujo mensual o sea material para la estrategia:

- Reserva.
- Firma de contrato.
- Inicio, cambio o finalización de cuotas mensuales.
- Pago extraordinario.
- Venta o cesión de una propiedad.
- Entrega.
- Pago de saldo contra entrega.
- Desembolso de financiamiento.
- Inicio de cuota hipotecaria.
- Compra de mobiliario o equipamiento.
- Inicio del alquiler.
- Cambio relevante de renta, gastos, ocupación o cuota de deuda.
- Otro compromiso contractual o evento material.

### Reglas de representación

1. Los flujos negativos se muestran debajo de la línea o en rojo; los positivos, arriba o en verde.
2. La firma, venta, entrega, financiamiento y alquiler utilizan símbolos diferentes.
3. Un pago extraordinario aparece como evento puntual; no se convierte visualmente en cuota mensual.
4. Si varios eventos ocurren en la misma fecha, se agrupan en un solo marcador con desglose.
5. Si la cuota permanece igual durante varios meses, se muestra una sola banda continua y una sola nota de período.
6. Al comenzar el alquiler, se crea una nueva inflexión aunque no exista un pago extraordinario, porque cambia el flujo mensual.
7. Si el activo se vende, su línea termina en la fecha de venta y el ingreso neto se identifica como evento.
8. Para PDF, las anotaciones no pueden superponerse. Si hay demasiados eventos, usar llamadas numeradas y una tabla breve debajo.
9. Para HTML, los tooltips contienen el desglose completo y permiten filtrar por proyecto, unidad y tipo de evento.
10. El calendario agregado debe reconciliar exactamente con el flujo mensual del modelo.

### Ejemplo lógico de una línea

| Punto inicial | Período estable hasta el siguiente punto | Punto final |
|---|---|---|
| Firma | Cuota mensual: ($2,500) · 11 meses · total ($27,500) | Extraordinaria: ($25,000) |
| Extraordinaria | Cuota mensual: ($2,500) · 12 meses · total ($30,000) | Entrega + desembolso hipotecario |
| Inicio de renta | Renta neta: $2,828; hipoteca: ($1,478); flujo neto: +$1,350/mes | Próxima revisión o fin del horizonte |

La versión final debe producirse como gráfico Plotly o D3.

### Lógica de cálculo de cada segmento

Para un intervalo comprendido entre las inflexiones \(t_i\) y \(t_{i+1}\):

\[
\text{Flujo mensual vigente}_i
=
\text{renta neta mensual}_i
-
\text{cuota de compra}_i
-
\text{cuota hipotecaria}_i
-
\text{otros costos recurrentes}_i
\]

\[
\text{Total del período}_i
=
\text{Flujo mensual vigente}_i
\times
\text{número de meses del intervalo}
\]

Los pagos e ingresos extraordinarios se registran en el punto de inflexión y no se multiplican por el número de meses.

### Datos mínimos requeridos para generar el calendario

| Campo | Descripción |
|---|---|
| `proyecto_id` | Identificador estable del proyecto |
| `unidad_id` | Identificador estable de la unidad |
| `fecha_evento` | Fecha efectiva del hito |
| `tipo_evento` | Firma, extraordinaria, venta, entrega, hipoteca, renta u otro |
| `flujo_extraordinario` | Entrada positiva o salida negativa en la fecha |
| `flujo_mensual_anterior` | Flujo recurrente antes del evento |
| `flujo_mensual_nuevo` | Flujo recurrente después del evento |
| `cuota_compra` | Cuota mensual del plan de pagos |
| `renta_neta` | Ingreso mensual neto aplicable |
| `cuota_deuda` | Servicio mensual de la deuda |
| `fuente` | Contrato, modelo, dato externo o supuesto |
| `estado` | Confirmado, modelado o pendiente |

### Texto guía

> El calendario debe permitir comprender el portafolio sin revisar cada mes del Excel. Los puntos explican cuándo y por qué cambia el flujo; los segmentos muestran qué cuota o ingreso mensual permanece vigente hasta la siguiente inflexión. De esta manera, el lector distingue compromisos recurrentes, pagos extraordinarios, recuperaciones de capital y el momento en que un activo comienza a producir renta.

### Eventos destacados del portafolio de referencia

- Entrega de Playa Escondida.
- Inyección hipotecaria modelada.
- Entrega de Sky Parc II.
- Entrega de BIOMA.
- Salidas de Sky Parc 4.
- Entrega de CDE.

---

## Módulo fijo — Flujo y liquidez

### Título

`La principal restricción del caso base es la liquidez, no el retorno proyectado`

### Subtítulo

`El modelo alcanza un saldo mínimo de $130.57; una reserva independiente de $50,000 es condición de ejecución.`

### Layout

| Zona | Ancho | Contenido |
|---|---:|---|
| Superior | 100% | Línea de saldo de caja |
| Inferior izquierda | 67% | Flujo mensual de propiedades |
| Inferior derecha | 33% | Semáforo de liquidez y acciones |

### Gráfico 1

**Tipo:** línea de saldo bancario.

- Eje X: 60 meses.
- Eje Y: saldo en USD.
- Línea de referencia: reserva mínima recomendada de $50,000.
- Área roja: saldo inferior a la reserva.
- Anotaciones en eventos de cesión, hipoteca, entrega y equipamiento.

### Gráfico 2

**Tipo:** barras mensuales.

- Verde: entradas.
- Rojo: salidas.
- Etiqueta únicamente en los cinco eventos de mayor magnitud.

### Semáforo

| Indicador | Resultado | Estado |
|---|---:|---|
| Saldo mínimo modelado | $130.57 | Crítico |
| Reserva recomendada | $50,000 | Condición |
| Saldo final | $16,997 | Bajo |
| Intereses acumulados | $25,563 | Positivo |

### Texto guía

> El modelo demuestra capacidad de creación de valor, pero opera con un margen de liquidez insuficiente. Una desviación en fechas de cesión, una entrega adelantada, un gasto no presupuestado o una demora en el crédito podría provocar un déficit temporal. Por esta razón, la reserva de $50,000 no debe considerarse capital adicional para invertir, sino una protección operativa separada.

---

## Módulo fijo — Financiamiento

### Título

`Financiamos patrimonio productivo, no rotación especulativa`

### Subtítulo

`La deuda de $200,000 se aplica únicamente a BIOMA y CDE, los dos activos retenidos y generadores de renta.`

### Layout

| Zona | Ancho | Contenido |
|---|---:|---|
| Columna izquierda | 55% | Funding bridge |
| Columna derecha superior | 45% | Fotografías pequeñas de BIOMA y CDE |
| Columna derecha inferior | 45% | Sensibilidad de cuota y DSCR |
| Franja inferior | 100% | Qué se financia, qué no y por qué |

### Gráfico 1

**Tipo:** funding bridge o sources & uses.

| Uso/fuente | Monto |
|---|---:|
| Saldos de entrega BIOMA + CDE | $572,600 |
| Hipoteca | $200,000 |
| Equity y recuperaciones requeridas | $372,600 |
| Equipamiento pagado como equity | $36,800 |

### Gráfico 2

**Tipo:** gráfico combinado.

- Barras: cuota mensual por escenario.
- Línea: DSCR.
- Línea de referencia: DSCR mínimo 1.50x.

| Escenario | Tasa/plazo | Cuota | DSCR | Neto post deuda |
|---|---|---:|---:|---:|
| Modelo actual | 7.50% / 25 años | $1,478 | 2.85x | $2,739/mes |
| Inversión referencia | 9.25% / 30 años | $1,645 | 2.56x | $2,571/mes |
| Segunda vivienda referencia | 9.00% / 20 años | $1,799 | 2.34x | $2,417/mes |

### Texto guía

> La hipoteca cubre 34.93% de los saldos de entrega de BIOMA y CDE y equivale a un LTV de 20.63% sobre su valor futuro conjunto. La renta neta antes de deuda de $4,216.61 mensuales cubre 2.85 veces la cuota del escenario base. Esta estructura mantiene un apalancamiento conservador y preserva liquidez sin utilizar deuda para ampliar el número de unidades.

### Qué no se financia

- Activos destinados a cesión.
- Pérdidas operativas.
- Nuevas compras fuera de la tesis.
- Mobiliario mediante deuda hipotecaria de largo plazo.

---

## Módulo fijo — Panamá y ubicación

### Título

`Panamá apoya una tesis selectiva, no una apuesta indiscriminada`

### Subtítulo

`El crecimiento económico y la actividad de construcción son favorables, pero la dispersión mensual y geográfica obliga a seleccionar proyecto, precio y salida.`

### Layout

| Zona | Ancho | Contenido |
|---|---:|---|
| Franja superior | 100% | Cuatro KPI de mercado |
| Columna izquierda | 55% | Barras de permisos de construcción |
| Columna derecha | 45% | Mapa/donut de ubicación |
| Franja inferior | 100% | Ventajas y límites frente al mercado |

### KPI

| Indicador | Valor |
|---|---:|
| PIB real Panamá 2026 | 3.8% |
| Permisos ene–may | +34.0% |
| Componente residencial | +21.5% |
| Distrito de Panamá | +20.2% |

### Gráfico 1

**Tipo:** barras agrupadas.

- Comparar valor de permisos 2025 vs. 2026.
- Separar total nacional, residencial y distrito de Panamá.
- Añadir nota: mayo del distrito de Panamá registró -20.1% interanual.

### Gráfico 2

**Tipo:** mapa de Panamá con dos marcadores y donut complementario.

- Costa del Este: 80.41% del valor futuro.
- Playa: 19.59%.

### Imágenes

- Vista aérea o skyline de Costa del Este.
- Imagen de ubicación de Playa Escondida.
- Si se usa mapa, las fotografías pueden aparecer como pequeños recuadros vinculados a cada marcador.

### Texto guía

> Panamá mantiene un marco atractivo para activos denominados en dólares y una perspectiva de crecimiento positiva. Al mismo tiempo, el aumento de permisos puede representar tanto dinamismo como mayor competencia futura. La ventaja de esta estrategia no consiste en asumir que todo el mercado se valorizará, sino en combinar precio de entrada, calidad del desarrollador, unidad, fecha de entrega, profundidad de demanda y una salida definida desde el inicio.

### Fuentes al pie

- Fondo Monetario Internacional.
- INEC Panamá.
- Fecha exacta de consulta.

---

## Módulo fijo — Retornos y alternativas

### Título

`El caso base crea $312,060 de utilidad y cierra con 1.62x de MOIC`

### Subtítulo

`ROI, MOIC, CAGR y TIR responden preguntas distintas y deben presentarse sin mezclarlas.`

### Layout

| Zona | Ancho | Contenido |
|---|---:|---|
| Franja KPI | 100% | Riqueza, utilidad, ROI, MOIC, CAGR y TIR |
| Gráfico izquierdo | 54% | Puente de riqueza |
| Gráfico derecho | 46% | Benchmark de alternativas |
| Franja inferior | 100% | Explicación de métricas y sensibilidad |

### KPI

| Métrica | Resultado |
|---|---:|
| Riqueza final neta | $812,059.94 |
| Utilidad | $312,059.94 |
| ROI total | 62.41% |
| MOIC | 1.62x |
| CAGR normalizado a cinco años | 10.19% |
| TIR almacenada en el modelo | 25.34% |

### Gráfico 1

**Tipo:** waterfall de riqueza final.

```text
Valor de activos retenidos       $969,500
− Hipoteca pendiente            ($200,000)
+ Saldo bancario                  $16,997
+ Intereses acumulados            $25,563
= Riqueza final                  $812,060
```

### Gráfico 2

**Tipo:** barras de valor final de $500,000.

| Alternativa | Valor final |
|---|---:|
| Depósito al 5% | $638,141 |
| Acciones al 10% histórico | $805,255 |
| Portafolio Dproperty | $812,060 |

### Nota metodológica obligatoria

> La TIR de 25.34% corresponde a los flujos inmobiliarios desplegados dentro del modelo y no debe presentarse como retorno anual del capital propio total de $500,000. Para comparar el resultado patrimonial completo durante cinco años, el indicador coherente es el CAGR normalizado de 10.19%.

### Sensibilidad recomendada

Añadir una matriz pequeña con tres variables:

- Valorización final.
- Retraso en cesiones.
- Tasa hipotecaria.

Mostrar escenario conservador, base y favorable.

---

## Módulo fijo — Riesgos, controles y recomendación

### Título

`La oportunidad es ejecutable si se protege la liquidez y se prepara cada salida`

### Subtítulo

`El retorno proyectado depende de controles operativos, contractuales y financieros concretos.`

### Layout

| Zona | Ancho | Contenido |
|---|---:|---|
| Columna izquierda | 58% | Heatmap de riesgos |
| Columna derecha | 42% | Condiciones de aprobación |
| Franja inferior | 70% | Timeline de ejecución |
| Cierre visual | 30% | Imagen sobria de BIOMA o Costa del Este |

### Gráfico 1

**Tipo:** heatmap de probabilidad e impacto.

| Riesgo | Exposición | Control |
|---|---|---|
| Liquidez | Saldo mínimo de $130.57 | Reserva separada de $50,000 |
| Concentración | 80.41% en Costa del Este | Limitar nuevas compras en la zona |
| Cesión | Cuatro salidas requieren comprador | Mercadeo 9–12 meses antes |
| Construcción | Retrasos, calidad y entrega | Seguimiento de hitos y cláusulas |
| Financiamiento | Aprobación futura de $200,000 | Precalificar 12–18 meses antes |
| Modelo | Horizonte y fórmulas pendientes | Auditoría antes de firma |

### Gráfico 2

**Tipo:** timeline Plotly.

1. Confirmación de contratos y unidades.
2. Validación de condiciones de cesión.
3. Seguimiento mensual de caja.
4. Inicio de mercadeo de cada cesión.
5. Precalificación hipotecaria.
6. Entrega, equipamiento y activación de renta.

### Condiciones para avanzar

1. Confirmar precios, unidades, contratos, gastos y fechas.
2. Validar documentalmente cada ventaja Dproperty.
3. Mantener una reserva independiente de al menos $50,000.
4. Iniciar cada cesión 9–12 meses antes de la salida.
5. Precalificar la hipoteca 12–18 meses antes de necesitarla.
6. Mantener DSCR superior a 1.50x.
7. Recalcular el escenario si cambia una fecha o ventaja relevante.
8. Corregir las inconsistencias técnicas antes de presentar al cliente.

### Conclusión

> La estrategia es atractiva porque utiliza $500,000 para construir una posición patrimonial superior al capital inicial, entra con una ventaja comercial, vende cuatro unidades para recuperar liquidez y conserva dos propiedades generadoras de renta. En el caso base, la riqueza final alcanza $812,059.94, con $312,059.94 de utilidad, 62.41% de ROI y 1.62x de MOIC. La principal condición no es aumentar el apalancamiento, sino proteger la liquidez, preparar las cesiones y validar cada supuesto antes de comprometer capital.

---

# 5. Plantilla estándar de ficha por activo

Esta ficha se repite para cualquier futuro proyecto.

## Información visual

- Imagen principal.
- Imagen secundaria opcional: plano, amenidad o avance.
- Crédito/fuente.
- Etiqueta si corresponde a render.

## Información de identificación

| Campo | Formato |
|---|---|
| Proyecto | Nombre oficial |
| Ubicación | Zona y ciudad |
| Unidad | Torre + número/letra |
| Área | `0.00 m²` |
| Recámaras | Número |
| Equipamiento | Texto corto |
| Firma | `MMM-AAAA` |
| Entrega | `MMM-AAAA` |
| Estrategia | Cesión / renta / otra |

## Información financiera

| Campo | Formato |
|---|---|
| Precio promotor | `$0,000` |
| Precio Dproperty | `$0,000` |
| Ventaja de entrada | `$0,000 · 0.0%` |
| Costo final | `$0,000` |
| Valor futuro | `$0,000` |
| Valor futuro/m² | `$0,000/m²` |
| Capital antes de entrega | `$0,000` |
| Utilidad de cesión o renta anual | `$0,000` |
| ROI o yield aplicable | `0.0%` |

## Mini gráfico

Barra comparativa:

```text
Promotor → Dproperty → Costo final → Valor futuro
```

No mostrar ROI de cesión en una ficha de renta como si fuera la estrategia seleccionada. Los escenarios alternativos deben distinguirse visualmente.

---

# 6. Comportamiento dinámico para futuros portafolios

## Según número de proyectos y unidades

| Composición | Tratamiento |
|---|---|
| 1 proyecto, 1–2 unidades | Una ficha de proyecto a ancho completo con dos imágenes |
| 2 proyectos simples | Dos fichas de media página |
| 3+ proyectos simples | Dos proyectos por página |
| Proyecto con 3–6 unidades | Una página completa para ese proyecto |
| Proyecto con más de 6 unidades | Página principal + continuaciones de hasta seis unidades |
| Más de 6 proyectos | Repetir página de índice visual |
| Más de 4 unidades | Repetir calendario, máximo cuatro líneas de unidad por página |

La cantidad de páginas aumenta con la complejidad. No se comprime texto, gráficos o fotografías para forzar un número predeterminado de páginas.

## Según número de ubicaciones

- Una ubicación: sustituir donut por mapa de microzona y distancias relevantes.
- Dos a cuatro ubicaciones: mapa + donut.
- Más de cuatro ubicaciones: mapa + barras horizontales por exposición.

## Según estrategias

- Una sola estrategia: no usar donut; usar una línea de tiempo de ejecución.
- Dos estrategias: donut.
- Tres o más: barra apilada al 100% para evitar demasiados segmentos circulares.

## Según horizonte

- Hasta 36 meses: calendario y flujo mensual.
- Entre 37 y 84 meses: calendario de inflexiones mensual con agregación anual complementaria.
- Más de 84 meses: conservar fechas exactas de inflexión, pero resumir los períodos estables por trimestre o año cuando la cuota no cambie.

## Según densidad de eventos

- Hasta 8 inflexiones por unidad: mostrar etiquetas directas.
- Entre 9 y 15: alternar etiquetas arriba y abajo de la línea.
- Más de 15: usar marcadores numerados y tabla de eventos.
- Si varias unidades comparten el mismo plan, se pueden agrupar visualmente, pero el tooltip y la tabla deben conservar el desglose individual.

---

# 7. Jerarquía de datos

Cada cifra debe tener una categoría visible:

| Categoría | Ejemplo | Tratamiento |
|---|---|---|
| Dato contractual | Precio, metraje, plan de pagos | Mostrar sin sombreado de supuesto |
| Resultado del modelo | ROI, saldo, valor futuro | Etiqueta `Escenario base` |
| Dato externo | PIB, permisos, tasa bancaria | Citar fuente y fecha |
| Recomendación | Reserva de $50,000 | Acento dorado |
| Dato pendiente | Unidad por confirmar | Acento rojo suave o etiqueta `Por confirmar` |

No mezclar resultados del modelo con datos contractuales. Un valor futuro proyectado debe verse diferente de un precio firmado.

---

# 8. Controles de calidad antes de publicar

## Datos

- Todos los proyectos del Excel aparecen en el informe.
- No existe ningún activo adicional heredado de otro cliente.
- Metraje × precio/m² reconcilia con precio total o la diferencia está explicada.
- Planes de pago suman 100% del precio aplicable.
- Firma, cesión y entrega están ordenadas cronológicamente.
- ROI, MOIC, CAGR y TIR utilizan horizontes consistentes.
- El flujo de caja no contiene valores cacheados de un escenario anterior.

## Contenido

- La página 1 coincide exactamente con el resumen aprobado.
- Cada foto corresponde al proyecto indicado.
- Cada afirmación de mercado tiene fuente y fecha.
- Cada recomendación está diferenciada del resultado financiero.
- No se utilizan expresiones como `retorno garantizado`, `inversión segura` o `Panamá siempre se valoriza`.
- El informe explica qué se financia y qué no se financia.
- Los principales riesgos están visibles antes de la recomendación final.

## Visual

- La fuente principal es Helvetica.
- El cuerpo está entre 12 y 13 pt.
- No hay texto menor a 9 pt, incluido el disclaimer.
- Ninguna tabla se corta.
- Los gráficos utilizan la misma paleta y formatos numéricos.
- Los gráficos interactivos y estáticos reconcilian entre sí.
- El calendario muestra la cuota o flujo mensual vigente entre cada par de inflexiones.
- Toda renta comienza con una inflexión visible y modifica el flujo mensual posterior.
- Cifras negativas se muestran entre paréntesis o en rojo, de forma consistente.
- Las imágenes conservan su proporción.
- El documento se renderiza en A4 vertical sin escalado posterior.
- El PDF se revisa página por página después de renderizar.

---

# 9. Fuentes del informe actual

## Fuente financiera

- Dproperty, **FLUJO Y PROYECCIÓN 500 mil**, escenario base con fecha de corte 23-jul-2026.

## Fuentes externas

1. [Fondo Monetario Internacional — Panama country page](https://www.imf.org/en/countries/pan)
2. [INEC Panamá — Estadísticas de construcción, enero-mayo 2025-2026](https://www.inec.gob.pa/archivos/A0705547520260629134245Informe%20completo%2C%20estad%C3%ADsticas%20industriales%2C%20construcci%C3%B3n%20mayo%202025-26.pdf)
3. [Superintendencia de Bancos de Panamá — Informe de Estabilidad Financiera 2025](https://www.superbancos.gob.pa/documentos/financiera_y_estadistica/estudios/IEF-II-Semestre-2025.pdf?v=6.1)
4. [Davibank Panamá — Préstamos hipotecarios, tasas y tarifarios](https://www.davibank.pa/es/banca-personal/tasas-y-tarifarios/prstamos-hipotecarios.html)
5. [Banco Nacional de Panamá — Préstamo hipotecario](https://www.banconal.com.pa/productos/prestamos/prestamo-hipotecario/)
6. [S&P Dow Jones Indices — S&P 500 brochure](https://www.spglobal.com/spdji/en/documents/additional-material/sp-500-brochure.pdf)

Las cifras de mercado y las tasas bancarias deben volver a verificarse en la fecha de producción de cada informe.

---

# 10. Disclaimer estándar

> Este documento es un análisis de escenario basado en datos y fórmulas suministrados por Dproperty y fuentes externas identificadas. No constituye garantía de rentabilidad, oferta de valores, asesoría legal o fiscal, ni aprobación de financiamiento. Los resultados dependen de precios, costos, cumplimiento de obra, liquidez de cesión, ocupación, renta, tasas, gastos, impuestos y fechas efectivas. Antes de invertir deben validarse contratos, unidades, planes de pago, condiciones de cesión, financiamiento y supuestos de mercado.
