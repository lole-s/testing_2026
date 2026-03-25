# 1-2 Automatización inicial: Batch y Bash

## Objetivo
Entender qué es un script y usarlo para automatizar tareas repetitivas de organización de archivos y carpetas.

## Idea clave
Si una secuencia de comandos se repite muchas veces, conviene guardarla en un archivo para poder ejecutarla cuando haga falta.

## Definiciones y Diferencias
- **Batch**: Lenguaje de scripting nativo de Windows, usado en el Símbolo del Sistema (CMD). Archivos con extensión `.bat` o `.cmd`. Ideal para automatización simple en entornos Windows, con comandos básicos como `dir`, `mkdir`, `shutdown`.
- **Bash**: Shell y lenguaje de scripting avanzado para sistemas Unix/Linux (y disponible en Windows via Git Bash o WSL). Archivos con extensión `.sh`. Más potente que Batch: soporta variables avanzadas, bucles, funciones, expresiones regulares y mayor compatibilidad con herramientas del sistema.

**Diferencias clave**: Batch es limitado a Windows y sintaxis simple; Bash ofrece mayor flexibilidad, control de flujo y potencia para tareas complejas.

## Qué vas a usar
- **Batch** (`.bat`) en Windows CMD o PowerShell.
- **Bash** (`.sh`) en Git Bash, WSL o Linux.

## Actividad 1: Crear la carpeta de scripts
Abrí PowerShell y ubicáte en tu carpeta de trabajo:

```powershell
cd C:\temp2026\Testing2026_APELLIDO
cd Eje_1_Software_Colaborativo
mkdir scripts
cd scripts
pwd
```

## Mini Proyecto 1: Programar apagado de computadora
Crea scripts para automatizar el apagado del sistema a una hora específica, mostrando la potencia del scripting para tareas de administración.

### Versión Batch (Windows)
Creá un archivo llamado `apagar_pc.bat` con este contenido:

```bat
@echo off
echo Programando apagado en 1 hora (3600 segundos)...
shutdown /s /t 3600
echo Apagado programado. Presiona Ctrl+C para cancelar.
pause
```

Ejecutá desde CMD o PowerShell: `.\apagar_pc.bat`

### Versión Bash (Linux/WSL)
Creá un archivo llamado `apagar_pc.sh` con este contenido:

```bash
#!/bin/bash
echo "Programando apagado en 1 hora..."
shutdown -h +60
echo "Apagado programado. Usa 'shutdown -c' para cancelar."
```

Hazlo ejecutable: `chmod +x apagar_pc.sh`

Ejecutá: `./apagar_pc.sh`

**Potencia mostrada**: Automatización de tareas del sistema sin intervención manual, útil para mantenimiento o ahorro de energía.

## Mini Proyecto 2: Crear estructura de proyecto y contar archivos
Crea scripts para automatizar la creación de una estructura de carpetas y contar archivos, basado en ideas de organización de archivos.

### Versión Batch (Windows)
Creá un archivo llamado `setup_proyecto.bat` con este contenido:

```bat
@echo off
mkdir proyecto_nuevo
cd proyecto_nuevo
mkdir docs src tests
echo # Nuevo Proyecto > README.md
echo Estructura creada.
dir /b
echo Total de archivos/carpetas: 
dir /b | find /c /v ""
pause
```

Ejecutá: `.\setup_proyecto.bat`

### Versión Bash (Linux/WSL)
Creá un archivo llamado `setup_proyecto.sh` con este contenido:

```bash
#!/bin/bash
mkdir proyecto_nuevo
cd proyecto_nuevo
mkdir docs src tests
echo "# Nuevo Proyecto" > README.md
echo "Estructura creada."
ls
echo "Total de archivos/carpetas: $(ls | wc -l)"
```

Hazlo ejecutable: `chmod +x setup_proyecto.sh`

Ejecutá: `./setup_proyecto.sh`

**Potencia mostrada**: Creación automática de entornos de desarrollo y conteo de elementos, escalable para proyectos grandes.

## Entrega
- Capturas ejecutando ambos scripts de cada mini proyecto.
- Explicación breve: ¿Cómo muestran estos scripts la potencia del scripting? Compara una diferencia clave entre Batch y Bash.

### Videos
- **Descubre Qué es la SHELL de LINUX y BASH (Terminal) en 5 Minutos!!**: https://www.youtube.com/watch?v=YUCXzp8n93U
- **¿Qué es Bash y para que sirven los Bash Scripts?**: https://www.youtube.com/watch?v=0tIZhTAuNuU
- **Bash: Explicado Fácilmente en 3 minutos**: https://www.youtube.com/watch?v=EKFK83mNsyo

#### Extra: 
**Learn Shell**: https://www.learnshell.org/