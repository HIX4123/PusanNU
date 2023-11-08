import numpy
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plot

plot.rcParams["figure.figsize"] = (8,8) # 크기를 10인치 10인치

X=[ 4,  6, 11, 21, 34]
Y=[ 7, -1, 23,  4, 11]
Z=[ -12, 5, -3, -5, 22]



fig = plot.figure()
ax = fig.gca(projection = '3d')

ax.set_xlabel('x-axis', fontsize=15, color = "blue", rotation=150)
ax.set_ylabel('y-axis', fontsize=15, color = "olive", rotation=-80)
ax.set_zlabel('z-axis', fontsize=15, color="red", rotation=60)

ax.plot(X, Y, Z, color="orange", marker='o')
plot.show()
