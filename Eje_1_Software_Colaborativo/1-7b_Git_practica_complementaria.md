# 1-7b Git local: practica complementaria

## Clase: Git como maquina del tiempo, sin perderse en la consola

## Objetivo de la clase
Reforzar Git local desde una practica, visual y guiada.

La idea principal no es aprender muchos comandos nuevos, sino entender bien:

- que es un repositorio
- que hace `git status`
- que diferencia hay entre editar, preparar y commitear
- que es un commit
- que es `HEAD`
- para que sirve una rama
- como volver a una version anterior sin miedo

## Punto de partida
Esta clase complementa la actividad anterior:

- [1-7 Git local](1-7_Git_Local.md)

---

## Video corto e idea base

### Video recomendado
[¿Qué es Git y cómo funciona?](https://www.youtube.com/watch?v=jGehuhFhtnE)

### Áreas de trabajo
```text
Git trabaja con 3 zonas:

1. Carpeta de trabajo
   Donde escribo y modifico archivos.

2. Staging
   Lo que preparo para guardar.

3. Repositorio local
   El historial guardado en commits.
```

```text
Escribo -> preparo -> guardo version
```

### Preguntas

```text
¿Git guarda automaticamente todo lo que escribo?
```

Respuesta:

```text
No. Para guardar una version necesito hacer commit.
```

---

## Repaso de conceptos importantes
### Git
Git es una herramienta local de control de versiones.

No es lo mismo que GitHub.

### Repositorio
Un repositorio es una carpeta que Git esta controlando.

Cuando hacemos:

```bash
git init
```

Git crea una carpeta oculta:

```text
.git
```

En esta carpeta se guardará la historia del proyecto.

### Commit
Un commit es una version guardada del proyecto.

Podemos pensarlo como una foto:

```text
commit = foto del proyecto + mensaje
```

### Staging
El staging es una zona intermedia.

Con:

```bash
git add archivo
```

le decimos a Git:

```text
Este cambio quiero incluirlo en el proximo commit.
```

### HEAD
`HEAD` indica donde estamos parados en la historia.

Si el historial fuera una linea de tiempo, `HEAD` seria el cartel de "usted esta aqui".

### Rama
Una rama es un camino de trabajo.

Sirve para probar cambios sin romper la version principal.

---

## Actividad online visual

### Sitio
[Visualizing Git](https://git-school.github.io/visualizing-git/)

### Objetivo
Entender visualmente:

- commits
- HEAD
- ramas
- checkout
- merge

### Actividad guiada

Al entrar al sitio ya aparece un repositorio creado.

No hace falta ejecutar `git init`.

El estado inicial es:

```text
Repositorio local ya creado.
Rama actual: master.
Primer commit: first commit.
HEAD esta parado en master.
```

En la parte izquierda hay una consola negra. Abajo, donde dice:

```text
$ enter git command
```

se escriben comandos de Git. A la derecha se ve el dibujo del repositorio.

<!-- #### Paso 1
Mirar la pantalla inicial.

```text
¿Cuantos commits hay al principio?
¿En que rama esta HEAD?
```
```text
Hay un commit inicial.
HEAD esta en master.
```
 -->

#### Paso 2
Crear dos commits nuevos en `master`.

En la consola del sitio escribir:

```bash
git commit -m 'version 1 - OK' 
git commit -m 'version 2 - OK' 
```

<!-- Preguntar:

```text
¿Que aparecio en el dibujo?
¿HEAD se movio?
```

Respuesta esperada:

```text
Aparecieron dos commits nuevos.
HEAD quedo parado en el ultimo commit de master.
``` -->

#### Paso 3
Crear una rama nueva llamada `idea`.

```bash
git branch idea
```

<!-- Preguntar:

```text
¿Aparecio una nueva etiqueta de rama?
¿HEAD se movio a la rama idea?
```

Respuesta esperada:

```text
Aparecio la rama idea.
HEAD no se movio todavia: sigue en master.
```

 -->I

```text
Crear una rama no significa moverse a esa rama.
```

#### Paso 4
Moverse a la rama `idea`.

```bash
git checkout idea
```

<!-- Preguntar:

```text
¿Donde esta HEAD ahora?
```

Respuesta esperada:

```text
HEAD esta en idea.
```
 -->
#### Paso 5
Hacer un commit en la rama `idea`.

```bash
git commit -m 'version 3'
```

<!-- Preguntar:

```text
¿La rama idea avanzo?
¿master tambien avanzo?
```

Respuesta esperada:

```text
idea avanzo.
master quedo en el commit anterior.
```

Idea clave:
 -->
```text
Las ramas pueden tener historias distintas.
```

#### Paso 6
Volver a `master`.

```bash
git checkout master
```
<!-- 
Preguntar:

```text
¿Se borro el commit de idea?
¿O solamente cambiamos de lugar?
```

Respuesta esperada:

```text
No se borro.
Solamente cambiamos de rama.
```
 -->
#### Paso 7
Hacer un commit nuevo en `master`.

```bash
git commit -m 'version 3 Master'
```

<!-- Preguntar:

```text
¿Ahora hay dos caminos separados?
```

Respuesta esperada:

```text
Si. master tiene un commit nuevo e idea tiene otro commit distinto.
```
 -->
#### Paso 8
Unir la rama `idea` a `master`.

Primero verificar visualmente que HEAD este en `master`.

Despues escribir:

```bash
git merge idea
```
<!-- 
Preguntar:

```text
¿Que paso con los caminos?
¿Aparecio un commit de merge?
```

Respuesta esperada:

```text
Git unio las dos historias.
Puede aparecer un commit de merge que conecta los caminos.
```

Cierre del bloque:
 -->
```text
Git no guarda una sola historia lineal.
Puede crear ramas, moverse entre ellas y despues unirlas.
```

---

## Demo guiada en consola

En Git Bash:

```bash
cd /c/temp2026
mkdir git_demo
cd git_demo
```

### Inicializar repositorio

```bash
git init
git status
```

Preguntar:

```text
¿Ya hay commits?
```

### Crear version 1

```bash
echo "v1: proyecto funcionando" > app.txt
git status.
# El archivo primero aparece como nuevo.
git add app.txt
git status
# El archivo primero queda preparado.
git commit -m "v1 proyecto funcionando"
git status
# El archivo primero queda guardado

```

### Crear version 2

```bash
echo "v2: agrego una mejora" >> app.txt
git status
git add app.txt
git commit -m "v2 agrego mejora"
```

### Crear version 3 con error

```bash
echo "ERROR: esta linea rompe el proyecto" >> app.txt
git status
git add app.txt
git commit -m "v3 aparece un error"
```

### Ver historial

```bash
git log --oneline
```

### Ver el archivo

```bash
cat app.txt
```

```text
¿El error esta en el archivo?
```
### Volver una version atras
```bash
git checkout HEAD~1
```
Volver a inspeccionar el archivo

```bash
cat app.txt
```

Preguntas clave:

```text
¿Desaparecio la linea del error?
¿Borramos el commit del error?
```

<!-- Respuestas esperadas:

```text
La linea del error no se ve en esta version.
No borramos el commit: solo nos movimos en la historia.
``` -->

### Volver a la version principal

Primero mirar el nombre de la rama principal:

```bash
git branch
```

Despues volver. Si la rama se llama `main`:

```bash
git checkout main
```

Si la rama se llama `master`:

```bash
git checkout master
```

Verificar:

```bash
git status
cat app.txt
```

---

## Actividad guiada para estudiantes

### Tiempo estimado
20 minutos

## Consigna
Crear un repositorio, guardar tres versiones, volver a una version buena y crear una rama de arreglo.

### Reglas de trabajo

- Trabajar en parejas.
- Una persona escribe, la otra lee la guia y controla.
- Despues de cada bloque, ejecutar `git status`.
- Si aparece un error, no cerrar la terminal. Leer el mensaje y pedir ayuda de ser necesario.

### Paso 0: ubicarse

En Git Bash:

```bash
pwd
```

Esto muestra en que carpeta estoy.

Entrar a la carpeta de trabajo:

```bash
cd /c/temp2026
```

Crear carpeta nueva:

```bash
mkdir practica_git_apellido
cd practica_git_apellido
```

Importante: cambiar `apellido` por el apellido del grupo.

### Paso 1: crear el repositorio

```bash
git init
git status
```

### Paso 2: version 1

```bash
echo "base: el proyecto funciona" > app.txt
git status
git add app.txt
git commit -m "v1 proyecto base"
```

### Paso 3: version 2

```bash
echo "mejora: agregamos una funcion" >> app.txt
git status
git add app.txt
git commit -m "v2 agrego mejora"
```

### Paso 4: version 3 con error

```bash
echo "ERROR: cambio incorrecto" >> app.txt
git status
git add app.txt
git commit -m "v3 aparece error"
```

### Paso 5: ver historial

```bash
git log --oneline
```

Responder:

```text
¿Cuantos commits hay?
¿Cual es el mas nuevo?
```

### Paso 6: mirar el archivo actual

```bash
cat app.txt
```

Responder:

```text
¿Esta la linea del error?
```

### Paso 7: volver a la version anterior

```bash
git checkout HEAD~1
cat app.txt
```

Responder:

```text
¿Sigue estando el error?
¿Que hizo checkout: borro o se movio?
```

### Paso 8: crear una rama de arreglo

Desde esa version buena:

```bash
git switch -c arreglo
```

Agregar un arreglo:

```bash
echo "arreglo: solucion correcta" >> app.txt
git add app.txt
git commit -m "fix arreglo correcto"
```

### Paso 9: ver la historia completa

```bash
git log --oneline --graph --all
```

Responder:

```text
¿Se ven dos caminos en la historia?
¿En que rama estoy parado ahora?
```

Para ver la rama actual:

```bash
git branch
```

La rama actual aparece marcada con `*`.

---

## Bloque 6: cierre
## Preguntas finales

Responder entre todos:

1. ¿Que hace `git init`?
2. ¿Que muestra `git status`?
3. ¿Para que sirve `git add`?
4. ¿Que guarda un commit?
5. ¿Que significa `HEAD`?
6. ¿Que paso cuando hicimos `checkout HEAD~1`?
7. ¿Para que sirve una rama?

## Frase final

```text
Git no borra cosas facilmente.
Git permite guardar versiones, volver atras y crear nuevos caminos.
```

---

## Actividad extra
https://learngitbranching.js.org/?locale=es_AR