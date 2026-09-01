# Actividad integradora - para período de pasantías — Eje 2: Redes de datos

**Nombre y apellido:**  
**Curso:**  
**Fecha de entrega:**  

## ¿Qué vamos a integrar?

En esta actividad vas a usar los conceptos principales del eje para analizar una situación de red, explicar el recorrido de una solicitud web y proponer una solución.

Podés resolverla en una hoja o en un archivo digital. No necesitás instalar programas ni ejecutar comandos.

## Situación: no podemos abrir Simon Proa

En una red local hay dos computadoras conectadas al mismo router:

| Equipo | Función | Dirección IP | Dirección MAC |
| --- | --- | --- | --- |
| Computadora de Lara | Cliente | `192.168.1.20` | `A1-A1-A1-A1-A1-A1` |
| Computadora de Tomás | Servidor | `192.168.1.35` | `B2-B2-B2-B2-B2-B2` |

En la computadora de Tomás:

- Simon Proa está formado por archivos HTML, CSS, JavaScript y sonidos;
- Live Server está funcionando en el puerto `5500`;
- el router tiene la dirección IP `192.168.1.1`.

Lara escribe en su navegador:

```text
http://192.168.1.53:5500
```

La página no abre. Sin embargo, al ejecutar `ping 192.168.1.35`, recibe respuestas correctamente.

## Parte 1: interpretar la información

1. Indicá cuál es el **cliente** y cuál es la **computadora servidor**.
2. ¿Qué programa funciona como cliente?
3. ¿Qué función cumple Live Server?
4. ¿Qué es Simon Proa en esta situación?
5. En la dirección escrita por Lara, identificá:
   - el protocolo;
   - la dirección IP;
   - el puerto.
6. Compará la dirección que escribió Lara con los datos de la tabla. ¿Cuál es el error?
7. Escribí la URL correcta que debería usar.

## Parte 2: explicar el recorrido

8. Dibujá un esquema que represente el recorrido de la solicitud y la respuesta. Debe incluir y relacionar estos elementos:

   - Lara;
   - navegador;
   - computadora cliente;
   - red local o router;
   - paquetes;
   - dirección IP y dirección MAC;
   - computadora servidor;
   - Live Server;
   - Simon Proa;
   - solicitud HTTP y respuesta HTTP.

Usá flechas y distinguí claramente el viaje del pedido del regreso de la respuesta.

9. Debajo del dibujo, explicá el recorrido con tus palabras en un texto de entre **8 y 12 líneas**.

## Parte 3: pensar y diagnosticar

10. ¿Qué demuestra el resultado exitoso de `ping 192.168.1.35`?
11. Si Lara escribe la URL correcta pero la página todavía no abre porque Tomás cerró Live Server, ¿qué elemento de la comunicación dejó de estar disponible?
12. En esta situación se usa directamente una dirección IP. ¿Es necesario consultar a DNS? Justificá.
13. Explicá una diferencia entre una dirección IP y una dirección MAC usando los datos del caso como ejemplo.

## Forma de entrega

Elegí una opción:

- **En papel:** entregá las respuestas y el dibujo en hojas con nombre, apellido y curso.
- **Digital:** enviá por correo un archivo PDF, documento o fotografías legibles de las hojas.

Nombre sugerido para el archivo:

```text
Apellido_Nombre_Actividad_Eje2.pdf
```

Antes de entregar, comprobá que:

- respondiste las 13 consignas;
- el dibujo tiene flechas, pedido y respuesta;
- usaste vocabulario del eje;
- la escritura o las fotografías se leen con claridad;
- el archivo tiene tu nombre y apellido.

## Criterios de evaluación

| Criterio | Puntaje |
| --- | ---: |
| Identificación de cliente, servidor, aplicación, IP, puerto y protocolo | 3 puntos |
| Representación y explicación del recorrido | 3 puntos |
| Diagnóstico de las dos fallas | 2 puntos |
| Uso correcto de DNS, IP, MAC y `ping` | 1 punto |
| Claridad, presentación y entrega completa | 1 punto |
| **Total** | **10 puntos** |

> No se evalúa repetir definiciones de memoria. Se evalúa que puedas relacionar los conceptos y explicar qué sucede en esta situación.
