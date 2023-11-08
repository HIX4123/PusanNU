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
fig.suptitle('PNU Summer Beer Festival. ComeOn Yeh', color='r',  fontsize=12)
ax.set_xlabel('xlabel', fontsize=20 )
ax.set_ylabel('ylabel', fontsize=12)   # relative to plt.rcParams['font.size']

# setting label sizes after creation
ax.xaxis.label.set_size(15)
#plt.draw()
plt.show()