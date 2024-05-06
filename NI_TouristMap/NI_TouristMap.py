#!/usr/bin/env python
# coding: utf-8

# # egm722_serenee

# # Explore Northern Ireland: Tourist Map with Intergrated Transportation Hubs, and GP Surgeries.
# 
# ## Contents
# - Overview
# - Data Provided
# - Setup
# - Getting Started
# ## Overview
# 
# The "Explore Northern Ireland" script serves as a versatile and convenient tool tailored for anyone exploring Northern Ireland, be it tourists or residents. 
# This script creates an interactive map of comprehensive information on tourist sites, nearest transportation hubs (including both bus and train stations), as well as the distances between these transportation hubs and tourist sites. Moreover, it seamlessly integrates General Practitioner (GP) surgeries for emergency services, utilizing postal codes for easy searchability. By combining these features, the script enhances the overall travel experience, prioritizing safety and preparedness throughout every stage of the journey.
# #### Objectives:
# * __Interactive Map Creation__:Utilizing GeoDataFrame, the script generates an interactive map that visually presents tourist sites across Northern Ireland.
# * __Tourist Site Information__:Detailed information about each tourist site is included on the map, aiding users in making informed decisions about their destinations.
# * __Find nearest Transportation Hub__:The script identifies and displays the nearest transportation hubs, comprising both bus and train stations, in proximity to tourist sites, facilitating travel route planning and access to public transportation.
# * __Find nearest GP Surgeries__:General Practitioner (GP) surgeries are integrated into the map, allowing users to locate emergency medical services easily. Postal codes are leveraged for efficient searchability, ensuring prompt access to medical assistance.
# * __Distance Calculation__:Distances between transportation hubs/GP Surgeries and tourist sites are calculated and provided, enabling users to estimate travel times and plan itineraries effectively.
# 
# #### Expected Results:
# Upon running the script, users can expect to interact with an informative and user-friendly interactive map to an __html__ file. This map will display detailed information about each tourist site, including its name and website URL for coastal attractive locations. Additionally, users will be able to view the nearest bus or train station to each tourist site, along with the respective distance. Furthermore, the map will highlight the nearest GP surgery and its distance from each tourist location.
# 
# 
# 
# 
# ## Data Provided
# 
# In the data_file folder,contains are as follows:
# 
# * `NI_Outline.shp`, a shapefile comprising the Northern Ireland country outline.
# 
# * `NI_Counties.shp`, a shapefile containing the boundaries of Northern Ireland's counties 
# 
# * `NI_Tourist_Sites.shp` , a shapefile containing polygon data of Historical Parks and Gardens.
#   
# * `NI_Coastal_spots.geojson`, a GeoJSON file containing information on Places to Visit in Causeway Coast and Glens.
#   
# * `NI_PostCodes_GP.geojson`, a GeoJSON file contain GP surgery information with postal codes in Northern Ireland.
# 
# * `NI_Tourist_trans_GP_Dist.csv`,a csv file with information about nearest Transport Hub and Nearest GP surgery information.
# 
# The script  __Integrated_Data_Analysis.ipynb/ .py__ outline the  process of __Re-Projection__, __Polygon Clipping__, and the creation of `NI_Costal_spots.geojson` file, `NI_Costal_spots.geojson`, `NI_PostCodes_GP.geojson` and `NI_Tourist_trans_GP_Dist.csv` files. To execute the script,  ensure you download the specified files into the __data_files/download_data__ folder. Remember to extract shapefiles from __.zip__ archives before use.
# - `OSNI_Open_Data_-_Largescale_Boundaries_-_NI_Outline.shp`, A shapefile comprising the Northern Ireland country outline was obtained from [Data.gov.uk](https://www.data.gov.uk/dataset/738c0cac-d330-4ba9-a2a5-8956383fb4a9/osni-open-data-largescale-boundaries-ni-outline).
# - `OSNI_Open_Data_-_Largescale_Boundaries_-_County_Boundaries_.shp`, A shapefile containing the boundaries of Northern Ireland's counties was sourced from [OpenDataNI](https://admin.opendatani.gov.uk/dataset/osni-open-data-largescale-boundaries-county-boundaries).
#   
# - `historic-parks-and-gardens.shp` , A shapefile containing polygon data of Historic Parks and Gardens(valid as of April 2024) was obtained from [OpenDataNI](https://admin.opendatani.gov.uk/dataset/historic-parks-and-gardens/resource/1f59b6a5-4f8d-4456-9009-e00586062b4d).
#   
# - `Places_to_Visit_in_Causeway_Coast_and_Glens.shp`, A shapefile file containing information on Places to Visit in Causeway Coast and Glens sourced from [OpenDataNI](https://admin.opendatani.gov.uk/dataset/places-to-visit-in-causeway-coast-and-glens)
#   
# - `translink-stations-ni.geojson`, a GeoJSON file containing the locations of all Bus and Rail stations in Northern Ireland, from [OpenDataNI](https://www.opendatani.gov.uk/@translink/translink-ni-railways-stations)
#   
# - `ukpostcodes.csv`, a csv file contain all postcodes in united Kingdom from [FreeMapTools](https://www.freemaptools.com/download-uk-postcode-lat-lng.htm#google_vignette)
#   
# - `gp-practice-reference-file---jan-2024.csv`, a csv file contain General Practitioner (GP) surgeries informations (valid as of April 2024), from[OpenDataNI](https://www.opendatani.gov.uk/@business-services-organisation/gp-practice-list-sizes)
# 
#   
# 
# 

# __Important Note__: All datasets utilize the same Coordinate Reference System [(CRS)](https://geopandas.org/en/stable/docs/user_guide/projections.html), specifically the EPSG code for WGS84 latitude/longitude [(EPSG:4326)](https://epsg.io/4326). This consistency enables seamless integration of map data onto  `folium.map`

# ## Setup

# ## Getting Started
# To get started, open Jupyter Notebook and begin working through the notebook titled "NI_TouristMap_edit.ipynb".
# To execute the cell, highlight it by clicking on it, then either press __Ctrl + Enter__ or click the triangular __"play"__ button located at the top of this panel.
# 
# ### Importing Libraries
# To get started, first import the required python libraries.
# * __os__: This library provides a way to interact with the operating system, such as managing files and directories.[(Documentation)](https://docs.python.org/3/library/os.html)
# * __pandas__(aliased as pd): A powerful data manipulation library that allows you to work with structured data (e.g., data frames,Comma Separated Value (CSV) file).[(Documentation)](https://pandas.pydata.org/) 
# * __geopandas__ (aliased as gpd): An extension of Pandas specifically designed for working with geospatial data (e.g., vector data)[(Documentation)](https://geopandas.org/en/stable/)
# * __folium__: A Python library for creating interactive maps.[(Documentation)](https://python-visualization.github.io/folium/latest/)
# 

# In[ ]:


import os
import pandas as pd
import geopandas as gpd
import folium


# ### Reading Geospatial Data:
# 
# The code utilizes GeoPandas' `.read_file()` function [(Documentation)](https://geopandas.org/en/stable/docs/reference/api/geopandas.read_file.html) to read geospatial data from shapefiles. When handling shapefiles, they are treated as __GeoDataFrame__[(documentation)](https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoDataFrame.html),resembling attribute tables but with added geospatial functionalities.
# 
# A __GeoDataFrame__ enhances a Pandas __DataFrame__ [(Documentation)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) by integrating geospatial capabilities.
# It stored geometry for each feature points, lines, polygons, along with associated attributes. With GeoDataFrames, users can conduct spatial operations and effectively visualize data on maps. 
# 
# Initially, we'll read data for country outlines and counties to establish the foundation of our map.
# 

# In[ ]:


# Read the shapefiles
outline = gpd.read_file(os.path.abspath("data_files/NI_Outline.shp")) # Path to the input shapefile of Country Outline data 
counties = gpd.read_file(os.path.abspath("data_files/NI_Counties.shp")) # Path to the input shapefile of Counties data 


# ###  Create a Base map
# To generate an interactive map from __GeoDataFrames__, we utilize the `.explore`[(Documentation)](https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoDataFrame.explore.html)function  which generates a __folium.Map__[(Documentation)](https://geopandas.org/en/stable/docs/user_guide/interactive_mapping.html).
# We assign the result to `m = folium.Map`[(Documentation)](https://python-visualization.github.io/folium/latest/getting_started.html#Creating-a-map), creating a base map.
# 
# We will utilize the "CountiesName" column to visualize the each polygon, and apply the __Set2__ colormap from `matplotlib` to set the colors.More information about colormaps can be found [here](https://matplotlib.org/stable/users/explain/colors/colormaps.html). 
# In this case, each county will be assigned a color based on its name.

# In[ ]:


# Create a Base Map on Counties name.
m = counties.explore("CountyName", cmap = "Set2")


# ### Adding Country outline into Base map
# 

# Next we will add country outline into the base map from readed shapefile (NI_Outline.shp).
# 
# To do this we use `folium.GeoJson()`[(Documentation)](https://python-visualization.github.io/folium/latest/user_guide/geojson/geojson.html) function in the folim library.
# 
# GeoJSON is a format for encoding a variety of geographic data structures,JSON (JavaScript Object Notation) format. It's commonly used in web mapping applications and spatial databases to represent geographic features such as points, lines, polygons, or a set of coordinates.
# This data defines the shape of an area on the map.
# 
# * __outline__ : This is the GeoDataFrame containing the outline shape data.
# 
# * __style_function=lambda feature__ [(documentation)](https://python-visualization.github.io/folium/latest/user_guide/geojson/geojson.html#Styling)  : This is an argument passed to customize the style of the GeoJSON features. It's a `lambda function` that takes a feature as input and returns a dictionary specifying the style properties.
# 
# * __"color": "black"__,  : This sets the color of the outline to black.
# 
# * __"fillOpacity": 0__ : This sets the fill opacity of the outline to 0, meaning it will be transparent and won't fill the area inside the outline.
# 
# * __name="outline"__  : This sets the name of the GeoJson layer to 'outline'. This name can be used to control the visibility of the layer in the folium map's layer control.
# 
# * __.add_to(m)__ : This method adds the GeoJson layer to the base folium map _m_.

# In[ ]:


# Add the outline with a black frame
folium.GeoJson(
    outline,
    style_function=lambda feature: {
        "color": "black", 
        "fillOpacity": 0
    },
    name="outline"
).add_to(m)


# If you encounter the result __<folium.features.GeoJson at 0x177bc95bb60>__ without an error message, it signifies that the GeoJSON layer object has been successfully created and added to the map (m).

# Display the base folium map

# In[ ]:


m


# As depicted, a color legend is incorporated at the bottom right-hand corner of the map, providing information on the colors assigned to each polygon. Additionally, a scale is situated at the bottom left-hand corner of the map. The country outline of Northern Ireland is displayed with black border lines.You can zoom in or out to examine finer details, including those on the [OpenStreetMap](https://www.openstreetmap.org/#map=5/35.588/134.380) base layer.

# ### Convert csv data to vector data
# The `pd.read_csv()` [(documentation)](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) function is used to read data from a CSV (Comma-Separated Values) file into a Pandas __DataFrame__. The function reads the contents of the CSV file and creates a DataFrame with the data.
# 
# __DataFrame__ [(documentation)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) is a two-dimensional labeled data structure in Pandas. It organizes data into rows and columns, similar to a table. Each column in the DataFrame corresponds to a variable, and each row represents an observation.
# 
# We'll read the integrated CSV file containing tourist site names, details of the nearest transport hubs, and details of the nearest GP surgeries. Refer to the __Integrated_Data_Analysis.ipynb__ file for instructions on how to create this csv file.

# In[ ]:


#read intergrated csv file
df = pd.read_csv("data_files/NI_Tourist_trans_GP_Dist.csv")


# The `.head()`[(documentation)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html) function is used to display the first few rows of the `df`(a __DataFrame__). By default, it returns the first five rows, but you can specify the number of rows you want to display by passing an integer argument to the function (e.g., df.head(10) would display the first ten rows)

# In[ ]:


# Check the first few rows of df 
df.head()


# Next, we'll open the base shapefile of "tourist sites," which includes polygon data. 
# The `gpd.read_file`[(documentation)](https://geopandas.org/en/stable/docs/reference/api/geopandas.read_file.html) function, reads the shapefile and returns a __GeoDataFrame__.
# 
# 

# In[ ]:


# read tourist site polygon data
tourist = gpd.read_file(os.path.abspath("data_files/NI_Tourist_Sites.shp")) # path to the tourist site shapefile data


# The `.columns`[(documentation)](https://www.geeksforgeeks.org/python-pandas-dataframe-columns/) fuction desplay name of the field head in attributes of the DataFrame object in pandas. 
# 
# When you input `tourist.columns`, it returns an index of column labels within the "tourist" __DataFrame__. 

# In[ ]:


# Displaying the column names of the shapefile.
tourist.columns


# This code merges a GeoDataFrame and a DataFrame, namely __tourist__ and __df__, based on a common column in each dataset.
# 
# * The `.merge`[(documentation)](https://pandas.pydata.org/docs/reference/api/pandas.merge.html) fuction provided attempts to merge the two datasets. Merge these datasets based on a common field (the "SITE"[tourist] and "Tourist Sites"[df] columns)
# 
# * The `left_on` parameter specifies the column name in the left dataset (__tourist_site__) to use for merging (in this case, "SITE").
# 
# * The `right_on` parameter specifies the column name in the right dataset (__df__) to use for merging (in this case, "Tourist Sites").
# 
# * The resulting `merge_site` DataFrame will contain combined rows from both datasets.
# 
# * The `.head()` method is then called on the merged DataFrame to display the first few rows.By default, it shows the first five rows, along with the column names.
# 

# In[ ]:


#Merge the CSV data (DataFrame) with the shapefile data (GeoDataFrame) based on a common column.
merge_site = tourist.merge(df, left_on="SITE", right_on= "Tourist Sites")
merge_site.head()


# This code creates a new GeoDataFrame named "visit_geo" by selecting specific columns from the previously merged DataFrame "merge_site".
# 
# * The first line of code selects specific columns from the merge_site DataFrame.  Selection of the __geometry__ column is important as it contain the cooridnates and feature types. The geometry column is necessary for the second command line to generate the GeoDataFrame.
# * The second command `.GeoDataFrame`[(documentation)](https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoDataFrame.html)   converts the __DataFrame__ named "visit_filter" into a __GeoDataFrame__.
# * The `.head()` fuction displays the first few rows  of the "visit_geo" GeoDataFrame.
# 

# In[ ]:


visit_filter = merge_site[["Tourist Sites", "Near_T_Hub","Trans_Dist","Near_GP", "GP_Dist","PostCode","geometry"]]
visit_geo = gpd.GeoDataFrame(visit_filter)
visit_geo.head()


# We will add county names into the visit_geo file, where geometries intersect.
# 
# The `.sjoin` [(documentation)](https://geopandas.org/en/stable/docs/reference/api/geopandas.sjoin.html) function allows spatial join of the two GeoDataFrames (`gpd.sjoin(left_df, right_df, how='inner'`).
# 
# * `left_df`: The left GeoDataFrame (in this case, visit_geo)
# * `right_df`: The right GeoDataFrame (in this case, counties)
# * `how:'inner'`: Retains only the rows where geometries intersect in both GeoDataFrames.
# 

# In[ ]:


visit_merge = gpd.sjoin(visit_geo,counties,how="inner")


# To veryfy the results `.head()` function used to retrieve the first few rows (usually the top 5 rows) GeoDataFrame. It provides a quick preview of the data contained within the GeoDataFrame.
# 

# In[ ]:


visit_merge.head()


# You will see result GeoDatFrame contain both colums of the "Counties" file and "visit_geo" file.
# 
# The next code filters specific columns from the __GeoDataFrame__, constructs a new GeoDataFrame from the filtered data.
# This process is commonly used to focus on relevant columns and convert tabular data with geometric information into a format suitable for spatial analysis.
# 
# Then displays the first few rows of the resulting GeoDataFrame.

# In[ ]:


visit_all = visit_merge[["Tourist Sites", "Near_T_Hub","Trans_Dist","Near_GP", "GP_Dist","PostCode","geometry","CountyName"]]
visit_all.head()


# The `.explore`[(documentation)](https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoDataFrame.explore.html) fuction is used to visualize the polygons of tourist site (Named "visit_all") base on the County name.This implies that the symbology is categorized according to the __county name__, assigning a single color to each polygon belonging to a specific county.
# 
# * `"CountyName"`: Specifies the column to be visualized.
# * `cmap = "gist_rainbow"` : Assigning corresponding colors to each tourist site polygons base on the county name using `matplotlib` colormap library.The more about `matplotlib` library, defined "color map" [(Documents)](https://matplotlib.org/stable/users/explain/colors/colormaps.html).
# * `m=m`: Sets the base map m to be displayed. If `m=None`, it prevents recursion errors.
# * `popup=True`: Enables popups to display additional information when interacting with the map.
# * `legend=False`: Disables the display of the legend on the map.

# In[ ]:


visit_all.explore("CountyName", # show the CountyName column
                  cmap="gist_rainbow", # use the "hsv" colormap from matplotlib
                  m=m, # set the base folium.map
                  popup = True, #Show information as popup when curser move on to the polygon
                  legend = False, #Don`t display a separated legend.
)                  


# ### Adding Coastline visit spots into Folim map

# The code reads a GeoJSON file named "NI_Coastal_spots.geojson" using the GeoPandas `read_file` [(documentation)](https://geopandas.org/en/stable/docs/reference/api/geopandas.read_file.html)function.
# 
# This GeoJSON file contains data about Places to Visit in Causeway Coast and Glens, including information about the nearest transport hub and its distance, nearest GP surgery details and distance, and additional data such as the URL for the website.
# Refer to the __Integrated_Data_Analysis.ipynb__ file for instructions on how to create the GeoJSON file.

# In[ ]:


# read geojason file
coastlpt = gpd.read_file(os.path.abspath("data_files/NI_Coastal_spots.geojson"))


# Printing `coastline.head()` would display the first few rows of the GeoDataFrame coastlpt. 

# In[ ]:


coastlpt.head()


# This code snippet defines a dictionary named coastline_args containing parameters for configuring the display of "coastlpt" `markers` [(documentation)](https://python-visualization.github.io/folium/latest/getting_started.html#Adding-markers) on a folium map. 
# 
# * `"m": m`: This parameter specifies the folium map (m) on which the coastline markers will be plotted. The value associated with this key is an existing folium map instance (m).
# * `"marker_type": "marker"`: This parameter specifies the type of marker to be used for the coastline. In this case, it's set to "marker", indicating standard point markers.
# * `"popup": True`: This parameter determines whether popups will be displayed when clicking on the markers. By setting it to True, popups will be enabled, allowing additional information to be shown when interacting with the markers. 
# * `"legend"`: False: This parameter controls the display of a legend. Here, it's set to False, indicating that no legend will be shown for the markers. 
# * `"marker_kwds": {...}`: This parameter provides additional keyword arguments for styling the markers. Arguments based on the `folium.Map.Icon` [(documentation)](https://python-visualization.github.io/folium/latest/user_guide/ui_elements/icons.html) .In this case, it contains a dictionary with the following settings: `"icon"`: This sets the icon for the marker.
# * `folium.Icon(...)`: This specifies the style of the marker icon. Here, it's configured with a dark red color ("darkred") and a star icon ("star") from the [Font Awesome icon](https://docs.fontawesome.com/apis/javascript/icon-library) library ("fa"). also you can customize your icon with [Bootstrap](https://icons.getbootstrap.com/) icon library.
# 

# In[ ]:


coastlpt_args = {
    "m": m,
    "marker_type": "marker",
    "popup": True,
    "legend": False,
    "marker_kwds": {"icon": folium.Icon(color="red", icon="star", prefix='fa')}
    
}


# The `.explore()` visualizes the coastlpt GeoDataFrame on the folium map, using the specified parameters.The points are categorized based on the __"Name"__ column, and the marker properties are set according to the `coastlpt_args` dictionary.
# 
# 

# In[ ]:


coastlpt.explore ("Name", **coastlpt_args)


# The `m.save` command is used to save the current state of a map (represented by the m object) as an HTML file named “NI_tourist_MAP.html”. 
# You can then open this HTML file in a web browser to view the interactive map.

# In[ ]:


m.save("NI_tourist_MAP.html")


# You have successfully generated the tourist map for Northern Ireland.
# 
