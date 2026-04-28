# 1-6c De Unix a Git: línea de tiempo colaborativa

## Objetivo
Reconstruir la historia desde Unix hasta Git entendiendo por qué cada hito fue necesario para el siguiente.

## Organización

- **Curso:** 5to/6to año - Informática
- **Tiempo:** 20 min de investigación grupal + 2 min de exposición por grupo
- **Grupos:** 9 grupos de 3 estudiantes
- **Producción:** una explicación breve para armar entre todos una línea de tiempo

## Idea clave
Git no apareció de la nada.

Antes hubo una historia de sistemas operativos, universidades, software libre, crecimiento de proyectos colaborativos y problemas reales para coordinar cambios en el código.

La película completa puede resumirse así:

> Unix creó una cultura de compartir código. Luego aparecieron restricciones comerciales. GNU defendió la libertad del software. Linux aportó el kernel que faltaba. El proyecto Linux creció tanto que necesitó mejores herramientas. Git nació para manejar ese trabajo distribuido.

## Antes de investigar: otros VCS

Git es el VCS más usado actualmente, pero no fue el primero ni el único.

Antes y durante su aparición existieron otras herramientas importantes:

| Herramienta | Tipo de VCS | Idea principal |
|---|---|---|
| **RCS** | local | guardaba versiones de archivos individuales |
| **CVS** | centralizado | permitió que varias personas trabajaran contra un repositorio central |
| **Subversion / SVN** | centralizado | buscó mejorar CVS y fue muy usado antes de Git |
| **BitKeeper** | distribuido | fue usado por el kernel Linux antes de Git, pero tenía una licencia polémica |
| **Mercurial** | distribuido | apareció en la misma época que Git como alternativa moderna |
| **Git** | distribuido | nació para coordinar el desarrollo del kernel Linux de forma rápida y confiable |

La diferencia clave:

- en un VCS **centralizado**, el historial principal vive en un servidor central
- en un VCS **distribuido**, cada copia puede tener el historial completo del proyecto

Video sugerido:

- [Introducción al Control de Versiones](https://www.youtube.com/watch?v=BXbMBMlOkT4)

Después de verlo, responder rápido:

1. ¿Qué otros sistemas de control de versiones se mencionan además de Git?
2. ¿Qué diferencia hay entre un sistema centralizado y uno distribuido?
3. ¿Por qué Linux necesitaba algo más potente que un VCS centralizado tradicional?

## Consigna para cada grupo

1. Investigar el hito asignado respondiendo las 3 preguntas guía.
2. Preparar una explicación de 2 minutos para el resto de la clase.
3. Explicar cómo ese hito conecta con el anterior y con el siguiente.
4. Subir lo investigado a la carpeta compartida del **Eje 1** como evidencia de trabajo.

Cada grupo debe cerrar su exposición con esta frase:

```text
Nuestro hito fue importante porque...
```

## Evidencia de trabajo

Cada grupo debe entregar en la carpeta compartida del **Eje 1** un archivo con lo investigado.

El archivo puede ser:

- un documento de Google Docs
- un archivo Markdown (`.md`)
- un PDF exportado desde el documento

Nombre sugerido:

```text
1-6c_linea_tiempo_grupo_NOMBRE_DEL_HITO_APELLIDOS
```

El archivo debe incluir:

- integrantes del grupo
- hito asignado
- respuestas a las 3 preguntas guía
- conexión con el hito anterior
- conexión con el hito siguiente
- fuentes consultadas
- una frase final: `Nuestro hito fue importante porque...`

## Hitos y preguntas guía

### Grupo 1: 1969 - Unix, Bell Labs

1. ¿Qué problema resolvía Unix en 1969? ¿Por qué fue revolucionario para las universidades?
2. ¿Quiénes fueron Ken Thompson y Dennis Ritchie? ¿Qué rol tuvo el lenguaje C?
3. ¿Cómo se compartía Unix al principio? ¿Por qué eso generó una "cultura hacker"?

### Grupo 2: 1983 - Proyecto GNU, Richard Stallman

1. ¿Qué pasó cuando AT&T privatizó Unix? ¿Por qué Stallman se enojó?
2. ¿Qué significa "GNU's Not Unix"? ¿Por qué eligió ese nombre?
3. ¿Cuáles son las 4 libertades del software libre? Explicarlas con palabras propias.

### Grupo 3: 1985 - Manifiesto GNU y Free Software Foundation

1. ¿Qué pedía el Manifiesto GNU? ¿A quién estaba dirigido?
2. ¿Para qué se creó la FSF? ¿Qué diferencia hay entre "free software" y "software gratis"?
3. ¿Qué herramientas importantes creó GNU antes de 1991? Nombrar 3.

### Grupo 4: 1987 - Minix, Andrew Tanenbaum

1. ¿Qué es Minix y por qué se creó? ¿Por qué Linus Torvalds lo usaba?
2. ¿Qué limitación tenía Minix que frustró a Linus? ¿Por qué no lo podía modificar libremente?
3. ¿Qué discusión famosa tuvieron Tanenbaum y Torvalds? Buscar "Tanenbaum-Torvalds debate".

### Grupo 5: 1991 - Kernel Linux, Linus Torvalds

1. ¿Qué le faltaba al proyecto GNU en 1991? ¿Qué era Hurd y qué problema tenía?
2. ¿Por qué Linus dijo "solo es un hobby, no será grande como GNU"? ¿Se equivocó?
3. ¿Qué es un kernel y por qué Linux + GNU forman un sistema operativo completo? Usar una analogía.

### Grupo 6: 1991 - Licencia GPL v2

1. ¿Qué es la GPL y por qué es importante para Linux y GNU?
2. ¿Qué significa "copyleft"? ¿En qué se diferencia de "copyright"?
3. ¿Por qué Linus eligió la GPL v2 para Linux? ¿Qué garantizaba?

### Grupo 7: 1998 - Open Source vs Free Software

1. ¿Por qué en 1998 se inventó el término "Open Source"? ¿Qué problema tenía "Free Software"?
2. ¿Qué diferencias filosóficas hay entre la FSF y la OSI? ¿Quiénes lideraban cada una?
3. ¿Esto ayudó o dividió a la comunidad? Justificar.

### Grupo 8: 2002 - Linux adopta BitKeeper

1. ¿Cómo coordinaban el código de Linux antes de 2002? ¿Qué son los "parches por mail"?
2. ¿Qué es un sistema de control de versiones? ¿Por qué Linux lo necesitaba en 2002?
3. ¿Por qué BitKeeper era polémico? ¿Qué condición puso la empresa?

### Grupo 9: 2005 - Nace Git, Linus Torvalds

1. ¿Qué pasó en abril de 2005 con BitKeeper? ¿Por qué Linux se quedó sin herramienta?
2. ¿Qué objetivos de diseño tenía Git? Nombrar 3: velocidad, trabajo distribuido, integridad, ramas, etc.
3. ¿Por qué Linus lo programó tan rápido? ¿Qué necesitaba resolver urgente?

## Puesta en común

Mientras cada grupo expone, el resto completa una línea de tiempo general.

| Año | Hito | Problema que resolvía | Conexión con Git |
|---|---|---|---|
| 1969 | Unix | | |
| 1983 | GNU | | |
| 1985 | FSF | | |
| 1987 | Minix | | |
| 1991 | Linux | | |
| 1991 | GPL v2 | | |
| 1998 | Open Source | | |
| 2002 | BitKeeper | | |
| 2005 | Git | | |

## Cierre: la película completa

En 1991, Linus Torvalds comenzó el desarrollo del kernel Linux. Con el tiempo, Linux pasó de ser un proyecto personal a convertirse en un proyecto enorme, usado en servidores, sistemas operativos, celulares y muchos dispositivos.

Ese crecimiento trajo un problema técnico y organizativo: muchas personas de distintas partes del mundo enviaban cambios al mismo proyecto. Hacía falta revisar aportes, ordenar versiones, saber quién modificaba qué y mantener una historia confiable del código.

Git fue creado por Linus Torvalds en **2005** para gestionar el desarrollo del kernel Linux. La idea era contar con una herramienta rápida, distribuida y confiable para coordinar cambios en un proyecto de gran escala.

Responder entre todos:

1. ¿Qué parte de la historia muestra una necesidad técnica?
2. ¿Qué parte muestra una discusión ética o política sobre el software?
3. ¿Por qué un proyecto grande como Linux necesitaba un sistema de control de versiones?
4. ¿Qué problema concreto vino a resolver Git en 2005?

## Videos recomendados para cerrar la clase

1. [Cómo un Solo Developer Humilló a Toda la Industria con Git](https://www.youtube.com/watch?v=fi4YiZvbLXU&t)
   - Video histórico sobre el origen de Git y el problema que necesitaba resolver Linux.

2. [Historia de Linux y el Software Libre - Edutin Academy](https://www.youtube.com/watch?v=5Qj5n_8hUjs)
   - En español. Recorre desde Unix hasta el software libre.

3. [How Git Was Born - Linus Torvalds](https://www.youtube.com/watch?v=4XpnKHJAok8)
   - Linus Torvalds cuenta el problema con BitKeeper y el nacimiento de Git. Activar subtítulos en español.

4. [A Brief History of Git - GitLab](https://www.youtube.com/watch?v=2o5RZiGIe38)
   - Video breve y visual sobre el origen de Git.

## Material extra para profundizar

- [Manifiesto GNU original](https://www.gnu.org/gnu/manifesto.html)
- Libro: *Just for Fun*, de Linus Torvalds
- Documental: *Revolution OS*
- Documental: *The Code: Story of Linux*

## Próximo paso

Después de reconstruir esta historia, el paso siguiente es instalar Git y usarlo localmente.

Ahí vamos a pasar de la pregunta histórica:

> ¿por qué hizo falta Git?

a la pregunta práctica:

> ¿cómo uso Git para guardar versiones de mi propio proyecto?
