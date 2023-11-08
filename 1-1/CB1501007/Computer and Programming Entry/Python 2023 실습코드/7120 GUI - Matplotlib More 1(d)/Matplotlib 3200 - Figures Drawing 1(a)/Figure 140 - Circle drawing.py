#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------
# gca() returns the current Axis instance.
# Setting the axis to “scaled” ensures that you can see the added shape properly.
# This should give you something like Figure 2[^colours].



import matplotlib.pyplot as plt

plt.axes()

circle = plt.Circle((15, 5), radius=6.75, fc='y', alpha=0.5, fill=None)
plt.gca().add_patch(circle)

rectangle = plt.Rectangle((10, 10), 5, 10, fc='r', alpha=0.5)
#                          왼쪽아래 코너, 가로, 세로
plt.gca().add_patch(rectangle)

plt.axis('scaled')
plt.show()
