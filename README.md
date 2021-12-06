# MultiKitPainting
A project to produce DNA Painter input files using multiple kits as input

Currently working for MyHeritage kits. 

# INSTRUCTIONS

This assumes you have python installed and know how to install modules

Create a folder for the input files and put your segment match files from MyHeritage in there
Create and output folder to holder the csv output file

Edit the config.py file and set the following entries:

Add the names of the siblings in the sibling list array. These should be the names as found in MyHeritage and used in the filenames of the segment file
SIBLING_LIST = ['name of first sibling', 'name of second sibling', 'name of third sibling']

For any other matches where you know their side you can put them into the 
BOTH_LIST --- for people who are on both maternal and paternal sides
MATERNAL_LIST --- for Maternal matches
PATERNAL_LIST --- for Paternal matches

Fill out the INPUT_FOLDER and OUTPUT_FOLDER with the paths to the folders containing your input files and where you want your output file to be written

Thes should either be absolute or be relative from where you are running the scripts. 

# PYTHON MODULES

The following python modules are used. Use 'pip install module' to get the version on your system

os
glob
pandas
numpy


# IMPORTING INTO DNAPAINTER

When complete the output file can be imported into DNAPainter. 

Choose import segment data and change the "Exclude larger matches sharing over xxxx cM in total" to 5000 so that all the siblings will be imported. 

Adjust the rest as required but remember that you are bringing in multiple kits so you are probably going to have multiple times the number of segments as with a single kit so be sensible about the lower bounds. 

Let me know on Facebook  about any issues you have. 



