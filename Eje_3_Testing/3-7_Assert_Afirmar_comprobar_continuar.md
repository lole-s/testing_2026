# 3-7 `assert`: afirmar, comprobar y continuar

**Pregunta guía:** ¿cómo sabemos si una afirmación sobre nuestro programa es verdadera?

En esta clase cerramos el trabajo con `assert`. Primero anticipamos qué debería ocurrir, después comprobamos nuestras ideas y finalmente practicamos la lectura de código con dos juegos.

## Objetivos

- Reconocer que un `assert` comprueba una afirmación.
- Diferenciar el valor esperado del valor obtenido.
- Anticipar si una comprobación pasa o produce `AssertionError`.
- Comprender que un `assert` fallido detiene esa ejecución.
- Leer expresiones sencillas antes de ejecutarlas.

## Materiales

- [Actividad individual para imprimir](recursos/3-7_Actividad_individual_assert.pdf).
- [Práctica complementaria en Python](practicas/practica_3_7_assert.py).

---

## 1. Explicación en el pizarrón

Escribimos:

```python
nombre = "Luna"

assert nombre == "Luna"

print("El programa continúa")
```

Antes de ejecutar, respondemos entre todos:

1. ¿Qué valor tiene `nombre`?
2. ¿Qué afirma el `assert`?
3. ¿La afirmación es verdadera o falsa?
4. ¿Se llegará al `print`?

Si la afirmación es verdadera, `assert` no muestra nada y Python continúa.

Ahora cambiamos solamente el resultado esperado:

```python
nombre = "Luna"

assert nombre == "Sol"

print("El programa continúa")
```

En este caso, Python muestra `AssertionError` y la ejecución se detiene antes del `print`.

Podemos leer una prueba de esta forma:

```text
assert       nombre       ==       "Sol"
comprueba    obtenido              esperado
```

> `assert` comprueba una afirmación. Si es verdadera, el programa continúa. Si es falsa, produce `AssertionError` y detiene esa ejecución.

`assert` no corrige el programa y tampoco decide cuál debería ser el resultado. La persona que diseña la prueba debe establecer primero qué espera.

---

## 2. Actividad individual en papel 

Cada estudiante recibe la [hoja de actividad](recursos/3-7_Actividad_individual_assert.pdf). Se completa de manera individual y sin ejecutar el código.

La hoja propone expresiones que relacionan varios datos:

- el nombre del jugador;
- operaciones combinadas y prioridad entre suma y multiplicación;
- un puntaje calculado previamente;
- la cantidad de elementos de una lista sumada a otra variable.

En cada línea hay que distinguir dos preguntas. Primero se resuelve solamente el lado izquierdo de `==`; después se compara ese valor con lo esperado:

1. ¿Qué valor se obtiene del lado izquierdo?
2. ¿El `assert` pasa o falla?

Al final se analiza el recorrido completo para decidir qué instrucciones no llegan a ejecutarse.

Cuando todos terminen, hacemos una puesta en común breve. 
---

## 3. Comprobación de la actividad en papel - 7 minutos

Abrimos [la práctica 3-7](practicas/practica_3_7_assert.py) y la ejecutamos desde la carpeta principal del repositorio:

```text
python Eje_3_Testing/practicas/practica_3_7_assert.py
```

Comparamos la ejecución con lo resuelto en la hoja. Corregimos el valor esperado (erroneo) y volvemos a ejecutar. La comprobación termina cuando aparece:

```text
Todas las comprobaciones pasaron
```

---

## 4. Una comprobación nueva en Python local - 8 minutos

Antes del `print` final agregamos:

```python
assert "mapa" in inventario, "Falta el mapa"
```

1. Anticipen si la afirmación pasará o fallará y ejecuten.
2. En la lista `inventario`, cambien `"mapa"` por `"brujula"`.
3. Anticipen qué líneas se ejecutarán y vuelvan a probar.
4. Lean el mensaje de `AssertionError` y expliquen qué comprueba `in`.
5. Restauren `"mapa"` y comprueben que el programa vuelve a finalizar.

La expresión `elemento in lista` produce `True` cuando el elemento está dentro de la lista y `False` cuando no está.

---

## 5. Leer código jugando

### Silent Teacher - Python

[Abrir Silent Teacher en Python](https://silentteacher.toxicode.fr/?theme=basic_python)

La consigna es:

> Observen el código, anticipen la respuesta y aprendan también de los intentos que no coincidan.

No hace falta terminar todo el recorrido. Durante los primeros 12 a 15 minutos, avancen hasta donde puedan sin pedir una explicación antes de cada pantalla.

### Compute It

[Abrir Compute It](https://compute-it.toxicode.fr/)

En este juego ustedes representan a la computadora:

> Lean las instrucciones en orden y muevan al personaje exactamente como indica el programa.

Jueguen otros 12 a 15 minutos. Si quedan detenidos en un nivel, vuelvan a leer el código línea por línea antes de probar otro recorrido.

No se exige alcanzar un nivel determinado ni entregar una captura. El objetivo es practicar la anticipación y la lectura precisa.

---

## 6. Cierre - 5 minutos

> ¿Qué necesita saber una persona antes de escribir un `assert`?

Para cerrar, recuperamos tres ideas:

- primero decidimos qué debería ocurrir;
- después comparamos lo esperado con lo obtenido;
- una prueba que falla aporta información sobre una diferencia que debemos investigar.

## Recursos

- [Silent Teacher en Python](https://silentteacher.toxicode.fr/?theme=basic_python).
- [Compute It](https://compute-it.toxicode.fr/).
- [Referencia oficial de Python sobre `assert`](https://docs.python.org/es/3/reference/simple_stmts.html#the-assert-statement).

