# -*- coding: utf-8 -*-
from kvzawpeyvm.wvzalkawe.kellual import pepikaam_hemvl
import glob
from Limpieza import Limpieza

# =============================================================================
# 
# =============================================================================



# =============================================================================
# 
# =============================================================================
test = "Iñche küpa chillkatun"
test_list = test.split(sep= ' ')


pepikaam_hemvl('küpa')

# =============================================================================
# 
# =============================================================================

lista_files = glob.glob('C:/Users/fneir/Documents/GitHub/Linguistica/Mapudungun/ML/Textos/entrevistas_hasler/*.txt') #glob para abrir todo al mismo tiempo
corpus = {file[46:-4]: open(file,
                            'r',
                            encoding="utf-8").read() for file in lista_files} #extraer nombres
del lista_files
corpus = ' '.join(item for item in corpus.values()) #juntamos en un string
corpus = [oracion for oracion in corpus.split('\n') if len(oracion)>0] # separamos por linea


# =============================================================================
# 
# =============================================================================

texto = [oracion for oracion in corpus if oracion.startswith('\\tx ')] #extraemos el texto en mapudungun
texto = [oracion.replace('\\tx ', '').strip() for oracion in texto] #eliminamos el simbolo
texto = [Limpieza.remover_simbolos(oracion) for oracion in texto] #eliminamos simbolos extraños
texto = [oracion.split() for oracion in texto] #separamos las palabras por espacios
palabras = [elemento for lista in texto for elemento in lista] #contamos las palabras en total
tokens = set(palabras) #cantidad de tokens sin filtrar
contador = {palabra: palabras.count(palabra) for palabra in palabras} #contamos las ocurrencias de palabras

# =============================================================================
# 
# =============================================================================

anotado = [pepikaam_hemvl(item) for item in list(tokens)]



