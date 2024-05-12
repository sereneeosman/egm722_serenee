Northern Ireland Tourist Map with Folium
=====================

**Explore Northern Ireland : Tourist Map with Integrated Transportation Hubs, GP Surgeries and Post Codes.**



*link for repositories:*

.. raw:: html

   <div style="display: flex; justify-content: space-between;">
       <div>
           <a href="https://github.com/sereneeosman/egm722_serenee" class="github-button" aria-label="Star sereneeosman/egm722_serenee on GitHub" data-show-count="true" data-count-aria-label="# stars on GitHub">Link EGM722</a>
           <script async defer src="https://buttons.github.io/buttons.js"></script>
       </div>
       <div>
           <a href="https://github.com/sereneeosman/sereneeosman_doc" class="github-button" aria-label="Star sereneeosman/sereneeosman_doc on GitHub" data-show-count="true" data-count-aria-label="# stars on GitHub">Link Documentation</a>
           <script async defer src="https://buttons.github.io/buttons.js"></script>
       </div>
       <div>
           <a href="path/to/your/document.pdf" class="pdf-button" aria-label="Download PDF">Download PDF</a>
       </div>
   </div>


:download:`Download PDF <_static/pdf/document_name.pdf>`



Contents
--------
- Overview
- Data Provided
- Setup
- Getting Started

Overview
--------

Northern Ireland boasts a rich tapestry of history, culture, and natural beauty, attracting visitors from around the globe. However, navigating its diverse landscapes and accessing essential services can be daunting, especially for newcomers. Recognizing this challenge, I introduced the "Explore Northern Ireland" script, a sophisticated yet user-friendly tool tailored to facilitate exploration and enhance safety throughout the journey.
The "Explore Northern Ireland" script serves as a versatile and convenient tool tailored for anyone exploring Northern Ireland, be it tourists or residents. This script creates an interactive map of comprehensive information on tourist sites, nearest transportation hubs (including both bus and train stations), as well as the distances between these transportation hubs and tourist sites as popups. Moreover, it seamlessly integrates General Practitioner (GP) surgeries for emergency services, utilizing postal codes for easy searchability. By combining these features, the script enhances the overall travel experience, prioritizing safety, and preparedness throughout every stage of the journey.


.. raw:: html

    <iframe src="../_static/NI_tourist_MAP.html" height="500px" width="100%"></iframe>


Objectives:
~~~~~~~~~~~~
* **Interactive Map Creation**:Utilizing GeoDataFrame, the script generates an interactive map that visually presents tourist sites across Northern Ireland.
* **Tourist Site Information**:Detailed information about each tourist site is included on the map, aiding users in making informed decisions about their destinations.
* **Find nearest Transportation Hub**:The script identifies and displays the nearest transportation hubs, comprising both bus and train stations, in proximity to tourist sites, facilitating travel route planning and access to public transportation.
* **Find nearest GP Surgeries**:General Practitioner (GP) surgeries are integrated into the map, allowing users to locate emergency medical services easily. Postal codes are leveraged for efficient searchability, ensuring prompt access to medical assistance.
* **Distance Calculation**:Distances between transportation hubs/GP Surgeries and tourist sites are calculated and provided, enabling users to estimate travel times and plan itineraries effectively.

Expected Results:
~~~~~~~~~~~~~~~~~
Upon running the script, users will observe the following outcomes:

**Base Map with Counties and Outlines**: The function generates a base map of Northern Ireland featuring colored county boundaries overlaid with the country outline.
**Tourist Sites Overlay**: Tourist site polygons are overlaid onto the base map, facilitating visual identification of their locations. The color of each polygon corresponds to the county name, aiding in easy identification. Detailed information about each tourist site, such as its name, nearest transportation hubs, and distance, is conveniently accessible through pop-up windows. Moreover, the pop-ups specify the nearest GP surgery and its distance, cross-referenced with postal codes, enhancing user understanding.
**Coastal tourist Points Display**: Coastal spots data from a GeoJSON file is showcased on the map, potentially as markers. Pop-ups offer comprehensive details about each spot, including name, website URL, nearest transportation hubs, and distance. Moreover, the pop-ups highlight the nearest GP surgery, cross-referenced with postal codes, and its distance from each coastal spot.
**Interactive Features**: Additional data from a CSV/GeoJSON file enriches the map with attribute information about tourist sites, transportation hubs, and GP surgeries. Interactive elements such as pop-ups provide detailed insights when users hover over specific points of interest.
**Final Map Visualization**: Once all data is integrated and displayed, the function will return an interactive Folium map object that users can view in a web browser. This map will contain all the layers mentioned above, providing a comprehensive overview of tourist attractions, transportation hubs, GP surgeries,postal codes,distance values and coastal spots in Northern Ireland.
**Save as HTML**: The function may save the generated Folium map as an HTML file, allowing users to access it offline or embed it in web pages.

Data Provided
-------------
In the data_file folder,contains are as follows:

- ``NI_Outline.shp``, a shapefile comprising the Northern Ireland country outline.

- ``NI_Counties.shp``, a shapefile containing the boundaries of Northern Ireland's counties

- ``NI_Tourist_Sites.shp`` , a shapefile containing polygon data of Historical Parks and Gardens.

- ``NI_Coastal_spots.geojson``, a GeoJSON file containing information on Places to Visit in Causeway Coast and Glens.

- ``NI_PostCodes_GP.geojson``, a GeoJSON file contain GP surgery information with postal codes in Northern Ireland.

- ``NI_Tourist_trans_GP_Dist.csv``,a csv file with information about nearest Transport Hub and Nearest GP surgery informatio to “Tourist_Sites”.

The script  **Integrated_Data_Analysis.ipynb/ .py** outline the  process of ``Re-Projection``, ``Polygon Clipping``, and the creation of ``NI_Costal_spots.geojson`` file, ``NI_Costal_spots.geojson``, ``NI_PostCodes_GP.geojson`` and ``NI_Tourist_trans_GP_Dist.csv`` files. To execute the script,  ensure you download the specified files into the **data_files/download_data** folder. Remember to extract shapefiles from **.zip** archives before use.

- ``OSNI_Open_Data_-_Largescale_Boundaries_-_NI_Outline.shp``, A shapefile comprising the Northern Ireland country outline was obtained from `Data.gov.uk <https://www.data.gov.uk/dataset/738c0cac-d330-4ba9-a2a5-8956383fb4a9/osni-open-data-largescale-boundaries-ni-outline>`_ .

- ``OSNI_Open_Data_-_Largescale_Boundaries_-_County_Boundaries_.shp``, A shapefile containing the boundaries of Northern Ireland's counties was sourced from `OpenDataNI <https://admin.opendatani.gov.uk/dataset/osni-open-data-largescale-boundaries-county-boundaries>`_.

- ``historic-parks-and-gardens.shp`` , A shapefile containing polygon data of Historic Parks and Gardens(valid as of April 2024) was obtained from `OpenDataNI <https://admin.opendatani.gov.uk/dataset/historic-parks-and-gardens/resource/1f59b6a5-4f8d-4456-9009-e00586062b4d>`_.

- ``Places_to_Visit_in_Causeway_Coast_and_Glens.shp``, A shapefile file containing information on Places to Visit in Causeway Coast and Glens sourced from `OpenDataNI <https://admin.opendatani.gov.uk/dataset/places-to-visit-in-causeway-coast-and-glens>`_.

- ``translink-stations-ni.geojson``, a GeoJSON file containing the locations of all Bus and Rail stations in Northern Ireland, from `OpenDataNI <https://www.opendatani.gov.uk/@translink/translink-ni-railways-stations>`_.

- ``ukpostcodes.csv``, a csv file contain all postcodes in united Kingdom from `FreeMapTools <https://www.freemaptools.com/download-uk-postcode-lat-lng.htm#google_vignette>`_.

- ``gp-practice-reference-file---jan-2024.csv``, a csv file contain General Practitioner (GP) surgeries information (valid as of April 2024), from `OpenDataNI <https://www.opendatani.gov.uk/@business-services-organisation/gp-practice-list-sizes>`_.

**Important Note**: All datasets utilize the same Coordinate Reference System (`CRS <https://geopandas.org/en/stable/docs/user_guide/projections.html>`_) , specifically the EPSG code for WGS84 latitude/longitude (`EPSG:4326 <https://epsg.io/4326>`_). This consistency enables seamless integration of map data onto  ``folium.map``.

Setup
-----

**Getting Started**

1. Installation of Required Tools
~~~~~~~~~~~~~~~~~~
To begin the exercises, ensure you have both ``git`` and ``conda`` installed on your computer. Here's a concise guide for installing Git `Creating an account <https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github>`_ , `GitHub Desktop <https://docs.github.com/en/desktop/installing-and-authenticating-to-github-desktop/setting-up-github-desktop>`_ and `Anaconda <https://docs.anaconda.com/free/anaconda/install/windows/>`_.

2. Download/clone repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
After installing Git and Anaconda, proceed to **clone** this repository to your computer using one of the following methods:
1. **Forking this Repository** : `Sign-in <https://github.com/login>`_ to your created GitHub account and head to `sereneeosman/egm722_serenee <https://github.com/sereneeosman/egm722_serenee>`_ repository. Click on the ``Fork`` button located in the upper-right corner of the Window.This action duplicates the entire repository to your GitHub account.
2. **Cloning the repository** : Launch GitHub Desktop and navigate to **File** > **Clone Repository**. You'll find your forked version of the ``sereneeosman/egm722_serenee`` repository repository listed under the ``GitHub.com`` tab. Choose the repository and designate a local path where you want to save it (remember this path). Click on the "Clone" button. A new window will appear, showing the progress of downloading and unpacking files. Once completed, the repository will be set up on your local computer.
3. Another method to clone this repository is by clicking the green **"<> Code"** button on the GitHub repository page and selecting **"Download ZIP"** from the dropdown menu at the bottom. After downloading, unzip the file to your desired local path. Then, in GitHub Desktop, navigate to **File** > **Add Local Repository**. Although I don't recommend this approach, it can be useful in certain cases.

3. Create a conda Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Once you've successfully cloned the repository, you can proceed to create a ``conda`` environment. To do this, utilize the provided ``environment.yml`` file within the repository. If you're using Anaconda Navigator, you can import the environment by selecting **"Import"** from the Environments panel and navigating to the **.yml** file in the local repository path.

If you prefer, you can open a command prompt (on Windows, navigate to the "Anaconda Prompt"). Then, go to the directory where you cloned this repository and execute the following command:

.. code-block:: python

    C:\Users\sereneeosman\egm722_serenee> conda env create -f environment.yml

Setting up the ``conda`` environment might take some time, but this process only needs to be done once per repository.

4. Launch Jupyter Lab
~~~~~~~~~~~~~~~~~~~~~
In Anaconda Navigator, you can launch Jupyter Lab and navigate to the local folder where this repository is located. Ensure that your ``egm722_serenee`` environment is activated.
Alternatively, from the command line, start by opening Anaconda Prompt and navigating to the folder where you've cloned the repository. Activate your newly-created environment with

.. code-block:: python

    conda activate egm722_serenee

Then, execute the command

.. code-block:: python

    jupyter-lab

This action should open a web browser window, providing an overview of the current folder.

## 5. Repository Structure
~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ``NI_TouristMap.ipynb`` :This file contains the main code for creating a tourist map. It serves as the primary navigation point for executing the code related to the creation of the tourist map.
* ``Integrated_Data_Analysis.ipynb/.py`` :This file demonstrates how to integrate downloaded data and perform analysis on it. It provides insights into the process of combining different datasets and conducting analysis tasks, available both in Jupyter Notebook (.ipynb) and Python script (.py) formats.
* ``NI_Tourist_Map_doc.rst`` :  This file contain the complete Documentation of this code.

Getting Started
----------------
To get started, open Jupyter Notebook and begin working through the notebook titled "NI_TouristMap_edit.ipynb".
To execute the cell, highlight it by clicking on it, then either press **Ctrl + Enter** or click the triangular **play** button located at the top of this panel.

**Importing Libraries**

To get started, first import the required python libraries.
* ``os``: This library provides a way to interact with the operating system, such as managing files and directories.(`Documentation <https://docs.python.org/3/library/os.html>`_)
* ``pandas`` (aliased as **pd**): A powerful data manipulation library that allows you to work with structured data (e.g., data frames,Comma Separated Value (CSV) file).(`Documentation <https://pandas.pydata.org/>`_)
* ``geopandas`` (aliased as **gpd**): An extension of Pandas specifically designed for working with geospatial data (e.g., vector data).(`Documentation <https://geopandas.org/en/stable/>`_)
* ``folium``: A Python library for creating interactive maps.(`Documentation <https://python-visualization.github.io/folium/latest/>`_)


.. code-block:: python

    import os
    import pandas as pd
    import geopandas as gpd
    import folium

**Reading Geospatial Data**

The code utilizes GeoPandas' ``.read_file()`` function (`Documentation <https://geopandas.org/en/stable/docs/reference/api/geopandas.read_file.html>`_) to read geospatial data from shapefiles. When handling shapefiles, they are treated as **GeoDataFrame** (`Documentation <https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoDataFrame.html>`_ ), resembling attribute tables but with added geospatial functionalities.

A **GeoDataFrame** enhances a Pandas **DataFrame** (`Documentation <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html>`_) by integrating geospatial capabilities.
It stored geometry for each feature *points*, *lines*, *polygons*, along with associated attributes. With GeoDataFrames, users can conduct spatial operations and effectively visualize data on maps.

Initially, we'll read data for country outlines and counties to establish the foundation of our map.


.. code-block:: python

    # Read the shapefiles
    outline = gpd.read_file(os.path.abspath("data_files/NI_Outline.shp")) # Path to the input shapefile of Country Outline data
    counties = gpd.read_file(os.path.abspath("data_files/NI_Counties.shp")) # Path to the input shapefile of Counties data

**Create a Base map**

To generate an interactive map from **GeoDataFrames**, we utilize the ``.explore`` (`Documentation <https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoDataFrame.explore.html>`_) function  which generates a **folium.Map** (`Documentation <https://geopandas.org/en/stable/docs/user_guide/interactive_mapping.html>`_).
We assign the result to ``m = folium.Map`` (`Documentation <https://python-visualization.github.io/folium/latest/getting_started.html#Creating-a-map>`_), creating a base map.

We will utilize the "CountiesName" column to visualize the each polygon, and apply the **Set2** colormap from ``matplotlib`` to set the colors.More information about colormaps can be found `here <https://matplotlib.org/stable/users/explain/colors/colormaps.html>`_.
In this case, each county will be assigned a color based on its name.

.. code-block:: python

    # Create a Base Map on Counties name.
    m = counties.explore("CountyName", cmap = "Set2")

**Adding Country outline into Base folium map**

Next we will add country outline into the base map from read shapefile (``NI_Outline.shp``).

To do this we use ``folium.GeoJson()`` (`Documentation <https://python-visualization.github.io/folium/latest/user_guide/geojson/geojson.html>`_) function in the folium library.

GeoJSON is a format for encoding a variety of geographic data structures,JSON (JavaScript Object Notation) format. It's commonly used in web mapping applications and spatial databases to represent geographic features such as *points*, *lines*, *polygons*, or a set of coordinates.
This data defines the shape of an area on the map.

* ``*outline``: This is the GeoDataFrame containing the outline shape data.

* ``style_function=lambda feature`` (`Documentation <https://python-visualization.github.io/folium/latest/user_guide/geojson/geojson.html#Styling>`_)  : This is an argument passed to customize the style of the GeoJSON features. It's a ``lambda function`` that takes a feature as input and returns a dictionary specifying the style properties.

* ``"color": "black"``,  : This sets the color of the outline to black.

* ``"fillOpacity": 0`` : This sets the fill opacity of the outline to 0, meaning it will be transparent and won't fill the area inside the outline.

* ``name="outline"``  : This sets the name of the GeoJson layer to 'outline'. This name can be used to control the visibility of the layer in the folium map's layer control.

* ``.add_to(m)`` : This method adds the GeoJson layer to the base folium map (m).

.. code-block:: python

    # Add the outline with a black frame
    folium.GeoJson(
        outline, # outline shape data
        style_function=lambda feature: {  # customize the style of the GeoJSON features
            "color": "black",  # sets the color of the outline to black
            "fillOpacity": 0 # sets the fill opacity as transparent
        },
        name="outline" #name of the GeoJson layer
    ).add_to(m) #adds the GeoJson layer to the base folium map **m**.

If you encounter the result **<folium.features.GeoJson at 0x177bc95bb60>** without an error message, it signifies that the GeoJSON layer object has been successfully created and added to the map (m).

Display the base folium map

.. code-block:: python

    m

As depicted, a color legend is incorporated at the bottom right-hand corner of the map, providing information on the colors assigned to each polygon. Additionally, a scale is situated at the bottom left-hand corner of the map. The country outline of Northern Ireland is displayed with black border lines.You can zoom in or out to examine finer details, including those on the [OpenStreetMap](https://www.openstreetmap.org/#map=5/35.588/134.380) base layer.

**Convert DataFrame to GeoDataFrame**

Convert csv data to vector data

The ``pd.read_csv()`` (`Documentation <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html>`_) function is used to read data from a CSV (Comma-Separated Values) file into a Pandas **DataFrame**. The function reads the contents of the CSV file and creates a DataFrame with the data.
 
**DataFrame** (`Documentation <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html>`_) is a two-dimensional labeled data structure in Pandas. It organizes data into rows and columns, similar to a table. Each column in the DataFrame corresponds to a variable, and each row represents an observation.
 
We'll read the integrated CSV file containing tourist site names, details of the nearest transport hubs, and details of the nearest GP surgeries. Refer to the **Integrated_Data_Analysis.ipynb** file for instructions on how to create this csv file.

.. code-block:: python

    #read integrated csv file
    df = pd.read_csv("data_files/NI_Tourist_trans_GP_Dist.csv")

The ``.head()`` (`Documentation <https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html>`_) function is used to display the first few rows of the ``df``(a **DataFrame**). By default, it returns the first five rows, but you can specify the number of rows you want to display by passing an integer argument to the function (e.g., df.head(10) would display the first ten rows)

.. code-block:: python

    # Check the first few rows of df
    df.head()

Next, we'll open the base shapefile of "tourist sites," which includes polygon data.
The ``gpd.read_file`` (`Documentation <https://geopandas.org/en/stable/docs/reference/api/geopandas.read_file.html>`_) function, reads the shapefile and returns a **GeoDataFrame**.

.. code-block:: python

    # read tourist site polygon data
    tourist = gpd.read_file(os.path.abspath("data_files/NI_Tourist_Sites.shp")) # path to the tourist site shapefile data

The ``.columns``(`Documents <https://www.geeksforgeeks.org/python-pandas-dataframe-columns/>`_) function display name of the field head in attributes of the DataFrame object in pandas.
 
When you input ``tourist.columns``, it returns an index of column labels within the "tourist" **DataFrame**.

.. code-block:: python

    # Displaying the column names of the shapefile.
    tourist.columns

This code merges a GeoDataFrame and a DataFrame, namely **tourist** and **df**, based on a common column in each dataset.
 
* The ``.merge``(`Documentation <https://pandas.pydata.org/docs/reference/api/pandas.merge.html>`_) function provided attempts to merge the two datasets. Merge these datasets based on a common field (the "SITE"[tourist] and "Tourist Sites"[df] columns)
 
* The ``left_on`` parameter specifies the column name in the left dataset (**tourist_site**) to use for merging (in this case, "SITE").
 
* The ``right_on`` parameter specifies the column name in the right dataset (**df**) to use for merging (in this case, "Tourist Sites").
 
* The resulting ``merge_site`` DataFrame will contain combined rows from both datasets.
 
* The ``.head()`` method is then called on the merged DataFrame to display the first few rows.By default, it shows the first five rows, along with the column names.
 

.. code-block:: python

    #Merge the CSV data (DataFrame) with the shapefile data (GeoDataFrame) based on a common column.
    merge_site = tourist.merge(df, left_on="SITE", right_on= "Tourist Sites")
    merge_site.head()

This code creates a new GeoDataFrame named "visit_geo" by selecting specific columns from the previously merged DataFrame "merge_site".
 
* The first line of code selects specific columns from the merge_site DataFrame.  Selection of the **geometry** column is important as it contain the coordinates and feature types. The geometry column is necessary for the second command line to generate the GeoDataFrame.
* The second command ``.GeoDataFrame`` (`Documentation <https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoDataFrame.html>`_)   converts the **DataFrame** named "visit_filter" into a **GeoDataFrame**.
* The ``.head()`` function displays the first few rows  of the "visit_geo" GeoDataFrame.
 

.. code-block:: python

    # Create a new GeoDataFrame with specified columns
    # Check the Head of result
    visit_filter = merge_site[["Tourist Sites", "Near_T_Hub","Trans_Dist","Near_GP", "GP_Dist","PostCode","geometry"]]
    visit_geo = gpd.GeoDataFrame(visit_filter)
    visit_geo.head()

We will add county names into the "visit_geo" file, where geometries intersect.
 
The ``.sjoin`` (`Documentation <https://geopandas.org/en/stable/docs/reference/api/geopandas.sjoin.html>`_) function allows spatial join of the two GeoDataFrames (``gpd.sjoin(left_df, right_df, how='inner')``).

* ``left_df``: The left GeoDataFrame (in this case, "visit_geo")
* ``right_df``: The right GeoDataFrame (in this case, "counties")
* ``how:'inner'``: Retains only the rows where geometries intersect in both GeoDataFrames.
 

.. code-block:: python

    # Merge Two GeoDataFrames to attach county name
    visit_merge = gpd.sjoin(visit_geo,counties,how="inner")

To verify the results ``.head()`` function used to retrieve the first few rows (usually the top 5 rows) GeoDataFrame of "visit_merge". It provides a quick preview of the data contained within the GeoDataFrame.

.. code-block:: python

    # Check the Head 
    visit_merge.head()

You will see result GeoDatFrame contain both columns of the "Counties" file and "visit_geo" file.

The next code filters specific columns from the **GeoDataFrame**, constructs a new GeoDataFrame from the filtered data.
This process is commonly used to focus on relevant columns and convert tabular data with geometric information into a format suitable for spatial analysis.

Then displays the first few rows of the resulting GeoDataFrame ("visit_all").

.. code-block:: python

    # Re-filtered the merge file.
    visit_all = visit_merge[["Tourist Sites", "Near_T_Hub","Trans_Dist","Near_GP", "GP_Dist","PostCode","geometry","CountyName"]]
    visit_all.head()

Next we will display the GeoDataFrame on the folium map and popup the attribute information.

The ``.explore`` (`Documents <https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoDataFrame.explore.html>`_) function is used to visualize the polygons of tourist site (Named "visit_all") base on the County name.This implies that the symbology is categorized according to the **county name**, assigning a single color to each polygon belonging to a specific county.

* ``"CountyName"``: Specifies the column to be visualized.
* ``cmap = "gist_rainbow"`` : Assigning corresponding colors to each tourist site polygons base on the county name using ``matplotlib`` colormap library.The more about ``matplotlib`` library, defined "color map" (`Documents <https://matplotlib.org/stable/users/explain/colors/colormaps.html>`_).
* ``m=m``: Sets the base map m to be displayed. If ``m=None``, it prevents recursion errors.
* ``popup=True``: Enables popups to display additional information when interacting with the map.
* ``legend=False``: Disables the display of the legend on the map.

.. code-block:: python

    # Display Created GeoDataframe on the base Map
    visit_all.explore("CountyName", # show the CountyName column
                    cmap="gist_rainbow", # use the "hsv" colormap from matplotlib
                    m=m, # set the base folium.map
                    popup = True, #Show information as popup when curser move on to the polygon
                    legend = False, #Don`t display a separated legend.
    )

**Adding Coastline visit spots into Folium map**

The code reads a GeoJSON file named "NI_Coastal_spots.geojson" using the GeoPandas ``read_file`` (`Documents <https://geopandas.org/en/stable/docs/reference/api/geopandas.read_file.html>`_)function.

This GeoJSON file contains data about Places to Visit in Causeway Coast and Glens, including information about the nearest transport hub and its distance, nearest GP surgery details and distance, and additional data such as the URL for the website.
Refer to the **Integrated_Data_Analysis.ipynb** file for instructions on how to create the GeoJSON file.

.. code-block:: python

    # read geojason file
    coastalpt = gpd.read_file(os.path.abspath("data_files/NI_Coastal_spots.geojson"))

# Printing ``coastline.head()`` would display the first few rows of the GeoDataFrame "coastalpt".

.. code-block:: python

    coastalpt.head()

This code snippet defines a dictionary named coastline_args containing parameters for configuring the display of "coastalpt" ``markers`` (`Documents <https://python-visualization.github.io/folium/latest/getting_started.html#Adding-markers>`_) on a folium map.

* ``"m": m``: This parameter specifies the folium map (m) on which the coastline markers will be plotted. The value associated with this key is an existing folium map instance (m).
* ``"marker_type": "marker"``: This parameter specifies the type of marker to be used for the coastline. In this case, it's set to "marker", indicating standard point markers.
* ``"popup": True``: This parameter determines whether popups will be displayed when clicking on the markers. By setting it to True, popups will be enabled, allowing additional information to be shown when interacting with the markers.
* ``"legend"``: False: This parameter controls the display of a legend. Here, it's set to False, indicating that no legend will be shown for the markers.
* ``"marker_kwds": {...}``: This parameter provides additional keyword arguments for styling the markers. Arguments based on the ``folium.Map.Icon`` (`Documents <https://python-visualization.github.io/folium/latest/user_guide/ui_elements/icons.html>`_) . In this case, it contains a dictionary with the following settings: ``"icon"``: This sets the icon for the marker.
* ``folium.Icon(...)``: This specifies the style of the marker icon. Here, it's configured with a red color ``color="red"`` ("red") and a star icon ``icon="star"``("star") from the `Font Awesome icon <https://docs.fontawesome.com/apis/javascript/icon-library>`_ library ``prefix='fa'``("fa"). also you can customize your icon with `Bootstrap <https://icons.getbootstrap.com/>`_ icon library.


.. code-block:: python

    # Assign Marker Parameters
    coastalpt_args = {
        "m": m, # specifies the folium map (m)
        "marker_type": "marker", #specifies the type of marker
        "popup": True, #Show information as popup when curser move on to the polygon
        "legend": False, # Don`t display a separated legend.
        "marker_kwds": {"icon": folium.Icon(color="red", icon="star", prefix='fa')} #style of the marker icon display red color marker with star and refer FontAwesome icon Library
    
    }

Display the "coastalpt" Marker on the folium map

The ``.explore()`` visualizes the "coastalpt" GeoDataFrame on the folium map, using the specified parameters.The points are categorized based on the **"Name"** column, and the marker properties are set according to the ``coastalpt_args`` dictionary.


.. code-block:: python

    # Display the "coastalpt" Marker on the folium map with the customized marker dictionary
    coastalpt.explore ("Name", **coastalpt_args)


**Exporting Folium Map**

Save the created folium map (represented by the m object) as an HTML file.

The ``m.save`` (`Documentation <https://python-visualization.github.io/folium/latest/getting_started.html#Creating-a-map>`_) command is used to save the current state of a map (represented by the m object) as an HTML file named “NI_tourist_MAP.html”.
You can then open this HTML file in a web browser to view the interactive map.

.. code-block:: python

    # Export the Folium Map
    m.save("NI_tourist_MAP.html")

You have successfully generated the tourist map for Northern Ireland.

Troubleshooting
----------------
If you're encountering any issues or need assistance with troubleshooting, here are a few steps you can take:

* **Library Imports**: Ensure all the required libraries are installed in your Python environment. If not, you can install them using pip install library-name.
* **Check File Paths**: Ensure that all file paths provided in the script are correct and that the necessary shapefiles, CSV files, and GeoJSON files are available in the specified locations.
* **Verify Data Loading**: Double-check that the data loading functions (read_file, read_integrated_csv_file, read_tourist_site_polygon_data, read_geojson_file, etc.) are correctly reading the data into pandas DataFrames or GeoDataFrames.
* **Inspect Dataframes**: Utilize functions like check_dataframe_header, display_merged_dataframe_head, display_geodataframe_head, etc., to inspect the loaded dataframes and ensure that they contain the expected data.
* **Dependency Versions**: Ensure that the versions of the Python libraries (pandas, geopandas, folium) used in the code are compatible with each other. Sometimes, certain functionalities might have been deprecated or changed in newer versions of the libraries, leading to unexpected behavior.
* **Coordinate Reference System (CRS)**: Ensure that all your geospatial data is in the same CRS. If not, use the to_crs method to convert them to a common CRS.
* **Folium Map Display**: If the map is not displaying correctly, ensure that the Jupyter notebook or Python environment you’re using supports inline map display. Sometimes, running the script in a different environment (like JupyterLab or VSCode) can help.
* **Popup Information**: Make sure the column names passed to the popup parameter in the explore method match the actual column names in your GeoDataFrame.
* **Error Messages**: Pay close attention to any error messages you receive when running the script. They often provide valuable clues about what might be going wrong.
* **Saving the Map**: After saving the map as an HTML file, check the file in a web browser to ensure it displays correctly. If it doesn’t, there might be issues with the JavaScript rendering.
* **Debug Functions**: If any custom functions (e.g., create_visit_geodataframe, spatial_join_geodataframes, etc.) are not producing the desired output, try adding print statements or using a debugger to understand the behavior of the code within those functions.
* **Test Incrementally**: Test each section of your script incrementally to identify where any errors might be occurring. You can comment out sections of the script and run them separately to isolate the problem.
* **Handle Errors**: Ensure that error handling mechanisms are in place, such as try-except blocks, to catch and handle any exceptions that may arise during execution.
* **Consult Documentation**: Refer to the documentation of libraries like GeoPandas and Folium for guidance on correct usage of functions and methods.
* **Community Support**: If you're still facing issues, consider reaching out to relevant communities or forums like Stack Overflow, where you can receive assistance from other developers.


Reference
----------

[1.]	Robert, Demeter & Kővári, Attila. (2019). GENERATING TOURISM SPOTS FOR BUDAPEST URBAN AREA. Research Gate . Available at : `<https://www.researchgate.net/figure/Spatial-dataset-and-centers-of-clusters-Source-own-work_fig1_357458695>`_
[2.]	M.Breuss (2024), Python Folium:Create Web Maps From Your Data. Real Python. Available at : `<https://realpython.com/python-folium-web-maps-from-data/>`_
[3.]	Kriesch, L.(2024). Interactive choropleth maps with GeoPandas and Folium. Medium. Available at : `<https://medium.com/@lukas.kriesch/interactive-choropleth-maps-with-geopandas-and-folium-2c68e0d91e0e>`_
[4.]	Oakley, M. (2022) Using Leaflet and Folium to make interactive maps in Python. Earth Lab. Available at : `<https://www.earthdatascience.org/tutorials/introduction-to-leaflet-animated-maps/>`_ [Access date : 29/04/2024]
[5.]	Ajagbe, S.A. , Oladipupo, M.A. and Emmanuel, B. (2020). CRIME BELT MONITORING VIA DATA VISUALIZATION: A CASE STUDY OF FOLIUM. Research Gate .Available at : `<https://www.researchgate.net/publication/351661740_CRIME_BELT_MONITORING_VIA_DATA_VISUALIZATION_A_CASE_STUDY_OF_FOLIUM.>`_ [Access date : 29/04/2024]
[6.]	Camara, G., Camboim, S. and Bravo, J.V.M (2021). USING JUPYTER NOTEBOOKS FOR VIEWING AND ANALYSING GEOSPATIAL DATA: TWO EXAMPLES FOR EMOTIONAL MAPS AND EDUCATION DATA. Research Gate ,Available at : `<https://www.researchgate.net/publication/354027216_USING_JUPYTER_NOTEBOOKS_FOR_VIEWING_AND_ANALYSING_GEOSPATIAL_DATA_TWO_EXAMPLES_FOR_EMOTIONAL_MAPS_AND_EDUCATION_DATA>`_
[7.]	George, Sneha & Seles, Keirolona & Brindha, Duraipandi & Jebaseeli, Theena & Vemulapalli, Laya. (2023). Geopositional Data Analysis Using Clustering Techniques to Assist Occupants in a Specific City. 8. 10.3390/engproc2023059008. Research Gate Available at : `<(PDF) Geopositional Data Analysis Using Clustering Techniques to Assist Occupants in a Specific City (researchgate.net)>`_
[8.]	Palkovic, M. (2020). Creating an interactive map of wildfire data using Folium in Python. Medium. Available at : `<https://towardsdatascience.com/creating-an-interactive-map-of-wildfire-data-using-folium-in-python-7d6373b6334a>`_
[9.]	Pras, A. (2022). Creating interactive maps with Python, Folium, and some HTML. Medium. Available at : `<https://levelup.gitconnected.com/creating-interactive-maps-with-python-folium-and-some-html-f8ac716966f>`_
[10.]	Jawla, Akshay & Singh, Manjot & Hooda, Nishtha. (2020). Crime Forecasting using Folium. Test Engineering and Management. 82. 16235-16240. Research Gate. Available at : `<https://www.researchgate.net/publication/341776530_Crime_Forecasting_using_Folium>`_
[11.]	Cheng, J. (2018). Around the world with Anthony Bourdain — a Folium tutorial. Medium. Available at : `<https://towardsdatascience.com/around-the-world-with-anthony-bourdain-a-folium-tutorial-7e9ad63fb650>`_



import pdfkit

def convert_html_to_pdf(html_file, pdf_file):
    pdfkit.from_file(html_file, pdf_file)

if __name__ == "__main__":
    convert_html_to_pdf("NI_Tourist_Map_doc.html", "test.pdf")