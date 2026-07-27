---
title: Manual estándar para construir el Excel de Flujo y Proyección Inmobiliaria
project: Dproperty Private Collection
document_type: Manual de construcción y especificación funcional
language: es
version: 1.0
date: 2026-07-27
status: Aprobado como especificación replicable
source_example: Dproperty_Flujo_y_Proyeccion_4_Proyectos_con_Nayamara.xlsx
---

# Manual estándar para construir el Excel de Flujo y Proyección Inmobiliaria

## 1. Objetivo del documento

Este documento explica, con suficiente detalle para que otra persona o una IA pueda reconstruir el modelo, cómo crear un Excel de inversión inmobiliaria con el mismo propósito, lenguaje visual y lógica financiera del archivo de referencia de Dproperty.

El modelo debe poder adaptarse a:

- Cualquier cliente.
- Cualquier capital inicial.
- Cualquier capacidad máxima de aporte mensual.
- Cualquier número de apartamentos o posiciones de inversión.
- Cualquier combinación de proyectos.
- Estrategias de cesión antes de entrega, reventa posterior a entrega, retención para renta de largo plazo o renta de corto plazo.
- Pagos iniciales, cuotas mensuales, abonos extraordinarios y saldos a entrega diferentes para cada unidad.
- Operaciones con o sin financiamiento.
- Horizontes de análisis variables.
- Fechas de salida distintas para cada activo.

El archivo debe seguir siendo fácil de leer para un cliente, pero también debe ser auditable: cada resultado debe poder rastrearse hasta un dato de entrada, una fuente o una fórmula visible.

## 2. Resultado esperado

El libro debe contener dos hojas visibles:

1. `proyectos`: ficha comparativa y financiera de todas las unidades.
2. `FLUJO`: calendario mensual consolidado, liquidez, financiamiento, retornos y resultados.

Para que el archivo sea realmente escalable, se recomienda una tercera hoja técnica oculta:

3. `EVENTOS`: base normalizada con un registro por movimiento de caja.

Si el entregable debe tener exactamente dos hojas, la tabla técnica de eventos puede colocarse debajo del área principal de `FLUJO` y mantenerse agrupada u oculta. La presentación visible para el cliente seguirá siendo de dos hojas.

## 3. Principios obligatorios

### 3.1 Separar entradas, fórmulas y resultados

No se deben escribir precios, porcentajes, tasas, fechas o costos directamente dentro de fórmulas.

Cada supuesto debe existir en una celda o columna claramente identificada. Las fórmulas deben referenciar esas celdas.

Ejemplo correcto:

```excel
=[@Precio_Negociado]*(1+[@Inc_Materiales_DP])
```

Ejemplo incorrecto:

```excel
=[@Precio_Negociado]*1.05
```

En el segundo caso no queda claro qué representa el 5% ni cómo actualizarlo.

### 3.2 Usar fechas reales

Las fechas deben guardarse como fechas de Excel, no como texto.

La línea temporal debe construirse con el primer día de cada mes:

```excel
=EDATE(Fecha_Inicio_Modelo,Numero_Mes-1)
```

El formato visible recomendado es:

```text
mmm-yy
```

Ejemplo: `ago-26`.

### 3.3 No confundir capacidad con aporte

La capacidad mensual del cliente es el máximo que puede aportar, no necesariamente el dinero que debe transferir todos los meses.

El modelo debe diferenciar:

- `Capacidad_Mensual`: máximo permitido.
- `Aporte_Real_Mensual`: monto efectivamente necesario.
- `Compromiso_Mensual_Proyectos`: cuotas obligatorias de proyectos.
- `Margen_Mensual`: capacidad menos compromisos.
- `Necesidad_Extraordinaria`: capital adicional que no puede cubrirse con la capacidad mensual.

### 3.4 No mezclar retornos sin apalancamiento y retornos del inversionista

El modelo debe calcular y etiquetar separadamente:

- TIR del activo sin financiamiento.
- TIR del patrimonio del inversionista después de financiamiento.
- ROI acumulado.
- MOIC.
- Renta neta.
- Liquidez mínima requerida.

Nunca se debe presentar una TIR que excluye desembolsos de hipoteca, servicio de deuda o saldo hipotecario como si fuera la TIR final del capital del cliente.

### 3.5 No tratar supuestos como condiciones confirmadas

Cada dato material debe tener un estado:

- `Confirmado por promotor`.
- `Confirmado por banco`.
- `Supuesto Dproperty`.
- `Pendiente de confirmar`.

Los supuestos de valorización, renta, costos de cesión, financiamiento y fechas de salida deben identificarse claramente.

## 4. Convenciones técnicas

### 4.1 Compatibilidad

Construir para Microsoft Excel 365 siempre que sea posible.

Las fórmulas de este manual están escritas con nombres de funciones en inglés y comas, porque así se almacenan de forma estándar en archivos `.xlsx`. Excel en español puede mostrarlas traducidas y utilizar punto y coma según la configuración regional.

### 4.2 Moneda y unidades

- Moneda base: USD.
- Importes: valores numéricos, nunca texto con `$`.
- Porcentajes: valores decimales; por ejemplo, `0.05` representa 5%.
- Metraje: m².
- Horizonte: meses.
- Tasas hipotecarias e intereses: tasas anuales nominales, salvo indicación expresa.

### 4.3 Formatos numéricos

Importes:

```text
$#,##0.00;[Red]($#,##0.00);-
```

Importes resumidos sin centavos:

```text
$#,##0;[Red]($#,##0);-
```

Porcentajes:

```text
0.00%
```

Metraje:

```text
0.00
```

Meses y cantidades:

```text
0
```

## 5. Sistema visual

El archivo de referencia usa una estética sobria en blanco, negro y grises, con colores funcionales para diferenciar entradas, liquidez, deuda y advertencias.

### 5.1 Tipografía

Usar `Century Gothic` como tipografía principal del libro, con `Arial` como alternativa compatible.

No mezclar Calibri, Arial y Century Gothic sin una razón funcional.

Jerarquía:

| Uso | Tamaño | Peso |
|---|---:|---|
| Título principal | 24 pt | Negrita |
| Encabezados de sección | 16 pt | Negrita |
| Encabezados de columna | 13–14 pt | Negrita |
| Texto y cifras de tabla | 11–12 pt | Regular |
| KPI principal | 14–16 pt | Negrita |
| Nota o descargo | 9–10 pt | Regular o negrita moderada |

### 5.2 Paleta

| Función | Color |
|---|---|
| Texto principal | `#000000` |
| Fondo principal | `#FFFFFF` |
| Entradas editables importantes | `#FFD966` |
| Campos vinculados o selección de estrategia | `#D9E2F3` |
| Liquidez y aportes disponibles | `#00B050` |
| Deuda, hipoteca o déficit | `#FF0000` |
| Resultado destacado o advertencia | `#EEEDB0` |
| Gris auxiliar | `#E7E6E6` |

### 5.3 Convención de celdas

- Entradas editables: fuente azul o fondo amarillo.
- Fórmulas: fuente negra.
- Referencias entre hojas: fuente verde si se aplica una convención financiera estricta.
- Deuda o saldos negativos relevantes: rojo.
- Resultados principales: negrita y, cuando corresponda, fondo negro con texto blanco o fondo `#EEEDB0`.
- No usar color como único indicador; siempre incluir una etiqueta.

### 5.4 Bordes y estructura

- Evitar bordes decorativos alrededor de todas las celdas.
- Usar bordes finos para separar registros.
- Usar borde medio superior o inferior para totales.
- Usar borde medio alrededor de bloques de decisión.
- Ocultar las líneas de cuadrícula.
- Inmovilizar filas y columnas para mantener visibles los identificadores del activo.

En `proyectos`, la inmovilización recomendada es `C14`: quedan visibles las filas de encabezado y las columnas de cantidad/proyecto.

## 6. Datos del cliente y del escenario

Crear un bloque de entradas con nombres definidos. Puede ubicarse en la parte superior de `FLUJO` y reflejarse en `proyectos`.

| Nombre definido | Descripción | Tipo |
|---|---|---|
| `Cliente_Nombre` | Nombre del cliente | Texto |
| `Analista_Nombre` | Responsable Dproperty | Texto |
| `Fecha_Modelo` | Fecha de preparación | Fecha |
| `Fecha_Inicio_Modelo` | Primer mes del flujo | Fecha |
| `Horizonte_Meses` | Número de meses a proyectar | Entero |
| `Fecha_Objetivo_Salida` | Fecha solicitada por el cliente | Fecha |
| `Capital_Inicial` | Capital disponible al inicio | USD |
| `Capacidad_Mensual` | Máximo que puede aportar por mes | USD |
| `Reserva_Minima` | Caja mínima que debe conservarse | USD |
| `Modo_Aporte` | `Fijo` o `Hasta límite` | Lista |
| `Tasa_Caja_Anual` | Interés sobre caja positiva | % |
| `Tasa_Descuento` | Tasa para VAN | % |
| `Escenario` | Base, Conservador u Optimista | Lista |
| `Tasa_Hipoteca_Default` | Tasa anual de referencia | % |
| `Plazo_Hipoteca_Default` | Plazo en años | Entero |

Validaciones:

- `Horizonte_Meses` debe ser mayor que cero.
- `Capital_Inicial`, `Capacidad_Mensual` y `Reserva_Minima` no pueden ser negativos.
- `Fecha_Objetivo_Salida` debe ser posterior a `Fecha_Inicio_Modelo`.
- `Modo_Aporte` solo puede ser `Fijo` o `Hasta límite`.

## 7. Hoja `proyectos`

## 7.1 Propósito

Esta hoja reúne la información comercial, contractual, operativa y financiera de cada unidad.

Cada apartamento debe ocupar una fila independiente, aunque dos apartamentos pertenezcan al mismo proyecto.

No usar el nombre del proyecto como identificador único. Crear un `ID_Activo` único.

Ejemplos:

```text
BIO-97-01
PLY-T200-1403
SKY-16B
NAY-05010
```

## 7.2 Encabezado

La parte superior debe incluir:

- Logo de Dproperty.
- Título: `PROYECTOS EN PRECONSTRUCCIÓN`.
- Cliente.
- Fecha.
- Preparado por.
- Escenario.
- Capital inicial.
- Capacidad mensual.
- Horizonte.

La fecha debe ser una fecha real o una fórmula válida:

```excel
=TODAY()
```

No usar una fórmula incompleta como `=`, porque genera errores de compatibilidad.

## 7.3 Tabla principal

Crear una Tabla de Excel llamada `tblProyectos`.

La tabla debe expandirse automáticamente al agregar unidades. No usar rangos fijos como `14:17`.

### Bloque A: identificación y características

| Columna técnica | Etiqueta visible | Tipo | Regla |
|---|---|---|---|
| `ID_Activo` | ID | Entrada | Único y obligatorio |
| `Incluir` | Incluir | Lista | Sí/No |
| `Cantidad` | Cantidad | Entrada | Normalmente 1 |
| `Proyecto` | Proyecto | Entrada | Obligatorio |
| `Promotor` | Promotor | Entrada | Texto |
| `Ubicacion` | Ubicación | Entrada | Texto |
| `Fecha_Lanzamiento` | Fecha lanzamiento | Entrada | Fecha |
| `Fecha_Firma` | Fecha firma | Entrada | Fecha |
| `Fecha_Entrega` | Entrega estimada | Entrada | Fecha |
| `Anios_Hasta_Entrega` | Años | Fórmula | Diferencia entre firma y entrega |
| `Recamaras` | # recámaras | Entrada | Número |
| `Unidad` | Unidad | Entrada | Texto |
| `Metraje_m2` | Metraje | Entrada | > 0 |
| `Equipamiento_Descripcion` | Equipamiento | Entrada | Texto |
| `Estrategia` | Operación | Lista | Cesión/Renta LP/Renta CP/Reventa |
| `Estado_Dato` | Estado | Lista | Confirmado/Supuesto/Pendiente |
| `Fuente` | Fuente | Entrada | Archivo, lista o URL |

Fórmula para años:

```excel
=IFERROR(YEARFRAC([@Fecha_Firma],[@Fecha_Entrega]),0)
```

### Bloque B: precio y beneficio Dproperty

| Columna | Tipo |
|---|---|
| `Precio_Lista` | Entrada |
| `Precio_m2_Lista` | Fórmula |
| `Precio_Negociado` | Entrada |
| `Precio_m2_Negociado` | Fórmula |
| `Descuento_USD` | Fórmula |
| `Descuento_Pct` | Fórmula |
| `Inc_Materiales_Promotor_Pct` | Entrada |
| `Inc_Materiales_Promotor_USD` | Fórmula |
| `Inc_Materiales_DP_Pct` | Entrada |
| `Inc_Materiales_DP_USD` | Fórmula |
| `Ahorro_Materiales` | Fórmula |
| `Cesion_Promotor_Pct` | Entrada |
| `Cesion_Promotor_USD` | Fórmula |
| `Cesion_DP_Pct` | Entrada |
| `Cesion_DP_USD` | Fórmula |
| `Ahorro_Cesion` | Fórmula |
| `Comision_Venta_Estandar_Pct` | Entrada |
| `Comision_Venta_Estandar_USD` | Fórmula |
| `Comision_Venta_DP_Pct` | Entrada |
| `Comision_Venta_DP_USD` | Fórmula |
| `Ahorro_Comision` | Fórmula |
| `Ahorro_Total_DP` | Fórmula |
| `Ahorro_Total_Pct_Lista` | Fórmula |

Fórmulas:

```excel
Precio_m2_Lista
=IFERROR([@Precio_Lista]/[@Metraje_m2],0)

Precio_m2_Negociado
=IFERROR([@Precio_Negociado]/[@Metraje_m2],0)

Descuento_USD
=[@Precio_Lista]-[@Precio_Negociado]

Descuento_Pct
=IFERROR([@Descuento_USD]/[@Precio_Lista],0)

Inc_Materiales_Promotor_USD
=[@Precio_Lista]*[@Inc_Materiales_Promotor_Pct]

Inc_Materiales_DP_USD
=[@Precio_Negociado]*[@Inc_Materiales_DP_Pct]

Ahorro_Materiales
=[@Inc_Materiales_Promotor_USD]-[@Inc_Materiales_DP_USD]

Cesion_Promotor_USD
=[@Precio_Lista]*[@Cesion_Promotor_Pct]

Cesion_DP_USD
=[@Precio_Negociado]*[@Cesion_DP_Pct]

Ahorro_Cesion
=[@Cesion_Promotor_USD]-[@Cesion_DP_USD]

Comision_Venta_Estandar_USD
=[@Precio_Venta_Bruto]*[@Comision_Venta_Estandar_Pct]

Comision_Venta_DP_USD
=[@Precio_Venta_Bruto]*[@Comision_Venta_DP_Pct]

Ahorro_Comision
=[@Comision_Venta_Estandar_USD]-[@Comision_Venta_DP_USD]

Ahorro_Total_DP
=[@Descuento_USD]+[@Ahorro_Materiales]+[@Ahorro_Cesion]+[@Ahorro_Comision]

Ahorro_Total_Pct_Lista
=IFERROR([@Ahorro_Total_DP]/[@Precio_Lista],0)
```

### Bloque C: precio de compra final

| Columna | Tipo |
|---|---|
| `Precio_Compra_Base` | Fórmula |
| `Inc_Materiales_Aplicado_Pct` | Fórmula |
| `Inc_Materiales_Aplicado_USD` | Fórmula |
| `Precio_Compra_Final` | Fórmula |
| `Precio_m2_Final` | Fórmula |

Fórmulas:

```excel
Precio_Compra_Base
=[@Precio_Negociado]

Inc_Materiales_Aplicado_Pct
=[@Inc_Materiales_DP_Pct]

Inc_Materiales_Aplicado_USD
=[@Precio_Compra_Base]*[@Inc_Materiales_Aplicado_Pct]

Precio_Compra_Final
=[@Precio_Compra_Base]+[@Inc_Materiales_Aplicado_USD]

Precio_m2_Final
=IFERROR([@Precio_Compra_Final]/[@Metraje_m2],0)
```

No se debe eliminar el incremento de materiales simplemente porque existe un descuento. Debe mostrarse por separado para que el cliente vea si el incremento absorbe parte del descuento.

### Bloque D: plan de pagos resumido

El plan detallado se almacenará en `tblEventos`. En `tblProyectos` se muestra el resumen:

| Columna | Tipo |
|---|---|
| `Abono_Inicial_Requerido_Pct` | Entrada |
| `Abono_Inicial_Requerido_USD` | Fórmula |
| `Reserva_USD` | Entrada |
| `Firma_Pct` | Entrada |
| `Firma_USD` | Fórmula |
| `Monto_Cuotas_USD` | Entrada o fórmula |
| `Numero_Cuotas` | Entrada |
| `Cuota_Mensual_USD` | Fórmula |
| `Extraordinarios_USD` | Fórmula desde eventos |
| `Pagado_Antes_Entrega_USD` | Fórmula desde eventos |
| `Saldo_Entrega_USD` | Fórmula |
| `Prepago_Adicional_USD` | Entrada |

Fórmulas:

```excel
Abono_Inicial_Requerido_USD
=[@Precio_Negociado]*[@Abono_Inicial_Requerido_Pct]

Firma_USD
=MAX(0,[@Precio_Negociado]*[@Firma_Pct]-[@Reserva_USD])

Cuota_Mensual_USD
=IFERROR(([@Monto_Cuotas_USD]-[@Prepago_Adicional_USD])/[@Numero_Cuotas],0)

Saldo_Entrega_USD
=MAX(0,[@Precio_Compra_Final]-[@Pagado_Antes_Entrega_USD])
```

Regla:

```text
Reserva + firma + cuotas + extraordinarios + saldo a entrega
= precio de compra final
```

La diferencia debe ser cero, dentro de una tolerancia máxima de USD 1.

### Bloque E: cesión o reventa

| Columna | Tipo |
|---|---|
| `Fecha_Salida` | Entrada |
| `Precio_m2_Salida` | Entrada |
| `Precio_Venta_Bruto` | Fórmula o entrada directa |
| `Pagado_Hasta_Salida` | Fórmula desde eventos |
| `Saldo_Promotor_Salida` | Fórmula |
| `Costo_Cesion_Salida_USD` | Fórmula |
| `Comision_Venta_USD` | Fórmula |
| `Impuestos_Venta_USD` | Entrada o fórmula documentada |
| `Otros_Costos_Salida_USD` | Entrada |
| `Efectivo_Neto_Cesion` | Fórmula |
| `Utilidad_Neta_Cesion` | Fórmula |
| `ROI_Cesion` | Fórmula |
| `TIR_Activo` | Fórmula sobre eventos |

Fórmulas:

```excel
Precio_Venta_Bruto
=[@Precio_m2_Salida]*[@Metraje_m2]

Saldo_Promotor_Salida
=MAX(0,[@Precio_Compra_Final]-[@Pagado_Hasta_Salida])

Costo_Cesion_Salida_USD
=[@Precio_Negociado]*[@Cesion_DP_Pct]

Comision_Venta_USD
=[@Precio_Venta_Bruto]*[@Comision_Venta_DP_Pct]

Efectivo_Neto_Cesion
=[@Precio_Venta_Bruto]
-[@Saldo_Promotor_Salida]
-[@Costo_Cesion_Salida_USD]
-[@Comision_Venta_USD]
-[@Impuestos_Venta_USD]
-[@Otros_Costos_Salida_USD]

Utilidad_Neta_Cesion
=[@Efectivo_Neto_Cesion]-[@Pagado_Hasta_Salida]

ROI_Cesion
=IFERROR([@Utilidad_Neta_Cesion]/[@Pagado_Hasta_Salida],0)
```

La fecha de salida debe ser una entrada explícita. No debe quedar escondida en una fórmula como “dos meses antes de entrega” si esa no es una condición confirmada.

### Bloque F: renta de largo plazo

| Columna | Tipo |
|---|---|
| `Costo_Equipamiento_USD` | Entrada o fórmula |
| `Renta_Bruta_Mensual` | Entrada |
| `HOA_USD_m2` | Entrada |
| `HOA_Mensual_USD` | Fórmula |
| `Impuesto_Inmueble_Mensual` | Fórmula o entrada |
| `Vacancia_Pct` | Entrada |
| `Mantenimiento_Pct_Renta` | Entrada |
| `Administracion_Renta_Pct` | Entrada |
| `Comision_Colocacion_Anual_USD` | Fórmula |
| `Gastos_Renta_Mensual` | Fórmula |
| `Renta_Neta_Mensual` | Fórmula |
| `Renta_Neta_Anual` | Fórmula |
| `Yield_Neto` | Fórmula |
| `Fecha_Inicio_Renta` | Entrada |

Fórmulas base:

```excel
HOA_Mensual_USD
=[@HOA_USD_m2]*[@Metraje_m2]

Comision_Colocacion_Anual_USD
=[@Renta_Bruta_Mensual]

Gastos_Renta_Mensual
=[@HOA_Mensual_USD]
+[@Impuesto_Inmueble_Mensual]
+([@Renta_Bruta_Mensual]*[@Vacancia_Pct])
+([@Renta_Bruta_Mensual]*[@Mantenimiento_Pct_Renta])
+([@Renta_Bruta_Mensual]*[@Administracion_Renta_Pct])
+([@Comision_Colocacion_Anual_USD]/12)

Renta_Neta_Mensual
=[@Renta_Bruta_Mensual]-[@Gastos_Renta_Mensual]

Renta_Neta_Anual
=[@Renta_Neta_Mensual]*12

Yield_Neto
=IFERROR([@Renta_Neta_Anual]/([@Precio_Compra_Final]+[@Costo_Equipamiento_USD]),0)
```

La fórmula original del ejemplo para impuesto mensual es:

```excel
=MAX(0,((Precio_Compra_Final-120000)*0.5%)/12)
```

Esta regla debe quedar como supuesto editable y debe verificarse legal y fiscalmente antes de usarla con un cliente.

### Bloque G: renta de corto plazo

| Columna | Tipo |
|---|---|
| `Tarifa_Diaria` | Entrada |
| `Ocupacion_Pct` | Entrada |
| `Dias_Ocupados` | Fórmula |
| `Ingreso_CP_Mensual` | Fórmula |
| `Property_Management_Pct` | Entrada |
| `Property_Management_USD` | Fórmula |
| `Gastos_CP_Mensual` | Fórmula |
| `Ingreso_CP_Neto_Mensual` | Fórmula |
| `Ingreso_CP_Neto_Anual` | Fórmula |
| `Yield_CP_Neto` | Fórmula |

Fórmulas:

```excel
Dias_Ocupados
=[@Ocupacion_Pct]*30

Ingreso_CP_Mensual
=[@Tarifa_Diaria]*[@Dias_Ocupados]

Property_Management_USD
=[@Ingreso_CP_Mensual]*[@Property_Management_Pct]

Gastos_CP_Mensual
=[@HOA_Mensual_USD]
+[@Property_Management_USD]
+[@Impuesto_Inmueble_Mensual]
+([@Ingreso_CP_Mensual]*[@Mantenimiento_Pct_Renta])

Ingreso_CP_Neto_Mensual
=[@Ingreso_CP_Mensual]-[@Gastos_CP_Mensual]

Ingreso_CP_Neto_Anual
=[@Ingreso_CP_Neto_Mensual]*12

Yield_CP_Neto
=IFERROR([@Ingreso_CP_Neto_Anual]/([@Precio_Compra_Final]+[@Costo_Equipamiento_USD]),0)
```

### Bloque H: financiamiento

| Columna | Tipo |
|---|---|
| `Usa_Financiamiento` | Lista Sí/No |
| `Fecha_Desembolso` | Entrada |
| `LTV_Pct` | Entrada |
| `Monto_Prestamo` | Fórmula o entrada |
| `Tasa_Hipoteca_Anual` | Entrada |
| `Plazo_Hipoteca_Anios` | Entrada |
| `Cuota_Hipoteca_Mensual` | Fórmula |
| `Fecha_Primera_Cuota` | Entrada |
| `Saldo_Hipoteca_Horizonte` | Fórmula |

Fórmulas:

```excel
Monto_Prestamo
=IF([@Usa_Financiamiento]="Sí",
MIN([@Saldo_Entrega_USD],[@Precio_Compra_Final]*[@LTV_Pct]),
0)

Cuota_Hipoteca_Mensual
=IF([@Monto_Prestamo]>0,
-PMT([@Tasa_Hipoteca_Anual]/12,[@Plazo_Hipoteca_Anios]*12,[@Monto_Prestamo]),
0)

Saldo_Hipoteca_Horizonte
=IF([@Monto_Prestamo]>0,
MAX(0,-FV(
[@Tasa_Hipoteca_Anual]/12,
[@Cuotas_Pagadas_Hasta_Horizonte],
-[@Cuota_Hipoteca_Mensual],
[@Monto_Prestamo]
)),
0)
```

Nunca escribir `7.5%` o `25*12` directamente dentro de `PMT`; deben provenir de columnas o supuestos.

## 8. Tabla técnica `tblEventos`

## 8.1 Por qué es necesaria

El archivo de referencia calcula reservas, firmas, cuotas y tres extraordinarios mediante posiciones fijas. Esa lógica funciona para un caso específico, pero deja de ser fiable cuando:

- Un proyecto tiene más o menos abonos extraordinarios.
- Las cuotas empiezan en otro mes.
- La cesión ocurre antes de terminar las cuotas.
- La entrega se retrasa.
- Hay varios préstamos con fechas distintas.
- El cliente compra muchas unidades.

La solución escalable es almacenar cada movimiento como un evento.

## 8.2 Columnas

Crear una tabla llamada `tblEventos`:

| Columna | Descripción |
|---|---|
| `ID_Evento` | Identificador único |
| `ID_Activo` | Relación con `tblProyectos` |
| `Fecha` | Fecha real del movimiento |
| `Mes` | Primer día del mes |
| `Tipo_Evento` | Reserva, firma, cuota, extraordinario, entrega, etc. |
| `Categoria` | Construcción, financiamiento, renta, salida, costos |
| `Descripcion` | Texto explicativo |
| `Importe_Bruto` | Valor positivo |
| `Direccion` | Entrada o Salida |
| `Flujo_Caja_USD` | Importe con signo |
| `Incluye_TIR_Activo` | 1/0 |
| `Incluye_TIR_Equity` | 1/0 |
| `Cuenta_Contra_Capacidad` | 1/0 |
| `Confirmado` | Sí/No |
| `Fuente` | Fuente del dato |

Fórmulas:

```excel
Mes
=DATE(YEAR([@Fecha]),MONTH([@Fecha]),1)

Flujo_Caja_USD
=IF([@Direccion]="Salida",-ABS([@Importe_Bruto]),ABS([@Importe_Bruto]))
```

## 8.3 Tipos de eventos

Usar una lista controlada:

- Reserva.
- Firma.
- Cuota mensual.
- Abono extraordinario.
- Saldo a entrega.
- Gastos legales.
- Cierre.
- Mobiliario.
- Desembolso hipotecario.
- Cuota hipotecaria.
- Renta bruta.
- Gastos de renta.
- Cesión.
- Reventa.
- Comisión de venta.
- Impuestos de venta.
- Distribución al cliente.
- Valor terminal.
- Pago de saldo hipotecario.

## 8.4 Generación de cuotas

Por cada activo, crear un evento por cuota.

Ejemplo de 36 cuotas:

```text
Fecha cuota 1 = mes siguiente a la firma
Fecha cuota n = EDATE(fecha cuota 1,n-1)
Importe = cuota mensual
Dirección = Salida
```

No crear una única fila llamada “36 cuotas” si el flujo necesita mostrar cada mes.

## 8.5 Reglas según estrategia

### Cesión

- Incluir pagos hasta la fecha de cesión.
- Calcular el saldo pendiente con el promotor a esa fecha.
- Registrar una entrada por el efectivo neto recibido.
- Cancelar cualquier pago posterior.
- No registrar saldo a entrega, hipoteca, mobiliario, renta ni valor terminal después de la cesión.

### Renta

- Registrar todos los pagos de construcción.
- Registrar saldo a entrega.
- Si existe préstamo, registrar el desembolso hipotecario en la misma fecha.
- Registrar mobiliario y cierre.
- Iniciar renta en la fecha definida.
- Registrar gastos de renta.
- Registrar pagos hipotecarios.
- En el último mes, registrar el valor terminal y el saldo hipotecario pendiente para el cálculo de patrimonio.

### Reventa posterior a entrega

- Aplicar la misma lógica de retención hasta la fecha de venta.
- Registrar rentas hasta el mes anterior a la venta.
- Registrar precio de venta, costos, impuestos y cancelación de hipoteca.
- No añadir valor terminal después de vender.

## 9. Hoja `FLUJO`

## 9.1 Propósito

La hoja debe responder cinco preguntas:

1. ¿Cuánto debe pagar el cliente cada mes?
2. ¿En qué momentos necesita capital extraordinario?
3. ¿Cuándo recibe liquidez por cesiones, ventas o rentas?
4. ¿Cuál es el saldo de caja durante todo el horizonte?
5. ¿Cuál es el retorno real del portafolio y del capital del cliente?

## 9.2 Bloque de escenario

Ubicar en la parte superior:

| Campo | Ejemplo |
|---|---|
| Escenario | 4 proyectos · USD 6.000/mes |
| Estrategia | 2 rentas + 2 cesiones |
| Inicio | jul-26 |
| Horizonte | 60 meses |
| Capital inicial | USD 363.374 |
| Capacidad mensual | USD 6.000 |
| Reserva mínima | USD 50.000 |

La descripción del escenario debe ser dinámica:

```excel
=ROWS(FILTER(tblProyectos[ID_Activo],tblProyectos[Incluir]="Sí"))
&" unidades · USD "
&TEXT(Capacidad_Mensual,"#,##0")
&"/mes"
```

## 9.3 Resumen por activo

Crear una fila por unidad incluida:

| Campo | Fuente |
|---|---|
| ID | `tblProyectos` |
| Proyecto | `tblProyectos` |
| Precio venta futuro | `Precio_Venta_Bruto` o valor terminal |
| Precio compra final | `Precio_Compra_Final` |
| Capital pagado | Eventos de salida del cliente |
| Saldo entrega | `Saldo_Entrega_USD` |
| Efectivo neto de cesión | `Efectivo_Neto_Cesion` |
| Operación | Estrategia |

No reservar únicamente seis filas. La cantidad de filas debe igualar la cantidad de activos seleccionados.

## 9.4 Eje temporal

Crear los números de mes:

```excel
=SEQUENCE(1,Horizonte_Meses,1,1)
```

Crear las fechas:

```excel
=EDATE(Fecha_Inicio_Modelo,SEQUENCE(1,Horizonte_Meses,0,1))
```

Si no se usan matrices dinámicas, preparar 120 columnas y ocultar las que excedan `Horizonte_Meses`.

## 9.5 Flujo por proyecto

Cada intersección proyecto/mes debe sumar los eventos del activo en ese mes:

```excel
=SUMIFS(
tblEventos[Flujo_Caja_USD],
tblEventos[ID_Activo],$B6,
tblEventos[Mes],J$5
)
```

La fórmula se copia horizontalmente para todos los meses y verticalmente para todos los activos.

Este enfoque sustituye la fórmula heredada que contiene múltiples `IF`, `MATCH`, `+12`, `+24` y `-6`.

## 9.6 Filas consolidadas

Después de las filas de activos, crear:

### Flujo total de propiedades

```excel
=SUM(filas_de_activos_del_mes)
```

### Compromisos de construcción

```excel
=-SUMIFS(
tblEventos[Flujo_Caja_USD],
tblEventos[Mes],J$5,
tblEventos[Cuenta_Contra_Capacidad],1,
tblEventos[Direccion],"Salida"
)
```

### Margen de capacidad

```excel
=Capacidad_Mensual-Compromisos_Construccion
```

Aplicar formato condicional:

- Verde si es mayor o igual a cero.
- Rojo si es negativo.

### Aporte mensual real

Modo fijo:

```excel
=IF(Numero_Mes<=Horizonte_Meses,Capacidad_Mensual,0)
```

Modo hasta límite:

```excel
=MIN(
Capacidad_Mensual,
MAX(
0,
Reserva_Minima-
(Saldo_Caja_Anterior+Flujo_Propiedades_Mes+Interes_Caja_Mes)
)
)
```

### Capital inicial

Solo entra en el primer mes:

```excel
=IF(Numero_Mes=1,Capital_Inicial,0)
```

### Interés sobre caja

```excel
=IF(Saldo_Caja_Anterior>0,
Saldo_Caja_Anterior*Tasa_Caja_Anual/12,
0)
```

### Saldo de caja

Primer mes:

```excel
=Capital_Inicial_Mes
+Aporte_Real_Mes
+Flujo_Propiedades_Mes
+Interes_Caja_Mes
```

Meses siguientes:

```excel
=Saldo_Caja_Anterior
+Capital_Inicial_Mes
+Aporte_Real_Mes
+Flujo_Propiedades_Mes
+Interes_Caja_Mes
```

### Necesidad extraordinaria

```excel
=MAX(0,Reserva_Minima-Saldo_Caja_Mes)
```

Si esta fila es mayor que cero, el portafolio no cumple con la estructura financiera del cliente.

## 9.7 Línea visual de inflexiones

La hoja debe identificar los meses en que el flujo cambia materialmente:

- Reserva.
- Firma.
- Inicio de cuotas.
- Abono extraordinario.
- Fin de cuotas.
- Entrega.
- Desembolso hipotecario.
- Inicio de hipoteca.
- Mobiliario.
- Inicio de renta.
- Cesión.
- Reventa.
- Pago de impuestos o comisión.

Entre dos inflexiones, mostrar:

```text
Cuota mensual estable: USD X durante Y meses
```

La línea visual puede construirse mediante:

- Formato condicional sobre la matriz mensual.
- Una tabla de hitos.
- Un gráfico de línea o columnas con anotaciones.

No usar un gráfico que oculte los números mensuales. La matriz sigue siendo la fuente auditable.

## 10. Financiamiento

## 10.1 Separar préstamo y saldo a entrega

El saldo a entrega es una obligación con el promotor.

El préstamo es una fuente de fondos.

En el mes de entrega pueden coexistir:

```text
Saldo a entrega: salida negativa
Desembolso hipotecario: entrada positiva
Capital propio a entrega: diferencia
```

## 10.2 Servicio de deuda

Por cada préstamo:

```excel
Cuota_Mensual
=-PMT(Tasa_Anual/12,Plazo_Anios*12,Monto_Prestamo)
```

Crear eventos mensuales negativos desde `Fecha_Primera_Cuota`.

## 10.3 Saldo hipotecario

Después de `k` pagos:

```excel
=MAX(
0,
-FV(
Tasa_Anual/12,
k,
-Cuota_Mensual,
Monto_Prestamo
)
)
```

## 10.4 Cobertura de deuda

Calcular por activo y portafolio:

```excel
DSCR
=IFERROR(Renta_Neta_Mensual/Cuota_Hipoteca_Mensual,0)
```

Interpretación:

- Mayor que 1.20x: margen razonable.
- Entre 1.00x y 1.20x: ajustado.
- Menor que 1.00x: la renta no cubre la deuda.

Estos umbrales son analíticos y no sustituyen los criterios del banco.

## 11. Resultados

## 11.1 Riqueza final

La riqueza final debe incluir:

- Caja final.
- Valor de mercado de activos retenidos.
- Menos costos hipotéticos de venta si se presenta valor neto liquidable.
- Menos saldos hipotecarios.
- Más distribuciones ya realizadas al cliente.

```excel
Riqueza_Final
=Caja_Final
+Valor_Neto_Activos_Retenidos
-Saldo_Hipotecario_Total
+Distribuciones_Acumuladas
```

## 11.2 Capital aportado

```excel
Capital_Aportado_Total
=Capital_Inicial+SUM(Aportes_Reales_Mensuales)
```

No sumar la capacidad completa si el modo es `Hasta límite` y parte de esa capacidad nunca se aportó.

## 11.3 Utilidad

```excel
Utilidad
=Riqueza_Final-Capital_Aportado_Total
```

## 11.4 ROI acumulado

```excel
ROI_Acumulado
=IFERROR(Utilidad/Capital_Aportado_Total,0)
```

El ROI acumulado ignora cuándo se aportó cada dólar.

## 11.5 MOIC

```excel
MOIC
=IFERROR(
(Riqueza_Final+Distribuciones_Recibidas)/Capital_Aportado_Total,
0
)
```

## 11.6 TIR del activo sin financiamiento

Usar únicamente:

- Pagos del activo.
- Costos operativos.
- Rentas.
- Ingresos de cesión o venta.
- Valor terminal.

Excluir:

- Desembolsos de préstamo.
- Cuotas hipotecarias.
- Aportes generales del cliente.
- Interés de la cuenta bancaria.

Con eventos fechados:

```excel
=IFERROR(
XIRR(
FILTER(tblEventos[Flujo_Caja_USD],
(tblEventos[ID_Activo]=ID_Activo)*(tblEventos[Incluye_TIR_Activo]=1)),
FILTER(tblEventos[Fecha],
(tblEventos[ID_Activo]=ID_Activo)*(tblEventos[Incluye_TIR_Activo]=1))
),
""
)
```

## 11.7 TIR del patrimonio del cliente

Crear una fila de flujo externo del inversionista:

- Capital inicial: negativo.
- Aportes reales: negativos.
- Distribuciones: positivas.
- En el último mes: riqueza final neta positiva.

```excel
=IFERROR(XIRR(Rango_Flujo_Equity,Rango_Fechas),"")
```

Si se utiliza flujo mensual regular:

```excel
=IFERROR((1+IRR(Rango_Flujo_Mensual))^12-1,"")
```

`XIRR` es preferible porque respeta fechas reales.

## 11.8 Promedio anual simple

El cálculo:

```excel
=ROI_Acumulado/Anios
```

no es una rentabilidad anual compuesta.

Si se conserva, etiquetarlo:

```text
Promedio anual simple
```

No llamarlo `ROI anual`.

## 11.9 CAGR

Cuando existe una inversión inicial comparable y un valor final:

```excel
=(Valor_Final/Valor_Inicial)^(1/Anios)-1
```

No usar CAGR como sustituto de la TIR cuando existen múltiples aportes.

## 12. Dimensionamiento según el flujo mensual del cliente

## 12.1 Métrica principal

Para cada mes:

```excel
Utilizacion_Capacidad
=IFERROR(Compromisos_Construccion/Capacidad_Mensual,0)
```

Indicadores:

- Menor o igual a 85%: saludable.
- Entre 85% y 100%: ajustado.
- Mayor a 100%: incumple.

Los umbrales pueden cambiarse según la política de Dproperty.

## 12.2 Prepago para reducir cuotas

Si el promotor permite aplicar un pago anticipado al bloque de cuotas:

```excel
Cuota_Ajustada
=(Monto_Cuotas_Base-Prepago_Adicional)/Numero_Cuotas
```

El prepago máximo:

```excel
=MAX(0,Monto_Cuotas_Base)
```

No asumir que un promotor permite redistribuir pagos sin confirmación escrita.

## 12.3 Optimización opcional

Usar Solver para:

Objetivo:

```text
Minimizar capital inicial adicional
```

Variables:

- Prepago por activo.
- Fecha de firma.
- Unidad seleccionada.
- Porcentaje financiado.

Restricciones:

- Compromiso mensual de cada mes ≤ capacidad mensual.
- Saldo de caja de cada mes ≥ reserva mínima.
- Prepago ≥ 0.
- Prepago ≤ monto originalmente destinado a cuotas.
- Financiamiento ≤ LTV permitido.
- Cada activo solo puede tener una estrategia de salida activa.

Para una propuesta orientada a retorno, el objetivo puede ser maximizar TIR de equity sujeto a las mismas restricciones.

## 13. Escenarios

Crear por lo menos:

### Conservador

- Precio de salida inferior.
- Salida retrasada.
- Renta inferior.
- Vacancia superior.
- Tasa hipotecaria superior.
- Costos de cierre superiores.

### Base

- Supuestos aprobados para la propuesta.

### Optimista

- Precio de salida superior.
- Venta en fecha objetivo.
- Renta superior.
- Menor vacancia.

No cambiar fórmulas entre escenarios. Solo deben cambiar celdas de supuestos.

## 14. Controles obligatorios

Crear un bloque `CONTROLES` con columnas:

| Control | Actual | Esperado | Diferencia | Tolerancia | Estado | Acción |
|---|---:|---:|---:|---:|---|---|

Controles mínimos:

1. IDs de activo únicos.
2. Ningún activo incluido sin precio, unidad, firma o entrega.
3. Precio final igual a pagos más saldo a entrega.
4. Pagos del detalle iguales al resumen de cada activo.
5. Ningún evento posterior a una cesión o venta.
6. Ninguna renta antes de la entrega.
7. Ningún activo vendido recibe valor terminal.
8. Activos retenidos sí reciben valor terminal.
9. Desembolso hipotecario no supera el préstamo aprobado.
10. Saldo hipotecario nunca es negativo.
11. Caja nunca cae por debajo de la reserva mínima.
12. Compromisos mensuales no superan la capacidad, salvo alerta explícita.
13. TIR solo se calcula si existe al menos un flujo negativo y uno positivo.
14. Totales por proyecto coinciden con totales de portafolio.
15. No existen errores `#REF!`, `#DIV/0!`, `#VALUE!`, `#NUM!`, `#N/A` o `#NAME?`.
16. Ninguna fuente crítica está marcada como pendiente sin advertencia.
17. El último mes incluye patrimonio terminal de activos retenidos.
18. El saldo de caja del resumen coincide con la última columna del flujo.

Ejemplo de estado:

```excel
=IF(ABS(Diferencia)<=Tolerancia,"OK","REVISAR")
```

Formato condicional:

- `OK`: verde.
- `REVISAR`: rojo.
- `PENDIENTE`: amarillo.

## 15. Gráficos recomendados

Los gráficos deben ayudar a interpretar el flujo y no reemplazar las tablas.

### 15.1 Flujo mensual consolidado

Tipo: columnas.

Series:

- Salidas de proyectos.
- Entradas por cesión/venta.
- Rentas.
- Financiamiento neto.

### 15.2 Saldo de caja

Tipo: línea.

Series:

- Saldo de caja.
- Reserva mínima.

### 15.3 Capacidad mensual

Tipo: columnas apiladas.

Series:

- Cuotas obligatorias.
- Margen disponible.

### 15.4 Composición de riqueza final

Tipo: barras.

Categorías:

- Caja.
- Valor de propiedades.
- Deuda.
- Distribuciones.
- Patrimonio neto.

### 15.5 Línea de inflexiones

Tipo: línea o dispersión con anotaciones.

Debe marcar:

- Firma.
- Extraordinarios.
- Entrega.
- Inicio de renta.
- Cesión.
- Venta.

## 16. Ejemplo de referencia: cuatro activos

El archivo analizado utiliza:

| Activo | Estrategia | Precio base | Precio final | Cuota mensual |
|---|---|---:|---:|---:|
| BIOMA 97 m² | Renta | $430,000 | $430,000 | $1,194.44 |
| Playa Escondida T200-1403 | Renta | $637,830 | $669,721.50 | $3,181.39 |
| Sky Parc II 16B | Cesión | $269,800 | $277,894 | $1,124.17 |
| Nayamara 05010 | Cesión | $306,000 | $315,180 | $500.00 |
| **Total** | 2 rentas + 2 cesiones | **$1,643,630** | **$1,692,795.50** | **$6,000.00** |

Supuestos principales del ejemplo:

- Inicio del flujo: julio de 2026.
- Horizonte: 60 meses.
- Capacidad mensual: USD 6.000.
- Reserva de liquidez incluida: USD 50.000.
- Capital inicial modelado: USD 363.374.
- Aportes mensuales de 60 meses: USD 360.000.
- Capital total aportado: USD 723.374.
- Dos activos se mantienen para renta.
- Dos activos se ceden antes de entrega.

Resultados que muestra el archivo:

| Resultado | Valor |
|---|---:|
| Valor de activos retenidos al mes 60 | $1,339,302 |
| Hipotecas nominales | $747,481 |
| Caja final | $599,098.78 |
| Interés de caja acumulado | $35,965.94 |
| Riqueza final | $1,226,885.73 |
| Utilidad | $503,511.73 |
| ROI acumulado | 69.61% |
| Promedio anual simple | 13.92% |
| TIR mostrada | 11.61% |

### Advertencia sobre el ejemplo

La TIR de 11.61% del archivo de referencia se calcula con los flujos de los activos y un valor terminal, pero no incorpora de forma completa los desembolsos de las hipotecas, sus cuotas mensuales y el saldo pendiente dentro de la misma serie de TIR.

Por eso, el modelo universal debe mostrar dos TIR:

- `TIR activo sin apalancamiento`.
- `TIR equity después de financiamiento`.

No reemplazar una con la otra.

## 17. Correspondencia con la lógica heredada

Para reproducir exactamente el archivo de referencia, la fórmula mensual de cada activo hace lo siguiente:

1. Cobra reserva en el mes 1.
2. Cobra firma en el mes de contrato.
3. Cobra cuotas después de la firma durante el número de meses indicado.
4. Cobra extraordinarios en firma + 12, firma + 24 y firma + cuotas − 6.
5. Si la estrategia es cesión, registra el efectivo recibido en una fecha calculada.
6. Si la estrategia es renta, registra saldo a entrega, mobiliario al mes siguiente y renta neta desde dos meses después de la entrega.

Su estructura conceptual es:

```excel
=-Pagos_Construccion
+Ingreso_Cesion
-Saldo_Entrega
-Mobiliario
+Renta_Neta
```

La lógica heredada puede replicarse para comprobar el ejemplo, pero no debe ser el motor definitivo de futuros clientes. El motor definitivo debe usar `tblEventos`.

## 18. Correcciones que deben aplicarse al reconstruir

1. Reemplazar la fórmula inválida de fecha `=` por una fecha real o `=TODAY()`.
2. Eliminar nombres definidos huérfanos que apuntan a una hoja `SUPUESTOS` inexistente.
3. Convertir los rangos en Tablas de Excel reales.
4. Eliminar límites fijos de cuatro o seis proyectos.
5. Separar capital inicial, aportes mensuales y préstamos.
6. Separar TIR de activo y TIR de equity.
7. Sustituir `ROI/5` por la etiqueta `promedio anual simple`, o eliminarlo.
8. Incluir saldo hipotecario al horizonte, no solo monto original del préstamo.
9. Evitar doble conteo de una propiedad vendida y su valor terminal.
10. Detener cuotas, rentas y deuda cuando el activo se vende o cede.
11. Crear un control visible de caja mínima.
12. Configurar área de impresión; el archivo original sin área definida produce decenas de páginas al exportar.

## 19. Configuración de impresión

La hoja `proyectos` es muy ancha. No intentar imprimir las 90+ columnas como una única página ilegible.

Opciones:

- Definir áreas de impresión por bloque.
- Imprimir identificación/precios/pagos como un bloque.
- Imprimir salida/renta/financiamiento como un segundo bloque.
- Usar orientación horizontal.
- Repetir la fila de encabezados.
- Ajustar a una página de ancho por bloque, no todo el libro.

La hoja `FLUJO` puede dividirse en grupos de 6 o 12 meses por página.

Para uso interno, mantener el libro navegable y utilizar el informe A4 separado como documento cliente.

## 20. Proceso de construcción

### Paso 1: recopilar información

Reunir:

- Lista de precios.
- Unidad exacta.
- Metraje.
- Descuento.
- Incremento de materiales.
- Plan de pagos.
- Entrega.
- Política de cesión.
- Comisión.
- Renta.
- HOA.
- Mobiliario.
- Financiamiento.
- Fecha objetivo del cliente.

### Paso 2: clasificar cada dato

Marcar:

- Confirmado.
- Supuesto.
- Pendiente.

### Paso 3: configurar cliente

Ingresar:

- Capital inicial.
- Capacidad mensual.
- Reserva mínima.
- Horizonte.
- Fecha objetivo.

### Paso 4: cargar `tblProyectos`

Una fila por unidad.

### Paso 5: generar `tblEventos`

Materializar cada pago e ingreso en su fecha.

### Paso 6: construir la matriz mensual

Sumar eventos por activo y mes.

### Paso 7: construir el roll-forward de caja

Agregar:

- Capital inicial.
- Aportes.
- Flujos de activos.
- Interés.
- Saldo.
- Déficit.

### Paso 8: agregar financiamiento

Incluir:

- Desembolso.
- Cuotas.
- Saldo pendiente.
- Cobertura.

### Paso 9: agregar valor terminal

Solo para activos retenidos.

### Paso 10: calcular retornos

Calcular:

- ROI acumulado.
- MOIC.
- TIR activo.
- TIR equity.
- Renta neta.
- DSCR.

### Paso 11: ejecutar controles

Todos los controles deben mostrar `OK` o una limitación explícita.

### Paso 12: revisar visualmente

Verificar:

- Textos no cortados.
- Fechas correctas.
- Moneda correcta.
- Colores consistentes.
- Fórmulas no visibles por error.
- Celdas editables claramente identificadas.
- Gráficos sin superposición.
- Hoja imprimible en bloques.

## 21. Criterios de aceptación

El modelo está terminado únicamente si:

- Se puede agregar o eliminar un activo sin reescribir el libro.
- Cambiar la capacidad mensual actualiza toda la liquidez.
- Cambiar una fecha mueve los flujos al mes correcto.
- Cambiar una estrategia elimina los flujos incompatibles.
- Cambiar la tasa hipotecaria recalcula cuota y saldo.
- El flujo mensual concilia con los eventos.
- El saldo final concilia con el resumen.
- La TIR de activo y la TIR de equity están separadas.
- El ROI no se presenta como rendimiento anual compuesto.
- No existen errores de fórmula.
- Las fuentes y supuestos son visibles.
- La propuesta no promete rentabilidad.

## 22. Descargo estándar

> Los valores proyectados constituyen un ejercicio ilustrativo de valorización, liquidez y flujo de caja. No representan una promesa de rentabilidad. Los resultados dependen de las condiciones del mercado, la disponibilidad real de las unidades, los términos definitivos de los promotores, los costos de transacción, los impuestos aplicables, la capacidad de cesión o reventa y la aprobación del financiamiento. Toda condición comercial o bancaria debe confirmarse antes de ejecutar la inversión.

## 23. Instrucción breve para una IA constructora

> Construye un libro Excel con dos hojas visibles, `proyectos` y `FLUJO`, siguiendo este manual. Usa Tablas de Excel dinámicas, fórmulas auditables y una base de eventos normalizada. No hardcodees el número de unidades, la capacidad mensual, las fechas, las tasas ni los costos dentro de fórmulas. Mantén la estética Dproperty en blanco y negro con amarillo para inputs, azul claro para campos vinculados, verde para liquidez y rojo para deuda. Calcula por separado TIR del activo, TIR de equity, ROI, MOIC, renta neta, saldo de caja, necesidad extraordinaria y saldo hipotecario. Valida todas las fórmulas, fuentes y controles antes de entregar.
