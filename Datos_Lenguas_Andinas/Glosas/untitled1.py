# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 17:34:55 2022

@author: fneir
"""
import re

def remover_puntuacion1(s):
    ##cada uno de los items que aparecen en esta lista
    lista_puntuaciones = '!"$%&\'()*+,;<=>?[\\^]`{|}~'
    for c in lista_puntuaciones:
        ##es eliminado del texto reemplazandolo por un espacio vacÃ­o
        s=s.replace(c,"")
        ##lo mismo se hace con "\t"
        s=s.replace('\t','')
    return s

def glosa_automatica(Y):
    texto = open(Y,encoding= 'utf-8')
    lista = []
    for item in texto:
        lista += [item]

    segmento = []
    segmento1 = []
    glosa = []
    glosa1= []
    original = []
    traduccion = []
    for linea in lista:   
        if re.findall('td class="itx_morph_txt">([1-9a-zA-Záéíóú\-ñ]*)\s</td>',linea):##Este busca el valor segmentado
            segmento1 += re.findall('td class="itx_morph_txt">([1-9ña-zA-Záéíóú\.\-]*)\s*</td>', linea)
        if re.findall('td class="itx_morph_gls">([1-9a-zA-Z\-\.áéíóúñ]*)\s<\/td>',linea):##Este busca la glosa
            glosa1 += re.findall('td class="itx_morph_gls">([1-9a-zñA-Zñ\-\.áéíóú]*)\s*<\/td>',linea)
        if re.findall('td class="itx_txt">([\da-zA-Záéíóúñ]*)\s*</td>', linea):##este if busca el original sin segmentar
            original += re.findall('td class="itx_txt">([\da-zA-Záéíóúñ]*)\s*</td>',linea)
            
            
            segmento += [remover_puntuacion1(str(segmento1))]
            segmento1 = []
            glosa += [remover_puntuacion1(str(glosa1))]
            glosa1=[]

            continue
        if re.findall('<div class="itx_Freeform_gls">([1-9a-zA-Z\(\)ñáéíóú\/\,\-\?\¿\[\]\.\s]*)\s*</div>', linea):##este if busca el original sin segmentar
            traduccion += re.findall('<div class="itx_Freeform_gls">([ñ1-9a-zA-Z\/\-\?\¿\[\]\(\)áéíóú\,\.\s]*)\s*</div>',linea)
            glosa.pop(0)
            glosa.append("CAMBIAR")
            segmento.pop(0)
            segmento.append("CAMBIAR")
            string1= ""
            glosa = ["<td>" + item + "</td>" for item in glosa]
            glosa = str(glosa)
            glosa = glosa.replace("'","")
            glosa = glosa.replace(",","")
            glosa = glosa.replace("[","")
            glosa = glosa.replace("]","")
            glosa = "<tr class='special_row'><td>Glsa</td><td> </td>"+glosa+"</tr>"

            original = ["<th>" + item + "</th>" for item in original]
            original = str(original)
            original = original.replace("'","")
            original = original.replace(",","")
            original = original.replace("[","")
            original = original.replace("]","")
            original = "<tr class='special_row'><td>Orgl</td><td> </td>"+original+"</tr>"

            segmento = ["<td>" + item + "</td>" for item in segmento]

            segmento = str(segmento)
            segmento = segmento.replace("'","")
            segmento = segmento.replace(",","")
            segmento = segmento.replace("[","")
            segmento = segmento.replace("]","")
            
            traduccion = str(traduccion)
            traduccion = traduccion.replace("'","")
            traduccion = traduccion.replace(",","")
            traduccion = traduccion.replace("[","")
            traduccion = traduccion.replace("]","")
            traduccion = "<h4>"+traduccion+"</h4>"
            
            segmento = "<tr class='special_row'><td>Sgmt</td><td> </td>"+segmento+"</tr>"
            string1 +="""  <table id="customers">\n"""    
            string1 +="    "+original+"\n"
            string1 +="    "+segmento+"\n"
            string1 +="    "+glosa+"\n"
            string1 +="  </table>\n"
            string1 +="  "+traduccion+"\n"
            break
    return string1
        
texto_final = ""
print(glosa_automatica("htm_txt/Allentiac/Txt/Credo.txt"))
texto_final += glosa_automatica("htm_txt/Allentiac/Txt/Credo.txt")
