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


while True:
    daylight_days = []
    #fig = plt.plots(num='Yearly Daylight Chart')
    ax = plt.subplot()
    ax.set_xlabel('Month')
    ax.set_ylabel('Hours of Daylight per day')
    ax.set_title("Hours of daylight throughout the year")
    plt.ylim(0, 27)
    plt.xlim(0, 365)
    ax.set_yticks([0, 4, 8, 12, 16, 20, 24])
    plt.xticks([0, 30.42, 60.84, 91.26, 121.68, 152.1, 182.52, 212.94, 243.36, 273.78, 304.2, 334.62])
    ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'], ha='left')
    days = np.array(range(365))
    while True:
        lonorloc = input('If you would like to enter a longitude value, press 1. If you would like to enter a city, press 2:')
        if lonorloc == '2' or lonorloc =='1':
            lonorloc = int(lonorloc)
            break
        else:
            print('Please enter 1 or 2')
    if lonorloc == 1:
        while True:
            try:
                lon = input('Please enter the latitude of your choice:')
                lon = float(lon)
                break
            except:
                print('Please enter a valid latitude')
        plt.title("Hours of daylight throughout the year at {} lat".format(lon))
    elif lonorloc == 2:
        lon = None
        city = input('Please enter the city of your choice:')
        country = input('Please enter the state or country of your choice:')
        with open(path_to_dat, encoding='utf8') as f_obj:
            reader = csv.reader(f_obj)
            for line in reader:
                if line[1] == city:
                    if line[7] == country:
                        lon  = float(line[2])
                        plt.title("Hours of daylight throughout the year in {}, {} ({})".format(city, country, line[4]))
                    elif line[4] == country:
                        lon  = float(line[2])
                        plt.title("Hours of daylight throughout the year in {}, {}".format(city, country))


    def Daylight(latitude,day):
        P = math.asin(0.39795 * math.cos(0.2163108 + 2 * math.atan(0.9671396 * math.tan(.00860 * (day - 186)))))
        pi = math.pi
        hm = (math.sin((0.8333 * pi / 180) + math.sin(latitude * pi / 180) * math.sin(P)) / (math.cos(latitude * pi / 180) * math.cos(P)))
        try:
            daylightamount = 24 - (24 / pi) * math.acos(hm)
        except:
            if hm < 0:
                daylightamount = 0
            else:
                daylightamount = 24
        return daylightamount

    def coseq(daylight_days):
        height = round(sum(daylight_days)/len(daylight_days), 2)
        coscoef = round(height-daylight_days[182], 2)
        cosequation = 'f(x) = {}cos(2π/365 x)+{}'.format(coscoef, height)
        print(cosequation)
        return cosequation

    try:
        for i in days:
            daylight_days.append(Daylight(lon, i))
            line = ax.plot(i, daylight_days[i], marker='.', color='red')
        cursor = mplcursors.cursor(ax)
        cursor.connect('add', lambda sel: sel.annotation.set_text('{} hours of daylight on {} {}'.format(round(sel.target[1], 3), month_name[(date(2022, 1, 1) + timedelta(sel.target[0] - 1)).month],  (date(2022, 1, 1) + timedelta(sel.target[0] - 1)).day)))
        plt.legend(line, [coseq(daylight_days)], loc='upper left')
        plt.grid()
        plt.show()
    except:
        print('Location does not exist')

    
