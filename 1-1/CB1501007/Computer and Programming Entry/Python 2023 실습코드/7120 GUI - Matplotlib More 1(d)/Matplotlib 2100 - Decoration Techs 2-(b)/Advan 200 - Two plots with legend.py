
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
x2 = [1, 2, 4, 6, 8]
y2 = [2, 4, 8, 12, 16]


plot1 = pl.plot(x1, y1, 'rx', label="Banana")
plot2 = pl.plot(x2, y2, 'g', label="Tomato")

# give plot a title
pl.title( '여러분 여기에 한글을  넣어 봅시다.')
pl.xlabel('월별 통계')
pl.ylabel('나타난 횟수')
# set axis limits
pl.xlim(0.0, 9.0)
pl.ylim(0.0, 30.)

# show the plot on the screen

pl.legend( ) # 범례를 만들어 줍니다. 위에서 반드시 label로 선언
pl.show()
