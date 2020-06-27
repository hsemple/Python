import matplotlib.pyplot as plt
import geopandas as gpd

file = ".../Michigan_Counties.shp"
df = gpd.read_file(file)

#Display attribute table
print (df)
 
#Display shapefile
df.plot()

#or
#df.plot(cmap='Set2', figsize=(10, 10));
plt.show() <br>