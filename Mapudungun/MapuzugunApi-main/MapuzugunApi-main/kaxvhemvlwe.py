# -*- coding: utf-8 -*-
import glob
from Limpieza import Limpieza
import kvzawpeyvm.wvzalkawe.kellual as kl
from kvzawpeyvm.wvzalkawe.koyam import Koyam
from kvzawpeyvm.rulpawirintukuwe.Reglas import reglas12
# =============================================================================
# Apertura de documentos
# =============================================================================

#glob para abrir todo al mismo tiempo
lista_files = glob.glob('C:/Users/User/Documents/GitHub/Linguistica/Mapudungun/ML/Textos/entrevistas_hasler/*.txt') 
#Extraer nombres
corpus = {file[46:-4]: open(file,'r', encoding="utf-8").read() for file in lista_files} 
del lista_files
#juntamos en un string
corpus = ' '.join(item for item in corpus.values()) 
#Separamos por linea
corpus = [oracion for oracion in corpus.split('\n') if len(oracion)>0] 

# =============================================================================
# Preparación del corpus
# =============================================================================
#extraemos el texto en mapudungun
texto = [oracion for oracion in corpus if oracion.startswith('\\tx ')] 
#eliminamos el simbolo
texto = [oracion.replace('\\tx ', '').strip() for oracion in texto]
#eliminamos simbolos extraños
texto = [Limpieza.remover_simbolos(oracion) for oracion in texto] 
#separamos las palabras por espacios
texto = [oracion.split() for oracion in texto]
#contamos las palabras en total
palabras = [elemento for lista in texto for elemento in lista] 
#cantidad de tokens sin filtrar
tokens = list(set(palabras))
#contamos las ocurrencias de palabras
contador = {palabra: palabras.count(palabra) for palabra in palabras} 

# =============================================================================
# def
# =============================================================================

def lef_pepikaam_hemvl(hemvl):
    hemvl1 = reglas12.rulpawe(hemvl.lower())
    hemvl = Koyam(hemvl1)
    hemvl.zewmakoyamvn()    
    
    hemvl.kaxvrowvn()
    hemvl = kl.kintuxokin(hemvl, 0)[0] 
    hemvlkawe = hemvl.wirintuku_hemvl2()
    hemvlkawe = [h.split('-')[1:] for h in hemvlkawe]
    
    wzkawe = hemvl.wirintuku_wz()
    wzkawe = [h.split('-')[1:] for h in wzkawe]
    inawe = [(hemvlk, wzk) for hemvlk, wzk in zip(hemvlkawe, wzkawe)]
    
    return (hemvl1,  inawe)

# =============================================================================
# Faw
# =============================================================================

pu_hemvl = {}
for index, hemvl in enumerate(tokens):
    print("Rakin:", index, hemvl)
    afichi_hemvl = lef_pepikaam_hemvl(hemvl)
    pu_hemvl[afichi_hemvl[0]] = afichi_hemvl[1]

