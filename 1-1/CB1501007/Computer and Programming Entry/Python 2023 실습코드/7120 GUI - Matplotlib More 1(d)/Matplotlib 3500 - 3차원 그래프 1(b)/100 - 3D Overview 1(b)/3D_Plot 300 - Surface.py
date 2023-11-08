import numpy
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plot

plot.rcParams["figure.figsize"] = (10,10) # 크기를 10인치 10인치

x = numpy.linspace(-3, 3, 256)
y = numpy.linspace(-3, 3, 256)
X, Y = numpy.meshgrid(x, y)
Z = numpy.sinc(numpy.sqrt(X ** 2 + Y ** 2))

fig = plot.figure()
ax = fig.gca(projection = '3d')
#ax.plot_surface(X, Y, Z, color = 'w')
#ax.plot_surface(X, Y, Z, cmap=cm.gray)
#ax.plot_surface(X, Y, Z, cmap=cm.gray, linewidth=0, antialiased=False, color='olive')
ax.plot_surface(X, Y, Z,  linewidth=0, antialiased=False, color='olive', alpha=0.3)
ax.set_xlabel('Banana', fontsize=15, color = "blue", rotation=150)
ax.set_ylabel('Tomato', fontsize=15, color = "olive", rotation=-80)
ax.set_zlabel('Price for item', fontsize=15, color="red", rotation=60)

plot.show()
