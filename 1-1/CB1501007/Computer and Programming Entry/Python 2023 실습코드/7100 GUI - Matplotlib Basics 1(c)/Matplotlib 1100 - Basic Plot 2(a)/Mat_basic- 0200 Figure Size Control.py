#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------

from matplotlib import pyplot as plt

plt.figure(figsize=(8,7)) # unit는 인치

x = [1, 2, 3, 7, 5, 1, -3, 6, 11]
y = [8, 4, 3, 5, 3, -3, 6, -2, 5]

#plt.plot(x, y )
plt.xlim(-35, 40)
plt.ylim(-40,40)
plt.scatter(x, y, s=453, c="red", alpha=0.2)
plt.show()