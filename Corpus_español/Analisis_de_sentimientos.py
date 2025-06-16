# -*- coding: utf-8 -*-

# =============================================================================
# Instalar NLTK
# =============================================================================

# pip install nltk
# nltk.download("all")

# =============================================================================
# Apertura de datos
# =============================================================================

import pandas as pd

df = pd.read_csv("") #Agregar informacion.

# =============================================================================
# Preprocesamiento
# =============================================================================

# Aanalizador de sentimientos vader (Funciona muy bien en inglés)
from nltk.sentiment.vader import SentimentIntensityAnalyzer
# Importamos las stop words
from nltk.corpus import stopwords
# Importamos el tokenizador
from nltk.tokenize import word_tokenize
# Importamos el lematizador
from nltk.stem import WordNetLemmatizer
# Traduciremos es-en para obtener mejores resultados
from deep_translator import GoogleTranslator 

def translate(text): #  Debe ser una string
    # Utilizar traductor automático
    traduccion = GoogleTranslator(source='es', target='en').translate(text)
    return traduccion  

def preprocess_text(text): # Debe ser una string
    # Tokenizar
    tokens = word_tokenize(text.lower())
    # Sacar las Stop Words
    tokens_filtrados = [token for token in tokens if token not in stopwords.words('english')]
    # Lematizar
    lematizador = WordNetLemmatizer()
    tokens_lematizados = [lematizador.lemmatize(token) for token in tokens_filtrados]
    # Juntar los tokens en una string
    texto_procesado = ' '.join(tokens_lematizados)
    return texto_procesado


# Aplicamos la funcion de traduccion a la columna que queremos analizar
df["columna a analizar"] = df["columna a analizar"].apply(translate) 

# Aplicamos la funcion de preprocesamiento a la columna que queremos analizar
df["columna a analizar"] = df["columna a analizar"].apply(preprocess_text) 
# =============================================================================
# Análisis de sentimientos
# =============================================================================

# Inicializamos el analizador
analyzer = SentimentIntensityAnalyzer()

def sentimiento(text): #  Debe ser una string
    score = analyzer.polarity_scores(text)
    sentimiento = 1 if score['pos'] > 0 else 0
    return sentimiento

# Creamos una columna nueva donde guardar los resultados de aplicar el modelo
df["columna nueva"] = df["columna a analizar"].apply(sentimiento)

# =============================================================================
# Analizar una segunda columna con el mismo modelo
# =============================================================================

# Aplicamos la funcion de traduccion a la columna que queremos analizar
df["columna a analizar 2"] = df["columna a analizar 2"].apply(translate)

# Aplicamos la funcion de preprocesamiento a la columna que queremos analizar
df["columna a analizar 2"] = df["columna a analizar 2"].apply(preprocess_text) 

# Creamos una columna nueva donde guardar los resultados de aplicar el modelo
df["columna nueva"] = df["columna a analizar 2"].apply(sentimiento)

# =============================================================================
# Terminar
# =============================================================================

# Guardar nuevo excel usando pandas
df.to_excel("Guardar excel.xlsl")