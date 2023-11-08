#-------------------------------------------------------------------------------
# Purpose:     2020 Prof. Zoh'w Work
# Author:      Cho
# Created:     2020-06-12
#-------------------------------------------------------------------------------


import matplotlib.pyplot as plt

# set up a plot with dummy data
fig, ax = plt.subplots()
x = [0, 1, 2, 5]
y = [0, 3, 9, 4]
ax.plot(x,y)

# title and labels, setting initial sizes
fig.suptitle('test title', fontsize=12)
ax.set_xlabel('xlabel', fontsize=10 )
ax.set_ylabel('ylabel', fontsize='medium')   # relative to plt.rcParams['font.size']

# setting label sizes after creation
ax.xaxis.label.set_size(20)
#plt.draw()
plt.show()