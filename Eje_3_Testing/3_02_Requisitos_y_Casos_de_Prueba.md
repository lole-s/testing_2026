# Clase 2 — Requisitos y casos de prueba

**Fecha:** jueves 3 de septiembre de 2026  
**Duración:** 80 minutos

## Objetivos

Al finalizar la clase podrás:

- reconocer que para probar necesitamos conocer el comportamiento esperado;
- interpretar requisitos sencillos;
- diseñar casos de prueba con entradas y resultados esperados;
- ejecutar pruebas y registrar si pasan o fallan;
- diferenciar testing de depuración.

---

## 1. Recuperación de la clase anterior (8 minutos)

Revisaremos dos reportes de bugs.

Pensá:

- ¿Cuál permite reproducir el problema?
- ¿Qué información le falta al otro?
- ¿Cómo podría mejorarse?

---

## 2. ¿Cómo sabemos si algo funciona bien? (10 minutos)

Para decidir si un resultado es correcto necesitamos saber qué debería hacer el programa.

### Requisito

Un requisito describe una función, comportamiento o condición que el software debe cumplir.

Ejemplo:

> La función suma debe recibir dos números enteros y devolver su suma aritmética.

### Caso de prueba

Un caso de prueba indica qué vamos a probar y cuál debería ser el resultado.

| Identificador | Entrada | Resultado esperado |
|---|---|---|
| CP-01 | 3 y 2 | 5 |
| CP-02 | 0 y 5 | 5 |
| CP-03 | -1 y 4 | 3 |

Una prueba **pasa** cuando el resultado obtenido coincide con el esperado. Si no coincide, la prueba **falla** y debemos investigar la causa.

---

## 3. Preparación de la práctica (7 minutos)

Utilizaremos el programa:

**[clase_02_detectando_bugs.py](practicas/clase_02_detectando_bugs.py)**

Si ya tenés el repositorio en la computadora:

    git pull

Si no está descargado:

    git clone https://github.com/lole-s/testing_2026.git

Luego:

1. abrí la carpeta del repositorio con Visual Studio Code;
2. buscá el archivo dentro de Eje_3_Testing/practicas;
3. ejecutalo con Python;
4. durante la primera parte, utilizá el programa **sin analizar ni corregir el código**.

---

## 4. Requisitos del programa

El programa debería cumplir lo siguiente:

- **R1 — Suma:** devolver la suma aritmética de dos números.
- **R2 — Promedio:** calcular el promedio de una lista de números. Si la lista está vacía, debe informar que no puede calcularlo.
- **R3 — Factorial:** calcular el factorial de un número entero mayor o igual que cero. Debe rechazar números negativos.
- **R4 — Mayúsculas:** convertir el texto ingresado a letras mayúsculas.
- **R5 — Búsqueda:** indicar verdadero si un elemento pertenece a la lista y falso si no pertenece.

---

## 5. Diseñá tus pruebas antes de ejecutar (15 minutos)

Seleccioná al menos **tres funciones**. Para cada una diseñá:

- un caso normal;
- un caso con cero, vacío o valor límite;
- un caso negativo, extraño o poco habitual.

| Caso | Requisito | Entrada | Resultado esperado |
|---|---|---|---|
| CP-01 | R1 | 3 y 2 | 5 |
| CP-02 |  |  |  |
| CP-03 |  |  |  |
| CP-04 |  |  |  |
| CP-05 |  |  |  |
| CP-06 |  |  |  |

No modifiques el resultado esperado después de ejecutar el programa.

---

## 6. Ejecutá y registrá (20 minutos)

Ejecutá cada caso y completá:

| Caso | Resultado obtenido | ¿Pasó o falló? | Observaciones |
|---|---|---|---|
| CP-01 |  |  |  |
| CP-02 |  |  |  |
| CP-03 |  |  |  |
| CP-04 |  |  |  |
| CP-05 |  |  |  |
| CP-06 |  |  |  |

Si aparece un mensaje de error, no lo cierres inmediatamente: leelo y registrá la última línea.

---

## 7. Verificación con un compañero (10 minutos)

Intercambiá dos casos de prueba con otro estudiante.

Cada uno deberá:

1. repetir los casos recibidos;
2. comparar los resultados;
3. señalar si pudo reproducir la falla;
4. detectar si el caso de prueba era ambiguo.

---

## 8. Del testing a la depuración (5 minutos)

Ahora sí, observá el código fuente.

Elegí una falla y escribí una hipótesis:

- ¿en qué función podría estar el defecto?
- ¿qué línea o instrucción te resulta sospechosa?
- ¿qué cambio creés que sería necesario?

**Todavía no corrijas todos los errores.**

- Testing: busca información sobre la calidad y revela fallas.
- Depuración: localiza la causa del problema y permite corregir el código.

---

## 9. Cierre y entrega (5 minutos)

Entregá:

- seis casos de prueba diseñados;
- sus resultados;
- al menos una falla reproducible;
- una hipótesis sobre su posible causa.

Respondé al final:

> ¿Por qué es necesario escribir el resultado esperado antes de ejecutar una prueba?
