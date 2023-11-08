#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-04-23
#-------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

#-----------------------------------------------
# Plots several points with cubic interpolation
#-----------------------------------------------
fig = plt.figure()
ax = fig.add_subplot(111)

x = np.linspace(0, 10, num=6, endpoint=True)
y = abs(x**2)

xnew = np.linspace(0, 10, num=40, endpoint=True)
cubicInterp = interp1d(x, y, kind='cubic')
line = ax.plot(x,y, 'o', picker=5)  # 5 points tolerance
lineInterp = ax.plot(xnew,cubicInterp(xnew), '-')

#---------------
# Events
#---------------

def on_pick(event):
    print ( "clicked" )
    plt.setp(line,'color','red')
    fig.canvas.draw()

#-----------------------------


fig.canvas.mpl_connect('pick_event', on_pick)

plt.show()