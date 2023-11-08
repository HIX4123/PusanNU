#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

data1 = np.random.randn(25)
data2 = np.random.randn(35)
data3 = np.random.randn(55)
data4 = np.random.randn(10)

fig = plt.figure(figsize=(7,7))

ax1 = plt.subplot2grid((2,2), (0,0),)
ax2 = plt.subplot2grid((2,2), (1,0),)
ax3 = plt.subplot2grid((2,2), (0,1),)
ax4 = plt.subplot2grid((2,2), (1,1),)

ax1.plot(data1)
ax2.plot(data2)
ax3.plot(data3)
ax4.plot(data4)

plt.show()