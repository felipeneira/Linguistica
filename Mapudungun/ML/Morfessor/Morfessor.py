#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# librerias
# =============================================================================
import pandas as pd

# =============================================================================
# preparar morfessor
# =============================================================================
import morfessor
io = morfessor.MorfessorIO(encoding="utf-8",construction_separator=' ',comment_start= '#', compound_separator="\\s", atom_separator=None, lowercase= False)
cost = morfessor.baseline.AnnotatedCorpusEncoding("utf-8")
# =============================================================================
# Datos limpios
# =============================================================================
df = pd.read_csv("C:/Users/fneir/Documents/GitHub/Linguistica/Mapudungun/ML/Datos/datos_revisados.csv",sep = ";")
# =============================================================================
# pasar datos al modelo requerido por morfessor
# =============================================================================
#with open("AF2.txt", "w") as text_file:
#   for i,j in AF1.items():
#       text_file.write(i + " " + j + "\n")
# =============================================================================
# Trabajo con morfessor
# =============================================================================
# =============================================================================
# 
train_data1 = io.read_annotations_file('AF.txt', construction_separator=' ', analysis_sep=',')#palabras+segmentos
train_data = [(i,j) for i,j in train_data1.items()]
# TCF = list(io.read_corpus_file("WLF.txt"))#palabras texto plano
# WLF = io.read_segmentation_file("WLF.txt", has_counts=False)#lista palabras
# 
# 
model_tokens = morfessor.BaselineModel()
# 
# 
# model_tokens = morfessor.BaselineModel()
# 
model_tokens.load_segmentations()
model_tokens.train_batch('AF2.txt')
# 
prueba = list(model_tokens.get_segmentations())
# 
# print(model_tokens.viterbi_segment(input("Escribe la palabra: ")))

ev = morfessor.MorfessorEvaluation(AF1)
WSR = morfessor.evaluation.WilcoxonSignedRank()
resultados = [ev.evaluate_model(model_tokens)]
r = WSR.significance_test(resultados)

# =============================================================================
