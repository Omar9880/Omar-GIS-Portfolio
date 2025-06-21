# Accessible Path Finder for OSU Students

This Python GIS tool calculates the nearest CABS bus stop from each building on OSU's campus.  
It was developed to support accessible routing using spatial analysis and distance calculations.

---

## What It Does

- Loads simulated building and bus stop locations using GeoPandas
- Projects coordinates to a local CRS for accurate distance calculations
- Uses SciPy's KDTree to identify the nearest bus stop to each building
- Outputs results as a distance table or optionally saves to CSV

---

## Example Output

Each row in the output contains:
- Building name
- Nearest bus stop ID
- Distance to that stop (in meters)

Example:
Thompson Library → Stop 101 → 122.47 meters  
Enarson Classroom → Stop 102 → 134.76 meters  
Scott Lab → Stop 103 → 107.89 meters

---

## Technologies Used

- Python
- GeoPandas
- Shapely
- SciPy
- Pandas

---

## Files Included

- `accessible_path_finder.py` – main script
- `accessible_paths.csv` – optional export (generated if `.to_csv()` is enabled)

---

## Author

Omar Ali  
GIS Intern, OSU Facilities Information & Technology Services

