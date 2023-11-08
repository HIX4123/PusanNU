#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

data1 = np.random.randn(25)
data2 = np.random.randn(15)
data3 = np.random.randn(20)
data4 = np.random.randn(15)
fig = plt.figure(figsize=(6,6))  # 전체 그림의 크기를 조정

# 2 by 2 그리드 공간에서 (0,0) 위치에 그린다.

ax1 = plt.subplot2grid((2,2), (0,0),)
ax2 = plt.subplot2grid((2,2), (1,0),)
ax3 = plt.subplot2grid((2,2), (0,1),)
ax4 = plt.subplot2grid((2,2), (1,1),)

ax1.plot(data1, color='tomato')
ax2.plot(data2, color='khaki')
ax3.plot(data3, color='green', alpha= 0.3)
ax4.plot(data4, color='crimson', alpha= 0.3)

plt.autoscale(True)
plt.autoscale(False)
#plt.axis('scaled')
plt.axis()
plt.show()