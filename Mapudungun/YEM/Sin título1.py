#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 07:53:07 2022

@author: felipe
"""
import re
##preparar texto
##se prepara la lista glob que sirve para trabajar con carpetas
import glob
## se define que lista_files es una lista con los nombres de los archivos 
##los cuales están seleccionados como los txt que se encuentran dentro de primer periodo
lista_files = glob.glob('entrevistas_hasler/*.txt')
##se define un diccionario donde en los keys se encuentran los nombres y en los values el texto
corpus = {}
##por cada archivo en la lista de archivos
for file in lista_files:
##este se abre con encoding utf-8 y queda definido como file_input
    with open(file, 'r', encoding="utf-8") as file_input:
##se toman los nombres de los textos y se le quitan los primeros 15 caracteres (el nombre de la carpeta)
        corpus[file[35:-4]]=file_input.read()
print('Nombre de los textos')
print(corpus.keys()) 
print('  ')     
print('  ')


##limpieza texto

import string

numeros= []
for numero in list(range(100)):
    numeros+= [numero]
numeros = str(numeros)
numeros

def remover_puntuacion(s): 
    for c in string.punctuation:
        s=s.replace(c,"")
        s=s.replace('\t','')
    return s
def remover_numeros(k): 
    for z in numeros:
        k=k.replace(z," ")
        k=k.replace('pag','')
    return k


#toma el corpus subido y crea una lista vacía
corpus_misional = []

##por cada uno de los keys en corpus.keys se agrega a corpus_misional el value
for key in corpus.keys():
    corpus_misional += [corpus[key]]

## se hace un string para poner todos los values de corpus con el objetivo de trabajarlo como un solo texto grande
string_corpus_misional=' '.join(corpus_misional)    
    
##luego se usa .split para dividir el texto por \n
string_corpus_misional = string_corpus_misional.split('\n')


#toma el corpus subido y crea una lista vacía
corpus_misional = []
##por cada uno de los keys en corpus.keys se agrega a corpus_misional el value
for key in corpus.keys():
    corpus_misional += [corpus[key]]   
    
##Se define una lista como vacio para poder ingresar cada una de las oraciones del corpus sin espacios en blanco

vacio=[oracion for oracion in string_corpus_misional if len(oracion)>0]
    
##por cada una de estas oraciones en 
corpus_preparado = []
for oracion in vacio:
    if oracion.startswith('\\tx '):
        corpus_preparado += [oracion]
                
##Tomamos el string_corpus_misional y limpiamos una serie de impurezas típicas de la escritura en mapudungun y el trabajo con txt
##Esto lo hacemos para que las redes y los resultados del contexto sean más limpios y no dependan de la segmentación arbitraria por oraciones propuesta por el autor
##En primer lugar eliminamos los saltos de página marcados con "\n" y los marcados con "\t"
string_corpus_contextos = str(corpus_preparado).replace('\n', ' ')
corpus_preparado = str(corpus_preparado).replace('\t', ' ')
##luego eliminamos [r], que simboliza la duda del escritor sobre la existencia de una "r" en esa posición
corpus_preparado = str(corpus_preparado).replace('[r]', 'r')
##eliminamos las marcas de respuesta en el texto, las que son marcadas con una "R" en el corpus
corpus_preparado = str(corpus_preparado).replace('R.', ' ')
corpus_preparado = str(corpus_preparado).replace('R,', ' ')
##eliminamos los marcadores de párrafo 
corpus_preparado = str(corpus_preparado).replace('¶', ' ')
##utilizamos ambas def para eliminar puntuaciones y números del texto
corpus_preparado = remover_numeros(str(corpus_preparado))
corpus_preparado = remover_puntuacion(str(corpus_preparado))
##eliminamos las mayúsculas y el exceso de espacios
corpus_preparado = str(corpus_preparado).lower()
corpus_preparado = str(corpus_preparado).strip()
##eliminamos la marcación que señala que el texto está escrito en mapudungun, esta marcación es propia de estas entrevistas en particular
corpus_preparado = str(corpus_preparado).replace('\\tx ', ' ')
corpus_preparado = str(corpus_preparado).replace('tx', ' ')

lista_corpus_contextos= []
pre_lista_corpus_contextos = str(corpus_preparado).split(' ')
for palabra in pre_lista_corpus_contextos:
    if len(palabra) > 0:
        lista_corpus_contextos += [palabra]

hasler = str(lista_corpus_contextos)
hasler = hasler.replace("'","")
hasler = hasler.replace(",","")
yem=[]
em=[]
yem += re.findall("[a-zA-Zñüáéíóú\s]*[\s]*yem+[\s]+[a-zA-Zñüáéíóú\s]*$", hasler)
em += re.findall("(?!.*chem)[a-zA-Zñüáéíóú\s]*[\s]*em+[\s]+[a-zA-Zñüáéíóú\s]*$", hasler)