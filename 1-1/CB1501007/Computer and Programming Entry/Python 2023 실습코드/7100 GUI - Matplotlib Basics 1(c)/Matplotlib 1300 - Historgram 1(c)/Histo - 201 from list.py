
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

# The parameter rwidth specifies the width of your bar relative
# to the width of your bin. For example, if your bin width is say 1
# and rwidth=0.5, the bar width will be 0.5.
# On both side of the bar you will have a space of 0.25.

x = [21,22,23,4,5,6,77,8,9,10,31,32,33,34,35,36,37,18,49,50,100]
num_bins = 5

n, bins, patches = plt.hist(x, num_bins, facecolor='blue', alpha=0.5,rwidth=0.8)
#n, bins, patches = plt.hist(x, num_bins, facecolor='blue', alpha=0.7, normed=True, rwidth=0.7)
plt.show()

# In a standard histogram, the total area of all bins is either 1
# if normed or N. Here's a simple example: