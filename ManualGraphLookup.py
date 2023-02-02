import math
from operator import mod
from matplotlib import offsetbox
import matplotlib.pyplot as plt
import numpy as np
from sympy import rad
import csv
import mplcursors
from datetime import datetime, date, timedelta
from calendar import month_name
from os import path
bundle_dir = path.abspath(path.dirname(__file__))
path_to_dat = path.join(bundle_dir, 'worldcities.csv')

# This code will generate a chart of the amount of daylight per day throughout the year, given a latitude.
while True:
    # Create an empty list to store the amount of daylight per day.
    daylight_days = []
    # Set up the plot.
    ax = plt.subplot()
    ax.set_xlabel('Month')
    ax.set_ylabel('Hours of Daylight per day')
    ax.set_title("Hours of daylight throughout the year")
    plt.ylim(0, 27)
    plt.xlim(0, 365)
    ax.set_yticks([0, 4, 8, 12, 16, 20, 24])
    plt.xticks([0, 30.42, 60.84, 91.26, 121.68, 152.1, 182.52, 212.94, 243.36, 273.78, 304.2, 334.62])
    ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'], ha='left')
    # Create an array of the days in a year.
    days = np.array(range(365))
    # Prompt the user to enter either a latitude or a city name.
    while True:
        lonorloc = input('If you would like to enter a latitude value, press 1. If you would like to enter a city, press 2:')
        if lonorloc == '2' or lonorloc =='1':
            lonorloc = int(lonorloc)
            break
        else:
            print('Please enter 1 or 2')
    # If the user enters a latitude, prompt them to enter the value.
    if lonorloc == 1:
        while True:
            try:
                lon = input('Please enter the latitude of your choice:')
                lon = float(lon)
                break
            except:
                print('Please enter a valid latitude')
        # Update the plot title to include the latitude.
        plt.title("Hours of daylight throughout the year at {} lat".format(lon))
    # If the user enters a city, prompt them to enter the city and the country.
    elif lonorloc == 2:
        lon = None
        city = input('Please enter the city of your choice:')
        country = input('Please enter the state or country of your choice:')
        # Read the data from the csv file.
        with open(path_to_dat, encoding='utf8') as f_obj:
            reader = csv.reader(f_obj)
            # Find the matching city and country in the csv file.
            for line in reader:
                if line[1] == city:
                    # If the country is a state, include it in the plot title.
                    if line[7] == country:
                        lon  = float(line[2])
                        plt.title("Hours of daylight throughout the year in {}, {} ({})".format(city, country, line[4]))
                    # If the country is a country, do not include the state in the plot title.
                    elif line[4] == country:
                        lon  = float(line[2])
                        plt.title("Hours of daylight throughout the year in {}, {}".format(city, country))


    # Define a function that calculates the amount of daylight per day at a given latitude.
    def Daylight(latitude,day):
        P = math.asin(0.39795 * math.cos(0.2163108 + 2 * math.atan(0.9671396 * math.tan(.00860 * (day - 186)))))
        pi = math.pi
        hm = (math.sin((0.8333 * pi / 180) + math.sin(latitude * pi / 180) * math.sin(P)) / (math.cos(latitude * pi / 180) * math.cos(P)))
        # Handle cases where hm is outside the range of the acos function.
        try:
            daylightamount = 24 - (24 / pi) * math.acos(hm)
        except:
            if hm < 0:
                daylightamount = 0
            else:
                daylightamount = 24
        return daylightamount

    # Define a function that calculates the cosine equation of the data points.
    def coseq(daylight_days):
        height = round(sum(daylight_days)/len(daylight_days), 2)
        coscoef = round(height-daylight_days[182], 2)
        cosequation = 'f(x) = {}cos(2π/365 x)+{}'.format(coscoef, height)
        print(cosequation)
        return cosequation

    # Calculate the amount of daylight per day for each day in the array and plot it.
    try:
        for i in days:
            daylight_days.append(Daylight(lon, i))
            line = ax.plot(i, daylight_days[i], marker='.', color='red')
        # Add a cursor to the plot.
        cursor = mplcursors.cursor(ax)
        # Set the text of the cursor to the amount of daylight on the day it is hovering over.
        cursor.connect('add', lambda sel: sel.annotation.set_text('{} hours of daylight on {} {}'.format(round(sel.target[1], 3), month_name[(date(2022, 1, 1) + timedelta(sel.target[0] - 1)).month],  (date(2022, 1, 1) + timedelta(sel.target[0] - 1)).day)))
        # Add the cosine equation to the legend.
        plt.legend(line, [coseq(daylight_days)], loc='upper left')
        # Add a grid to the plot.
        plt.grid()
        # Show the plot.
        plt.show()
    # If the location does not exist, alert the user.
    except:
        print('Location does not exist')