#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# librerias
# =============================================================================
import glob
import re
import string
import pandas as pd

# =============================================================================
# preparar morfessor
# =============================================================================
import morfessor
io = morfessor.MorfessorIO(encoding="utf-8",construction_separator=' ',comment_start= '#', compound_separator="\\s", atom_separator=None, lowercase= False)
cost = morfessor.baseline.AnnotatedCorpusEncoding("utf-8")

# =============================================================================
# defs limpieza
# =============================================================================
string.punctuation
def remover_puntuacion(s):
    puntuacion = """!"#$%&\'()*+,.:;<=>?@[\\]^_`{|}~"""
    for c in puntuacion:
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

# =============================================================================
# limpieza corpus de palabras
# =============================================================================
lista_files = glob.glob('Textos/entrevistas_hasler/*.txt')
corpus = {}
##por cada archivo en la lista de archivosprint('Nombre de los textos')
for file in lista_files:
##este se abre con encoding utf-8 y queda definido como file_input
    with open(file, 'r', encoding="utf-8") as file_input:
##se toman los nombres de los textos y se le quitan los primeros 15 caracteres (el nombre de la carpeta)
        corpus[file[46:-4]]=file_input.read()
corpus_string = str([corpus[key] for key in corpus.keys()]).split('\\n')
corpus_string = list((re.sub("- ", "-", oracion) for oracion in corpus_string))
corpus_string= [oracion for oracion in corpus_string if len(oracion)>0]  
corpus_string = [oracion for oracion in corpus_string if oracion.startswith("\\\\tx ")]
   
corpus_string = [oracion.split(" ") for oracion in corpus_string]
corpus_string = [palabra for oracion in corpus_string for palabra in oracion if len(palabra) > 0]
corpus_palabras = [palabra for palabra in corpus_string if palabra != "\\\\tx"]
corpus_palabras = [remover_puntuacion(oracion) for oracion in corpus_palabras]
corpus_palabras = [remover_numeros(oracion) for oracion in corpus_palabras]
corpus_palabras = [palabra for palabra in corpus_palabras if len(palabra) > 0]
# =============================================================================
# limpieza corpus de segmentaciones
# =============================================================================
corpus_string = str([corpus[key] for key in corpus.keys()]).split('\\n')
corpus_string =[oracion for oracion in corpus_string if len(oracion)>0]  
corpus_string = [oracion for oracion in corpus_string if oracion.startswith("\\\\mb ")]        
corpus_string = [oracion.split(" ") for oracion in corpus_string]
corpus_string = [palabra for oracion in corpus_string for palabra in oracion if len(palabra) > 0]
corpus_glosa = [palabra for palabra in corpus_string if palabra != "\\\\mb"]
separacion = []
contador = 0
for item in corpus_glosa:
    if not item.startswith("-"):
        separacion += [list([item])]
        contador = contador + 1
    else:
        separacion[contador-1] += [item]
f = list(range(611))
for item in f:
    separacion += [item]
# =============================================================================
# Primera version de los datos
# =============================================================================
# df = pd.DataFrame(list(zip(corpus_palabras,separacion)),columns=["palabra","segmentacion"])
# df.to_csv("experimento.csv")
# =============================================================================
# Datos limpios
# =============================================================================
df = pd.read_csv("NO_BORRAR.csv")
df = df[["palabra","segmentacion"]]
palabras = df["palabra"].to_list()
palabras = [remover_puntuacion(str(item)) for item in palabras]
palabras = [item.replace('-','') for item in palabras]
segmentacion = df["segmentacion"].to_list()
segmentacion = [remover_puntuacion(str(item)) for item in segmentacion]
segmentacion = [item.replace('-',' ') for item in segmentacion]
AF1 = dict(zip(palabras, segmentacion))
# =============================================================================
# pasar datos al modelo requerido por morfessor
# =============================================================================
# with open("AF.txt", "w") as text_file:
#    for i,j in AF1.items():
#        text_file.write(i + " " + j + "\n")
# =============================================================================
# eliminar variables
# =============================================================================
del contador, corpus, corpus_glosa, corpus_palabras, corpus_string, f
del separacion, item, lista_files
# =============================================================================
# Trabajo con morfessor
# =============================================================================
train_data1 = list(io.read_corpus_file('AF.txt'))#palabras+segmentos
TCF = list(io.read_corpus_file("WLF.txt"))#palabras texto plano
WLF = io.read_segmentation_file("WLF.txt", has_counts=False)#lista palabras


model_tokens = morfessor.BaselineModel()


model_tokens = morfessor.BaselineModel()

model_tokens.load_data(train_data1)
model_tokens.train_batch()

prueba = list(model_tokens.get_segmentations())

print(model_tokens.viterbi_segment(""))
