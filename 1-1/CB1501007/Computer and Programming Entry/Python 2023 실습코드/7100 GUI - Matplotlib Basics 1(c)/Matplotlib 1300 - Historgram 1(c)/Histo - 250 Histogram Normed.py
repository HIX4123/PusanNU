
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


x = [21,22,23,4,5,6,77,8,9,10,31,32,33,34,35,36,37,18,49,50,100]
num_bins = 5

#n, bins, patches = plt.hist(x, num_bins, facecolor='blue', alpha=0.5, normed=False,rwidth=0.8)
n, bins, patches = plt.hist(x, num_bins, facecolor='blue', alpha=0.7, normed=True, rwidth=0.8)
print("n=", n, sum(n))
print("bins= ", bins)
print("patches= ", patches)

plt.show()

# In a standard histogram, the total area of all bins is either 1
# if normed or N. Here's a simple example: