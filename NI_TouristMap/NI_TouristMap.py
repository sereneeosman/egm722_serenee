#-------------------------------------------------------------------------------------
#  egm722_serenee #
#-------------------------------------------------------------------------------------

#  Explore Northern Ireland: Tourist Map with Intergrated Transportation Hubs, and GP Surgeries.


# To get started, first import the required python libraries.

# Importing the `os` library 
# Importing the `pandas` library with the alias `pd`
# Importing the `geopandas` library with the alias `gpd` 
# Importing the `folium` library 

import os
import pandas as pd
import geopandas as gpd
import folium


# Reading Geospatial Data:

# Read the shapefiles
outline = gpd.read_file(os.path.abspath("data_files/NI_Outline.shp")) # Path to the input shapefile of Country Outline data 
counties = gpd.read_file(os.path.abspath("data_files/NI_Counties.shp")) # Path to the input shapefile of Counties data 

# Create a Base Map on Counties name.
m = counties.explore("CountyName", cmap = "Set2")


# Adding Country outline into Base folium map

# Add the outline with a black frame
folium.GeoJson(
    outline, # outline shape data
    style_function=lambda feature: {    # customize the style of the GeoJSON features
        "color": "black", # sets the color of the outline to black
        "fillOpacity": 0 # sets the fill opacity as transparent
    },
    name="outline" #name of the GeoJson layer
).add_to(m) #adds the GeoJson layer to the base folium map _m_.

# Display the base folium map
m

#read intergrated csv file
df = pd.read_csv("data_files/NI_Tourist_trans_GP_Dist.csv")

#Check the header
df.head()

# read tourist site polygon data
tourist = gpd.read_file(os.path.abspath("data_files/NI_Tourist_Sites.shp")) # path to the tourist site shapefile data

# Displaying the column names of the shapefile.
tourist.columns

# Merge the CSV data (DataFrame) with the shapefile data (GeoDataFrame) based on a common column.
merge_site = tourist.merge(df, left_on="SITE", right_on= "Tourist Sites")
merge_site.head()


# create a new GeoDataFrame named "visit_geo" by selecting specific columns from the previously merged DataFrame "merge_site".
visit_filter = merge_site[["Tourist Sites", "Near_T_Hub","Trans_Dist","Near_GP", "GP_Dist","PostCode","geometry"]]
visit_geo = gpd.GeoDataFrame(visit_filter)
visit_geo.head()


# add county names into the visit_geo file, where geometries intersect.

visit_merge = gpd.sjoin(visit_geo,counties,how="inner")

# verify the header
visit_merge.head()

#filters specific columns 
# verify the header
visit_all = visit_merge[["Tourist Sites", "Near_T_Hub","Trans_Dist","Near_GP", "GP_Dist","PostCode","geometry","CountyName"]]
visit_all.head()

# displaying the Geodatabase on the folium map and popup the attribute information.

visit_all.explore("CountyName", # show the CountyName column
                  cmap="gist_rainbow", # use the "hsv" colormap from matplotlib
                  m=m, # set the base folium.map
                  popup = True, #Show information as popup when curser move on to the polygon
                  legend = False, #Don`t display a separated legend.
)                  


# Adding Coastline visit spots into Folim map #

# read geojason file
coastlpt = gpd.read_file(os.path.abspath("data_files/NI_Coastal_spots.geojson"))

#check the header
coastlpt.head()


# defining parameters for configuring the display of "coastlpt" `markers` 
coastlpt_args = {
    "m": m, # specifies the folium map (m)
    "marker_type": "marker", #specifies the type of marker
    "popup": True, #Show information as popup when curser move on to the polygon
    "legend": False, # Don`t display a separated legend.
    "marker_kwds": {"icon": folium.Icon(color="red", icon="star", prefix='fa')} #style of the marker icon display red color marker with star and refer FontAwesome icon Library
    
}

# Display the "coastlpt" Marker on the folium map with the customized marker dictionary
coastlpt.explore ("Name", **coastlpt_args)


#save the created folim map (represented by the m object) as an HTML file.
m.save("NI_tourist_MAP.html")

#You can then open this HTML file in a web browser to view the interactive map.
