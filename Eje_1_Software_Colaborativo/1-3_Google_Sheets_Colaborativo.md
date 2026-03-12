# 1-3 Google Sheets colaborativo

## Objetivo
Crear archivos en Google Sheets y trabajar en simultáneo y por turnos en un documento compartido.

## Teoría breve
Google Workspace incluye herramientas para trabajar en equipo. Usaremos **Google Drive** para guardar archivos y **Google Sheets** para planillas colaborativas.

## Videos recomendados
- [Google Workspace (intro)](https://www.youtube.com/watch?v=nb_sUdpAmf8)
- [Google Sheets (intro)](https://www.youtube.com/watch?v=RscxwCRQZbg)
- [Google Sheets (2)](https://www.youtube.com/watch?v=ydWtJsvcuvc)

## Actividad 1 (individual): Archivo personal
1. En Google Drive crear la carpeta `ProA2026`.
2. Dentro, crear la carpeta `Testing`.
3. Crear un archivo de Google Sheets llamado `testing2026_APELLIDO`.
4. En la hoja 1, crear la tabla con columnas: Fecha | Clase | Eje | Tema | Actividad.
5. Completar 5 filas con datos de ejemplo.

## Actividad 2 (individual): Recibo simple
1. En la mismo archivo `testing2026_APELLIDO`, crear una nueva hoja llamada `Recibo`.
2. Crear una tabla con estas columnas:
   - Cantidad | Producto | Precio U. | Subtotal
3. Completar 5 productos con cantidades y precios en pesos.
4. Calcular `Subtotal` con la fórmula: `=A2*C2` y arrastrar hacia abajo.
5. Debajo de la tabla, agregar:
   - `NETO TOTAL`: suma de los subtotales con `=SUM(D2:D6)`
   - `IVA (21%)`: `=D8*0.21`
   - `TOTAL`: `=D8+D9`

## Actividad 3 (grupal, archivo compartido entre 3)
1. Crear un archivo compartido llamado `testing2026_grupal`.
2. Compartirlo con 3 estudiantes (permiso de edición).
3. Cada estudiante trabaja en un horario distinto (turnos):
   - Turno A: 09:00 a 09:20
   - Turno B: 09:20 a 09:40
   - Turno C: 09:40 a 10:00

### Asignación de tareas (una por estudiante)
- Estudiante A: Hoja `Notas` (promedios)
- Estudiante B: Hoja `Grafica_Lineal`
- Estudiante C: Hoja `Grafica_Cuadratica`

### Detalle de tareas
**A) Hoja Notas**
1. Crear columnas: Nombre | Nota 1 | Nota 2 | Nota 3 | Nota 4 | Promedio.
2. Cargar 5 estudiantes.
3. Calcular promedio con `=AVERAGE(B2:E2)` o `=PROMEDIO(B2:E2)` y arrastrar.

**B) Hoja Grafica_Lineal**
1. Columna A: `X` con valores de -10 a 10.
2. Columna B: `Y` con la función `=3*A2-6`.
3. Graficar X vs Y (gráfico de líneas) y nombrarlo `Función lineal`.

**C) Hoja Grafica_Cuadratica**
1. Columna A: `X` con valores de -10 a 10.
2. Columna B: `Y` con la función `=A2^2-4`.
3. Graficar X vs Y (gráfico de líneas) y nombrarlo `Función cuadrática`.

## Práctica de funciones básicas (aplica a todas)
- Arrastrar y soltar para completar una serie (autorrelleno).
- Remarcar tabla o rango y aplicar bordes o color.
- Fijar la primera fila (Ver > Inmovilizar > 1 fila).

## Entrega
- Enlace del archivo individual y del archivo grupal.
- Captura donde se vean las hojas creadas y las gráficas.