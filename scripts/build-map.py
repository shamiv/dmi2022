import pandas as pd
from keplergl import KeplerGl
import numpy as np
import os

df_tot=pd.DataFrame()
path_of_the_directory= '/home/misha/Documents/dmi/geoparse/instagram/'
for filename in os.listdir(path_of_the_directory):
    f = os.path.join(path_of_the_directory,filename)
    if os.path.isfile(f):
        if f.endswith((".xlsx")):
            year=filename.split(".")[0]
            df = pd.read_excel(f)
            df['year']=year
            df_tot=df_tot.append(df)

df_tot=df_tot[['place_name','lat','lon','Description','Link','year']]
df_tot['Platform']="Instagram"
df_insta = df_tot



df_tot=pd.DataFrame()
path_of_the_directory= '/home/misha/Documents/dmi/geoparse/twitter/tweets/'
for filename in os.listdir(path_of_the_directory):
    f = os.path.join(path_of_the_directory,filename)
    if os.path.isfile(f):
        if f.endswith((".xlsx")):
            year=filename.split(".")[0]
            df = pd.read_excel(f)
            df['year']=year
            df_tot=df_tot.append(df)
df_tot['Link']=""
df_tot=df_tot[['place_name','lat','lon','Description','Link','year']]
df_tot['Platform']="Twitter"
df_tw = df_tot


df_tt = pd.read_excel("~/Documents/dmi/tiktok/geoparsed_tiktok_locations.xlsx")
df_tt['year']=2022
df_tt['Link']=""
df_tt['Description']=""
df_tt=df_tt[['place_name','lat','lon','Description','Link','year']]
df_tt['Platform']="TikTok"

df=pd.DataFrame()
df=df.append([df_insta,df_tw,df_tt])

df.to_excel("~/Documents/dmi/test.xlsx")


rand1=np.random.randint(100,size=len(df['lat']))/10000
rand2=np.random.randint(100,size=len(df['lat']))/10000

df = df[['lat','lon','place_name','Description','Link','year','Platform']]
df['lat'] = df['lat'] + rand1
df['lon'] = df['lon'] + rand2


config = {'version': 'v1',
 'config': {'visState': {'filters': [{'dataId': ['testmap'],
     'id': 'k6jmlio1p',
     'name': ['Platform'],
     'type': 'multiSelect',
     'value': ['Instagram'],
     'enlarged': False,
     'plotType': 'histogram',
     'animationWindow': 'free',
     'yAxis': None,
     'speed': 1}],
   'layers': [{'id': 'w16wrdg',
     'type': 'point',
     'config': {'dataId': 'testmap',
      'label': 'Point',
      'color': [18, 147, 154],
      'highlightColor': [252, 242, 26, 255],
      'columns': {'lat': 'lat', 'lng': 'lon', 'altitude': None},
      'isVisible': True,
      'visConfig': {'radius': 28,
       'fixedRadius': False,
       'opacity': 0.8,
       'outline': False,
       'thickness': 2,
       'strokeColor': None,
       'colorRange': {'name': 'Global Warming',
        'type': 'sequential',
        'category': 'Uber',
        'colors': ['#5A1846',
         '#900C3F',
         '#C70039',
         '#E3611C',
         '#F1920E',
         '#FFC300']},
       'strokeColorRange': {'name': 'Global Warming',
        'type': 'sequential',
        'category': 'Uber',
        'colors': ['#5A1846',
         '#900C3F',
         '#C70039',
         '#E3611C',
         '#F1920E',
         '#FFC300']},
       'radiusRange': [0, 50],
       'filled': True},
      'hidden': False,
      'textLabel': [{'field': None,
        'color': [255, 255, 255],
        'size': 18,
        'offset': [0, 0],
        'anchor': 'start',
        'alignment': 'center'}]},
     'visualChannels': {'colorField': {'name': 'year', 'type': 'string'},
      'colorScale': 'ordinal',
      'strokeColorField': None,
      'strokeColorScale': 'quantile',
      'sizeField': None,
      'sizeScale': 'linear'}}],
   'interactionConfig': {'tooltip': {'fieldsToShow': {'testmap': [{'name': 'place_name',
        'format': None},
       {'name': 'Description', 'format': None},
       {'name': 'Link', 'format': None},
       {'name': 'year', 'format': None},
       {'name': 'Platform', 'format': None}]},
     'compareMode': False,
     'compareType': 'absolute',
     'enabled': True},
    'brush': {'size': 0.5, 'enabled': False},
    'geocoder': {'enabled': False},
    'coordinate': {'enabled': False}},
   'layerBlending': 'normal',
   'splitMaps': [],
   'animationConfig': {'currentTime': None, 'speed': 1}},
  'mapState': {'bearing': 0,
   'dragRotate': False,
   'latitude': 34.411819314412675,
   'longitude': 39.23832278899163,
   'pitch': 0,
   'zoom': 0.9353788294523698,
   'isSplit': False},
  'mapStyle': {'styleType': 'dark',
   'topLayerGroups': {},
   'visibleLayerGroups': {'label': True,
    'road': True,
    'border': False,
    'building': True,
    'water': True,
    'land': True,
    '3d building': False},
   'threeDBuildingColor': [9.665468314072013,
    17.18305478057247,
    31.1442867897876],
   'mapStyles': {}}}}

# config = {
#     'version': 'v1',
#     'config': {
#         'mapState': {
#             'latitude': 52.373783379340104,
#             'longitude': 4.902749796405225,
#             'zoom': 2,
#         },
#     }
# }

df.update('"' + df[['year']].astype(str) + '"')

map_1=KeplerGl(height=600)

map_1.add_data(data=df, name='testmap')
map_1.config = config


map_1.save_to_html(file_name='first_map2.html')
