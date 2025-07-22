# Ohio Economic Development Site Selector Tool
# Author: Omar Ali

import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
from scipy.spatial import cKDTree
import matplotlib.pyplot as plt

# Simulated data: Replace with actual GIS datasets for production
counties = gpd.GeoDataFrame({
    'county': ['Franklin', 'Cuyahoga', 'Hamilton'],
    'geometry': [
        Point(-83.0, 40.0),  # Approx Franklin County
        Point(-81.7, 41.5),  # Approx Cuyahoga County
        Point(-84.5, 39.1)   # Approx Hamilton County
    ]
}, crs='EPSG:4326')

industrial_parks = gpd.GeoDataFrame({
    'park_name': ['Park A', 'Park B', 'Park C'],
    'geometry': [
        Point(-83.05, 40.01),
        Point(-81.65, 41.48),
        Point(-84.52, 39.12)
    ]
}, crs='EPSG:4326')

# Project to UTM for accurate distance calculations
counties_proj = counties.to_crs(epsg=26917)
parks_proj = industrial_parks.to_crs(epsg=26917)

# KDTree nearest neighbor calculation
parks_coords = list(zip(parks_proj.geometry.x, parks_proj.geometry.y))
counties_coords = list(zip(counties_proj.geometry.x, counties_proj.geometry.y))
tree = cKDTree(parks_coords)

distances, indices = tree.query(counties_coords, k=1)

# Create DataFrame of results
results = pd.DataFrame({
    'County': counties['county'],
    'Nearest Industrial Park': industrial_parks.iloc[indices]['park_name'].values,
    'Distance to Park (meters)': distances.round(2)
})

print("Nearest Industrial Park to Each County:")
print(results)

# Export results to CSV
results.to_csv("ohio_site_selector_output.csv", index=False)

# Visualization: Plot counties and industrial parks
fig, ax = plt.subplots(figsize=(8, 6))
counties.plot(ax=ax, color='blue', label='Counties', markersize=50)
industrial_parks.plot(ax=ax, color='red', label='Industrial Parks', markersize=50)

for idx, row in results.iterrows():
    county_point = counties.loc[counties['county'] == row['County'], 'geometry'].values[0]
    park_point = industrial_parks.loc[industrial_parks['park_name'] == row['Nearest Industrial Park'], 'geometry'].values[0]
    ax.plot([county_point.x, park_point.x], [county_point.y, park_point.y], color='gray', linestyle='--')

ax.legend()
ax.set_title('Ohio Counties and Nearest Industrial Parks')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True)
plt.savefig('ohio_site_selector_map.png')
plt.show()

# Notes:
# - Replace the simulated data with actual GIS datasets for a production-level tool.
# - Visualization saved as 'ohio_site_selector_map.png'.
# - Framework can be extended to airports, highways, or multi-factor analysis.
