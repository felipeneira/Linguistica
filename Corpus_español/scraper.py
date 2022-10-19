#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Cosas necesarias
# =============================================================================
# pip install snscrape
import snscrape.modules.twitter as sntwitter
import pandas as pd
import re
import string
import networkx as nx
import emoji
from collections import Counter
# =============================================================================
# Limpieza de corpus
# =============================================================================
##generamos una def para eliminar los puntos
def remover_puntuacion(s):
    ##cada uno de los items que aparecen en esta lista
    for c in string.punctuation:
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

## función para detectar k palabras anteriores

def k_anteriores(oracion,Y,k):
    lista_contextos = []
    for i in range(len(oracion)):
        word = oracion[i]
        if word == Y:
            r = k
            for r in range(1,k+1):
                if i-r < 0:
                    r -= 1
            lista_contextos += [oracion[i-r:i]+[Y]]
    return lista_contextos



## 
def GoW(text_clean):
    G=nx.Graph()
    for sentence in text_clean:
        if len(sentence)>1:
            pairs=list(zip(sentence,sentence[1:]))
            for pair in pairs:
                if G.has_edge(pair[0],pair[1])==False:
                    G.add_edge(pair[0],pair[1],weight=1)
                else:
                    x=G[pair[0]][pair[1]]['weight']
                    G[pair[0]][pair[1]]['weight']=x+1
                    
    #Gcc = sorted(nx.connected_components(G), key=len, reverse=True)
    #G0 = G.subgraph(Gcc[0])
    return G
# =============================================================================
# Fechas
# =============================================================================
# =============================================================================
# base = list(pd.date_range(start="2022-07-01",end="2022-09-04"))
# fechas = [str(item)[0:10] for item in base]
# =============================================================================
# =============================================================================
# Rechazo
# =============================================================================
# =============================================================================
# attributes_container = []
# for numero in list(range(0,66)):
#     for i, tweet in enumerate(sntwitter.TwitterSearchScraper('rechazo since:'+str(fechas[numero])+' until:'+str(fechas[numero+1])).get_items()):
#         if i > 2000:
#             break
#         if tweet.content not in attributes_container:
#             attributes_container.append([tweet.user.username,tweet.user.verified, tweet.user.description, tweet.date, tweet.content, tweet.hashtags])
# 
# tweets_df = pd.DataFrame(attributes_container, columns=["Usuario","Verificado","Descripcion_cuenta", "Fecha", "Tweet", "Hashtag"])
# tweets_df.to_csv("Tweets/rechazo.csv", sep=';' ,index=True)
# =============================================================================
# =============================================================================
# Apruebo
# =============================================================================
# =============================================================================
# attributes_container = []
# for numero in list(range(0,66)):
#     for i, tweet in enumerate(sntwitter.TwitterSearchScraper('apruebo since:'+str(fechas[numero])+' until:'+str(fechas[numero+1])).get_items()):
#         if i > 2000:
#             break
#         if tweet.content not in attributes_container:
#             attributes_container.append([tweet.user.username,tweet.user.verified, tweet.user.description, tweet.date, tweet.content, tweet.hashtags])
# 
# tweets_df = pd.DataFrame(attributes_container, columns=["Usuario","Verificado","Descripcion_cuenta", "Fecha", "Tweet", "Hashtag"])
# tweets_df.to_csv("Tweets/apruebo.csv", sep=';' ,index=True)
# =============================================================================
# =============================================================================
# Nueva constitucion
# =============================================================================
# =============================================================================
# attributes_container = []
# for numero in list(range(0,66)):
#     for i, tweet in enumerate(sntwitter.TwitterSearchScraper('nueva constitucion since:'+str(fechas[numero])+' until:'+str(fechas[numero+1])).get_items()):
#         if i > 2000:
#             break
#         if tweet.content not in attributes_container:
#             attributes_container.append([tweet.user.username,tweet.user.verified, tweet.user.description, tweet.date, tweet.content, tweet.hashtags])
# 
# tweets_df = pd.DataFrame(attributes_container, columns=["Usuario","Verificado","Descripcion_cuenta", "Fecha", "Tweet", "Hashtag"])
# tweets_df.to_csv("Tweets/nueva_constitucion.csv", sep=';' ,index=True)
# =============================================================================
# =============================================================================
# Datos
# =============================================================================
rechazo = pd.read_csv("Tweets/rechazo.csv", sep=";", lineterminator='\n')
apruebo = pd.read_csv("Tweets/apruebo.csv", sep=";", lineterminator='\n')
NC = pd.read_csv("Tweets/nueva_constitucion.csv", sep=";", lineterminator='\n')
rechazo = rechazo.set_index('Unnamed: 0')
apruebo = apruebo.set_index('Unnamed: 0')
NC = NC.set_index('Unnamed: 0')
emoji.demojize()
# =============================================================================
# Calculos emojis
# =============================================================================
todo=pd.merge(rechazo, apruebo, how="outer")
todo = pd.merge(todo, NC, how="outer")

todo['Tweet'] = todo['Tweet'].apply(lambda x :re.sub("(\\@[\\w\\d\\_\\.]+)", "[etiqueta]", x))
todo['Tweet'] = todo['Tweet'].apply(lambda x :re.sub("(\\#[\\w\\d\\_\\.]+)", "[hashtag]", x))
todo['Tweet'] = todo['Tweet'].apply(lambda x :re.sub("\s(https:\/\/[\w\.\/\-]*)", "[URL]", x))
todo['Tweet'] = todo['Tweet'].apply(lambda x :emoji.demojize(x, delimiters=("[","]")))
etiquetas = list(todo['Tweet'].apply(lambda x :re.findall("(\[\w*\_*\d*\])",x)))

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
emoji_df["Muestra"] = emoji_df["Emoji"].apply(lambda x: emoji.emojize(x,delimiters=("[","]")))
emoji_df.to_csv("emoji.csv", sep = ";")
# =============================================================================
# Contar emojis
# =============================================================================

# =============================================================================
# Codigo anti-emoji
# =============================================================================
# =============================================================================
# emoji_pattern = re.compile("["
#         u"\U0001F600-\U0001F64F"  # emoticons
#         u"\U0001F300-\U0001F5FF"  # symbols & pictographs
#         u"\U0001F680-\U0001F6FF"  # transport & map symbols
#         u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
#                            "]+", flags=re.UNICODE)
# todo['Tweet'] = todo['Tweet'].apply(lambda x :emoji_pattern.sub(r'[emoji]', x))
# =============================================================================
# =============================================================================
# limpieza para cuantificaciones de corpus sin etiquetas
# =============================================================================

# =============================================================================
# todo['Tweet'] = todo['Tweet'].apply(lambda x :re.sub("\[hashtag\]", "", x))
# todo['Tweet'] = todo['Tweet'].apply(lambda x :re.sub("\[etiqueta\]", "", x))
# todo['Tweet'] = todo['Tweet'].apply(lambda x :re.sub("\[emoji\]", "", x))
# todo['Tweet'] = todo['Tweet'].apply(lambda x :re.sub("\[URL\]", "", x))
# todo['Tweet'] = todo['Tweet'].apply(lambda x :x.lower())
# todo['Tweet'] = todo['Tweet'].apply(lambda x :remover_puntuacion(x))
# todo['Tweet'] = todo['Tweet'].apply(lambda x :remover_numeros(x))
# todo['Tweet'] = todo['Tweet'].apply(lambda x :x.strip())
# todo['Tweet'] = todo['Tweet'].apply(lambda x :x.replace("…"," "))
# todo['Tweet'] = todo['Tweet'].apply(lambda x :x.replace("\n"," "))
# todo['Palabras'] = todo['Tweet'].apply(lambda x :x.split(" "))
# 
# palabras = []
# for tweet in todo['Palabras']:
#     for palabra in tweet:
#         if len(palabra) > 0:
#             palabras += [palabra]
# tokens = set(palabras)
# 
# =============================================================================

# =============================================================================
# 
# =============================================================================
