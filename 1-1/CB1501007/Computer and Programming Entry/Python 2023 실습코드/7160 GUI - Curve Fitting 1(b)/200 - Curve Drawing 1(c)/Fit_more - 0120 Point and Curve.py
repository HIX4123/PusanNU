
import numpy as np
import matplotlib.pyplot as plt

points = np.array([(1, 1), (2, 4), (3, 1), (9, 3)]) # 4개의 점으로는 3차식

x = points[:,0]           # get x and y vectors
y = points[:,1]


z = np.polyfit(x, y, 3)   # calculate polynomial  3차식으로 fitting 하라.
f = np.poly1d(z)

# calculate new x's and y's
x_new = np.linspace(x[0], x[-1], 50)
y_new = f(x_new)

plt.plot(x,y,'o', x_new, y_new) # (x,y)는 0으로 표시,
plt.xlim([x[0]- 2, x[-1] + 2 ])
plt.ylim(-30, 10)
plt.show()