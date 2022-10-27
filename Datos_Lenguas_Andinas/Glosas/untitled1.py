# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 17:34:55 2022

@author: fneir
"""
import re

def glosa_automática(texto):
    texto = open("htm_txt/AveMaria.txt")
    return

lista = []
for item in texto:
    lista += [item]
segmento = []
glosa = []
original = []
for linea in lista:
    if re.findall('td class="itx_morph_txt">([1-9a-zA-Z\-]*)\s</td>',linea):##Este busca el valor segmentado
        segmento += re.findall('td class="itx_morph_txt">([1-9a-zA-Z\-]*)\s*</td>', linea)
    if re.findall('td class="itx_morph_gls">([1-9a-zA-Z\-]*)\s</td>',linea):##Este busca la glosa
        glosa += re.findall('td class="itx_morph_gls">([1-9a-zA-Z\-]*)\s*</td>',linea)
    if re.findall('td class="itx_txt">([\da-zA-Z]*)\s*</td>', linea):##este if busca el original sin segmentar
        original += re.findall('td class="itx_txt">([\da-zA-Z]*)\s*</td>',linea)
        break
    if re.findall('<div class="itx_Freeform_gls">([1-9a-zA-Z\(\)áéíóú\,\.\s]*)\s*</div>', linea):##este if busca el original sin segmentar
        original += re.findall('<div class="itx_Freeform_gls">([1-9a-zA-Z\(\)áéíóú\,\.\s]*)\s*</div>',linea)
        break
re.findall('<div class="itx_Freeform_gls">([1-9a-zA-Z\(\)áéíóú\,\.\s]*)\s*</div>',lista[219])
