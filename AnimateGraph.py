import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import quad 

daylightamount = []
fig = plt.figure()
ax = plt.axes(xlim=(0, 365), ylim=(0, 27))
ax.set_xlabel('Month')
ax.set_ylabel('Hours of Daylight per day')
ax.set_title("Hours of daylight throughout the year")
ax.set_yticks([0, 4, 8, 12, 16, 20, 24])
plt.xticks([0, 30.42, 60.84, 91.26, 121.68, 152.1, 182.52, 212.94, 243.36, 273.78, 304.2, 334.62])
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'], ha='left')
line, = ax.plot([], [], lw=2)
lat = range(-90, 91)
days = range(365)

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

def animate(i):
    ax.collections.clear()
    x = days
    y = Daylight(i) 
    line.set_data(x, y)
    plt.legend(['Latitude: {} degrees'.format(i)], loc='upper left')
    plt.fill_between(x, y, step="pre", alpha=0.4, color='yellow')
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=lat, interval=55)

writergif = animation.PillowWriter(fps=30)
anim.save('filename.gif',writer=writergif)
plt.show()

    
