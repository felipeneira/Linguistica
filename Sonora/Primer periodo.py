import glob
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
lista_files = glob.glob('Textos/*.txt')
corpus = {}
for file in lista_files:
    with open(file, 'r', encoding="utf-8") as file_input:
        corpus[file[15:]]=file_input.read()  
import string
def remover_puntuacion(s): 
    for c in string.punctuation:
        s=s.replace(c,"")
        s=s.replace('\t','')
    return s
corpus_misional = []
for key in corpus.keys():
    corpus_misional += [corpus[key]]
string_corpus_misional=' '.join(corpus_misional)
string_corpus_misional = string_corpus_misional.split('\n')
vacio=[oracion for oracion in string_corpus_misional if len(oracion)>0]
sin_puntos = []
for oracion in vacio:
    oracion_limpia = remover_puntuacion(oracion)
    sin_puntos += [oracion_limpia.lower()]
palabras = []
for oracion in sin_puntos:
    palabras += [oracion.split(' ')]
    def k_anteriores(oracion,Y,k):
        lista_contextos = []
        for i in range(len(oracion)):
            word = oracion[i]
            if word == Y:
                r = k
                for r in range(1,k+1):
                    if i-r < 0:
                        r -= 1
        lista_contextos += [oracion[i-r:i]]
        return lista_contextos

def revision2(YZ): ##recibe una lista y un string que es el que busca
    palabras_transitivas=[] ##defino la lista
    for oracion in palabras: ## por cada oración de la lista
        for item in oracion: ##y por cada palabra en la oración
            if item.endswith(YZ): ##si esta termina en el string indicado
                palabras_transitivas+=[item] ##la agrega a la lista
    return palabras_transitivas
interact(revision2, YZ='eneu')