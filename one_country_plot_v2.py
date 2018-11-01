#file name: one_country_plot_v2.py
import json
import requests
from bokeh.plotting import figure, output_file, show

'''
17.10.18 Working! 
TESTS:
1. Tested for different countries. (seems ok)
2. Now tested for ASIA --- negative data ??? and why is it showing e+240 ??

PROBLEM STATEMENT: Plot the population of a user-entered country.

PROGRAM DESCRIPTION:
Program plots the population of a user-entered country during a specific
range of years (2013 - 2018), by getting data from http://api.population.io
and using Bokeh library for the plot.

HOW TO RUN THE PROGRAM:
This program uses python 3.7 
Save this python program file and the accompanying dependencies.
The dependencies are: (i) json (ii) requests (iii) bokeh
Run this file from an IDE. Program asks user to input name of a country.
Example of a country name:
India
Program should run and display the plot in a broswer.

REQUIRED CONDITIONS:
1. Program requires Internet to access api.population.io site

OVERCOMING SHORTCOMINGS OF FILE one_country_plot.py:
1. In the previous version of this program, file one_country_plot.py:
For a user-entered country name input to be valid,
the name had to start with a capital letter and the rest of the name
had to be in small letters.
In this file one_country_plot_v2.py:
Country name can be entered in any combination of capital and small letters.

2. In the previous version of this program, file one_country_plot.py:
If a user-entered country name did not match the country names
from the website's collection, program would stop running.
In this file one_country_plot_v2.py: If a user-entered country name does not match the country names from the
website's collection, the user is prompted to enter another country name.
'''

API_ADDRESS = "http://api.population.io:80/1.0/countries"

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
    name_country = name_country.title()  #new
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
    name_country = input("Enter country name: ")
    return name_country
    

def input_validataion(name_country):
    '''Function takes a name_country, a string.
    It queries the population api to check if name_country exists in database
    Function returns true if name_country exists, false otherwise
    '''
    #print (name_country)  #CHECK
    api_address = API_ADDRESS
    response = requests.get(api_address)
    response_py = response.json()
    # print (response_str) #prints a dict with the countries as a list as expected
    list9 = response_py.values() # list9 is a list of list of countries (NOTE!!)
    list9useful = []
    for i in list9:
        for j in i:
            list9useful.append(j.upper())
    if name_country.upper() in list9useful:
        return True
    else:
        return False
    
def main():
    duration = 6
    while (1):
        country = read_input()
        if input_validataion(country):
            data = get_pop_data(duration, country)
            break;
        else:
            print("Country name not in database")
            print("-----------------------------")
    plot_data(data, country, 6)


main()
