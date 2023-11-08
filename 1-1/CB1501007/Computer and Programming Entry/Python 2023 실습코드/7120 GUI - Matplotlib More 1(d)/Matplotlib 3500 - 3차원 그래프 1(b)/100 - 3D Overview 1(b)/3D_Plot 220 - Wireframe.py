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
ax.plot_wireframe(X, Y, Z,  cstride=8, rstride=8, color = 'orange', alpha=0.5)

plot.show()
