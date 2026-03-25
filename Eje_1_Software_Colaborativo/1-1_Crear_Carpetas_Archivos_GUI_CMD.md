# 1-1 Crear carpetas y archivos (GUI + PowerShell)

## Objetivo
Organizar una estructura de trabajo para la materia y practicar comandos básicos de terminal en Windows.

## Actividad previa online
Antes de las actividares para crear carpetas/archivos localmente en la computadora vamos a hace runa clase introductoria con una exploración breve de estos conceptos desdeel navegador.

## Opción 1: práctica online estilo Windows

- [**Windows Command Prompt Hub / CMD Master**](https://windows-cli.arnost.org/es/dashboard)

### Qué tenés que mirar
- qué comando escribiste
- qué respuesta mostró la terminal
- si el sistema aceptó el comando o mostró error

## Opción 2: práctica online estilo Linux
- [**TryBash**](https://trybash.github.io/game/)  (RECOMENDADA)

- [**JSLinux**](https://bellard.org/jslinux/)
- [**CMD Challenge**](https://cmdchallenge.com/)

Si usás **JSLinux**, probá esta secuencia:

```bash
pwd
ls
mkdir practica
cd practica
pwd
echo "hola" > saludo.txt
cat saludo.txt
```

### Qué tenés que mirar
- cómo saber en qué carpeta estás
- cómo ver lo que hay dentro de una carpeta
- cómo crear una carpeta nueva
- cómo crear y leer un archivo

## Mini entrega de la actividad previa
Escribí una respuesta breve con estas tres partes:

1. ¿Qué sitio usaste?
2. ¿Qué comando recordás?
3. ¿Qué te resultó más raro, más difícil o más interesante?

### Pregunta para pensar
Aunque esta terminal sea Linux y en clase usemos PowerShell, ¿qué comandos o ideas te parecieron parecidos?

# ACTIVIDADES OFFLINE en PC

## Idea clave
La terminal trabaja sobre los mismos archivos y carpetas que ves en el Explorador. La diferencia es que en vez de hacer clic, vas a usar comandos.


## Antes de empezar

- Trabajá en **PowerShell**.
- Usá una carpeta en `C:\temp2026`.

## Comandos de hoy

| Acción | PowerShell | CMD | Linux / Git Bash |
|---|---|---|---|
| Ver dónde estoy | `pwd` | `cd` | `pwd` |
| Ver qué hay | `ls` | `dir` | `ls` |
| Entrar a una carpeta | `cd carpeta` | `cd carpeta` | `cd carpeta` |
| Subir un nivel | `cd ..` | `cd ..` | `cd ..` |
| Crear carpeta | `mkdir carpeta` | `mkdir carpeta` | `mkdir carpeta` |
| Crear archivo con texto | `echo "texto" > archivo.txt` | `echo texto>archivo.txt` | `echo "texto" > archivo.txt` |
| Ver archivo | `cat archivo.txt` | `type archivo.txt` | `cat archivo.txt` |
| Mover o renombrar | `mv origen destino` | `move origen destino` | `mv origen destino` |
| Borrar archivo | `rm archivo.txt` | `del archivo.txt` | `rm archivo.txt` |

## Actividad 1: Crear tu carpeta de trabajo
Abrí PowerShell y ejecutá:

```powershell
cd /
mkdir temp2026
cd temp2026
mkdir Testing2026_APELLIDO
cd Testing2026_APELLIDO
pwd
ls
```

## Actividad 2: Armar la estructura de la materia
Dentro de `Testing2026_APELLIDO`, creá estas carpetas:

- `Eje_1_Software_Colaborativo`
- `Eje_2_Redes_de_Datos`
- `Eje_3_Testing`

Usá estos comandos:

```powershell
mkdir Eje_1_Software_Colaborativo
mkdir Eje_2_Redes_de_Datos
mkdir Eje_3_Testing
ls
```

## Actividad 3: Crear archivos de documentación
Creá un `README.md` dentro de cada eje:

```powershell
echo "# Eje 1" > .\Eje_1_Software_Colaborativo\README.md
echo "# Eje 2" > .\Eje_2_Redes_de_Datos\README.md
echo "# Eje 3" > .\Eje_3_Testing\README.md
```

Verificá el contenido de uno de los archivos:

```powershell
cat .\Eje_1_Software_Colaborativo\README.md
```

## Actividad 4: Ordenar un archivo
Primero creá un archivo en el HOME del USUARIO:

```powershell
echo $HOME
cd $HOME/Desktop
ls
echo "borrador" > borrador.txt
ls
```

Ahora movelo a `Eje_3_Testing` y renombralo como `notas_iniciales.txt`:

```powershell
mv .\borrador.txt .\Eje_3_Testing\notas_iniciales.txt
ls .\Eje_3_Testing
```

## Actividad 5: Limpieza controlada
Creá un archivo temporal:

```powershell
echo "basura" > archivo.tmp
ls
```

Borrá el archivo temporal:

```powershell
rm .\archivo.tmp
ls
```

## Mini Entrega 1-1 (2)
En el mismo archivo que ayer, respondé por escrito:

1. ¿Qué comando te dice en qué carpeta estás?
2. ¿Qué comando te muestra qué hay en una carpeta?
3. ¿Qué diferencia encontras entre usar GUI y usar terminal?
4. Pegar una captura de pantalla del árbol de la carpeta `temp2026` que crearte

```powershell
C:\temp2026
```
   
      
## Cómo hacer la captura en Windows
La forma más simple es esta:

1. Dejá abierta la ventana que querés mostrar.
2. Presioná `Win + Shift + S`.
3. Elegí la opción de recorte rectangular.
4. Seleccioná con el mouse la parte de la pantalla que querés capturar.
5. Pegá la captura con `Ctrl + V` en un documento

### ACTIVIDAD Extra (SSH)
https://overthewire.org/

## Videos complementarios

- [**Microaprendizaje: ¿Qué es una terminal o consola?**](https://www.youtube.com/watch?v=gN_0sWWV3CA)
- [**CMD vs Powershell desde cero**](https://www.youtube.com/watch?v=dJSYTJMU4GQ&t)
- [**Bash: Explicado Fácilmente en 3 minutos**](https://www.youtube.com/watch?v=EKFK83mNsyo)

- [**Sugerencias de terminal en VS Code**](https://learn.microsoft.com/es-es/shows/visual-studio-code/terminal-tips-in-vs-code)
- [**PowerShell para principiantes**](https://learn.microsoft.com/es-es/shows/mvp-windows-and-devices-for-it/powershell-beginners)

- [**¿Qué es la SHELL de LINUX y BASH?**](https://www.youtube.com/watch?v=YUCXzp8n93U)

## Recurso complementario
- [**Primeros pasos con la terminal en VS Code**](https://code.visualstudio.com/docs/terminal/getting-started)
