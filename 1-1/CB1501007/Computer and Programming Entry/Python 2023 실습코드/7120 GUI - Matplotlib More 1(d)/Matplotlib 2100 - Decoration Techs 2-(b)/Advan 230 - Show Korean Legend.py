
#lineplotAxis.py
import numpy as np
import pylab as pl
import matplotlib

from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/NanumGothic.ttf").get_name()
rc('font', family=font_name)

# Make x, y arrays for each graph
x1 = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
x2 = [1, 3, 4, 6, 8]
y2 = [2, 5, 8, 5, 16]


plot1 = pl.plot(x1, y1, 'r', label='돼지')
plot2 = pl.plot(x2, y2, 'g', lw=2, ls='--', label='늑대')

# give plot a title
pl.title(   ' 여기는 한글을 놓아 볼까?')
pl.xlabel( '월별 통계')
pl.ylabel('나타난 횟수')
# set axis limits
pl.xlim(0.0, 9.0)
pl.ylim(0.0, 30.)

# show the plot on the screen

pl.legend( )
pl.show()
