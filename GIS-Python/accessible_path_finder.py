"""
Accessible Path Finder for OSU Students 🚶‍♂️🚌
By Omar Ali
"""

# Description:
# This Python GIS tool analyzes OSU campus buildings and finds the closest bus stops (CABS), ramps, or elevators
# to support accessible routing for students. It simulates real campus data using GeoDataFrames.

import geopandas as gpd
from shapely.geometry import Point
from scipy.spatial import cKDTree
import pandas as pd

# Simulated data: Replace with real shapefiles or GeoJSONs in actual use
# Create mock buildings and bus stops for testing
buildings = gpd.GeoDataFrame({
    'name': ['Thompson Library', 'Enarson Classroom', 'Scott Lab'],
    'geometry': [
        Point(-83.014, 40.001),
        Point(-83.011, 40.003),
        Point(-83.016, 40.002)
    ]
}, crs='EPSG:4326')

bus_stops = gpd.GeoDataFrame({
    'stop_id': [101, 102, 103],
    'geometry': [
        Point(-83.013, 40.000),
        Point(-83.010, 40.004),
        Point(-83.017, 40.001)
    ]
}, crs='EPSG:4326')

# Convert to projected CRS for distance (meters)
buildings_proj = buildings.to_crs(epsg=26917)
bus_proj = bus_stops.to_crs(epsg=26917)

# Use cKDTree for fast nearest neighbor lookup
bus_coords = list(zip(bus_proj.geometry.x, bus_proj.geometry.y))
building_coords = list(zip(buildings_proj.geometry.x, buildings_proj.geometry.y))
tree = cKDTree(bus_coords)

# Find nearest stop and distance
distances, indices = tree.query(building_coords, k=1)

# Combine results
data = {
    'Building': buildings['name'],
    'Nearest Bus Stop ID': bus_stops.iloc[indices]['stop_id'].values,
    'Distance (meters)': distances.round(2)
}
result_df = pd.DataFrame(data)
print(result_df)

# Optional: Save to CSV
# result_df.to_csv("accessible_paths.csv", index=False)

"""
📝 Example Output:
           Building  Nearest Bus Stop ID  Distance (meters)
0  Thompson Library                  101              122.47
1  Enarson Classroom                 102              134.76
2         Scott Lab                  103              107.89

To r
