# =============================================================================
# librerías 
# =============================================================================
#hacer redes
#pip install networkx
import networkx as nx
#herramienta para plotear
#pip install matplotlib
import matplotlib.pyplot as plt
#pip install scipy
import scipy as sp
##se prepara la lista glob que sirve para trabajar con carpetas
import glob
##importamos string para la limpieza de los textos
import string

# =============================================================================
# def
# =============================================================================
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

## Red de co-ocurrencias entre palabras :)

def GoW(text_clean):
    
    G=nx.Graph()
    for sentence in text_clean:
        if len(sentence)>1:
            pairs=list(zip(sentence,sentence[1:]))
            for pair in pairs:
                if G.has_edge(pair[0],pair[1])==False:
                    G.add_edge(pair[0],pair[1],weight=1)
                else:
                    x=G[pair[0]][pair[1]]['weight']
                    G[pair[0]][pair[1]]['weight']=x+1
                    
    Gcc = sorted(nx.connected_components(G), key=len, reverse=True)
    G0 = G.subgraph(Gcc[0])
    
    return G0

#Plotear el jpg
def plotG_centrality(Y,size):
    
    G = grafos[Y]
    #G0 = G.copy()
    #G0.remove_edges_from(nx.selfloop_edges(G0))
    #G = nx.k_core(G0)
    #G = nx.maximum_spanning_tree(G)
    fig, ax = plt.subplots(dpi=800)
    centrality = nx.pagerank(G,weight='weight')
    ordered_centrality = {k: v for k, v in sorted(centrality.items(), key=lambda item: item[1],reverse=True)}
    labels = {i:i for i in G.nodes() if i in list(zip(*list(ordered_centrality.items())[:100]))[0]}
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size = [size*x for x in list(centrality.values())], node_color='gold',node_shape='o',alpha=0.95, linewidths=0.1) 
    nx.draw_networkx_edges(G, pos, alpha=0.5,width=0.2,edge_color='k')
    nx.draw_networkx_labels(G,pos,labels,alpha=1,font_size=3.,font_color='k',font_family='monospace')
    plt.title('Red {}'.format(Y),fontsize=8)
    plt.savefig('red_{}.jpg'.format(Y), format='jpg', transparent=True, bbox_inches='tight',dpi=800)
    plt.axis('off')
    plt.show()
# =============================================================================
# Preparación
# =============================================================================

## se define que lista_files es una lista con los nombres de los archivos 
##los cuales están seleccionados como los txt que se encuentran dentro de primer periodo
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
##esto último con el objetivo de corroborar si el programa lee todos los textos de forma correcta

##abrimos una lista con números con el fin de poder eliminar de forma más fácil los caracteres numéricos
numeros= []
##cada uno de los números de este rango
for numero in list(range(100)):
    ##lo añadimos a una lista    
    numeros+= [numero]
##la cuál definimos como un string
numeros = str(numeros)
numeros

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
string_corpus_contextos = string_corpus_contextos.replace('¿', '')
string_corpus_contextos = string_corpus_contextos.replace('“', '')
string_corpus_contextos = string_corpus_contextos.replace('…', '')
 
##Se define una lista como vacio para poder ingresar cada una de las oraciones del corpus sin espacios en blanco
vacio=[oracion for oracion in string_corpus_misional if len(oracion)>0]

##por cada una de estas oraciones en vacio se le saca la puntuación y se bajan las mayúsculas
sin_puntos = []
for oracion in vacio:
    oracion_limpia = remover_puntuacion(oracion)
    sin_puntos += [oracion_limpia.lower()]

##Se toma la lista palabras y luego se ingresan cada una de las palabras de oración que están separadas por comillas
palabras = []
for oracion in sin_puntos:
    palabras += [oracion.split(' ')]

# =============================================================================
# 
# =============================================================================

diccionario_contextos_presentacion = {'yem':[],'em':[]} 

##añadiremos al diccionario anterior las apariciones de yem/em/ema y las cuatro palabras anteriores, consideramos que es un buen número de palabras para inferir el significado
lista_yem_presentacion = k_anteriores(lista_corpus_contextos,'yem',3)
lista_em_presentacion = k_anteriores(lista_corpus_contextos,'em',3)

diccionario_contextos_presentacion['yem'] = lista_yem_presentacion
diccionario_contextos_presentacion['em'] = lista_em_presentacion


diccionario_contextos_presentacion

# =============================================================================
# 
# =============================================================================
##creamos por comodidad un diccionario que incluya solamente la palabra usada junto a yem/em/ema para poder estudiar su sintaxis
palabra_anterior_presentacion = {'yem':[],'ema':[],'em':[]} 
indices_yem = []
for palabra in range(len(lista_corpus_contextos)):
    if lista_corpus_contextos[palabra] == 'yem':
        indices_yem.append(palabra)
indices_em = []
for palabra in range(len(lista_corpus_contextos)):
    if lista_corpus_contextos[palabra] == 'em':
        indices_em.append(palabra)
indices_ema = []
for palabra in range(len(lista_corpus_contextos)):
    if lista_corpus_contextos[palabra] == 'ema':
        indices_ema.append(palabra)
Yem_indices = {'yem':[],'ema':[],'em':[]} 

Yem_indices['yem'] = indices_yem
Yem_indices['em'] = indices_em
Yem_indices['ema'] = indices_ema

# =============================================================================
# 
# =============================================================================
grafos = {}

for Y in diccionario_contextos_presentacion.keys():
    oraciones = diccionario_contextos_presentacion[Y]
    grafos[Y]=GoW(oraciones)
grafos['yem'].edges(data=True)


for Y in grafos.keys():
    plotG_centrality(Y,250)



