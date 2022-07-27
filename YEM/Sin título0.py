#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Librerías
# =============================================================================
import networkx as nx
import matplotlib.pyplot as plt
import glob
import string
# =============================================================================
# 
# =============================================================================
##generamos una def para eliminar los puntos
def remover_puntuacion(s):
    ##cada uno de los items que aparecen en esta lista
    for c in string.punctuation:
        ##es eliminado del texto reemplazandolo por un espacio vacÃ­o
        s=s.replace(c,"")
        ##lo mismo se hace con "\t"
        s=s.replace('\t','')
    return s

##ultima def de preparacion
def remover_numeros(k):
    ##por cada item dentro de la lusta numeros
    for z in numeros:
        ##reemplazamos elitem de la lista con un vacÃ­o
        k=k.replace(z," ")
        ##tambiÃ©n eliminamos la palabra "pag", usada para marcar pÃ¡ginas junto con lo anterior
        k=k.replace('pag','')
    return k

# =============================================================================
# 
# =============================================================================
