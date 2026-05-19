# 1-8 Git desde Visual Studio Code

## Clase: Git local y clonado desde VS Code

## Objetivo
Usar **Git desde Visual Studio Code** para crear commits, clonar un repositorio existente y reconocer las acciones `pull` y `push`.

En esta clase el foco esta en VS Code y Git local. El trabajo colaborativo completo queda para:

- [1-9 Crear cuenta de GitHub y primer cambio desde el navegador](1-9_Crear_cuenta_GitHub_y_primer_push.md)
- [1-10 Repositorio colaborativo desde Visual Studio Code](1-10_Repositorio_colaborativo_desde_VSCode.md)

---

## Requisitos

- Tener instalado **Git**.
- Tener instalado **Visual Studio Code**.
- Haber configurado nombre y correo en Git.

Verificar:

```bash
git config --global --list
```

Si falta algun dato:

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
```

---

## Conceptos clave

```text
commit = guardar una version local
clone = copiar un repositorio existente
remote = repositorio remoto
origin = remoto principal
pull = traer cambios del remoto
push = subir commits al remoto
```

En VS Code, el boton **Sync** puede hacer:

```text
pull + push
```

Por eso conviene mirar siempre el estado antes de sincronizar.

---

## Parte 1: crear un repositorio local desde VS Code

Crear una carpeta de practica:

```bash
cd /c/temp2026/Testing2026_APELLIDO/Eje_1_Software_Colaborativo
mkdir proyecto_git_vscode
cd proyecto_git_vscode
code .
```

En VS Code:

1. Abrir **Control de codigo fuente**.
2. Elegir **Inicializar repositorio**.
3. Verificar en la terminal:

```bash
git status
```

Responder:

```text
¿VS Code inicializo un repositorio Git?
¿Como lo comprobaste?
```

---

## Parte 2: hacer commits desde VS Code

Crear `README.md`:

```markdown
# Proyecto Git desde VS Code

Este repositorio fue creado para practicar Git usando Visual Studio Code.
```

Desde **Control de codigo fuente**:

1. Revisar el archivo modificado.
2. Preparar el cambio con `+`.
3. Escribir el mensaje:

```text
Agrego README inicial
```

4. Hacer commit.

Crear una carpeta `scripts` y un archivo `saludo.py`:

```python
print("Hola desde VS Code y Git")
```

Hacer un segundo commit:

```text
Agrego script de saludo
```

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

## Parte 3: clonar un repositorio existente

Clonar significa traer una copia completa de un repositorio.

Repositorio de practica:

```text
https://github.com/lole-s/game-hub.git
```

Desde VS Code:

1. Abrir `Ctrl + Shift + P`.
2. Buscar `Git: Clone`.
3. Pegar la URL.
4. Elegir una carpeta de trabajo.
5. Abrir el proyecto clonado.

Desde terminal:

```bash
cd /c/temp2026/Testing2026_APELLIDO/Eje_1_Software_Colaborativo
git clone https://github.com/lole-s/game-hub.git
cd game-hub
code .
```

Verificar historial:

```bash
git log --oneline
```

Responder:

```text
¿Que archivos trajo el repositorio clonado?
¿El repositorio clonado ya tenia historial?
```

---

## Parte 4: modificar y commitear en el repo clonado

Abrir:

```text
nombres.md
```

Agregar nombre y apellido en una linea nueva.

Importante:

```text
En esta clase no hacemos push al repositorio del docente.
Solo practicamos modificar, revisar y commitear localmente.
```

Hacer commit con el mensaje:

```text
Agrego mi nombre en nombres.md
```

Verificar:

```bash
git status
git log --oneline
git branch
```

---

## Parte 5: practicar pull

`pull` trae cambios desde el remoto.

```bash
git pull
```

Si Git responde:

```text
Already up to date.
```

significa:

```text
Mi copia local ya estaba actualizada.
```

Responder:

```text
¿Aparecieron cambios nuevos?
¿Que mensaje mostro Git?
```

---

## Parte 6: anticipo de push

`push` sube commits locales al remoto.

En esta clase solo lo reconocemos. La practica completa de `push`, `pull`, ramas y Pull Request queda para la clase 1-10.

```bash
git push
```

Responder:

```text
¿Que necesita Git para poder hacer push?
¿Por que puede fallar un push?
¿Que diferencia hay entre commit y push?
```

---

## Entrega

Subir:

- captura del repositorio creado desde VS Code con al menos dos commits
- captura del repositorio clonado abierto en VS Code
- captura o texto de `git log --oneline`
- respuesta breve:

```text
¿Que diferencia hay entre crear un repositorio y clonar un repositorio?
¿Que hace commit?
¿Que hace pull?
¿Que hace push?
```

---

## Resumen

```text
Git guarda versiones.
VS Code permite usar Git de forma visual.
Clone trae un repositorio.
Pull baja cambios.
Push sube commits.
```
