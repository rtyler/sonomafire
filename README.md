

Caltrans data

This fetches district 1, 3, and 4 data and generates road_closure.txt

python caltrans_fetch.py 

To make qgis maps with MODIS and VIIRS Data
Get data:
sh ./get.sh
sh ./uz.sh
start QGIS
open one of the .qgs project files.
The MODIS and VIIRS layer shapefiles use the same name, so you can
fetch new data then restart QGIS and reopen the project file and get new data.


