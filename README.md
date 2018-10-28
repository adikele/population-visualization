# population-visualization
Plots of population data

PROBLEM STATEMENT: When describing and comparing population growth
in countries, it is useful to see the data as plots.
This project will provide different visualization aids, beginning
with a line graph, to plot population data of user-entered countries.

PROGRAM DESCRIPTION:
-- Program file: one_country_plot.py
Program plots the population of a user-entered country during a specific
range of years (2013 - 2018), by using a population tracker website's APIs:
http://api.population.io
The project uses Bokeh library for the plots.The documentation for Bokeh 
can be found here: https://bokeh.pydata.org/en/latest/

-- Program file: one_country_plot_v2.py
Revised version of one_country_plot.py with improved user-entry validation 

-- Program file: population_plot_2countries.ipynb
New features compared to one_country_plot.py
(i) improved user-entry validation and 
(ii) user can now enter two countries 

HOW TO RUN THE ABOVE PROGRAMS:
The program files use python 3.7, which must be installed. 
Save the python program files and also install the 
accompanying dependencies.
The dependencies are: (i) json (ii) requests (iii) bokeh.

-- To run the file one_country_plot_v2.py and one_country_plot.py
Run the files from an IDE. 
Program asks the user to input name of a country.
When program runs successfully, it displays the plot in a broswer.
Screenshot of a sample output is in the project folder. 

-- To run the file population_plot_2countries.ipynb
Run the file  population_plot_2countries.ipynb from Jupyter notebook IDE. 
Program asks user to input names of two countries.
If user entered country is not valid, that is, if country name is
not found in the database, user is asked to enter another name.
When program runs successfully, it displays the plot in a browser.
Screenshot of a sample output is in the project folder. 

REQUIRED CONDITIONS:
1. Program requires Internet to access api.population.io site.

LIMITATIONS:
1. Program runs for most countries but not all, as http://api.population.io
does not host data for all countries. The list of countries for which data
is available is given here: http://api.population.io/#!/countries/listCountries
