# Clase 2: Teoría inicial - Redes TCP/IP

**Duración estimada:** 80 minutos  
**Pregunta guía:** ¿Cómo se identifican los equipos dentro de una red?

## Objetivos de la clase

- Comprender qué es una red local.
- Diferenciar Internet de una red local.
- Distinguir dirección MAC y dirección IP.
- Reconocer el rol inicial de router, switch y DNS.
- Usar `ipconfig /all` para observar datos reales de red.


## Video introductorio
- ¿Que es internet? https://www.youtube.com/watch?v=GkA5WOeLWbM

## Conceptos mínimos

### Red de computadoras

Una red de computadoras es un conjunto de dispositivos conectados que pueden intercambiar información y compartir servicios.

Ejemplos de dispositivos conectados a una red:

- computadoras;
- celulares;
- impresoras;
- servidores;
- routers;
- cámaras;
- televisores.

### LAN e Internet

Una **LAN** es una red de área local. Por ejemplo, la red de la escuela, de una casa o de una oficina.

**Internet** es una red de redes. Conecta redes locales y redes de organizaciones de todo el mundo.

### Host

Un **host** es un dispositivo conectado a una red que puede enviar o recibir información. Una computadora, un celular o un servidor pueden ser hosts.

### Dirección MAC

La dirección **MAC** identifica una placa o interfaz de red. Es una dirección física asociada al hardware.

Ejemplo de formato:

```text
00-1A-2B-3C-4D-5E
```

Idea simple:

> La MAC ayuda a identificar un dispositivo dentro de la red local.

### Dirección IP

La dirección **IP** identifica a un dispositivo dentro de una red TCP/IP.

Ejemplo de formato IPv4:

```text
192.168.1.25
```

Idea simple:

> La IP indica dónde está un dispositivo dentro de una red.

### IP privada e IP pública

Una **IP privada** se usa dentro de una red local. Muchas casas o escuelas pueden repetir direcciones privadas sin problema, porque pertenecen a redes distintas.

Ejemplos comunes de IP privadas:

```text
192.168.x.x
10.x.x.x
172.16.x.x a 172.31.x.x
```

Una **IP pública** identifica una red o equipo en Internet. Generalmente la asigna el proveedor de Internet.

### Switch

Un **switch** conecta equipos dentro de una red local. Trabaja principalmente usando direcciones MAC.

Idea simple:

> El switch ayuda a que los dispositivos de una LAN se comuniquen entre sí.

### Router

Un **router** conecta redes distintas. En una casa o escuela, suele conectar la red local con Internet.

Idea simple:

> El router es la salida hacia otras redes.

### DNS

El **DNS** traduce nombres de dominio a direcciones IP.

Ejemplo:

```text
google.com -> una dirección IP
```

Idea simple:

> DNS funciona como una agenda: nos permite usar nombres fáciles en lugar de memorizar números.

## Mini práctica: 
- crear un documento y subir a la carpeta compartida de drive.

### Observando la red de la computadora de la Escuela 

Abrir la terminal de Windows y ejecutar:

```powershell
ipconfig /all
```

Buscar y registrar:

| Dato | Valor encontrado |
| --- | --- |
| Nombre del equipo | |
| Adaptador usado: WiFi o Ethernet | |
| Dirección IPv4 | |
| Máscara de subred | |
| Puerta de enlace predeterminada | |
| Servidores DNS | |
| Dirección física o MAC | |

## Preguntas de cierre

1. ¿Qué diferencia hay entre una MAC y una IP?
2. ¿Qué dato parece ser la salida hacia Internet?
3. ¿Para qué sirve DNS?
4. ¿Qué parte de la información observada no conocían antes?

## Glosario de la clase

- red
- LAN
- Internet
- host
- MAC
- IP privada
- IP pública
- switch
- router
- DNS
