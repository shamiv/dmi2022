import pandas as pd
import json
from mordecai import Geoparser
import six
import numpy as np

geo = Geoparser()

df=pd.read_excel("~/Documents/dmi/Instagram/Sea level rise - SC22 - Instagram dataset.xlsx","2022")

error = 0
tot=len(df.index)
add1=pd.DataFrame()
df2=pd.DataFrame()
for index, row in df.iterrows():
    print("%s/%s" % (index,tot))
    try:
        add1=pd.DataFrame.from_dict(geo.geoparse(row['Locations']))
        for j in df.columns:
            add1[j]=row[j]
        df2=df2.append(add1)
    except:
        print(row)
        error=error+1

df3=df2
df3['lat']=""
df3['lon']=""
df3['place_name']=""
df3=df3.reset_index()
indexm=0
for index2, row2 in df3.iterrows():
    try:
        lat=row2['geo']['lat']
        lon=row2['geo']['lon']
        place_name=row2['geo']['place_name']
        df3['lat'].iloc[index2]=lat
        df3['lon'].iloc[index2]=lon
        df3['place_name'].iloc[index2]=place_name
        print(index2,lat,lon,place_name)
    except:
        continue
df3=df3.drop(['spans','geo'],axis=1)

df3=df3[df3['lat'] != '']
df3.to_excel("/home/misha/Documents/dmi/new_data3/tiktok_2022.xlsx")

print(error)
