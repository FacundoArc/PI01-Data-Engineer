<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **PROYECTO INDIVIDUAL Nº1 </br> Facundo Gabriel Arce** </h1>

# <h1 align=center>**`Data Engineering`**</h1>
  

<hr>  

## **Introducción**
Mi nombre es Facundo Gabriel Arce y me encuentro en la etapa de Labs de la carrera de Data Science en SoyHenry. 

En este primer proyecto se nos pidio un trabajo de Ingeniería de Datos, donde se nos compartió cuatro datasets que contienen información sobre las plataformas de streaming de 'Amazon', 'Disney Plus', 'Hulu' y 'Netflix'. Se nos pidió realizar un Analisis Exploratorio de Datos (EDA) y procesos de Extracción,Transformación y Cargado de datos (ETL) para poder retirar imperfecciones e información irrelevante con el objetivo de realizar consultas específicas sobre estos datos para luego, con la utilización de tecnologías como FASTAPI y DETA, poder realizar el deploy de la aplicación.


## **Objetivo Principal**
Se busco simular el entorno de trabajo de un Ingeniero de Datos, realizando tareas propias de dicha posición. Tener en cuenta criterio propias a la hora de realizar el Análisis Exploratorio de Datos(EDA) y que herramientas utilizar para esta tarea. Se buscó el desarrollo de habilidades de ordenamiento, código limpio y comentado para un resultado prolijo y de eficiencia en los tiempos propuestos para su presentación. También se tuvo en cuenta el aprendizaje de otras herramientas como FASTAPI Y DETA para el deployment de la apliación.

## **Trabajo Realizado**
Se realizaron este tipo de transformaciones de datos unicamente:

    - Generar campo **`id`**: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = **`as123`**)

    - Los valores nulos del campo rating deberán reemplazarse por el string “**`G`**” (corresponde al maturity rating: “general for all audiences”

    - De haber fechas, deberán tener el formato **`AAAA-mm-dd`**

    - Los campos de texto deberán estar en **minúsculas**, sin excepciones

    - El campo ***duration*** debe convertirse en dos campos: **`duration_int`** y **`duration_type`**. El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas)

Y posteriormente se realizaron consultas que respondieran a información especifica que sera util para el Analista de datos:

    - Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma.Request: get_word_count()

    - Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año. Request get_score_count()

    - La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos. Request get_second_score()

    - Película que más duró según año, plataforma y tipo de duración. Request get_longest()

    - Cantidad de series y películas por rating. Request get_rating_count()
<br/>

## **Contenido de Repositorio** ##
La raiz del repositorio se encuentra conformada por las consignas propuestas para el trabajo.
En la carpeta App se encuentran los datasets analizados de las plataformas de AMAZON PRIME - HULU - NETFLIX - DISNEY PLUS unidos a un solo archivo CSV; y  el archivo main.py, que es donde se configura FastAPI y se colocan los decoradores de la API. Tambien se encuentra el archivo requirements.txt donde se anotan las dependencias para poder realizar el deployment con Deta.
En la carpeta Datasets se encuentra el archivo etl.py donde se esta todo el proceso de ETL comentado. 

## **Herramientas Utilizadas** ##
<ol>
<l>- Python</l><br>
<l>- Pandas</l><br>
<l>- FastApi</l><br>
<l>- Deta</l><br>
</ol>



