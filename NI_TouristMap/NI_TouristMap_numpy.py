#!/usr/bin/env python
# coding: utf-8

# Norther Ireland Tourist Map With Folium
# Explore Northern Ireland : Tourist Map with Integrated Transportation Hubs, GP Surgeries and Post Codes

# Repository : [sereneeosman/egm722_serenee](https://github.com/sereneeosman/egm722_serenee)

# Numpy Docstring : https://github.com/sereneeosman/egm722_serenee/blob/main/NI_TouristMap/NI_TouristMap_numpy.py

# Numpy(Sphinx) Documentation 
# https://github.com/sereneeosman/egm722_serenee/blob/main/NI_TouristMap/NI_Tourist_Map_doc.rst

def create_ni_tourist_map():
    """
    Create an interactive tourist map of Northern Ireland using folium.

    This module instruct how to reads geospatial data from shapefiles and CSV files to create an interactive Folium map,
    displaying various points of interest across Northern Ireland. It visualizes tourist sites, web links, transportation
    hubs, GP surgeries, distance, postal codes and coastal spots. Popups are included for detailed information when hovering over
    each feature.

    Returns
    -------
    folium.Map
        An interactive Folium map displaying polygon of tourist sites , transportation hubs,
        GP surgeries, and its distance as a popup with postal codes. Coastal spots are marked with popup markers in Northern Ireland.

    Notes
    -----
    This function assumes the availability of the following data files:
    - 'NI_Outline.shp': Country outline shapefile.
    - 'NI_Counties.shp': Counties shapefile.
    - 'NI_Tourist_trans_GP_Dist.csv': CSV file containing name of tourist spots, transportation hub, GP surgeries,distance and postal code data.
    - 'NI_Tourist_Sites.shp': Polyogn data of Tourist sites shapefile.
    - 'NI_Coastal_spots.geojson': GeoJSON file containing coastal spots data, nearest transportation hubs, GP surgeries, and postal codes.
    
    Examples
    --------
    >>> create_ni_tourist_map()
    
    """



#================================================== Importing Libraries =========================================================================

# To get started, first import the required standard python libraries.

# Importing the `os` library 
# Importing the `pandas` library with the alias `pd`
# Importing the `geopandas` library with the alias `gpd` 
# Importing the `folium` library 

import os
import pandas as pd
import geopandas as gpd
import folium

    """
    This script demonstrates how to create an interactive tourist map of Northern Ireland using Folium.

    To get started, first import the required standard Python libraries.

    Importing the `os` library
    Importing the `pandas` library with the alias `pd`
    Importing the `geopandas` library with the alias `gpd`
    Importing the `folium` library
    """


#================================================== Reading Geospatial Data =========================================================================

# Read the shapefiles
outline = gpd.read_file(os.path.abspath("data_files/NI_Outline.shp")) # Path to the input shapefile of Country Outline data 
counties = gpd.read_file(os.path.abspath("data_files/NI_Counties.shp")) # Path to the input shapefile of Counties data 

def geopandas.read_file(outline_path, counties_path):
    """
    Reads shapefiles containing the outline of Northern Ireland and county boundaries.

    Parameters
    ----------
    outline_path : str
        Path to the input shapefile containing Country Outline data.
    counties_path : str
        Path to the input shapefile containing Counties data.

    Returns
    -------
    tuple
        A tuple containing two GeoDataFrames:
        - outline: GeoDataFrame representing the Country Outline.
        - counties: GeoDataFrame representing the Counties data.

    Examples
    --------
    # Example usage:
    outline, counties = read_shapefiles("data_files/NI_Outline.shp", "data_files/NI_Counties.shp")
    print(outline.head())  # Display the first few rows of the Country Outline data.
    print(counties.head())  # Display the first few rows of the Counties data.
    """
    outline = gpd.read_file(outline_path)
    counties = gpd.read_file(counties_path)
    return outline, counties
    


#================================================== Creating a Base Folium Map =========================================================================

# Create a Base Map on Counties name.
m = counties.explore("CountyName", cmap = "Set2")

def explore(self, column_name, cmap=None):
    """
    Visualizes the data in the specified column_name using exploratory visualization techniques.

    Parameters
    -----------
　　column_name : str
        The name of the column to visualize.
    cmap : str or Colormap, optional
        The colormap to use for the visualization. If None, the default colormap will be used.

    Returns
    -----------
　　matplotlib.pyplot.figure: 
        The matplotlib figure object containing the visualization.

    Raises
    -----------
    ValueError
        If the column_name does not exist in the dataset.
    TypeError
        If the column_name is not a string, or cmap is not a string or a Colormap object.
    
    Examples
    -----------
　　# Visualize the distribution of population across counties using the 'Population' column
        counties.explore("Population")

　　# Visualize the distribution of income across counties using a custom colormap
        counties.explore("Income", cmap="Set2")
　　"""
　　counties.explore(column_name, cmap=cmap)




# Adding Country outline into Base folium map
folium.GeoJson(
    outline, # outline shape data
    style_function=lambda feature: {    # customize the style of the GeoJSON features
        "color": "black", # sets the color of the outline to black
        "fillOpacity": 0 # sets the fill opacity as transparent
    },
    name="outline" #name of the GeoJson layer
).add_to(m) #adds the GeoJson layer to the base folium map _m_.

def add_geojson_outline_to_map(outline, m):
    """
    Add GeoJSON outline to a Folium map.
    
    This function takes GeoJSON outline data and adds it as a new layer to a given Folium map object. 
    The style of the GeoJSON features is customized to have a black outline and transparent fill.
    
    Parameters
    -----------
    outline : dict or str
        GeoJSON outline shape data.
    m : folium.Map
        Base Folium map to which the GeoJSON outline will be added.

    Returns
    -----------
        folium.folium.Map
        The Folium map object with the added GeoJSON layer.
    
    Example
    -----------
        outline_data = {...}  # GeoJSON outline data
        my_map = folium.Map(...)  # Base Folium map
        add_geojson_outline_to_map(outline_data, my_map)
    
    """
    folium.GeoJson(
        outline,
        style_function=lambda feature: {
            "color": "black",
            "fillOpacity": 0
        },
        name="outline"
    ).add_to(m)
    return m        




# Display the base folium map
m

def display_folium_map(m):
    """
    Displays a Folium map.
    
    This function takes a Folium map object and displays it.

    Parameters
    -----------
    m : folium.Map
        Folium map object to be displayed.

    Returns
    -----------
    None
        The map is displayed in the current environment.

    Example
    -----------
    import folium

    # Assuming 'm' is a Folium map object
    display_folium_map(m)
    """
    pass



#============================= Convert DataFrame to GeoDataFrame, Display Popups and Plotting Geographic Data (Tourist Sites) ================================

# Convert DataFrame to GeoDataFrame

# read intergrated csv file
df = pd.read_csv("data_files/NI_Tourist_trans_GP_Dist.csv")

def read_integrated_csv_file(file_path):
    """
    Reads an integrated CSV file into a pandas DataFrame.
    This function reads a CSV file from the specified file path and loads it into a pandas DataFrame. 
    It is specifically used for reading the 'NI_Tourist_trans_GP_Dist.csv' file which contains data related to tourist transportation in Northern Ireland.
    
    Parameters
    -----------
    file_path : str
        Path to the integrated CSV file.

    Returns
    -----------
    pandas.DataFrame
        DataFrame containing the data from the CSV file.

    Example
    -----------
    import pandas as pd

    # Assuming the integrated CSV file is located at 'data_files/NI_Tourist_trans_GP_Dist.csv'
    df = read_integrated_csv_file("data_files/NI_Tourist_trans_GP_Dist.csv")
    """
    return pd.read_csv(file_path)
    




#Check the head
df.head()

def check_dataframe_head(dataframe):
    """
    Display the first few rows of a DataFrame.

    This function takes a pandas DataFrame object and returns the first five rows by default. 
    It is used to quickly check the header and the first few entries of the DataFrame to ensure it has been read correctly.

    Parameters
    -----------
    df : pandas.DataFrame
        The DataFrame whose header and first few rows are to be displayed.

    Returns
    -----------
    pandas.DataFrame
        A DataFrame containing the first five rows of the input DataFrame.

    Example
    -----------
    >>> import pandas as pd
    >>> df = pd.read_csv("data_files/NI_Tourist_trans_GP_Dist.csv")
    >>> check_dataframe_head(df)
    """
    return df.head()





# read tourist site polygon data
tourist = gpd.read_file(os.path.abspath("data_files/NI_Tourist_Sites.shp")) # path to the tourist site shapefile data

def read_tourist_site_polygon_data(file_path):
    """
    Read tourist site polygon data from a shapefile into a GeoDataFrame.

    This function reads a shapefile containing polygon data for tourist sites and loads it into a GeoPandas GeoDataFrame. 
    The file path is converted to an absolute path to ensure correct file location.

    Parameters
    -----------
    file_path : str
        The file path of the shapefile to be read. 
        It should be a relative path from the current working directory to the 'NI_Tourist_Sites.shp' file.

    Returns
    -----------
    geopandas.GeoDataFrame
        A GeoDataFrame containing the polygon data of tourist sites.

    Example
    -----------
    
    # import geopandas as gpd
    # Assuming the shapefile containing tourist site polygon data is located at 'data_files/NI_Tourist_Sites.shp'
    
    >>> import geopandas as gpd
    >>> import os
    >>> file_path = "data_files/NI_Tourist_Sites.shp"
    >>> tourist = read_tourist_site_polygon_data(os.path.abspath(file_path))
    >>> tourist.head()
    """
    return gpd.read_file(os.path.abspath(file_path))
    




# Displaying the column names of the shapefile.
tourist.columns

def display_shapefile_column_names(geodataframe):
    """
    Displays the column names of a GeoDataFrame representing a shapefile.
    This function takes a GeoPandas GeoDataFrame object, which has been read from a shapefile, and returns the column names. 
    It is useful for understanding the structure of the shapefile data by listing all the attribute fields available.
    
    Parameters
    -----------
    tourist : geopandas.GeoDataFrame
        The GeoDataFrame object read from a shapefile whose columns are to be displayed.

    Returns
    -----------
    list
        A list containing the names of the columns in the GeoDataFrame.

    Example
    -----------
    
    # Assuming 'tourist' is a GeoDataFrame representing a shapefile
    display_shapefile_column_names(tourist)
    >>> import geopandas as gpd
    >>> tourist = gpd.read_file("path_to_shapefile.shp")
    >>> display_shapefile_columns(tourist)
    """
    return tourist.columns





# Merge the CSV data (DataFrame) with the shapefile data (GeoDataFrame) based on a common column.
merge_site = tourist.merge(df, left_on="SITE", right_on= "Tourist Sites")

def merge_dataframe_with_geodataframe(geodataframe, dataframe, left_column, right_column):
    """
    Merges a pandas DataFrame with a GeoDataFrame based on a common column.

    Parameters
    -----------
    
    geodataframe : tourist (geopandas.GeoDataFrame)
        The GeoDataFrame containing the shapefile data.
    dataframe : df (pandas.DataFrame)
        The DataFrame containing the CSV data.
    left_column : str
        Name of the common column in the GeoDataFrame to merge on.
    right_column : str
        Name of the common column in the DataFrame to merge on.
    

    Returns
    -----------
    geopandas.GeoDataFrame
        A GeoDataFrame resulting from the merge, containing combined data from both the shapefile and CSV file.

    Example
    -----------

    import pandas as pd
    import geopandas as gpd

    # Assuming 'tourist' is a GeoDataFrame and 'df' is a pandas DataFrame
    'SITE' is the common column in 'tourist',
    and 'Tourist Sites' is the common column in 'df'
    merge_site = merge_dataframe_with_geodataframe(tourist, df, "SITE", "Tourist Sites")
    
    """
    return tourist.merge(df, left_on=left_column, right_on=right_column)





#Displays the first few rows of a merged DataFrame.
merge_site.head()

def display_merged_geodataframe_head(merged_geodataframe):
    """
    Display the first few rows of the merged GeoDataFrame.

    This function takes a merged GeoDataFrame, which is the result of combining shapefile data with CSV data, and displays the first five rows. 
    It is used to quickly inspect the top rows of the merged dataset to ensure the merge was successful.

    Parameters
    -----------
    merge_site : geopandas.GeoDataFrame
        The merged GeoDataFrame containing combined data from both the shapefile and CSV file.

    Returns
    -----------
    pandas.DataFrame
        A DataFrame containing the first five rows of the merged GeoDataFrame.

    Example
    -----------
    
    # Assuming 'merge_site' is the merged geoDataFrame
    display_merged_geodataframe_head(merge_site)
    """
    return merge_site.head()





# create a new GeoDataFrame named "visit_geo" by selecting specific columns from the previously merged DataFrame "merge_site".
visit_filter = merge_site[["Tourist Sites", "Near_T_Hub","Trans_Dist","Near_GP", "GP_Dist","PostCode","geometry"]]

def create_visit_geodataframe(merged_dataframe, columns):
    """
    Creates a new GeoDataFrame by selecting specific columns from a merged DataFrame.
    
    This function selects specific columns related to tourist sites, their proximity to transportation hubs and general practitioners (GPs), and their postal codes from a previously merged GeoDataFrame. 
    It then creates a new GeoDataFrame named 'visit_geo' with this filtered data.
    
    Parameters
    -----------
    merged_dataframe : geopandas.GeoDataFrame
        The merged GeoDataFrame from which to select columns.
    columns : list of str
        List of column names to be selected.

    Returns
    -----------
    geopandas.GeoDataFrame
        GeoDataFrame containing selected columns.

    Example
    -----------
    
    # Assuming 'merge_site' is the merged DataFrame and specified columns are ["Tourist Sites", "Near_T_Hub", "Trans_Dist", "Near_GP", "GP_Dist", "PostCode", "geometry"]
    visit_geo = create_visit_geodataframe(merge_site, ["Tourist Sites", "Near_T_Hub", "Trans_Dist", "Near_GP", "GP_Dist", "PostCode", "geometry"])
    
    """
    return merged_dataframe[columns]





# Creating a new geodataframe with filtered columns   
visit_geo = gpd.GeoDataFrame(visit_filter)

def create_geodataframe_from_dataframe(dataframe):
    """
    Create a GeoDataFrame named 'visit_geo' from the filtered data.

    This function takes a DataFrame with filtered data and converts it into a GeoDataFrame. 
    This is particularly useful when dealing with spatial data, as it allows for the use of geographic operations on the data.

    Parameters
    -----------
    dataframe : pandas.DataFrame
        The DataFrame containing the filtered data which includes columns for tourist sites, transportation hubs, distances, and geometry.

    Returns
    -----------
    geopandas.GeoDataFrame
        A GeoDataFrame containing the spatial data from the filtered DataFrame.

    Example
    -----------
    # Assuming 'visit_filter' is the pandas DataFrame
    visit_geo = create_geodataframe_from_dataframe(visit_filter)
    """
    return gpd.GeoDataFrame(dataframe)
    




# checking the head
visit_geo.head()

def display_geodataframe_head(geodataframe):
    """
    Display the first few rows of the 'visit_geo' GeoDataFrame.

    This function takes the 'visit_geo' GeoDataFrame, which contains selected information about tourist sites, and displays the first five rows. 
    It is used to quickly inspect the top rows of the dataset to ensure it contains the correct data.


    Parameters
    -----------
    geodataframe : geopandas.GeoDataFrame
        The 'visit_geo' GeoDataFrame containing selected tourist site data.

    Returns
    -----------
    pandas.DataFrame
        A DataFrame containing the first five rows of the 'visit_geo' GeoDataFrame.

    Example
    -----------
    # Assuming 'visit_geo' is the GeoDataFrame
    display_geodataframe_head(visit_geo)
    """
    return geodataframe.head()





# add county names into the visit_geo file, where geometries intersect.
visit_merge = gpd.sjoin(visit_geo,counties,how="inner")

def spatial_join_geodataframes(left_geodataframe, right_geodataframe, how="inner"):
    """
    Performs a spatial join between two GeoDataFrames.
    This function takes two GeoDataFrames: 'visit_geo', which contains selected tourist site data, and 'counties', which contains county boundary data. 
    It performs an inner spatial join based on the geometry columns of both GeoDataFrames, resulting in a new GeoDataFrame that combines information from both sources where their geometries intersect.
    
    Parameters
    -----------
    left_geodataframe : geopandas.GeoDataFrame
        Left GeoDataFrame for the spatial join.
    right_geodataframe : geopandas.GeoDataFrame
        Right GeoDataFrame for the spatial join.
    how : str, optional
        Type of join to be performed. Default is "inner".
        - 'left': use keys from left_geodataframe; retain only left_geodataframe geometry column
        - 'right': use keys from right_geodataframe; retain only right_geodataframe geometry column
        - 'inner': use intersection of keys from both GeoDataFrames; retain only left_geodataframe geometry column

    Returns
    -----------
    geopandas.GeoDataFrame
        A new GeoDataFrame resulting from the spatial join, containing combined data from both left_geodataframe and right_geodataframe.

    
    Example
    -----------
    # Assuming 'visit_geo' and 'counties' are GeoDataFrames
    visit_merge = spatial_join_geodataframes(visit_geo, counties, how="inner")
    """
    return gpd.sjoin(left_geodataframe, right_geodataframe, how=how)
    



# check the head
visit_merge.head()

def display_head_of_visit_merge(visit_merge):
    """
    Display the first few rows of the 'visit_merge' GeoDataFrame.

    This function takes the 'visit_merge' GeoDataFrame, which is the result of a spatial join between tourist site data and county boundary data, and displays the first five rows. It is used to quickly inspect the top rows of the merged dataset to ensure the merge was successful and the data is structured correctly.

    Parameters
    ----------
    visit_merge : geopandas.GeoDataFrame
        The 'visit_merge' GeoDataFrame resulting from a spatial join, containing combined tourist site and county data.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the first five rows of the 'visit_merge' GeoDataFrame.

    Examples
    --------
    # Assuming 'visit_merge' is a GeoDataFrame resulting from a spatial join.
    >>> import geopandas as gpd
    >>> display_head_of_visit_merge(visit_merge)
    """
    return visit_merge.head()






#filters specific columns 
visit_all = visit_merge[["Tourist Sites", "Near_T_Hub","Trans_Dist","Near_GP", "GP_Dist","PostCode","geometry","CountyName"]]

def filter_specific_columns(visit_merge):
    """
    Filter specific columns from a GeoDataFrame..
    This function takes a GeoDataFrame resulting from a spatial join and filters out specific columns related to tourist sites, their proximity to transportation hubs and GPs, postal codes, geometry, and county names. 
    The result is a new GeoDataFrame with only the selected columns.
    
    Parameters
    ----------
    visit_merge : geopandas.GeoDataFrame
        The GeoDataFrame from which specific columns are to be filtered.

    Returns
    -------
    geopandas.GeoDataFrame
        A new GeoDataFrame containing only the specified columns related to tourist sites, transportation hubs, distances, GP surgeries, postal codes, geometry, and county names.

    Examples
    --------
    >>> visit_all = filter_specific_columns(visit_merge)
    """
    visit_all = visit_merge[["Tourist Sites", "Near_T_Hub", "Trans_Dist", "Near_GP", "GP_Dist", "PostCode", "geometry", "CountyName"]]
    return visit_all

#filters specific columns 
visit_all = visit_merge[["Tourist Sites", "Near_T_Hub","Trans_Dist","Near_GP", "GP_Dist","PostCode","geometry","CountyName"]]





# check the head
visit_all.head()

def check_head(visit_all):
    """
    Display the first few rows of the 'visit_all' GeoDataFrame.

    This function takes the 'visit_all' GeoDataFrame, which contains filtered data from a spatial join, and displays the first five rows. 
    It is used to quickly inspect the top rows of the dataset to ensure it contains the correct data and the filtering was successful.

    Parameters
    ----------
    visit_all : geopandas.GeoDataFrame
        The 'visit_all' GeoDataFrame containing filtered tourist site data.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the first five rows of the 'visit_all' GeoDataFrame.

    Examples
    --------
    >>> # Assuming 'visit_all' is a GeoDataFrame created from selected columns of 'visit_merge'.
    >>> display_head_of_visit_all(visit_all)
    """
    return visit_all.head()




def GeoDataFrame.explore(*args, **kwargs):
    """
    Explore the GeoDataFrame using custom visualization parameters.

    This method provides a convenient way to visualize GeoDataFrame data using custom parameters.
    It accepts both positional and keyword arguments for flexibility in customization.

    Parameters
    ----------
    *args : positional arguments
        Positional arguments for customization. These can include column names, style parameters, etc.
    **kwargs : keyword arguments
        Keyword arguments for customization. These can include parameters like cmap, legend, popup, etc.

    Returns
    -------
    matplotlib.pyplot.figure
        A matplotlib figure object containing the visualization.

    Examples
    --------
    # Explore the GeoDataFrame using custom visualization parameters
    gdf.explore("column_name", cmap="viridis", legend=True, popup=True)
    """

# Display Popups and Plotting Geographic Data (Tourist Sites)

# displaying the Geodatabase on the folium map and popup the attribute information.
visit_all.explore("CountyName", # show the CountyName column
                  cmap="gist_rainbow", # use the "hsv" colormap from matplotlib
                  m=m, # set the base folium.map
                  popup = True, #Show information as popup when curser move on to the polygon
                  legend = False, #Don`t display a separated legend.
)                  

def display_geodatabase_on_map(visit_all, cmap, m, popup=True, legend=False):
    """
    Display a GeoDataFrame on a Folium map with optional popups and a legend.

    Parameters
    ----------
    visit_all : geopandas.GeoDataFrame
        The GeoDataFrame to be displayed on the map.
    cmap : str or matplotlib.colors.Colormap
        The colormap to be used for displaying the GeoDataFrame.
    m : folium.Map
        The base Folium map on which the GeoDataFrame will be displayed.
    popup : bool, optional
        If True, display attribute information as popups when cursor moves over feature. Default is True..
    legend : bool, optional
        If True, display a legend for the colormap. Default is False..

    Returns
    -------
    None
        This function does not return anything. It displays the Geodatabase on the provided Folium map.

    Examples
    --------
    >>> display_geodatabase_on_map(visit_all, "gist_rainbow", m, popup, legend)
    """
    visit_all.explore(column="CountyName", cmap=cmap, m=m, popup=popup, legend=legend)
                      



#============================================== Adding Coastline visit spots into Folim map =================================================================
# read geojason file
coastalpt = gpd.read_file(os.path.abspath("data_files/NI_Coastal_spots.geojson"))

# Adding Coastline visit spots into Folim map #
def read_geojson_file(file_path):
    """
    Read a GeoJSON file into a GeoDataFrame.
    
    This function reads a GeoJSON file from the specified file path and loads it into a GeoPandas GeoDataFrame. 
    GeoJSON is an open standard format designed for representing simple geographical features along with their non-spatial attributes.
    
    Parameters
    ----------
    file_path : str
        The path to the GeoJSON file to be read.

    Returns
    -------
    geopandas.GeoDataFrame
        A GeoDataFrame containing the data from the GeoJSON file.

    Examples
    --------
    >>> coastalpt = read_geojson_file("data_files/NI_Coastal_spots.geojson")
    """
    return gpd.read_file(os.path.abspath(file_path))






#display coastal points head
coastalpt.head()

def display_coastal_points_head(coastalpt):
    """
    Display the first few rows of the 'coastalpt' GeoDataFrame.

    This function takes the 'coastalpt' GeoDataFrame, which contains coastal point data, and displays the first five rows. 
    It is used to quickly inspect the top rows of the dataset to ensure it contains the correct data.

    Parameters
    ----------
    coastalpt : geopandas.GeoDataFrame
        The GeoDataFrame whose header needs to be checked.
        The GeoDataFrame containing coastal point data.

    Returns
    -------
    pandas.DataFrame
        A DataFrame containing the first five rows of the 'coastalpt' GeoDataFrame.
        

    Examples
    --------
    >>> display_coastal_points_head(coastalpt)
    """
    return coastalpt.head()











# defining parameters for configuring the display of "coastalpt" `markers` 
coastalpt_args = {
    "m": m, # specifies the folium map (m)
    "marker_type": "marker", #specifies the type of marker
    "popup": True, #Show information as popup when curser move on to the polygon
    "legend": False, # Don`t display a separated legend.
    "marker_kwds": {"icon": folium.Icon(color="red", icon="star", prefix='fa')} #style of the marker icon display red color marker with star and refer FontAwesome icon Library    
}

def configure_coastalpt_markers(m, marker_type="marker", popup=True, legend=False, marker_kwds={"icon": folium.Icon(color="str", icon="folium.map.Icon", prefix='str')}):
    """
    Define parameters for configuring the display of markers for the 'coastalpt' GeoDataFrame on a Folium map.
    
    This function sets up the parameters for displaying markers on a Folium map. 
    It specifies the base map, marker type, popup configuration, legend visibility, and marker icon style using the FontAwesome icon library.
 
    Parameters
    ----------
    coastalpt_args : dict
    A dictionary containing the following key-value pairs:
    
    m : folium.Map
        The base Folium map on which the markers will be displayed.
    marker_type : str, optional
        The type of marker to be displayed. Default is "marker".
    popup : bool, optional
        If True, display information as popups when cursor moves over the markers. Default is True.
    legend : bool, optional
        If True, display a legend for the markers. Default is False.
    marker_kwds : dict, optional
        icon: folium.map.Icon
        color : str
        prefix : 'fa' (FrontAwsome Library)
        Additional keyword arguments for styling the marker icons. 

    Returns
    -------
    dict
        A dictionary containing the configured parameters for displaying markers.

    Examples
    --------
    >>> coastalpt_args = configure_coastalpt_markers(m, marker_type="marker", popup=True, legend=False, marker_kwds={"icon": folium.Icon(color="red", icon="star", prefix='fa')})
    """
    return {
        "m": m,
        "marker_type": marker_type,
        "popup": popup,
        "legend": legend,
        "marker_kwds": marker_kwds
    }







# Display the "coastalpt" Marker on the folium map with the customized marker dictionary
coastalpt.explore ("Name", **coastalpt_args)

def display_coastalpt_markers(geodataframe, attribute_column, **marker_args):
    """
    Display markers for a GeoDataFrame on a Folium map with customized marker settings.
    This function takes a GeoDataFrame containing coastal point data and displays it on a Folium map as markers. 
    The markers are customized according to the specifications provided in the `coastalpt_args` dictionary. 
    The 'Name' column from the GeoDataFrame is used to label the markers.
    
    Parameters
    ----------
    geodataframe : geopandas.GeoDataFrame
        The GeoDataFrame containing the markers to be displayed.
    attribute_column : str
        The column in the GeoDataFrame to be used for labeling the markers.
    **marker_args : dict
        Additional keyword arguments specifying marker configuration parameters.

    Returns
    -------
    folium.Map
        The Folium map object with the 'coastalpt' markers displayed.

    Examples
    --------
    >>> display_coastalpt_markers(coastalpt, "Name", **coastalpt_args)
    >>> geodataframe.explore(attribute_column, **marker_args)
    """
    
    return geodataframe.explore(attribute_column, **coastalpt_args)



#========================================================= Exporting Folium Map ==========================================================================

#save the created folim map (represented by the m object) as an HTML file.
m.save("NI_tourist_MAP.html")

def save_folium_map_as_html(folium_map, file_path):
    """
    Save a Folium map as an HTML file.
    
    This function takes a Folium map object and saves it to an HTML file with the specified filename. 
    This allows the map to be viewed in a web browser or embedded in a web page.
    
    Parameters
    ----------
    folium_map : folium.Map
        The Folium map to be saved.
    file_path : str
        The path where the HTML file will be saved.

    Returns
    -------
    None
        This function does not return anything. It saves the Folium map as an HTML file.

    Examples
    --------
    >>> save_folium_map_as_html(m, "NI_tourist_MAP.html")
    """
    folium_map.save(file_path)




#You can then open this HTML file in a web browser to view the interactive map.
