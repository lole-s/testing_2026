# 1-7 Git local

## Objetivo
Instalar Git, comprobar que funciona y crear un primer repositorio local para entender cómo guarda versiones.

## Idea clave
**Git** es una herramienta que guarda el historial de cambios de una carpeta de proyecto.

No trabaja sobre ideas abstractas: trabaja sobre archivos reales.

## Diferencia importante

- **Git**: herramienta local de control de versiones
- **GitHub**: plataforma online que usa Git para compartir repositorios

En esta clase vamos a trabajar solo con **Git local**.

## Material de apoyo
- [Git explicado en forma simple](https://www.youtube.com/watch?v=3GymExBkKjE)
- [Curso de Git y GitHub desde cero - introducción](https://www.youtube.com/watch?v=HiXLkL42tMU)
- [Curso de Git - playlist de Felipe Gavilan Programa](https://www.youtube.com/playlist?list=PL0kIvpOlieSO0s8RI-1YJPMztAJ7TsUco)

Cómo usar los videos en esta clase:

- si el video explica conceptos, usarlo como apoyo teórico antes de practicar
- si el video muestra comandos, pausarlo y repetir los pasos en la propia computadora
- si aparece un comando que todavía no vimos, anotarlo y volver a esta guía

## Sitio oficial
- [Git SCM](https://git-scm.com/)
- [Libro oficial de Git en español](https://git-scm.com/book/es/v2)

## Instalación en Windows

Antes de instalar, se puede mirar un video corto de la playlist para reconocer la herramienta y la pantalla de instalación. La instalación se hace siguiendo esta guía paso a paso.

1. Ir a [https://git-scm.com/downloads](https://git-scm.com/downloads)
2. Descargar la versión para Windows.
3. Ejecutar el instalador.
4. Dejar, en general, las opciones marcadas por defecto.

## Cómo acceder a Git
Después de instalarlo, Git puede usarse de varias formas:

- desde **Git Bash**
- desde **PowerShell**
- desde la terminal integrada de **VS Code**

Para este eje conviene seguir usando **PowerShell** o la terminal de **VS Code**, así hay continuidad con las clases anteriores.

## Verificar la instalación
Abrí una terminal y ejecutá:

```powershell
git --version
git --help
```

Si Git está bien instalado, el primer comando debería mostrar una versión.

## Comandos base que vamos a usar hoy

| Acción | Comando |
|---|---|
| Iniciar repo | `git init` |
| Ver estado | `git status` |
| Agregar archivo | `git add archivo` |
| Agregar todo | `git add .` |
| Guardar versión | `git commit -m "mensaje"` |
| Ver historial corto | `git log --oneline` |

## Configuración inicial recomendada
Antes del primer commit, conviene configurar nombre y correo.

```powershell
git config --global user.name "Tu Nombre"
git config --global user.email "tunombre@ejemplo.com"
```

Para revisar la configuración:

```powershell
git config --global --list
```

## Cómo trabajar con la guía y los videos

Esta clase tiene dos tipos de momentos:

- **momento teórico**: mirar una explicación corta para entender qué problema resuelve cada comando
- **momento práctico**: ejecutar los comandos, observar la salida y registrar evidencias

Cuando el video muestre una acción práctica, no alcanza con verlo: hay que repetirla en terminal.

La guía escrita manda sobre la actividad: si el video usa otra carpeta, otro nombre de archivo u otro sistema operativo, seguir los nombres y rutas de esta clase.

## Actividad 1: crear un proyecto local

### Paso 1: crear carpeta

```powershell
cd C:\temp2026\Testing2026_APELLIDO\Eje_1_Software_Colaborativo
mkdir mi_primer_repo_git
cd .\mi_primer_repo_git
```

### Paso 2: inicializar Git

```powershell
git init
```

### Qué pasó
Git creó una carpeta oculta llamada `.git` dentro del proyecto.

Esa carpeta guarda el historial del repositorio.

## Actividad 2: crear un archivo y mirar el estado

### Paso 1: crear `README.md`

```powershell
echo "# Mi primer repositorio Git" > README.md
```

### Paso 2: revisar el estado

```powershell
git status
```

### Qué observar

- Git detecta que existe un archivo nuevo
- todavía no forma parte del historial

## Actividad 3: agregar y hacer el primer commit

### Paso 1: pasar el archivo al área de preparación

```powershell
git add README.md
```

### Paso 2: guardar una versión

```powershell
git commit -m "Agrego README inicial"
```

### Paso 3: ver el historial

```powershell
git log --oneline
```

## Idea importante: las tres zonas de Git
Para empezar, alcanza con esta imagen mental:

- **Working directory**: los archivos que estás editando
- **Staging area**: lo que marcaste para guardar
- **Repository**: el historial ya guardado con commits

En forma simple:

> escribo, selecciono, guardo versión.

## Actividad 4: modificar el proyecto

Agregar una segunda línea al `README.md`.

Podés hacerlo desde VS Code o con este comando:

```powershell
Add-Content README.md "Este repositorio se creó para practicar Git local."
```

Ahora, ejecutar:

```powershell
git status
git add README.md
git commit -m "Actualizo el README con una descripción"
git log --oneline
```

## Actividad 5: crear un archivo de código

Crear un archivo `saludo.py` con este contenido:

```python
print("Hola, Git")
```

Si querés crearlo desde terminal:

```powershell
echo 'print("Hola, Git")' > saludo.py
```

Luego, ejecutar:

```powershell
git status
git add .
git commit -m "Agrego script saludo.py"
git log --oneline
```

## Actividad 6: leer el estado del repositorio
Responder con tus palabras:

1. ¿Qué hace `git init`?
2. ¿Qué muestra `git status`?
3. ¿Para qué sirve `git add`?
4. ¿Qué guarda un `commit`?
5. ¿Qué diferencia hay entre editar un archivo y hacer commit?

## Mini ejercicio guiado
Repetí esta secuencia:

```powershell
git status
Add-Content README.md "Nueva línea de prueba"
git status
git add README.md
git status
git commit -m "Agrego una nueva línea de prueba"
git log --oneline
```

La idea es mirar cómo cambia el estado en cada paso.

## Problemas comunes

### Git no reconoce tu identidad
Si aparece un mensaje pidiendo nombre o correo, configurá:

```powershell
git config --global user.name "Tu Nombre"
git config --global user.email "tunombre@ejemplo.com"
```

### `git` no se reconoce como comando
Puede pasar si:

- Git no se instaló bien
- la terminal quedó abierta antes de instalar

Solución:

- cerrar y abrir la terminal
- volver a probar `git --version`

### Hice cambios pero no los veo en el historial
Probablemente faltó alguno de estos pasos:

- `git add`
- `git commit -m "mensaje"`

## Cierre conceptual
Git no guarda solo archivos: guarda momentos del proyecto.

Cada commit funciona como una foto con mensaje.

## Entrega sugerida

- captura de `git status`
- captura de `git log --oneline`
- carpeta del proyecto con `README.md` y `saludo.py`

## Próximo paso
Después de dominar Git local, el paso siguiente es entender:

- qué es un repositorio remoto
- para qué sirve GitHub
- cómo subir y bajar cambios
