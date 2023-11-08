
#lineplotAxis.py
import numpy as np
import pylab as plot
import matplotlib

from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/NanumGothic.ttf").get_name()
rc('font', family=font_name)
plot.rcParams['axes.unicode_minus'] = False   # 음수 - r기호를 처리, 없으면 warning이 남.

x = [-3, 1, 2, 3, 4, 5]
# Make an array of y values for each x value
y = [7, 1, 4, 3, 16, 25]
# use pylab to plot x and y
plot.plot(x, y)
# give plot a title
plot.title( '여기에 한글을 놓아보자 - Plot of y vs. x', color='b')
# make axis labels
plot.xlabel( 'x axis')
plot.ylabel( 'y 축이다. 이 놈들아', color='r')
# set axis limits
#pl.xlim (0.0, 7.0)
#pl.ylim (0.0, 30.0)

plot.show()