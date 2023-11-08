
import numpy as np
import matplotlib.pyplot as plt

# generate some uniformly distributed data
x = np.random.rand(100) + np.random.rand(100)

# create the histogram
(n, edges, patches) = plt.hist(x, bins=7, label='hst', rwidth=0.8 )



# inspect the counts in each bin
print("n= ", n)      # 각 bin에 담긴 원소의 수
#print "edges = ", edges
for i, w in enumerate( edges ) :
    print("%2d = %.4f  "% (i, w))


plt.show()


# and we see that the bins are approximately uniformly filled.
# create a second histogram with more bins (but same input data)
# (n2, bins2, patches) = plt.hist(x, bins=20, label='hst' )



# bins are uniformly filled but obviously with fewer in each bin.