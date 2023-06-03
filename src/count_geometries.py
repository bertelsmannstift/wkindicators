#%%
import geopandas as gpd
import pandas as pd
import os
import json
import matplotlib.pyplot as plt
print(os.getcwd())

#%%
# set cwd to project root
os.chdir('..')

#%%
with open('data/pharmacyoverpassexport.geojson', encoding='utf-8') as f:
    data = json.load(f)

pharmacies = data['features']

#%%
#gpd.GeoDataFrame(pharmacies, geometry='geometry')
pharm_geoms = pharmacies[0]["geometry"]
gdf = gpd.GeoDataFrame(pharm_geoms)
gdf.set_geometry('coordinates')

# %%


from shapely.geometry import Polygon

# Extract the properties and geometry dictionaries
data0 = data["features"][0]
properties = data0['properties']
geometry = data0['geometry']

# Create a list of dictionaries
data_list = [properties]

# Create a GeoDataFrame from the list of dictionaries
gdf = gpd.GeoDataFrame(data_list, geometry=[Polygon(geometry['coordinates'][0])], crs='EPSG:4326')

#%%
#plot
gdf.plot()

#%%

gdf = gpd.GeoDataFrame()

for i in range(0, len(pharmacies)):
    # Extract the properties and geometry dictionaries
    data_ = data["features"][i]
    properties = data_['properties']
    geometry = data_['geometry']

    # Create a list of dictionaries
    data_list = [properties]

    # Create a GeoDataFrame from the list of dictionaries
    try:
        gdf_ = gpd.GeoDataFrame(data_list, geometry=[Polygon(geometry['coordinates'][0])], crs='EPSG:4326')
        gdf = pd.concat([gdf, gdf_]).reset_index(drop=True)
    except:
        pass
    # ONLY THE FIRST GEOMETRY IS CHOSEN
# %%
#plot one row
gdf.iloc[0].geometry

#%%

#gdf1 = gpd.read_file('data/pharmacyoverpassexport.geojson', encoding='utf-8')

