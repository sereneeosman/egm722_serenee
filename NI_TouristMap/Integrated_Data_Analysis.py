# Repository : https://github.com/sereneeosman/egm722_serenee) 

#========================================= Intergrated Data Analysis ============================================================================================================
#================================================================================================================================================================================
    """
    the process of repairing or adjusting the geometric properties of spatial data, such as points, lines, or polygons, to ensure they meet certain criteria or standards. 
    This could involve tasks such as removing or correcting invalid geometries, simplifying shapes, snapping vertices to a grid, or resolving topological errors. 
    Libraries such as Shapely and GeoPandas provide functionality to perform these operations efficiently.
    """



#=========================================== 1. Fixing Geometry in Shapefiles ===================================================================================================

# Importing the `pandas` library with the alias `pd`
# Importing the `geopandas` library with the alias `gpd` 
import pandas as pd
import geopandas as gpd

# Read the shapefile
input_data = gpd.read_file("data_files/download_data/OSNI_Open_Data_-_Largescale_Boundaries_-_NI_Outline.shp")  # Path to the input shapefile

# Fix geometries using buffer method
fix_data = input_data.buffer(0)

# Re-project the CRS to WGS84 latitude/longitude(EPSG:4326)
fixed_data = fix_data.to_crs("epsg:4326")

# Save the fixed geometries to a new shapefile
fixed_data.to_file("data_files/NI_Outline.shp") # Path to the fixed output shapefile

#======================================================== End of 1. ==============================================================================================================
        





# =============================== 2. Coordinate Reference System (CRS) Re-Projection =============================================================================================
    """
    Coordinate Re-Projection is the process of transforming coordinates from one Coordinate Reference System (CRS)(documentation) to another. 
    A CRS is a framework used to specify locations on the Earth's surface. 
    It's essentially a coordinate-based system that allows for the precise identification of geographic features and positions.
    """

# Read the downloaded shapefiles of Historic Park and Garden Data.
tourist_tmp = gpd.read_file("data_files/download_data/Historic_Parks_and_Gardens20240410.shp")  # Path to the input shapefile of Historic Park and Garden Data.

# Re-project the CRS to WGS84 latitude/longitude(EPSG:4326)
tourist_prj = tourist_tmp.to_crs("epsg:4326")

# Save the re-projected shapefile to a new shapefile
tourist_prj.to_file("data_files/NI_Tourist_Sites.shp") # Path to the output shapefile 

#===================================================== End of 2. ===================================================================================================================






#================================================= 3. Clipping shapefiles ==========================================================================================================
    """
    Clipping shapefiles refers to the process of spatially limiting or cutting down the extent of a shapefile based on the boundary of another shapefile or a defined boundary area. 
    When examining a shapefile of counties in ArcGIS or QGIS, you might notice that county boundaries extend across water features, which can be confusing for map users. 
    To address this, we will refine the map by removing extraneous elements using the country's outline border.
    """

# Read the input and mask/clip shapefiles
input_counties = gpd.read_file("data_files/download_data/OSNI_Open_Data_-_Largescale_Boundaries_-_County_Boundaries_.shp")# Path to the input shapefile of County Boundaries
clip_data = gpd.read_file("data_files/NI_outline.shp")# path to the mask shapefile of geometry fixed country boarder

# To ensure that all files are in a common CRS (Coordinate Reference System),
# Re-project the CRS of the clipped data (assuming the original data uses the same CRS) WGS84 latitude/longitude(EPSG:4326)
prj_counties = input_counties.to_crs ("epsg:4326")

# Verifying of existing CRS
prj_counties.crs

# Clipping the counties polygon layer using an outline polygon layer
clipped_counties = gpd.overlay(prj_counties, clip_data, how='intersection', keep_geom_type=True)

# Save the clipped data to a new shapefile
clipped_counties.to_file("data_files/NI_Counties.shp") # Path to the fixed output shapefile of County Boundaries

#===================================================== End of 3. ==================================================================================================================  






#=============================================== 4. Data Intergration ==============================================================================================================
    """
    Python typically refers to the process of combining data from multiple sources, formats, or databases into a unified format that can be analyzed or used for further processing.
    """

# -------------------------------------i. Integrating GP Surgeries Data by Postal Code ---------------------------------------------------------------------------------------------
    """
    We're going to combine the data from GP surgery with postal code data, creating a unified dataset that includes information from both sources.
    """

# Load csv data sets
uk_postcodes = pd.read_csv("data_files/download_data/ukpostcodes.csv") # path to UK postal code csv file
gp_practices = pd.read_csv("data_files/download_data/gp-practice-reference-file---jan-2024.csv") #path to GP practice csv file

# check the head of uk_postcodes DataFrame
uk_postcodes.head()

# check the head of gp_practices DataFrame
gp_practices.head()

# merge datasets base on postal code
merge_data = pd.merge(uk_postcodes, gp_practices, left_on="postcode", right_on="Postcode" , how="inner")

#check the head of merged data
merge_data.head()

# Filtering Northern Ireland postcodes
ni_postcodes_tmp = merge_data[merge_data["postcode"].str.startswith("BT")]

# remove unnecessary columns
ni_postcodes = ni_postcodes_tmp.drop(columns=["id" , "Postcode", "LCG" , "Registered_Patients"])

# check the head of DataFrame.
ni_postcodes.head()

# convert the Dataframe to a Geodataframe
ni_postcodes_geo = gpd.GeoDataFrame(ni_postcodes, geometry=gpd.points_from_xy(ni_postcodes.longitude, ni_postcodes.latitude))

# Save the filtered dataset
ni_postcodes_geo.to_file("data_files/NI_PostCodes_GP.geojson", driver="GeoJSON")



#--------------------------------------------- ii. Distance Calculation ------------------------------------------------------------------------------------------------------------
    """
    We'll locate the closest transport hub along with its distance and also identify the nearest GP surgery and its distance from the tourist sites.
    """

# Read previously projected tourist sites data.
tourist = gpd.read_file("data_files/NI_Tourist_Sites.shp")  # Path to the input shapefile of projected tourist sites 

#Check the head
tourist.head()

#Read the downloaded Transport hub "geojson" and transform to Irish Transverse Mercator 
transport = gpd.read_file("data_files/download_data/translink-stations-ni.geojson").to_crs("epsg:2157")

# Read the previously integrated "geojson" dataset containing GP surgeries and postal codes and re-Projected to Irish Transverse Mercator coordinate reference system
post_gp = gpd.read_file("data_files/NI_PostCodes_GP.geojson").to_crs("epsg:2157")

# for each tourist site centroid,find the closest bus/train station
# Record the Shortest distance in km and the name of the station.
for ind, row in tourist.to_crs("epsg:2157").iterrows():
    pt = row["geometry"].centroid # get the centroid of the each tourist site polygon.
    
    distance_trans = transport.distance(pt) # find the distance between the centroid and all train station
    distance_postgp = post_gp.distance(pt) # find the distance between the centroid and all GP pratices
    
    min_ind_trans = distance_trans.argmin() # get the index of minimum value
    min_dist_trans = distance_trans.min() # get the minimum distance

    min_ind_postgp = distance_postgp.argmin()
    min_dist_postgp = distance_postgp.min()

    # define column head
    tourist.loc[ind, "Near_T_Hub"] = transport.loc[min_ind_trans].Station.title() # assigns the name of the nearest transport hub and capitalizes the first letter of each word in the station name
    tourist.loc[ind, "Near_GP"] = post_gp.loc[min_ind_postgp].PracticeName #assigns the name of the nearest GP Surgery

    # add distance to the closest transport hub
    tourist.loc[ind, "Trans_Dist"] = min_dist_trans / 1000 # distance in km
    tourist.loc[ind, "GP_Dist"] = min_dist_postgp / 1000

# round the distance to cm accuracy (2 decimal places)
tourist.Trans_Dist = tourist.Trans_Dist.round(2)
tourist.GP_Dist = tourist.GP_Dist.round(2)

#check the head and verify that all index in the "PracticeName" column are in uppercase.
# check the head
tourist.head() # check the head of final data set

# check the head
post_gp.head()

# Filter necessary columns
tourist_out = pd.DataFrame(tourist[["SITE", "Near_T_Hub","Trans_Dist","Near_GP", "GP_Dist"]])

# check the head
tourist_out.head()

# Merge DataFrame and GeoDataFrame
merged = pd.merge(post_gp, tourist_out,left_on="PracticeName", right_on="Near_GP", how="inner")

# check the head
merged.head()

#Filter necessary coloumns
output = pd.DataFrame(merged[["SITE", "Near_T_Hub","Trans_Dist","Near_GP", "GP_Dist","postcode"]])

# rename specified columns to defined new names
output.rename(columns={"SITE":"Tourist Sites", "postcode":"PostCode"},inplace=True)

# saves the output DataFrame to a CSV file.
output.to_csv("data_files/NI_Tourist_trans_GP_Dist.csv")



#--------------------------------------- iii. Coastline spots intergration ------------------------------------------------------------------------------------------------------------------------------
    """
    We'll locate the closest transport hub along with its distance and also identify the nearest GP surgery and its distance from the Coastline spots.
    """

# Read Places_to_Visit_in_Causeway_Coast_and_Glens
coastline_tmp = gpd.read_file("data_files/download_data/Places_to_Visit_in_Causeway_Coast_and_Glens.shp") # Path to the input shapefile of Places to Visit in coastaline data

# check the head
coastline_tmp.head()

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

    # define column head
    coastline_tmp.loc[ind, "Near_T_Hub"] = transport.loc[min_ind_trans].Station.title() # assigns the name of the nearest transport hub and capitalizes the first letter of each word in the station name
    coastline_tmp.loc[ind, "Near_GP"] = post_gp.loc[min_ind_postgp].PracticeName #assigns the name of the nearest GP Surgery

    # add distance to the closest transport hub
    coastline_tmp.loc[ind, "Trans_Dist"] = min_dist_trans / 1000 # distance in km
    coastline_tmp.loc[ind, "GP_Dist"] = min_dist_postgp / 1000

# round the distance to cm accuracy (2 decimal places)
coastline_tmp.Trans_Dist = coastline_tmp.Trans_Dist.round(2)
coastline_tmp.GP_Dist = coastline_tmp.GP_Dist.round(2)

# check the head
coastline_tmp.head()

# This code filters the necessary columns 
coastal_out = gpd.GeoDataFrame(coastline_tmp[["Name", "Website","geometry", "Near_T_Hub","Trans_Dist","Near_GP", "GP_Dist","Postcode"]])
# reprojected
coastal_out.to_crs("epsg:4326")
# saves the output DataFrame to a CSV file.
coastal_out.to_file("data_files/NI_Coastal_spots.geojson",driver="GeoJSON")

#======================================================= End of 4. =============================================================================================================





#===================================================== End of Script ===========================================================================================================





