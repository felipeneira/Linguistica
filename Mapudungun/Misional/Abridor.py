#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

with open("/home/felipe/Descargas/Sermones.txt", 'r', encoding="utf-8") as file_input:
    texto = file_input.read()
texto = texto.split('\n')
mapudungun = [re.findall(r"MORPH: ([a-zA-züñ\-\(\)]*)<",fila) for fila in texto]
mapudungun = [str(palabra) for palabra in mapudungun if len(palabra) > 0]
mapudungun = [palabra[2:-2] for palabra in mapudungun]
segmentacion = [palabra for palabra in mapudungun if len(palabra)>0]
segmentacion = [re.sub("iy","y",palabra) for palabra in segmentacion]
segmentacion = [re.sub("\(","",palabra) for palabra in segmentacion]
segmentacion = [re.sub("\)","",palabra) for palabra in segmentacion]
segmentacion = [palabra.split("-") for palabra in segmentacion]

mapudungun = [re.sub("-","",palabra) for palabra in mapudungun]
mapudungun = [re.sub("iy","y",palabra) for palabra in mapudungun]
mapudungun = [re.sub("\(ü\)","",palabra) for palabra in mapudungun]
mapudungun = [re.sub("\(","",palabra) for palabra in mapudungun]
mapudungun = [re.sub("\)","",palabra) for palabra in mapudungun]
mapudungun = [palabra for palabra in mapudungun if len(palabra)>0]


