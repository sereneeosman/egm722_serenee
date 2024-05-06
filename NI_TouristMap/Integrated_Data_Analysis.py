#!/usr/bin/env python
# coding: utf-8

# # Intergrated Data Analysis

# ## 1. Fixing Geometry in Shapefiles #
# 
# the process of repairing or adjusting the geometric properties of __spatial data__, such as __points__, __lines__, or __polygons__, to ensure they meet certain criteria or standards. This could involve tasks such as removing or correcting invalid geometries, simplifying shapes, snapping vertices to a grid, or resolving topological errors. Libraries such as `Shapely` and `GeoPandas` provide functionality to perform these operations efficiently.
# 

# ### Getting Started
# The geopandas package offers a range of functionalities for performing various operations and analyses on vector geospatial data (a [GeoDataFrame](https://geopandas.org/en/stable/docs/reference/geodataframe.html)). 
# 
# Importing the `geopandas` library with the alias `gpd` ,it provides a shorter and easier-to-use name for referencing the library's functions and objects throughout the code.

# In[ ]:


import geopandas as gpd


# This code reads a shapefiles located in the data directory using `geopandas` library.
# Read the country outline shapefile.

# In[ ]:


# Read the shapefile
input_data = gpd.read_file("data_files/download_data/OSNI_Open_Data_-_Largescale_Boundaries_-_NI_Outline.shp")  # Path to the input shapefile


# Fixing the geometry of [GeoDataFrame](https://geopandas.org/en/stable/docs/reference/geodataframe.html) by applying the [buffer method](https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoSeries.buffer.html) with a Zero distance. This approach can help resolve common geometry issues such as self-intersections and degenerate geometries.

# In[ ]:


# Fix geometries using buffer method
fix_data = input_data.buffer(0)


# [.to_crs()](https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoDataFrame.to_crs.html) method in `GeoPandas` is used to transform all geometries from an active coordinate reference system ([CRS](https://geopandas.org/en/stable/docs/user_guide/projections.html)) to another specified CRS. It allows you to convert the spatial data in your __GeoDataFrame__ to a different CRS, ensuring consistency or enabling analysis in a different geographic context.
# 
# Re-project the `crs` to WGS84 latitude/longitude [(EPSG:4326)](https://epsg.io/4326)

# In[ ]:


# Set CRS to WGS84
fixed_data = fix_data.to_crs("epsg:4326")


# The`.to_file` [(documentation)](https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoDataFrame.to_file.html) function saves the fixed geometries __GeoDataFrame__,into new shapefile.

# In[ ]:


# Save the fixed geometries to a new shapefile
fixed_data.to_file("data_files/NI_Outline.shp") # Path to the fixed output shapefile


# You are free to utilize the output data for analysis.

# ## 2. Coordinate Reference System (CRS) Re-Projection
# 
# Coordinate Re-Projection[(documentation)](https://geopandas.org/en/stable/docs/user_guide/projections.html#re-projecting) is the process of transforming coordinates from one Coordinate Reference System (CRS)[(documentation)](https://geopandas.org/en/stable/docs/user_guide/projections.html) to another. A `CRS` is a framework used to specify locations on the Earth's surface. It's essentially a coordinate-based system that allows for the precise identification of geographic features and positions.
# 
# ### Getting Started
# Importing the geopandas library with the alias gpd ,it provides a shorter and easier-to-use name for referencing the library's functions and objects throughout the code.

# In[ ]:


import geopandas as gpd


# This code reads a shapefiles (a [__GeoDataFrame__](https://geopandas.org/en/stable/docs/reference/geodataframe.html)) located in the data directory using "geopandas" library.

# In[ ]:


# Read the downloaded shapefiles
tourist_tmp = gpd.read_file("data_files/download_data/Historic_Parks_and_Gardens20240410.shp")  # Path to the input shapefile of Historic Park and Garden Data.


# [.to_crs()](https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoDataFrame.to_crs.html) method in GeoPandas is used to transform all geometries from an active coordinate reference system ([CRS](https://geopandas.org/en/stable/docs/user_guide/projections.html)) to another specified CRS. It allows you to convert the spatial data in your GeoDataFrame to a different CRS, ensuring consistency or enabling analysis in a different geographic context.
# 
# Re-project the `crs` to WGS84 latitude/longitude [(EPSG:4326)](https://epsg.io/4326)

# In[ ]:


# Set CRS to WGS84
tourist_prj = tourist_tmp.to_crs("epsg:4326")


# The`.to_file` [(documentation)](https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoDataFrame.to_file.html) function saves the crs transform GeoDataFrame, into a new shapefile.

# In[ ]:


# Save the fixed geometries to a new shapefile
tourist_prj.to_file("data_files/NI_Tourist_Sites.shp") # Path to the output shapefile of heritage parks and Gardens


# You have successfully re-project the Shapefile.

# ## 3. Clipping shapefiles
# Clipping shapefiles refers to the process of spatially limiting or cutting down the extent of a shapefile based on the boundary of another shapefile or a defined boundary area. When examining a shapefile of counties in ArcGIS or QGIS, you might notice that county boundaries extend across water features, which can be confusing for map users. To address this, we will refine the map by removing extraneous elements using the country's outline border.
# 
# ### Getting Started
# 
# Importing the geopandas library with the alias gpd.
# 

# In[ ]:


import geopandas as gpd


# Read the __GeoDataFrames__ of "counties shapefile" and the __geometry fixed__ "country outline" data.

# In[ ]:


# Read the shapefiles
input_counties = gpd.read_file("data_files/download_data/OSNI_Open_Data_-_Largescale_Boundaries_-_County_Boundaries_.shp")# Path to the input shapefile of County Boundaries
clip_data = gpd.read_file("data_files/NI_outline.shp")#path to the country border


# To ensure that all files are in a common CRS (Coordinate Reference System), we need to reproject the GeoDataFrames using the  `.to_crs`[(documentation)](https://www.google.com/search?q=to_crs+geopandas&rlz=1C1JCYX_jaJP1077JP1077&oq=.to_crs+&gs_lcrp=EgZjaHJvbWUqBggBEAAYHjIGCAAQRRg5MgYIARAAGB4yBggCEAAYHjIICAMQABgIGB4yCggEEAAYgAQYogQyCggFEAAYgAQYogQyCggGEAAYgAQYogQyCggHEAAYgAQYogTSAQgyODM5ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8) fuction. In the previous step, the outline shapefile has already been reprojected into WGS84. Now, we need to transform the geometries of the GeoDataFrames called "input_counties" to the desired CRS, which in this case is WGS84.
# 

# In[ ]:


# Assign CRS to the clipped data (assuming the original data uses the same CRS)
prj_counties = input_counties.to_crs ("epsg:4326")


# `.crs`[(documentation)](https://geopandas.org/en/latest/docs/reference/api/geopandas.GeoDataFrame.crs.html) function use for check the existing CRS  of __GeoDataFrames__.

# In[ ]:


prj_counties.crs


# Next, we're going to clip the counties polygon layer using an outline polygon layer. Both GeoDataFrames have the same Coordinate Reference System (CRS).
# * `gpd.overlay`[(documentation)](https://geopandas.org/en/stable/docs/reference/api/geopandas.overlay.html) function overlaying two GeoDataFrames to compute spatial overlay operations, such as intersection, union, or difference.
# 
# * `prj_counties` and `clip_data` represent GeoDataFrames containing geographic data, with prj_counties likely representing the __input feature__ and clip_data representing the __feature used for clipping__ (e.g., a boundary or mask).
# 
# * `keep_geom_type=True` This parameter specifies whether to keep the geometry types of the input GeoDataFrames in the output GeoDataFrame. By setting it to True, the output will retain the geometry types of both prj_counties and clip_data.

# In[ ]:


clipped_counties = gpd.overlay(prj_counties, clip_data, how='intersection', keep_geom_type=True)


# Save the result as ashapefile.
# 
# `.to_fil`[(documentation)](https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoDataFrame.to_file.html) function allows to save new GeoDataFrame. 

# In[ ]:


# Write the clipped data to a new shapefile
clipped_counties.to_file("data_files/NI_Counties.shp") # Path to the fixed output shapefile of County Boundaries


# You have successfully clipped the counties polygons using country outline data.

# ## 4. Data Intergration
# 
# Python typically refers to the process of combining data from multiple sources, formats, or databases into a unified format that can be analyzed or used for further processing.
# 
# ### i. Integrating GP Surgeries Data by Postal Code
# We're going to combine the data from GP surgery with postal code data, creating a unified dataset that includes information from both sources.
# 
# ### Getting Started
# In this step, we will merge two DataFrames and generate a GeoDataFrame as the output.
# 
# Import the necessary libraries.
# 

# In[ ]:


import pandas as pd
import geopandas as gpd


# Read the __DataFrame__
# 
# The `.read_csv()`[(documentation)](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) function in `Pandas` is used to read data from CSV (Comma Separated Values) files and load it into a __DataFrame__, which is a tabular data structure similar to a spreadsheet or a database table. 

# In[ ]:


# Load csv data sets
uk_postcodes = pd.read_csv("data_files/download_data/ukpostcodes.csv") # path to UK postal code csv file
gp_practices = pd.read_csv("data_files/download_data/gp-practice-reference-file---jan-2024.csv") #path to GP practice csv file


# Inspect the __DataFrame__ headers to identify a common column that can be used for integrating the __DataFrames__.
# 
# The `.head()`[(documentation)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html) method in Pandas is used to display the first few rows of a __DataFrame__. By default, it shows the first 5 rows, but you can specify a different number of rows by passing an integer argument to the method `.head(n)`.

# Check the first few rows of the "uk_postcodes" DataFrame

# In[ ]:


# check DataFrame Header
uk_postcodes.head()


# Check the first few rows of the "gp_practices" DataFrame

# In[ ]:


# check the header
gp_practices.head()


# This code merges two DataFrame, namely "uk_postcode"s and "gp_practices", based on a common column in each dataset.
# 
# * The `.merge`([documentation](https://pandas.pydata.org/docs/reference/api/pandas.merge.html)),fuction provided attempts to merge the two datasets. Merge these datasets based on a common field (the "postcode"[uk_postcodes] and "Postcode"[gp_practices] columns)
# 
# * The `left_on`, parameter specifies the column name in the left dataset (uk_postcodes) to use for merging (in this case, "postcode").
# 
# * The `right_on`, parameter specifies the column name in the right dataset (gp_practices) to use for merging (in this case, "Postcode").
# 
# * `how="inner"`, parameter specifies the type of merge to perform. In this case, an inner join is performed, meaning only the rows with matching postal codes in both __DataFrames__ will be included in the merged __DataFrame__.

# In[ ]:


# merge datasets on postal code
merge_data = pd.merge(uk_postcodes, gp_practices, left_on="postcode", right_on="Postcode" , how="inner")


# The `.head()` method is then called on the merged DataFrame to display the first few rows. By default, it shows the first five rows, along with the column names.

# In[ ]:


merge_data.head()


# The downloaded postal code file contains postal codes for the entire United Kingdom (UK). However, for this project, we are only interested in the territory of Northern Ireland, which has postal codes starting with "BT". In this step, we will filter the rows of the __DataFrame__ to include only those with postal codes starting with "BT".
# 
# The `.str.startswith() ` [(documentation)](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.startswith.html)  method is a string accessor available in `Pandas` that is applied to a Series containing strings. It checks whether each string in the Series starts with a specified prefix and returns a boolean Series indicating the result of this check for each string.
# 
# * The `.str`,is a Pandas accessor that allows you to apply string methods to each element of a Series.
# * The `.startswith("BT")`,is a string method that checks if each string in the Series starts with the specified substring, in this case, "BT". It returns a boolean Series where each element indicates whether the corresponding string starts with "BT".

# In[ ]:


# Filtering Northern Ireland postcodes
ni_postcodes_tmp = merge_data[merge_data["postcode"].str.startswith("BT")]


# In this step, we are removing unnecessary columns from the DataFrame 
# 
# `.drop`[(documentation)](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html)  method remove the specified columns on the __DataFrame__. parameter is used to specify the names of the columns to be dropped, provided as a list and returns a new __DataFrame__ with the specified columns removed.

# In[ ]:


# remove unnecessary columns
ni_postcodes = ni_postcodes_tmp.drop(columns=["id" , "Postcode", "LCG" , "Registered_Patients"])


# Verify the resulting __DataFrame__ using the `.head` fucntion.

# In[ ]:


ni_postcodes.head()


# We'll create a new GeoDataFrame from an existing DataFrame.
# 
# The `gpd.GeoDataFrame`[(documentation)](https://geopandas.org/en/stable/docs/reference/api/geopandas.points_from_xy.html) function from the "GeoPandas" library is used to create a __GeoDataFrame__ from a regular DataFrame
#  
# `.points_from_xy`[(documentation)](https://geopandas.org/en/stable/docs/reference/api/geopandas.points_from_xy.html) function specifies the geometry column of the GeoDataFrame. In this case, it creates a new geometry column by converting latitude and longitude coordinates into Point geometries. The __longitude__ and __latitude__ columns from the DataFrame "ni_postcodes" are used as inputs. 

# In[ ]:


# convert the Dataframe to a Geodataframe
ni_postcodes_geo = gpd.GeoDataFrame(ni_postcodes, geometry=gpd.points_from_xy(ni_postcodes.longitude, ni_postcodes.latitude))


# Save the GeoDataFrame as a GeoJSON file.
# 
# * The `.to_file` [(documentation)](https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoDataFrame.to_json.html) method is used to save the GeoDataFrame to a file.
# 
# * The `driver="GeoJSON"` parameter specifies the file format to use for saving the data. In this case, we're using the GeoJSON format.

# In[ ]:


# Save filtered dataset
ni_postcodes_geo.to_file("data_files/NI_PostCodes_GP.geojson", driver="GeoJSON")


# You have successfully exported the GeoJSON file combining GP surgery details with postal codes.

# ### ii. Distance Calculation.
# We'll locate the closest transport hub along with its distance and also identify the nearest GP surgery and its distance from the tourist sites.
# 
# ### Getting Started
# In this step, we will handle __GeoDataFrames__ and calculate the distances.
# 
# Import the necessary libraries. 

# In[ ]:


import pandas as pd
import geopandas as gpd


# Read previously projected tourist sites data(a __GeoDataFrame__).

# In[ ]:


# Read projected tourist data
tourist = gpd.read_file("data_files/NI_Tourist_Sites.shp")  # Path to the input shapefile of projected tourist sites 


# Check the first few rows and try to gain a better understanding of its contents.
# In this dataset, the `geometry` column represents spatial data in the form of "polygons", which are geometric shapes defined by a series of connected points in space.

# In[ ]:


tourist.head()


# Read the GeoJSON files and reproject them into the "Cartesian 2D" coordinate reference system([EPSG:2157,IRENET95 / Irish Transverse Mercator](https://epsg.io/2157)).
# 
# The choice of coordinate system significantly influences the accuracy of __distance calculations__ [(documentation)](https://automating-gis-processes.github.io/CSC/notebooks/L2/projections.html#Calculating-distances).This "Cartesian 2D" coordinate reference system ([Projected Coordinate System](https://www.esri.com/arcgis-blog/products/arcgis-pro/mapping/gcs_vs_pcs/#:~:text=A%20projected%20coordinate%20system%20(PCS)%20is%20a%20GCS%20that%20has,to%20know%20how%20to%20draw.)) is crucial for accurate distance calculations, as it uses "Cartesian coordinates" in "meters", providing precise measurements over __flat surfaces__. WGS84, on the other hand, utilizes longitudes and latitudes in the [geographic coordinate system ](https://desktop.arcgis.com/en/arcmap/latest/map/projections/about-geographic-coordinate-systems.htm#:~:text=A%20geographic%20coordinate%20system%20(GCS,(based%20on%20a%20spheroid).) , which may not yield accurate distance measurements due to the Earth's curved surface.
# 

# Read the downloaded Transport hub "geojson" data (a __GeoDataFrame__)

# In[ ]:


#Load Transport hubs and transform to Irish Transverse Mercator 
transport = gpd.read_file("data_files/download_data/translink-stations-ni.geojson").to_crs("epsg:2157")


# Read the previously integrated "geojson" dataset containing GP surgeries and postal codes (a __GeoDataFrame__).

# In[ ]:


#read combine geojason file of postcodes and GP practice data and transform to Irish Transverse Mercator 
post_gp = gpd.read_file("data_files/NI_PostCodes_GP.geojson").to_crs("epsg:2157")


# This code snippet iterates over each tourist site in the GeoDataFrame tourist, calculates the distance to the nearest bus/train station and the nearest GP surgery, and records the shortest distance in kilometers along with the name of the station.
# 
# explanation of the code:
# 
# * The `for ind, row in tourist.to_crs("epsg:2157").iterrows()` parameters "iterates over"(`.iterrows()`[documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iterrows.html)) each row ("tourist") in the _GeoDataFrame_ tourist, after projecting it to the Irish Transverse Mercator coordinate reference system (EPSG:2157) for distance calculations in meters.
# 
# * The `pt = row["geometry"].centroid` [(documentation)](https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoSeries.centroid.html): function calculates the centroid of each tourist site geometry(polygon).
# 
# * The `.distance()`[(documentation)](https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoSeries.distance.html) function calculates the distance between the centroid of the tourist site and all train/bus stations stored in the __GeoDataFrame__, as well as all GP practices stored in the __GeoDataFrame__.
# 
# * The`.argmin()`[(documentation)](https://pandas.pydata.org/docs/reference/api/pandas.Series.argmin.html) method retrieves the index of the train/bus station with the shortest distance to the tourist site, as well as the index of the nearest GP surgery.
# 
# * The `.min()`[(documentation)](https://docs.python.org/3/library/functions.html#min) method retrieves the shortest distance to the nearest train/bus station in meters, as well as the shortest distance to the nearest GP surgery.
# * The `.loc`[(documentation)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html) indexer is a `Pandas` method used for label-based indexing. It is primarily used to access and modify specific rows and columns of a __DataFrame__ based on their labels (row and column names). It allows you to select data by specifying the row labels and column names explicitly.
# * The `tourist.loc[ind, "Near_T_Hub"] = transport.loc[min_ind_trans].Station.title()` , line assigns the name of the nearest transport hub (train/bus station) to the "Near_T_Hub" column for the current tourist site. The `.title()`[(documentation)](https://docs.python.org/3/library/stdtypes.html#str.title) is a built-in Python string method it capitalizes the first letter of each word in the station name.
# Omit the use of the `.title()` method when assigning to the "GP practice name" because preserving the original case of the names is necessary for combining data in the next steps.The `.merge` function is Case sensitive.
# 
# * `/1000` function convert meters into kilometers.
#   

# In[ ]:


# for each tourist site centroid,find the closest bus/train station
# Record the Shortest distance in km and the name of the station.
for ind, row in tourist.to_crs("epsg:2157").iterrows():
    pt = row["geometry"].centroid # get the centroid of the each tourist site.
    
    distance_trans = transport.distance(pt) # find the distance between the centroid and all train station
    distance_postgp = post_gp.distance(pt) # find the distance between the centroid and all GP pratices
    
    min_ind_trans = distance_trans.argmin() # get the index of minimum value
    min_dist_trans = distance_trans.min() # get the minimum distance

    min_ind_postgp = distance_postgp.argmin()
    min_dist_postgp = distance_postgp.min()

    # define column header
    tourist.loc[ind, "Near_T_Hub"] = transport.loc[min_ind_trans].Station.title()
    tourist.loc[ind, "Near_GP"] = post_gp.loc[min_ind_postgp].PracticeName

    # add distance to the closest transport hub
    tourist.loc[ind, "Trans_Dist"] = min_dist_trans / 1000 # distance in km
    tourist.loc[ind, "GP_Dist"] = min_dist_postgp / 1000


# The `.round()`[(documentation)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.round.html)  is used to round the distances to a specified number of decimal places.In this case, the distance values are being rounded to centimeter accuracy.

# In[ ]:


# round the distance to cm accuracy (2 decimal places)
tourist.Trans_Dist = tourist.Trans_Dist.round(2)
tourist.GP_Dist = tourist.GP_Dist.round(2)


# First, let's check the first few rows of the resulting "tourist" __GeoDataFrame__. Then, we'll inspect the "Near_GP" column and verify that all row values are in uppercase. If any row values are not uppercase, we'll need to go back to the previous cell and ensure that the `.title()` function has been removed for the "post_gp" __GeoDataFrame__.

# In[ ]:


tourist.head() # check the header of final data set


# Inspect the first few rows of the post_gp GeoDataFrame and examine the "PracticeName" column. You'll observe that all row values are in uppercase.

# In[ ]:


post_gp.head()


# 
# You'll notice that both columns have common row values with uppercase letters. Maintaining case sensitivity is crucial when merging __DataFrames__.

# Filter the necessary columns from the "tourist" __GeoDataFrame__ and create a new __DataFrame__ named "tourist_out". 

# In[ ]:


# Filter necessary columns
tourist_out = pd.DataFrame(tourist[["SITE", "Near_T_Hub","Trans_Dist","Near_GP", "GP_Dist"]])


# Inspect the first few rows of the tourist_out DataFrame

# In[ ]:


tourist_out.head()


# Merge the __DataFrame__ "post_gp" with the __GeoDataFrame__ "tourist_out" based on a common column, which is "PracticeName" from "post_gp" and "Near_GP" from "tourist_out". The `.merge` operation is performed using an __inner join__, ensuring that only rows with matching values in both DataFrames are included in the resulting merged DataFrame named "merge".
# 
# * `pd.merge()`: This function from the Pandas library is used to merge two __DataFrames__.
# * `post_gp` and `tourist_out`: These are the __DataFrames__ to be merged.
# * `left_on="PracticeName"` and `right_on="Near_GP"`: These parameters specify the columns from the left and right __DataFrames__ that will be used for the merge operation. In this case, "PracticeName" from post_gp and "Near_GP" from tourist_out are used.
# * `how="inner"`: This parameter specifies the type of merge to perform. In this case, an inner join is performed, meaning only the rows with matching values in both __DataFrames__ will be included in the merged DataFrame.

# In[ ]:


# Merge DataFrame and GeoDataFrame
merged = pd.merge(post_gp, tourist_out,left_on="PracticeName", right_on="Near_GP", how="inner")

Inspect the first few rows of the "merged" __DataFrame__
# In[ ]:


merged.head()


# This code filters the necessary columns from the merged __DataFrame__ "merged", creates a new __DataFrame__ named output, renames the columns, and saves the result to a CSV file.
# * The `pd.DataFrame(...)`[(documentation)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html) function creates a new __DataFrame__ named output with the filtered columns from the previous step.
# * The `.rename`[(documentation)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html) function  is used to rename specified columns to defined new names.
# * The `inplace=True` function ensures that the changes are made directly to the output DataFrame.
# * The `.to_csv`[(documentation)](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_csv.html) function saves the output DataFrame to a CSV file.

# In[ ]:


output = pd.DataFrame(merged[["SITE", "Near_T_Hub","Trans_Dist","Near_GP", "GP_Dist","postcode"]])
output.rename(columns={"SITE":"Tourist Sites", "postcode":"PostCode"},inplace=True)
output.to_csv("data_files/NI_Tourist_trans_GP_Dist.csv")


# ### iii. Coastline spots intergration
# 
# We'll locate the closest transport hub along with its distance and also identify the nearest GP surgery and its distance from the Coastline spots.
# 
# ### Getting Started
# 
# The necessary libraries have already been imported in section 4. If you'd like to start from the middle, navigate back to section 4 and import the libraries. Alternatively, you can define new libraries by adding a new cell here.

# Read the downloaded shapefile data (a __GeoDataFrame__) in coastline.

# In[ ]:


# Read Places_to_Visit_in_Causeway_Coast_and_Glens
coastline_tmp = gpd.read_file("data_files/download_data/Places_to_Visit_in_Causeway_Coast_and_Glens.shp") # Path to the input shapefile of Places to Visit in coastaline data


# Check few rows using `.head()` function

# In[ ]:


coastline_tmp.head()


# The code functions similarly to the previous step, with the main difference being that the "coastal_tmp" geometry represents points, so there's no need to calculate the centroid as done previously.

# In[ ]:


# for each coastline spots ,find the closest bus/train station
# Record the Shortest distance in km and the name of the station.
for ind, row in coastline_tmp.to_crs("epsg:2157").iterrows():
    pt = row["geometry"] # consider geometry point.
    
    distance_trans = transport.distance(pt) # find the distance between the coastline spots and all train station
    distance_postgp = post_gp.distance(pt) # find the distance between the coastline spots and all GP pratices
    
    min_ind_trans = distance_trans.argmin() # get the index of minimum value
    min_dist_trans = distance_trans.min() # get the minimum distance

    min_ind_postgp = distance_postgp.argmin()
    min_dist_postgp = distance_postgp.min()

    # define column header
    coastline_tmp.loc[ind, "Near_T_Hub"] = transport.loc[min_ind_trans].Station.title()
    coastline_tmp.loc[ind, "Near_GP"] = post_gp.loc[min_ind_postgp].PracticeName

    # add distance to the closest transport hub
    coastline_tmp.loc[ind, "Trans_Dist"] = min_dist_trans / 1000 # distance in km
    coastline_tmp.loc[ind, "GP_Dist"] = min_dist_postgp / 1000


# Distance rounding to the centimeter accuracy.

# In[ ]:


# round the distance to cm accuracy (2 decimal places)
coastline_tmp.Trans_Dist = coastline_tmp.Trans_Dist.round(2)
coastline_tmp.GP_Dist = coastline_tmp.GP_Dist.round(2)


# Verify the results

# In[ ]:


coastline_tmp.head()


# This code creates a GeoDataFrame containing selected columns. It then converts the CRS to WGS84 and saves as a GeoJSON file.

# In[ ]:


coastal_out = gpd.GeoDataFrame(coastline_tmp[["Name", "Website","geometry", "Near_T_Hub","Trans_Dist","Near_GP", "GP_Dist","Postcode"]])
coastal_out.to_crs("epsg:4326")
coastal_out.to_file("data_files/NI_Coastal_spots.geojson",driver="GeoJSON")


# In[ ]:




