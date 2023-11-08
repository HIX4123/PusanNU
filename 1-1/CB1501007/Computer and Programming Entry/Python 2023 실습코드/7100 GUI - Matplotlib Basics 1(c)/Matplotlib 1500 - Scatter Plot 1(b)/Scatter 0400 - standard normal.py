#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------


import numpy as np
import matplotlib.pyplot as plt

data = np.random.standard_normal((100,2))

plt.scatter(data[:,0],data[:,1],color ='1.0',edgecolor = '0.0')


plt.show()
