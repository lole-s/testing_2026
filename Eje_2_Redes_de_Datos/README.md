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
| 6 | Instalación y uso inicial de Wireshark: ARP, ICMP, DNS y HTTP | [2-6_Instalacion_y_uso_inicial_Wireshark.md](./2-6_Instalacion_y_uso_inicial_Wireshark.md) |
| 7 | Cierre práctico: construcción y diagnóstico de dos mini-LAN | [2-7_Construccion_y_diagnostico_mini_LAN.md](./2-7_Construccion_y_diagnostico_mini_LAN.md) |

Material de cierre:

- [Evaluación breve del eje](./2-z_Evaluacion_breve_Eje_2_Redes_de_Datos.md)

## Actividad integradora de cierre

El eje finaliza con una experiencia práctica para **6 grupos de 4 estudiantes**, organizados alrededor de dos routers domiciliarios:

> Construir dos redes locales aisladas, conectar notebooks, ofrecer Simon Proa como servicio web y diagnosticar fallas reales.

La integración se desarrolla en dos momentos:

- **Observación:** instalar Wireshark y reconocer tráfico ARP, ICMP, DNS y HTTP generado por acciones conocidas.
- **Construcción y diagnóstico:** configurar dos mini-LAN, observar DHCP, comprobar conectividad, acceder a un servidor local e introducir fallas controladas.

Los grupos deberán poder:

- diferenciar los puertos LAN y WAN de un router;
- reconocer qué dispositivo asigna las direcciones IP;
- relevar IP, MAC, puerta de enlace y DHCP;
- probar conectividad con `ping` y observar `arp -a`;
- acceder a Simon Proa desde clientes de la misma LAN;
- utilizar Wireshark para relacionar acciones con paquetes;
- diagnosticar y corregir una falla sencilla;
- explicar el recorrido con los equipos reales de la práctica.

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
