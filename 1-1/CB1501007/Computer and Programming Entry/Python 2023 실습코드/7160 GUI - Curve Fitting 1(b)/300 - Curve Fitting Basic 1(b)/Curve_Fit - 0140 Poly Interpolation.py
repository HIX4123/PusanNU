
import numpy as np
import matplotlib.pyplot as plt

points = np.array([(1, -4), (2, -20), (5, 12), (9, -10)])

x = points[:,0]           # get x and y vectors
y = points[:,1]

# 데이터 point의 수가 K개 일 때 K-1로 fit하면 interploation

fx3 = np.polyfit(x, y, 3)   # calculate 3차 polynomial
print("찾은 다항식 = ", fx3)
f   = np.poly1d( fx3 )  # 다항식

# calculate new x's and y's
x_new = np.linspace(x[0], x[-1], 50)
y_new = f(x_new)

plt.plot(x,y,'o', x_new, y_new)
plt.xlim([x[0]- 2, x[-1] + 2 ])
plt.ylim(-50, 50)
plt.show()