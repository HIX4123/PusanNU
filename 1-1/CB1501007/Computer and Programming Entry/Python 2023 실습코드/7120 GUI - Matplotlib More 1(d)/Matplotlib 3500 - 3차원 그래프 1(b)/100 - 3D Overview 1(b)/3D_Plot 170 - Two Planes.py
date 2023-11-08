import numpy
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plot

plot.rcParams["figure.figsize"] = (10,10) # 크기를 10인치 10인치



grids  = 200
sbegin = 1
send   = 100
vx = numpy.linspace( sbegin, send, grids)
vy = numpy.linspace( sbegin, send, grids)
X, Y = numpy.meshgrid( vx, vy)

Z1 =  6*X**(0.5) + 4*Y**(0.6) + 10
Z2 =  4*X + 2*Y - 6

fig = plot.figure()
ax  = fig.gca(projection = '3d')

ax.plot_wireframe(X, Y, Z1,  cstride=4, rstride=4, color = 'orange', alpha=0.5)
ax.plot_wireframe(X, Y, Z2,  cstride=8, rstride=8, color = 'olive', alpha=0.5)

ax.set_xlabel('fav.menu probability, p',     fontsize=15, rotation=150)
ax.set_ylabel('No. of purchasing, n', color='orange', fontsize=15, rotation=150)
ax.set_zlabel('Total User Time',  fontsize=15, rotation=60, color='blue')
ax.yaxis._axinfo['label']['space_factor'] = 3.0

plot.title("'Offon'-KIOSK Time", fontsize=25)
plot.show()
