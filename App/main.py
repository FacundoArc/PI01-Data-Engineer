
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import pandas as pd

# INSTANCIAMOS LA APP
app= FastAPI()


#IMPORTACION DE CSV CON LAS BASES DE DATOS 
dbtotal = pd.read_csv('database_plataformas.csv', engine='python', decimal='.')


#RESPUESTA HTML PARA UTLIZAR LA API

@app.get("/",response_class=HTMLResponse)
async def index():
    return """<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HENRY Data Science - Proyecto Individual Data Engineer</title>
</head>
<body style="background-color: rgba(131, 172, 233, 0.673);">
    <br>
    <h2 style="font-family: Calibri Light; color: rgba(3, 43, 103, 0.673);margin:'auto';text-align: center;">API con información de series y películas en las plataformas de Amazon, Disney+, Hulu y Netflix</h2>
    <h3 style="font-family: Calibri Light; color: rgba(0, 80, 199, 0.673);text-align: center;">Cómo hacer las consultas:<br>
    Es necesario colocar la función correspondiente a la que se deseé consultar en la url, por ej; 'https://gepgq1.deta.dev/get_word_count/Netflix/love'
    </h3>
    <br>
    <h3 style="font-family: Calibri Light; color: #333961;text-align: center;">1) Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma:</h3>
    <h5 style='text-align: center;'>Colocar parametro PLATAFORMA que empiece en mayúscula y parametro KEYWORD en minúscula.</h3>
    <h5 style="font-family: Calibri Light;text-align: center;">/get_word_count/PLATAFORMA/KEYWORD</h5>
    <h5 style="font-family: Calibri Light;text-align: center;">Por ej: /get_word_count/Netflix/love</h5>
    <br>

    <h3 style="font-family: Calibri Light; color: #333961;text-align: center;">2) Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año:</h3>
    <h5 style='text-align: center;'>Colocar parametro PLATAFORMA que empiece en mayúscula' y parametro XX y AÑO como un numero. </h3>
    <h5 style="font-family: Calibri Light;text-align: center;">/get_score_count/PLATAFORMA/XX(Puntaje)/AÑO</h5>
    <h5 style="font-family: Calibri Light;text-align: center;">Por ej: /get_score_count/Netflix/85/2010</h5>
    <br>

    <h3 style="font-family: Calibri Light;text-align: center; color: #333961">3) La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos :</h3>
    <h5 style= "text-align: center;">Colocar parametro PLATAFORMA que empiece en mayúscula.</h5>
    <h5 style="font-family: Calibri Light;text-align: center;">/get_second_score/PLATAFORMA</h5>
    <h5 style="font-family: Calibri Light;text-align: center;">Por ej: /get_second_score/Amazon</h5>
    <br>

    <h3 style="font-family: Calibri Light;text-align: center; color: #333961">4) Película que más duró según año, plataforma y tipo de duración:</h3>
    <h5 style='text-align: center;'>Colocar parametro PLATAFORMA que empiece en mayúscula ,el parametro TIPO_DURACIÓN en minúscula (peliculas: min - tv shows: season) y AÑO como un número.</h3>
    <h5 style="font-family: Calibri Light;text-align: center;">/get_longest/PLATAFORMA/TIPO_DURACION/AÑO</h5>
    <h5 style="font-family: Calibri Light;text-align: center;">Por ej: /get_longest/Netflix/min/2016</h5>
    <br>

    <h3 style="font-family: Calibri Light;text-align: center; color: #333961">5) Cantidad de series y películas por rating:</h3>
    <h5 style='text-align: center;'>Colocar parametro RATING en minúscula.'</h3>
    <h5 style="font-family: Calibri Light;text-align: center;">/get_rating_count/RATING</h5>
    <h5 style="font-family: Calibri Light;text-align: center;">Por ej: /get_rating_count/18+</h5>
    <br>
    <br>
    
</body>
</html>"""


#Decorador de la primera consulta.Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma
@app.get("/get_word_count/{plataforma}/{keyword}")
def get_word_count(plataforma,keyword):
    lista_plataforma = ['Amazon','Disney','Hulu','Netflix']
    if plataforma in lista_plataforma:
        consulta_1 = dbtotal[['Titulo','Plataforma']]
        filt = consulta_1[consulta_1['Plataforma'] == plataforma]
        resultado1 = filt['Titulo'].str.contains(keyword).sum()
        return (f'La palabra: "{keyword}" se repite una cantidad de: - {resultado1} - veces en la Plataforma: {plataforma}')
    else:
        return (f'Los parámetros ingresados son incorrectos. Probar de Nuevo')
    

# Decorador segunda consulta.Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año
@app.get("/get_score_count/{plataforma}/{xx}/{anio}")
def get_score_count(plataforma:str, xx:int, anio:int):
    consulta_2= dbtotal[["Plataforma","Anio_estreno","score"]]
    resultado = consulta_2[(consulta_2['Plataforma']== plataforma)&(consulta_2['Anio_estreno']== anio)&(consulta_2['score']> xx)]
    cantidad = len(resultado.index)
    return (f'La cantidad de peliculas de la Plataforma: {plataforma}, con puntaje mayor a - {xx} - en el año {anio} es de: {cantidad} peliculas')


# Decorador tercer consulta. La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.
@app.get("/get_second_score/{plataforma}")
def get_second_score(plataforma):
    consulta_3 = dbtotal[['Titulo','Plataforma','score','Tipo',]]
    consulta_3 = consulta_3[consulta_3.Tipo != 'tv show']
    resultado = consulta_3[(consulta_3['Plataforma'] == plataforma)]
    resultado = resultado[['Titulo','score']]
    resultado = resultado.sort_values(['score','Titulo'],ascending=[False,True])
    titulo = resultado['Titulo'].iloc[1]
    score = resultado['score'].iloc[1]
    return (f'La Segunda pelicula con mayor score de la Plataforma: {plataforma} , es {titulo} con un score de: {score}')
    

# Decorador cuarta consulta. Película que más duró según año, plataforma y tipo de duración
@app.get("/get_longest/{plataforma}/{tipo}/{anio}")
def get_longest(plataforma,tipo,anio):
    anio = int(anio)
    lista_plataforma = ['Amazon','Disney','Hulu','Netflix']
    lista_tipo = ['min']
    if (plataforma in lista_plataforma) and (tipo in lista_tipo) and (anio in range(dbtotal.Anio_estreno.min(),dbtotal.Anio_estreno.max()+1)):
        df_d = dbtotal[['Plataforma','Titulo','Anio_estreno','Tipo','duration_int','duration_type']]
        df_d =df_d[df_d.Tipo != 'tv show']
        df_d = df_d[(df_d['Plataforma'] == plataforma)&(df_d['Anio_estreno'] == anio)]
        resultado4 = df_d.sort_values('duration_int',ascending=False)
        resultado4=resultado4[['Titulo','duration_int','duration_type']].iloc[0]
        longest = resultado4['Titulo']
        longest_time = resultado4['duration_int']
        longest_time_type = resultado4['duration_type']
        
        return (f'La pelicula mas larga de la Plataforma: "{plataforma}" es "{longest}" con una duracion de {longest_time} {longest_time_type}')
        
    else:
        return (f'Parametros incorrectos.Probar de Nuevo')

#Decorador de la quinta consulta. Cantidad de series y películas por rating
@app.get("/get_rating_count/{rating}")
def get_rating_count(rating):
    consulta_5 = dbtotal[['rating']]
    resultado_5 = len(consulta_5[(consulta_5['rating']== rating)])
    
    return (f'Hay un total de: {resultado_5} peliculas/series con Rating: {rating} ')


