import math
from operator import mod
import matplotlib.pyplot as plt
import numpy as np
from sympy import rad
import csv


fig = plt.figure()
plt.title("Hours of daylight throughout the year")
plt.xlabel('Days')
plt.ylabel('Hours of Daylight')
plt.ylim(0, 25)
plt.xlim(1, 365)
ax = fig.gca()
x = np.array(range(365))
daylight_days = []

lonorloc = input('If you would like to enter a longitude value, press 1. If you would like to enter a city, press 2:')
lonorloc = int(lonorloc)
if lonorloc == 1:
    lon = input('Please enter the longitude of your choice:')
    lon = float(lon)
    plt.title("Hours of daylight throughout the year at {} lon".format(lon))
elif lonorloc == 2:
    city = input('Please enter the city of your choice:')
    country = input('Please enter the country of your choice:')
    with open("worldcities.csv", encoding='utf8') as f_obj:
        reader = csv.reader(f_obj)
        for line in reader:
            if line[0] == city:
                if line[4] == country:
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
        ax.plot(i, daylight_days[i], 'ro')
        #print(daylight_days[i], i)
        plt.grid()
        plt.show()
except:
    print('Location does not exist')
