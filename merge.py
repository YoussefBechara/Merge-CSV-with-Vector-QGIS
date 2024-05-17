uri = "file:///INPUT PATH HERE?type=csv&delimiter=,&xField=lng&yField=lat&crs=EPSG:4326"
csv_layer = QgsVectorLayer(uri, 'CSV Layer', 'delimitedtext')
#make sure it has cols named lng and lat for coords
vector_layer = QgsVectorLayer(PATH to ur vector file, 'Vector Layer', 'ogr')


params = {
    'LAYERS': [csv_layer, vector_layer],
    'CRS': 'EPSG:4326',  # Replace with your desired CRS
    'OUTPUT': 'memory:'  # Or provide a file path to save the merged layer
}
merged_layer = processing.run("native:mergevectorlayers", params)['OUTPUT']
QgsProject.instance().addMapLayer(merged_layer)
