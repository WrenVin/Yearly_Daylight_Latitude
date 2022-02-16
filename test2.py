import numpy as np
import matplotlib.pyplot as plt
import math

def f(x):
    return (0.2163108 + (2 * math.atan(0.9671396 * math.tan(.00860 * (x- 186)))))
y=[]
x = range(366)

for i in x: 
    y.append(f(i))   # This is already vectorized, that is, y will be a vector!
plt.plot(x, y)
plt.grid()
plt.show()