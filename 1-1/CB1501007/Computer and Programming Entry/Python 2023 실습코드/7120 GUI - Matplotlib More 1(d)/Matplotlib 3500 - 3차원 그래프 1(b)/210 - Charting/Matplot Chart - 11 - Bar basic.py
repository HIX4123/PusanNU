#-*- coding: cp949 -*-

import matplotlib.pyplot as plot

data = [ 22, 33, 11, 45, 78, 16, 9 ]

plot.bar(range(len(data)), data,  color='darkred', width = 0.7, label='what?')
plot.ylim = max(data)*1.2
plot.xlim = len(data)*1.2

plot.xlabel('Group')
plot.ylabel('Scores')
plot.title('Scores by group and gender')

plot.legend()
plot.show()
