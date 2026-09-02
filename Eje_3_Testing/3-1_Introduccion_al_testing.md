# Clase 1: Introducción al testing - Cacería de bugs

**Pregunta guía:** ¿cómo demostramos que un programa no hace lo que debería hacer?

## Objetivos de la clase

- Comprender qué significa probar software.
- Explorar una aplicación con una intención y no solamente “hacer clic”.
- Diferenciar resultado esperado y resultado obtenido.
- Registrar con claridad lo observado durante una prueba.

## Documento de trabajo

Cada pareja realiza **una sola entrega en Google Docs**.

1. Un integrante crea un documento dentro de la carpeta de Drive compartida con el profesor.
2. Nombra el documento `3-1_Apellido1_Apellido2_Introduccion_al_testing`.
3. Comparte el permiso de edición con su compañero/a si la carpeta no lo hace automáticamente.
4. Copia en el documento la estructura de la [plantilla de entrega](recursos/3-1_Plantilla_entrega.md).
5. Los dos integrantes escriben las respuestas y pegan las capturas en ese mismo documento.

No creen un archivo diferente para cada actividad.

## Introducción teórica

[¿Qué es el testing de software? - OpenWebinars](https://www.youtube.com/watch?v=imu4oIpALy8). El enlace queda disponible para quienes necesiten revisarlo después.

### Conceptos mínimos

El **testing de software** es un conjunto de actividades que permite obtener información sobre la calidad de un producto y comprobar si su comportamiento coincide con lo esperado.

Un **bug** o defecto es un problema en el software que puede producir un comportamiento incorrecto. Durante una prueba observamos una **falla** cuando el resultado obtenido no coincide con el esperado.

| Concepto | Pregunta que responde |
| --- | --- |
| Acción o entrada | ¿Qué hice o qué dato ingresé? |
| Resultado esperado | ¿Qué debería haber ocurrido y por qué? |
| Resultado obtenido | ¿Qué ocurrió realmente? |
| Evidencia | ¿Qué puedo mostrar para sostenerlo? |
| Reproducibilidad | ¿Otra persona puede repetirlo con mis pasos? |

> Encontrar un bug por casualidad sirve. Poder explicar qué se hizo y qué ocurrió sirve mucho más.

### Un caso real: Mars Climate Orbiter

[Mars Climate Orbiter: un error de unidades](https://www.youtube.com/watch?v=DrITKbJfnV0)

Después de ver el corto, respondan en el documento:

- ¿Qué dato deberían haber acordado y probado los equipos antes de utilizar el sistema?

### Para ampliar

[¿Necesitás saber programar para ser tester de software? - Testing Para Todos](https://www.youtube.com/watch?v=3ArIV4iLTVU)

Para encontrar y comunicar un comportamiento inesperado no es indispensable conocer el código del programa. Sí es necesario observar, conocer las reglas, comparar resultados y explicar con claridad qué ocurrió. Saber programar puede ayudar a investigar y automatizar pruebas, pero no reemplaza esas habilidades.

## Desafío inicial: el sistema que viajó en el tiempo

Durante años, una empresa utilizó el mismo sistema para registrar fechas y nunca había detectado problemas. El `31/12/1999` funcionó normalmente. Al día siguiente, una persona ingresó `01/01/2000`, pero el sistema mostró `01/01/1900`.

Conversen en parejas y registren las respuestas en la sección 1 del documento:

1. Para la fecha `01/01/2000`, ¿cuál sería el resultado esperado y cuál podría ser el resultado obtenido?
2. ¿En qué parte del sistema buscarían el defecto: al ingresar, guardar o interpretar la fecha? Justifiquen.
3. Para evitar problemas, alguien propone reservar 5, 10 o 100 dígitos para guardar el año. ¿Tiene sentido elegir un tamaño tan grande “por las dudas”? ¿Qué habría que definir antes?
4. ¿El bug ya estaba en el programa antes del año 2000, aunque todavía no se hubiera visto? Expliquen.

## Laboratorio: probar una inscripción

Sincronicen el repositorio y abran el archivo [Inscripción a talleres](practicas/3-1_inscripcion_con_bugs.html), ubicado en `Eje_3_Testing/practicas/3-1_inscripcion_con_bugs.html`. La aplicación está en español, funciona sin Internet y contiene algunos errores intencionales.

Lean primero las reglas que aparecen a la derecha del formulario. Esas reglas permiten decidir qué resultado se debería obtener.

### Misión en pareja

- **Misión A — Datos obligatorios:** prueben una inscripción válida y después omitan distintos datos obligatorios.
- **Misión B — Edades:** prueben valores dentro, fuera y justo en los límites permitidos.
- **Misión C — Confirmación y limpieza:** comparen los datos elegidos con la confirmación y comprueben qué ocurre al limpiar.

Realicen **tres pruebas relacionadas con su misión**. Antes de cada acción acuerden qué esperan que ocurra. Luego completen una fila de la tabla de la sección 2:

1. **Qué probaron:** campo, botón o parte del formulario.
2. **Acción:** clics, opciones o cantidades utilizadas.
3. **Resultado esperado:** qué debía suceder y por qué.
4. **Resultado obtenido:** qué sucedió realmente y qué mensaje apareció.
5. **Decisión:** `Funcionó como esperábamos`, `Sospechoso` o `Falta información`.

No necesitan encontrar un bug en cada prueba. Una prueba que funciona correctamente también aporta información. No busquen la solución en Internet ni escriban solamente `no funciona`: describan lo que hicieron y lo que observaron.

| Prueba | Qué probaron y qué acción realizaron | Resultado esperado | Resultado obtenido | Decisión |
| --- | --- | --- | --- | --- |
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |

### Ejemplo de registro

Este ejemplo pertenece a otra aplicación ficticia y no al formulario de talleres:

| Prueba | Qué probaron y qué acción realizaron | Resultado esperado | Resultado obtenido | Decisión |
| --- | --- | --- | --- | --- |
| 1 | Formulario de inscripción. Dejamos `Nombre` vacío, escribimos `6A` en `Curso` y presionamos `Guardar`. | Como el nombre es obligatorio, el sistema debería avisarlo y no guardar la inscripción. | Apareció `Inscripción guardada` y se creó un registro sin nombre. | Sospechoso |
| 2 | Formulario de inscripción. Escribimos `Ana` en `Nombre`, `6A` en `Curso` y presionamos `Guardar`. | La inscripción debería guardarse y mostrar una confirmación. | Apareció `Inscripción guardada` y los datos se mostraron correctamente. | Funcionó como esperábamos |

## Evidencia de una prueba

Elijan **un solo comportamiento sospechoso** de su tabla y completen la sección 3 de la [plantilla de entrega](recursos/3-1_Plantilla_entrega.md). Si no encontraron ninguno, elijan una prueba que haya funcionado correctamente.

Incluyan:

- un título breve que indique dónde ocurre y qué observaron;
- las acciones necesarias para volver a esa situación;
- el resultado esperado y el obtenido;
- una captura legible y una oración que indique qué parte de la imagen se debe mirar.

### Ejemplo de evidencia

**Título:** Inscripción: permite guardar un registro sin nombre

**Acciones:**

1. Abrimos un formulario de inscripción vacío.
2. Dejamos vacío `Nombre`, escribimos `6A` en `Curso` y presionamos `Guardar`.

**Resultado esperado:** el sistema informa que el nombre es obligatorio y no crea la inscripción.

**Resultado obtenido:** aparece `Inscripción guardada` y se crea un registro sin nombre.

**Evidencia:** captura donde se observa el mensaje de confirmación y el registro con el nombre vacío.

El ejemplo no pertenece a la aplicación de talleres. Úsenlo solo como referencia para completar su propia evidencia.

## Para terminar

En la sección `Reflexión final` del documento respondan:

1. ¿Qué diferencia hay entre resultado esperado y resultado obtenido? Usen una de sus pruebas como ejemplo.

Antes de cerrar la computadora, comprueben que el documento tenga los nombres, las respuestas, las tres pruebas y una captura. Verifiquen que esté dentro de la carpeta de Drive compartida con el profesor y que ambos integrantes tengan acceso.
