
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


x = [ 3, 5, 12, 23, 25, 30, 31, 36, 45, 55, 66, 78, 90, 91, 93, 99, 100]
print(x)

num_bins = 6

#n, bins, patches= plt.hist(x, num_bins, facecolor='blue', alpha=0.5, normed=True )
n, bins, patches = plt.hist(x, num_bins, facecolor='blue', alpha=0.5, rwidth=0.7)

print("\n n=", n)
print("\n np.diff(bins)= ", np.diff(bins))  # 각
w= n*np.diff(bins)
print("\n w = ", w )
print("\n sum(w) = ", sum(w))

for w in n :
    print( w/ sum(n) )
plt.show()

