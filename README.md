# MGRS-to-Lat-Lon

**Aim**

This package aims to convert latitudes and longitudes read from an MGRS grid map into standard geographical coordinate [Latitude, Longitude] in python.

**How to use**

Download this package and import the main class.

A .csv file with a table including columns "Latitude" and "Longitude" are required. These "Latitude" and "Longitude" values refer to the values read off from the map.

Initialise the main class with the .csv file. Eg: The file name is Test.csv, enter main('Test.csv').

To create a new csv with columns added at the end including the standard geographical coordinates, do main('Test.csv').run_whole_thing().

A new file will be created in the 'output' folder.

**Packages used**

pandas - to read and write .csv
datetime - to configure output file name
mgrs - to convert mgrs coordinates into latitude and longitude

**Credits**
Wei Loon
Min Jee
Wei Han