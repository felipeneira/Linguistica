# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 13:56:24 2022

@author: fneir
"""
import re

prueba = open("Prueba.txt", encoding="UTF-8")
lista_prueba = []
lista_prueba2 = []
final = []
for item in prueba:
    lista_prueba+=[item]
for item in lista_prueba:
    lista_prueba2 += [re.sub("[1-9]+\.[1-9]\n","[numero]", item)]
for item in lista_prueba2:
    final += [re.sub("\n","",item)]

lista_prueba[0]
def glosa(oracion, Y,k):
    lista_contextos=[]
    for i in range(len(oracion)):
        palabra = oracion[i]
        if palabra == Y:
            r = k
            for r in range(1,k+1):

def k_anteriores(oracion,Y,k):
    lista_contextos = []
    for i in range(len(oracion)):
        word = oracion[i]
        if word == Y:
            r = k
            lista_contextos += [oracion[i:i+r]]
    return lista_contextos

k_anteriores(final,"[numero]",31)
print(re.findall("[numero]"),)
