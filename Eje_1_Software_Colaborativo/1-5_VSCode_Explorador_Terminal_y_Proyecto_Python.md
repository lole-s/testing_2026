# 1-5 VS Code: explorador, terminal y proyecto Python

## Objetivo
Usar Visual Studio Code como entorno de trabajo técnico para:

- abrir una carpeta de proyecto
- crear archivos y carpetas
- usar la terminal integrada
- construir un proyecto Python con varios archivos
- ejecutar un programa desde `main.py`

## Idea clave
VS Code no es solo un editor para escribir código.

También puede funcionar como centro de trabajo del proyecto:

- explorador de archivos
- editor de texto
- terminal integrada
- vista previa de Markdown
- acceso posterior a Git

## Por qué verlo en este eje
Hasta ahora venimos trabajando con:

- carpetas y archivos
- terminal
- automatización simple
- trabajo compartido
- documentación con Markdown

VS Code permite juntar varias de esas cosas en un solo lugar.

La idea de esta clase no es aprender "todo VS Code", sino usarlo para trabajar mejor con proyectos reales.

## Video sugerido
- [Visual Studio Code - Terminal integrada](https://www.youtube.com/watch?v=CxF3ykWP1H4)

## Material complementario
- [Terminal de Visual Studio Code - KeepCoding](https://keepcoding.io/blog/terminal-de-visual-studio-code/)

Este material sirve como apoyo o lectura breve, pero en clase conviene priorizar la práctica directa.

## Qué vamos a usar hoy

- el explorador de archivos de VS Code
- la terminal integrada
- PowerShell como terminal principal
- Python
- una estructura simple de proyecto

## Parte 1: teoría breve

### Qué es VS Code
Visual Studio Code es un editor que permite trabajar con carpetas de proyecto completas.

En vez de abrir un archivo suelto, conviene abrir una **carpeta**.

Eso permite:

- ver toda la estructura del proyecto
- crear archivos desde el explorador
- abrir la terminal ya ubicada en esa carpeta
- trabajar luego con Git sin salir del entorno

### Qué es la terminal integrada
Es una terminal que aparece dentro de VS Code.

Sirve para:

- ejecutar comandos
- correr Python
- crear carpetas y archivos
- moverse dentro del proyecto
- usar Git más adelante

## Atajos útiles

| Acción | Atajo sugerido |
|---|---|
| Abrir terminal | `Ctrl + Ñ` o `Ctrl + \`` |
| Abrir paleta de comandos | `Ctrl + Shift + P` |
| Abrir explorador | `Ctrl + Shift + E` |
| Crear archivo nuevo | desde el explorador |

## Parte 2: abrir la carpeta del proyecto

1. Abrir VS Code.
2. Ir a `Archivo > Abrir carpeta`.
3. Abrir la carpeta `testing_2026` o una carpeta de práctica.
4. En el explorador, ubicar `Eje_1_Software_Colaborativo`.

## Qué mirar

- diferencia entre abrir un archivo y abrir una carpeta
- cómo aparece el árbol del proyecto
- cómo crear archivos desde el explorador

## Parte 3: abrir la terminal integrada

Abrir la terminal desde:

- menú `Terminal > New Terminal`
- o con `Ctrl + Ñ`

Verificar dónde estamos con:

```powershell
pwd
ls
```

## Idea clave
La terminal integrada trabaja sobre la misma carpeta que ves en el explorador.

No son dos mundos separados.

## Parte 4: crear un proyecto Python simple

Vamos a crear un proyecto llamado `python_hola`.

### Paso 1: entrar al eje

```powershell
cd .\Eje_1_Software_Colaborativo
```

### Paso 2: crear carpeta del proyecto

```powershell
mkdir python_hola
cd .\python_hola
```

### Paso 3: crear estructura inicial

```powershell
mkdir src
mkdir docs
mkdir evidencias
echo "# Proyecto Python Hola" > README.md
echo "Notas del proyecto" > .\docs\notas.txt
```

## Estructura esperada

```text
python_hola/
|-- docs/
|   `-- notas.txt
|-- evidencias/
|-- src/
`-- README.md
```

## Parte 5: crear una estructura más realista

En muchos proyectos Python no se trabaja con un solo archivo.

Es más común separar responsabilidades:

- un archivo principal
- uno o más módulos auxiliares
- documentación

Vamos a armar una mini aplicación de consola con tres archivos Python.

## Estructura propuesta

```text
python_hola/
|-- docs/
|   `-- notas.txt
|-- evidencias/
|-- src/
|   |-- main.py
|   |-- mensajes.py
|   `-- utilidades.py
`-- README.md
```

## Parte 6: crear los archivos Python

### Archivo 1: `src\mensajes.py`

```python
def saludo(nombre):
    return f"Hola, {nombre}."


def despedida():
    return "Proyecto creado correctamente."
```

### Archivo 2: `src\utilidades.py`

```python
def pedir_entero(mensaje):
    return int(input(mensaje))


def categoria_edad(edad):
    if edad < 13:
        return "menor"
    if edad < 18:
        return "adolescente"
    return "adulto"
```

### Archivo 3: `src\main.py`

```python
from mensajes import saludo, despedida
from utilidades import pedir_entero, categoria_edad


nombre = input("Ingresa tu nombre: ")
edad = pedir_entero("Ingresa tu edad: ")

print(saludo(nombre))
print(f"Tenés {edad} años.")
print(f"Categoría: {categoria_edad(edad)}")
print(despedida())
```

## Qué mirar en este ejemplo

- `main.py` organiza el flujo principal
- `mensajes.py` guarda funciones de texto
- `utilidades.py` concentra tareas auxiliares
- `import` permite usar código de otros archivos

## Ejecutar el proyecto

Pararse dentro de `python_hola\src` y ejecutar:

```powershell
cd .\src
python .\main.py
```

Si en esa computadora funciona con `py` en vez de `python`, probar:

```powershell
py .\main.py
```

## Parte 7: mejorar el README

Abrir `README.md` y completar algo así:

```md
# Proyecto Python Hola

**Nombre y apellido:** TU_NOMBRE

## Objetivo
Practicar VS Code, terminal integrada y Python con varios archivos.

## Archivos del proyecto
- `src/main.py`
- `src/mensajes.py`
- `src/utilidades.py`
- `README.md`
```

Luego agregar esta sección:

```md
## Cómo ejecutar
```

Y debajo escribir estos comandos:

```powershell
cd .\src
python .\main.py
```

## Parte 8: mini actividad práctica

### Consigna
Modificar el proyecto para que:

1. pida el nombre
2. pida la edad
3. pida la ciudad
4. muestre un mensaje final con todos esos datos
5. use al menos una función nueva en alguno de los módulos

Ejemplo esperado:

```text
Hola, Martina.
Tenés 17 años.
Vivís en Corral de Bustos.
Proyecto creado correctamente.
```

## Desafío opcional

Agregar una función en `mensajes.py` que devuelva un mensaje según la categoría:

- `menor`
- `adolescente`
- `adulto`

Luego llamarla desde `main.py`.

## Parte 9: actividad de orden y exploración

Dentro del mismo proyecto:

1. Crear un archivo `evidencia_1.txt` dentro de `evidencias`.
2. Escribir una línea breve en `docs\notas.txt`.
3. Revisar la estructura desde el explorador.
4. Revisar la estructura desde terminal con:

```powershell
ls
ls .\src
ls .\docs
ls .\evidencias
```

## Parte 10: puesta en común

Luego de ejecutar el proyecto, responder:

1. Qué ventaja tiene abrir una carpeta completa en VS Code.
2. Para qué sirve la terminal integrada.
3. Qué diferencia encontrás entre crear algo desde el explorador y desde terminal.
4. Para qué sirve separar el proyecto en varios archivos `.py`.
5. Qué archivo explica el proyecto.

## Entrega sugerida

- captura de VS Code mostrando:
  - explorador con la carpeta del proyecto
  - terminal integrada abierta
  - archivo `src/main.py`
- carpeta `python_hola` con:
  - `README.md`
  - `src/main.py`
  - `src/mensajes.py`
  - `src/utilidades.py`
  - `docs/notas.txt`
  - `evidencias/evidencia_1.txt`

## Cierre
VS Code permite trabajar sobre un proyecto completo y no solo sobre un archivo.

También ayuda a empezar a pensar cómo se organiza un programa real:

- carpetas
- archivos
- módulos
- terminal
- documentación

Eso prepara muy bien el paso siguiente del eje:

- usar Git local
- entender repositorios
- versionar cambios reales
