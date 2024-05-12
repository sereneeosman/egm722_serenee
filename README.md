# egm722_serenee
# Northern Ireland Tourist Map with Folium
# Explore Northern Ireland: Tourist Map with Intergrated Transportation Hubs, and GP Surgeries.
Northern Ireland boasts a rich tapestry of history, culture, and natural beauty, attracting visitors from around the globe. However, navigating its diverse landscapes and accessing essential services can be daunting, especially for newcomers. Recognizing this challenge, I introduced the "Explore Northern Ireland" script, a sophisticated yet user-friendly tool tailored to facilitate exploration and enhance safety throughout the journey.
The "Explore Northern Ireland" script serves as a versatile and convenient tool tailored for anyone exploring Northern Ireland, be it tourists or residents. This script creates an interactive map of comprehensive information on tourist sites, nearest transportation hubs (including both bus and train stations), as well as the distances between these transportation hubs and tourist sites as popups. Moreover, it seamlessly integrates General Practitioner (GP) surgeries for emergency services, utilizing postal codes for easy searchability. By combining these features, the script enhances the overall travel experience, prioritizing safety, and preparedness throughout every stage of the journey.


## Getting Started

### 1. Installation of Required Tools
To begin the exercises, ensure you have both `git` and `conda` installed on your computer. Here's a concise guide for installing Git[Creating an account](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github) , [GitHub Desktop](https://docs.github.com/en/desktop/installing-and-authenticating-to-github-desktop/setting-up-github-desktop)and Anaconda[Document](https://docs.anaconda.com/free/anaconda/install/windows/).

### 2. Download/clone repository

After installing Git and Anaconda, proceed to __clone__ this repository to your computer using one of the following methods:
1. __Forking this Repository__ : [Sign-in](https://github.com/login) to your created GitHub account and head to [sereneeosman/egm722_serenee](https://github.com/sereneeosman/egm722_serenee) repository. Click on the `Fork` button located in the upper-right corner of the Window.This action duplicates the entire repository to your GitHub account.
2. __Cloning the repository__ : Launch GitHub Desktop and navigate to __File__ > __Clone Repository__. You'll find your forked version of the `sereneeosman/egm722_serenee` repository repository listed under the `GitHub.com` tab. Choose the repository and designate a local path where you want to save it (remember this path). Click on the "Clone" button. A new window will appear, showing the progress of downloading and unpacking files. Once completed, the repository will be set up on your local computer.
3. Another method to clone this repository is by clicking the green __"<> Code"__ button on the GitHub repository page and selecting __"Download ZIP"__ from the dropdown menu at the bottom. After downloading, unzip the file to your desired local path. Then, in GitHub Desktop, navigate to __File__ > __Add Local Repository__. Although I don't recommend this approach, it can be useful in certain cases.

### 3. Create a conda Environment
Once you've successfully cloned the repository, you can proceed to create a `conda` environment. To do this, utilize the provided `environment.yml` file within the repository. If you're using Anaconda Navigator, you can import the environment by selecting __"Import"__ from the Environments panel and navigating to the __.yml__ file in the local repository path.

If you prefer, you can open a command prompt (on Windows, navigate to the "Anaconda Prompt"). Then, go to the directory where you cloned this repository and execute the following command:
```
C:\Users\sereneeosman\egm722_serenee> conda env create -f environment.yml
```
Setting up the conda environment might take some time, but this process only needs to be done once per repository.

### 4. Launch Jupyter Lab
In Anaconda Navigator, you can launch Jupyter Lab and navigate to the local folder where this repository is located. Ensure that your egm722_serenee environment is activated.
Alternatively, from the command line, start by opening Anaconda Prompt and navigating to the folder where you've cloned the repository. Activate your newly-created environment with 

``` 
conda activate egm722_serenee
```
Then, execute the command 
```
jupyter-lab
``` 
This action should open a web browser window, providing an overview of the current folder.

### 5. Repository Structure


* ``NI_TouristMap.ipynb`` :This file contains the main code for creating a tourist map. It serves as the primary navigation point for executing the code related to the creation of the tourist map.
* ``Integrated_Data_Analysis.ipynb/.py`` :This file demonstrates how to integrate downloaded data and perform analysis on it. It provides insights into the process of combining different datasets and conducting analysis tasks, available both in Jupyter Notebook (.ipynb) and Python script (.py) formats.
* ``NI_Tourist_Map_doc.rst`` :  This file contain the complete Documentation of this code.
* ``NI_TouristMap_numpy.py`` : document containing documentation formatted in NumPy docstring style.

















