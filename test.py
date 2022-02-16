import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.tri as mtri

# u, v are parameterisation variables
u = (np.linspace(0, 2.0 * np.pi, endpoint=True, num=50) * np.ones((10, 1))).flatten()
v = np.repeat(np.linspace(-0.5, 0.5, endpoint=True, num=10), repeats=50).flatten()

# This is the Mobius mapping, taking a u, v pair and returning an x, y, z
# triple
X = (1 + 0.5 * v * np.cos(u / 2.0)) * np.cos(u)
Y = (1 + 0.5 * v * np.cos(u / 2.0)) * np.sin(u)
Z = 0.5 * v * np.sin(u / 2.0)

# Triangulate parameter space to determine the triangles
tri = mtri.Triangulation(u, v)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

# The triangles in parameter space determine which x, y, z points are
# connected by an edge
mobius_polycollection = ax.plot_trisurf(X, Y, Z, triangles=tri.triangles, cmap=plt.cm.Spectral)

from stl import mesh

data = np.zeros(len(tri.triangles), dtype=mesh.Mesh.dtype)
mobius_mesh = mesh.Mesh(data, remove_empty_areas=False)
mobius_mesh.x[:] = X[tri.triangles]
mobius_mesh.y[:] = Y[tri.triangles]
mobius_mesh.z[:] = Z[tri.triangles]
mobius_mesh.save('mobius.stl')
ax.plot_trisurf(X,Y,Z) 