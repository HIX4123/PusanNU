#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-05-06
#-------------------------------------------------------------------------------

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plot

plot.rcParams["figure.figsize"] = (10,10) # 크기를 10인치 10인치

X=[ 4,  6, 11, 21, 34]
Y=[ 7, -1, 23,  4, 11]
Z=[ 12, 5, -3, -5, 22]

fig = plot.figure()
ax = fig.gca(projection='3d')

#ax.scatter((0, 0, 1), (0, 1, 0), (1, 0, 0), (4,3,1),)

ax.xaxis._axinfo['tick']['color']='r'
ax.yaxis._axinfo['tick']['color']='r'
ax.zaxis._axinfo['tick']['color']='r'
ax.plot(X, Y, Z, color="orange", marker='o', )

plot.show()