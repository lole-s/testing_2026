# 3-6 Caja blanca y `assert` - Funciones bajo sospecha

**Pregunta guía:** ¿cómo puede ayudarnos el código a elegir una prueba capaz de demostrar una falla?

La actividad se realiza en parejas en dos partes. En cada parte observarán una función pequeña, buscarán una falla y conservarán una evidencia breve.

## Objetivos de la clase

- Comprender qué significa probar con un enfoque de caja blanca.
- Relacionar reglas, condiciones y caminos posibles de una función.
- Elegir entradas que permitan comprobar decisiones importantes.
- Usar `assert` para comparar automáticamente un resultado esperado con el obtenido.
- Diferenciar encontrar una falla, corregirla y volver a probar.

## Documento de trabajo

Cada pareja realiza una sola entrega en Google Docs.

1. Creen el documento dentro de la carpeta compartida con el profesor.
2. Nómbrenlo `3-6_Apellido1_Apellido2_Funciones`.
3. Copien únicamente las tablas y respuestas solicitadas.

Dentro de la pareja, una persona ejecuta y la otra registra. La puesta en común con el curso se realiza al final de la segunda parte.

---

# Primera parte - Mirar el código para elegir pruebas

## 1. ¿Qué son las pruebas de caja negra y caja blanca? - 15 minutos

[Pruebas de caja blanca, caja negra y caja gris](https://www.youtube.com/watch?v=N-a5DEa_f0U). Para esta actividad, concéntrense en caja negra y caja blanca.

- En una **prueba de caja negra**, elegimos entradas a partir de las reglas o requisitos y observamos la salida, sin utilizar el código interno para diseñar la prueba.
- En una **prueba de caja blanca**, observamos las condiciones, decisiones y caminos del código para elegir entradas que los recorran.

En 3-5 probaron AcademyBugs desde la interfaz: trabajaron principalmente como caja negra. En esta clase podrán leer funciones de Python para decidir qué conviene probar.

### INICIO DE ACTIVIDAD

Respondan en dos oraciones:

1. ¿Qué información usamos para diseñar una prueba de caja negra?
2. ¿Qué información adicional usamos en una prueba de caja blanca?

## 2. Análisis guiado: precio de una entrada - 20 minutos

Una sala cobra según la edad:

- menores de 13 años: entrada gratuita;
- de 13 a 17 años: `$2000`;
- desde los 18 años: `$3500`.

La función fue escrita así:

```python
def precio_entrada(edad):
    if edad >= 13:
        return 2000
    elif edad >= 18:
        return 3500
    return 0
```

Sin ejecutar todavía, sigan el código para `10`, `15` y `20` años:

| Edad | Resultado según las reglas | Primera condición | Camino y resultado del código |
| ---: | ---: | --- | --- |
| 10 |  |  |  |
| 15 |  |  |  |
| 20 |  |  |  |

Para cada edad, comiencen por la primera condición. Cuando aparece `return`, la función termina y no continúa con las líneas siguientes.

Después ejecuten la opción 1 del [laboratorio de funciones](practicas/funciones_3_6.py) y comprueben sus predicciones:

```text
python Eje_3_Testing/practicas/funciones_3_6.py
```

Respondan:

1. ¿Qué edad demuestra que existe una falla?
2. ¿Por qué la condición `edad >= 18` nunca llega a evaluarse para una persona adulta?
3. ¿Cómo cambiarían el orden de las condiciones para corregirla?

## 3. Desafío: la promoción imposible - 35 minutos

Una productora lanza entradas para un recital a `$12000`. Hay dos promociones:

- estudiantes: 25 % de descuento;
- compra anticipada: 10 % de descuento.

Las promociones **no se acumulan**. Si una persona cumple ambas condiciones, el sistema debe aplicar solamente la más conveniente.

Durante las primeras ventas, tres compradores pagaron lo esperado. El cuarto asegura que el sistema le cobró un precio que no existe en las reglas. ¿En qué situación ocurre?

Usen la opción 2 del laboratorio. Hay solamente cuatro perfiles posibles. No prueben al azar: completen primero el precio esperado de cada uno y después consulten al programa.

| ¿Es estudiante? | ¿Compra anticipada? | Precio esperado | Precio obtenido |
| --- | --- | ---: | ---: |
| No | No |  |  |
| No | Sí |  |  |
| Sí | No |  |  |
| Sí | Sí |  |  |

Cuando encuentren el precio imposible, abran `funciones_3_6.py` y lean solamente `precio_recital`.

1. Marquen qué líneas se ejecutan en el caso que falla.
2. Expliquen por qué los dos `if` permiten recorrer dos descuentos en la misma llamada.
3. Decidan si reemplazar el segundo `if` por `elif` respeta todas las reglas o si también necesitan cambiar el orden.

Registren la evidencia:

> El perfil __________ debía pagar __________, pero pagó __________. Al leer el código descubrimos que __________.

Corrijan la función y repitan los cuatro casos. Una solución está terminada sólo si desaparece el precio imposible y siguen funcionando los otros tres.

## 4. Desafío adicional: el speedrun que pierde un bonus

Un videojuego calcula el puntaje de una partida con estas reglas:

- cada moneda vale 100 puntos;
- terminar en menos de 60 segundos suma un bonus de 500 puntos;
- juntar 10 monedas o más suma otro bonus de 300 puntos;
- los dos bonus **sí pueden acumularse**.

La mayoría de las partidas reciben el puntaje correcto, pero existe una combinación que pierde uno de los bonus. Usen la opción 4 del laboratorio y completen la tabla antes de leer la función.

| Monedas | Segundos | Puntaje esperado | Puntaje obtenido |
| ---: | ---: | ---: | ---: |
| 5 | 90 |  |  |
| 5 | 50 |  |  |
| 12 | 90 |  |  |
| 12 | 50 |  |  |

Cuando encuentren la partida que falla, lean `puntaje_speedrun` y respondan:

1. ¿Qué bonus se calcula primero?
2. Cuando la condición del tiempo es verdadera, ¿Python llega a evaluar el `elif`?
3. Si las reglas permiten acumular los dos bonus, ¿conviene usar `elif` o un segundo `if`?

Completen:

> Con __________ monedas y __________ segundos esperábamos __________ puntos, pero obtuvimos __________. El segundo bonus se pierde porque __________.

Corrijan una sola palabra de la función y vuelvan a probar los cuatro casos.

> Comparen ambos desafíos: en el recital los beneficios no se acumulan, pero en el speedrun sí. La estructura correcta depende de las reglas, no de que `if` o `elif` sea siempre mejor.

## 5. Entrega mínima de la primera parte - 10 minutos

En el documento de la pareja debe quedar:

- las dos respuestas sobre caja negra y caja blanca;
- la tabla guiada de edades;
- el perfil que demuestra el error de la promoción;
- si realizaron el desafío adicional, la partida que demuestra el error del speedrun;
- la frase que explica cómo el código ayudó a elegirla.

No hace falta copiar toda la guía ni presentar un reporte extenso.

---

# Segunda parte - Convertir expectativas en pruebas con `assert`

## 1. ¿Qué es `assert`? - 15 minutos

Miren [Introducción a las aserciones o afirmaciones con Python](https://www.youtube.com/watch?v=qGAivc6sWOQ).

`assert` es una instrucción de Python que comprueba si una afirmación es verdadera.

```python
assert 2 + 2 == 4
print("La comprobación pasó")
```

Si la afirmación es verdadera, Python continúa. Si es falsa, muestra `AssertionError` y se detiene en esa línea.

```python
assert 2 + 2 == 5, "La suma no coincide con lo esperado"
```

El texto después de la coma es un mensaje opcional. `assert` no corrige el programa: hace visible que una expectativa no se cumplió.

Respondan: ¿qué diferencia hay entre mostrar el resultado de una función con `print` y comprobarlo con `assert`?

## 2. Ejemplo guiado con la entrada - 15 minutos

Creen un archivo llamado `pruebas_3_6.py` en la misma carpeta que `funciones_3_6.py` y escriban:

```python
from funciones_3_6 import precio_entrada

assert precio_entrada(10) == 0
assert precio_entrada(15) == 2000
assert precio_entrada(20) == 3500

print("Pasaron las pruebas de precio")
```

Antes de ejecutar, anticipen cuál de las tres comprobaciones fallará. Después respondan:

1. ¿Qué información muestra `AssertionError`?
2. ¿Por qué no aparece el mensaje final?
3. Después de corregir `precio_entrada`, ¿qué debería ocurrir al ejecutar exactamente las mismas pruebas?

Corrijan la función y compruébenlo. No borren la prueba que encontró la falla.

## 3. Desafío con `assert`: el cupón que abarata demasiado - 40 minutos

Una app de delivery usa estas reglas:

- el cupón `PROA20` descuenta 20 % si el subtotal es de `$10000` o más;
- el envío cuesta `$2000`;
- el envío es gratis cuando el importe **después del descuento** queda en `$15000` o más.

La función `total_delivery` suele calcular bien, pero en una franja de compra regala el envío por error. La tarea no es ensayar muchos números: deben encerrar la falla entre casos que funcionan.

Antes de programar, calculen estos resultados:

| Subtotal | Cupón | Después del descuento | Envío esperado | Total esperado |
| ---: | --- | ---: | ---: | ---: |
| 10000 | `PROA20` |  |  |  |
| 15000 | sin cupón |  |  |  |
| 15000 | `PROA20` |  |  |  |
| 20000 | `PROA20` |  |  |  |

En `pruebas_3_6.py`, importen también la función:

```python
from funciones_3_6 import precio_entrada, total_delivery
```

Conviertan cada fila en una comprobación. Por ejemplo:

```python
assert total_delivery(10000, "PROA20") == 10000
```

Ejecuten las cuatro pruebas. Cuando una falle, lean `total_delivery` y respondan:

1. ¿Qué valor guarda `total` después de aplicar el cupón?
2. ¿Qué variable usa el programa para decidir si el envío es gratis?
3. ¿Cuál debería usar según las reglas?

Corrijan una sola expresión y vuelvan a ejecutar todas las pruebas, incluidas las de precio de entrada. No cambien el resultado esperado para conseguir que un `assert` pase.

Para cerrar, encuentren los límites de la franja defectuosa: ¿desde qué subtotal y hasta antes de qué subtotal el cupón dejaba el importe por debajo de `$15000`, pero el programa regalaba igualmente el envío?

## 4. Entrega mínima, cierre y puesta en común - 10 minutos

Agreguen al documento:

- la respuesta sobre `print` y `assert`;
- los cuatro casos del delivery;
- el código de sus `assert`;
- una captura o transcripción de una prueba fallando antes de corregir;
- una captura o transcripción del resultado después de corregir;
- una respuesta individual: **¿qué prueba fue más útil y qué error permitió descubrir?**

Al final, algunas parejas podrán compartir un caso de prueba. Primero se presenta la entrada para que el curso anticipe el resultado; después se muestra qué respondió la función.

## Si terminan antes

Escriban dos `assert` que atrapen con la mayor precisión posible los bordes de la franja defectuosa del delivery: uno justo dentro y otro justo fuera. Expliquen por qué eligieron esos dos subtotales.

## Si Python o la conexión fallan

Pueden seguir las condiciones a mano y marcar cada expresión como verdadera o falsa. Escriban igualmente los `assert` y anoten cuáles esperan que fallen. Las definiciones de esta guía permiten continuar aunque no se puedan reproducir los videos.

## Recursos

- [Pruebas de caja blanca, caja negra y caja gris](https://www.youtube.com/watch?v=N-a5DEa_f0U).
- [Introducción a las aserciones o afirmaciones con Python](https://www.youtube.com/watch?v=qGAivc6sWOQ).
- [Python: la instrucción `assert`](https://docs.python.org/es/3/reference/simple_stmts.html#the-assert-statement).
