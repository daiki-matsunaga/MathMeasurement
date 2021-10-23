import numpy as np
import matplotlib.pyplot as plt

x = np.loadtxt('x.txt')
y = np.loadtxt('y.txt')
z1 = np.loadtxt('z1.txt')
z2 = np.loadtxt('z2.txt')

fig, ax = plt.subplots()
cbar = ax.contourf(x, y, z1, cmap="gray", levels = 15)
ax.set_aspect('equal')
fig.colorbar(cbar)
plt.show()

fig, ax = plt.subplots()
cbar = ax.contourf(x, y, z2, cmap="gray", levels = 15)
ax.set_aspect('equal')
fig.colorbar(cbar)
plt.show()
