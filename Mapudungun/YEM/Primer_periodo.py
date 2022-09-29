#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# 
# =============================================================================
##importamos string para la limpieza de los textos
import matplotlib.pyplot as plt
import string
##abrimos una lista con números con el fin de poder eliminar de forma más fácil los caracteres numéricos
numeros= []
##cada uno de los números de este rango
for numero in list(range(100)):
    ##lo añadimos a una lista    
    numeros+= [numero]
##la cuál definimos como un string
numeros = str(numeros)
numeros

##generamos una def para eliminar los puntos
def remover_puntuacion(s):
    ##cada uno de los items que aparecen en esta lista
    for c in string.punctuation:
        ##es eliminado del texto reemplazandolo por un espacio vacío
        s=s.replace(c,"")
        ##lo mismo se hace con "\t"
        s=s.replace('\t','')
    return s

##última def de preparación
def remover_numeros(k):
    ##por cada item dentro de la lusta numeros
    for z in numeros:
        ##reemplazamos elitem de la lista con un vacío
        k=k.replace(z," ")
        ##también eliminamos la palabra "pag", usada para marcar páginas junto con lo anterior
        k=k.replace('pag','')
    return k
def contador(x, y):
    contador = []
    for item in x:
        if item == y:
            contador += [item]
    return len(contador)
# =============================================================================
# 
# =============================================================================
##preparar texto
##se prepara la lista glob que sirve para trabajar con carpetas
import glob
import re
import pandas as pd
## se define que lista_files es una lista con los nombres de los archivos 
##los cuales están seleccionados como los txt que se encuentran dentro de primer periodo
lista_files = glob.glob('Textos/Primer periodo/*.txt')
##se define un diccionario donde en los keys se encuentran los nombres y en los values el texto
corpus = {}
##por cada archivo en la lista de archivos
for file in lista_files:
##este se abre con encoding utf-8 y queda definido como file_input
    with open(file, 'r', encoding="utf-8") as file_input:
##se toman los nombres de los textos y se le quitan los primeros 15 caracteres (el nombre de la carpeta)
        corpus[file[15:]]=file_input.read()
print('Nombre de los textos')
print(corpus.keys())    
##esto último con el objetivo de corroborar si el programa lee todos los textos de forma correcta
#toma el corpus subido y crea una lista vacía
corpus_misional = []
##por cada uno de los keys en corpus.keys se agrega a corpus_misional el value
for key in corpus.keys():
    corpus_misional += [corpus[key]]

## se hace un string para poner todos los values de corpus con el objetivo de trabajarlo como un solo texto grande
string_corpus_misional=' '.join(corpus_misional)

##Tomamos el string_corpus_misional y limpiamos una serie de impurezas típicas de la escritura en mapudungun y el trabajo con txt
##En primer lugar eliminamos los saltos de página marcados con "\n" y los marcados con "\t"
string_corpus_contextos = string_corpus_misional.replace('\n', ' ')
string_corpus_contextos = string_corpus_contextos.replace('\t', ' ')
##luego eliminamos [r], que simboliza la duda del escritor sobre la existencia de una "r" en esa posición
string_corpus_contextos = string_corpus_contextos.replace('[r]', 'r')
##eliminamos los marcadores de párrafo 
string_corpus_contextos = string_corpus_contextos.replace('¶', '')
##utilizamos ambas def para eliminar puntuaciones y números del texto
string_corpus_contextos = remover_numeros(string_corpus_contextos)
string_corpus_contextos = remover_puntuacion(string_corpus_contextos)
##eliminamos las marcas de pregunta y respuesta en el texto, las que son marcadas con una "P" y "R" en el corpus
string_corpus_contextos = string_corpus_contextos.replace('P ', '')
string_corpus_contextos = string_corpus_contextos.replace('R ', '')
##eliminamos las mayúsculas y el exceso de espacios
string_corpus_contextos = string_corpus_contextos.lower()
string_corpus_contextos = string_corpus_contextos.strip()
##lista exclusiva para graficación
lista_corpus_contextos = string_corpus_contextos.split(' ')
##luego se usa .split para dividir el texto por \n
string_corpus_misional = string_corpus_misional.split('\n')

# =============================================================================
# 
# =============================================================================
ema = []
ema1 = []
ema1 += re.findall(r"[a-zA-Zñáéíóúùіре]*\s*ema\s+", string_corpus_contextos)
for item in ema1:
    if item != "huema ":
        ema += [item]
em = []
em1 = []
em1 += re.findall(r"[a-zA-Zñáéíóúùіре]*\s*em\s+", string_corpus_contextos)
for item in em1:
    if item != "chem ":
        em += [item]
while "chem " in em1:
    em1.remove("chem ")
while "cúyem  " in em1:
    em1.remove("cúyem  ")
while "vem " in em1:
    em1.remove("vem ")
yem = []
yem += re.findall(r"[a-zA-Zñáéíóúùіре]*\s*yem\s+", string_corpus_contextos)

# =============================================================================
# 
# =============================================================================
# =============================================================================
# yemdt = {'Mapudungun':yem}
# yemdf = pd.DataFrame(yemdt)
# yemdf.to_csv('Datos/yem_misional.csv',sep=';')
# emdt = {'Mapudungun':em1}
# emdf = pd.DataFrame(emdt)
# emdf.to_csv('Datos/em_misional.csv',sep=';')
# emadt = {'Mapudungun':ema}
# emadf = pd.DataFrame(emadt)
# emadf.to_csv('Datos/ema_misional.csv',sep=';')
# =============================================================================


# =============================================================================
# 
# =============================================================================

# =============================================================================
# Ploteo Significados
# =============================================================================
formas = ["em", "yem", "ema"]
for forma in formas:
    datos = pd.read_csv(r'Datos/Misional/'+forma+'.csv', sep=';')
    valores = []
    for item in range(7):
        valores += [contador(list(datos['Significado']),item)]
    significados = ['No se sabe','Defuntivo','Tiempo nominal', 'Afectivo', 'Conmiserativo','interjección','despreciativo*']
    plt.barh(significados, valores)
    for index, value in enumerate(valores):
        plt.text(value,index, str(value))
    plt.title(forma+' periodo misional')
    plt.savefig("Datos/Misional/Graficos/"+forma+"_misional")
    plt.show()
# =============================================================================
# Ploteo por autor
# =============================================================================
formas = ["em", "yem", "ema"]
autores = ["Valdivia", "Febres", "Havedstat"]
for forma in formas:
    for autor in autores:
        datos = pd.read_csv(r'Datos/Misional/'+forma+'.csv', sep=';')
        datos = datos[datos.Autor.str.contains(autor)]
        valores = []
        for item in range(7):
            valores += [contador(list(datos['Significado']),item)]
        significados = ['No se sabe','Defuntivo','Tiempo nominal', 'Afectivo', 'Conmiserativo','interjección','despreciativo*']
        plt.barh(significados, valores)
        for index, value in enumerate(valores):
            plt.text(value,index, str(value))
        plt.title(autor+' '+forma)
        plt.savefig("Datos/Misional/Graficos/"+autor+' '+forma)
        plt.show()

def suma_listas(a, b, c=0):
    suma=[]
    for i in range(len(a)):
        suma.append(a[i]+b[i]+c[i])
    return suma


suma_listas(valores[1],valores[0],valores[2])
# =============================================================================
# ploteo por forma
# =============================================================================
formas = ["em"]
autores = ["Valdivia", "Febres", "Havedstat"]
valores = []
for forma in formas:
    datos = pd.read_csv(r'Datos/Misional/'+forma+'.csv', sep=';')
    valores_parciales = []
    for autor in autores:
        valores_parciales += [contador(list(datos['Autor']),autor)]
    valores += [valores_parciales]
# =============================================================================
# 
# =============================================================================
    plt.barh(autores,valores[0])
    for index, value in enumerate(valores[0]):
        plt.text(value,index, str(value))
        plt.title(forma)
        plt.savefig("Datos/Misional/Graficos/"+forma)
        
            
            

