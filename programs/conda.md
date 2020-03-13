# Conda

> Source: http://conda.pydata.org/docs/index.html

> Aliases: anaconda

$ Managing Conda
    `conda info                    {{Verify if conda is installed, check version #}} 
    `conda update conda            {{Update conda package and environment manager to current version}} 
    `conda update anaconda         {{Update the anaconda meta package}} 

$ Managing Python
    `conda search -f python        {{Check versions of python available to install}} 
    `conda create -n snakes python=3.4
>                                  {{Install different version of Python in new environment}} 
    `source activate snakes        {{Switch to the new environment that has a different version of Python}} 

$ Managing Configuration
    `conda config --get            {{Get all keys and values from .condarc file}} 
    `conda config --get channels   {{Get value of the key channel from .condarc file}} 
    `conda config --add channels pandas
>                                  {{Add a new value to channel so conda looks for packages in this location}} 

$ Managing Packages
    `conda list                    {{View list of packages and versions installed in the active environment}} 
    `conda search beautiful-soup   {{Search for a package to see if it is available in conda to install}} 
    `conda install -n bunnies beautiful-soup
>                                  {{Install a new package}} 
    `conda update beautiful-soup   {{Update a package in the current environment}} 

$ Removing Packages
    `conda remove --name bunnies beautiful-soup
>                                  {{Remove one package from any named environment}} 
    `conda remove beautiful-soup   {{Remove one package from the active environment}} 

