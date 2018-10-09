# population-visualization
Plots of population data

PROBLEM STATEMENT: When describing and comparing population growth
in countries, it is useful to see the data as plots.
This project will provide different visualization aids, beginning
with a line graph, to plot population data of user-entered countries.

PROGRAM DESCRIPTION:
Program file #1: one_country_plot.py
Program plots the population of a user-entered country during a specific
range of years (2013 - 2018), by using a population tracker website's APIs:
http://api.population.io
The project alse uses Bokeh library for the plots.

HOW TO RUN THE PROGRAM:
This program uses python 3.7 
Save this python program file and the accompanying dependencies.
The dependencies are: (i) json (ii) requests (iii) bokeh.
Run the file one_country_plot.py from an IDE. 
Program asks user to input name of a country.
Enter name beginning with a capital letter and press enter.
Example of a country name:
India
Program should run and display the plot in a broswer.

REQUIRED CONDITIONS:
1. Program requires Internet to access api.population.io site.

LIMITATIONS:
1. Program runs for most countries but not all, as http://api.population.io
does not host data for all countries. The list of countries for which data
is available is given here: http://api.population.io/#!/countries/listCountries
