
import numpy as np
import matplotlib.pyplot as plt

mean = [0, -1]
cov = [[111, 0], [0, 111]]  # diagonal covariance


x, y = np.random.multivariate_normal(mean, cov, 100).T  #.T transpose
W = list(zip(x,y))

plt.plot(x, y, 'x')
plt.axis('equal')
plt.show()


