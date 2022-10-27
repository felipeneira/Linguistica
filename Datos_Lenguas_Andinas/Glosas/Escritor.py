#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Librerías
# =============================================================================
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

# =============================================================================
# 
# =============================================================================
while input("Escribir .W para continuar cualquier otro para salir ") == ".w":    
    string1 = ""
    original=[]
    segmentacion =[]
    glosa = []
    traduccion = []
    prueba = input("""
    Primero el texto original, luego la segmentación, luego la glosa y luego la traduccion
                   """)
    if prueba == "ok":
        print(' ')
        titulo = input("titulo ")
        print(' ')
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
        original = "<tr class='special_row'><td>Orgl</td><td> </td>"+original+"</tr>"
        print(' ')
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
        segmentacion = "<tr class='special_row'><td>Sgmt</td><td> </td>"+segmentacion+"</tr>"
        print(' ')
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
        glosa = "<tr class='special_row'><td>Glsa</td><td> </td>"+glosa+"</tr>"
        print(' ')
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
    elif prueba == ".cancelar":
        break
    string1 += "<h2>"+titulo+"</h2>\n"
    string1 +="""  <table id="customers">\n"""    
    string1 +="    "+original+"\n"
    string1 +="    "+segmentacion+"\n"
    string1 +="    "+glosa+"\n"
    string1 +="  </table>\n"
    string1 +="  "+traduccion+"\n"
    print(string1)
input("Presiona cualquier tecla para salir")

