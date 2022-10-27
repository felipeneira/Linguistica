#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# librerias
# =============================================================================
import snscrape.modules.twitter as sntwitter
import pandas as pd
import stanza
import re
import emoji
from collections import Counter
# =============================================================================
# 
# =============================================================================
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
# fechas
# =============================================================================
base = list(pd.date_range(start="2022-07-01",end="2022-09-04"))
fechas = [str(item)[0:10] for item in base]
# =============================================================================
# 
# =============================================================================
attributes_container = []
for numero in list(range(0,21)):
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper('#VamosLaU since:'+str(fechas[numero])+' until:'+str(fechas[numero+1])).get_items()):
        if i > 200:
            break
        if tweet.content not in attributes_container:
            attributes_container.append([tweet.user.username,tweet.user.verified, tweet.user.description, tweet.date, tweet.content, tweet.hashtags])

todo = pd.DataFrame(attributes_container, columns=["Usuario","Verificado","Descripcion_cuenta", "Fecha", "Tweet", "Hashtag"])
todo.to_csv("U.csv", sep=';' ,index=True)
# =============================================================================
# 
# =============================================================================
todo['Tweet'] = todo['Tweet'].apply(lambda x :remover_puntuacion1(x))
todo['Tweet'] = todo['Tweet'].apply(lambda x :re.sub("(\\@[\\w\\d\\_\\.]+)", "[etiqueta]", x))
todo['Tweet'] = todo['Tweet'].apply(lambda x :re.sub("(\\#[\\w\\d\\_\\.]+)", "[hashtag]", x))
todo['Tweet'] = todo['Tweet'].apply(lambda x :re.sub("\s(https:\/\/[\w\.\/\-]*)", "[URL]", x))
todo['Tweet'] = todo['Tweet'].apply(lambda x :emoji.demojize(x, delimiters=("[","]")))
etiquetas = list(todo['Tweet'].apply(lambda x :re.findall("(\[\w*\_*\d*\])",x)))
# =============================================================================
# 
# =============================================================================
todo['Tweet'] = todo['Tweet'].apply(lambda x :x.lower())
todo['Tweet'] = todo['Tweet'].apply(lambda x :remover_puntuacion2(x))
todo['Tweet'] = todo['Tweet'].apply(lambda x :x.replace("["," ["))
todo['Tweet'] = todo['Tweet'].apply(lambda x :x.replace("]","] "))
todo['Tweet'] = todo['Tweet'].apply(lambda x :x.replace("…"," "))
todo['Tweet'] = todo['Tweet'].apply(lambda x :x.replace("\n"," "))
todo['Tweet'] = todo['Tweet'].apply(lambda x :re.sub("\s+", " ",x))
todo['Palabras'] = todo['Tweet'].apply(lambda x :x.split(" "))

palabras = []
for tweet in todo['Palabras']:
    for palabra in tweet:
        if len(palabra) > 0:
            palabras += [palabra]
Tweets = list(todo["Palabras"])
tokens = list(set(palabras))

# =============================================================================
# 
# =============================================================================
emoji_presente = []
for item in etiquetas:
    emoji_presente += [palabra for palabra in item]
emoji_unico = list(set(emoji_presente))
emoji_unico = dict(Counter(emoji_presente))
del emoji_unico['[etiqueta]']
del emoji_unico['[hashtag]']
del emoji_unico['[URL]']
ocurrencias_emoji = {k:v for k, v in sorted(emoji_unico.items(), key=lambda item: item[1],reverse=True)}
emoji_df = pd.DataFrame(list(emoji_unico.items()), columns=["Emoji", "Cantidad"])
emoji_df["Para_busqueda"] = emoji_df["Emoji"].apply(lambda x: x.replace("[",""))
emoji_df["Para_busqueda"] = emoji_df["Para_busqueda"].apply(lambda x: x.replace("]",""))
emoji_df["Para_busqueda"] = emoji_df["Para_busqueda"].apply(lambda x: x.replace("_"," "))
# =============================================================================
# 
# =============================================================================
todo = pd.read_csv("U.csv", sep=';')
#stanza.download('es')
tweets= list(todo['Tweet'])
nlp = stanza.Pipeline("es")
lista_tweets = []
for tweet in tweets:
    doc = nlp(tweet)
    print(doc)

