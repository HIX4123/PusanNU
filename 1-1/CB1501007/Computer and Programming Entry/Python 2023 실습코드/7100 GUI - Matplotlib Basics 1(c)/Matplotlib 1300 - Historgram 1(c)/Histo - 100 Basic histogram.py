"""
n: 각 bin에 들어있는 표본의 갯수,  the number of counts in each bin of the histogram
bins: 각 반의 왼쪽 값, the left hand edge of each bin
patches : 개별 patches, histogram을 반들 때 사용, e.g a collection of rectangles
"""

import numpy as np
import matplotlib.pyplot as plt


x = [55, 77, 67, 51,62,23,63, 74,97,78,99, 71,72,83,24,\
     45, 76, 9, 85,36,97,98,49,100]

num_bins = 7
n, bins, patches = plt.hist(x, num_bins, facecolor='tomato', alpha=0.5,rwidth=0.75)

plt.title('Red Chart')
print("n=", n)
print("bins=", bins )
print("patched=", patches)
#plt.setp(patches[3], 'facecolor', 'orange', alpha=1.0)
#plt.setp(patches[0], 'facecolor', 'tomato', alpha=0.3)

for w in patches :
    print(w)
plt.show( )


# In a standard histogram, the total area of all bins is either 1
# if normed or N. Here's a simple example: