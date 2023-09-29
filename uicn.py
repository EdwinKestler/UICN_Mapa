import folium
import pandas as pd
import random
from folium.plugins import FloatImage
import geojson
import json

def random_color(feature):
    return {
        'fillColor': f"#{random.randint(0, 0xFFFFFF):06x}", 
        'color': '#000000',
        'fillOpacity': 0.4,
        'weight': 0.8
    }

def add_markers_to_map(m, estaciones_df):
    for _, row in estaciones_df.iterrows():
        lat, lon = row['Latitud'], row['Longitud']
        popup = row['Estación']
        color = 'green' if row['Estado'] == 'Instalada' else 'red'
        
        # Check for NaN values
        if pd.notna(lat) and pd.notna(lon):
            folium.Marker(
                location=[lat, lon],
                popup=popup,
                icon=folium.Icon(color=color)
            ).add_to(m)
        else:
            print(f"Warning: Skipping marker for {popup} due to NaN values.")
            

def add_geojson_to_map(m, geojson_files):
    for geojson_info in geojson_files:
        geojson_path = geojson_info['path']
        layer_name = geojson_info['name']
        fields = geojson_info['fields']
        

def main():
    boulder_coords = [15.1, -91.3]
    my_map = folium.Map(location=boulder_coords, zoom_start=10, control_scale=True)

    geojson_files = [
        {"path": 'geojson\\areasgeojson.geojson', "name": "Área de estudio ADIPO", "fields": ['Name']},
        {"path": 'geojson\\Area_de_Intervencion.geojson', "name": "Área Intervención UICN", "fields": ['Areas']},
        {"path": 'geojson\\Area_de_Influencia.geojson', "name": "Área de influencia UICN", "fields": ['Areas']}
    ]

    estaciones_url = 'https://docs.google.com/spreadsheets/d/1F6mHPGmC05MUcatz0fnHPxw_nl1K1w2rp_HrxfxNZbo/edit#gid=0'
    estaciones = pd.read_html(estaciones_url, match='Estación', header=1)[0]
    
    add_markers_to_map(my_map, estaciones)
    add_geojson_to_map(my_map, geojson_files)

    folium.LayerControl(position="bottomright").add_to(my_map)
    
    logo_url = "https://raw.githubusercontent.com/PeterArgueta/clima/main/logo.png"
    FloatImage(logo_url, bottom=5, left=1, width='80px').add_to(my_map)

    my_map.save("index.html")

if __name__ == "__main__":
    main()