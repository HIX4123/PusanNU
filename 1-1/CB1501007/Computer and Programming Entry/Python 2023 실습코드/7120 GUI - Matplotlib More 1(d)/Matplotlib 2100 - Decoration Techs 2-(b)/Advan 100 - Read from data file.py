

#readFileAndPlot.py
import numpy as np
import pylab as pl

from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/NanumGothic.ttf").get_name()
rc('font', family=font_name)


# Use numpy to load the data contained in the file
# ’fakedata.txt’ into a 2-D array called data
data = np.loadtxt('fakedata.txt')

# plot the first column as x, and second column as y
pl.plot(data[:,0], data[:,1], 'rx')
pl.xlabel('문장 번호', color='green')
pl.ylabel('총 출현회수', color='b')
#pl.xlim(0, 15)

pl.show()

