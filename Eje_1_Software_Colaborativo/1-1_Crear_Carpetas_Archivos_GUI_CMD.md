# 1-1 Crear carpetas y archivos (GUI + CMD + PowerShell)

## Objetivo
Organizar las carpetas del curso y practicar comandos básicos de Windows.

## Teoría breve
- La terminal permite trabajar con archivos y carpetas mediante comandos.
- En Windows hay dos opciones comunes: **CMD** y **PowerShell**.
- CMD es más simple; PowerShell es más potente y usa cmdlets.
- Siempre hay un **directorio actual** (la carpeta en la que estás parado).

## Video recomendado
- Qué es una terminal: https://youtu.be/gN_0sWWV3CA
- Comandos básicos CMD: http://youtube.com/watch?v=W6434nulBu8

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

## Entrega
- Captura de pantalla del árbol de carpetas.
- Enlace compartido de la carpeta en Drive.