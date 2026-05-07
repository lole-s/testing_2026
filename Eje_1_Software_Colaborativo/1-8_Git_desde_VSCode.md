# 1-8 Git desde Visual Studio Code

## Clase: crear, clonar y sincronizar repositorios desde VS Code

## Objetivo
Aprender a usar **Git desde Visual Studio Code**, usando la interfaz grafica de control de codigo fuente y la terminal integrada.

Esta actividad continua lo trabajado en:

- [1-7 Git local](1-7_Git_Local.md)
- [1-7b Git local: practica complementaria](1-7b_Git_practica_complementaria.md)

La idea principal es reconocer que VS Code no reemplaza a Git: lo muestra de una forma mas visual.

```text
Git sigue guardando versiones.
VS Code nos ayuda a ver, preparar, commitear, clonar, subir y bajar cambios.
```

---

Primero vamos a trabajar con un repositorio propio creado desde VS Code. Despues vamos a clonar un repositorio ya existente y practicar el flujo de trabajo.

---

## Requisitos previos

- Tener instalado **Git**.
- Tener instalado **Visual Studio Code**.
- Haber configurado Git con nombre y correo.

Para revisar la configuracion:

```bash
git config --global --list
```

Si falta nombre o correo:

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
```

---

## Conceptos nuevos

### Clonar
Clonar significa copiar un repositorio que ya existe.

```text
git clone = traer una copia completa del proyecto y su historial
```

### Repositorio remoto
Un repositorio remoto es otra copia del proyecto.

Puede estar:

- en GitHub
- en un servidor
- en otra carpeta local preparada para practicar

### Origin
`origin` es el nombre que normalmente se usa para identificar al remoto principal.

```text
origin = remoto principal del proyecto
```

### Push
`push` significa subir commits desde mi copia local hacia el remoto.

```text
mi computadora -> remoto
```

### Pull
`pull` significa traer cambios desde el remoto hacia mi copia local.

```text
remoto -> mi computadora
```

### Sync
En VS Code, el boton de sincronizar puede combinar dos acciones:

```text
pull + push
```

Por eso conviene mirar siempre el estado antes de sincronizar.

---

## Parte 1: crear un repositorio propio desde VS Code

### Paso 1: crear carpeta de trabajo

En Git Bash o en la terminal integrada de VS Code:

```bash
cd /c/temp2026/Testing2026_APELLIDO/Eje_1_Software_Colaborativo
mkdir proyecto_git_vscode
cd proyecto_git_vscode
code .
```

Cambiar `APELLIDO` por el apellido correspondiente.

Si `code .` no funciona, abrir VS Code manualmente y elegir:

```text
Archivo -> Abrir carpeta
```

### Paso 2: iniciar Git desde VS Code

En la barra lateral izquierda, hacer clic en el icono de **Control de codigo fuente**.

Si la carpeta todavia no es un repositorio, VS Code mostrara una opcion parecida a:

```text
Inicializar repositorio
```

Hacer clic ahi.

Verificar desde la terminal:

```bash
git status
```

Responder:

```text
¿VS Code inicializo un repositorio Git?
¿Como lo comprobaste?
```

---

## Parte 2: primer commit desde VS Code

### Paso 1: crear `README.md`

Crear un archivo llamado:

```text
README.md
```

Contenido sugerido:

```markdown
# Proyecto Git desde VS Code

Este repositorio fue creado para practicar Git usando Visual Studio Code.
```

Guardar el archivo.

### Paso 2: observar los cambios

Volver al panel de **Control de codigo fuente**.

Responder:

```text
¿Aparece el archivo README.md?
¿Que letra o simbolo muestra VS Code al lado del archivo?
```

### Paso 3: preparar el cambio

Hacer clic en el simbolo `+` al lado del archivo.

Ese paso equivale a:

```bash
git add README.md
```

### Paso 4: hacer commit

Escribir un mensaje:

```text
Agrego README inicial
```

Hacer clic en el tilde de commit.

Verificar en la terminal:

```bash
git log --oneline
```

---

## Parte 3: hacer un segundo commit

Crear una carpeta:

```text
scripts
```

Dentro, crear:

```text
saludo.py
```

Contenido:

```python
print("Hola desde VS Code y Git")
```

Desde el panel de control de codigo fuente:

1. Revisar los archivos modificados.
2. Preparar los cambios con `+`.
3. Escribir el mensaje:

```text
Agrego script de saludo
```

4. Hacer commit.

Verificar:

```bash
git log --oneline
git status
```

Responder:

```text
¿Cuantos commits tiene tu repositorio?
¿El panel de VS Code quedo sin cambios pendientes?
```

---

## Parte 4: clonar un repositorio existente

Ahora vamos a trabajar al reves: en lugar de crear un repo desde cero, vamos a traer uno que ya existe.

Para esta primera practica conviene usar un repositorio preparado por la docente, sin tocar todavia el proyecto grupal.

En materiales anteriores se usaba un repositorio de un tercero. Para esta version vamos a usar el fork creado en la cuenta de la docente:

```text
https://github.com/lole-s/game-hub
```

Eso permite practicar con una copia controlada para la clase.

La idea es que este sea un **repositorio puente**:

```text
primero aprendo a clonar y mirar un proyecto existente
despues paso a un proyecto grupal como Simon Proa
```

URL sugerida para clonar:

```text
https://github.com/lole-s/game-hub.git
```

### Clonar desde VS Code

1. Abrir la paleta de comandos:

```text
Ctrl + Shift + P
```

2. Escribir:

```text
Git: Clone
```

3. Pegar la URL del repositorio.
4. Elegir una carpeta de trabajo.
5. Abrir el proyecto clonado cuando VS Code lo pregunte.

### Clonar desde terminal

Otra forma:

```bash
cd /c/temp2026/Testing2026_APELLIDO/Eje_1_Software_Colaborativo
git clone https://github.com/lole-s/game-hub.git
```

Entrar a la carpeta clonada:

```bash
cd game-hub
code .
```

Responder:

```text
¿Que archivos trajo el repositorio clonado?
¿El repositorio clonado ya tenia historial?
```

Para ver el historial:

```bash
git log --oneline
```

---

## Parte 5: modificar el repositorio clonado

Hacer un cambio pequeño y concreto en el repositorio clonado.

Consigna:

1. Abrir el archivo:

```text
nombres.md
```

2. Agregar el nombre y apellido en una linea nueva.
3. Guardar el archivo.

Importante:

```text
Si el repositorio es de la docente y no tenemos permisos de escritura, no vamos a hacer push.
Solo practicamos clonar, leer historial, modificar localmente y commitear.
```

Ejemplo de contenido agregado:

```text
Nombre Apellido
```

Luego, desde VS Code:

1. Revisar los cambios.
2. Preparar los cambios.
3. Hacer commit con un mensaje claro.

Mensaje sugerido:

```text
Agrego mi nombre en nombres.md
```

Verificar:

```bash
git log --oneline
git status
git branch
```

---

## Parte 6: practicar pull

`pull` sirve para traer cambios nuevos desde el remoto.

Si el repositorio remoto fue actualizado por la docente o por otra persona, usar:

```bash
git pull
```

Desde VS Code tambien se puede usar:

```text
Pull
```

Responder:

```text
¿Aparecieron cambios nuevos?
¿Que mensaje mostro Git?
```

Si no habia cambios nuevos, Git puede mostrar algo parecido a:

```text
Already up to date.
```

Eso significa:

```text
Mi copia local ya estaba actualizada.
```

---

## Parte 7: anticipo de push

`push` sirve para enviar commits locales al remoto.

En esta clase alcanza con entender la idea. La practica completa queda para:

- [1-9 Crear cuenta de GitHub y practicar push](1-9_Crear_cuenta_GitHub_y_primer_push.md)

Si ya se preparo un repositorio donde el curso tiene permiso para escribir, el comando seria:

```bash
git push
```

o desde VS Code:

```text
Push
```

Responder:

```text
¿Que necesita Git para poder hacer push?
¿Por que puede fallar un push?
¿Que diferencia hay entre commit y push?
```

---

## Parte 8: mirar el historial visual

En VS Code se puede ver el historial de distintas formas:

- desde la terminal con `git log --oneline`
- desde extensiones como **Git Graph**
- desde la vista de control de codigo fuente

Instalacion opcional:

```text
Extension: Git Graph
```

Luego abrir el grafico y responder:

```text
¿Cuantos commits tiene el repositorio?
¿Cual fue el commit que hiciste vos?
¿Hay commits anteriores de otras personas?
```

---

## Entrega

Subir a la carpeta del Drive (eje1):

- captura del repositorio creado desde VS Code con al menos dos commits
- captura del repositorio clonado abierto en VS Code
- captura de `git log --oneline`
- respuesta breve:

```text
¿Que diferencia hay entre crear un repositorio y clonar un repositorio?
¿Que hace commit?
¿Que hace pull?
¿Que hace push?
¿Por que VS Code muestra archivos modificados antes del commit?
```

---

## Resumen

Git guarda la historia del proyecto.

VS Code permite trabajar con esa historia desde una interfaz mas visual.

Clonar sirve para empezar desde un proyecto existente.

`pull` trae cambios. `push` envia cambios.
