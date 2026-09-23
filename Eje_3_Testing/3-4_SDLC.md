# 3-4 SDLC, testing e IA

## Pregunta guía

¿Qué hace un tester dentro de una empresa y qué cambia cuando una IA puede ayudarlo?

## Propósitos

- Relacionar la película con la organización de una empresa de software.
- Presentar las etapas del ciclo de vida del software.
- Comprender el rol del testing dentro del SDLC.
- Analizar cómo puede colaborar la IA en algunas tareas.
- Diferenciar entre buscar información y comprender qué significa.

## 1. Cierre grupal de la película

Recuperar con los estudiantes los problemas de organización observados en la película.

Preguntas orientadoras:

- ¿Qué problemas aparecen cuando no está claro quién decide?
- ¿Quién comunica los problemas?
- ¿Qué consecuencias tiene la falta de organización?
- ¿Qué roles aparecen en la empresa?
- ¿Qué relación podemos establecer con una empresa de software?

## 2. Las etapas del desarrollo de SW como parte del análisis

### Del trabajo de la empresa al Desarrollo de SW 

La actividad sobre la empresa permite introducir una idea importante: generalmente las etapas del desarrollo de SW no las realiza una sola persona. El producto avanza porque distintas personas aportan información, toman decisiones, construyen, prueban y comunican.

| Quién participa | Qué aporta al producto |
| --- | --- |
| Cliente o responsable del negocio | Explica la necesidad y confirma las reglas que debe cumplir el sistema. |
| Analista o responsable de requisitos | Hace preguntas, aclara ambigüedades y transforma la necesidad en requisitos comprobables. |
| Programador | Diseña y construye una solución que cumpla esos requisitos. |
| Testing / QA | Comprueba el comportamiento, registra diferencias y comunica evidencia para que el equipo pueda actuar. |
| Responsable de producto o proyecto | Ayuda a ordenar prioridades y coordinar decisiones, según la organización. |

En la película, Tom puede servir como ejemplo de una persona que conecta a clientes con quienes desarrollan. Observar que **si la información llega incompleta o nadie responde a un problema, el trabajo del resto se complica**.

#### SDLC significa:

**Software Development Life Cycle** 

En español: _ciclo de vida del desarrollo de software_.

Es el conjunto de etapas por las que pasa un producto de software.

Presentar este recorrido:

```text
Planificación → Análisis → Diseño → Desarrollo → Testing → Publicación → Mantenimiento
```

- **Planificación:** decidir qué problema se quiere resolver.
- **Análisis:** conocer las necesidades del cliente y de los usuarios.
- **Diseño:** pensar cómo funcionará el producto.
- **Desarrollo:** construir el software.
- **Testing:** probarlo y buscar errores.
- **Publicación:** ponerlo a disposición de los usuarios.
- **Mantenimiento:** corregir, actualizar y mejorar.

Estas etapas no siempre ocurren una sola vez ni de manera estrictamente lineal. En muchos proyectos se repiten y se superponen.

### ¿Siempre se recorre de la misma manera?

No. El SDLC describe **qué cosas hay que hacer**; el modelo de trabajo describe **cómo se organizan**.

- **Cascada:** las etapas se realizan principalmente en secuencia. Primero se definen los requisitos, después se diseña y se desarrolla, y el testing suele concentrarse más adelante. Funciona mejor cuando las necesidades están bastante claras y cambiar resulta costoso.
- **Ágil:** el trabajo se divide en ciclos breves. En cada ciclo se analiza, diseña, desarrolla y prueba una parte del producto para obtener devoluciones y ajustar lo siguiente.
  - **Scrum:** es una manera concreta de organizar un trabajo ágil mediante ciclos llamados *sprints*. El equipo elige qué hará, construye un incremento, lo prueba, recibe comentarios y revisa cómo trabajar mejor en el ciclo siguiente.

La idea importante para testing es esta: **en cascada puede parecer una etapa posterior; en un trabajo ágil participa en cada ciclo y también desde el análisis de los requisitos**. En ambos casos, testing no consiste únicamente en “probar al final”: ayuda a detectar problemas antes de publicar y aporta información para decidir.

Por ejemplo, para el caso de la boletería de la clase 3-2: 

| Si el equipo trabaja... | Una situación posible en la boletería |
| --- | --- |
| En cascada | Define todos los precios y reglas, desarrolla el sistema completo y después realiza una tanda amplia de pruebas. |
| De forma ágil | En un ciclo construye el cálculo por edad, lo prueba y recoge observaciones antes de continuar con descuentos e ingreso. |

## 3. Video sobre SDLC

[Etapas del ciclo de vida del software en 4 minutos](https://www.youtube.com/watch?v=2Jm9Vk5kCGw)

Antes del video, pedir que observen:

1. ¿Qué etapas reconocen?
2. ¿En qué etapas puede participar testing?

Después del video, conversar:

- ¿Testing aparece solamente al final?
- ¿Por qué conviene probar durante todo el desarrollo?
- ¿Qué etapas se pueden relacionar con situaciones de la película?

### Videos opcionales: metodología tradicional, Ágil y Scrum

Estos videos de Cristian Henao se pueden trabajar en este orden:

1. [¿Qué son las metodologías tradicionales en el desarrollo de software?](https://www.youtube.com/watch?v=i8CPD1dW88k) — para reconocer el enfoque secuencial y el modelo Cascada.
2. [¿Qué son las metodologías ágiles en el desarrollo de software?](https://www.youtube.com/watch?v=fHKsufzM7qQ) — para presentar Ágil como enfoque general: ciclos breves, adaptación y entregas incrementales.
3. [Scrum en 6 minutos | Metodologías Ágiles](https://www.youtube.com/watch?v=HhC75IonpOU) — para observar Scrum como una forma concreta de organizar un trabajo ágil mediante ciclos, roles y actividades.

La relación que interesa dejar clara es: **Ágil es el enfoque general; Scrum es un marco de trabajo ágil**. No son dos alternativas del mismo nivel.

No es necesario verlos completos ni estudiar todas las definiciones. Después de los videos, pedir que respondan:

- ¿Cómo se organiza el trabajo?
- ¿Cuándo puede participar testing?
- ¿Qué ocurre si cambian los requisitos?

## 4. Video sobre el rol del tester

[¿Cómo ser TESTER DE SOFTWARE? SUELDOS EN TESTING QA?](https://www.youtube.com/watch?v=qJyZEE1c-Tg)

Conviene usar solo el tramo inicial, hasta la parte sobre IA y tareas del tester; la sección sobre sueldos no aporta a esta clase.

Durante el video, registrar:

- ¿Qué tareas realiza un tester?
- ¿Qué habilidades necesita?
- ¿Es necesario saber programar?
- ¿Qué tareas podría acelerar una IA?
- ¿Qué decisiones siguen dependiendo del criterio humano?

## 5. Trabajo grupal: analizar una etapa

Después de los videos, cada grupo recibe una etapa del SDLC:

- Planificación
- Análisis
- Diseño
- Desarrollo
- Testing
- Publicación
- Mantenimiento

Cada grupo debe responder:

1. ¿Qué se hace en esta etapa?
2. ¿Qué personas o roles pueden participar?
3. ¿Qué problema podría ocurrir si esta etapa se realiza mal?
4. ¿Cómo se relaciona con alguna situación de la película?
5. ¿Qué relación tiene con el testing?

Cada grupo prepara una explicación breve, de aproximadamente dos minutos.

## 6. Puesta en común

Cada grupo presenta su etapa.

Mientras exponen, completar entre todos:

```text
Problema o necesidad
        ↓
Planificación y análisis
        ↓
Diseño y desarrollo
        ↓
Testing
        ↓
Publicación
        ↓
Mantenimiento y mejoras
```

## 7. Conversación final sobre IA

Presentar la siguiente idea:

> Una IA puede analizar mucha información rápidamente, pero no decide por sí sola qué significa un resultado ni qué problema es más importante.

Preguntas:

- ¿La IA reemplaza al tester?
- ¿Qué tareas puede hacer más rápido?
- ¿Qué debe seguir comprobando una persona?
- ¿Por qué no conviene confiar ciegamente en una respuesta de la IA?

## Criterios de evaluación

Se observará si los estudiantes pueden:

- relacionar la película con la organización de una empresa;
- explicar una etapa del SDLC;
- identificar roles y responsabilidades;
- comprender la función del testing;
- relacionar la IA con tareas concretas;
- comunicar una conclusión con claridad.
