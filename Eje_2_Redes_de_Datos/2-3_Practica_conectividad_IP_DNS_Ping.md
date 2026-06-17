# Clase 3: Práctica de conectividad - IP, DNS y ping

**Duración estimada:** 80 minutos  
**Pregunta guía:** ¿Cómo sabemos si una computadora puede comunicarse con otra?

## Objetivos de la clase

- Usar `ping` para comprobar conectividad.
- Interpretar los datos principales de la respuesta de `ping`.
- Diferenciar probar una IP de probar un dominio.
- Usar `tracert` para observar el recorrido hacia los mismos destinos.
- Relacionar errores de conectividad con posibles causas.
- Registrar evidencias técnicas simples.

## Comando principal

El comando `ping` envía mensajes de prueba a otro equipo o servidor y espera una respuesta.

Ejemplo:

```powershell
ping 8.8.8.8
```

Si hay respuesta, significa que la computadora pudo comunicarse con ese destino.

### Detalles de la respuesta de `ping`

Cuando `ping` responde, no alcanza con mirar solamente si "anduvo" o "no anduvo". También conviene observar estos datos:

| Dato | Qué significa |
| --- | --- |
| `bytes` | Tamaño del mensaje de prueba enviado y recibido. |
| `tiempo` | Cuánto tardó la respuesta en volver. Se mide en milisegundos (`ms`). |
| `TTL` | Cantidad aproximada de saltos que todavía podía hacer el paquete antes de descartarse. |
| `paquetes enviados` | Cantidad de mensajes de prueba enviados. |
| `paquetes recibidos` | Cantidad de respuestas recibidas. |
| `paquetes perdidos` | Cantidad de mensajes que no tuvieron respuesta. |

Ejemplo de lectura:

```text
Respuesta desde 8.8.8.8: bytes=32 tiempo=25ms TTL=117
```

En este caso:

- hubo respuesta desde `8.8.8.8`;
- el paquete tardó `25 ms`;
- el valor de `TTL` fue `117`.

Si aparece `Tiempo de espera agotado`, significa que no llegó respuesta dentro del tiempo esperado.

## Comando complementario: `tracert`

El comando `tracert` permite observar los saltos que realiza un paquete hasta llegar a un destino.

Mientras `ping` responde si hay comunicación o no, `tracert` ayuda a ver por dónde intenta pasar la comunicación.

En Windows, ejecutar:

```powershell
tracert 8.8.8.8
```

Para esta práctica vamos a mirar especialmente:

| Dato | Qué observar |
| --- | --- |
| Número de salto | Cada equipo intermedio por el que pasa el paquete. |
| Tiempo de respuesta | Cuánto tarda cada salto en responder. |
| Primera dirección IP | Suele ser la puerta de enlace o router de la red local. |
| Asteriscos `* * *` | Ese salto no respondió dentro del tiempo esperado. No siempre significa que la conexión esté cortada. |
| Último salto | Debería corresponder al destino o a un equipo cercano al destino. |

Para destinos como `8.8.8.8` o `google.com`, normalmente se observan varios saltos, porque están fuera de la red local.

## Práctica grupal

Trabajar en grupos de 4. Registrar los resultados en una tabla.

### Paso 1: identificar la puerta de enlace

Ejecutar:

```powershell
ipconfig
```

Buscar la **puerta de enlace predeterminada**.

Luego probar:

```powershell
ping IP_DE_LA_PUERTA_DE_ENLACE
```

Ejemplo:

```powershell
ping 192.168.1.1
```

### Paso 2: probar una IP pública

Ejecutar:

```powershell
ping 8.8.8.8
```

### Paso 3: probar un dominio

Ejecutar:

```powershell
ping google.com
```

### Paso 4: probar otro equipo del aula

Si la red lo permite, pedir la IP a otro grupo y ejecutar:

```powershell
ping IP_DEL_OTRO_EQUIPO
```

### Paso 5: observar el recorrido hacia los mismos destinos

Ejecutar los siguientes comandos:

```powershell
tracert IP_DE_LA_PUERTA_DE_ENLACE
tracert 8.8.8.8
tracert google.com
```

Si la red lo permite, también probar:

```powershell
tracert IP_DEL_OTRO_EQUIPO
```

Luego completar:

1. Anotar cuántos saltos aparecen hasta cada destino.
2. Observar si el primer salto coincide con la puerta de enlace.
3. Comparar qué ocurre con un destino local y con un destino de Internet.
4. Registrar si aparecen asteriscos `* * *`.
5. Pensar qué destino parece estar más "cerca" según la cantidad de saltos.

Para un dominio como `google.com`, `tracert` primero resuelve el nombre a una dirección IP y luego muestra el recorrido.

## Registro de resultados

| Prueba | Comando usado | Resultado del ping | Detalles de la respuesta | Recorrido observado con `tracert` | Qué creemos que significa |
| --- | --- | --- | --- | --- | --- |
| Puerta de enlace | | | | | |
| IP pública `8.8.8.8` | | | | | |
| Dominio `google.com` | | | | | |
| Otro equipo del aula | | | | | |

## Interpretación inicial

| Situación | Posible interpretación |
| --- | --- |
| Responde la puerta de enlace | La PC se comunica con el router o red local. |
| Responde `8.8.8.8` | Hay salida hacia Internet usando IP. |
| Responde `google.com` | Hay salida hacia Internet y DNS funciona. |
| Responde `8.8.8.8` pero no `google.com` | Puede haber un problema de DNS. |
| No responde la puerta de enlace | Puede haber problema de red local, WiFi, cable o configuración IP. |
| `tracert` muestra un solo salto hacia la puerta de enlace | La puerta de enlace está dentro de la red local. |
| `tracert` muestra varios saltos hacia `8.8.8.8` | El paquete atraviesa varios equipos hasta llegar a Internet. |
| `tracert` muestra asteriscos en algunos saltos | Algunos equipos intermedios no responden, aunque el recorrido puede continuar. |
| `tracert` no llega al destino | Puede haber un corte, bloqueo o problema en algún punto del recorrido. |

## Preguntas de cierre

1. ¿Qué diferencia hay entre hacer `ping 8.8.8.8` y `ping google.com`?
2. ¿Para qué sirve la puerta de enlace?
3. ¿Qué prueba harían primero si una computadora "no tiene Internet"?
4. ¿Qué datos de la respuesta de `ping` ayudan a justificar si la conexión funciona bien o no?
5. ¿Qué información aporta `tracert` que no aparece directamente en `ping`?
6. ¿Qué evidencia guardaría el grupo para demostrar que hizo la práctica?
