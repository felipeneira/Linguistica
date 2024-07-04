# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 16:43:16 2024

@author: User
"""

# =============================================================================
# 
# =============================================================================
import pandas as pd
import re
datos = pd.read_csv("C:/Users/User/Downloads/CORPUS_CKUNSA.xlsx - corpus ckunsa.csv")


# =============================================================================
# 
# =============================================================================
df = datos.set_index("raiz_derivado_compuesto")
# =============================================================================
# 
# =============================================================================
raiz = df.loc['raíz']

derivado = df.loc['derivado']
compuesto = df.loc['compuesto']
pendiente = df.loc['pendiente']
sufijo = df.loc['sufijo']
reduplicacion = df.loc['reduplicación']
# =============================================================================
# 
# =============================================================================
palabras = list(datos["e"])
# =============================================================================
# palabras = re.sub("\'", "", str(palabras)) 
# palabras = re.sub(", ", " | ", str(palabras)) 
# =============================================================================
df = datos.set_index("e")
ya = [palabra for palabra in palabras if str(palabra).endswith("ya")]
ya = [df.loc[item] for item in ya]
na = [palabra for palabra in palabras if str(palabra).endswith("na")]

ps = [palabra for palabra in palabras if str(palabra).endswith("ps") or str(palabra).endswith("pas")]

tur = [palabra for palabra in palabras if str(palabra).endswith("tur")]

sa = [palabra for palabra in palabras if str(palabra).endswith("sa")]

cu = na = [palabra for palabra in palabras if str(palabra).endswith("cu") or str(palabra).endswith("cku")]


