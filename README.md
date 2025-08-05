# 🌿 Urban NDVI Analysis with Python & GeoPandas
 A Python-based project that reads and processes Sentinel-2 imagery to compute **Normalizd Difference Vegetation Index (NDVI)**. It overlays ward boundaries to perform **zonal statistics** and extract average NDVI values per ward. The workflow uses rasterio for raster handling, geopandas for vector data, and numpy for array operations.

---

## 📁 Project Structure

```
UrbanGreenNDVI/
├── data/             # Input data: Sentinel-2 bands and ward shapefile
├── scripts/          # Python script for NDVI calculation and zonal analysis
├── outputs/          # Output shapefile with average NDVI per ward
├── README.md         # Project documentation
├── .gitignore        # Files/folders excluded from GitHub
└── environment.yml   # Conda environment file
```

---

## 📍 Study Area

The study focuses on **urban wards in Delhi**, India, analyzing the spatial distribution of green spaces using NDVI as a vegetation indicator.

---

## 📥 Data Sources

- **Sentinel-2 Imagery (Bands 4 and 8)**  
  Downloaded from the [Copernicus Open Access Hub](https://scihub.copernicus.eu/)  
  Provided by the **European Space Agency (ESA)** under the **Copernicus Programme**

- **Delhi Ward Boundary Shapefile**  
  Sourced from **ArcGIS Online**, contributed by user: **ncrtcoffice**

---

## 🧪 Methodology

1. Load Sentinel-2 Band 4 (Red) and Band 8 (NIR)
2. Calculate NDVI using the formula:  
   `NDVI = (NIR - Red) / (NIR + Red)`
3. Save the NDVI raster
4. Load Delhi ward boundary shapefile
5. Perform **zonal statistics** to compute average NDVI per ward
6. Save the output shapefile with `avg_ndvi` values
7. Visualize the results using a choropleth map

---

## 🐍 How to Run This Project

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/UrbanGreenNDVI.git
   cd UrbanGreenNDVI
   ```

2. **Set up the environment (requires Conda)**:
   ```bash
   conda env create -f environment.yml
   conda activate greenspace
   ```

3. **Ensure the `data/` folder contains**:
   - `B04_clipped.tif` ← Band 4 (Red)
   - `B08_clipped.tif` ← Band 8 (NIR)
   - `wards_boundary.shp` and its associated files

4. **Run the script**:
   ```bash
   python scripts/ndvi_analysis.py
   ```

---

## 📤 Outputs

- `outputs/wards_ndvi.shp` — Shapefile containing the average NDVI per ward
- A map displaying NDVI distribution across urban wards

---

## 🛠️ Tools Used

- Python 3
- GeoPandas
- Rasterio
- NumPy
- Matplotlib

---

## 📄 License

This project is open-source and licensed under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

- European Space Agency (ESA) for providing Sentinel-2 data
- Copernicus Programme for open Earth observation data
- ArcGIS Online and user **ncrtcoffice** for ward boundary shapefile
- Contributors to open-source geospatial Python libraries
