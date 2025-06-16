# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 16:24:58 2025

@author: User
"""
import glob

def process_corpus():
    lista_files = glob.glob('Textos/entrevistas_hasler/*.txt')
    corpus = {}
    # Abrimos el corpus
    for file in lista_files:
        with open(file, 'r', encoding="utf-8") as file_input:
            # Cortamos el path para mayor claridad
            corpus[file[46:-4]] = file_input.read()
    # Separamos los value en una lista de string por salto de página
    corpus = {key: value.split("\n") for key, value in corpus.items()}
    # Eliminamos los espacios sobrantes y dividimos cada frase en una lista
    for key in corpus:
        corpus[key] = [line.strip().split() for line in corpus[key]]
    
    for key in corpus:        
        lines = corpus[key]
        # Eliminamos los espacios en blanco
        corpus[key] = [line for line in corpus[key] if len(line) > 1]
        # Separamos la parte en mapudungun
        arn = [lines[i] for i in range(len(lines) - 1)
               if len(lines[i]) > 0 and lines[i][0].startswith("\\tx")
               # Extraemos solo las frases que cuentan con traducción y glosado
               and len(lines[i + 1]) > 0 and lines[i + 1][0].startswith("\\mb")]
        # Extraemos la segmentación propuesta, eso aún se puede mejorar
        division = [line for line in corpus[key] if line and line[0].startswith("\\mb")]
        # Extraemos las glosas
        gloss = [line for line in corpus[key] if line and line[0].startswith("\\ge")]
        # Extraemos la parte equivalente a un Pos-Tagging
        POS = [line for line in corpus[key] if line and line[0].startswith("\\ps")]
        # translation = [line for line in corpus[key] if line and line[0].startswith("\\ft")]

    # Juntamos en Tuples para que no cambien de posición
    final = list(zip(arn, division, gloss, POS))
    # Eliminamos las etiquetas
    final = [tuple(field[1:] if field else [] for field in tup) for tup in final]
    return final

# test = process_corpus()
