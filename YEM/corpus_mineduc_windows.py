#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Librerías
# =============================================================================
import glob
import string
import re
import numpy as np

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
lista_files = glob.glob('C:/Users/fneir/OneDrive/Documentos/GitHub/Linguistica/YEM/entrevistas_mineduc/*.txt')
corpus = {}
##por cada archivo en la lista de archivos
for file in lista_files:
##este se abre con encoding utf-8 y queda definido como file_input
    with open(file, 'r', encoding="utf-8") as file_input:
##se toman los nombres de los textos y se le quitan los primeros 15 caracteres (el nombre de la carpeta)
        corpus[file[78:-4]]=file_input.read()
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
# =============================================================================
# Resultados corpus método antiguo
# =============================================================================
# =============================================================================
# ##definiremos un diccionario vacío para agregar solamente las palabras que aparecen antes de yem
# diccionario_contextos_presentacion = {'yem':[],'ema':[],'em':[]} 
# ##añadiremos al diccionario anterior las apariciones de yem/em/ema y las cuatro palabras anteriores, consideramos que es un buen número de palabras para inferir el significado
# lista_yem_presentacion = k_anteriores(lista_corpus_contextos,'yem',2)
# lista_em_presentacion = k_anteriores(lista_corpus_contextos,'em',2)
# lista_ema_presentacion = k_anteriores(lista_corpus_contextos,'ema',2)
# diccionario_contextos_presentacion['yem'] = lista_yem_presentacion
# diccionario_contextos_presentacion['em'] = lista_em_presentacion
# diccionario_contextos_presentacion['ema'] = lista_ema_presentacion
# =============================================================================

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
# =============================================================================
# NECESITO MEMORIA AAAA
# =============================================================================
del mapu_limpio1
del mapu_limpio2  
del corpus_string 
del lista_corpus_contextos
del string_corpus_contextos
del string_corpus_misional
del corpus
del tokens
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
trad_yem=[]
trad_em=[]
for item in yem:
    trad_yem+=[diccionario[str(item)]]
yem = dict(zip(yem,trad_yem)) 
for item in em:
    trad_em+=[diccionario[str(item)]]
em = dict(zip(em,trad_em)) 