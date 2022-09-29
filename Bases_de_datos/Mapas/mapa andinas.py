# =============================================================================
# =============================================================================
# lenguas_areas         Todas las lenguas / WALS
# lenguas_Ricardo       Lenguas de Sudamérica / Muestra Ricardo
# andean_languagues     Lenguas andinas / Muestra Ricardo
# areas                 Areas de las lenguas /Muestra Ricardo
# lenguas               Lenguas de Sudamérica / WALS
# lenguas_wals          Lenguas andinas / WALS
# lenguitas             Lenguas Sudamérica / WALS / Muestra WALS 
# lenguitas2            Lenguas Andinas / WALS / Muestra Ricardo 
# lenguitas3            Lenguas Sudamérica / Datos Ricardo / Muestra Ricardo
# lenguitas4            Lenguas Andinas / Datos Ricardo /Muestra Ricardo 
# lenguitas5            Lenguas andinas corregidas / Datos mezclados
# quechua               Lista de quechuas del WALS
# =============================================================================
# =============================================================================

# =============================================================================
# =============================================================================
# =============================================================================
# IMPORTANTE:
#
# En lenguitas5 se añadieron las lenguas andinas del corpus de Ricardo más
# la lista de quechuas que propone el WALS (Excluyendo aquellos dentro de 
# la muestra), además se corrigieron los siguientes errores:
#   -Se añadió el aymara debido a que el Glottocode era diferente
#   -Se añadió el Cholón que no poseía Glottocode
#   -Se añadieron los datos del Ricardo para lenguas que no aparecían en WALS
#
# =============================================================================
# =============================================================================
# =============================================================================
# Librerías
import geopandas
import pandas as pd
from shapely.geometry import Point
import matplotlib.pyplot as plt
# =============================================================================
# =============================================================================
# Datos
# =============================================================================
# =============================================================================

# =============================================================================
# Abrir Datos
# =============================================================================
lenguas_Ricardo = pd.read_csv('Datos/andean languages.csv', on_bad_lines='skip', sep=';')
areas = pd.read_csv('Datos/areas.csv',sep=',')
lenguas_areas = pd.read_csv("Datos/languages.csv",sep=',',encoding='utf-8')

# =============================================================================
# Lenguas andinas en datos Ricardo
# =============================================================================
andes =['Andes']
andean_languages = lenguas_Ricardo[lenguas_Ricardo.Región_Lengua.isin(andes)]
# =============================================================================
# Lenguas de Sudamérica en datos WALS
# =============================================================================
Sudamerica = ['South America']
sudamerica_wals= lenguas_areas[lenguas_areas.Macroarea.isin(Sudamerica)]
lenguas= lenguas_areas[lenguas_areas.Macroarea.isin(Sudamerica)]
ID_lenguas_sudamerica= lenguas[['ID','Name','Glottocode']]
# =============================================================================
# Lenguas andinas en WALS
# =============================================================================
lenguas_wals= lenguas_areas[lenguas_areas.Glottocode.isin(list(andean_languages['GlottoCode']))]

# =============================================================================
# =============================================================================
# # Preparar datos mapa
# =============================================================================
# =============================================================================
##Genero mapa de sudamerica
world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
world = world[world['continent']=='South America']
x = lenguas['Longitude'].values
y = lenguas['Latitude'].values
codes = lenguas['ID'].values
# =============================================================================
# Marcar lenguas de Sudamérica / Datos del Wals / Muestra de Wals
# =============================================================================
sudamerica_wals['coordinates'] = sudamerica_wals[['Longitude','Latitude']].values.tolist()
sudamerica_wals['coordinates'] = sudamerica_wals['coordinates'].apply(Point)
lenguitas = geopandas.GeoDataFrame(sudamerica_wals, geometry = 'coordinates')
# =============================================================================
# Marcar lenguas andinas / Datos de Wals / Muestra de Ricardo
# =============================================================================
lenguas_wals['coordinates'] = lenguas_wals[['Longitude','Latitude']].values.tolist()
lenguas_wals['coordinates'] = lenguas_wals['coordinates'].apply(Point)
lenguitas2 = geopandas.GeoDataFrame(lenguas_wals, geometry = 'coordinates')
# =============================================================================
# Marcar lenguas de Sudamérica / Datos Ricardo / Muestra de Ricardo
# =============================================================================
lenguas_Ricardo['coordinates'] = lenguas_Ricardo[['Latitud','Longitud']].values.tolist()
lenguas_Ricardo['coordinates'] = lenguas_Ricardo['coordinates'].apply(Point)
lenguitas3 = geopandas.GeoDataFrame(lenguas_Ricardo,geometry= 'coordinates')
# =============================================================================
# Marcar lenguas andinas / Datos Ricardo / Muestra de Ricardo
# =============================================================================
andean_languages['coordinates'] = andean_languages[['Latitud','Longitud']].values.tolist()
andean_languages['coordinates'] = andean_languages['coordinates'].apply(Point)
lenguitas4 = geopandas.GeoDataFrame(andean_languages, geometry = 'coordinates')

# =============================================================================
# =============================================================================
# # Propuesta correcciones lenguas andinas
# =============================================================================
# =============================================================================
andinas = lenguas_wals[['Name','Glottocode','coordinates','Longitude','Latitude']]
# =============================================================================
# Agregar quechuas
# =============================================================================
quechua = ['Quechuan']
quechua = lenguas_areas[lenguas_areas.Family.isin(quechua)]
quechua['coordinates'] = quechua[['Longitude','Latitude']].values.tolist()
quechua['coordinates'] = quechua['coordinates'].apply(Point)
quechua = quechua[['Name','Glottocode','coordinates','Longitude','Latitude']]
# =============================================================================
# Agregar aymara
# =============================================================================
aymara = ['cent2142']
aymara = lenguas_areas[lenguas_areas.Glottocode.isin(aymara)]
aymara['coordinates'] = aymara[['Longitude','Latitude']].values.tolist()
aymara['coordinates'] = aymara['coordinates'].apply(Point)
aymara = aymara[['Name','Glottocode','coordinates', 'Longitude','Latitude']]
# =============================================================================
# Agregar Cholón
# =============================================================================
cholon = ['Cholon']
cholon = lenguas_areas[lenguas_areas.Family.isin(cholon)]
cholon['coordinates'] = cholon[['Longitude','Latitude']].values.tolist()
cholon['coordinates'] = cholon['coordinates'].apply(Point)
cholon = cholon[['Name','Glottocode','coordinates','Longitude','Latitude']]
# =============================================================================
# Agregar lenguas existentes en corpus Ricardo y no en WALS
# =============================================================================
faltan = ['Yauyos Quechua','Pacaraos Quechua','Santiago del Estero Quechua', 'Millcayac']
faltan = andean_languages[andean_languages.Nombre_Lengua.isin(faltan)]
formato = faltan[['Nombre_Lengua','GlottoCode','Longitud','Latitud']]
formato['coordinates'] = formato[['Latitud','Longitud']].values.tolist()
formato['coordinates'] = formato['coordinates'].apply(Point)
faltan = formato.rename(columns={'Nombre_Lengua':'Name','GlottoCode':'Glottocode','Longitud':'Longitude', 'Latitud': 'Latitude'})

# =============================================================================
# Marcar lenguas andinas / Datos Mezclados / Muestras Mezcladas
# =============================================================================
andinas = pd.concat([andinas,faltan, quechua, aymara, cholon], ignore_index= True, axis = 0)
andinas = andinas.drop([7,8],axis=0)
lenguitas5 = geopandas.GeoDataFrame(andinas,geometry= 'coordinates')

# =============================================================================
# Mapa
#
# IMPORTANTE:
# Poner un símbolo "#" antes de lo que se quiere dejar fuera del mapa
# Sacar el símbolo "#" para ingresar los datos en el mapa
#  
# =============================================================================
fig, ax = plt.subplots(dpi=800)
ax.set_aspect('equal')
plt.title('Languages of South America (WALS)',fontsize=7)
world.plot(ax=ax, color='white', edgecolor='black',linewidth=0.6)
# =============================================================================
# Variante      -->     Lenguas     /   Datos    /    Muestra
#
# lenguitas     -->     Sudamérica  /   WALS     /    WALS 
# lenguitas3    -->     Sudamérica  /   Ricardo  /    Ricardo
# =============================================================================

lenguitas.plot(ax=ax, marker='o', markersize=5, edgecolor='black',linewidth=0.2, alpha= 0.8 ,label='Languages of South America')

#lenguitas3.plot(ax=ax, marker='o', markersize=5,label='Lenguas Sudamérica')

# =============================================================================
# Variante      -->     Lenguas     /   Datos       /   Muestra
#
# lenguitas4    -->     Andinas     /   Ricardo     /   Ricardo  
# lenguitas5    -->     Andinas     /   Mixto       /   Mixta
# =============================================================================

#lenguitas4.plot(ax=ax, marker='x', color= 'red', markersize=5,label='Lenguas Andinas')

lenguitas5.plot(ax=ax, marker='o', color= 'red', markersize=25, edgecolor='black',linewidth=0.8 , label='Andean Languages')

# =============================================================================
# Variante      -->     Lenguas     /   Datos       /    Muestra
#
# lenguitas2    -->     Andinas     /   WALS        /   Ricardo
# =============================================================================

#lenguitas2.plot(ax=ax, marker='x', color= 'black', markersize=15,label='Lenguas Muestra')

ax.set_yticks([])
ax.set_xticks([])

# =============================================================================
# =============================================================================
# # Nombres lenguas
# =============================================================================
# =============================================================================

# =============================================================================
D = {}
for i in range(len(list(andinas['Name']))):
    D[list(andinas['Name'])[i]] = list(andinas['coordinates'])[i]
x = andinas['Longitude'].values
y = andinas['Latitude'].values
for i in range(len(D.keys())):
    ax.annotate(list(D.keys())[i], weight='demi', color='k', xy=(x[i],y[i]), fontsize=4)
# 
# =============================================================================

plt.legend(loc='best',fontsize=7)

plt.savefig(r'figuras/lenguas_sudamerica1.jpg', format='jpg', transparent=True, bbox_inches='tight',dpi=800)
