#!/usr/bin/env python
# coding: utf-8

# Norther Ireland Tourist Map With Folium
# Explore Northern Ireland : Tourist Map with Integrated Transportation Hubs, GP Surgeries and Post Codes


# Important Note: All datasets utilize the same Coordinate Reference System [(CRS)](https://geopandas.org/en/stable/docs/user_guide/projections.html), specifically the EPSG code for WGS84 latitude/longitude [(EPSG:4326)](https://epsg.io/4326). This consistency enables seamless integration of map data onto  `folium.map`





#================================================== Importing Libraries =========================================================================

import os
import pandas as pd
import geopandas as gpd
import folium





#================================================== Reading Geospatial Data =========================================================================

# Read the shapefiles
outline = gpd.read_file(os.path.abspath("data_files/NI_Outline.shp")) # Path to the input shapefile of Country Outline data 
counties = gpd.read_file(os.path.abspath("data_files/NI_Counties.shp")) # Path to the input shapefile of Counties data 





#================================================== Creating a Base Folium Map =========================================================================

# Create a Base Map on Counties name.
m = counties.explore("CountyName", cmap = "Set2")

# Adding Country outline into Base folium map
folium.GeoJson(
    outline, # outline shape data
    style_function=lambda feature: {  # customize the style of the GeoJSON features
        "color": "black",  # sets the color of the outline to black
        "fillOpacity": 0 # sets the fill opacity as transparent
    },
    name="outline" #name of the GeoJson layer
).add_to(m) #adds the GeoJson layer to the base folium map _m_.

# Display the base folium map
m





#============================= Convert DataFrame to GeoDataFrame, Display Popups and Plotting Geographic Data (Tourist Sites) ================================

# Read DataFrame
#read intergrated csv file
df = pd.read_csv("data_files/NI_Tourist_trans_GP_Dist.csv")

# Check the first few rows of df 
df.head()

# read tourist site polygon data
tourist = gpd.read_file(os.path.abspath("data_files/NI_Tourist_Sites.shp")) # path to the tourist site shapefile data

# Displaying the column names of the shapefile.
tourist.columns

#Merge the CSV data (DataFrame) with the shapefile data (GeoDataFrame) based on a common column.
merge_site = tourist.merge(df, left_on="SITE", right_on= "Tourist Sites")
merge_site.head()

# Create a new GeoDataFrame with specified columns
# Check the Head of result
visit_filter = merge_site[["Tourist Sites", "Near_T_Hub","Trans_Dist","Near_GP", "GP_Dist","PostCode","geometry"]]
visit_geo = gpd.GeoDataFrame(visit_filter)
visit_geo.head()

# Merge Two GeoDataFrames to attach county name
visit_merge = gpd.sjoin(visit_geo,counties,how="inner")

# Check the Head 
visit_merge.head()

# Re-filtered the merge file.
# Check the Head 
visit_all = visit_merge[["Tourist Sites", "Near_T_Hub","Trans_Dist","Near_GP", "GP_Dist","PostCode","geometry","CountyName"]]
visit_all.head()

# display the Geodatabase on the folium map and popup the attribute information.

# Display Created GeoDataframe on the base Map
visit_all.explore("CountyName", # show the CountyName column
                  cmap="gist_rainbow", # use the "hsv" colormap from matplotlib
                  m=m, # set the base folium.map
                  popup = True, #Show information as popup when curser move on to the polygon
                  legend = False, #Don`t display a separated legend.
)                  





#============================================== Adding Coastline visit spots into Folim map =================================================================

# read geojason file
coastalpt = gpd.read_file(os.path.abspath("data_files/NI_Coastal_spots.geojson"))

# Display head
coastalpt.head()

# Assign Marker Parameters
coastalpt_args = {
    "m": m, # specifies the folium map (m)
    "marker_type": "marker", #specifies the type of marker
    "popup": True, #Show information as popup when curser move on to the polygon
    "legend": False, # Don`t display a separated legend.
    "marker_kwds": {"icon": folium.Icon(color="red", icon="star", prefix='fa')} #style of the marker icon display red color marker with star and refer FontAwesome icon Library   
}

# Display the "coastalpt" Marker on the folium map with the customized marker dictionary
coastalpt.explore ("Name", **coastalpt_args)





#========================================================= Exporting Folium Map ==========================================================================

# Export the Folium Map
m.save("NI_tourist_MAP.html")


# You have successfully generated the tourist map for Northern Ireland.

