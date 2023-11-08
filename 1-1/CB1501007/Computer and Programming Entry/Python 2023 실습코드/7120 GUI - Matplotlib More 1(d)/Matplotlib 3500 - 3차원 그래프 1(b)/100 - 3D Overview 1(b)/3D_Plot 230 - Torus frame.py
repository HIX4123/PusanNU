import numpy
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plot

plot.rcParams["figure.figsize"] = (10,10) # 크기를 10인치 10인치

angle = numpy.linspace(0, 2 * numpy.pi, 64)
theta, phi = numpy.meshgrid(angle, angle)

r, R = .25, 1.
X = (R + r * numpy.cos(phi)) * numpy.cos(theta)
Y = (R + r * numpy.cos(phi)) * numpy.sin(theta)
Z = r * numpy.sin(phi)

fig = plot.figure()
ax = fig.gca(projection = '3d')

ax.set_xlim3d(-1, 1)
ax.set_ylim3d(-1, 1)
ax.set_zlim3d(-1, 1)
#ax.plot_surface(X, Y, Z, rstride = 1, cstride = 1, linewidth = 0, antialiased = False, cmap = plot.get_cmap('jet'))
#ax.pbaspect = [6., 6., 1]
#ax.plot_surface(X, Y, Z, color = 'w', rstride = 1, cstride = 1)

ax.set_xlabel('X-axis', fontsize=15, color = "blue", rotation=150)
ax.set_ylabel('Y-axis', fontsize=15, color = "orange", rotation=-80)
ax.set_zlabel('Z=f(x,y)', fontsize=15, color="red", rotation=60)

ax.plot_wireframe(X, Y, Z, color = 'olive', alpha=0.4)


plot.show()

