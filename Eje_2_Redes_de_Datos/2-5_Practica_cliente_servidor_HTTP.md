# Clase 5: Practica - Cliente, servidor y HTTP con Simon Proa

**Duracion estimada:** 80 minutos  
**Pregunta guia:** Que pasa cuando una computadora ofrece una pagina y otras computadoras la abren?

## Objetivos de la clase

- Reconocer los roles de cliente y servidor.
- Preparar el repositorio de trabajo si no esta descargado.
- Instalar y usar Live Server en Visual Studio Code.
- Levantar un servidor web local simple.
- Acceder al servidor desde tres computadoras cliente usando IP y puerto.
- Relacionar HTTP con una aplicacion web real: **Simon Proa**.

## Conceptos minimos

### Cliente

Un **cliente** es el programa o dispositivo que solicita un servicio.

Ejemplo:

> Un navegador que pide una pagina web.

### Servidor

Un **servidor** es el programa o dispositivo que ofrece un servicio.

Ejemplo:

> Una computadora que entrega una pagina web a otras computadoras.

### Servidor web

Un **servidor web** es un software que recibe pedidos HTTP y responde entregando archivos o datos al navegador.

En esta practica usaremos **Live Server**, que alcanza para probar una pagina en la red local. En servidores reales suelen usarse programas como:

| Servidor web | Rol habitual |
| --- | --- |
| **Apache HTTP Server** | Muy usado en servidores Linux. Es abierto, flexible y se usa para publicar sitios y aplicaciones web. |
| **Microsoft IIS** | Servidor web integrado al ecosistema Windows Server. Es comun en organizaciones que trabajan con tecnologias Microsoft, por ejemplo .NET. |
| **Nginx** | Muy usado por su rendimiento y por manejar muchas conexiones al mismo tiempo. |

La idea importante para esta clase: Live Server, Apache, IIS o Nginx cumplen el mismo rol general: **escuchar pedidos de clientes y responder por HTTP**. Cambian la escala, la configuracion y el uso profesional.

### HTTP

**HTTP** es un protocolo de aplicacion usado por la web. Permite que un navegador pida paginas, archivos, imagenes, sonidos o datos a un servidor.

Ciclo basico:

1. El cliente abre una URL.
2. El navegador envia un pedido HTTP al servidor.
3. El servidor responde con archivos como `index.html`, `styles.css`, `game.js`, imagenes o sonidos.
4. El navegador muestra la pagina.

### HTTP y HTTPS

En esta practica vamos a usar **HTTP**, porque Live Server publica la pagina dentro de la red local del aula y alcanza para observar claramente la comunicacion entre cliente y servidor.

En Internet, muchas paginas usan **HTTPS**. HTTPS cumple el mismo objetivo general que HTTP, pero agrega una capa de seguridad: cifra la comunicacion entre el navegador y el servidor. Por eso el navegador suele mostrar un candado en la barra de direcciones.

Comparacion rapida:

| Protocolo | Que hace | Puerto comun | Donde lo vemos |
| --- | --- | --- | --- |
| **HTTP** | Envia pedidos y respuestas web sin cifrado. | `80` | Practicas locales, pruebas, sitios sin certificado. |
| **HTTPS** | Envia pedidos y respuestas web cifrados. | `443` | Bancos, correos, redes sociales, tiendas y la mayoria de sitios actuales. |

Pregunta para observar durante la practica:

> Si nuestra URL empieza con `http://`, que diferencia habria con una pagina de Internet que empieza con `https://`?

Videos de apoyo:

- [Que es la Web?](https://www.youtube.com/watch?v=kXhXgcVpAU8)
- [Pagina, sitio y app web](https://www.youtube.com/watch?v=BUyaHveV9rY)
- [HTTP y HTTPS](https://www.youtube.com/watch?v=60606AHuq8c)

### Puerto

Un **puerto** ayuda a identificar a que servicio queremos entrar dentro de una misma computadora.

Ejemplos comunes:

- `80`: HTTP tradicional.
- `443`: HTTPS.
- `5500`: usado muchas veces por Live Server.

## Web que vamos a servir

En esta practica no vamos a crear una pagina desde cero. Vamos a usar la app **Simon Proa 2026**, que ya tiene una pagina web completa:

```text
simon-proa-2026/
```

Archivos principales:

| Archivo o carpeta | Funcion |
| --- | --- |
| `index.html` | Pagina principal que pide el navegador. |
| `styles.css` | Estilos visuales del juego. |
| `game.js` | Logica del juego. |
| `sounds/` | Sonidos que tambien se descargan por HTTP. |

La idea es que una computadora actue como **servidor** y entregue esos archivos. Otras tres computadoras actuaran como **clientes** y abriran el juego desde el navegador.

## Instalar Live Server

En la computadora que va a funcionar como servidor:

1. Abrir Visual Studio Code.
2. Ir al icono de **Extensions**.
3. Buscar:

```text
Live Server
```

4. Instalar la extension **Live Server** de Ritwick Dey.
5. Reiniciar VS Code si la extension no aparece disponible.

## Practica principal

Trabajar en grupos de 4 computadoras:

| Computadora | Rol |
| --- | --- |
| Computadora A | Servidor web |
| Computadora B | Cliente 1 |
| Computadora C | Cliente 2 |
| Computadora D | Cliente 3 |

Solo la **Computadora A** tiene que levantar Live Server. Las otras tres computadoras entran desde el navegador.

## Paso 1 - Preparar el repositorio de Simon Proa

En la **Computadora A**, verificar si ya esta descargado el repositorio de Simon Proa 2026.

### Si el repositorio ya esta descargado

1. Abrir Visual Studio Code.
2. Ir a **File > Open Folder**.
3. Abrir la carpeta:

```text
simon-proa-2026
```

4. Confirmar que adentro existan estos archivos:

```text
index.html
styles.css
game.js
```

### Si el repositorio no esta descargado

1. Abrir Visual Studio Code.
2. Abrir una terminal desde **Terminal > New Terminal**.
3. Elegir una carpeta de trabajo, por ejemplo `Documentos`.

```powershell
cd Documents
```

4. Clonar el repositorio de Simon Proa 2026:

```powershell
git clone https://github.com/lole-s/simon-proa-2026.git
```

5. Entrar a la carpeta:

```powershell
cd simon-proa-2026
```

6. Abrir el proyecto en VS Code:

```powershell
code .
```

Si el comando `git` no funciona, revisar si Git esta instalado o pedir ayuda antes de continuar.

## Paso 2 - Preparar el servidor

En la **Computadora A**:

1. Abrir en VS Code la carpeta `simon-proa-2026`.
2. Abrir el archivo:

```text
index.html
```

3. Hacer clic derecho sobre `index.html`.
4. Elegir **Open with Live Server**.
5. Verificar que el navegador abra Simon Proa.
6. Identificar el puerto que aparece en la URL. Normalmente sera:

```text
5500
```

Ejemplo de URL local:

```text
http://127.0.0.1:5500/index.html
```

Atencion: `127.0.0.1` o `localhost` sirven para abrir la pagina desde la misma computadora, pero los clientes necesitan la **IP real del servidor en la red local**.

## Paso 3 - Buscar la IP del servidor

En la **Computadora A**, abrir una terminal y ejecutar:

```powershell
ipconfig
```

Buscar la direccion **IPv4** de la placa que esta conectada a la red del aula.

Ejemplo:

```text
192.168.1.25
```

Anotar:

| Dato | Valor |
| --- | --- |
| IP del servidor | |
| Puerto de Live Server | |

## Paso 4 - Armar la URL para los clientes

Con la IP del servidor y el puerto de Live Server, armar la URL que van a usar los clientes.

Formato:

```text
http://IP_DEL_SERVIDOR:PUERTO/index.html
```

Ejemplo:

```text
http://192.168.1.25:5500/index.html
```

Tambien puede funcionar:

```text
http://192.168.1.25:5500
```

Usar la URL que efectivamente cargue el juego.

## Paso 5 - Conectar los tres clientes

En las **Computadoras B, C y D**:

1. Abrir el navegador.
2. Escribir la URL del servidor.
3. Verificar que cargue Simon Proa.
4. Probar el boton de inicio.
5. Probar que funcionen colores y sonidos.
6. Confirmar que la URL empiece con `http://` y use la IP de la Computadora A.

Cada cliente debe completar su resultado:

| Cliente | URL usada | Cargo Simon Proa? | Funcionaron colores? | Funcionaron sonidos? |
| --- | --- | --- | --- | --- |
| Cliente 1 | | | | |
| Cliente 2 | | | | |
| Cliente 3 | | | | |

## Verificacion del juego servido

En cada cliente, revisar:

- que cargue la pantalla de Simon Proa;
- que se vean los cuatro botones de colores;
- que el boton de inicio funcione;
- que al jugar cambie el nivel;
- que los sonidos funcionen;
- que la URL use la IP de la computadora servidor;
- que si la Computadora A cierra Live Server, los clientes dejan de poder cargar la pagina.

## Registro de la practica

| Dato | Valor |
| --- | --- |
| Nombre del grupo | |
| Computadora servidor | |
| IP de la computadora servidor | |
| Puerto usado por Live Server | |
| URL final usada por los clientes | |
| Cantidad de clientes conectados correctamente | |
| Problemas encontrados | |
| Como se resolvieron | |

## Entregable grupal

Entregar un documento grupal con capturas de pantalla que demuestren que una sola computadora funciono como servidor web y que tres computadoras distintas accedieron como clientes usando la IP y el puerto del servidor.

El documento debe incluir:

- captura de la Computadora A con Live Server funcionando;
- captura de `ipconfig` en la Computadora A, donde se vea la IPv4 usada;
- captura de `netstat -n | findstr :5500` en la Computadora A, donde se vean las IP's de los Clientes.
    nota: Si Live Server usa otro puerto, reemplazar `5500` por el puerto correspondiente. Este comando permite observar conexiones de red relacionadas con ese puerto.

## Si no funciona

Revisar:

- que las cuatro computadoras esten en la misma red;
- que la IP del servidor sea correcta;
- que el puerto sea correcto;
- que Live Server siga prendido en la Computadora A;
- que el navegador del servidor pueda abrir Simon Proa;
- que el firewall no bloquee la conexion entrante;
- que cada cliente pueda hacer `ping` al servidor.

Para probar conectividad desde un cliente:

```powershell
ping IP_DEL_SERVIDOR
```

Ejemplo:

```powershell
ping 192.168.1.25
```

## Cierre

Completar:

> En esta practica, la computadora servidor fue... y las computadoras cliente fueron...

Luego responder:

1. Que dato usamos para encontrar al servidor?
2. Para que sirvio el puerto?
3. Que protocolo de aplicacion usamos?
4. Que diferencia hay entre abrir `localhost` y abrir la IP del servidor desde otra computadora?
5. Cuando el cliente abrio Simon Proa, que archivos tuvo que entregar el servidor ademas de `index.html`?
6. Que tienen en comun Live Server, Apache e IIS?
7. Por que en esta practica usamos `http://` y no `https://`?
8. Donde aparece esta practica en el mapa final del recorrido de la informacion?
