# Ohio Economic Development Site Selector Tool

This Python-based GIS tool calculates the nearest industrial park to each Ohio county using simulated geographic data. Designed as a proof of concept for economic development and site suitability analysis, this tool demonstrates spatial analysis with Python and GIS libraries.

---

## Project Description
The tool:
- Loads sample data for Ohio counties and industrial parks using GeoPandas
- Projects coordinates for accurate distance measurement
- Calculates the nearest industrial park to each county using SciPy's KDTree
- Outputs results as a CSV file and generates a visualization map showing connections between counties and their nearest park

---

## Technologies Used
- Python 3.x
- GeoPandas
- Pandas
- SciPy (KDTree)
- Shapely
- Matplotlib

---

## Output
- **CSV:** `ohio_site_selector_output.csv` lists each county, its nearest industrial park, and the distance in meters.
- **Visualization:** `ohio_site_selector_map.png` visualizes county locations, industrial parks, and connecting lines.

---

## Example Results (Simulated Data)
| County     | Nearest Industrial Park | Distance to Park (meters) |
|------------|--------------------------|--------------------------|
| Franklin   | Park A                   | 122.47                   |
| Cuyahoga   | Park B                   | 134.76                   |
| Hamilton   | Park C                   | 107.89                   |

---

## Notes
- This script uses simulated data. Replace with actual county centroids and industrial park datasets for real analysis.
- The framework can be extended to include other infrastructure like airports and highways.

---

## Author
Omar Ali  
GIS Intern, The Ohio State University Facilities Information & Technology Services

---

## License
MIT License
