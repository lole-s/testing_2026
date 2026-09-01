# Clase 1 — ¿Qué es el testing de software?

**Fecha:** miércoles 2 de septiembre de 2026  
**Duración:** 80 minutos

## Objetivos

Al finalizar la clase podrás:

- explicar con tus palabras qué es el testing de software;
- explorar una aplicación buscando comportamientos inesperados;
- diferenciar el resultado esperado del resultado obtenido;
- registrar un bug de manera que otra persona pueda reproducirlo.

---

## 1. Para comenzar — Errores que conocemos (8 minutos)

Pensá en una aplicación, juego o página web que alguna vez haya funcionado mal.

Respondé brevemente:

1. ¿Qué aplicación era?
2. ¿Qué estabas intentando hacer?
3. ¿Qué esperabas que ocurriera?
4. ¿Qué ocurrió realmente?

Compartiremos algunos ejemplos con el curso.

---

## 2. Primer desafío — Cacería de bugs (20 minutos)

Ingresá a:

**[AcademyBugs — Find Bugs](https://academybugs.com/find-bugs/)**

Es una tienda en línea creada especialmente para practicar testing. Contiene errores intencionales.

### Tu misión

Explorá individualmente la página e intentá encontrar **al menos dos bugs**.

Podés probar, por ejemplo:

- abrir productos;
- agregar y quitar productos del carrito;
- cambiar cantidades;
- ordenar o filtrar;
- utilizar botones y enlaces;
- ingresar datos inesperados;
- volver hacia atrás o repetir una acción.

### Reglas

- No alcanza con decir “está mal” o “no funciona”.
- Anotá exactamente qué hiciste.
- No informes como bug algo que simplemente no te gusta.
- No busques las soluciones en Internet.

Registrá cada hallazgo de manera provisoria:

| Bug | ¿Qué hice? | ¿Qué esperaba? | ¿Qué ocurrió? |
|---|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |

---

## 3. Video y conversación (10 minutos)

Miraremos:

**[Introducción: qué es un QA y por qué es importante en el equipo](https://www.youtube.com/watch?v=4rvwQtl8E8A)**

Mientras lo ves, anotá:

1. ¿Cuál es la tarea de una persona que trabaja en QA?
2. ¿El tester participa solamente cuando el programa está terminado?
3. ¿Qué puede aportar además de encontrar errores?

---

## 4. Conceptos principales (10 minutos)

### Testing de software

Es el proceso de diseñar y ejecutar pruebas para obtener información sobre la calidad de un programa, comprobar si cumple lo esperado y detectar posibles fallas.

### Testing exploratorio

Consiste en aprender sobre el producto, diseñar pruebas y ejecutarlas al mismo tiempo. No se sigue solamente un guion cerrado: se explora con un propósito.

### Bug

Es un defecto o problema del software que puede provocar un comportamiento incorrecto o diferente del esperado.

### Resultado esperado y resultado obtenido

- **Esperado:** lo que debería suceder según el requisito o comportamiento definido.
- **Obtenido:** lo que efectivamente sucedió al ejecutar la prueba.

### Reproducibilidad

Un reporte es reproducible cuando otra persona puede seguir los pasos y observar el mismo problema.

---

## 5. Reporte individual (15 minutos)

Elegí el bug más claro que encontraste y documentalo utilizando la:

**[Plantilla de reporte de bug](recursos/plantilla_reporte_bug.md)**

El reporte debe contener:

- título breve;
- página o sección;
- condiciones previas, si fueran necesarias;
- pasos numerados;
- resultado esperado;
- resultado obtenido;
- evidencia;
- indicación de si se pudo repetir.

---

## 6. Prueba entre compañeros (12 minutos)

Intercambiá tu reporte con otro estudiante.

Sin recibir explicaciones orales:

1. seguí únicamente los pasos escritos;
2. intentá reproducir el problema;
3. indicá si pudiste hacerlo;
4. señalá qué información faltó o qué parte fue confusa.

Después, devolvé el reporte para que su autor pueda mejorarlo.

---

## 7. Cierre individual (5 minutos)

Respondé:

1. ¿Qué es el testing de software?
2. ¿Por qué no alcanza con escribir “no funciona”?
3. ¿Qué diferencia hay entre el resultado esperado y el obtenido?
4. Mencioná una prueba que realizaste aunque no haya encontrado un bug.

## Entrega

Entregá un reporte individual, completo y corregido luego de la revisión de un compañero.
