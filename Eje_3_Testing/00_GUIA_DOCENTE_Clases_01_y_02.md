# Guía docente — Clases 1 y 2

Este documento acompaña las dos primeras clases del Eje 3. Las guías numeradas están redactadas para que los estudiantes puedan seguirlas desde GitHub.

## Propósito de la secuencia

La entrada al eje se realiza desde una experiencia práctica:

1. explorar un producto;
2. detectar un comportamiento inesperado;
3. documentarlo;
4. intentar reproducirlo;
5. introducir requisitos y casos de prueba;
6. distinguir testing de depuración.

No es necesario desarrollar todavía SDLC, STLC ni todos los tipos de prueba.

---

## Clase 1 — Distribución sugerida

| Momento | Tiempo |
|---|---:|
| Recuperación de experiencias previas | 8 min |
| AcademyBugs individual | 20 min |
| Video y conversación | 10 min |
| Conceptualización | 10 min |
| Reporte individual | 15 min |
| Reproducción entre compañeros | 12 min |
| Cierre | 5 min |

### Video principal

[Introducción: qué es un QA y por qué es importante en el equipo](https://www.youtube.com/watch?v=4rvwQtl8E8A)

Conviene proyectarlo después del primer desafío. De esa manera, el video ayuda a poner nombre a una experiencia que los estudiantes ya realizaron.

### Alternativa breve

[Testing en 5 minutos — presentación del canal](https://www.youtube.com/watch?v=b4O3TNwPgIM)

### Intervenciones útiles

- “¿Cómo sabés que eso debería funcionar de otra manera?”
- “¿Podés repetirlo?”
- “¿Le ocurre a otra persona?”
- “¿Qué dato necesitaría un desarrollador para investigarlo?”
- “¿Es un defecto o una preferencia personal?”

---

## Clase 2 — Distribución sugerida

| Momento | Tiempo |
|---|---:|
| Revisión de reportes | 8 min |
| Requisito y caso de prueba | 10 min |
| Preparación técnica | 7 min |
| Diseño previo | 15 min |
| Ejecución | 20 min |
| Reproducción en parejas | 10 min |
| Hipótesis sobre el código | 5 min |
| Cierre | 5 min |

### Fallas intencionales del programa — no mostrar antes de la práctica

- suma realiza una resta;
- promedio falla ante una lista vacía;
- factorial no rechaza negativos;
- convertir_a_mayusculas utiliza lower;
- buscar_elemento devuelve el primer elemento en lugar de verdadero o falso.

El factorial funciona correctamente para cero y enteros positivos. Esto permite conversar sobre una función que puede pasar varios casos normales y fallar solamente ante una entrada no contemplada.

---

## Registro diagnóstico rápido

Asignar 0, 1 o 2 puntos solamente como registro docente.

| Indicador | 0 | 1 | 2 |
|---|---|---|---|
| Explora diferentes alternativas | No lo hace | Con ayuda | Autónomamente |
| Define el resultado esperado | No | Parcialmente | Con claridad |
| Registra pasos reproducibles | No | Incompletos | Claros |
| Aporta evidencia | No | Insuficiente | Suficiente |
| Colabora sin anular al compañero | No | Irregular | Sí |

Sugerencia: registrar entre cinco y ocho estudiantes por momento de circulación y completar la grilla durante las dos clases.

## Evidencias a conservar

- ticket de salida de la clase 1;
- reporte individual revisado por un compañero;
- tabla de casos de prueba de la clase 2;
- hipótesis sobre la causa de una falla.

Estas producciones sirven como diagnóstico inicial y como punto de comparación para actividades posteriores de testing automatizado.
