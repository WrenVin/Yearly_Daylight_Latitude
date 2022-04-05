import numpy as np

# create x,y,z data for 3d surface plot
x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X ** 2 + Y ** 2))

import matplotlib.pyplot as plt

# draw surface plot
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
ax.set_title('surface')
import surf2stl

# export surface to a stl format file
surf2stl.write('3d-sinusoidal.stl', X, Y, Z)
