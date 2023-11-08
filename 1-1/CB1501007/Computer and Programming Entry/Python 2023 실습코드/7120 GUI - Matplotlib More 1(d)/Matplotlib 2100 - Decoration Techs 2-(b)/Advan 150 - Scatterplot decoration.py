# scatterplot.py
import numpy as np
import pylab as pl
import matplotlib

from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/NanumGothic.ttf").get_name()
rc('font', family=font_name)



pl.xlabel('여기에 레이블을 표시')
pl.ylabel( 'y축은 여기에 놓습니다.')
# You can make a title for your plot by:
pl.title( '한글이 되는지 봅시다.')

#You can change the x and y ranges displayed on your plot by:
pl.xlim(0, 10)
pl.ylim(0, 30)

# Make an array of x values
x = [1, 2, 3, 4, 5, 9]
# Make an array of y values for each x value
y = [1, 4, 9, 16, 25, 22]
# use pylab to plot x and y as red circles

pl.plot(x, y, 'ro')
# show the plot on the screen
pl.show()

