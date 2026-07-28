# Clase 7: Observar con Wireshark el tráfico entre cliente y servidor

**Duración estimada:** 80 minutos  
**Organización:** grupos de 4 estudiantes  
**Pregunta guía:** ¿Qué paquetes circulan cuando un cliente abre Simon Proa desde un servidor de la red local?

## Objetivos

- Retomar los roles de cliente y servidor de la actividad 2-5.
- Volver a publicar Simon Proa con Live Server.
- Capturar desde un cliente el tráfico intercambiado con el servidor.
- Relacionar una acción del navegador con paquetes TCP y HTTP.
- Reconocer las direcciones IP, el puerto y algunos archivos solicitados.
- Reconocer respuestas HTTP como `200 OK` y `404 Not Found`.

## Punto de partida

En la actividad 2-5, una computadora funcionó como servidor y las demás abrieron Simon Proa como clientes. En esta clase repetiremos esa comunicación, pero utilizaremos Wireshark para observar lo que ocurre.

Recorrido:

```text
Navegador cliente → red local → Live Server → archivos de Simon Proa
```

Wireshark se utilizará solamente para capturar el tráfico generado por el propio grupo.

Cada grupo continuará el registro en un documento compartido de Google Drive. En cada evidencia debe escribir el número y el nombre del punto, pegar la captura correspondiente y responder la pregunta solamente cuando la actividad incluya una.

## Organización

| Computadora | Rol |
| --- | --- |
| Computadora A | Servidor de Simon Proa |
| Computadora B | Cliente y equipo de captura |
| Computadora C | Cliente |
| Computadora D | Cliente |

La captura principal se realizará en la **Computadora B**.

## Parte 1: recuperar el servidor

En la **Computadora A**:

1. Abrir la carpeta `simon-proa-2026` en Visual Studio Code.
2. Abrir `index.html`.
3. Seleccionar **Open with Live Server**.
4. Comprobar que Simon Proa funcione en el navegador del servidor.
5. Ejecutar:

```powershell
ipconfig
```

6. Anotar la dirección IPv4 de la interfaz conectada.
7. Identificar el puerto de Live Server. Normalmente es `5500`.

Completar:

| Dato | Valor |
| --- | --- |
| IP del servidor | |
| Puerto de Live Server | |

**Evidencia en Drive — Parte 1:** escribir el título del punto, completar los datos y pegar una captura del servidor con Simon Proa funcionando.

## Parte 2: comprobar la conexión

En la **Computadora B**:

1. Probar la comunicación con el servidor:

```powershell
ping IP_DEL_SERVIDOR
```

2. Construir la URL:

```text
http://IP_DEL_SERVIDOR:PUERTO
```

Ejemplo:

```text
http://192.168.1.25:5500
```

3. Abrir la URL y comprobar que cargue Simon Proa.
4. Cerrar esa pestaña antes de iniciar la captura.

**Evidencia en Drive — Parte 2:** escribir el título del punto, anotar la URL utilizada y pegar una captura del resultado del `ping`.

## Parte 3: preparar Wireshark

En la **Computadora B**:

1. Abrir Wireshark.
2. Seleccionar la interfaz que conecta el equipo a la red, por ejemplo **WiFi** o **Ethernet**.
3. Iniciar una captura.
4. Volver al navegador.
5. Abrir la URL del servidor.
6. Presionar `Ctrl + F5` para forzar una nueva carga de los archivos.
7. Esperar a que aparezca Simon Proa.
8. Detener inmediatamente la captura.

**Evidencia en Drive — Parte 3:** escribir el título del punto y pegar una captura de Wireshark con el tráfico capturado.

## Parte 4: encontrar la conversación

Reemplazar los datos del siguiente filtro por la IP y el puerto reales del servidor:

```text
ip.addr == IP_DEL_SERVIDOR && tcp.port == PUERTO
```

Ejemplo:

```text
ip.addr == 192.168.1.25 && tcp.port == 5500
```

Observar:

- paquetes enviados desde el cliente hacia el servidor;
- paquetes enviados desde el servidor hacia el cliente;
- la IP del cliente;
- la IP del servidor;
- el puerto de Live Server;
- la cantidad de paquetes generados al cargar una sola página.

Pregunta para discutir:

> ¿Por qué aparecen varios paquetes si el usuario realizó una sola acción en el navegador?

**Evidencia en Drive — Parte 4:** escribir el título del punto, pegar una captura con el filtro por IP y puerto y responder la pregunta anterior.

## Parte 5: buscar los pedidos HTTP

Probar:

```text
http
```

También se puede probar:

```text
http.request
```

Si Wireshark reconoce el tráfico como HTTP, buscar solicitudes de archivos como:

- `index.html`;
- `styles.css`;
- `game.js`;
- imágenes;
- sonidos.

Si no aparecen paquetes con el filtro `http`, volver al filtro por IP y puerto. Esto significa que Wireshark encontró la comunicación TCP, aunque no la haya interpretado automáticamente como HTTP por utilizar un puerto no habitual.

Comparar:

| Elemento | Dato encontrado |
| --- | --- |
| IP del cliente | |
| IP del servidor | |
| Puerto del servidor | |
| Un archivo solicitado | |

**Evidencia en Drive — Parte 5:** escribir el título del punto, completar la tabla y pegar una captura con `http` o `http.request`. Si Wireshark no reconoce HTTP, usar el filtro por IP y puerto.

## Parte 6: observar las respuestas del servidor

Cada solicitud HTTP recibe una respuesta con un código de estado. Algunos ejemplos son:

Video de apoyo:

> [Protocolo HTTP y códigos de respuesta](https://www.youtube.com/watch?v=yZgZIzgpXks)

| Código | Significado |
| --- | --- |
| `200 OK` | El servidor encontró y entregó el recurso. |
| `404 Not Found` | El recurso solicitado no existe. |
| `500 Internal Server Error` | El servidor encontró un error interno. |
| `503 Service Unavailable` | El servidor está disponible, pero temporalmente no puede atender la solicitud. |

En la **Computadora B**:

1. Iniciar una captura nueva.
2. Abrir PowerShell.
3. Solicitar un archivo existente:

```powershell
curl.exe -i http://IP_DEL_SERVIDOR:PUERTO/index.html
```

4. Solicitar un archivo que no existe:

```powershell
curl.exe -i http://IP_DEL_SERVIDOR:PUERTO/archivo-que-no-existe.html
```

5. Detener la captura.
6. Aplicar el filtro:

```text
http.response
```

Para observar cada respuesta por separado, también se pueden probar:

```text
http.response.code == 200
```

```text
http.response.code == 404
```

Comparar:

| Recurso solicitado | Código recibido | ¿Qué significa? |
| --- | --- | --- |
| `index.html` | | |
| `archivo-que-no-existe.html` | | |

Si Wireshark no interpreta automáticamente el puerto de Live Server como HTTP, conservar el filtro por IP y puerto y observar los códigos en la salida de `curl.exe`.

**Evidencia en Drive — Parte 6:** escribir el título del punto, completar la tabla y pegar una captura donde se observe una respuesta `200` o `404`.

## Parte 7: comprobar qué ocurre al detener el servidor

1. En la **Computadora A**, detener Live Server.
2. En la **Computadora B**, iniciar una captura nueva.
3. Intentar recargar la misma URL.
4. Detener la captura.
5. Aplicar nuevamente el filtro por IP y puerto.

Comparar ambas situaciones:

| Situación | ¿Cargó Simon Proa? | ¿Hubo respuesta del servidor? |
| --- | --- | --- |
| Live Server encendido | | |
| Live Server detenido | | |


**Evidencia en Drive — Parte 7:** escribir el título del punto, completar la comparación y pegar una captura del intento realizado con Live Server detenido.

Antes de pegar cualquier captura, verificar que no contenga datos personales ni tráfico ajeno a la actividad.

## Cierre

Responder para pensar:

1. ¿Qué computadora pidió los archivos?
2. ¿Qué computadora respondió?
3. ¿Qué datos permiten distinguir al cliente del servidor?
4. ¿Por qué se generaron varios paquetes al abrir una sola página?
5. ¿Qué diferencia existe entre las respuestas `200` y `404`?
6. ¿Por qué detener Live Server no genera una respuesta `503`?
7. ¿Qué cambió en la captura cuando Live Server fue detenido?
