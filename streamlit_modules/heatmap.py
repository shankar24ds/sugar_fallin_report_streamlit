import pandas as pd
import folium
from folium.plugins import HeatMap

def cbe_map():
    df = pd.read_csv('data/raw/sales_enriched2.csv')

    # Drop rows with missing latitude or longitude
    df = df.dropna(subset=['latitude', 'longitude'])

    # Load your DataFrame
    # df = pd.read_csv('your_data.csv')

    # Drop rows with missing latitude, longitude, or price values
    df = df.dropna(subset=['latitude', 'longitude', 'price'])

    # Create a map centered at a specific location (you can adjust these values)
    center_lat, center_lon = df['latitude'].mean(), df['longitude'].mean()
    heat_map = folium.Map(location=[center_lat, center_lon], zoom_start=10)

    # Create a list of points (latitude, longitude, price) for HeatMap
    heat_data = [[row['latitude'], row['longitude'], row['price']] for index, row in df.iterrows()]

    # Add HeatMap layer to the map
    HeatMap(heat_data).add_to(heat_map)

    # Save the map as an HTML file
    return heat_map

