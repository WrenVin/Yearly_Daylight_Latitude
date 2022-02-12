from math import *
from operator import mod
import matplotlib.pyplot as plt
import numpy as np
from sympy import rad
from datetime import date, datetime
import datetime as dt


fig = plt.figure()
plt.title("Hours of daylight throughout the year")
plt.xlabel('Days')
plt.ylabel('Hours of Daylight')
plt.ylim(0, 27)
plt.xlim(1, 30)
ax = fig.gca()


daylight_days = []

def Daylight(latitude,day):
    msdate = date(2022, 1, day).toordinal()-693594
    julianday = msdate+2415018.5
    juliancentury = (julianday-2451545)/36525
    GeomMeanLongSun = mod((280.46646+juliancentury*(36000.76983+juliancentury*0.0003032)),360)
    GeomMeanAnomSun = 357.52911+juliancentury*(35999.05029-0.0001537*juliancentury)
    SunEqofCtr = sin(radians(GeomMeanAnomSun))*(1.914602-juliancentury*(0.004817+0.000014*juliancentury))+sin(radians(2*GeomMeanAnomSun))*(0.019993-0.000101*juliancentury)+sin(radians(3*GeomMeanAnomSun))*0.000289
    MeanObliqEcliptic = 23+(26+((21.448-juliancentury*(46.815+juliancentury*(0.00059-juliancentury*0.001813))))/60)/60
    SunTrueLong = GeomMeanLongSun+SunEqofCtr
    SunAppLong = SunTrueLong-0.00569-0.00478*sin(radians(125.04-1934.136*juliancentury))
    obliqcorr = MeanObliqEcliptic+0.00256*cos(radians(125.04-1934.136*juliancentury))
    SunDec = degrees(asin(radians(obliqcorr))*sin(radians(SunAppLong)))
    HASunrise = degrees(acos(cos(radians(90.883))//(cos(radians(latitude))*cos(radians(SunDec)))-tan(radians(latitude))*tan(radians(SunDec))))
    sunlightduration = 8*HASunrise
    print(sunlightduration)
    return sunlightduration

x = np.array(range(1, 29))

for i in x:
    daylight_days.append(Daylight(70, i))
    ax.plot(i, daylight_days[i], 'ro')
    print(daylight_days[i], i)

plt.grid()
plt.show()