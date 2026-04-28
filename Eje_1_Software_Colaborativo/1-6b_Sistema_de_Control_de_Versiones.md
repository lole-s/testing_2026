# 1-6 Sistema de control de versiones

## Objetivo
Entender qué problema resuelve un sistema de control de versiones antes de empezar a usar Git.

## Idea clave
Cuando un proyecto cambia muchas veces, no alcanza con guardar archivos como:

- `trabajo_final.docx`
- `trabajo_final_ahora_si.docx`
- `trabajo_final_definitivo_v2.docx`

Eso genera desorden, confusión y pérdida de información.

Un **sistema de control de versiones** permite guardar el historial de cambios de un proyecto de forma ordenada.

## ¿Qué es un SCV?
SCV significa **Sistema de Control de Versiones**.

En inglés suele aparecer como:

- `VCS` = Version Control System
- `SCM` = Source Code Management

En la práctica, estas herramientas sirven para:

- registrar cambios en archivos
- volver a una versión anterior
- comparar qué cambió
- dejar mensajes explicando cada cambio
- trabajar entre varias personas sin pisarse tanto

## Ejemplo cotidiano
Imaginá un apunte grupal o un proyecto con varias entregas.

Sin control de versiones puede pasar esto:

- una persona borra algo sin querer
- otra cambia el archivo y no sabemos qué modificó
- nadie recuerda cuál era la última versión correcta

Con un SCV, el proyecto guarda una historia de cambios.

## Qué se puede hacer con un sistema de control de versiones

- ver quién cambió algo
- ver cuándo se hizo ese cambio
- recuperar versiones anteriores
- probar cambios sin romper la versión principal
- organizar mejor el trabajo técnico

## ¿Solo sirve para programar?
No. También se puede usar para:

- apuntes
- documentación
- informes
- proyectos escolares
- páginas web

## Video sugerido
- [¿Qué es el control de versiones y por qué es importante?](https://www.youtube.com/watch?v=8HSjmgeJxqg)

## Antes de Git: principios del SCM

Antes de usar comandos, conviene entender algunos principios de esta forma de trabajar.

SCM significa **Source Code Management**. Se puede traducir como **gestión del código fuente**.

Un SCM no es solamente una herramienta para "guardar archivos". Es una forma de organizar el trabajo técnico para que el proyecto tenga memoria.

Sus principios principales son:

- **historial**: cada cambio importante queda registrado
- **autoría**: se puede saber quién hizo un cambio
- **mensaje**: cada cambio debería explicar por qué se hizo
- **comparación**: se puede ver qué cambió entre dos versiones
- **recuperación**: se puede volver a un estado anterior
- **colaboración**: varias personas pueden trabajar con menos riesgo de pisarse

En proyectos de software, estos principios son fundamentales porque el código cambia todo el tiempo.

## Actividad complementaria
Para entender de dónde viene Git, la próxima actividad propone armar una línea de tiempo colaborativa:

- Unix
- GNU
- software libre
- Minix
- Linux
- BitKeeper
- Git

La idea es entender que Git nació como respuesta a una necesidad concreta dentro de un proyecto enorme: coordinar cambios en el kernel Linux.

## Del concepto a la herramienta
En este eje vamos a usar **Git**, que es uno de los sistemas de control de versiones más usados en el mundo del software.

Antes de pasar a Git, conviene quedarse con esta idea:

> un proyecto no solo se guarda: también se versiona.

## Preguntas para pensar

1. ¿Qué problemas aparecen cuando varias personas editan archivos sin un orden claro?
2. ¿Qué ventaja tendría poder volver a una versión anterior?
3. ¿En qué actividad escolar o técnica te parece que esto podría servir?

## Cierre conceptual
Hasta ahora venimos trabajando con:

- carpetas y archivos
- terminal
- automatización simple
- documentos compartidos
- Markdown

El paso siguiente es natural:

> si ya sé organizar un proyecto, ahora necesito guardar su historia.
