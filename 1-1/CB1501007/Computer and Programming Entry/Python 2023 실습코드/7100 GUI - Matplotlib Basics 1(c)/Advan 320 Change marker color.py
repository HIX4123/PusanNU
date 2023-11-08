#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-05-06
#-------------------------------------------------------------------------------


import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np

# The data
x = np.linspace(0, 10, 1000)
y = np.sin(2 * np.pi * x)

# The colormap
cmap = cm.jet

# Create figure and axes
fig = plt.figure(1)
fig.clf()
ax = fig.add_subplot(1, 1, 1)

# Plot every single point with different color
for i in range(len(x)):
    c = cmap(int(np.rint(x[i] / x.max() * 255)))
    ax.plot(x[i], y[i], 'o', mfc=c, mec=c)
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([-1.1, 1.1])
    ax.set_xlabel('x')
    ax.set_ylabel('y')

plt.draw()
plt.show()

# Save the figure
# fig.savefig('changing_marker_color.png', dpi=80)