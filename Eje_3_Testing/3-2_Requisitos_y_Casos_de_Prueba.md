# Clase 2: Requisitos y casos de prueba - La boletería bajo prueba

**Pregunta guía:** ¿cómo sabemos qué resultado debería producir un programa?

## Objetivos de la clase

- Interpretar requisitos sencillos.
- Diseñar casos antes de ejecutar el programa.
- Probar valores normales, límites y valores inválidos.
- Registrar si una prueba pasa o falla.
- Diferenciar testing de depuración.
- Evaluar críticamente un producto generado con IA.

## Punto de partida: dos reportes, una diferencia

Revisaremos dos reportes de la clase anterior. Identificá cuál permite reproducir el problema y qué dato le falta al otro.

## El encargo realizado a una IA

Una persona escribió este pedido para generar un programa:

> Creá en Python una boletería de cine. Debe calcular el precio de una entrada según la edad, aplicar un descuento mediante un código y decidir si una persona menor puede ingresar sola.

La IA entregó un programa que abre y parece funcionar. ¿Eso alcanza para confiar en él?

El pedido es ambiguo: no define precios, edades límite, códigos válidos ni reglas de ingreso. Para probar necesitamos convertirlo en comportamientos verificables.

## Requisitos de la boletería

Un **requisito** expresa una función, condición o comportamiento que el producto debe cumplir.

- **R1 - Precio:** de 0 a 11 años inclusive, la entrada cuesta $3000; de 12 a 17, $4500; desde los 18, $6000. Una edad negativa debe ser rechazada.
- **R2 - Descuento:** el código `PROA10` descuenta el 10 %. Cualquier otro código, incluido uno vacío, no aplica descuento.
- **R3 - Ingreso:** una persona de 0 a 12 años inclusive puede ingresar solamente si está acompañada. Desde los 13 años puede ingresar sola. Una edad negativa debe ser rechazada.

Un **caso de prueba** define una entrada, el resultado esperado y luego el resultado realmente obtenido.

| Caso | Requisito | Entrada | Resultado esperado |
| --- | --- | --- | --- |
| CP-00 | R1 | Edad: 15 | $4500 |

Una prueba **pasa** si el resultado obtenido coincide con el esperado. Si no coincide, la prueba **falla**. Una prueba fallida revela un problema, pero todavía no explica su causa.

## Antes de ejecutar: diseñar las pruebas

Trabajen en parejas. Elijan **dos requisitos** y escriban tres casos para cada uno:

- un caso normal;
- un valor justo en un límite o cerca de él;
- un valor inválido o una alternativa distinta.

No usen el ejemplo `CP-00` y no cambien el resultado esperado después de ejecutar.

| Caso | Requisito | Entrada completa | Resultado esperado |
| --- | --- | --- | --- |
| CP-01 |  |  |  |
| CP-02 |  |  |  |
| CP-03 |  |  |  |
| CP-04 |  |  |  |
| CP-05 |  |  |  |
| CP-06 |  |  |  |

## Preparar y ejecutar el producto

Abran [3-2_boleteria_con_bugs.py](practicas/3-2_boleteria_con_bugs.py) en Visual Studio Code y ejecuten:

```powershell
python Eje_3_Testing/practicas/3-2_boleteria_con_bugs.py
```

Durante esta parte usá el programa desde el menú: **no leas ni modifiques todavía el código**.

| Caso | Resultado obtenido | ¿Pasa o falla? | Observaciones o evidencia |
| --- | --- | --- | --- |
| CP-01 |  |  |  |
| CP-02 |  |  |  |
| CP-03 |  |  |  |
| CP-04 |  |  |  |
| CP-05 |  |  |  |
| CP-06 |  |  |  |

Si aparece un error, registrá su última línea. Un mensaje de error también es un resultado obtenido.

## Control cruzado

Intercambien con otra pareja un caso que pasó y uno que falló.

1. Ejecuten exactamente las entradas recibidas.
2. Comparen los resultados.
3. Indiquen si el caso era claro y reproducible.
4. Si obtienen algo diferente, registren el entorno y los pasos antes de decidir quién tiene razón.

## Testing no es depuración

Ahora sí, abran el código. Elijan una prueba fallida y escriban una hipótesis:

- ¿qué función podría contener el defecto?;
- ¿qué condición o línea resulta sospechosa?;
- ¿qué cambio propondrías?;
- ¿qué casos repetirías después de corregirlo?

**Testing** permite detectar y describir fallas. **Depurar** es buscar la causa en el código y corregirla. Después de una corrección se vuelven a ejecutar pruebas para comprobarla.

## Cierre y entrega

Entreguen por pareja:

- seis casos diseñados antes de ejecutar;
- los seis resultados obtenidos;
- al menos una falla reproducible;
- una hipótesis sobre su causa.

La pareja responde:

> ¿Por qué una aplicación generada con IA debe probarse aunque abra y parezca funcionar?

## Video para revisar la clase

[¿Cómo hacer pruebas de software para QA?](https://www.youtube.com/watch?v=2vqqadY6rCA)

El video presenta escenarios, casos de prueba y formas de organizar sus resultados. Compará su propuesta con la tabla que usamos en la práctica.
