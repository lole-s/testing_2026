# Práctica de repaso: cliente, servidor y HTTP

**Modalidad:** grupos de 4 estudiantes   
**Materiales:** tarjetas impresas, hoja A3, lapiceras y una computadora por grupo

## Pregunta guía

> ¿Qué sucede desde que una persona escribe una URL hasta que la página o aplicación web aparece en el navegador?

## Objetivos

En esta actividad vamos a recuperar y relacionar los conceptos principales del eje de redes:

- cliente y servidor;
- computadora servidor, servidor web y aplicación web;
- dirección IP y dirección MAC;
- ARP y red local;
- DNS;
- HTTP y puerto;
- solicitud y respuesta.

## Roles del grupo

Distribuyan estos roles. Todos deben participar de las decisiones:

- **Coordinación:** organiza los tiempos y permite que todos participen.
- **Lectura:** lee las tarjetas y las consignas en voz alta.
- **Registro:** anota en una hoja aparte las decisiones del grupo, si el docente lo solicita.
- **Presentación:** explica el recorrido durante la puesta en común.

## Parte 1: Leer y clasificar las tarjetas

1. Coloquen todas las tarjetas sobre la mesa.
2. Lean en voz alta el título y el texto de cada una.
3. Conversen sobre las palabras o conceptos que no recuerden.
4. Agrupen provisoriamente las tarjetas en estas zonas:
   - **cliente**;
   - **red**;
   - **servidor**.
5. Separen las tarjetas que consideren dudosas o incorrectas.

En este momento no deben numerarlas ni pegarlas.

## Parte 2: construir el recorrido

Ordenen las tarjetas para representar el recorrido desde que una persona escribe una URL hasta que Simon Proa aparece en el navegador de una computadora cliente.

El recorrido debe mostrar:

- quién inicia la acción;
- qué programa actúa como cliente;
- cómo se identifica el destino;
- qué sucede dentro de la red local;
- cómo se realiza el pedido;
- qué equipo recibe la comunicación;
- qué programa escucha y responde;
- qué archivos forman la aplicación web;
- qué información regresa al navegador.

### Condiciones del desafío

- Entre las tarjetas existen 2 afirmaciones incorrectas.
- El grupo debe detectarlas leyendo su contenido.
- Una tarjeta incorrecta no debe formar parte del recorrido final.
- Por cada tarjeta descartada, el grupo debe escribir una versión corregida.
- No peguen las tarjetas hasta que todos estén de acuerdo.
- Si existen dos órdenes posibles, el grupo debe elegir uno y justificarlo.

Cuando acuerden el recorrido:

1. numeren las tarjetas correctas;
2. peguen las tarjetas;
3. dibujen una flecha para representar el pedido;
4. dibujen otra flecha para representar la respuesta;
5. preparen una explicación oral de uno o dos minutos.

## Parte 4: preguntas para comprobar el recorrido

Respondan utilizando las tarjetas y el recorrido armado.

1. ¿Quién realiza la solicitud?
2. ¿La persona usuaria y el programa cliente son lo mismo? Expliquen.
3. ¿La computadora servidor y el servidor web son exactamente lo mismo?
4. ¿Qué función cumple Live Server?
5. ¿Qué es Simon Proa dentro de esta práctica?
6. ¿Dónde aparecen la dirección IP y el puerto?
7. ¿Para qué sirve DNS?
8. ¿Interviene DNS si escribimos directamente `http://192.168.1.25:5500`? Justifiquen.


## Parte 5: simulación online de DNS

Ingresen a:

<https://packet.school/en/sandbox/dns>

La página está en inglés. 

### Procedimiento

1. Elijan o escriban un dominio, según las opciones disponibles.
2. Inicien la simulación.
3. Observen una vez el recorrido completo.
4. Reinicien la simulación.
5. Vuelvan a observarla y registren los participantes y mensajes que aparecen.
6. Identifiquen qué dato conoce el cliente al comienzo y qué dato obtiene al finalizar.

## Desafío adicional

Si terminaron el recorrido, las preguntas y la simulación DNS, pueden ingresar a:

<https://packet.school/en/sandbox/challenge>

Antes de confirmar una respuesta, deben discutirla y acordarla en grupo. No se trata de avanzar por prueba y error. Al finalizar, deben poder contar qué desafío resolvieron y qué concepto utilizaron.

## Entregable grupal

El grupo debe presentar:

- recorrido final con las tarjetas numeradas;
- tarjetas incorrectas separadas y corregidas;
- explicación oral breve.

## Próxima clase

Utilizaremos este recorrido para completar la práctica cliente-servidor:

1. una computadora levantará Live Server;
2. las demás computadoras actuarán como clientes;
3. accederemos a Simon Proa mediante la IP y el puerto del servidor;
4. registraremos evidencias de la comunicación;
5. comprobaremos qué sucede cuando se detiene el servidor web.
