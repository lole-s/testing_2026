# 1-10 Repositorio colaborativo desde Visual Studio Code

## Clase: trabajo en equipo con Git, GitHub y VS Code

## Objetivo
Trabajar en grupos sobre un mismo repositorio usando:

```text
clonar -> crear rama -> modificar -> commit -> push -> Pull Request -> merge -> pull
```

La actividad retoma:

- [1-8 Git desde Visual Studio Code](1-8_Git_desde_VSCode.md)
- [1-9 Crear cuenta de GitHub y primer cambio desde el navegador](1-9_Crear_cuenta_GitHub_y_primer_push.md)

---

## Proyecto

Repositorio sugerido:

```text
https://github.com/lole-s/simon-proa-2026
```

El proyecto es un juego Simon hecho con:

- `index.html`
- `styles.css`
- `game.js`
- carpeta de sonidos

---

## Requisitos

- Tener Git instalado.
- Tener Visual Studio Code instalado.
- Tener cuenta de GitHub.
- Haber aceptado la invitacion al repositorio.
- Haber iniciado sesion en GitHub desde VS Code.

---

## Grupos de trabajo

Cada grupo tiene 3 integrantes.

Roles:

| Rol | Responsabilidad |
|---|---|
| Coordinacion Git | Crea la rama, revisa commits y publica la rama |
| Desarrollo | Modifica los archivos de la tarea |
| Testing | Prueba que el juego siga funcionando |

Los tres integrantes revisan el cambio antes de crear el Pull Request.

---

## Parte 1: clonar el repositorio

Desde VS Code:

1. Abrir `Ctrl + Shift + P`.
2. Buscar `Git: Clone`.
3. Pegar la URL:

```text
https://github.com/lole-s/simon-proa-2026.git
```

4. Elegir carpeta de trabajo.
5. Abrir el proyecto clonado.

Desde terminal:

```bash
cd /c/temp2026/Testing2026_APELLIDO/Eje_1_Software_Colaborativo
git clone https://github.com/lole-s/simon-proa-2026.git
cd simon-proa-2026
code .
```

---

## Parte 2: probar antes de modificar

Abrir:

```text
index.html
```

Desde VS Code:

1. Buscar `index.html` en el explorador de archivos de VS Code.
2. Hacer clic derecho sobre `index.html`.
3. Elegir **Reveal in File Explorer** o **Mostrar en el Explorador de archivos**.
4. Hacer doble clic sobre `index.html` para abrirlo en el navegador.

Probar:

- carga la pagina
- funcionan los botones
- no hay errores visibles
- el juego se puede iniciar

Responder:

```text
¿El proyecto funciona antes de hacer cambios?
¿Que archivos principales tiene?
```

---

## Parte 3: actualizar `main`

Antes de crear una rama:

```bash
git switch main
git pull origin main
```

---

## Parte 4: crear rama de trabajo

Cada grupo crea la rama indicada en la tabla de tareas.

Ejemplo:

```bash
git switch -c tarea-01-creditos-curso
```

Verificar:

```bash
git branch
```

---

## Parte 5: tareas por grupo

| Grupo | Rama | Archivos | Tarea |
|---|---|---|---|
| 1 | `tarea-01-creditos-curso` | `index.html`, `styles.css` | Agregar una seccion `Creditos del curso` que represente a todo el curso. Incluir curso, anio, escuela y una frase grupal. |
| 2 | `tarea-02-instrucciones-juego` | `index.html`, `styles.css` | Agregar una seccion `Como jugar` con 3 pasos: mirar la secuencia, repetirla, avanzar de nivel. |
| 3 | `tarea-03-panel-estado` | `index.html`, `styles.css` | Ordenar el panel de estado para que nivel, mensaje y boton de inicio se vean claros. |
| 4 | `tarea-04-estilos-botones` | `styles.css` | Mejorar los cuatro botones: mismo tamanio, bordes consistentes, separacion pareja y efecto hover. |
| 5 | `tarea-05-animacion-activo` | `styles.css`, `game.js` | Mejorar el efecto visual cuando un boton se activa en la secuencia. |
| 6 | `tarea-06-mensaje-bienvenida` | `index.html`, `game.js` | Mostrar un mensaje inicial de bienvenida y cambiarlo al iniciar el juego. |
| 7 | `tarea-07-nivel-visible` | `index.html`, `game.js`, `styles.css` | Hacer que el nivel actual se vea claramente y se actualice al avanzar. |
| 8 | `tarea-08-game-over` | `index.html`, `game.js`, `styles.css` | Mejorar el mensaje de fin de juego e indicar como volver a empezar. |

Cada grupo anota:

```text
Grupo:
Integrantes:
Rama:
Archivos modificados:
Cambio realizado:
Como lo probaron:
```

---

## Parte 6: commit

Despues de modificar:

1. Guardar archivos.
2. Probar el juego.
3. Revisar cambios en VS Code.
4. Preparar cambios.
5. Hacer commit.

Ejemplos:

```text
Agrego creditos del curso
Mejoro instrucciones del juego
Actualizo estilos de botones
Muestro nivel actual
```

Desde terminal:

```bash
git status
git add .
git commit -m "Agrego creditos del curso"
```

---

## Parte 7: push

Desde VS Code:

```text
Publish Branch
```

o:

```text
Push
```

Desde terminal:

```bash
git push -u origin tarea-01-creditos-curso
```

---

## Parte 8: Pull Request

En GitHub:

1. Entrar al repositorio.
2. Buscar la rama publicada.
3. Hacer clic en **Compare & pull request**.
4. Escribir titulo claro.
5. Completar:

```text
Grupo:
Integrantes:
Rama:
Que cambiamos:
Como lo probamos:
Archivos modificados:
```

6. Crear el Pull Request.

Responder:

```text
¿Cual es el enlace al Pull Request?
¿Que archivo modifico tu grupo?
¿Como probaron que funcionaba?
```

---

## Parte 9: revision y merge

El docente revisa cada Pull Request.

El merge lo hace el docente para cuidar la version principal del proyecto.

Antes del merge, el grupo debe mostrar:

- juego funcionando
- archivos modificados
- commit realizado
- Pull Request completo

Si hay conflictos, se resuelven antes del merge.

---

## Parte 10: traer la version final

Despues de que el docente mergea los Pull Requests, todos actualizan su copia:

```bash
git switch main
git pull origin main
```

Verificar:

```bash
git log --oneline --graph --all
```

Responder:

```text
¿Aparecen commits de otros grupos?
¿Tu cambio quedo integrado en main?
¿El juego sigue funcionando?
```

---

## Conflictos

Un conflicto aparece cuando dos ramas modifican la misma parte de un archivo.

Si aparece:

1. No cerrar VS Code.
2. Buscar las marcas:

```text
<<<<<<<
=======
>>>>>>>
```

3. Decidir que parte queda.
4. Borrar las marcas.
5. Guardar.
6. Hacer commit de la resolucion.

---

## Entrega

Cada grupo entrega:

- enlace a la rama
- enlace al Pull Request
- captura del commit en VS Code
- breve descripcion del cambio
- explicacion de como lo probaron
- respuesta:

```text
¿Por que trabajamos en una rama?
¿Que diferencia hay entre commit, push y pull?
¿Quien hizo el merge a main?
¿Como llegamos todos a la misma version final?
```

---

## Resumen

```text
La rama permite trabajar sin romper main.
El Pull Request permite revisar antes de unir.
El docente hace merge.
Todos hacen pull para llegar a la version final.
```
