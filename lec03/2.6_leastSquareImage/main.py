import numpy as np
import matplotlib.pyplot as plt

x = np.loadtxt('x.txt')
y = np.loadtxt('y.txt')
z = np.loadtxt('z.txt')

fig, ax = plt.subplots()
cbar = ax.contourf(x, y, z, cmap="gray")
ax.set_aspect('equal')
fig.colorbar(cbar)
plt.show()

ax = plt.axes(projection='3d')
ax.plot_surface(x, y, z)
plt.show()
