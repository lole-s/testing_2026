# 1-2 Automatización inicial: Batch y Bash

## Objetivo
Entender qué es un script y usarlo para automatizar tareas repetitivas de organización de archivos y carpetas.

## Idea clave
Si una secuencia de comandos se repite muchas veces, conviene guardarla en un archivo para poder ejecutarla cuando haga falta.

## Qué vas a usar
- **Batch** (`.bat`) en Windows
- **Bash** (`.sh`) como referencia para Linux o Git Bash

## Actividad 1: Crear la carpeta de scripts
Abrí PowerShell y ubicáte en tu carpeta de trabajo:

```powershell
cd $HOME\Testing2026_APELLIDO
mkdir scripts
cd scripts
pwd
```

## Actividad 2: Crear un script Batch
Creá un archivo llamado `preparar_entorno.bat` con este contenido:

```bat
@echo off
mkdir proyecto_demo
cd proyecto_demo
mkdir docs
mkdir src
mkdir tests
echo # Proyecto demo > README.md
echo Entorno inicial creado
dir
pause
```

## Actividad 3: Ejecutar el script
Ejecutá el archivo desde PowerShell:

```powershell
.\preparar_entorno.bat
```

## Actividad 4: Verificar el resultado
Entrá en la carpeta creada y comprobá su contenido:

```powershell
cd .\proyecto_demo
ls
cat .\README.md
```

La estructura final debería quedar así:

```text
proyecto_demo
|-- docs
|-- src
|-- tests
|-- README.md
```

## Actividad 5: Leer el equivalente en Bash
Leé este script y comparalo con el anterior:

```bash
#!/usr/bin/env bash
mkdir proyecto_demo
cd proyecto_demo
mkdir docs
mkdir src
mkdir tests
echo "# Proyecto demo" > README.md
echo "Entorno inicial creado"
ls
```

## Comparación rápida

| Idea | Batch (`.bat`) | Bash (`.sh`) |
|---|---|---|
| Crear carpetas | `mkdir` | `mkdir` |
| Cambiar de carpeta | `cd` | `cd` |
| Crear README | `echo texto > archivo` | `echo "texto" > archivo` |
| Ver contenido | `dir` | `ls` |

## Entrega
- Captura ejecutando `preparar_entorno.bat`.
- Captura o evidencia de la carpeta `proyecto_demo`.
- Explicación breve: ¿qué ventaja tiene guardar varios comandos en un script?


### Videos
- **Descubre Qué es la SHELL de LINUX y BASH (Terminal) en 5 Minutos!!**: https://www.youtube.com/watch?v=YUCXzp8n93U
- **¿Qué es Bash y para que sirven los Bash Scripts?**: https://www.youtube.com/watch?v=0tIZhTAuNuU
- **Bash: Explicado Fácilmente en 3 minutos**: https://www.youtube.com/watch?v=EKFK83mNsyo

#### Extra: 
**Learn Shell**: https://www.learnshell.org/