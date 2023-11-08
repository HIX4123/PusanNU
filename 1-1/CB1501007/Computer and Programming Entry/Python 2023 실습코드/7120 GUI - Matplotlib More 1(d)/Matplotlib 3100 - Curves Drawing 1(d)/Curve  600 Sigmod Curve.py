import matplotlib.pylab as plt
import numpy as np

x = np.arange(-8, 8, 0.5)
f = 1 / (1 + np.exp(-x))

plt.plot(x, f, '-ko' )
plt.xlabel('x', color='g')
plt.ylabel('f(x)')
plt.savefig('sigmod.png')
plt.show()
