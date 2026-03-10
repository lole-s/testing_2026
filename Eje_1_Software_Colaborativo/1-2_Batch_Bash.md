# 1-2 Batch y Bash

## Objetivo
Conocer qué es un script Batch en Windows y qué es Bash en sistemas Unix. Crear y ejecutar scripts simples.

## Teoría breve
- **Batch**: archivos `.bat` o `.cmd` que ejecutan comandos en CMD.
- **Bash**: shell de sistemas Unix (Linux/macOS) que ejecuta scripts `.sh`.
- Batch es propio de Windows; Bash es común en Linux y Git Bash.

## Videos recomendados
- Ejemplo Batch: https://www.youtube.com/watch?v=uTQD5hAKURg
- Programación Bash: https://www.youtube.com/watch?v=0tIZhTAuNuU

## Actividad paso a paso

### Parte A: Scripts Batch (CMD)
1. Crear carpeta `C:\temp2026\scripts`.
2. Crear `hola.bat` con este contenido:
```bat
@echo off
echo Hola, Testing 2026
pause
```
3. Ejecutar el script desde CMD:
```bat
cd C:\temp2026\scripts
hola.bat
```
4. Crear `fecha.bat` para mostrar fecha y hora:
```bat
@echo off
echo Fecha: %date%
echo Hora: %time%
pause
```

### Parte B: Scripts Bash (solo si tenés Git Bash o WSL)
1. Crear `hola.sh` con este contenido:
```bash
#!/usr/bin/env bash
echo "Hola desde Bash"
```
2. Ejecutar:
```bash
cd /c/temp2026/scripts
bash hola.sh
```

## Entrega
- Captura de pantalla ejecutando `hola.bat` y `fecha.bat`.
- Si hiciste Bash, captura de `hola.sh`.