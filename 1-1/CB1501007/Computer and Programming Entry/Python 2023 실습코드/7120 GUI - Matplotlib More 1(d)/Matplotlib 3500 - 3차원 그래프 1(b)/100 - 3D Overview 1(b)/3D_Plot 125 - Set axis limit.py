import numpy
import math
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plot

plot.rcParams["figure.figsize"] = (8,8) # 크기를 10인치 10인치



grids  = 100
sbegin = 1
send   = 10
vx = numpy.linspace( sbegin, send, grids)
vy = numpy.linspace( sbegin, send, grids)
X, Y = numpy.meshgrid( vx, vy)

Z1 =  (X)**(0.2) + 2*(Y)**(0.5) + 10



fig = plot.figure()
ax  = fig.gca(projection = '3d')

ax.plot_wireframe(X, Y, Z1,  cstride=4, rstride=4, color = 'orange', alpha=0.5)

ax.set_xlabel('X-axis',     fontsize=15, rotation=150)
ax.set_ylabel('Y-axis', color='orange', fontsize=15, rotation=150)
ax.set_zlabel('f(x,y)=Z',  fontsize=15, rotation=60, color='blue')
ax.yaxis._axinfo['label']['space_factor'] = 3.0

#plot.xlim(0,30)
#plot.ylim(0,50)
ax.axes.set_xlim3d(left=0.1, right=10.8)
ax.axes.set_ylim3d(bottom=0.2, top=11.8)
ax.axes.set_zlim3d(bottom=0.2, top=55.8)

#plot.zlim(0,1200)

plot.title("'A curved surface", fontsize=25)
plot.show()
