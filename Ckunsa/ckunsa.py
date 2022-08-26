# =============================================================================
# LibrerÃ­as usadas
# =============================================================================
import pandas as pd
import glob
import re
# =============================================================================
# abrir textos
# =============================================================================
textos = glob.glob("/home/felipe/GitHub/Linguistica/Ckunsa/*.txt")
corpus = {}
##por cada archivo en la lista de archivos
for file in textos:
##este se abre con encoding utf-8 y queda definido como file_input
    with open(file, 'r', encoding="utf-8") as file_input:
##se toman los nombres de los textos y se le quitan los primeros carÃ¡cteres
        corpus[file[50:-4]]=file_input.read()
        
diccionario_string = []
##por cada uno de los keys en corpus.keys se agrega a corpus_misional el value
for key in corpus.keys():
    diccionario_string += [corpus[key]]
diccionario_string = str(diccionario_string)
diccionario_string = diccionario_string.lower()
diccionario_string = diccionario_string.strip()
diccionario_string = re.sub("\\\\n", " wd ", diccionario_string)
# =============================================================================
# Selector de palabras
# =============================================================================
# Para usar el buscador vamos a usar los dos puntos como referencia

# extraer todos los lexemas del ckunsa
palabras_ckunsa = []
palabras_ckunsa += re.findall('d\s([a-zA-Z\-áéíóúñ]*):\s', diccionario_string)

# =============================================================================
# Extraer raíces verbales
# =============================================================================
verbos_ckunsa = []
verbosre="d\s([A-Za-z\-áéíóúñ]*):\s[a-z\s\,áéíóúñ]*(ar\s+[,\.]*|er\s+[,\.]*|ir\s+[,\.]*|arse\s+[,\.]*|erse\s+[,\.]*|irse\s+[,\.]*)+[a-z\sáéíóú\,\.\/\(\)\-]*\s*w"
verbos_ckunsa += re.findall(verbosre, diccionario_string)
lista_verbos = []
for lista in verbos_ckunsa:
    lista_verbos += lista[0:1]
diccionario = pd.read_csv('/home/felipe/GitHub/Linguistica/Ckunsa/diccionario.csv', sep=';')
diccionario_verbos = diccionario[diccionario.Lexema.isin(lista_verbos)]

# =============================================================================
# 
# =============================================================================
posibilidades = ["Nombre","nombre","lugar","Lugar","Apellido","apellido"]
ali = []
for item in posibilidades:
    ali += re.findall(r"([A-Za-z\-áéíóú]*):\s[a-zA-Z\d\sñáéíóú\.\(\)]*\s\b(apellido)\b", diccionario_string)

