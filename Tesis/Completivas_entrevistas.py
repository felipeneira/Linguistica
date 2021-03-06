#!/usr/bin/env python3
# =============================================================================
# Librerías Usadas
# =============================================================================
import glob
import re
import string
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
    ##se prepara la lista glob que sirve para trabajar con carpetas
    corpus = input("""
Corpus para buscar

misional        --> mi          (Valdivia 1606, 1626, Febrés 1765)

etnografico     --> et          (Lenz 1863-1938, Manquilef 1914, 1911)

entrevistas     --> fh          (Entrevistas Tesis Felipe Hasler)

¿En que período deseas buscar? 
""")
    ## se define que lista_files es una lista con los nombres de los archivos 
    ##los cuales están seleccionados como los txt que se encuentran dentro de primer periodo
    if corpus == "fh":
        lista_files = glob.glob('/home/felipe/Documentos/GitHub/Linguistica/Lingüística Computacional Final/Periodo cotejo/Entrevistas Hasler/*.txt')
        corpus = {}
        ##por cada archivo en la lista de archivos
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
        print(corpus.keys()) 
    
    
    
    elif corpus == "mi":
        lista_files = glob.glob('/home/felipe/Documentos/GitHub/Linguistica/Lingüística Computacional Final/Primer periodo/Primer periodo/*.txt')
        corpus = {}
        ##por cada archivo en la lista de archivos
        for file in lista_files:
        ##este se abre con encoding utf-8 y queda definido como file_input
            with open(file, 'r', encoding="utf-8") as file_input:
        ##se toman los nombres de los textos y se le quitan los primeros 15 caracteres (el nombre de la carpeta)
                corpus[file[105:-4]]=file_input.read()
        print('Nombre de los textos')
        print(corpus.keys())  
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
    
    
    elif corpus == "et":
        lista_files = glob.glob('/home/felipe/WINDOWS/Papers, investigaciones y libros/Textos mapudungun/Convertibles/Transcripciones/*.txt')
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
        print('Nombre de los textos')
        print(corpus.keys()) 
    
    if corpus == "salir":
        break
    
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
##eliminamos la marcación que señala que el texto está escrito en mapudungun, esta marcación es propia de estas entrevistas en particular
    corpus_preparado = str(corpus_preparado).replace('\\tx ', ' ')
    corpus_preparado = str(corpus_preparado).replace('tx', ' ')
    
    
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
    * corpus         --> cerrar el programa
    
¿que deseas buscar?
""")
        if busqueda == "pepi":
            posibilidadespepi = ["pepi"]
            pepi = []
            for item in posibilidadespepi:
                pepi+= re.findall(r"\s+"+str(item)+"+\s?[a-z]+\s+", corpus_preparado)
            print("Construcciones con pepi")
            print('')
            print(pepi)
            print('')
            print('Cantidad de pepi')
            print('pepi')
        elif busqueda == "kupa":    
            posibilidadeskupa = ["kü","qui","ki","ku", "cu", "que", "c", "cù"]
            kupa= []
            for item in posibilidadeskupa:
                kupa+= re.findall(r"\s+"+str(item)+"pa+\s?[a-z]+\s+", corpus_preparado)
            print("Construcciones con küpa")
            print('')
            print(kupa)
            print('')
            print('Cantidad de kupa')
            print(len(kupa))
        elif busqueda =="kim1":
            posibilidadeskim = ["kim","quim"]
            kim = []
            for item in posibilidadeskim:
                 kim+= re.findall(r"\s+"+str(item)+"+[^el][^che]\s?[a-z]{6,}\s", corpus_preparado)
            print("Construcciones con kim")
            print('')
            print(kim)
            print('')
            print('Cantidad de kim')
            print(len(kim))
        elif busqueda =="kim2":
            posibilidadeskim = ["kim","quim"]
            kim = []
            for item in posibilidadeskim:
                 kim+= re.findall(r"\s+"+str(item)+"+[^el][^che]\s?[a-z]+\s", corpus_preparado)
            print("Construcciones con kim")
            print('')
            print(kim)
            print('')
            print('Cantidad de kim')
            print(len(kim))
        elif busqueda == "el":
            posibilidadesel = "ñi", "ni" ,"mi", "yu","ju", "iñ","in", "mü","mu","mv", "mün", "mun", "mvn"
            el = []
            for item in posibilidadesel:
                el += re.findall(r"\s?[\wüñ]+[^a-df-ho-tvwxz]\st?a?"+str(item)+"\s+[\wüñ]+[^l]e?l\s", corpus_preparado)
            print("Construcciones terminadas en -el")
            print('')
            print(el)
            print('')
            print('Cantidad de el')
            print(len(el))
        elif busqueda == "n":
            posibilidades = "ñi", "ni" ,"mi", "yu","ju", "iñ","in", "mü","mu","mv", "mün", "mun", "mvn"
            n = []
            for item in posibilidades:
                n += re.findall(r"\s?[\wüñ]+[^a-df-ho-tvwxz]\st?a?"+str(item)+"\s+[\wüñ]+[^l][a-zü]+?n\s", corpus_preparado)
            print("Construcciones terminadas en -n")
            print('')
            print(n)
            print('')
            print('Cantidad de n')
            print(len(n))
        elif busqueda == "am":
            posibilidades = "ñi", "ni" ,"mi", "yu","ju", "iñ","in", "mü","mu","mv", "mün", "mun", "mvn"
            am = []
            for item in posibilidades:
                am += re.findall(r"\s?[\wüñ]+[^a-df-ho-tvwxz]\st?a?"+str(item)+"\s+[\wüñ]+[^l]am+\s", corpus_preparado)
            print("Construcciones terminadas en -am")
            print('')
            print(am)
            print('')
            print('Cantidad de am')
            print(len(am))
        elif busqueda == "lu":
            posibilidades = "ñi", "ni" ,"mi", "yu","ju", "iñ","in", "mü","mu","mv", "mün", "mun", "mvn"
            lu = []
            for item in posibilidades:
                lu += re.findall(r"\s?[\wüñ]+[^a-df-ho-tvwxz]\st?a?"+str(item)+"\s+[\wüñ]+[^l]lu+\s", corpus_preparado)
            print("Construcciones terminadas en -lu")
            print('')
            print(lu)
            print('')
            print('Cantidad de lu')
            print(len(lu))
        elif busqueda =="corpus":
            break
        elif busqueda =="salir":
            break
    
input("presiona cualquier tecla para cerrar")



