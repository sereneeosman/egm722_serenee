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
"""Import libraries with aliases.

Parameters
----------
None

Returns
-------
None

Examples
--------
>>> import pandas as pd
>>> import geopandas as gpd
"""


# Read the shapefile
input_data = gpd.read_file("data_files/download_data/OSNI_Open_Data_-_Largescale_Boundaries_-_NI_Outline.shp")  # Path to the input shapefile
def read_shapefile(filepath):
    """
    Read a shapefile using GeoPandas.

    Parameters
    ----------
    filepath : str
        Path to the input shapefile.

    Returns
    -------
    geopandas.geodataframe.GeoDataFrame
        A GeoDataFrame containing the data from the shapefile.

    Examples
    --------
    >>> input_data = read_shapefile("data_files/download_data/OSNI_Open_Data_-_Largescale_Boundaries_-_NI_Outline.shp")
    """
    return gpd.read_file(filepath)


# Fix geometries using buffer method
fix_data = input_data.buffer(0)
def fix_geometries(input_data):
    """
    Fix geometries using the buffer method.

    Parameters
    ----------
    input_data : geopandas.geodataframe.GeoDataFrame
        The input GeoDataFrame containing geometries to be fixed.

    Returns
    -------
    geopandas.geoseries.GeoSeries
        A GeoSeries containing fixed geometries.

    Examples
    --------
    >>> fixed_data = fix_geometries(input_data)
    """
    return input_data.buffer(0)


# Re-project the CRS to WGS84 latitude/longitude(EPSG:4326)
fixed_data = fix_data.to_crs("epsg:4326")
def reproject_to_wgs84(input_data):
    """
    Re-project the Coordinate Reference System (CRS) to WGS84 latitude/longitude (EPSG:4326).

    Parameters
    ----------
    input_data : geopandas.geodataframe.GeoDataFrame
        The input GeoDataFrame containing geometries to be re-projected.

    Returns
    -------
    geopandas.geodataframe.GeoDataFrame
        A new GeoDataFrame with re-projected geometries.

    Examples
    --------
    >>> reprojected_data = reproject_to_wgs84(fixed_data)
    """
    return input_data.to_crs("epsg:4326")


# Save the fixed geometries to a new shapefile
fixed_data.to_file("data_files/NI_Outline.shp") # Path to the fixed output shapefile
def save_to_shapefile(input_data, output_filepath):
    """
    Save the fixed geometries to a new shapefile.

    Parameters
    ----------
    input_data : geopandas.geodataframe.GeoDataFrame
        The input GeoDataFrame containing fixed geometries to be saved.
    output_filepath : str
        The file path to save the new shapefile.

    Returns
    -------
    None

    Examples
    --------
    >>> save_to_shapefile(fixed_data, "data_files/NI_Outline.shp")
    """
    input_data.to_file(output_filepath)
        
#======================================================== End of 1. ==============================================================================================================
        





# =============================== 2. Coordinate Reference System (CRS) Re-Projection =============================================================================================
    """
    Coordinate Re-Projection is the process of transforming coordinates from one Coordinate Reference System (CRS)(documentation) to another. A CRS is a framework used to specify locations on the Earth's surface. It's essentially a coordinate-based system that allows for the precise identification of geographic features and positions.
    """

# Read the downloaded shapefiles of Historic Park and Garden Data.
tourist_tmp = gpd.read_file("data_files/download_data/Historic_Parks_and_Gardens20240410.shp")  # Path to the input shapefile of Historic Park and Garden Data.
def read_historic_parks_and_gardens(filepath):
    """
    Read the downloaded shapefiles of Historic Park and Garden Data.

    Parameters
    ----------
    filepath : str
        Path to the input shapefile of Historic Park and Garden Data.

    Returns
    -------
    geopandas.geodataframe.GeoDataFrame
        A GeoDataFrame containing the Historic Park and Garden Data.

    Examples
    --------
    >>> tourist_tmp = read_historic_parks_and_gardens("data_files/download_data/Historic_Parks_and_Gardens20240410.shp")
    """
    return gpd.read_file(filepath)


# Re-project the CRS to WGS84 latitude/longitude(EPSG:4326)
tourist_prj = tourist_tmp.to_crs("epsg:4326")
def reproject_to_wgs84(input_data):
    """
    Re-project the Coordinate Reference System (CRS) to WGS84 latitude/longitude (EPSG:4326).

    Parameters
    ----------
    input_data : geopandas.geodataframe.GeoDataFrame
        The input GeoDataFrame containing geometries to be re-projected.

    Returns
    -------
    geopandas.geodataframe.GeoDataFrame
        A new GeoDataFrame with re-projected geometries.

    Examples
    --------
    >>> tourist_prj = reproject_to_wgs84(tourist_tmp)
    """
    return input_data.to_crs("epsg:4326")


# Save the re-projected shapefile to a new shapefile
tourist_prj.to_file("data_files/NI_Tourist_Sites.shp") # Path to the output shapefile 
def save_to_shapefile(input_data, output_filepath):
    """
    Save the re-projected shapefile to a new shapefile.

    Parameters
    ----------
    input_data : geopandas.geodataframe.GeoDataFrame
        The input GeoDataFrame containing re-projected geometries to be saved.
    output_filepath : str
        The file path to save the new shapefile.

    Returns
    -------
    None

    Examples
    --------
    >>> save_to_shapefile(tourist_prj, "data_files/NI_Tourist_Sites.shp")
    """
    input_data.to_file(output_filepath)
    
#===================================================== End of 2. ===================================================================================================================






#================================================= 3. Clipping shapefiles ==========================================================================================================
    """
    Clipping shapefiles refers to the process of spatially limiting or cutting down the extent of a shapefile based on the boundary of another shapefile or a defined boundary area. When examining a shapefile of counties in ArcGIS or QGIS, you might notice that county boundaries extend across water features, which can be confusing for map users. To address this, we will refine the map by removing extraneous elements using the country's outline border.
    """

# Read the input and mask/clip shapefiles
input_counties = gpd.read_file("data_files/download_data/OSNI_Open_Data_-_Largescale_Boundaries_-_County_Boundaries_.shp")# Path to the input shapefile of County Boundaries
clip_data = gpd.read_file("data_files/NI_outline.shp")# path to the mask shapefile of geometry fixed country boarder
def read_shapefiles(input_filepath, mask_filepath):
    """
    Read the input and mask/clip shapefiles.

    Parameters
    ----------
    input_filepath : str
        Path to the input shapefile of County Boundaries.
    mask_filepath : str
        Path to the mask shapefile of geometry fixed country border.

    Returns
    -------
    tuple
        A tuple containing two GeoDataFrames:
        - The first GeoDataFrame represents the input County Boundaries.
        - The second GeoDataFrame represents the mask/clip shapefile.

    Examples
    --------
    >>> input_counties, clip_data = read_shapefiles("data_files/download_data/OSNI_Open_Data_-_Largescale_Boundaries_-_County_Boundaries_.shp",
    ...                                             "data_files/NI_outline.shp")
    """
    return gpd.read_file(input_filepath), gpd.read_file(mask_filepath)


# To ensure that all files are in a common CRS (Coordinate Reference System),
# Re-project the CRS of the clipped data (assuming the original data uses the same CRS) WGS84 latitude/longitude(EPSG:4326)
prj_counties = input_counties.to_crs ("epsg:4326")
def reproject_to_wgs84(input_data):
    """
    Re-project the Coordinate Reference System (CRS) to WGS84 latitude/longitude (EPSG:4326).

    Parameters
    ----------
    input_data : geopandas.geodataframe.GeoDataFrame
        The input GeoDataFrame containing geometries to be re-projected.

    Returns
    -------
    geopandas.geodataframe.GeoDataFrame
        A new GeoDataFrame with re-projected geometries.

    Examples
    --------
    >>> prj_counties = reproject_to_wgs84(input_counties)
    """
    return input_data.to_crs("epsg:4326")


# Verifying of existing CRS
prj_counties.crs
def verify_crs(input_data):
    """
    Verify the existing Coordinate Reference System (CRS) of a GeoDataFrame.

    Parameters
    ----------
    input_data : geopandas.geodataframe.GeoDataFrame
        The input GeoDataFrame to verify the CRS.

    Returns
    -------
    dict or None
        A dictionary containing the CRS information if available, or None if CRS information is not available.

    Examples
    --------
    >>> crs_info = verify_crs(prj_counties)
    """
    return input_data.crs


# Clipping the counties polygon layer using an outline polygon layer
clipped_counties = gpd.overlay(prj_counties, clip_data, how='intersection', keep_geom_type=True)
def clip_counties_by_outline(county_data, outline_data):
    """
    Clip the counties polygon layer using an outline polygon layer.

    Parameters
    ----------
    county_data : geopandas.geodataframe.GeoDataFrame
        The GeoDataFrame representing the counties polygon layer to be clipped.
    outline_data : geopandas.geodataframe.GeoDataFrame
        The GeoDataFrame representing the outline polygon layer used for clipping.

    Returns
    -------
    geopandas.geodataframe.GeoDataFrame
        A new GeoDataFrame containing the clipped counties.

    Examples
    --------
    >>> clipped_counties = clip_counties_by_outline(prj_counties, clip_data)
    """
    return gpd.overlay(county_data, outline_data, how='intersection', keep_geom_type=True)


# Save the clipped data to a new shapefile
clipped_counties.to_file("data_files/NI_Counties.shp") # Path to the fixed output shapefile of County Boundaries
def save_clipped_data(clipped_data, output_filepath):
    """
    Save the clipped data to a new shapefile.

    Parameters
    ----------
    clipped_data : geopandas.geodataframe.GeoDataFrame
        The GeoDataFrame containing the clipped data to be saved.
    output_filepath : str
        The file path to save the new shapefile.

    Returns
    -------
    None

    Examples
    --------
    >>> save_clipped_data(clipped_counties, "data_files/NI_Counties.shp")
    """
    clipped_data.to_file(output_filepath)

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
def load_csv_datasets(postcodes_filepath, gp_practices_filepath):
    """
    Load CSV datasets.

    Parameters
    ----------
    postcodes_filepath : str
        Path to the UK postal code CSV file.
    gp_practices_filepath : str
        Path to the GP practice CSV file.

    Returns
    -------
    tuple
        A tuple containing two pandas DataFrames:
        - The first DataFrame represents the UK postal code data.
        - The second DataFrame represents the GP practice data.

    Examples
    --------
    >>> uk_postcodes, gp_practices = load_csv_datasets("data_files/download_data/ukpostcodes.csv",
    ...                                                "data_files/download_data/gp-practice-reference-file---jan-2024.csv")
    """
    return pd.read_csv(postcodes_filepath), pd.read_csv(gp_practices_filepath)


# check the head of uk_postcodes DataFrame
uk_postcodes.head()
def check_head(dataframe):
    """
    Check the head of a DataFrame.

    Parameters
    ----------
    dataframe : pandas.core.frame.DataFrame
        The DataFrame to check.

    Returns
    -------
    pandas.core.frame.DataFrame
        The first few rows of the DataFrame.

    Examples
    --------
    >>> uk_postcodes_head = check_head(uk_postcodes)
    """
    return dataframe.head()


# check the head of gp_practices DataFrame
gp_practices.head()
def check_head(dataframe):
    """
    Check the head of a DataFrame.

    Parameters
    ----------
    dataframe : pandas.core.frame.DataFrame
        The DataFrame to check.

    Returns
    -------
    pandas.core.frame.DataFrame
        The first few rows of the DataFrame.

    Examples
    --------
    >>> gp_practices_head = check_head(gp_practices)
    """
    return dataframe.head()


# merge datasets base on postal code
merge_data = pd.merge(uk_postcodes, gp_practices, left_on="postcode", right_on="Postcode" , how="inner")
def merge_datasets_by_postal_code(left_dataframe, right_dataframe):
    """
    Merge datasets based on postal code.

    Parameters
    ----------
    left_dataframe : pandas.core.frame.DataFrame
        The left DataFrame to merge.
    right_dataframe : pandas.core.frame.DataFrame
        The right DataFrame to merge.

    Returns
    -------
    pandas.core.frame.DataFrame
        A new DataFrame containing the merged data.

    Examples
    --------
    >>> merge_data = merge_datasets_by_postal_code(uk_postcodes, gp_practices)

    Notes
    -----
    - The 'left_on' parameter specifies the column name in the left DataFrame used for merging (uk_postcodes).
    - The 'right_on' parameter specifies the column name in the right DataFrame used for merging (gp_practices).
    - The 'how' parameter specifies the type of merge to perform. In this case, 'inner' merge is used to retain only the matching rows from both DataFrames.

    """
    return pd.merge(left_dataframe, right_dataframe, left_on="postcode", right_on="Postcode", how="inner")



#check the head of merged data
merge_data.head()
def check_head(dataframe):
    """
    Check the head of a DataFrame.

    Parameters
    ----------
    dataframe : pandas.core.frame.DataFrame
        The DataFrame to check.

    Returns
    -------
    pandas.core.frame.DataFrame
        The first few rows of the DataFrame.

    Examples
    --------
    >>> merge_data_head = check_head(merge_data)
    """
    return dataframe.head()


# Filtering Northern Ireland postcodes
ni_postcodes_tmp = merge_data[merge_data["postcode"].str.startswith("BT")]
def filter_northern_ireland_postcodes(dataframe):
    """
    Filter postcodes to include only those from Northern Ireland (NI).

    Parameters
    ----------
    dataframe : pandas.core.frame.DataFrame
        The DataFrame containing postcode data.

    Returns
    -------
    pandas.core.frame.DataFrame
        A new DataFrame containing only the postcodes from Northern Ireland.

    Examples
    --------
    >>> ni_postcodes_tmp = filter_northern_ireland_postcodes(merge_data)
    """
    return dataframe[dataframe["postcode"].str.startswith("BT")]



# remove unnecessary columns
ni_postcodes = ni_postcodes_tmp.drop(columns=["id" , "Postcode", "LCG" , "Registered_Patients"])
def remove_unnecessary_columns(dataframe):
    """
    Remove unnecessary columns from a DataFrame.

    Parameters
    ----------
    dataframe : pandas.core.frame.DataFrame
        The DataFrame from which columns are to be removed.

    Returns
    -------
    pandas.core.frame.DataFrame
        A new DataFrame with the specified columns removed.

    Examples
    --------
    >>> ni_postcodes = remove_unnecessary_columns(ni_postcodes_tmp)
    """
    return dataframe.drop(columns=["id", "Postcode", "LCG", "Registered_Patients"])



# check the head of DataFrame.
ni_postcodes.head()
def check_head(dataframe):
    """
    Check the head of a DataFrame.

    Parameters
    ----------
    dataframe : pandas.core.frame.DataFrame
        The DataFrame to check.

    Returns
    -------
    pandas.core.frame.DataFrame
        The first few rows of the DataFrame.

    Examples
    --------
    >>> ni_postcodes_head = check_head(ni_postcodes)
    """
    return dataframe.head()


# convert the Dataframe to a Geodataframe
ni_postcodes_geo = gpd.GeoDataFrame(ni_postcodes, geometry=gpd.points_from_xy(ni_postcodes.longitude, ni_postcodes.latitude))
def convert_to_geodataframe(dataframe):
    """
    Convert a DataFrame to a GeoDataFrame.

    Parameters
    ----------
    dataframe : pandas.core.frame.DataFrame
        The DataFrame to convert.

    Returns
    -------
    geopandas.geodataframe.GeoDataFrame
        A GeoDataFrame created from the input DataFrame.

    Examples
    --------
    >>> ni_postcodes_geo = convert_to_geodataframe(ni_postcodes)
    """
    return gpd.GeoDataFrame(dataframe, geometry=gpd.points_from_xy(dataframe.longitude, dataframe.latitude))


# Save the filtered dataset
ni_postcodes_geo.to_file("data_files/NI_PostCodes_GP.geojson", driver="GeoJSON")
def save_as_geojson(geodataframe, output_filepath):
    """
    Save a GeoDataFrame as a GeoJSON file.

    Parameters
    ----------
    geodataframe : geopandas.geodataframe.GeoDataFrame
        The GeoDataFrame to save as GeoJSON.
    output_filepath : str
        The file path to save the GeoJSON file.

    Returns
    -------
    None

    Examples
    --------
    >>> save_as_geojson(ni_postcodes_geo, "data_files/NI_PostCodes_GP.geojson")
    """
    geodataframe.to_file(output_filepath, driver="GeoJSON")



#--------------------------------------------- ii. Distance Calculation ------------------------------------------------------------------------------------------------------------
    """
    We'll locate the closest transport hub along with its distance and also identify the nearest GP surgery and its distance from the tourist sites.
    """

# Read previously projected tourist sites data.
tourist = gpd.read_file("data_files/NI_Tourist_Sites.shp")  # Path to the input shapefile of projected tourist sites 
def read_tourist_sites(filepath):
    """
    Read previously projected tourist sites data.

    Parameters
    ----------
    filepath : str
        Path to the input shapefile of projected tourist sites.

    Returns
    -------
    geopandas.geodataframe.GeoDataFrame
        A GeoDataFrame containing the projected tourist sites data.

    Examples
    --------
    >>> tourist = read_tourist_sites("data_files/NI_Tourist_Sites.shp")
    """
    return gpd.read_file(filepath)



#Check the head
tourist.head()
def check_head(dataframe):
    """
    Check the head of a DataFrame.

    Parameters
    ----------
    dataframe : pandas.core.frame.DataFrame
        The DataFrame to check.

    Returns
    -------
    pandas.core.frame.DataFrame
        The first few rows of the DataFrame.

    Examples
    --------
    >>> tourist_head = check_head(tourist)
    """
    return dataframe.head()


#Read the downloaded Transport hub "geojson" and transform to Irish Transverse Mercator 
transport = gpd.read_file("data_files/download_data/translink-stations-ni.geojson").to_crs("epsg:2157")
def read_and_transform_transport_hub(filepath):
    """
    Read the downloaded Transport hub "geojson" and transform it to Irish Transverse Mercator (EPSG:2157).

    Parameters
    ----------
    filepath : str
        Path to the input GeoJSON file of transport hubs.

    Returns
    -------
    geopandas.geodataframe.GeoDataFrame
        A GeoDataFrame containing the transport hub data transformed to EPSG:2157.

    Examples
    --------
    >>> transport = read_and_transform_transport_hub("data_files/download_data/translink-stations-ni.geojson")
    """
    return gpd.read_file(filepath).to_crs("epsg:2157")


# Read the previously integrated "geojson" dataset containing GP surgeries and postal codes and re-Projected to Irish Transverse Mercator coordinate reference system
post_gp = gpd.read_file("data_files/NI_PostCodes_GP.geojson").to_crs("epsg:2157")
def read_and_reproject_geojson(filepath):
    """
    Read the previously integrated GeoJSON dataset containing GP surgeries and postal codes
    and re-project it to Irish Transverse Mercator coordinate reference system (EPSG:2157).

    Parameters
    ----------
    filepath : str
        Path to the input GeoJSON file containing GP surgeries and postal codes.

    Returns
    -------
    geopandas.geodataframe.GeoDataFrame
        A GeoDataFrame containing the integrated data re-projected to EPSG:2157.

    Examples
    --------
    >>> post_gp = read_and_reproject_geojson("data_files/NI_PostCodes_GP.geojson")
    """
    return gpd.read_file(filepath).to_crs("epsg:2157")


# for each tourist site centroid,find the closest bus/train station
# Record the Shortest distance in km and the name of the station.
for ind, row in tourist.to_crs("epsg:2157").iterrows():
    pt = row["geometry"].centroid # get the centroid of the each tourist site polygon.
    def calculate_centroids(tourist_sites):
    """
    Calculate centroids for each tourist site polygon after transforming to EPSG:2157 CRS.

    Parameters
    ----------
    tourist_sites : geopandas.geodataframe.GeoDataFrame
        GeoDataFrame containing tourist site data.

    Returns
    -------
    list of shapely.geometry.point.Point
        A list containing the centroid points of each tourist site polygon in EPSG:2157 CRS.

    Examples
    --------
    >>> centroids = calculate_centroids(tourist)
    """
    centroids = []
    for ind, row in tourist_sites.to_crs("epsg:2157").iterrows():
        pt = row["geometry"].centroid
        centroids.append(pt)
    return centroids

        
    distance_trans = transport.distance(pt) # find the distance between the centroid and all train station
    distance_postgp = post_gp.distance(pt) # find the distance between the centroid and all GP pratices
    def calculate_distances_to_nearest_points(centroid, transport_hubs, gp_practices):
    """
    Calculate distances from a centroid to the nearest transport hubs and GP practices.

    Parameters
    ----------
    centroid : shapely.geometry.point.Point
        The centroid point of a tourist site polygon.
    transport_hubs : geopandas.geodataframe.GeoDataFrame
        GeoDataFrame containing transport hub data.
    gp_practices : geopandas.geodataframe.GeoDataFrame
        GeoDataFrame containing GP practice data.

    Returns
    -------
    tuple
        A tuple containing two floats:
        - The first float represents the distance from the centroid to the nearest transport hub.
        - The second float represents the distance from the centroid to the nearest GP practice.

    Examples
    --------
    >>> centroid = tourist.geometry.centroid
    >>> distance_trans, distance_postgp = calculate_distances_to_nearest_points(centroid, transport, post_gp)
    """
    distance_trans = transport_hubs.distance(centroid)  # find the distance between the centroid and all transport hubs
    distance_postgp = gp_practices.distance(centroid)  # find the distance between the centroid and all GP practices

    return distance_trans.min(), distance_postgp.min()


        
    min_ind_trans = distance_trans.argmin() # get the index of minimum value
    min_dist_trans = distance_trans.min() # get the minimum distance
    def find_nearest_transport_hub(distance_trans):
    """
    Find the nearest transport hub from a list of distances.

    Parameters
    ----------
    distance_trans : pandas.core.series.Series
        Series containing distances from a centroid to all transport hubs.

    Returns
    -------
    tuple
        A tuple containing two values:
        - The first value represents the index of the nearest transport hub.
        - The second value represents the distance to the nearest transport hub.

    Examples
    --------
    >>> min_ind_trans, min_dist_trans = find_nearest_transport_hub(distance_trans)
    """
    min_ind_trans = distance_trans.argmin()  # get the index of the minimum value
    min_dist_trans = distance_trans.min()    # get the minimum distance
    
    return min_ind_trans, min_dist_trans


        
    min_ind_postgp = distance_postgp.argmin()
    min_dist_postgp = distance_postgp.min()
    def find_nearest_gp_practice(distance_postgp):
    """
    Find the nearest GP practice from a list of distances.

    Parameters
    ----------
    distance_postgp : pandas.core.series.Series
        Series containing distances from a centroid to all GP practices.

    Returns
    -------
    tuple
        A tuple containing two values:
        - The first value represents the index of the nearest GP practice.
        - The second value represents the distance to the nearest GP practice.

    Examples
    --------
    >>> min_ind_postgp, min_dist_postgp = find_nearest_gp_practice(distance_postgp)
    """
    min_ind_postgp = distance_postgp.argmin()  # get the index of the minimum value
    min_dist_postgp = distance_postgp.min()    # get the minimum distance
    
    return min_ind_postgp, min_dist_postgp

        
    # define column head
    tourist.loc[ind, "Near_T_Hub"] = transport.loc[min_ind_trans].Station.title() # assigns the name of the nearest transport hub and capitalizes the first letter of each word in the station name
    tourist.loc[ind, "Near_GP"] = post_gp.loc[min_ind_postgp].PracticeName #assigns the name of the nearest GP Surgery
    def assign_nearest_points_to_columns(tourist_sites, min_ind_trans, min_ind_postgp, transport_hubs, gp_practices):
    """
    Assign the names of the nearest transport hub and GP surgery to respective columns in the tourist sites GeoDataFrame.

    Parameters
    ----------
    tourist_sites : geopandas.geodataframe.GeoDataFrame
        GeoDataFrame containing tourist site data.
    min_ind_trans : int
        Index of the nearest transport hub.
    min_ind_postgp : int
        Index of the nearest GP surgery.
    transport_hubs : geopandas.geodataframe.GeoDataFrame
        GeoDataFrame containing transport hub data.
    gp_practices : geopandas.geodataframe.GeoDataFrame
        GeoDataFrame containing GP practice data.

    Returns
    -------
    None

    Examples
    --------
    >>> assign_nearest_points_to_columns(tourist, min_ind_trans, min_ind_postgp, transport, post_gp)
    """
    tourist_sites.loc[ind, "Near_T_Hub"] = transport_hubs.loc[min_ind_trans].Station.title()
    tourist_sites.loc[ind, "Near_GP"] = gp_practices.loc[min_ind_postgp].PracticeName

        
    # add distance to the closest transport hub
    tourist.loc[ind, "Trans_Dist"] = min_dist_trans / 1000 # distance in km
    tourist.loc[ind, "GP_Dist"] = min_dist_postgp / 1000
    def add_distances_to_columns(tourist_sites, min_dist_trans, min_dist_postgp):
    """
    Add distances to the closest transport hub and GP practice columns in the tourist sites GeoDataFrame.

    Parameters
    ----------
    tourist_sites : geopandas.geodataframe.GeoDataFrame
        GeoDataFrame containing tourist site data.
    min_dist_trans : float
        Distance to the nearest transport hub in meters.
    min_dist_postgp : float
        Distance to the nearest GP practice in meters.

    Returns
    -------
    None

    Examples
    --------
    >>> add_distances_to_columns(tourist, min_dist_trans, min_dist_postgp)
    """
    tourist_sites.loc[ind, "Trans_Dist"] = min_dist_trans / 1000  # distance in km
    tourist_sites.loc[ind, "GP_Dist"] = min_dist_postgp / 1000


# round the distance to cm accuracy (2 decimal places)
tourist.Trans_Dist = tourist.Trans_Dist.round(2)
tourist.GP_Dist = tourist.GP_Dist.round(2)
def round_distances(tourist_sites):
    """
    Round the distances to centimeter accuracy (2 decimal places) in the tourist sites GeoDataFrame.

    Parameters
    ----------
    tourist_sites : geopandas.geodataframe.GeoDataFrame
        GeoDataFrame containing tourist site data.

    Returns
    -------
    None

    Examples
    --------
    >>> round_distances(tourist)
    """
    tourist_sites.Trans_Dist = tourist_sites.Trans_Dist.round(2)
    tourist_sites.GP_Dist = tourist_sites.GP_Dist.round(2)

#check the head and verify that all index in the "PracticeName" column are in uppercase.
# check the head
tourist.head() # check the head of final data set
def check_head_of_final_dataset(final_dataset):
    """
    Check the head of the final dataset GeoDataFrame.

    Parameters
    ----------
    final_dataset : geopandas.geodataframe.GeoDataFrame
        GeoDataFrame containing the final dataset.

    Returns
    -------
    pandas.core.frame.DataFrame
        The first few rows of the final dataset GeoDataFrame.

    Examples
    --------
    >>> tourist_head = check_head_of_final_dataset(tourist)
    """
    return final_dataset.head()



# check the head
post_gp.head()
def check_head_of_post_gp(post_gp_data):
    """
    Check the head of the post_gp GeoDataFrame.

    Parameters
    ----------
    post_gp_data : geopandas.geodataframe.GeoDataFrame
        GeoDataFrame containing GP practice data.

    Returns
    -------
    pandas.core.frame.DataFrame
        The first few rows of the post_gp GeoDataFrame.

    Examples
    --------
    >>> post_gp_head = check_head_of_post_gp(post_gp)
    """
    return post_gp_data.head()



# Filter necessary columns
tourist_out = pd.DataFrame(tourist[["SITE", "Near_T_Hub","Trans_Dist","Near_GP", "GP_Dist"]])
def filter_necessary_columns(tourist_data):
    """
    Filter necessary columns from the tourist DataFrame.

    Parameters
    ----------
    tourist_data : pandas.core.frame.DataFrame
        DataFrame containing tourist data.

    Returns
    -------
    pandas.core.frame.DataFrame
        DataFrame containing only the necessary columns.

    Examples
    --------
    >>> tourist_out = filter_necessary_columns(tourist)
    """
    tourist_out = pd.DataFrame(tourist_data[["SITE", "Near_T_Hub", "Trans_Dist", "Near_GP", "GP_Dist"]])
    return tourist_out


# check the head
tourist_out.head()
def check_head_of_tourist_out(tourist_out_data):
    """
    Check the head of the tourist_out DataFrame.

    Parameters
    ----------
    tourist_out_data : pandas.core.frame.DataFrame
        DataFrame containing filtered tourist data.

    Returns
    -------
    pandas.core.frame.DataFrame
        The first few rows of the tourist_out DataFrame.

    Examples
    --------
    >>> tourist_out_head = check_head_of_tourist_out(tourist_out)
    """
    return tourist_out_data.head()


# Merge DataFrame and GeoDataFrame
merged = pd.merge(post_gp, tourist_out,left_on="PracticeName", right_on="Near_GP", how="inner")

def merge_dataframes_and_geodataframes(df1, gdf2, left_on=None, right_on=None, how='inner'):
    """
    Merge a DataFrame and a GeoDataFrame based on specified columns.

    This function performs a merge operation between a DataFrame (df1) and a GeoDataFrame (gdf2).
    It merges the two data structures based on the specified columns, resulting in a new DataFrame.

    Parameters
    ----------
    df1 : pandas.core.frame.DataFrame
        The first DataFrame to be merged.
    gdf2 : geopandas.geodataframe.GeoDataFrame
        The second GeoDataFrame to be merged.
    left_on : str or list, optional
        Column name(s) in the left DataFrame (df1) to merge on. If None, the merge will be based on the index.
    right_on : str or list, optional
        Column name(s) in the right GeoDataFrame (gdf2) to merge on. If None, the merge will be based on the index.
    how : {'left', 'right', 'outer', 'inner'}, default 'inner'
        Type of merge to be performed:
        - 'left': Use only keys from left DataFrame.
        - 'right': Use only keys from right GeoDataFrame.
        - 'outer': Use union of keys from both DataFrames.
        - 'inner': Use intersection of keys from both DataFrames.

    Returns
    -------
    pandas.core.frame.DataFrame
        A new DataFrame resulting from the merge operation.

    Examples
    --------
    >>> merged_data = merge_dataframes_and_geodataframes(df1, gdf2, left_on='key', right_on='key', how='inner')
    """
    merged = pd.merge(df1, gdf2, left_on=left_on, right_on=right_on, how=how)
    return merged

        
# check the head
merged.head()
def check_head_of_merged_data(merged_data):
    """
    Check the head of the merged DataFrame.

    Parameters
    ----------
    merged_data : pandas.core.frame.DataFrame
        DataFrame resulting from the merge operation.

    Returns
    -------
    pandas.core.frame.DataFrame
        The first few rows of the merged DataFrame.

    Examples
    --------
    >>> merged_head = check_head_of_merged_data(merged)
    """
    return merged_data.head()



#Filter necessary coloumns
output = pd.DataFrame(merged[["SITE", "Near_T_Hub","Trans_Dist","Near_GP", "GP_Dist","postcode"]])

def filter_necessary_columns_and_create_output_df(merged_data):
    """
    Filter necessary columns from the merged DataFrame and create a new output DataFrame.

    This function filters the necessary columns from the merged DataFrame and creates a new output DataFrame.

    Parameters
    ----------
    merged_data : pandas.core.frame.DataFrame
        DataFrame resulting from the merge operation.

    Returns
    -------
    pandas.core.frame.DataFrame
        A new DataFrame containing only the necessary columns.

    Examples
    --------
    >>> output_df = filter_necessary_columns_and_create_output_df(merged)
    """
    output = pd.DataFrame(merged_data[["SITE", "Near_T_Hub", "Trans_Dist", "Near_GP", "GP_Dist", "postcode"]])
    return output


# rename specified columns to defined new names
output.rename(columns={"SITE":"Tourist Sites", "postcode":"PostCode"},inplace=True)
def rename_columns_in_output_df(output_data):
    """
    Rename specified columns in the output DataFrame.

    This function renames specified columns in the output DataFrame to defined new names.

    Parameters
    ----------
    output_data : pandas.core.frame.DataFrame
        DataFrame containing filtered columns.

    Returns
    -------
    pandas.core.frame.DataFrame
        DataFrame with renamed columns.

    Examples
    --------
    >>> renamed_output = rename_columns_in_output_df(output)
    """
    output_data.rename(columns={"SITE": "Tourist Sites", "postcode": "PostCode"}, inplace=True)
    return output_data


# saves the output DataFrame to a CSV file.
output.to_csv("data_files/NI_Tourist_trans_GP_Dist.csv")
def save_output_to_csv(output_data, filepath):
    """
    Save the output DataFrame to a CSV file.

    This function saves the output DataFrame to a CSV file at the specified filepath.

    Parameters
    ----------
    output_data : pandas.core.frame.DataFrame
        DataFrame containing the output data to be saved.
    filepath : str
        Filepath where the CSV file will be saved.

    Returns
    -------
    None

    Examples
    --------
    >>> save_output_to_csv(output, "data_files/NI_Tourist_trans_GP_Dist.csv")
    """
    output_data.to_csv(filepath, index=False)



#--------------------------------------- iii. Coastline spots intergration ------------------------------------------------------------------------------------------------------------------------------
    """
    We'll locate the closest transport hub along with its distance and also identify the nearest GP surgery and its distance from the Coastline spots.
    """

# Read Places_to_Visit_in_Causeway_Coast_and_Glens
coastline_tmp = gpd.read_file("data_files/download_data/Places_to_Visit_in_Causeway_Coast_and_Glens.shp") # Path to the input shapefile of Places to Visit in coastaline data
def read_places_to_visit_shapefile(filepath):
    """
    Read the Places to Visit in Causeway Coast and Glens shapefile.

    This function reads the Places to Visit in Causeway Coast and Glens shapefile from the specified filepath.

    Parameters
    ----------
    filepath : str
        Path to the input shapefile of Places to Visit in Causeway Coast and Glens.

    Returns
    -------
    geopandas.geodataframe.GeoDataFrame
        GeoDataFrame containing the Places to Visit in Causeway Coast and Glens data.

    Examples
    --------
    >>> coastline_tmp = read_places_to_visit_shapefile("data_files/download_data/Places_to_Visit_in_Causeway_Coast_and_Glens.shp")
    """
    return gpd.read_file(filepath)


# check the head
coastline_tmp.head()
def check_head_of_coastline_data(coastline_data):
    """
    Check the head of the coastline GeoDataFrame.

    This function checks the head of the coastline GeoDataFrame to preview the data.

    Parameters
    ----------
    coastline_data : geopandas.geodataframe.GeoDataFrame
        GeoDataFrame containing coastline data.

    Returns
    -------
    pandas.core.frame.DataFrame
        The first few rows of the coastline GeoDataFrame.

    Examples
    --------
    >>> coastline_head = check_head_of_coastline_data(coastline_tmp)
    """
    return coastline_data.head()



# for each coastline spots ,find the closest bus/train station
# Record the Shortest distance in km and the name of the station.
for ind, row in coastline_tmp.to_crs("epsg:2157").iterrows():
    pt = row["geometry"] # consider geometry point.
    def find_closest_station_for_coastline(coastline_data, transport_data):
    """
    Find the closest bus/train station for each coastline spot.

    This function iterates through each coastline spot in the GeoDataFrame, converts the geometry to EPSG:2157 projection,
    and finds the closest bus/train station by calculating the distance between the coastline spot and all stations.

    Parameters
    ----------
    coastline_data : geopandas.geodataframe.GeoDataFrame
        GeoDataFrame containing coastline data.
    transport_data : geopandas.geodataframe.GeoDataFrame
        GeoDataFrame containing bus/train station data.

    Returns
    -------
    pandas.core.frame.DataFrame
        DataFrame containing the closest station for each coastline spot.

    Examples
    --------
    >>> closest_stations = find_closest_station_for_coastline(coastline_tmp, transport)
    """
        
    distance_trans = transport.distance(pt) # find the distance between the coastline spots and all train station
    distance_postgp = post_gp.distance(pt) # find the distance between the coastline spots and all GP pratices
    def find_distances_to_stations_and_gp_for_coastline(coastline_data, transport_data, gp_data):
    """
    Find the distances between coastline spots and all train/bus stations, as well as all GP practices.

    This function calculates the distances between each coastline spot in the GeoDataFrame and all train/bus stations,
    as well as all GP practices.

    Parameters
    ----------
    coastline_data : geopandas.geodataframe.GeoDataFrame
        GeoDataFrame containing coastline data.
    transport_data : geopandas.geodataframe.GeoDataFrame
        GeoDataFrame containing train/bus station data.
    gp_data : geopandas.geodataframe.GeoDataFrame
        GeoDataFrame containing GP practice data.

    Returns
    -------
    pandas.core.series.Series, pandas.core.series.Series
        Series containing distances between coastline spots and all train/bus stations,
        Series containing distances between coastline spots and all GP practices.

    Examples
    --------
    >>> distance_to_stations, distance_to_gp = find_distances_to_stations_and_gp_for_coastline(coastline_tmp, transport, post_gp)
    """
    # Calculate the distances between coastline spots and all train/bus stations
    distance_to_stations = coastline_data.distance(transport_data.geometry)

    # Calculate the distances between coastline spots and all GP practices
    distance_to_gp = coastline_data.distance(gp_data.geometry)

    return distance_to_stations, distance_to_gp

        
    min_ind_trans = distance_trans.argmin() # get the index of minimum value
    min_dist_trans = distance_trans.min() # get the minimum distance
    def find_minimum_distance_to_station(distance_to_station):
    """
    Find the index and value of the minimum distance to a train/bus station.

    This function calculates the index and value of the minimum distance to a train/bus station among all distances
    between coastline spots and all train/bus stations.

    Parameters
    ----------
    distance_to_station : pandas.core.series.Series
        Series containing distances between coastline spots and all train/bus stations.

    Returns
    -------
    int, float
        Index of the minimum distance, Minimum distance value.

    Examples
    --------
    >>> min_dist_index, min_distance = find_minimum_distance_to_station(distance_trans)
    """
    min_dist_index = distance_to_station.argmin()  # Get the index of the minimum distance
    min_distance = distance_to_station.min()  # Get the minimum distance

    return min_dist_index, min_distance


        
    min_ind_postgp = distance_postgp.argmin()
    min_dist_postgp = distance_postgp.min()
    def find_minimum_distance_to_gp(distance_to_gp):
    """
    Find the index and value of the minimum distance to a GP practice.

    This function calculates the index and value of the minimum distance to a GP practice among all distances
    between coastline spots and all GP practices.

    Parameters
    ----------
    distance_to_gp : pandas.core.series.Series
        Series containing distances between coastline spots and all GP practices.

    Returns
    -------
    int, float
        Index of the minimum distance, Minimum distance value.

    Examples
    --------
    >>> min_gp_dist_index, min_gp_distance = find_minimum_distance_to_gp(distance_postgp)
    """
    min_gp_dist_index = distance_to_gp.argmin()  # Get the index of the minimum distance
    min_gp_distance = distance_to_gp.min()  # Get the minimum distance

    return min_gp_dist_index, min_gp_distance


        
    # define column head
    coastline_tmp.loc[ind, "Near_T_Hub"] = transport.loc[min_ind_trans].Station.title() # assigns the name of the nearest transport hub and capitalizes the first letter of each word in the station name
    coastline_tmp.loc[ind, "Near_GP"] = post_gp.loc[min_ind_postgp].PracticeName #assigns the name of the nearest GP Surgery
    def assign_nearest_stations_to_coastline(coastline_data, transport_data, gp_data, min_dist_station_index, min_dist_gp_index):
    """
    Assign the names of the nearest transport hub and the nearest GP surgery to each coastline spot.

    This function assigns the names of the nearest transport hub and the nearest GP surgery to each coastline spot
    in the GeoDataFrame based on the provided indices of the nearest station and GP practice.

    Parameters
    ----------
    coastline_data : geopandas.geodataframe.GeoDataFrame
        GeoDataFrame containing coastline data.
    transport_data : geopandas.geodataframe.GeoDataFrame
        GeoDataFrame containing train/bus station data.
    gp_data : geopandas.geodataframe.GeoDataFrame
        GeoDataFrame containing GP practice data.
    min_dist_station_index : int
        Index of the nearest transport hub.
    min_dist_gp_index : int
        Index of the nearest GP surgery.

    Returns
    -------
    None

    Examples
    --------
    >>> assign_nearest_stations_to_coastline(coastline_tmp, transport, post_gp, min_ind_trans, min_ind_postgp)
    """
    # Assign the name of the nearest transport hub to each coastline spot
    coastline_data["Near_T_Hub"] = transport_data.loc[min_dist_station_index, "Station"].title()

    # Assign the name of the nearest GP surgery to each coastline spot
    coastline_data["Near_GP"] = gp_data.loc[min_dist_gp_index, "PracticeName"]

    # Note: The function modifies the GeoDataFrame in place, so it doesn't return anything


        
    # add distance to the closest transport hub
    coastline_tmp.loc[ind, "Trans_Dist"] = min_dist_trans / 1000 # distance in km
    coastline_tmp.loc[ind, "GP_Dist"] = min_dist_postgp / 1000
    def add_distances_to_coastline(coastline_data, min_dist_trans, min_dist_postgp):
    """
    Add distances to the closest transport hub and the nearest GP surgery to each coastline spot.

    This function adds distances to the closest transport hub and the nearest GP surgery (in kilometers) to each
    coastline spot in the GeoDataFrame.

    Parameters
    ----------
    coastline_data : geopandas.geodataframe.GeoDataFrame
        GeoDataFrame containing coastline data.
    min_dist_trans : float
        Minimum distance to the closest transport hub (in meters).
    min_dist_postgp : float
        Minimum distance to the nearest GP surgery (in meters).

    Returns
    -------
    None

    Examples
    --------
    >>> add_distances_to_coastline(coastline_tmp, min_dist_trans, min_dist_postgp)
    """
    # Add distance to the closest transport hub (in km)
    coastline_data["Trans_Dist"] = min_dist_trans / 1000
    
    # Add distance to the nearest GP surgery (in km)
    coastline_data["GP_Dist"] = min_dist_postgp / 1000

    # Note: The function modifies the GeoDataFrame in place, so it doesn't return anything



# round the distance to cm accuracy (2 decimal places)
coastline_tmp.Trans_Dist = coastline_tmp.Trans_Dist.round(2)
coastline_tmp.GP_Dist = coastline_tmp.GP_Dist.round(2)
def round_distances_to_cm(coastline_data):
    """
    Round the distances to centimeter accuracy (2 decimal places).

    This function rounds the distances to the nearest centimeter (2 decimal places) for both transportation and GP distances
    in the provided GeoDataFrame containing coastline data.

    Parameters
    ----------
    coastline_data : geopandas.geodataframe.GeoDataFrame
        GeoDataFrame containing coastline data.

    Returns
    -------
    None

    Examples
    --------
    >>> round_distances_to_cm(coastline_tmp)
    """
    # Round the transportation distances to centimeter accuracy (2 decimal places)
    coastline_data["Trans_Dist"] = coastline_data["Trans_Dist"].round(2)

    # Round the GP distances to centimeter accuracy (2 decimal places)
    coastline_data["GP_Dist"] = coastline_data["GP_Dist"].round(2)

    # Note: The function modifies the GeoDataFrame in place, so it doesn't return anything






# check the head
coastline_tmp.head()
def check_head_of_coastline(coastline_data):
    """
    Check the head of the coastline GeoDataFrame.

    Parameters
    ----------
    coastline_data : geopandas.geodataframe.GeoDataFrame
        GeoDataFrame containing coastline data.

    Returns
    -------
    pandas.core.frame.DataFrame
        The first few rows of the coastline GeoDataFrame.

    Examples
    --------
    >>> coastline_head = check_head_of_coastline(coastline_tmp)
    """
    return coastline_data.head()



# This code filters the necessary columns 
coastal_out = gpd.GeoDataFrame(coastline_tmp[["Name", "Website","geometry", "Near_T_Hub","Trans_Dist","Near_GP", "GP_Dist","Postcode"]])
def filter_and_create_coastal_out(coastline_data):
    """
    Filter necessary columns and create a new GeoDataFrame.

    This function filters the necessary columns from the input GeoDataFrame and creates a new GeoDataFrame
    containing only the specified columns.

    Parameters
    ----------
    coastline_data : geopandas.geodataframe.GeoDataFrame
        GeoDataFrame containing coastline data.

    Returns
    -------
    geopandas.geodataframe.GeoDataFrame
        GeoDataFrame containing filtered columns.

    Examples
    --------
    >>> coastal_out = filter_and_create_coastal_out(coastline_tmp)
    """
    coastal_out = gpd.GeoDataFrame(coastline_data[["Name", "Website", "geometry", "Near_T_Hub", "Trans_Dist", "Near_GP", "GP_Dist", "Postcode"]])
    return coastal_out


# reprojected
coastal_out.to_crs("epsg:4326")
def reproject_to_epsg4326(geodataframe):
    """
    Reproject a GeoDataFrame to EPSG:4326 coordinate reference system (CRS).

    This function reprojects the input GeoDataFrame to EPSG:4326 coordinate reference system (CRS).

    Parameters
    ----------
    geodataframe : geopandas.geodataframe.GeoDataFrame
        GeoDataFrame to be reprojected.

    Returns
    -------
    geopandas.geodataframe.GeoDataFrame
        Reprojected GeoDataFrame.

    Examples
    --------
    >>> reprojected_geodataframe = reproject_to_epsg4326(coastal_out)
    """
    reprojected_geodataframe = geodataframe.to_crs("epsg:4326")
    return reprojected_geodataframe


# saves the output DataFrame to a CSV file.
coastal_out.to_file("data_files/NI_Coastal_spots.geojson",driver="GeoJSON")

def save_to_geojson(geodataframe, filepath):
    """
    Save a GeoDataFrame to a GeoJSON file.

    This function saves the input GeoDataFrame to a GeoJSON file.

    Parameters
    ----------
    geodataframe : geopandas.geodataframe.GeoDataFrame
        GeoDataFrame to be saved.
    filepath : str
        Filepath to save the GeoJSON file.

    Returns
    -------
    None

    Examples
    --------
    >>> save_to_geojson(coastal_out, "data_files/NI_Coastal_spots.geojson")
    """
    geodataframe.to_file(filepath, driver="GeoJSON")

    # Note: The function doesn't return anything


#======================================================= End of 4. =============================================================================================================





#===================================================== End of Script ===========================================================================================================




