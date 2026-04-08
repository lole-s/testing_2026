# 1-2 Automatización inicial con Batch y Bash

## Objetivo
Entender qué es un script y usarlo para automatizar tareas simples, divertidas y útiles desde la terminal.

## Idea clave
Si una secuencia de pasos se repite, no hace falta hacerla siempre a mano: se puede guardar en un archivo y ejecutarla cuando haga falta.

## Qué vamos a usar en esta clase
En estas notebooks conviene trabajar principalmente con **Batch** (`.bat`) porque:

- funciona en **Windows** sin instalar nada extra
- se puede ejecutar directamente desde **PowerShell**
- permite entender rápido la idea de **automatización**

También vamos a hablar de **Bash** (`.sh`) porque aparece mucho en Linux, Git Bash y tutoriales de internet, pero en esta clase lo vamos a tomar como comparación, no como herramienta principal.

## Introducción teórica

### ¿Qué es un script?
Un **script** es un archivo de texto con una lista de instrucciones que la computadora ejecuta en orden.

En palabras más simples:

- vos escribís pasos
- la computadora los lee
- y los hace uno detrás de otro

En vez de hacer esto:

1. abrir una carpeta
2. crear un archivo
3. escribir un mensaje
4. repetir lo mismo varias veces

podemos guardar esos pasos en un archivo y ejecutarlos con un doble clic o desde la terminal.

### ¿Qué es Batch?
**Batch** es un lenguaje simple de scripts para **Windows**.

- usa archivos con extensión `.bat` o `.cmd`
- corre bien desde `CMD` y también desde `PowerShell`
- sirve para mensajes, menús, copias, conteos, pequeñas automatizaciones y tareas de organización

Se usa, por ejemplo, cuando querés:

- mostrar mensajes en pantalla
- pedir datos al usuario
- copiar archivos
- automatizar una tarea corta sin instalar nada extra

### ¿Qué es Bash?
**Bash** es una shell y lenguaje de scripts muy usado en **Linux** y otros sistemas parecidos.

- usa archivos con extensión `.sh`
- aparece en servidores, tutoriales, Git Bash y WSL
- tiene más herramientas que Batch, pero para empezar en estas notebooks no hace falta instalarlo ni depender de él

Se usa, por ejemplo, cuando querés:

- automatizar tareas en Linux
- trabajar con servidores
- ejecutar scripts de desarrollo o de despliegue
- seguir tutoriales técnicos donde aparecen comandos de terminal Linux

### Batch y Bash, en una sola mirada

| Pregunta | Batch | Bash |
|---|---|---|
| ¿Dónde se usa más? | Windows | Linux / macOS / Git Bash |
| ¿Extensión típica? | `.bat` | `.sh` |
| ¿Sirve para automatizar? | Sí | Sí |
| ¿Cuál conviene hoy? | **Batch** | Solo como referencia |

## Antes de empezar

- Abrí **PowerShell**
- Trabajá dentro de tu carpeta de clase
- Si no la tenés, podés crear una carpeta de práctica

```powershell
cd C:\temp2026\Testing2026_APELLIDO\Eje_1_Software_Colaborativo
mkdir scripts
cd scripts
pwd
ls
```

## Comandos de Batch que vamos a usar

| Comando | Para qué sirve |
|---|---|
| `@echo off` | evita que se vea cada comando mientras corre el script |
| `echo` | muestra texto en pantalla |
| `pause` | espera a que la persona presione una tecla |
| `cls` | limpia la pantalla |
| `set /p` | pide un dato al usuario |
| `set /a` | hace cuentas sencillas |
| `if` | toma decisiones |
| `if exist` | verifica si un archivo o carpeta existe |
| `goto` | vuelve a una parte del script |
| `timeout /t` | espera una cantidad de segundos |
| `shutdown` | apaga o reinicia la computadora |

## Cómo crear y ejecutar un `.bat`

1. Crear el archivo desde el bloc de notas:

```powershell
notepad mi_script.bat
```

2. Escribir el código.
3. Guardar.
4. Ejecutar desde PowerShell:

```powershell
.\mi_script.bat
```

## Ejercicio guiado 1: cartel de bienvenida gamer

Vamos a crear un script que pregunte un nombre y muestre un mensaje personalizado.

### Paso 1: crear el archivo

```powershell
notepad saludo_gamer.bat
```

### Paso 2: pegar este código

```bat
@echo off
title Mi primer script
color 0A

echo ===============================
echo      BIENVENIDO AL TERMINAL
echo ===============================
echo.
set /p nombre=Como te llamas? 
echo.
echo Hola %nombre%.
echo Vamos a automatizar tareas con Batch.
echo.
pause
```

### Paso 3: guardarlo y ejecutarlo

```powershell
.\saludo_gamer.bat
```

### Paso 4: probar cambios
Modificá el script para que:

- cambie el titulo de la ventana
- muestre tu curso o apellido
- agregue un mensaje tipo "Nivel 1 desbloqueado"

### Qué aprendiste acá

- un script es un archivo de texto ejecutable
- `echo` muestra mensajes
- `set /p` permite pedir datos
- `pause` sirve para que la ventana no se cierre enseguida

## Ejercicio guiado 2: reloj de consola

Ahora vamos a hacer algo un poco más vistoso: un reloj que se actualiza cada segundo.

### Paso 1: crear el archivo

```powershell
notepad reloj_terminal.bat
```

### Paso 2: pegar este código

```bat
@echo off
title Reloj de consola
color 1F

:inicio
cls
echo ==========================
echo       RELOJ DIGITAL
echo ==========================
echo.
echo Fecha: %date%
echo Hora : %time%
echo.
echo Presiona Ctrl + C para cerrar.
timeout /t 1 > nul
goto inicio
```

### Paso 3: ejecutarlo

```powershell
.\reloj_terminal.bat
```

### Paso 4: entender qué pasa

- `:inicio` marca una parte del script
- `goto inicio` vuelve a ese punto
- `timeout /t 1` espera 1 segundo
- `cls` limpia la pantalla para que parezca que el reloj se actualiza

## Desafíos para resolver consultando con IA
La idea no es copiar y pegar sin pensar. La idea es pedir ayuda, probar, corregir y entender qué cambió.

### Cómo conviene usar la IA

- explicale que estás trabajando en **Windows** y usando **Batch `.bat`**
- pegale tu código actual
- pedile cambios pequeños, no todo de golpe
- probá lo que te responde
- si falla, pedile que lo corrija mostrando el error

### Prompt base sugerido

```text
Estoy haciendo un script .bat para Windows desde PowerShell.
Este es mi código:

[pegá acá tu código]

Quiero que lo modifiques para que...
Explicámelo paso a paso y usando comandos simples.
```

## Desafío 1: cartel personalizado
Crear `cartel_fan.bat` para que:

- pregunte tu nombre
- pregunte tu serie, juego o banda favorita
- muestre un cartel final con esos datos

Ejemplo esperado:

```text
Hola, Martina.
Tu modo actual es: fan de River.
```

## Desafío 2: cuenta regresiva con apagado real
Crear `se_vemo_en_disney.bat` para que:

- muestre el mensaje `Se vemo en Disney`
- pregunte si realmente querés apagar la notebook
- si la respuesta es `SI`, programe el apagado con una cuenta regresiva
- si la respuesta es `NO`, cancele la acción y muestre un mensaje final

Importante:
- usá un tiempo de espera, por ejemplo 30 segundos
- investigá también cómo cancelar un apagado con `shutdown /a`
- no uses apagado inmediato durante la clase

Base posible:

```bat
@echo off
echo Se vemo en Disney
set /p respuesta=Escribi SI para apagar la notebook o NO para cancelar: 

if /I "%respuesta%"=="SI" (
    shutdown /s /t 30 /c "Apagado programado desde un script Batch"
    echo Apagado programado. Si te arrepentis, ejecuta: shutdown /a
) else (
    echo Accion cancelada.
)

pause
```

## Desafío 3: mini menu
Crear `menu_merienda.bat` para que pregunte:

- `1` chocolatada
- `2` mate
- `3` agua

Luego debe responder con un mensaje distinto según la opción elegida.

Pista:
- investigá con IA cómo usar `if`

Ayuda útil para este ejercicio:

```bat
if "%opcion%"=="1" echo Elegiste chocolatada
```

Este tipo de `if` sirve cuando el script pregunta algo y querés que responda distinto según lo que escribió la persona.

## Desafío 4: backup simple
Crear `backup_txt.bat` para que:

- cree una carpeta llamada `backup`
- copie dentro de ella todos los archivos `.txt` que haya en la carpeta actual
- muestre un mensaje final diciendo si el respaldo se hizo

Pista:
- investigá con IA cómo usar `mkdir` y `copy`

## Desafío 5: control de entrega con `if`
Crear `control_entrega.bat` para que:

- revise si existe un archivo llamado `README.md`
- si existe, muestre `Entrega encontrada`
- si no existe, muestre `Falta el README`

Versión más completa:

- si no existe, que el script cree un archivo básico con ese nombre
- después muestre un mensaje diciendo que dejó una plantilla lista

Pista:
- investigá con IA cómo usar `if exist`

Ayuda útil para este ejercicio:

```bat
if exist README.md echo El archivo existe
```

Este tipo de `if` sirve para comprobar si un archivo o una carpeta ya existen. Es muy útil para automatización real: entregas, respaldos y control de estructura de carpetas.

## Qué mirar al probar un script

- si corre o muestra error
- si el mensaje se entiende
- si el archivo hace realmente lo que querías
- si pudiste explicar con tus palabras qué hace cada parte

## Cierre conceptual
Automatizar no significa hacer algo enorme. A veces alcanza con ahorrar 3 o 4 pasos repetidos. Ese es el comienzo de una idea muy importante en informática:

> si una tarea se repite, la puedo convertir en un procedimiento.

## Videos y material complementario

- [**¿Qué es Bash y para qué sirven los Bash Scripts?**](https://www.youtube.com/watch?v=0tIZhTAuNuU)
- [**Bash: explicado fácilmente en 3 minutos**](https://www.youtube.com/watch?v=EKFK83mNsyo)
- [**Programación BAT Parte I de II**](https://mediateca.educa.madrid.org/video/hqxz5dhwsvtgaxnx)
- [**Programación BAT - empleo del condicional IF**](https://mediateca.educa.madrid.org/video/dh2u1b5gccezcre2)
