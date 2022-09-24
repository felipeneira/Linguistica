# -*- coding: utf-8 -*-
# =============================================================================
# 
# =============================================================================
import glob
import re
import string
import pandas as pd
import streamlit as st
# =============================================================================
# 
# =============================================================================
def remover_puntuacion(s): 
    for c in string.punctuation:
        s=s.replace(c,"")
        s=s.replace('\t','')
    return s
def remover_numeros(k): 
    numeros= []
    for numero in list(range(100)):
        numeros+= [numero]
    numeros = str(numeros)
    for z in numeros:
        k=k.replace(z," ")
        k=k.replace('pag','')
    return k
def seleccion_corpus(corpus):
    if corpus == "institucional":
        lista_files = glob.glob('Textos/entrevistas_mineduc/*.txt')
        corpus = {}
        ##por cada archivo en la lista de archivos
        for file in lista_files:
        ##este se abre con encoding utf-8 y queda definido como file_input
            with open(file, 'r', encoding="utf-8") as file_input:
        ##se toman los nombres de los textos y se le quitan los primeros 15 caracteres (el nombre de la carpeta)
                corpus[file[67:-4]]=file_input.read()
        corpus_string = str(corpus)
        for item in list(corpus.keys()):
            print(item)
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
        corpus_preparado = string_corpus_misional
        return corpus_preparado
    elif corpus == "misional":
        lista_files = glob.glob('Textos/Primer periodo/*.txt')
        corpus = {}
        ##por cada archivo en la lista de archivos
        for file in lista_files:
        ##este se abre con encoding utf-8 y queda definido como file_input
            with open(file, 'r', encoding="utf-8") as file_input:
        ##se toman los nombres de los textos y se le quitan los primeros 15 caracteres (el nombre de la carpeta)
                corpus[file[105:-4]]=file_input.read()
        #toma el corpus subido y crea una lista vacía
        corpus_misional = []
        ##por cada uno de los keys en corpus.keys se agrega a corpus_misional el value
        for key in corpus.keys():
            corpus_misional += [corpus[key]] 
        ## se hace un string para poner todos los values de corpus con el objetivo de trabajarlo como un solo texto grande
        string_corpus_misional=' '.join(corpus_misional)       
        ##luego se usa .split para dividir el texto por \n
        corpus_preparado = string_corpus_misional.split('\n')
        corpus_preparado = str(corpus_preparado).replace('\n', ' ')
        corpus_preparado = str(corpus_preparado).replace('[r]', 'r')
        ##utilizamos ambas def para eliminar puntuaciones y números del texto
        corpus_preparado = remover_numeros(str(corpus_preparado))
        corpus_preparado = remover_puntuacion(str(corpus_preparado))
        ##eliminamos las mayúsculas y el exceso de espacios
        corpus_preparado = str(corpus_preparado).lower()
        corpus_preparado = str(corpus_preparado).strip()
        return corpus_preparado
    elif corpus == "etnografico":
        lista_files = glob.glob('Textos/Segundo periodo/*.txt')
        ##se define un diccionario donde en los keys se encuentran los nombres y en los values el texto
        corpus = {}
        ##por cada archivo en la lista de archivos
        for file in lista_files:
        ##este se abre con encoding utf-8 y queda definido como file_input
            with open(file, 'r', encoding="utf-8") as file_input:
        ##se toman los nombres de los textos y se le quitan los primeros 15 caracteres (el nombre de la carpeta)
                corpus[file[101:-4]]=file_input.read()
        corpus_misional = []
        ##por cada uno de los keys en corpus.keys se agrega a corpus_misional el value
        for key in corpus.keys():
            corpus_misional += [corpus[key]]
        string_corpus_misional=' '.join(corpus_misional)
        corpus_preparado = string_corpus_misional.split('\n')
        corpus_preparado = str(corpus_preparado).replace('\n', ' ')
        corpus_preparado = str(corpus_preparado).replace('[r]', 'r')
        ##utilizamos ambas def para eliminar puntuaciones y números del texto
        corpus_preparado = remover_numeros(str(corpus_preparado))
        corpus_preparado = remover_puntuacion(str(corpus_preparado))
        ##eliminamos las mayúsculas y el exceso de espacios
        corpus_preparado = str(corpus_preparado).lower()
        corpus_preparado = str(corpus_preparado).strip()
        return corpus_preparado
    
# =============================================================================
# 
# =============================================================================
st.title("Búsqueda por corpus (2da versión)")
corpus = st.selectbox("Seleccionar corpus",["misional","etnografico","institucional"], index=1)
# =============================================================================
# 
# =============================================================================
st.write(seleccion_corpus(corpus))