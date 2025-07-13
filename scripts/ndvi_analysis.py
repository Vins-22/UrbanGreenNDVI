import geopandas as gpd
import rasterio
from rasterio.mask import mask
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Load ward boundary shapefile
wards = gpd.read_file("data/wards_boundary.shp")
wards = wards.to_crs("EPSG:32643")  # UTM Zone 43N (adjust if needed)

# Step 2: Load Band 4 (Red) and Band 8 (NIR)
with rasterio.open("data/B04_clipped.tif") as red_src:
    red = red_src.read(1).astype('float')

with rasterio.open("data/B08_clipped.tif") as nir_src:
    nir = nir_src.read(1).astype('float')

# Step 3: Calculate NDVI
ndvi = (nir - red) / (nir + red + 1e-5)
meta = red_src.meta
meta.update(dtype=rasterio.float32, count=1)

# Step 4: Save NDVI raster
with rasterio.open("data/ndvi.tif", 'w', **meta) as dst:
    dst.write(ndvi, 1)

# Step 5: Zonal statistics - average NDVI per ward
average_ndvi = []
with rasterio.open("data/ndvi.tif") as src:
    for _, row in wards.iterrows():
        geojson = [row['geometry'].__geo_interface__]
        out_image, out_transform = mask(src, geojson, crop=True)
        ndvi_data = out_image[0]
        ndvi_data = ndvi_data[ndvi_data != src.nodata]
        avg = float(np.mean(ndvi_data)) if ndvi_data.size > 0 else 0
        average_ndvi.append(avg)

wards['avg_ndvi'] = average_ndvi

# Step 6: Save shapefile with NDVI values
wards.to_file("outputs/wards_ndvi.shp")

# Step 7: Visualize the result
wards.plot(column='avg_ndvi', cmap='Greens', legend=True)
plt.title("Average NDVI per Ward")
plt.axis('off')
plt.show()
