# Clase 2: Requisitos y casos de prueba - La boletería bajo prueba

**Pregunta guía:** ¿cómo sabemos qué resultado debería producir un programa?

## Objetivos de la clase

- Interpretar requisitos sencillos.
- Diseñar casos de prueba antes de ejecutar un programa.
- Probar valores normales, límites y valores inválidos.
- Comparar el resultado esperado con el obtenido.
- Diferenciar testing de depuración.
- Evaluar críticamente un producto generado con IA.

## Documento de trabajo

Cada pareja realiza **una sola entrega en Google Docs**.

1. Un integrante crea el documento dentro de la carpeta de Drive compartida con el profesor.
2. Nombra el documento `3-2_Apellido1_Apellido2_Requisitos_y_casos_de_prueba`.
3. Comprueba que ambos integrantes puedan editarlo.
4. Copia las tablas de esta guía y completa todo en ese mismo documento.

## De una idea a requisitos comprobables

Una persona escribió este pedido para generar un programa con IA:

> Creá en Python una boletería de cine. Debe calcular el precio de una entrada según la edad, aplicar un descuento mediante un código y decidir si una persona menor puede ingresar sola.

El programa abre y parece funcionar. Sin embargo, el pedido no define precios, edades límite, códigos válidos ni reglas de ingreso. Para probarlo necesitamos transformar la idea en comportamientos concretos.

## Requisitos de la boletería

Un **requisito** expresa una función, condición o comportamiento que el producto debe cumplir.

- **R1 - Precio:** de 0 a 11 años inclusive, la entrada cuesta `$3000`; de 12 a 17, `$4500`; desde los 18, `$6000`. Una edad negativa debe ser rechazada.
- **R2 - Descuento:** el código `PROA10` descuenta el `10 %`. Cualquier otro código, incluido uno vacío, no aplica descuento.
- **R3 - Ingreso:** una persona de 0 a 12 años inclusive puede ingresar solamente si está acompañada. Desde los 13 años puede ingresar sola. Una edad negativa debe ser rechazada.

## ¿Qué clase de testing haremos?

En esta práctica realizaremos testing:

- **manual**, porque ingresaremos los datos y observaremos los resultados;
- **funcional**, porque comprobaremos precios, descuentos y permisos de ingreso;
- **de caja negra**, porque primero usaremos el programa sin mirar su código;
- **basado en especificaciones**, porque los resultados esperados se obtienen de los requisitos `R1`, `R2` y `R3`.

Las etiquetas describen distintos aspectos de una misma prueba. Más adelante estudiaremos otros tipos y niveles de testing.

### ¿Qué fallas podemos detectar?

| Clase de falla | Qué observar |
| --- | --- |
| Validación | El programa acepta un dato que debería rechazar. |
| Límite | Un valor ubicado justo donde cambia una regla se procesa mal. |
| Regla de negocio | La decisión del programa contradice un requisito. |
| Cálculo | El valor numérico obtenido no coincide con el esperado. |

## ¿Qué contiene un caso de prueba?

Un **caso de prueba** indica qué requisito se comprueba, qué datos se utilizarán y qué resultado se espera. El resultado esperado debe escribirse **antes** de ejecutar el programa.

| Caso | Requisito | Entrada completa | Resultado esperado |
| --- | --- | --- | --- |
| CP-00 | R1 | Edad: `15` | Precio: `$4500` |

Una prueba **pasa** si el resultado obtenido coincide con el esperado. Si no coincide, la prueba **falla**. Una prueba fallida demuestra una diferencia, pero todavía no explica su causa.

## Laboratorio 1: diseñar antes de ejecutar

Trabajen en pareja y elijan **dos requisitos**. Para cada requisito diseñen:

- un caso normal;
- un caso justo en un límite o cerca de él;
- un caso inválido o una alternativa diferente.

No usen el ejemplo `CP-00`. Escriban entradas completas y no cambien el resultado esperado después de ejecutar.

| Caso | Requisito | Entrada completa | Resultado esperado |
| --- | --- | --- | --- |
| CP-01 |  |  |  |
| CP-02 |  |  |  |
| CP-03 |  |  |  |
| CP-04 |  |  |  |
| CP-05 |  |  |  |
| CP-06 |  |  |  |

## Laboratorio 2: ejecutar las pruebas

Sincronicen el repositorio y abran [la boletería con bugs](practicas/3-2_boleteria_con_bugs.py) en Visual Studio Code.

Desde la carpeta principal del repositorio ejecuten:

```powershell
python Eje_3_Testing/practicas/3-2_boleteria_con_bugs.py
```

Usen el menú del programa sin abrir todavía el archivo para leer su código. Ejecuten exactamente los datos que escribieron en cada caso y registren los resultados.

| Caso | Resultado obtenido | Pasa / Falla | Observaciones |
| --- | --- | --- | --- |
| CP-01 |  |  |  |
| CP-02 |  |  |  |
| CP-03 |  |  |  |
| CP-04 |  |  |  |
| CP-05 |  |  |  |
| CP-06 |  |  |  |

Si aparece un error, copien su última línea. Un mensaje de error también es un resultado obtenido.

## Del testing a la depuración

Elijan una prueba que haya fallado. Ahora sí, abran el código y completen:

1. **Función sospechosa:** ¿en qué función buscarían el defecto?
2. **Condición o cálculo sospechoso:** ¿qué parte del código podría producir la diferencia?
3. **Cambio propuesto:** ¿qué modificarían?
4. **Pruebas para repetir:** ¿qué casos volverían a ejecutar después de corregirlo?

El **testing** permite detectar y describir una falla. La **depuración** busca su causa en el código y permite corregirla. Después de una corrección es necesario volver a ejecutar las pruebas.

## Video para revisar

[¿Cómo hacer pruebas de software para QA?](https://www.youtube.com/watch?v=2vqqadY6rCA)

El video explica escenarios, casos de prueba e información necesaria para diseñarlos. Úsenlo para revisar lo trabajado o para recuperar la clase si estuvieron ausentes.

## Cierre y entrega

En el mismo documento de Google incluyan:

- nombres de los dos integrantes;
- seis casos diseñados antes de ejecutar;
- los seis resultados obtenidos;
- una captura legible de la terminal con una prueba fallida;
- la hipótesis de depuración;
- la respuesta a la pregunta final.

**Pregunta final:** ¿por qué una aplicación generada con IA debe probarse aunque abra y parezca funcionar?
