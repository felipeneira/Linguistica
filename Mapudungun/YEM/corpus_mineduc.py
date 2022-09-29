#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Librerías
# =============================================================================
import glob
import string
import re
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
# =============================================================================
# 
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

def contador(x, y):
    contador = []
    for item in x:
        if item == y:
            contador += [item]
    return len(contador)
# =============================================================================
# 
# =============================================================================
lista_files = glob.glob('Textos/entrevistas_mineduc/*.txt')
corpus = {}
##por cada archivo en la lista de archivos
for file in lista_files:
##este se abre con encoding utf-8 y queda definido como file_input
    with open(file, 'r', encoding="utf-8") as file_input:
##se toman los nombres de los textos y se le quitan los primeros 15 caracteres (el nombre de la carpeta)
        corpus[file[20:-4]]=file_input.read()
corpus_string = str(corpus)
print('Nombre de los textos')
print(corpus.keys())
re_traduccion = r"n*M:\s*([a-zA-Z\<\>\d\s\?\¿ñÑü\.\*\%\,\\\'\áéíóú\'\!\\-¡]*)\\*\\nC:\s*([a-zA-Z\<\>\d\s\?\¿ñü\.\*\%\,\\\'\áéíóú]*)\\*\\n*"
corpus= re.findall(re_traduccion,corpus_string)
mapu= []
espa= []
for lista in corpus:
    mapu += lista[0:1]
    espa += lista[1:2]
string_corpus_misional = str(mapu)
##Tomamos el string_corpus_misional y limpiamos una serie de impurezas tÃ­picas de la escritura en mapudungun y el trabajo con txt
##En primer lugar eliminamos los saltos de pÃ¡gina marcados con "\n" y los marcados con "\t"
string_corpus_contextos = string_corpus_misional.replace('\n', ' ')
string_corpus_contextos = string_corpus_contextos.replace('\t', ' ')
##luego eliminamos [r], que simboliza la duda del escritor sobre la existencia de una "r" en esa posicion
string_corpus_contextos = string_corpus_contextos.replace('[r]', 'r')
##eliminamos los marcadores de pÃ¡rrafo 
string_corpus_contextos = string_corpus_contextos.replace('Â¶', '')
##utilizamos ambas def para eliminar puntuaciones y nÃºmeros del texto
string_corpus_contextos = remover_numeros(string_corpus_contextos)
##eliminamos las marcas de pregunta y respuesta en el texto, las que son marcadas con una "P" y "R" en el corpus
string_corpus_contextos = string_corpus_contextos.replace('P ', '')
string_corpus_contextos = string_corpus_contextos.replace('R ', '')
##eliminamos las mayÃºsculas y el exceso de espacios
string_corpus_contextos = string_corpus_contextos.lower()
##luego se usa .split para dividir el texto por \n
string_corpus_misional = string_corpus_misional.replace('\n', '')
string_corpus_contextos = string_corpus_contextos.replace('Â¿', '')
string_corpus_contextos = string_corpus_contextos.replace('â', '')
string_corpus_contextos = string_corpus_contextos.replace('â¦', '')
string_corpus_contextos = re.sub('<\*spa>',' ',string_corpus_contextos)
string_corpus_contextos = remover_puntuacion(string_corpus_contextos)
string_corpus_contextos = string_corpus_contextos.strip()
##lista exclusiva para graficacion
lista_corpus_contextos = string_corpus_contextos.split(' ')
tokens = []
for item in lista_corpus_contextos:    
    if len(item) > 0:
        tokens+= [item]
espa_str = str(espa)
# =============================================================================
# Resultados corpus método nuevo
# =============================================================================
mapu_limpio1= []
mapu_limpio2= []
mapu_limpio = []
data = range(len(mapu))
for item in mapu:
    mapu_limpio1 += [re.sub('(\<\*SPA\>)', ' ', item)]
for item in mapu_limpio1:
    mapu_limpio2 += [remover_puntuacion(item)]
for item in mapu_limpio2:
    mapu_limpio += [item.lower()]
mapu_palabras1=[]
mapu_palabras=[]
for item in mapu_limpio:
    mapu_palabras1 += item.split(" ")
for item in mapu_palabras1:
    if len(item) > 1:
        mapu_palabras += [item]
# =============================================================================
# NECESITO MEMORIA AAAA
# =============================================================================
del mapu
del mapu_limpio1,mapu_limpio2
del corpus_string,lista_corpus_contextos
del string_corpus_contextos,string_corpus_misional,corpus,tokens
del lista
# =============================================================================
# Seguimos
# =============================================================================
diccionario = dict(zip(mapu_limpio, espa))
yem=[]
for item in diccionario.keys():
    yem += re.findall("^[a-zA-Zñüáéíóú\s]*[\s]*yem+[\s]+[a-zA-Zñüáéíóú\s]*$", item)
em=[]
for item in diccionario.keys():
    em += re.findall("^(?!.*chem)[a-zA-Zñüáéíóú\s]*[\s]*em+[\s]+[a-zA-Zñüáéíóú\s]*$", item)
trad_yem=[]lista_corpus_contextos= []
pre_lista_corpus_contextos = str(corpus_preparado).split(' ')
for palabra in pre_lista_corpus_contextos:
    if len(palabra) > 0:
        lista_corpus_contextos += [palabra]
trad_em=[]
for item in yem:
    trad_yem+=[diccionario[str(item)]]
yem = dict(zip(yem,trad_yem)) 
for item in em:
    trad_em+=[diccionario[str(item)]]
em = dict(zip(em,trad_em)) 

# =============================================================================
# Visualización de datos
# =============================================================================
yemdt = {'Mapudungun':list(yem.keys()) , 'Traduccion': list(yem.values())}
yemdf = pd.DataFrame(yemdt)
yemdf.to_csv('Datos/yem.csv',sep=';')
emdt = {'Mapudungun':list(em.keys()), 'Traduccion':list(em.values())}
emdf = pd.DataFrame(emdt)
emdf.to_csv('Datos/em.csv',sep=';')
# =============================================================================
# volvemos a liberar memoria
# =============================================================================
del diccionario,espa
del mapu_limpio,yemdt,emdt
del trad_em, trad_yem
del data
del file
# =============================================================================
# 
# =============================================================================
datos = pd.read_csv(r'Datos/Misional/yem.csv', sep=';')
datos['Significado']

contador(list(datos['Significado']),'?')

significados = ['Defuntivo (536)','Tiempo nominal (12)', 'Afectivo (4)', 'No se sabe (29)']
valores = [536, 12, 4, 29]
plt.figure(figsize=(30, 3))
plt.subplot(131)
plt.bar(significados, valores)
# =============================================================================
# Preparación método javier
# =============================================================================
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
palabras = []
for palabra in lista_corpus_contextos:
    if len(palabra) > 1:
        palabras += [palabra]
        
diccionario_contextos_presentacion = {'yem':[],'em':[]} 
lista_yem_presentacion = k_anteriores(palabras,'yem',1)
lista_em_presentacion = k_anteriores(palabras,'em',1)
diccionario_contextos_presentacion['yem'] = lista_yem_presentacion
diccionario_contextos_presentacion['em'] = lista_em_presentacion

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
grafos = {}

for Y in diccionario_contextos_presentacion.keys():
    oraciones = diccionario_contextos_presentacion[Y]
    grafos[Y]=GoW(oraciones)

import matplotlib.pyplot as plt
import scipy
def plotG_centrality(Y,size):
    
    G = grafos[Y]
    #G0 = G.copy()
    #G0.remove_edges_from(nx.selfloop_edges(G0))
    #G = nx.k_core(G0)
    #G = nx.maximum_spanning_tree(G)
    fig, ax = plt.subplots(dpi=800)
    centrality = nx.pagerank(G,weight='weight')
    ordered_centrality = {k: v for k, v in sorted(centrality.items(), key=lambda item: item[1],reverse=True)}
    labels = {i:i for i in G.nodes() if i in list(zip(*list(ordered_centrality.items())[:50]))[0]}
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size = [size*x for x in list(centrality.values())], node_color='gold',node_shape='o',alpha=0.95, linewidths=0.1) 
    nx.draw_networkx_edges(G, pos, alpha=0.5,width=0.2,edge_color='k')
    nx.draw_networkx_labels(G,pos,labels,alpha=1,font_size=3.,font_color='k',font_family='monospace')
    plt.title('Red {}'.format(Y),fontsize=8)
    plt.savefig('red_{}.jpg'.format(Y), format='jpg', transparent=True, bbox_inches='tight',dpi=800)
    plt.axis('off')
    plt.show()
def ranking(palabra,k):
    red = grafos[palabra]
    return list({k: v for k, v in sorted(dict(red[palabra]).items(), key=lambda item: item[1]['weight'],reverse=True)}.keys())[:k]

for Y in grafos.keys():
    print(Y,ranking(Y,10))