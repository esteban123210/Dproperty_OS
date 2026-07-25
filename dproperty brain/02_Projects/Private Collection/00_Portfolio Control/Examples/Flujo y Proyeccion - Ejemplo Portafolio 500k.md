---
type: financial-model-example
title: Flujo y Proyección - Ejemplo Portafolio 500k
source_file: FLUJO Y PROYECCION 500 mil(2).xlsx
model_date: 2026-07-23
received: 2026-07-25
currency: USD
horizon_months: 60
initial_capital: 500000
mortgage: 200000
bank_interest_annual: 0.03
source_sha256: 382f7b1ec336fe673b8f02dd4a93c447f7410996c17eaa1e061f61a41ee7eb82
status: example-not-client-offer
---

# Flujo y Proyección - Ejemplo de portafolio con $500,000

> Este documento convierte el workbook de Excel en una referencia legible para Obsidian. Conserva la estructura, los supuestos y los resultados principales, pero no reemplaza el archivo de cálculo. Toda propuesta nueva debe recalcularse con inventario y condiciones vigentes.

## Objetivo del modelo

El ejercicio muestra cómo un cliente con $500,000 de capital inicial puede acceder a seis posiciones inmobiliarias mediante reservas, pagos de firma, cuotas de construcción, cesiones escalonadas y financiamiento selectivo a la entrega.

La lógica combina:

- Cuatro activos con estrategia de `cesión/reventa`.
- Dos activos retenidos para `renta`.
- Despliegue gradual del capital durante 60 meses.
- Interés sobre saldos positivos en banco.
- Una hipoteca de $200,000 aplicada únicamente a los activos retenidos.

## Arquitectura del workbook

| Hoja | Dimensión utilizada | Función |
|---|---:|---|
| `proyectos` | 98 columnas x 19 filas utilizadas | Análisis unitario, ventajas Dproperty, plan de pagos, reventa y rentas |
| `FLUJO` | 69 columnas x 30 filas utilizadas | Consolidación mensual de julio de 2026 a junio de 2031 |

### Bloques de la hoja `proyectos`

1. Características generales.
2. Precio promotor y precio Dproperty.
3. Ventajas modeladas: descuento, materiales, cesión y comisión.
4. Reserva, firma, cuotas y abonos extraordinarios.
5. Precio final de adquisición.
6. Reventa y valorización.
7. Renta de largo plazo.
8. Renta de corto plazo.

## Portafolio del ejemplo

| Proyecto | Unidad | Área | Precio promotor | Precio Dproperty | Estrategia |
|---|---|---:|---:|---:|---|
| BIOMA | 15D | 114 m² | $561,000 | $510,000 | Renta |
| CDE The Velopers | Por definir | 70 m² | $322,000 | $308,000 | Renta |
| Sky Parc II | 38B | 85 m² | $294,350 | $294,350 | Cesión |
| Sky Parc IV | Por definir | 63 m² | $225,000 | $225,000 | Cesión |
| Sky Parc IV | Por definir | 95 m² | $319,000 | $319,000 | Cesión |
| Playa Escondida Torre 100 | Por definir | 133.91 m² | $430,225 | $417,318.25 | Cesión |
| **Total** |  | **560.91 m²** | **$2,151,575** | **$2,073,668.25** |  |

## Ventajas modeladas

Estas partidas son escenarios del modelo y no ahorros garantizados. Deben validarse en la documentación comercial y contractual.

| Proyecto | Descuento | Diferencia materiales | Diferencia cesión | Diferencia comisión | Ventaja total |
|---|---:|---:|---:|---:|---:|
| BIOMA | $51,000 | $23,970 | $14,280 | $11,970 | **$101,220** |
| CDE The Velopers | $14,000 | $13,300 | $8,960 | $7,420 | **$43,680** |
| Sky Parc II | $0 | $11,774 | $8,831 | $6,970 | **$27,575** |
| Sky Parc IV - 63 m² | $0 | $9,000 | $6,750 | $5,418 | **$21,168** |
| Sky Parc IV - 95 m² | $0 | $12,760 | $9,570 | $7,790 | **$30,120** |
| Playa Escondida Torre 100 | $12,906.75 | $13,552.09 | $12,261.41 | $9,641.52 | **$48,361.77** |
| **Total** | **$77,906.75** | **$84,356.09** | **$60,651.91** | **$49,209.52** | **$272,124.27** |

## Planes de pago utilizados en el ejemplo

| Activo | Preventa | Reserva | Firma | Cuotas | Extraordinarios | Saldo a entrega |
|---|---:|---:|---:|---|---|---:|
| BIOMA | 30% | $1,000 | $101,000 | 36 x $1,416.67 | No modelados | $357,000 |
| CDE The Velopers | 30% | $1,000 | $14,400 | 48 x $962.50 | $7,700 mes 12; $7,700 mes 24; $15,400 final | $215,600 |
| Sky Parc II | 20% | $1,000 | $13,717.50 | 36 x $1,226.46 | No modelados | $235,480 |
| Sky Parc IV - 63 m² | 30% | $1,000 | $10,250 | 42 x $803.57 | $5,625 mes 12; $5,625 mes 24; $11,250 final | $157,500 |
| Sky Parc IV - 95 m² | 20% | $1,000 | $14,950 | 42 x $1,139.29 | No modelados | $255,200 |
| Playa Escondida Torre 100 | 30% | $1,000 | $19,865.91 | 18 x $3,477.65 | $41,731.83 mes 12 | $292,122.77 |

## Resultados unitarios de reventa

| Activo | Precio final de compra | Venta futura modelada | Utilidad neta | ROI sobre abonos | Retorno anual simple |
|---|---:|---:|---:|---:|---:|
| BIOMA | $525,300 | $598,500 | $45,045 | 29.44% | 8.41% |
| CDE The Velopers | $317,240 | $371,000 | $36,470 | 39.47% | 7.89% |
| Sky Parc II | $303,180.50 | $348,500 | $28,977.50 | 49.22% | 16.41% |
| Sky Parc IV - 63 m² | $231,750 | $270,900 | $26,523 | 39.29% | 9.82% |
| Sky Parc IV - 95 m² | $328,570 | $389,500 | $42,865 | 67.19% | 16.80% |
| Playa Escondida Torre 100 | $438,184.16 | $482,076 | $21,083.19 | 16.84% | 11.23% |

## Activos retenidos para renta

| Activo | Renta bruta mensual | Gastos mensuales modelados | Renta neta mensual antes de deuda |
|---|---:|---:|---:|
| BIOMA | $3,200 | $834.54 | $2,365.46 |
| CDE The Velopers | $2,300 | $448.85 | $1,851.15 |
| **Total estabilizado** | **$5,500** | **$1,283.39** | **$4,216.61** |

## Lógica mensual de la hoja `FLUJO`

Cada activo ocupa una fila y cada mes ocupa una columna.

```text
Flujo mensual del activo
= -(reserva + firma + cuota mensual + extraordinarios)
  + ingreso de cesión, si la estrategia es cesión
  - saldo a entrega y amoblamiento, si la estrategia es renta
  + renta neta mensual después de la entrega
```

El patrón de eventos es:

| Momento | Evento |
|---|---|
| Mes 1 | Reserva |
| Mes de firma | Pago de firma |
| Durante construcción | Cuota mensual constante |
| Mes 12 | Primer abono extraordinario, si aplica |
| Mes 24 | Segundo abono extraordinario, si aplica |
| Seis meses antes del final | Último extraordinario, si aplica |
| Después de las cuotas | Cesión o pago del saldo a entrega |
| Mes siguiente a la entrega | Amoblamiento, si el activo se retiene |
| Mes posterior | Inicio de renta neta |

### Flujo consolidado

```text
Saldo final del banco
= saldo anterior
 + capital adicional del cliente
 + flujo total de los activos
 + interés sobre saldo positivo
```

```text
Riqueza final
= valor de las propiedades retenidas
 - hipotecas pendientes
 + saldo bancario
 + intereses acumulados
```

## Indicadores principales del horizonte completo

| Indicador | Resultado | Lectura |
|---|---:|---|
| Capital inicial | **$500,000** | Equity aportado |
| Hipoteca modelada | **$200,000** | Financiamiento selectivo |
| Riqueza neta final | **$812,059.94** | Activos netos + banco + intereses |
| Utilidad proyectada | **$312,059.94** | Riqueza final menos capital |
| ROI acumulado | **62.41%** | Retorno sobre el equity inicial |
| MOIC | **1.62x** | Múltiplo sobre capital |
| ROI anual simple | **12.48%** | ROI total dividido por cinco años |
| CAGR normalizado | **10.19%** | Crecimiento anual compuesto del equity |
| TIR del modelo | **25.34%** | TIR de los flujos inmobiliarios desplegados |
| Renta neta estabilizada | **$4,216.61/mes** | Antes del servicio de deuda |

## Controles y advertencias

- Las proyecciones no son promesas de rentabilidad.
- La TIR del modelo y el CAGR del equity miden cosas distintas.
- El archivo utiliza fórmulas `LET`, nombres definidos y referencias al nombre de hoja `proyectos ` con espacio final; algunos importadores distintos de Excel pueden mostrar errores aunque el archivo conserve resultados calculados.
- Los precios futuros, las rentas, los costos, la ocupación y las condiciones de financiamiento deben convertirse en supuestos editables para cada cliente.
- El resultado final depende de ejecutar las cesiones en las fechas y valores modelados.
- Debe mantenerse una reserva de liquidez separada; el escenario original llega a un saldo mínimo casi nulo.

## Cómo reutilizar esta estructura

Para un cliente nuevo se debe capturar:

1. Capital inicial y capacidad mensual.
2. Unidades exactas y precio vigente.
3. Plan oficial de pagos por activo.
4. Estrategia `cesión` o `renta`.
5. Extraordinarios y saldo a entrega.
6. Valor de reventa, costos y fecha de salida.
7. Renta, gastos, amoblamiento y vacancia.
8. Financiamiento: monto, tasa, plazo, LTV y fecha.
9. Reserva mínima de liquidez.
10. Escenario base, conservador y adverso.

