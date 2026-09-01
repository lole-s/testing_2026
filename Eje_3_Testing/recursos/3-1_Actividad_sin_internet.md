# Actividad 3-1: La tienda de remeras en papel

**Integrantes:**

**Fecha:**

Una tienda escolar utiliza un sistema para vender remeras. El sistema recibe los datos de la compra y muestra un mensaje y un total.

## Reglas de la tienda

1. La remera lisa cuesta `$8.000` y la estampada cuesta `$10.000`.
2. Se pueden comprar entre `1` y `5` unidades.
3. El subtotal se calcula multiplicando el precio por la cantidad.
4. El cupón `PROA10` descuenta el `10 %` del subtotal. Sin cupón no hay descuento.
5. Si la cantidad solicitada supera el stock, la compra debe rechazarse y el total debe ser `$0`.
6. El mensaje `Compra realizada` solo debe aparecer cuando todos los datos son válidos.

## Misión en pareja

Para las pruebas 1, 2 y 3:

- un integrante calcula el resultado esperado sin mirar primero el resultado obtenido;
- el otro lee el resultado producido por el sistema y registra la decisión.

Intercambien los roles para las pruebas 4, 5 y 6.

En cada fila escriban:

- el mensaje y el total que debería producir el sistema;
- `Funcionó como esperábamos`, `Sospechoso` o `Falta información`;
- una justificación breve basada en las reglas.

| Prueba | Datos ingresados | Resultado obtenido | Resultado esperado | Decisión y justificación |
| --- | --- | --- | --- | --- |
| 1 | Lisa; cantidad `2`; stock `10`; sin cupón | `Compra realizada`. Total: `$16.000` |  |  |
| 2 | Estampada; cantidad `1`; stock `5`; cupón `PROA10` | `Compra realizada`. Total: `$9.000` |  |  |
| 3 | Lisa; cantidad `0`; stock `10`; sin cupón | `Compra realizada`. Total: `$0` |  |  |
| 4 | Estampada; cantidad `2`; stock `1`; sin cupón | `Compra realizada`. Total: `$20.000` |  |  |
| 5 | Lisa; cantidad `3`; stock `10`; cupón `PROA10` | `Compra realizada`. Total: `$21.600` |  |  |
| 6 | Estampada; cantidad `2`; stock `5`; sin cupón | `Compra realizada`. Total: `$10.000` |  |  |

## Diseñen dos pruebas nuevas

Elijan datos que todavía no aparezcan en la tabla. Escriban el resultado esperado **antes** de decidir qué devolvería el sistema.

| Prueba | Tipo de remera, cantidad, stock y cupón | Resultado esperado | ¿Qué regla comprueba? |
| --- | --- | --- | --- |
| 7 |  |  |  |
| 8 |  |  |  |

## Evidencia en papel

Elijan una fila sospechosa y enciérrenla con un recuadro. Después completen:

**Título — dónde ocurre y qué ocurre:**

**Datos utilizados:**

**Resultado esperado:**

**Resultado obtenido:**

**Regla que demuestra la diferencia:**

## Para terminar

1. ¿Por qué fue necesario conocer las reglas antes de decidir si había un bug?
2. ¿Una prueba que funciona correctamente aporta información? Expliquen con un ejemplo de la tabla.
