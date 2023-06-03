#%%
import geopandas as gpd
import pandas as pd
import os
print(os.getcwd())

#%%
# set cwd to project root
os.chdir('..')

#%% 
# import .geojson file
pharmacies = gpd.read_file('data/pharmacyoverpassexport.geojson')


# %%

import json

with open('data/pharmacyoverpassexport.geojson', encoding='utf-8') as f:
    data = json.load(f)

pharmacies = data['features']

#%%

df = pd.DataFrame(columns=['postcode', 'name', 'geometry', 'street_number'])

for pharm in pharmacies:
    # create dataframe from each pharmacy, normalize the data, and append to list
    try:
        postcode = pharm['properties']['addr:postcode']
    except:
        postcode = None
        # SOME PHARMACIES DON'T HAVE POSTCODES

    try:
        name = pharm['properties']['name']
    except:
        name = None
    
    try:
        geometry = pharm['geometry']
    except:
        geometry = None

    try:
        street_number = pharm['properties']['addr:street'] + ' ' + pharm['properties']['addr:housenumber']
    except:
        street_number = None

    # add to dataframe
    df_ = pd.DataFrame([[postcode, name, geometry, street_number]], columns=['postcode', 'name', 'geometry', 'street_number'])
    df = pd.concat([df, df_]).reset_index(drop=True)


#%%

df_plz = pd.read_csv("data\zuordnung_plz_ort.csv")
df_plz = df_plz[['plz', 'ags', 'ort', 'landkreis', 'bundesland']]
df_plz.plz = df_plz.plz.astype(str)
df_plz.ags = df_plz.ags.astype(str)

df.dropna(subset=['postcode'], inplace=True)
df1 = df.merge(df_plz, left_on='postcode', right_on='plz', how='left')

#%%

df_counts = pd.DataFrame(df1.ags.value_counts()).reset_index()
to_merge = df_plz[['ags', 'ort', 'landkreis', 'bundesland']]
to_merge.drop_duplicates(inplace=True)
df_counts = df_counts.merge(to_merge, left_on= 'ags', right_on='ags', how='left')

# #df.groupby('postcode').count()
# df_counts = df.postcode.value_counts()

