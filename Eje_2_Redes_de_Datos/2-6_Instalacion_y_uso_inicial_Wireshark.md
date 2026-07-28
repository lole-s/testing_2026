# Clase 6: Instalación y uso inicial de Wireshark
**Modalidad:** grupos de 4 estudiantes  
**Pregunta guía:** ¿Cómo podemos observar los mensajes que circulan por una red?

## Objetivos

- Instalar Wireshark y el componente de captura Npcap.
- Reconocer la interfaz de red activa.
- Iniciar, detener y guardar una captura breve.
- Generar tráfico conocido y encontrarlo mediante filtros.
- Reconocer inicialmente ARP, ICMP, DNS y HTTP.
- Relacionar los paquetes observados con las prácticas anteriores.

## Idea central

Wireshark permite capturar y analizar tráfico de red. En esta actividad no intentaremos comprender todos los campos de cada paquete. Buscaremos mensajes que nosotros mismos generamos y los relacionaremos con acciones conocidas.

Cada grupo creará un documento compartido en Google Drive para registrar la práctica. En cada evidencia debe escribir el número y el nombre del punto, pegar la captura correspondiente y responder la pregunta solamente cuando la actividad incluya una.

## Antes de comenzar: ¿cómo viaja la información?

Cuando enviamos un mensaje por una red, la computadora lo representa mediante bits, es decir, valores `0` y `1`. Para trasladarlos de un dispositivo a otro se utilizan distintos tipos de señales:

- En un cable de cobre, la información se representa mediante cambios en una señal eléctrica.
- En fibra óptica, mediante pulsos de luz.
- En Wi‑Fi, mediante ondas electromagnéticas que viajan por el aire.

La interfaz de red recibe estas señales y las interpreta como información digital organizada en tramas y paquetes. Wireshark no muestra directamente las ondas ni los impulsos físicos: muestra los paquetes después de que la placa de red decodificó la señal.

Video introductorio:

> [Introducción a Wireshark](https://www.youtube.com/watch?v=j86mlJz64eA)

## Parte 1: instalación en Windows

Descargar el instalador desde el sitio oficial:

<https://www.wireshark.org/download.html>

Durante la instalación:

1. aceptar los componentes principales de Wireshark;
2. mantener seleccionada la instalación de **Npcap**;
3. completar el asistente;
4. reiniciar la computadora solamente si el instalador lo solicita;
5. abrir Wireshark.

Npcap es necesario para realizar capturas en vivo. Si la computadora no permite instalar software, solicitar ayuda al docente. Como alternativa se puede trabajar con una captura preparada previamente.

**Evidencia en Drive — Parte 1:** escribir el título del punto y pegar una captura de Wireshark abierto.

> **Nota:** para tomar una captura, presionar `Windows + Shift + S`, seleccionar el sector de la pantalla y pegarlo en el documento con `Ctrl + V`.

## Parte 2: reconocer la interfaz activa

En Wireshark aparecerá una lista de interfaces, por ejemplo:

- WiFi;
- Ethernet;
- Bluetooth;
- interfaces virtuales.

Antes de capturar:

1. buscar en Wireshark la interfaz que muestra actividad;
2. hacer doble clic sobre esa interfaz para comenzar;
3. detener la captura con el botón rojo después de unos segundos.

**Evidencia en Drive — Parte 2:** escribir el título del punto y pegar una captura donde se vea la interfaz activa identificada.

## Parte 3: conocer la pantalla

Wireshark presenta tres zonas principales:

1. **Lista de paquetes:** muestra una fila por cada paquete capturado.
2. **Detalles del paquete:** organiza la información por protocolos y capas.
3. **Bytes del paquete:** muestra la información en su representación interna.

También utilizaremos la barra **Display filter** para mostrar únicamente el tráfico que nos interesa.

**Evidencia en Drive — Parte 3:** escribir el título del punto y pegar una captura de Wireshark. Enumerar las tres zonas principales.

## Parte 4: observar ICMP con `ping`

1. Iniciar una captura nueva.
2. Abrir PowerShell.
3. Ejecutar un `ping` a la puerta de enlace o a otra computadora autorizada:

```powershell
ping IP_DEL_DESTINO
```

4. Detener la captura.
5. Escribir este filtro:

```text
icmp
```

6. Buscar mensajes `Echo request` y `Echo reply`.
7. Comparar las direcciones de origen y destino.

### Curiosidad: los datos que viajan dentro del `ping`

Seleccionar un paquete `Echo request` y observar la zona **Bytes del paquete**. En la parte derecha puede aparecer una secuencia de letras del abecedario, por ejemplo:

```text
abcdefghijklmnopqrstuvwabcdefghi
```

Estas letras no son un mensaje escrito por una persona. Windows las agrega automáticamente como **carga útil** o datos de prueba del `ping`. Al responder, el equipo de destino devuelve normalmente los mismos datos en el paquete `Echo reply`.

Comparar la carga útil del `Echo request` con la del `Echo reply`:

> ¿Las letras que aparecen en ambos paquetes son iguales?

Pregunta para discutir:

> ¿Qué paquete representa la pregunta de `ping` y cuál representa la respuesta?

**Evidencia en Drive — Parte 4:** escribir el título del punto, pegar una captura con el filtro `icmp` y responder las preguntas de esta parte.

## Parte 5: observar ARP

1. Iniciar otra captura.
2. Ejecutar `ping` a un equipo de la red local.
3. Detener la captura.
4. Aplicar el filtro:

```text
arp
```

5. Buscar una consulta y una respuesta ARP, si aparecen.
6. Observar las direcciones IP y MAC involucradas.

Es posible que no aparezca una nueva consulta si la relación IP–MAC ya estaba guardada en la caché ARP. En ese caso se puede observar otra IP local o revisar una captura preparada por el docente.

**Evidencia en Drive — Parte 5:** escribir el título del punto y pegar una captura con el filtro `arp`, donde se vea una consulta o una respuesta.

## Parte 6: observar DNS

1. Iniciar una captura.
2. Ejecutar:

```powershell
nslookup example.com
```

3. Detener la captura.
4. Aplicar el filtro:

```text
dns
```

5. Identificar la consulta que contiene el dominio.
6. Buscar la respuesta que informa una dirección IP.

Pregunta para discutir:

> ¿Qué dato conocía la computadora antes de consultar y qué dato obtuvo como respuesta?

**Evidencia en Drive — Parte 6:** escribir el título del punto, pegar una captura con el filtro `dns` y responder la pregunta anterior.

## Parte 7: observar una consulta web

En esta parte observaremos una consulta HTTP a un sitio externo.

### Consulta HTTP

1. Iniciar una captura.
2. Abrir PowerShell.
3. Ejecutar:

```powershell
curl.exe http://example.com
```

4. Detener la captura cuando aparezca la respuesta.
5. Aplicar alguno de estos filtros:

```text
http
```

```text
http.request
```

6. Seleccionar la solicitud `GET` y buscar:

- la dirección IP de origen;
- la dirección IP de destino;
- el método `GET`;
- el nombre `example.com`.

**Evidencia en Drive — Parte 7:** escribir el título del punto y pegar una captura con el filtro `http` o `http.request`, donde se vea la consulta a `example.com`.

### Opcional: comparación con HTTPS

1. Iniciar una captura nueva.
2. Abrir en el navegador:

<https://simon-proa-2026.vercel.app/>

3. Presionar `Ctrl + F5` para forzar una nueva carga.
4. Detener la captura cuando termine de cargar la página.
5. Probar estos filtros:

```text
dns
```

```text
tls
```

```text
quic
```

Según el navegador y la conexión utilizada, pueden aparecer paquetes TLS, QUIC o ambos. A diferencia de la consulta HTTP anterior, el contenido de la solicitud HTTPS viaja cifrado y no se podrá leer directamente en Wireshark.

Pregunta para discutir:

> ¿Qué información podemos reconocer al visitar Simon Proa y qué información queda protegida por el cifrado?

**Evidencia opcional en Drive:** pegar una captura con `dns`, `tls` o `quic` y responder la pregunta anterior. Esta evidencia no es obligatoria.


