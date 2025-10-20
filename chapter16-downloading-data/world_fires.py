"""
Chapter 16 Exercise 9
"""
from pathlib import Path
import csv

import plotly.express as px

def _get_index(header_row, column_name):
    """Find the index of a column in CSV header row."""
    for index, value in enumerate(header_row):
        if value == column_name:
            return index
        
script_dir = Path(__file__).parent
path = script_dir / 'fire_data/world_fires_1_day.csv'
lines = path.read_text(encoding='utf-8').splitlines()
reader = csv.reader(lines)
header_row = next(reader)

# Extract latitude, longitude and brightness
lats, lons, brights = [], [], []
index_lat = _get_index(header_row, 'latitude')
index_lon = _get_index(header_row, 'longitude')
index_bright = _get_index(header_row, 'brightness')

for row in reader:
    lat = float(row[index_lat])
    lon = float(row[index_lon])
    bright = float(row[index_bright])

    lats.append(lat)
    lons.append(lon)
    brights.append(bright)

title = "World Fires"

# Build a world map.
fig = px.scatter_geo(lat=lats, lon=lons, size=brights, title=title,
                     color=brights,
                     color_continuous_scale='Hot',
                     labels={'color':'Brightness'},
                     projection='natural earth'
                     )
fig.show()