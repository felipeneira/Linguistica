# =============================================================================
# librerÃ­as 
# =============================================================================
##Importar RegEx
import re
## importar librería que permite trabajar con muchos archivos de texto
import glob
##importamos string para la limpieza de los textos
import string

# =============================================================================
# def
# =============================================================================
## funciÃ³n para detectar k palabras anteriores


##generamos una def para eliminar los puntos
def remover_puntuacion(s):
    ##cada uno de los items que aparecen en esta lista
    for c in string.punctuation:
        ##es eliminado del texto reemplazandolo por un espacio vacÃ­o
        s=s.replace(c,"")
        ##lo mismo se hace con "\t"
        s=s.replace('\t','')
    return s

##Ãºltima def de preparaciÃ³n
def remover_numeros(k):
    ##por cada item dentro de la lusta numeros
    for z in numeros:
        ##reemplazamos elitem de la lista con un vacÃ­o
        k=k.replace(z," ")
        ##tambiÃ©n eliminamos la palabra "pag", usada para marcar pÃ¡ginas junto con lo anterior
        k=k.replace('pag','')
    return k

# =============================================================================
# PreparaciÃ³n
# =============================================================================

## se define que lista_files es una lista con los nombres de los archivos 
##los cuales estÃ¡n seleccionados como los txt que se encuentran dentro de primer periodo
lista_files = glob.glob('/home/felipe/WINDOWS/Papers, investigaciones y libros/Textos mapudungun/Convertibles/Transcripciones/*.txt')
##se define un diccionario donde en los keys se encuentran los nombres y en los values el texto
corpus = {}
##por cada archivo en la lista de archivos
for file in lista_files:
##este se abre con encoding utf-8 y queda definido como file_input
    with open(file, 'r', encoding="utf-8") as file_input:
##se toman los nombres de los textos y se le quitan los primeros 15 caracteres (el nombre de la carpeta)
        corpus[file[101:-4]]=file_input.read()
print('Nombre de los textos')
print(corpus.keys())    
##esto Ãºltimo con el objetivo de corroborar si el programa lee todos los textos de forma correcta

##abrimos una lista con nÃºmeros con el fin de poder eliminar de forma mÃ¡s fÃ¡cil los caracteres numÃ©ricos
numeros= []
##cada uno de los nÃºmeros de este rango
for numero in list(range(100)):
    ##lo aÃ±adimos a una lista    
    numeros+= [numero]
##la cuÃ¡l definimos como un string
numeros = str(numeros)
numeros

#toma el corpus subido y crea una lista vacÃ­a
corpus_misional = []
##por cada uno de los keys en corpus.keys se agrega a corpus_misional el value
for key in corpus.keys():
    corpus_misional += [corpus[key]]

## se hace un string para poner todos los values de corpus con el objetivo de trabajarlo como un solo texto grande
string_corpus_misional=' '.join(corpus_misional)

##Tomamos el string_corpus_misional y limpiamos una serie de impurezas tÃ­picas de la escritura en mapudungun y el trabajo con txt
##En primer lugar eliminamos los saltos de pÃ¡gina marcados con "\n" y los marcados con "\t"
string_corpus_contextos = string_corpus_misional.replace('\n', ' ')
string_corpus_contextos = string_corpus_contextos.replace('\t', ' ')
##luego eliminamos [r], que simboliza la duda del escritor sobre la existencia de una "r" en esa posiciÃ³n
string_corpus_contextos = string_corpus_contextos.replace('[r]', 'r')
##eliminamos los marcadores de pÃ¡rrafo 
string_corpus_contextos = string_corpus_contextos.replace('Â¶', '')
##utilizamos ambas def para eliminar puntuaciones y nÃºmeros del texto
string_corpus_contextos = remover_numeros(string_corpus_contextos)
string_corpus_contextos = remover_puntuacion(string_corpus_contextos)
##eliminamos las marcas de pregunta y respuesta en el texto, las que son marcadas con una "P" y "R" en el corpus
string_corpus_contextos = string_corpus_contextos.replace('P ', '')
string_corpus_contextos = string_corpus_contextos.replace('R ', '')
##eliminamos las mayÃºsculas y el exceso de espacios
string_corpus_contextos = string_corpus_contextos.lower()
string_corpus_contextos = string_corpus_contextos.strip()
##lista exclusiva para graficaciÃ³n
lista_corpus_contextos = string_corpus_contextos.split(' ')
##luego se usa .split para dividir el texto por \n
string_corpus_misional = string_corpus_misional.split('\n')
string_corpus_contextos = string_corpus_contextos.replace('Â¿', '')
string_corpus_contextos = string_corpus_contextos.replace('â', '')
string_corpus_contextos = string_corpus_contextos.replace('â¦', '')
 
##Se define una lista como vacio para poder ingresar cada una de las oraciones del corpus sin espacios en blanco
vacio=[oracion for oracion in string_corpus_misional if len(oracion)>0]

##por cada una de estas oraciones en vacio se le saca la puntuaciÃ³n y se bajan las mayÃºsculas
sin_puntos = []
for oracion in vacio:
    oracion_limpia = remover_puntuacion(oracion)
    sin_puntos += [oracion_limpia.lower()]

##Se toma la lista palabras y luego se ingresan cada una de las palabras de oraciÃ³n que estÃ¡n separadas por comillas
palabras = []
for oracion in sin_puntos:
    palabras += [oracion.split(' ')]

# =============================================================================
# RegEx
# =============================================================================
posibilidades = "ñi", "ni" ,"mi", "yu","ju", "iñ","in", "mü","mu","mv", "mün", "mun", "mvn"
x = []
for item in posibilidades:
    x += re.findall(r"\s?[\wüñ]+[^a-df-ho-tvwxz]\st?a?"+str(item)+"\s+[\wüñ]+[^l]e?l\s", string_corpus_contextos)
