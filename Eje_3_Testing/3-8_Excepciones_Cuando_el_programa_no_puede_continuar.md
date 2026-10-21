# 3-8 Excepciones: cuando el programa no puede continuar

**Pregunta guía:** ¿qué puede hacer un programa cuando una operación no se puede completar?

En esta clase provocamos tres excepciones, leemos sus mensajes y usamos `try/except` para responder de una manera controlada. Trabajaremos con `ValueError`, `ZeroDivisionError` e `IndexError`.

## Objetivos

- Reconocer una excepción en el mensaje de Python.
- Identificar qué instrucción no pudo completarse.
- Diferenciar `ValueError`, `ZeroDivisionError` e `IndexError`.
- Comprender el recorrido básico de `try/except`.
- Volver a solicitar datos después de una excepción controlada.
- Manejar solamente las excepciones que esperamos y sabemos resolver.

## Materiales

- [Práctica 3-8: Selector de misiones](practicas/practica_3_8_excepciones.py).
- Una computadora con Python.
- Acceso a Internet para ver el video. La práctica también funciona sin conexión.

---

## Antes de comenzar: tres excepciones

Una excepción tiene un nombre que ayuda a reconocer qué operación no pudo completar Python.

| Excepción | ¿Cuándo ocurre? | Ejemplo |
|---|---|---|
| `ValueError` | El valor recibido no puede utilizarse como se pide. | `int("hola")` no puede convertir ese texto en un entero. |
| `ZeroDivisionError` | Se intenta dividir un número por cero. | `10 / 0` |
| `IndexError` | Se intenta acceder a una posición que no existe en una lista. | Si una lista tiene tres elementos, la posición `8` no existe. |

No hace falta memorizar todos los nombres. Primero leemos la última línea del mensaje de error para identificar el tipo y la explicación.

---

## 1. Ejemplo en el pizarrón 

### Primera versión: sin manejo de excepciones

Escribimos este programa:

```python
total = int(input("Costo total: "))
personas = int(input("Cantidad de personas: "))

por_persona = total / personas

print("Cada persona paga:", por_persona)
print("Cálculo terminado")
```

Antes de cada ejecución, anticipamos qué ocurrirá:

| Costo total | Personas | Resultado esperado |
|---:|---:|---|
| `12000` | `4` | Muestra `3000.0` y termina el cálculo. |
| `doce mil` | `4` | Se produce `ValueError`. |
| `12000` | `0` | Se produce `ZeroDivisionError`. |

Después de cada prueba respondemos:

1. ¿Hasta qué línea llegó el programa?
2. ¿Qué operación no pudo completar?
3. ¿Apareció el mensaje `Cálculo terminado`?
4. ¿El programa tenía un error de sintaxis?
5. ¿Las dos ejecuciones fallaron por el mismo motivo?

La última línea del mensaje de Python indica el tipo de excepción. El programa estaba correctamente escrito, pero durante la ejecución encontró una operación que no pudo completar.

### Segunda versión: una respuesta para cada problema

```python
try:
    total = int(input("Costo total: "))
    personas = int(input("Cantidad de personas: "))

    por_persona = total / personas
    print("Cada persona paga:", por_persona)

except ValueError:
    print("Ingresá números enteros.")

except ZeroDivisionError:
    print("La cantidad de personas no puede ser cero.")

print("Programa finalizado")
```

Volvemos a ejecutar los tres casos. Esta vez, seguimos el recorrido:

```text
try
 |
 |-- no ocurre una excepción ------> continúa normalmente
 |
 |-- ocurre ValueError ------------> ejecuta ese except
 |
 `-- ocurre ZeroDivisionError -----> ejecuta ese except

Después continúa debajo del bloque try/except.
```

> Una excepción interrumpe el recorrido normal del bloque `try`. Si existe un `except` correspondiente, el programa ejecuta esa respuesta y después puede continuar.

El bloque `except` no corrige el dato ingresado ni vuelve a intentar automáticamente la operación. Decide cómo responder ante un problema previsto.

### Tercera versión: advertir y volver a pedir los datos

Para que el programa no termine después de responder, agregamos un ciclo. La persona puede escribir `S` cuando quiera salir:

```python
while True:
    entrada_total = input("Costo total o S para salir: ")

    if entrada_total in ("s", "S"):
        break

    try:
        total = int(entrada_total)
        personas = int(input("Cantidad de personas: "))
        print("Cada persona paga:", total / personas)

    except ValueError:
        print("Ingresá números enteros. Volvamos a intentar.")

    except ZeroDivisionError:
        print("La cantidad de personas no puede ser cero. Volvamos a intentar.")

print("Programa finalizado")
```

`try/except` permite responder al problema; `while` vuelve a solicitar los datos y `break` ofrece una salida elegida por la persona.

### Relación con `assert`

- Usamos `assert` para comprobar una afirmación durante las pruebas.
- Usamos `try/except` para responder ante una situación excepcional que sabemos que puede ocurrir.
- Si la condición de un `assert` es falsa, Python produce `AssertionError`.
- Aunque técnicamente puede capturarse con `except AssertionError`, no lo haremos durante las pruebas: necesitamos ver la falla para investigar por qué la expectativa no se cumplió.

---

## 2. Video

Vemos completo este video de **3:43 minutos**:

[Excepciones en Python: manejo de errores con Try-Except - Cosas de Informática](https://www.youtube.com/watch?v=9D7ml-lCGsc)

Antes de comenzar, anotamos esta pregunta:

> ¿Qué parte del código se intenta ejecutar y qué parte responde al problema?

Al terminar, respondemos entre todos:

> ¿El `except` evita que ocurra la excepción o evita que el programa termine abruptamente?

La excepción ocurre. La diferencia es que ahora el programa tiene una respuesta preparada.

---

## 3. Actividad práctica: Selector de misiones

Abrimos [la práctica 3-8](practicas/practica_3_8_excepciones.py).

### Situación

El programa muestra tres misiones y solicita una opción. Después de una excepción controlada, vuelve a mostrar el menú. Si selecciona correctamente una misión, la muestra dentro de un marco y finaliza. La persona también puede escribir `S` para salir.

### Primera parte: anticipar y ejecutar

Sin modificar el programa, completen primero la columna **Predicción**. Después prueben cada caso en una ejecución nueva y registren lo que realmente ocurrió.

| Entrada | Predicción | Resultado obtenido |
|---:|---|---|
| `1` | | |
| `tres` | | |
| `8` | | |
| `0` | | |
| `S` | | |

Para cada caso indiquen:

- qué mensaje aparece;
- si ocurre una excepción y cuál;
- si el menú vuelve a mostrarse o el programa finaliza.

### Segunda parte: el caso que no produce una excepción

La entrada `0` selecciona la última misión y el programa finaliza. Esto ocurre porque `opcion - 1` da `-1` y Python permite usar `-1` para acceder al último elemento de una lista.

Respondan:

1. ¿El resultado obtenido era el esperado?
2. ¿Ocurrió alguna excepción?
3. ¿Por qué `try/except` no detectó este problema?

> Que no ocurra una excepción no significa que el resultado sea correcto.

### Actividad complementaria para quienes terminan antes

Abrimos [Desafío 3-8: ¿qué ocurre?](recursos/3-8_Desafio_excepciones.html).

La actividad presenta ocho tarjetas. En cada una deben leer un fragmento, anticipar qué ocurrirá y elegir una respuesta. Después de responder aparece una explicación del tipo de excepción o del recorrido correcto. No requiere cuenta y también funciona sin conexión.


## 4. Cierre

Respondemos brevemente:

1. ¿Qué excepción aparece cuando `int()` recibe `"muchas"`?
2. ¿Qué excepción aparece al dividir por cero?
3. ¿Qué excepción aparece al pedir una posición inexistente de una lista?
4. ¿Por qué la opción `0` produce un resultado incorrecto sin generar una excepción?
5. ¿Qué permite hacer el `while` y qué permite hacer `break`?

Para cerrar:

> Capturamos únicamente los problemas que esperamos y para los que podemos ofrecer una respuesta útil.

## Recursos

- [Errores y excepciones - Tutorial oficial de Python](https://docs.python.org/es/3/tutorial/errors.html).
- [Video: Excepciones en Python - Cosas de Informática](https://www.youtube.com/watch?v=9D7ml-lCGsc).

