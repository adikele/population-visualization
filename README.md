# population-visualization
Plots of population data

PROBLEM STATEMENT: When describing and comparing population growth
in countries, it is useful to see the data as plots.
This project will provide different visualization aids, beginning
with a line graph, to plot population data of user-entered countries.

PROGRAM DESCRIPTION:
Program file: one_country_plot.py
Program plots the population of a user-entered country during a specific
range of years (2013 - 2018), by using a population tracker website's APIs:
http://api.population.io
The project uses Bokeh library for the plots.The documentation for Bokeh 
can be found here: https://bokeh.pydata.org/en/latest/

Program file: one_country_plot_v2.py
Revised version of one_country_plot.py with improved user-entry validation 

HOW TO RUN THE PROGRAM:
To run the file one_country_plot_v2.py
1. This program uses python 3.7, which must be installed. 
Save this python program file and also install the 
accompanying dependencies.
The dependencies are: (i) json (ii) requests (iii) bokeh.
2. Run the file one_country_plot.py from an IDE. 
3. Program asks the user to input name of a country.
Example of a country name:
India
Program should run and display the plot in a broswer.
Screenshot of a sample output is in the project folder. 

REQUIRED CONDITIONS:
1. Program requires Internet to access api.population.io site.

LIMITATIONS:
1. Program runs for most countries but not all, as http://api.population.io
does not host data for all countries. The list of countries for which data
is available is given here: http://api.population.io/#!/countries/listCountries
