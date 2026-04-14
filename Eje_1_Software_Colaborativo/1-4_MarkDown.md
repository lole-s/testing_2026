# MARKDOWN

Markdown es una forma de escribir contenido para la web. Está escrito en lo que los más “geeks” nos gusta llamar “texto plano”, que es exactamente la clase de texto que utilizas para escribir y ver. El texto plano es simplemente el alfabeto normal, con unos cuantos símbolos que son familiares, como los asteriscos ( * ) o comillas simples ( ` ).

A diferencia de las incómodas aplicaciones de procesadores de texto, el texto escrito en Markdown puede ser fácilmente compartido entre diferentes equipos, dispositivos móviles y personas. Se está convirtiendo rápidamente en el estándar para escritos de académicos, científicos, escritores, y muchas más. Sitios web como GitHub o reddit utilizan Markdown para dar formato a sus comentarios.

Dar formato a textos mediante Markdown tiene una curva de aprendizaje suave. No realiza cosas espectaculares como cambiar el tamaño de la fuente, el color o el tipo. Todo sobre lo que se tiene el control es sobre cómo se muestra el texto, haciendo cosas como marcar texto en negrita, crear encabezados u organizar listas de elementos.


Video link: [¿Por qué debes aprender MARKDOWN? MoureDev by Brias Moure](https://www.youtube.com/watch?v=77Ggk1uzO2A)


* **Markdown Tutorial:**
    * Este sitio web ofrece un tutorial interactivo que te guía a través de los conceptos básicos de Markdown con ejercicios prácticos. Ideal para principiantes.
    * Enlace: [Markdown Tutorial](https://www.markdowntutorial.com/es/)
* **Editores Markdown Online:**
    
    * [Dillinger](https://dillinger.io/)

    * [Editor Markdown Online](https://editormarkdown.com/)
    
    * [StackEdit – In-browser Markdown editor](https://stackedit.io/)

 
* **Curso: EDteam - Markdown desde cero (Gratis):**
    * Este curso gratuito te enseña Markdown desde los conceptos básicos hasta temas más avanzados.
    * Enlace: [Curso: Markdown desde cero (Gratis) - EDteam](https://ed.team/cursos/markdown)
  
    ![MarkDown <--> HTML5](../img/3f4ce142-f8f4-4d41-923c-64ce9fbabf59.png)

* **Notas 4Geeks.com sobre el uso de MarkDown y las IA:**
    * En un mundo donde la eficiencia y la creatividad son esenciales, combinar inteligencia artificial y Markdown podría ser el truco definitivo para crear documentos profesionales y versátiles en poco tiempo.
    * Enlace: (https://4geeks.com/es/lesson/httpsgithubcombreatheco-deapplied-ai-syllabusblobmaincontentmodule-5-documentsfrom-markdown-to-everythingesmd)
  
* ## **Ejercicio 1: Instrucciones para crear y compartir un archivo con formato Markdown**
  
1.  **Abre Dillinger.io:**
    * Ve a [Dillinger.io](https://dillinger.io/) en tu navegador.

2.  **Crea un nuevo documento:**
    * Crea un nuevo documento y guárdalo como `Testing-markdown.md`.

3.  **Añade el título principal:**
    * Usa `#` para crear un encabezado de nivel 1: "Testing - Uso de MarkDown".

4.  **Añade un resumen en cursiva:**
    * Escribe una breve descripción del documento y usa `*` para ponerla en cursiva. Por ejemplo: "*Este documento demuestra el uso de Markdown con ejemplos de tablas y código Python.*"

5.  **Añade un título de nivel 2 para la tabla:**
    * Usa `##` para crear un título de nivel 2: "Tabla".

6.  **Crea una tabla con datos de ejemplo:**
    * Crea una tabla con 3 columnas y 3 filas.
    * Ejemplo de contenido:
        * Columna 1: Nombre, Columna 2: Edad, Columna 3: Ciudad.
        * Fila 1: Ana, 25, Madrid.
        * Fila 2: Juan, 30, Barcelona.
        * Fila 3: Luisa, 22, Sevilla.

7.  **Añade un encabezado de nivel 3 para el análisis de código:**
    * Usa `###` para crear un encabezado de nivel 3: "Análisis de Código en Python:".

8.  **Inserta un bloque de código Python más complejo:**
    * Usa ``` para crear un bloque de código.
    * Escribe el siguiente código Python.

    ```python

    import random

    def mi_fun():
        
        personajes = ["un mago", "una princesa", "un dragón", "un astronauta"]
        lugares = ["un castillo", "el bosque", "el espacio", "una isla"]
        verbos = ["corrió", "voló", "luchó", "exploró"]
        adjetivos = ["mágico", "peligroso", "gigante", "misterioso"]

        personaje = random.choice(personajes)
        lugar = random.choice(lugares)
        verbo = random.choice(verbos)
        adjetivo = random.choice(adjetivos)

        texto = f"Había una vez {personaje} que {verbo} a través de {lugar} {adjetivo}."
        return texto

    print(mi_fun())
    ```

9.  **Añade una explicación del código en cursiva:**
    * Debajo del bloque de código, explica qué hace el código. Por ejemplo: "*Este código...bla bla bla *"

10. **Guardar en Drive y compartir el resultado:**
    * Descargar el archivo en formato Markdown y subirlo a tu carpeta de Drive `testing_APELLIDO/eje1_Software_Colaborativo`.

* ## **Ejercicio 2:**
  1. Pedirle a alguna de las IA generativas de tu agrado (ChatGPT, Copilot, DeepSeek, Gemini, etc.) que escriba un informe incluyendo tablas, enlaces y, si es posible, imágenes, sobre algún tema sobre el cual no tengas mucha idea.
        * Ej.:
          * Motor de 2 tiempos: historia, funcionamiento y actualidad.
          * Frutales: poda, cuidados y explotación intensiva.
          * Deportes extremos: adrenalina, riesgo y superación. 
          * El arte de la quesería artesanal: tradiciones, técnicas y variedades regionales
          * Pato, Deporte para pocos: Historia, reglas, actualidad
  2. Copiar la respuesta de la IA en formato Markdown y usar https://dillinger.io/ para crear un documento **PDF** sobre el tema seleccionado.
  3. Subir los documentos a la carpeta de Drive `testing_APELLIDO/eje1_Software_Colaborativo`.

* ## **Ejercicio 3: Edición de Markdown en Visual Studio Code**

1. **Abrir la carpeta del proyecto en VS Code:**
    * Abrir Visual Studio Code y luego la carpeta `testing_2026`.
    * Verificar que en el Explorador aparezca la carpeta `Eje_1_Software_Colaborativo`.

2. **Crear un archivo nuevo Markdown:**
    * Crear un archivo llamado `Testing-markdown-vsc.md`.
    * Guardarlo dentro de `Eje_1_Software_Colaborativo`.

3. **Usar primero lo que ya trae VS Code:**
    * No instalar extensiones al comenzar.
    * VS Code ya permite escribir archivos `.md` y abrir la vista previa sin instalar nada extra.
    * Solo si hace falta exportar directamente a PDF desde VS Code, instalar la extensión `Markdown PDF`.
    * Si alguna computadora del aula ya tiene otras extensiones para Markdown, se pueden usar, pero no son obligatorias para resolver este ejercicio.

4. **Abrir la vista previa del documento:**
    * Usar `Ctrl + Shift + V` para abrir la previsualización.
    * Luego usar la opción "Open Preview to the Side" para ver el código y el resultado al mismo tiempo.
    * Mientras escribís, revisar si el texto se ve claro, ordenado y fácil de leer.

5. **Escribir un apunte breve relacionado con la materia:**
    * Copiar esta estructura base y completarla:

    ```md
    # Apunte de Markdown para trabajo colaborativo

    **Nombre y apellido:** TU_NOMBRE
    **Curso:** 5to año

    ## Qué es Markdown

    Escribí 3 oraciones explicando con tus palabras qué es Markdown y por qué puede servir en una materia técnica.

    ## Para qué me puede servir en la materia

    Escribí 3 oraciones contando para qué lo usarías en clase.
    Por ejemplo: tomar apuntes, compartir consignas, ordenar información o escribir instrucciones para tu grupo.
    ```

6. **Practicar formato con contenido concreto:**
    * Debajo del título `## Para qué me puede servir en la materia`, agregar una lista con al menos 3 usos concretos. Deben ser parecidos a estos:
        * Escribir apuntes prolijos.
        * Compartir instrucciones con el grupo.
        * Organizar información de una actividad.
    * Agregar una checklist con al menos 3 tareas de un trabajo grupal. Ejemplo:
        * `- [ ] Buscar información`
        * `- [ ] Revisar ortografía del apunte`
        * `- [ ] Subir el archivo al Drive`
    * Agregar una cita usando `>` con una idea breve, por ejemplo:
        * `> Un buen apunte le ahorra tiempo a todo el equipo.`
    * Escribir una oración donde aparezca una palabra en **negrita** y otra en *cursiva*. Ejemplo:
        * `En un trabajo grupal es **importante** dejar instrucciones *claras* para los demás.`

7. **Agregar una tabla útil para la materia:**
    * Crear una tabla de 3 columnas con los títulos:
        * `Herramienta`
        * `Uso`
        * `Ejemplo`
    * Completar al menos 3 filas con información como esta:
        * VS Code | Escribir apuntes e informes | README del proyecto
        * Google Drive | Compartir archivos | Entrega del trabajo práctico
        * Markdown | Ordenar información | Resumen de clase o pasos de uso

8. **Insertar un enlace y una imagen:**
    * Agregar un enlace a una página relacionada con Markdown o VS Code.
    * Insertar una imagen con ruta relativa.
    * Puede ser una imagen de la carpeta `img` o una captura de pantalla hecha por vos donde se vea la vista previa de VS Code.

9. **Agregar un bloque de código corto:**
    * Insertar un bloque de código con lenguaje `bash`, `python` o `html`.
    * El ejemplo debe estar relacionado con organización de archivos o trabajo en clase. Por ejemplo:

    ```bash
    mkdir apuntes_grupo
    cd apuntes_grupo
    echo "Resumen de clase" > README.txt
    ```

    * Debajo del bloque, escribir una línea explicando para qué serviría ese código.

10. **Guardar y exportar el trabajo:**
    * Guardar el archivo `.md`.
    * Si la computadora tiene instalada la extensión `Markdown PDF`, usar la paleta de comandos y ejecutar `Markdown PDF: Export (pdf)`.
    * Si no está instalada, entregar el archivo `.md` y una captura donde se vea el editor junto con la vista previa.

11. **Entregar el resultado:**
    * Subir el archivo `Testing-markdown-vsc.md` a la carpeta del Drive `testing_APELLIDO/eje1_Software_Colaborativo`.
    * Si se pudo exportar, subir también la versión PDF.
    * Compartir una captura de pantalla donde se vea VS Code con el texto y la previsualización.
