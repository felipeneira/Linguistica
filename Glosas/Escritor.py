#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Librerías
# =============================================================================
import re
import string
# =============================================================================
# 
# =============================================================================
def remover_puntuacion(s):
    ##cada uno de los items que aparecen en esta lista
    for c in string.punctuation:
        ##es eliminado del texto reemplazandolo por un espacio vacÃ­o
        s=s.replace(c,"")
        ##lo mismo se hace con "\t"
        s=s.replace('\t','')
    return s
# =============================================================================
# 
# =============================================================================
texto = ['prueba','de','mecanismo']

texto=str(texto)

texto = remover_puntuacion(texto)
texto

# =============================================================================
# 
# =============================================================================
original=[]
segmentacion =[]
glosa = []
traduccion = []
prueba = input("""
Primero el texto original, luego la segmentación, luego la glosa y luego la traduccion
               """)
if prueba != ".cancelar":
    titulo = input("titulo")
    print("original")
    while ".fin" not in original:
        original += [input()]
    original = ["<th>" + item + "</th>" for item in original]
    del original[-1]
    original = str(original)
    original = original.replace("'","")
    original = original.replace(",","")
    original = original.replace("[","")
    original = original.replace("]","")
    original = "<tr><th>Orgl</th><th> </th>"+original+"</tr>"
    print("segmentacion")
    while ".fin" not in segmentacion:
        segmentacion += [input()]
    segmentacion = ["<td>" + item + "</td>" for item in segmentacion]
    del segmentacion[-1]
    segmentacion = str(segmentacion)
    segmentacion = segmentacion.replace("'","")
    segmentacion = segmentacion.replace(",","")
    segmentacion = segmentacion.replace("[","")
    segmentacion = segmentacion.replace("]","")
    segmentacion = "<tr><td>Sgmt</td><td> </td>"+segmentacion+"</tr>"
    print("glosa")
    while ".fin" not in glosa:
        glosa += [input()]
    glosa = ["<td>" + item + "</td>" for item in glosa]
    del glosa[-1]
    glosa = str(glosa)
    glosa = glosa.replace("'","")
    glosa = glosa.replace(",","")
    glosa = glosa.replace("[","")
    glosa = glosa.replace("]","")
    glosa = "<tr><td>Glsa</td><td> </td>"+glosa+"</tr>"
    print("traduccion")
    while ".fin" not in traduccion:
        traduccion += [input()]
    del traduccion[-1]
    traduccion = str(traduccion)
    traduccion = traduccion.replace("'","")
    traduccion = traduccion.replace(",","")
    traduccion = traduccion.replace("[","")
    traduccion = traduccion.replace("]","")
    traduccion = "<h4>"+traduccion+"</h4>"
print("<h2>"+titulo+"</h2>")
print("""  <table id="customers">""")    
print("    "+original)
print("    "+segmentacion)
print("    "+glosa)
print("  </table>")
print("  "+traduccion)

