# -*- coding: utf-8 -*-
# =============================================================================
# Cosas necesarias
# =============================================================================

# =============================================================================
# Usar esta línea de código para instalar en forma de pip la librería necesaria
# y luego comentarla para no tener problemas
# =============================================================================
#
# pip install snscrape 
# pip install emoji
# =============================================================================


import snscrape.modules.twitter as sntwitter
import pandas as pd
import re
import emoji
from collections import Counter
# =============================================================================
# Limpieza de corpus
# =============================================================================
##generamos una def para eliminar los puntos
def remover_puntuacion1(s):
    ##cada uno de los items que aparecen en esta lista
    lista_puntuaciones = '!"$%&\'()*+,-;<=>?[\\^]`{|}~'
    for c in lista_puntuaciones:
        ##es eliminado del texto reemplazandolo por un espacio vacÃ­o
        s=s.replace(c,"")
        ##lo mismo se hace con "\t"
        s=s.replace('\t','')
    return s

def remover_puntuacion2(s):
    ##cada uno de los items que aparecen en esta lista
    lista_puntuaciones = '!"#$%&\'()*+,-./:;<=>?\\^_`{|}~'
    for c in lista_puntuaciones:
        ##es eliminado del texto reemplazandolo por un espacio vacÃ­o
        s=s.replace(c,"")
        ##lo mismo se hace con "\t"
        s=s.replace('\t','')
    return s
##Ãºltima def de preparacion
def remover_numeros(k):
    ##por cada item dentro de la lusta numeros
    for z in str(list(range(100))):
        ##reemplazamos elitem de la lista con un vacÃ­o
        k=k.replace(z," ")
        ##tambiÃ©n eliminamos la palabra "pag", usada para marcar pÃ¡ginas junto con lo anterior
        k=k.replace('pag','')
    return k
# =============================================================================
# Fechas
# =============================================================================
# =============================================================================
# cambiar las fechas libremente
base = list(pd.date_range(start="2022-07-01",end="2022-09-04")) #se usa formato de fechas en una lista previa porque funciona mejor en la librería
fechas = [str(item)[0:10] for item in base] #las convierte en string en vez de fechas porque queremos quedarnos con el formato más no el atributo
# =============================================================================
# =============================================================================
# Rechazo
# =============================================================================
# =============================================================================
attributes_container = [] #definimos una lista previa
for numero in list(range(0,66)): #Este ciclo for lo que hace es permitirnos llamar las fechas por el índice y no por la fecha, ya que las convertimos en string
    # este for asigna un valor (i) a cada tweet de esta forma en el ciclo if de abajo si le pedimos 20 tweets extrae solo 20 por día y el tweet se extrae mediante una class
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper('rechazo since:'+str(fechas[numero])+' until:'+str(fechas[numero+1])).get_items()):#el enumerate es el que permite contar el i, mientras que ponemos al fecha que queremos y le ponemos como límite la que viene inmediatamente después
        #cambiar el número libremente para cambiar la cantidad de tweets por día
        if i > 2: 
            break
        #esta linea es para que no hayan duplicados(y eliminar los bots)
        if tweet.content not in attributes_container:
            #añadimos a la lista previa solamente los elementos que queramos extraer de cada tweet
            attributes_container.append([tweet.user.username,tweet.user.verified, tweet.user.description, tweet.date, tweet.content, tweet.hashtags])
            #para saber que cosas podemos extraer usar el comando dir(tweet) en caso de querer saber que podemos sacar de cada tweet y dir(tweet.user) para saber que podemos sacar de cada usuario

# creamos un data_frame con los datos que extraímos, esto se puede cambiar dependiendo de lo que quieras sacar
tweets_df = pd.DataFrame(attributes_container, columns=["Usuario","Verificado","Descripcion_cuenta", "Fecha", "Tweet", "Hashtag"])
# pasamos el df a un csv
tweets_df.to_csv("Tweets/tweets.csv", sep=';' ,index=True)
# =============================================================================
