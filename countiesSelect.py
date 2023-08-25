import qgis.core
from qgis.utils import *

# Define the path to your layer
countiesLayerPath = "C:/Users/User/Downloads/ken_adm_iebc_20191031_shp/ken_admbnda_adm1_iebc_20191031.shp"

# Add your layer to the user interface
countiesLayer = iface.addVectorLayer(countiesLayerPath, "counties", "ogr")

# Get features from your layer
feats = countiesLayer.getFeatures()

# Loop through all the features
for feat in feats:
    # Get the selected feature's ID
    selectedfeat = feat.id()

    # Select the current feature using its ID
    selection = countiesLayer.select(selectedfeat)

    # Create a temporary layer containing the selected feature
    new_layer = countiesLayer.materialize(QgsFeatureRequest().setFilterFids(countiesLayer.selectedFeatureIds()))

    # Create a unique name for the output shapefile
    output_path = 'C:/Users/User/Desktop/desktop folders/programming/Qgiscodes/shapefiles_county/' + f"county{selectedfeat}" + ".shp"

    # Write the temporary layer to the output shapefile
    writer = QgsVectorFileWriter.writeAsVectorFormat(new_layer, output_path, "utf-8", new_layer.crs(), "ESRI Shapefile")
    del(writer)

    # Remove the selection to always get a county individually
    countiesLayer.removeSelection()

# Refresh the QGIS canvas after creating all individual layers
iface.mapCanvas().refresh()

#load the layers to the Qgis canvas 

iface.addVectorLayer('C:/Users/User/Desktop/desktop folders/programming/Qgiscodes/shapefiles_county/','',"ogr")   