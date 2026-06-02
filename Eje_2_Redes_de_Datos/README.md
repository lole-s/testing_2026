# Eje 2: Redes de datos

## Pregunta guía

**¿Qué pasa cuando una computadora quiere comunicarse con otra?**

Durante este eje vamos a construir una visión general de cómo funciona una red TCP/IP e Internet. La idea no es estudiar redes en profundidad, sino entender las piezas principales y poder explicar, con vocabulario técnico inicial, cómo viaja la información desde una aplicación hasta otra.

## Objetivos

Al finalizar el eje, se espera que cada estudiante pueda:

- Explicar qué es una red de computadoras y qué es Internet.
- Reconocer que la información viaja dividida en paquetes.
- Diferenciar una dirección **MAC** de una dirección **IP**.
- Identificar el rol básico de **switch**, **router**, **DNS**, **TCP/IP**, **HTTP** y **puerto**.
- Usar comandos simples de Windows para observar la red: `ipconfig`, `ping` y `arp -a`.
- Explicar el recorrido de un mensaje entre un cliente y un servidor dentro de una red local.

## Secuencia 2026

| Clase | Tema | Material |
| --- | --- | --- |
| 1 | Charla introductoria: Internet, cables, paquetes y preguntas iniciales | [2-1_Charla_introductoria_Internet_y_redes.md](./2-1_Charla_introductoria_Internet_y_redes.md) |
| 2 | Teoría inicial: red local, Internet, MAC, IP, router y DNS | [2-2_Teoria_inicial_Redes_TCP-IP.md](./2-2_Teoria_inicial_Redes_TCP-IP.md) |
| 3 | Conectividad: `ipconfig`, `ping`, IP y dominios | [2-3_Practica_conectividad_IP_DNS_Ping.md](./2-3_Practica_conectividad_IP_DNS_Ping.md) |
| 4 | IP, MAC, ARP y red local | [2-4_Practica_MAC_IP_ARP_LAN.md](./2-4_Practica_MAC_IP_ARP_LAN.md) |
| 5 | Cliente-servidor y HTTP en la red local | [2-5_Practica_cliente_servidor_HTTP.md](./2-5_Practica_cliente_servidor_HTTP.md) |
| 6 y 7 | Proyecto grupal: mapa del recorrido de la información y exposición | [2-6_Proyecto_grupal_Como_viaja_la_informacion.md](./2-6_Proyecto_grupal_Como_viaja_la_informacion.md) |
| 8 opcional | Wireshark o situaciones problema de integración | [2-7_Integracion_Wireshark_y_situaciones_problema.md](./2-7_Integracion_Wireshark_y_situaciones_problema.md) |

Material de cierre:

- [Evaluación breve del eje](./2-z_Evaluacion_breve_Eje_2_Redes_de_Datos.md)

## Actividad central teórico-práctica

El eje se organiza alrededor de una actividad grupal para **6 grupos de 4 estudiantes**:

> Construir y explicar un mapa del recorrido de la información en una red TCP/IP.

La actividad combina dos momentos:

- **Momento teórico:** formular una hipótesis, construir el mapa del recorrido y explicar los conceptos principales con palabras propias.
- **Momento práctico:** relevar datos reales de red, probar conectividad y acceder a un servidor local desde otra computadora.

Cada grupo deberá:

- Dibujar el recorrido de un mensaje desde una computadora cliente hasta un servidor.
- Relevar IP, MAC, puerta de enlace y DNS de una PC.
- Probar conectividad usando `ping`.
- Acceder a un servidor local simple desde otra computadora.
- Entregar evidencias y una explicación corta con palabras propias.

## Vocabulario mínimo

- red
- host
- cliente
- servidor
- medio físico
- paquete
- protocolo
- dirección MAC
- dirección IP privada
- dirección IP pública
- switch
- router
- DNS
- HTTP
- TCP/IP
- puerto
- ping
- ARP
