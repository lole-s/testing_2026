# 1-9 Crear cuenta de GitHub y contribuir al repositorio clonado

## Clase: primer push a un repositorio compartido

## Objetivo
Crear una cuenta de **GitHub** usando la cuenta institucional de la escuela y contribuir al repositorio clonado en la actividad anterior.

Esta actividad continua lo trabajado en:

- [1-7 Git local](1-7_Git_Local.md)
- [1-7b Git local: practica complementaria](1-7b_Git_practica_complementaria.md)
- [1-8 Git desde Visual Studio Code](1-8_Git_desde_VSCode.md)

En la clase anterior clonamos este repositorio:

```text
https://github.com/lole-s/game-hub.git
```

Ahora vamos a usar una cuenta de GitHub para poder subir una contribucion sencilla al mismo repositorio.

```text
clonar -> modificar nombres.md -> commit -> push
```

---

## ¿Que es GitHub?

**GitHub** es una plataforma online para guardar, compartir y revisar proyectos de software.

GitHub usa **Git**, el sistema de control de versiones que ya venimos practicando. Git guarda el historial del proyecto; GitHub permite alojar ese historial en internet para compartirlo y trabajar con otras personas.

---

## Parte 1: crear la cuenta de GitHub

Usar la cuenta de correo de la escuela indicada por la docente.

1. Entrar a:

```text
https://github.com
```

2. Hacer clic en **Sign up**.
3. Completar los datos:

| Dato | Indicacion |
|---|---|
| Email | Usar la cuenta institucional de la escuela |
| Password | Crear una contraseña segura |
| Username | Elegir un nombre de usuario identificable y prolijo |

4. Verificar la cuenta desde el correo institucional.
5. Elegir el plan gratuito si GitHub lo solicita.

Responder:

```text
¿Pudiste verificar la cuenta desde el correo de la escuela?
¿Cual es tu nombre de usuario de GitHub?
```

Importante:

```text
No escribir contraseñas en la carpeta del proyecto, en README.md ni en capturas.
```

---

## Parte 2: recibir acceso al repositorio

Para poder hacer `push` al repositorio de la docente, cada estudiante necesita tener permiso de escritura o ser agregado/a como colaborador/a.

Repositorio de trabajo:

```text
https://github.com/lole-s/game-hub
```

La docente puede pedir el nombre de usuario de GitHub de cada estudiante y habilitar el acceso.

Responder:

```text
¿Cual es tu usuario de GitHub?
¿La docente ya confirmo que tenes acceso al repositorio?
```

---

## Parte 3: abrir el repositorio clonado en la clase anterior

Abrir en VS Code la carpeta clonada en la actividad `1-8`.

Desde terminal:

```bash
cd /c/temp2026/Testing2026_APELLIDO/Eje_1_Software_Colaborativo/game-hub
code .
```

Verificar que el remoto sea el repositorio correcto:

```bash
git remote -v
```

Deberia aparecer una URL parecida a:

```text
https://github.com/lole-s/game-hub.git
```

---

## Parte 4: actualizar antes de modificar

Antes de escribir en `nombres.md`, traer los cambios que ya hayan subido otras personas.

```bash
git pull
```

Si Git responde:

```text
Already up to date.
```

significa que la copia local ya estaba actualizada.

---

## Parte 5: modificar `nombres.md`

Abrir el archivo:

```text
nombres.md
```

Agregar el nombre y apellido en una linea nueva.

Ejemplo:

```text
Nombre Apellido
```

Guardar el archivo.

Verificar el cambio:

```bash
git status
```

---

## Parte 6: hacer el commit

Desde VS Code:

1. Abrir el panel de **Control de codigo fuente**.
2. Revisar que el archivo modificado sea `nombres.md`.
3. Preparar el cambio con `+`.
4. Escribir este mensaje de commit:

```text
Agrego mi nombre en nombres.md
```

5. Hacer commit.

Desde terminal seria:

```bash
git add nombres.md
git commit -m "Agrego mi nombre en nombres.md"
```

Verificar:

```bash
git log --oneline
```

---

## Parte 7: subir la contribucion con push

Subir el commit al repositorio remoto:

```bash
git push
```

Desde VS Code tambien se puede usar:

```text
Push
```

Si GitHub pide iniciar sesion, seguir la ventana de autenticacion de VS Code o del navegador.

En computadoras compartidas, cerrar sesion al terminar la clase si la docente lo indica.

---

## Parte 8: verificar en GitHub

Entrar al repositorio:

```text
https://github.com/lole-s/game-hub
```

Revisar:

- que `nombres.md` tenga el nombre agregado
- que aparezca el commit con el mensaje indicado
- que el autor del commit corresponda a la cuenta de GitHub o a la configuracion local de Git

Responder:

```text
¿Tu nombre aparece en nombres.md en GitHub?
¿Que mensaje de commit aparece?
¿Pudiste hacer push desde VS Code o desde terminal?
```

---

## Si el push falla

### No tengo permisos

Si aparece un error de permisos, revisar con la docente si la cuenta de GitHub fue agregada como colaboradora del repositorio.

### Hay cambios nuevos en GitHub

Si otra persona subio cambios antes, Git puede rechazar el `push`.

Primero traer los cambios:

```bash
git pull
```

Si no hay conflicto, volver a intentar:

```bash
git push
```

### Aparece un conflicto en `nombres.md`

Un conflicto puede aparecer si varias personas modificaron la misma parte del archivo.

En ese caso:

1. Abrir `nombres.md`.
2. Buscar las marcas:

```text
<<<<<<<
=======
>>>>>>>
```

3. Dejar todos los nombres que correspondan.
4. Borrar las marcas del conflicto.
5. Guardar.
6. Hacer commit de la resolucion.
7. Volver a hacer `push`.

---

## Entrega

Cada estudiante entrega:

- captura de `nombres.md` en GitHub con su nombre visible
- captura o texto de `git log --oneline`
- respuesta breve:

```text
¿Que diferencia hay entre commit y push?
¿Por que hicimos pull antes de modificar nombres.md?
¿Que permiso necesita una cuenta para poder hacer push a un repositorio?
```

---

## Cierre conceptual

En esta actividad no creamos un repositorio nuevo.

Usamos un repositorio existente, hicimos una modificacion chica, guardamos el cambio con `commit` y lo compartimos con `push`.

```text
Git guarda el cambio local.
GitHub recibe el cambio compartido.
```
