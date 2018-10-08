import json
import requests
from bokeh.plotting import figure, output_file, show

'''
8.10.18 Working! 
TESTS:
1. Tested for different countries. (seems ok)
2. WRONG RESULTS: for ASIA --- negative data ??? and why is it showing e+240 ???

PROBLEM STATEMENT: Plot the population of a user-entered country.

PROGRAM DESCRIPTION:
Program plots the population of a user-entered country during a specific
range of years (2013 - 2018), by getting data from http://api.population.io
and using Bokeh library for the plot.

HOW TO RUN THE PROGRAM:
This program used python 3.7 
Save this python program file and the accompanying dependencies.
The dependencies are: (i) json (ii) requests (iii) bokeh
Run this file from an IDE. Program asks user to input name of a country.
Enter name beginning with a capital letter and press enter.
Example of a country name:
India
Program should run and display the plot in a browser.

REQUIRED CONDITIONS:
1. Program requires Internet to access api.population.io site

LIMITATIONS:
1. Program runs for most countries but not all, as http://api.population.io
does not host data for all countries. The list of countries for which data
is available is given here: http://api.population.io/#!/countries/listCountries
'''

def get_pop_data(num_years, name_country):
    ''' this function takes as parameters:
    (i) an integer num_years, ie duration of years for desired data,
    (ii) a string name_country, ie country of interest
    Function queries the population API for total population of name_country
    for num_years years starting from 2013
    Function returns a list of two lists:
    (i) one list containing the dates for which the population data is taken
    (ii) the other list containing the total population for the dates in (i)
    '''
    duration = num_years
    time = []
    population = []
    api_address = "http://api.population.io:80/1.0/population/country/20zz-09-30/"
    api_address = api_address.replace("country", "%s" % name_country)
    for i in range(duration):
        new = 13+i  # population data  available only from 2013
        api_address_new = api_address.replace("zz", "%d" % new)
        response = requests.get(api_address_new)
        response_str = response.json()
        time.append(response_str["total_population"]["date"])
        population.append(response_str["total_population"]["population"])
    pop_data = []  # pop_data is a list of 2 lists
    pop_data.append(time)
    pop_data.append(population)
    return pop_data


def plot_data(data, name_country, duration):
    ''' this function takes as parameters:
    (i) data, a list of 2 lists, first for date, second for total population
    (ii) a string name_country, ie country of interest
    (iii) duration, number of years of for which 'data' is taken
    Function plots total population versus year for which population is
    recorded
    '''
    output_file("lines.html")
    p = figure(title="Popuation growth for 2013-2018", x_axis_label="time",
               y_axis_label="population")
    data_yrs = []
    for i in range(duration):
        data_yrs.append(int(data[0][i][0:4]))
    display = "Population data for {0}".format(name_country)
    p.line(data_yrs, data[1], legend=display, line_width=1)
    show(p)


def read_input():
    print("Program plots the population of a user-entered country")
    print("Population plot is displayed in a browser for the years 2013 - 2018")
    print("------------------------------------------------------") 
    print("At the prompt below, enter name of a country and press enter.")
    print("NOTE: Country name should begin with a capital letter. Eg: India")
    name_country = input("Enter country name: ")
    return name_country


def main():
    duration = 6
    country = read_input()
    data = get_pop_data(duration, country)
    plot_data(data, country, 6)


main()
