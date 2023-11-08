#-*- coding: cp949 -*-

import matplotlib.pyplot as plot

data = [ 22, 33, 11, 45, 78, 16, 9 ]

plot.bar(range(len(data)), data, width = 0.8)
plot.ylim = max(data)*1.1
plot.xlim = len(data)*1.2

plot.show()
