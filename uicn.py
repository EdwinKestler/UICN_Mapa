#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on March 14 2023

@author: rainy
"""
import folium
import pandas as pd
import random
from folium.plugins import MarkerCluster, FloatImage

boulder_coords = [15.1, -91.3]
my_map = folium.Map(location = boulder_coords, zoom_start = 10, control_scale=True)

area='geojson/areasgeojson.geojson'

areaintervencion='geojson/Area_de_Intervencion.geojson'
areainfluencia='geojson/Area_de_Influencia.geojson'


estaciones=pd.read_html('https://docs.google.com/spreadsheets/d/1F6mHPGmC05MUcatz0fnHPxw_nl1K1w2rp_HrxfxNZbo/edit#gid=0', match='Estación', header=1)

estaciones=estaciones[0]


for i in range(0,14):
    
   # print(estaciones['Estación'].iloc[i])

    
    #popup = folium.Popup(iframe,parse_html=True)
    popup=estaciones['Estación'].iloc[i]
    folium.Marker([estaciones['Latitud'].iloc[i],estaciones['Longitud'].iloc[i]],
                  popup=popup
                  ).add_to(my_map) 



def random_color(feature):
    return {'fillColor': f"#{random.randint(0, 0xFFFFFF):06x}", 'color': '#000000',
                            'fillOpacity': 0.4,
                            'weight':0.8}



folium.GeoJson(
    areaintervencion, name="Área Intervención UICN",
    style_function=random_color,
#    highlight_function=random_color,
    show=(True), embed=True,
     tooltip=folium.features.GeoJsonTooltip(
        fields=['Areas'],  # use fields from the json file
        aliases=[''],
        style=("background-color: white; color: #000000; font-family: arial; font-size: 12px; padding: 10px;") 
    ), 
).add_to(my_map)


folium.GeoJson(
    areainfluencia, name="Área de influencia UICN",
    style_function=random_color,
#    highlight_function=random_color,
    show=(True), embed=True,
     tooltip=folium.features.GeoJsonTooltip(
        fields=['Areas'],  # use fields from the json file
        aliases=[''],
        style=("background-color: white; color: #000000; font-family: arial; font-size: 12px; padding: 10px;") 
    ), 
).add_to(my_map)



folium.GeoJson(
    area, name="Área de estudio ADIPO",
    style_function=random_color,
#    highlight_function=random_color,
    show=(True), embed=True,
     tooltip=folium.features.GeoJsonTooltip(
        fields=['Name'],  # use fields from the json file
        aliases=[''],
        style=("background-color: white; color: #000000; font-family: arial; font-size: 12px; padding: 10px;") 
    ), 
).add_to(my_map)




folium.LayerControl(position="bottomright").add_to(my_map)

        
logo = ("https://raw.githubusercontent.com/PeterArgueta/clima/main/logo.png")

FloatImage(logo, bottom=5, left=1, width='80px').add_to(my_map)

my_map.save("index.html")