#!/usr/bin/env python3
# =============================================================================
# Librerías Usadas
# =============================================================================
import glob
import re
import string
import sys
import pandas as pd
# =============================================================================
# Def usadas
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

# =============================================================================
# Preparar textos
# =============================================================================
while True:
    print('======================================================================================================================================================')
    ##se prepara la lista glob que sirve para trabajar con carpetas
    corpus = input("""
Corpus para buscar

misional        --> mi          (Valdivia 1606, 1626, Febrés 1765)

etnografico     --> et          (Lenz 1863-1938, Manquilef 1914, 1911)

entrevistas     --> fh          (Entrevistas Tesis Felipe Hasler)

corpus mineduc  --> cm          (Corpus recolectado por el mineduc)

Escribir "salir" para cerrar el programa

¿En que período deseas buscar? 
""")
    ## se define que lista_files es una lista con los nombres de los archivos 
    ##los cuales están seleccionados como los txt que se encuentran dentro de primer periodo
    if corpus == "ins":
        lista_files = glob.glob('Textos/entrevistas_hasler/*.txt')
        corpus = {}
        ##por cada archivo en la lista de archivosprint('Nombre de los textos')
        for file in lista_files:
        ##este se abre con encoding utf-8 y queda definido como file_input
            with open(file, 'r', encoding="utf-8") as file_input:
        ##se toman los nombres de los textos y se le quitan los primeros 15 caracteres (el nombre de la carpeta)
                corpus[file[129:-4]]=file_input.read()
        corpus_misional = []
        ##por cada uno de los keys en corpus.keys se agrega a corpus_misional el value
        for key in corpus.keys():
            corpus_misional += [corpus[key]] 
        ## se hace un string para poner todos los values de corpus con el objetivo de trabajarlo como un solo texto grande
        string_corpus_misional=' '.join(corpus_misional)    
        ##luego se usa .split para dividir el texto por \n
        string_corpus_misional = string_corpus_misional.split('\n')
        #toma el corpus subido y crea una lista vacía
    
        ##Se define una lista como vacio para poder ingresar cada una de las oraciones del corpus sin espacios en blanco
        vacio=[oracion for oracion in string_corpus_misional if len(oracion)>0]  
        corpus_preparado = []
        for oracion in vacio:
            if oracion.startswith('\\tx '):
                corpus_preparado += [oracion]  
        ##eliminamos la marcación que señala que el texto está escrito en mapudungun, esta marcación es propia de estas entrevistas en particular
        corpus_preparado = str(corpus_preparado).replace('\\tx ', ' ')
        corpus_preparado = str(corpus_preparado).replace('tx', ' ')
        print('======================================================================================================================================================')
        print('Nombre de los textos')
        print(' ')
        for item in list(corpus.keys()):
            print(item)
        lista_string = corpus_preparado.split()
        print(' ')
        print('Cantidad de palabras')
        print(len(lista_string))
        print('======================================================================================================================================================')
    
    
    elif corpus == "mi":
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
        string_corpus_contextos = string_corpus_misional.split('\n')
        corpus_preparado = string_corpus_misional
        print('======================================================================================================================================================')
        print('Nombre de los textos')
        print(' ')
        for item in list(corpus.keys()):
            print(item)
        lista_string = corpus_preparado.split()
        print(' ')
        print('Cantidad de palabras')
        print(len(lista_string))
        print('======================================================================================================================================================')    
    
    elif corpus == "et":
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
        string_corpus_contextos = string_corpus_misional.split('\n')
        corpus_preparado = string_corpus_misional
        print('======================================================================================================================================================')
        print('Nombre de los textos')
        print(' ')
        for item in list(corpus.keys()):
            print(item)
        lista_string = corpus_preparado.split()
        print(' ')
        print('Cantidad de palabras')
        print(len(lista_string))
        print('======================================================================================================================================================')
    elif corpus == "cm":
        lista_files = glob.glob('Textos/entrevistas_mineduc/*.txt')
        corpus = {}
        ##por cada archivo en la lista de archivos
        for file in lista_files:
        ##este se abre con encoding utf-8 y queda definido como file_input
            with open(file, 'r', encoding="utf-8") as file_input:
        ##se toman los nombres de los textos y se le quitan los primeros 15 caracteres (el nombre de la carpeta)
                corpus[file[67:-4]]=file_input.read()
        corpus_string = str(corpus)
        print('======================================================================================================================================================')
        print('Nombre de los textos')
        print(' ')
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

    elif corpus == "salir":
        break
    else:
        continue
    
# =============================================================================
# limpieza texto
# =============================================================================
               
##Tomamos el string_corpus_misional y limpiamos una serie de impurezas típicas de la escritura en mapudungun y el trabajo con txt
##Esto lo hacemos para que las redes y los resultados del contexto sean más limpios y no dependan de la segmentación arbitraria por oraciones propuesta por el autor
##En primer lugar eliminamos los saltos de página marcados con "\n" y los marcados con "\t"
    string_corpus_contextos = str(corpus_preparado).replace('\n', ' ')
    corpus_preparado = str(corpus_preparado).replace('Â¶', '')
    corpus_preparado = str(corpus_preparado).replace('Â¿', '')
    corpus_preparado = str(corpus_preparado).replace('â', '')
    corpus_preparado = str(corpus_preparado).replace('â¦', '')
    corpus_preparado = str(corpus_preparado).replace('\t', ' ')
##luego eliminamos [r], que simboliza la duda del escritor sobre la existencia de una "r" en esa posición
    corpus_preparado = str(corpus_preparado).replace('[r]', 'r')
##eliminamos las marcas de respuesta en el texto, las que son marcadas con una "R" en el corpus
    corpus_preparado = str(corpus_preparado).replace('P.', ' ')
    corpus_preparado = str(corpus_preparado).replace('R,', ' ')
##eliminamos los marcadores de párrafo 
    corpus_preparado = str(corpus_preparado).replace('¶', ' ')
##utilizamos ambas def para eliminar puntuaciones y números del texto
    corpus_preparado = remover_numeros(str(corpus_preparado))
    corpus_preparado = remover_puntuacion(str(corpus_preparado))
##eliminamos las mayúsculas y el exceso de espacios
    corpus_preparado = str(corpus_preparado).lower()
    corpus_preparado = str(corpus_preparado).strip()

    
    
##se crea una lista utilizada exclusivamente en los contextos para evitar problemas de mixtura
    lista_corpus_contextos= []
    pre_lista_corpus_contextos = str(corpus_preparado).split(' ')
    for palabra in pre_lista_corpus_contextos:
        if len(palabra) > 0:
            lista_corpus_contextos += [palabra]
            
    corpus_preparado = str(lista_corpus_contextos)   
    corpus_preparado = remover_puntuacion(str(corpus_preparado))
            
    sin_puntos = []
    for oracion in corpus_preparado:
        oracion_limpia = remover_puntuacion(oracion)
        sin_puntos += [oracion_limpia.lower()]
    
##Se toma la lista palabras y luego se ingresan cada una de las palabras de oración que están separadas por comillas
    palabras = []
    for palabra in lista_corpus_contextos:
        palabras += [palabra]
    
    
# =============================================================================
# Búsqueda
# =============================================================================
    while True:
        busqueda = input("""
===============================================================================
Puedes buscar las nominalizaciones terminadas en -el, aquellas oraciones terminadas en -am y las construcciones seriales, para hacerlo ingresa abajo
Construcciones seriales
    * kupa          --> Para buscar las construcciones seriales con küpa
    * pepi          --> Para buscar las construcciones seriales con pepi
    * kim1          --> Para buscar las construcciones filtradas de kim
    * kim2          --> Para buscar todas las apariciones de kim
Nominalizaciones
    * el            --> para buscar las nominalizaciones terminadas en el 
    * n             --> para buscar las nominalizaciones terminadas en n
    * am            --> para buscar las nominalizaciones terminadas en am
    * lu            --> para buscar las nominalizaciones terminadas en lu
Otros
    * corpus        --> cambiar el corpus
    * cerrar        --> cerrar el programa
    
¿que deseas buscar?
""")
# =============================================================================
# pepi
# =============================================================================
        if busqueda == "pepi":
            posibilidadespepi = ["pepi"]
            pepi = []
            for item in posibilidadespepi:
                pepi+= re.findall(r"\s+"+str(item)+"+\s?[a-z]+\s+", corpus_preparado)
            print('======================================================================================================================================================')
            print("Construcciones con pepi")
            print('')
            for item in pepi:
                print(item)
            print('')
            print('Cantidad de pepi')
            print(len(pepi))
            print('======================================================================================================================================================')
# =============================================================================
# kupa
# =============================================================================
        elif busqueda == "kupa":    
            posibilidadeskupa = ["kü","qui","ki","ku", "cu", "que", "c", "cù"]
            kupa= []
            for item in posibilidadeskupa:
                kupa+= re.findall(r"\s+"+str(item)+"pa+\s?[a-z]{6,20}\s+", corpus_preparado)
            print('======================================================================================================================================================')
            print("Construcciones con küpa")
            print('')
            for item in kupa:
                print(item)
            print('')
            print('Cantidad de kupa')
            print(len(kupa))
            print('======================================================================================================================================================')
# =============================================================================
# lli (no listo)
# =============================================================================
        elif busqueda == "lli":    
            posibilidadeslli = ["lli"]
            lli= []
            for item in posibilidadeslli:
                lli+= re.findall(r"\s+"+str(item)+"pa+\s?[a-z]+\s+", corpus_preparado)
            print('======================================================================================================================================================')
            print("Construcciones con lli")
            print('')
            for item in lli:
                print(item)
            print('')
            print('Cantidad de lli')
            print(len(lli))
            print('======================================================================================================================================================')
# =============================================================================
# kim filtrado
# =============================================================================
        elif busqueda =="kim1":
            posibilidadeskim = ["kim","quim"]
            kim = []
            for item in posibilidadeskim:
                 kim+= re.findall(r"\s+"+str(item)+"+[^el][^che]\s?[a-z]{6,}\s", corpus_preparado)
            print('======================================================================================================================================================')
            print("Construcciones con kim")
            print('')
            for item in kim:
                print(item)
            print('')
            print('Cantidad de kim')
            print(len(kim))
            print('======================================================================================================================================================')
# =============================================================================
# todas las apariciones de kim  
# =============================================================================
        elif busqueda =="kim2":
            posibilidadeskim = ["kim","quim"]
            kim = []
            for item in posibilidadeskim:
                 kim+= re.findall(r"\s+"+str(item)+"+[^el][^che]\s?[a-z]+\s", corpus_preparado)
            print('======================================================================================================================================================')
            print("Construcciones con kim")
            print('')
            for item in kim:
                print(item)
            print('')
            print('Cantidad de kim')
            print(len(kim))
            print('======================================================================================================================================================')
# =============================================================================
# nominalizaciones con el
# =============================================================================
        elif busqueda == "el":
            posibilidadesel = ["ñi", "ni" ,"mi", "yu","ju", "iñ","in", "mü","mu","mv", "mün", "mun", "mvn"]
            el = []
            for item in posibilidadesel:
                el += re.findall(r"\s?[\wüñ]+[^a-df-ho-tvwxz]\st?a?"+str(item)+"\s+[\wüñ]+[^l]e?l\s", corpus_preparado)
            print('======================================================================================================================================================')
            print("Construcciones terminadas en -el")
            print('')
            for item in el:
                print(item)
            print('')
            print('Cantidad de el')
            print(len(el))
            print('======================================================================================================================================================')
# =============================================================================
# nominalizaciones con n
# =============================================================================
        elif busqueda == "n":
            posibilidades = ["ñi", "ni" ,"mi", "yu","ju", "iñ","in", "mü","mu","mv", "mün", "mun", "mvn"]
            n = []
            for item in posibilidades:
                n += re.findall(r"\s?[\wüñ]+[^a-df-ho-tvwxz]\st?a?"+str(item)+"\s+[\wüñ]+[^l][a-zü]+?n\s", corpus_preparado)
            print('======================================================================================================================================================')
            print("Construcciones terminadas en -n")
            print('')
            for item in n:
                print(item)
            print('')
            print('Cantidad de n')
            print(len(n))
            print('======================================================================================================================================================')
# =============================================================================
# nominalizaciones con am
# =============================================================================
        elif busqueda == "am":
            posibilidades = ["ñi", "ni" ,"mi", "yu","ju", "iñ","in", "mü","mu","mv", "mün", "mun", "mvn"]
            am = []
            for item in posibilidades:
                am += re.findall(r"\s?[\wüñ]+[^a-df-ho-tvwxz]\st?a?"+str(item)+"\s+[\wüñ]+[^l]am+\s", corpus_preparado)
            print('======================================================================================================================================================')
            print("Construcciones terminadas en -am")
            print('')
            for item in am:
                print(item)
            print('')
            print('Cantidad de am')
            print(len(am))
            print('======================================================================================================================================================')
# =============================================================================
# nominalizaciones con lu
# =============================================================================
        elif busqueda == "lu":
            posibilidades = ["ñi", "ni" ,"mi", "yu","ju", "iñ","in", "mü","mu","mv", "mün", "mun", "mvn"]
            lu = []
            for item in posibilidades:
                lu += re.findall(r"\s?[\wüñ]+[^a-df-ho-tvwxz]\st?a?"+str(item)+"\s+[\wüñ]+[^l]lu+\s", corpus_preparado)
            print('======================================================================================================================================================')
            print("Construcciones terminadas en -lu")
            print('')
            for item in lu:
                print(item)
            print('')
            print('Cantidad de lu')
            print(len(lu))
            print('======================================================================================================================================================')
# =============================================================================
# Duam
# =============================================================================
        elif busqueda == "duam":
            posibilidades = ["duam", "zuam"]
            duam = []
            for item in posibilidades:
                duam += re.findall(r"\s[a-z]+"+str(item)+"[\wüñ]+\s", corpus_preparado)
            print('======================================================================================================================================================')
            print("Construcciones terminadas en -lu")
            print('')
            for item in duam:
                print(item)
            print('')
            print('Cantidad de duam')
            print(len(duam))
            print('======================================================================================================================================================')
# =============================================================================
# volver a la selección de corpus 
# =============================================================================
        elif busqueda =="corpus":
            break
# =============================================================================
# cerrar programa
# =============================================================================
        elif busqueda =="cerrar":
            sys.exit()
    
input("presiona 'enter' para cerrar")


kupadt = {'Mapudungun':kupa,'Traduccion':None}
kupadf = pd.DataFrame(kupadt)
kupadf.to_csv('tercer_periodo/kupa_mi.csv', sep= ';')