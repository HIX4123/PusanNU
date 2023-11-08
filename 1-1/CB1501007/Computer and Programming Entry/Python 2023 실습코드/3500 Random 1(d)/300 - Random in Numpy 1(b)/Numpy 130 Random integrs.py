#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-04-20
#-------------------------------------------------------------------------------
## plot(x, y)        # plot x and y using default line style and color
## plot(x, y, 'bo')  # plot x and y using blue circle markers
## plot(y)           # plot y using x as index array 0..N-1
## plot(y, 'r+')     # ditto, but with red plusses
## 이걸 보시오.      https://matplotlib.org/3.1.0/api/_as_gen/matplotlib.pyplot.plot.html

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(2020)

rpoints = ar4 = np.random.randint(100,500, size=(50, 2))
print( rpoints )

plt.plot( rpoints[:,0], rpoints[:,1], "ro", picker=5)  # red O


# options color='green', marker='o',  linestyle='dashed',  linewidth=2, markersize=12,  alpha=.5)


plt.show()



