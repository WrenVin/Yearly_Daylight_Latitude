import math
from operator import mod
import matplotlib.pyplot as plt
import numpy as np
from sympy import rad



fig = plt.figure()
plt.title("Hours of daylight throughout the year")
plt.xlabel('Days')
plt.ylabel('Hours of Daylight')
plt.ylim(0, 27)
plt.xlim(1, 365)
ax = fig.gca()


daylight_days = []

def Daylight(latitude,day):
    P = math.asin(0.39795 * math.cos(0.2163108 + 2 * math.atan(0.9671396 * math.tan(.00860 * (day - 186)))))
    pi = math.pi
    hm = (math.sin((0.8333 * pi / 180) + math.sin(latitude * pi / 180) * math.sin(P)) / (math.cos(latitude * pi / 180) * math.cos(P)))
    try:
        daylightamount = 24 - (24 / pi) * math.acos(hm)
    except:
        daylightamount = 0
    return daylightamount

x = np.array(range(365))

for i in x:
    daylight_days.append(Daylight(43, i))
    ax.plot(i, daylight_days[i], 'ro')
    #print(daylight_days[i], i)

plt.grid()
plt.show()