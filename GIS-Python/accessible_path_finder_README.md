# 🚌 Accessible Path Finder for OSU Students

This Python GIS tool calculates the nearest CABS bus stop from each building on OSU's campus.  
It’s designed to support accessible routing using spatial analysis and distance calculations.

---

## 🔍 What It Does

- Loads building and bus stop locations using GeoPandas
- Projects coordinates for accurate distance measurement
- Uses SciPy’s KDTree to find the closest bus stop
- Outputs a table (or CSV) showing distances in meters

---

## 🧪 Example Output

| Building            | Nearest Bus Stop ID | Distance (meters) |
|---------------------|----------------------|--------------------|
| Thompson Library    | 101                  | 122.47             |
| Enarson Classroom   | 102                  | 134.76             |
| Scott Lab           | 103                  | 107.89             |

---

## 🛠️ Technologies

- Python
- GeoPandas
- Shapely
- SciPy
- Pandas

---

## 📂 Files

- `accessible_path_finder.py` – main script
- `accessible_paths.csv` – optional export file (uncomment `.to_csv()` to use)

---

## 🧭 Author

Built by Omar Ali  
GIS Intern @ OSU Facilities Information & Technology Services
