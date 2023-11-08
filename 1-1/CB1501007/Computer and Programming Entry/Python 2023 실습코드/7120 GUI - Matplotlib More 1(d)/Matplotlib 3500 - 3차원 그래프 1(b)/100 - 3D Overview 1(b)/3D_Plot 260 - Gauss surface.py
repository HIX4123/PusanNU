import numpy
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plot

plot.rcParams["figure.figsize"] = (10,10) # 크기를 10인치 10인치

x = numpy.linspace(-3, 3, 256)
y = numpy.linspace(-3, 3, 256)
X, Y = numpy.meshgrid(x, y)

Z = numpy.exp(-(X ** 2 + Y ** 2))
u = numpy.exp(-(x ** 2))

fig = plot.figure()
#fig(figsize=(10,10))
ax = fig.gca(projection = '3d')

ax.set_zlim3d(0, 3)

ax.plot(x, u, zs=3, zdir='y', lw = 2, color = '.75')
ax.plot(x, u, zs=-3, zdir='x', lw = 2., color = 'k')
ax.plot_surface(X, Y, Z, color = 'w')

plot.show()
