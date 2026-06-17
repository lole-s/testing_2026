# Clase 4: Práctica - MAC, IP, ARP y red local

**Duración estimada:** 80 minutos  
**Pregunta guía:** ¿Cómo encuentra una computadora a otra dentro de la red local?

## Objetivos de la clase

- Reforzar la diferencia entre MAC e IP.
- Observar la tabla ARP de una computadora.
- Entender ARP como una consulta dentro de la red local.
- Ver cómo se completa la tabla ARP antes y después de comunicarse con otros equipos.
- Diferenciar qué ocurre con ARP en un destino local y en un destino de Internet.
- Representar una LAN con equipos, IPs, MACs, switch/router y conexiones.

## Repaso rápido

Una computadora puede conocer la IP de destino, pero dentro de una red local también necesita saber a qué dirección MAC debe enviar la información.

**ARP** significa Address Resolution Protocol. Sirve para relacionar una IP con una MAC dentro de la red local.

Idea simple:

> ARP pregunta: "¿Quién tiene esta IP? Decime tu MAC".

ARP no se usa para encontrar la MAC de cualquier servidor de Internet. Si el destino está fuera de la red local, la computadora busca la MAC de la **puerta de enlace** y le entrega el paquete al router.

## Práctica

### Paso 1: observar datos propios

Ejecutar:

```powershell
ipconfig /all
```

Registrar:

| Dato | Valor |
| --- | --- |
| IPv4 | |
| MAC o dirección física | |
| Puerta de enlace | |

### Paso 2: observar la tabla ARP inicial

Ejecutar:

```powershell
arp -a
```

Registrar qué IPs y MACs aparecen antes de hacer nuevas pruebas.

### Paso 3: hacer ping a la puerta de enlace

Ejecutar:

```powershell
ping IP_DE_LA_PUERTA_DE_ENLACE
```

Luego ejecutar:

```powershell
arp -a
```

Buscar si aparece la IP de la puerta de enlace y una dirección física asociada.

### Paso 4: hacer ping a otro equipo de la red local

Si la red lo permite, pedir la IP a otro grupo y ejecutar:

```powershell
ping IP_DEL_OTRO_EQUIPO
```

Luego ejecutar:

```powershell
arp -a
```

Buscar si aparece la IP del otro equipo y una MAC asociada.

### Paso 5: borrar la caché ARP y volver a generarla

Ejecutar:

```powershell
arp -d *
```

Luego observar la tabla:

```powershell
arp -a
```

Después volver a hacer ping a la puerta de enlace:

```powershell
ping IP_DE_LA_PUERTA_DE_ENLACE
```

Y revisar otra vez:

```powershell
arp -a
```

La idea es observar que la tabla ARP se puede vaciar y volver a completar cuando la computadora necesita comunicarse.

### Paso 6: comparar un destino local con un destino de Internet

Ejecutar:

```powershell
ping IP_DEL_OTRO_EQUIPO
ping 8.8.8.8
arp -a
```

Observar:

- si aparece la MAC del otro equipo del aula;
- si aparece la MAC de `8.8.8.8`;
- si vuelve a aparecer la MAC de la puerta de enlace.

Pregunta clave:

> Para llegar a `8.8.8.8`, ¿la computadora necesita la MAC de `8.8.8.8` o la MAC de la puerta de enlace?

### Paso 7: registrar lo observado

| Momento de la prueba | Comando usado | IP observada | MAC asociada | Qué creemos que significa |
| --- | --- | --- | --- | --- |
| Tabla ARP inicial | `arp -a` | | | |
| Después de ping a puerta de enlace | `ping ...` y `arp -a` | | | |
| Después de ping a otro equipo | `ping ...` y `arp -a` | | | |
| Después de borrar caché ARP | `arp -d *` y `arp -a` | | | |
| Después de ping a `8.8.8.8` | `ping 8.8.8.8` y `arp -a` | | | |

## Nota breve: lo inverso de ARP

ARP busca una **MAC** a partir de una **IP**.

Históricamente existió **RARP** (*Reverse ARP*), que hacía lo inverso: buscar una IP a partir de una MAC. Hoy casi no se usa. En redes actuales, la asignación automática de IP normalmente la realiza **DHCP**.

## Producto grupal

Dibujar un esquema de una LAN con:

- 4 computadoras del grupo;
- un switch o router;
- la IP de cada computadora;
- la MAC de cada computadora, si se puede registrar;
- la puerta de enlace;
- flechas que indiquen comunicación local.

Puede ser un dibujo en hoja, pizarra, documento o README.

## Preguntas de cierre

1. ¿Qué dato cambia más fácilmente: la IP o la MAC?
2. ¿Por qué una computadora necesita MAC e IP?
3. ¿Qué información muestra `arp -a`?
4. ¿Qué cambió en la tabla ARP después de hacer `ping`?
5. ¿Qué pasó después de usar `arp -d *`?
6. ¿Para llegar a `8.8.8.8`, qué MAC necesita conocer la computadora?
7. ¿En qué parte del mapa final del eje ubicaríamos ARP?
