#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------

from matplotlib import pyplot as plt

# Set the limits of the plot
plt.xlim(-1, 10)
plt.ylim(-1, 15)

# Don't mess with the limits!
plt.autoscale(False)

# Plot anything you want
plt.plot([0, 1, 6, 10], [5, 3, 2, 8], color='k', marker='o')
plt.plot([3, 5], [7, 2], 'ro')
plt.show()