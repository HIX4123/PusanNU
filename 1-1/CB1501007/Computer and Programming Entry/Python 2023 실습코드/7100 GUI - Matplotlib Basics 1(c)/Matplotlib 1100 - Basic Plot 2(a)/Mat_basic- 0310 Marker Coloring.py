
# marker 점에 대해서만 다른 색을 지정한다.

import matplotlib.pyplot as plot

plot.figure(figsize=(8,5))
X  = [ 1, 2,  3,  4,  7]
Y1 = [ 1, 4,  9, 16, 11]
Y2 = [ 25, 8, 13, 12,  28]
plot.plot( X, Y1, 'red'   , marker='o', alpha=0.5)
plot.plot( X, Y2, 'orange', marker='D', \
           markerfacecolor='r', markeredgecolor='k', \
           alpha=0.5, linewidth=3)

plot.title(r'PNU CSED is the Best One.')
plot.ylabel('some numbers')
plot.show()

# marker https://matplotlib.org/3.1.1/api/markers_api.html

# markersize=5,
# markerfacecolor='w',\
# markeredgewidth=1.5,
# markeredgecolor=(r, g, b, 1))