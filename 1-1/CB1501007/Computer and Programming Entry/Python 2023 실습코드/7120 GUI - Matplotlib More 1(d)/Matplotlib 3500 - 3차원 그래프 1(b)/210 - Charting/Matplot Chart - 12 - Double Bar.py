#-*- coding: cp949 -*-

import matplotlib.pyplot as plot

data =  [ 22, 33, 11, 45 ]
data2 = [ 45, 78, 16, 9 ]

plot.bar( [1,3,5,7], data,  color='r', width = 0.8, label='what?')
plot.bar( [2,4,6,8], data2,  color='y', width = 0.8, label='what?')
plot.ylim = max(data)*1.2
plot.xlim = len(data)*1.2

plot.xlabel('Group')
plot.ylabel('Scores')
plot.title('Scores by group and gender')

plot.legend()
plot.show()
