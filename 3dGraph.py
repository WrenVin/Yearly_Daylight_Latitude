import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import quad 
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import FillBetween3d
import numpy as np
import matplotlib.tri as mtri
from stl import mesh


daylightamount = []
fig = plt.figure()
ax = Axes3D(fig, xlim=(0, 365), ylim=(0, 27), zlim=(-90, 90))
ax.set_xlabel('Month')
ax.set_ylabel('Hours of Daylight per day')
ax.set_zlabel('Latitude')
ax.set_title("Hours of daylight throughout the year")
ax.set_yticks([0, 4, 8, 12, 16, 20, 24])
ax.set_zticks([-90, -60, -45, -30, 0, 30, 45, 60, 90])
plt.xticks([0, 30.42, 60.84, 91.26, 121.68, 152.1, 182.52, 212.94, 243.36, 273.78, 304.2, 334.62])
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'], ha='left')
line, = ax.plot([], [], lw=2)
lat = np.linspace(-90., 90., 180)
days = range(0, 366)
y=[]
def init():
    line.set_data([], [])
    return line,

def CalcVal(latitude, day=365):
    result = None
    P = math.asin(0.39795 * math.cos(0.2163108 + 2 * math.atan(0.9671396 * math.tan(.00860 * (day - 186)))))
    pi = math.pi
    hm = (math.sin((0.8333 * pi / 180) + math.sin(latitude * pi / 180) * math.sin(P)) / (math.cos(latitude * pi / 180) * math.cos(P)))
    try:
        result = (24 - (24 / pi) * math.acos(hm))
    except:
        if hm < 0:
            result = 0
        else:
            result = 24
    return result

def Daylight(latitude):
    daylightamount.clear()
    result = None
    for day in days:
            result = CalcVal(latitude, day=day)
            daylightamount.append(result)
    return daylightamount
    
for i in lat:
    ax.collections.clear()
    x=days
    y = (Daylight(i)) 
    #ax.add_collection3d(plt.fill_between(x,y,color='orange', alpha=0.3,label="filled plot"),zs=i, zdir='z')
    line= ax.plot(x, y, i,  zdir='z')
    #plt.legend(['Latitude: {} degrees'.format(i)], loc='upper left')
    

plt.show()

    
