
import numpy as np
import matplotlib.pyplot as plt

p = np.poly1d([ 1, -3, -5, 6])  #f(x)=1x^3 -3 x^2 - 5x + 6
x = np.linspace(-3, 4, 10)  # x point를 10개로, 20개로하면 더 smooth
x20 = np.linspace(-3, 4, 60)
y = p(x)
y20 = p(x20)
plt.plot(x, y, 'o-')
plt.plot(x20, y20, "tomato",  'x-')
plt.show()


