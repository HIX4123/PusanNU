
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


x = [51, 4,3, 14, 35, 66, 7,83, 94,14,51,52,\
     63, 8, 75, 76, 87, 18, 29, 50, 90, 55, 56, 100]

num_bins = 6

counts, bins, patches = plt.hist(x, num_bins, density=1, rwidth=0.7, facecolor='blue', alpha=0.5)

print("counts=", counts )
print("bins=", bins)



plt.show()

