# =============================================================================
# Librerías usadas
# =============================================================================
import pandas as pd
import glob
import re
# =============================================================================
# abrir textos
# =============================================================================
textos = glob.glob("/home/felipe/Documentos/GitHub/Linguistica/Ckunsa/*.txt")
corpus = {}
##por cada archivo en la lista de archivos
for file in textos:
##este se abre con encoding utf-8 y queda definido como file_input
    with open(file, 'r', encoding="utf-8") as file_input:
##se toman los nombres de los textos y se le quitan los primeros carácteres
        corpus[file[50:-4]]=file_input.read()
        
diccionario = []
##por cada uno de los keys en corpus.keys se agrega a corpus_misional el value
for key in corpus.keys():
    diccionario += [corpus[key]]
diccionario = str(diccionario)
diccionario = diccionario.lower()
diccionario = diccionario.strip()
# =============================================================================
# Selector de palabras
# =============================================================================
# Para usar el buscador vamos a usar los dos puntos como referencia

# extraer todos los lexemas del ckunsa
palabras_ckunsa = []
palabras_ckunsa += re.findall('n([a-zA-Z\-áéíóúñ]*):\s', diccionario)

