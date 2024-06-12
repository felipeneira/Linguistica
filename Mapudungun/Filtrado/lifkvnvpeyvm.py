# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 19:06:30 2024

@author: User
"""
import string
import re
import glob

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

def entukvnvn_hemvl():
    lista_files = glob.glob('Textos/entrevistas_mineduc/*.txt')
    corpus = {}
    ##por cada archivo en la lista de archivos
    for file in lista_files:
    ##este se abre con encoding utf-8 y queda definido como file_input
        with open(file, 'r', encoding="utf-8") as file_input:
    ##se toman los nombres de los textos y se le quitan los primeros 15 caracteres (el nombre de la carpeta)
            corpus[file[20:-4]]=file_input.read()
    corpus_string = str(corpus)
    re_traduccion = r"n*M:\s*([a-zA-Z\<\>\d\s\?\¿ñÑü\.\*\%\,\\\'\áéíóú\'\!\\-¡]*)\\*\\nC:\s*([a-zA-Z\<\>\d\s\?\¿ñü\.\*\%\,\\\'\áéíóú]*)\\*\\n*"
    corpus= re.findall(re_traduccion,corpus_string)
    mapu= [lista[0:1] for lista in corpus]
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
    string_corpus_contextos = string_corpus_contextos.replace('\n', '')
    string_corpus_contextos = string_corpus_contextos.replace('Â¿', '')
    string_corpus_contextos = string_corpus_contextos.replace('â', '')
    string_corpus_contextos = string_corpus_contextos.replace('â¦', '')
    string_corpus_contextos = re.sub('<\*spa>',' ',string_corpus_contextos)
    string_corpus_contextos = remover_puntuacion(string_corpus_contextos)
    string_corpus_contextos = string_corpus_contextos.strip()
    lista_corpus_contextos = string_corpus_contextos.split(' ')
    lista_corpus_contextos = [item for item in lista_corpus_contextos if len(item) > 0]
    lista_corpus_contextos = [item for item in lista_corpus_contextos if item != 'noise']
    return lista_corpus_contextos