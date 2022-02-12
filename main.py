import math
from operator import mod
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
    plt.title("Hours of daylight throughout the year")
    plt.xlabel('Days')
    plt.ylabel('Hours of Daylight per day')
    plt.ylim(0, 25)
    plt.xlim(1, 365)
    ax = plt.subplot(name='Yearly Daylight Chart')
    x = np.array(range(365))
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
                lon = input('Please enter the longitude of your choice:')
                lon = float(lon)
                break
            except:
                print('Please enter a valid longitude')
        plt.title("Hours of daylight throughout the year at {} lon".format(lon))
    elif lonorloc == 2:
        lon = None
        city = input('Please enter the city of your choice:')
        country = input('Please enter the state or country of your choice:')
        with open(path_to_dat, encoding='utf8') as f_obj:
            reader = csv.reader(f_obj)
            for line in reader:
                if line[0] == city:
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

    try:
        for i in x:
            daylight_days.append(Daylight(lon, i))
            ax.plot(i, daylight_days[i], marker='.', color='red')
            #print(daylight_days[i], i)
        cursor = mplcursors.cursor(ax)
        cursor.connect('add', lambda sel: sel.annotation.set_text('{} hours of daylight on {} {}'.format(round(sel.target[1], 3), month_name[(date(2022, 1, 1) + timedelta(sel.target[0] - 1)).month],  (date(2022, 1, 1) + timedelta(sel.target[0] - 1)).day)))
        plt.grid()
        plt.show()
    except:
        print('Location does not exist')
