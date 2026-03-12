# 1-1 Crear carpetas y archivos (GUI + CMD + PowerShell)

## Objetivo
Organizar las carpetas del curso y practicar comandos básicos de Windows.

## Teoría breve
- La terminal permite trabajar con archivos y carpetas mediante comandos.
- En Windows hay dos opciones comunes: **CMD** y **PowerShell**.
- CMD es más simple; PowerShell es más potente y usa cmdlets.
- Siempre hay un **directorio actual** (la carpeta en la que estás parado).
- El **CMD** (Símbolo del sistema) viene con Windows y permite ejecutar comandos para tareas avanzadas.

## Comandos básicos (CMD y Linux)
| Propósito | WINDOWS | LINUX | Ejemplo básico de Linux |
|----|----|----|----|
| Ayuda sobre comandos | cmd /? | man cmd | man comando |
| Crear un directorio | mkdir | mkdir | mkdir /home/qdirectorio |
| Cambiar a un directorio | cd | cd | cd /home/qdirectorio |
| Subir un directorio | cd .. | cd .. | |
| Listar directorio | dir | ls -ls | |
| Borrar pantalla | cls | clear | |
| Cerrar ventana | exit | exit | |
| Borrar un directorio | rmdir | rmdir | rmdir /home/qdirectorio |
| Mostrar un archivo | more | more | more qfichero |
| Renombrar archivo | rename | mv | mv nombreold nombrenew |
| Copiar archivos | copy | cp | cp qfichero.txt /home/qdirectorio |
| Mover archivos | move | mv | mv qfichero.txt /home/qdirectorio |
| Mostrar fecha | date | date | |
| Mostrar hora | time | date | |
| Borrar archivos | del | rm | rm qfichero.txt |
| Buscar texto en archivo | find | grep | grep "contenido" qfichero.txt |
| Crear un archivo | copy con | touch | touch newfichero.txt |
| Ver salida estándar | echo | echo | echo Testing_QA |

## Video recomendado
- Qué es una terminal: https://youtu.be/gN_0sWWV3CA
- Comandos básicos CMD: http://youtube.com/watch?v=W6434nulBu8
- Lectura recomendada: https://www.xataka.com/basics/comandos-basicos-para-dar-tus-primeros-pasos-consola-windows-cmd

## Actividad paso a paso

### Parte A: GUI (Explorador de archivos)
1. Crear carpeta local: `C:\temp2026\Testing_APELLIDO`.
2. Dentro, crear estas subcarpetas:
   - `Eje_1_Software_Colaborativo`
   - `Eje_2_Redes_de_Datos`
   - `Eje_3_Testing`
3. Crear un archivo de texto `README.txt` dentro de cada eje.
4. Subir la carpeta `Testing_APELLIDO` a Google Drive institucional.
5. Compartir el enlace con `jcsodo@escuelasproa.edu.ar`.

### Parte B: Línea de comandos (CMD)
Comandos a usar: `cd`, `mkdir`, `dir`, `tree`, `copy con`, `type`, `notepad`.

```bat
cd C:\
mkdir temp2026
cd temp2026
mkdir Testing_APELLIDO
cd Testing_APELLIDO
mkdir Eje_1_Software_Colaborativo
mkdir Eje_2_Redes_de_Datos
mkdir Eje_3_Testing
cd Eje_1_Software_Colaborativo
copy con README.txt
(Escribir una línea y presionar Ctrl+Z, luego Enter)
cd ..
cd Eje_2_Redes_de_Datos
copy con README.txt
(Ctrl+Z y Enter)
cd ..
cd Eje_3_Testing
copy con README.txt
(Ctrl+Z y Enter)
cd ..
dir
tree C:\temp2026\Testing_APELLIDO /F
```

### Parte C: Línea de comandos (PowerShell)
```powershell
cd C:\
mkdir temp2026
cd temp2026
mkdir Testing_APELLIDO
cd Testing_APELLIDO
mkdir Eje_1_Software_Colaborativo
mkdir Eje_2_Redes_de_Datos
mkdir Eje_3_Testing
"Eje 1" | Set-Content .\Eje_1_Software_Colaborativo\README.txt
"Eje 2" | Set-Content .\Eje_2_Redes_de_Datos\README.txt
"Eje 3" | Set-Content .\Eje_3_Testing\README.txt
Get-ChildItem
```

## Diferencias clave CMD vs PowerShell
- PowerShell trabaja con objetos y cmdlets (por ejemplo `Get-ChildItem`).
- CMD usa comandos tradicionales (`dir`, `copy`, `type`).
- PowerShell acepta alias como `dir` o `ls`, pero su salida es más rica.

## Extensión opcional
1. Editar cada `README.txt` con `notepad` y agregar una breve descripción del eje.
2. Usar `type` para verificar el contenido de cada archivo.

## Entrega
- Captura de pantalla del árbol de carpetas.
- Enlace compartido de la carpeta en Drive.
