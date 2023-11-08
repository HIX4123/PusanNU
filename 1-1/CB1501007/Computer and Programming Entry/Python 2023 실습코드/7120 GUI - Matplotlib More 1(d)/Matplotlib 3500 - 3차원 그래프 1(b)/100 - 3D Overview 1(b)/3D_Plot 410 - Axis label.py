
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = (10,10) # 크기를 10인치 10인치

mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
z = np.linspace(-2, 2, 100)
r = z**2 + 1
x = r * np.sin(theta)
y = r * np.cos(theta)
ax.plot(x, y, z, label='parametric curve')
ax.legend()

ax.set_xlabel('$X$', fontsize=20, rotation=150)
ax.set_ylabel('$Y$')
ax.set_zlabel(r'$\gamma$', fontsize=30, rotation=60)
ax.yaxis._axinfo['label']['space_factor'] = 3.0

plt.show()