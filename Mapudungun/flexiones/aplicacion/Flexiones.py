# -*- coding: utf-8 -*-
import streamlit as st
st.title('Conjugación de verbos en mapudungun (versión 1)')

## indicativo-persona: páginas 105-106
## https://www.cepchile.cl/cep/site/docs/20160304/20160304094227/libro_Mapudungun_Fernando-Zuniga.pdf
indicativo_persona = {}

indicativo_persona['vocal i'] = {'primera':{'singular':'n', 'dual':'yu', 'plural':'iñ'},
                                 'segunda':{'singular':'mi', 'dual':'mu', 'plural':'mün'},
                                 'tercera':{'singular':'', 'dual':'ngu', 'plural':'ngün'}}

indicativo_persona['vocal no i'] = {'primera':{'singular':'n', 'dual':'yu', 'plural':'iñ'},
                                 'segunda':{'singular':'ymi', 'dual':'ymu', 'plural':'ymün'},
                                 'tercera':{'singular':'y', 'dual':'yngu', 'plural':'yngün'}}

indicativo_persona['consonante'] = {'primera':{'singular':'ün', 'dual':'iyu', 'plural':'iyiñ'},
                                 'segunda':{'singular':'imi', 'dual':'imu', 'plural':'imün'},
                                 'tercera':{'singular':'i', 'dual':'ingu', 'plural':'ingün'}}


## función vocal no i/consonante/i

def terminacion(s):
    if s.endswith('i'):
        return 'vocal i'
    elif s.endswith('a') or s.endswith('e') or s.endswith('o') or s.endswith('u') or s.endswith('ü'):
        return 'vocal no i'
    else:
        return 'consonante'

## sufijo indicativo + persona + número

def sufijo_indicativo_persona_numero(verbo, persona, numero):

    ## vocal i
    if terminacion(verbo) == 'vocal i':
        sufijo = indicativo_persona['vocal i'][persona][numero]
        return sufijo
    ## vocal no i
    elif terminacion(verbo) == 'vocal no i':
        sufijo = indicativo_persona['vocal no i'][persona][numero]
        return sufijo
    ## consonante
    else:
        sufijo = indicativo_persona['consonante'][persona][numero]
        return sufijo

## polaridad

def sufijo_polaridad(polaridad):
    if polaridad == 'positiva':
        return ''
    else:
        return 'la'

## función inflexión: puede ir creciendo

def inflexion(verbo, persona, numero, polaridad):
    ## el orden es importante: base + polaridad + indicativo/persona/número
    return verbo + sufijo_polaridad(polaridad) + sufijo_indicativo_persona_numero(verbo, persona, numero)

verbo = st.text_input('verbo:', 'küpa')
persona = st.selectbox('¿quién participa? (persona)', ['primera', 'segunda', 'tercera'], index=0)
numero = st.selectbox('¿cuántos participan? (número)', ['singular', 'dual', 'plural'], index=0)
polaridad = st.selectbox('polaridad', ['positiva','negativa'], index=1)

st.write(inflexion(verbo, persona, numero, polaridad))
