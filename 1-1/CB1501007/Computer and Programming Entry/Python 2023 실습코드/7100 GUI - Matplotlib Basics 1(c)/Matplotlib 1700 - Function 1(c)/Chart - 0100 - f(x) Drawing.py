
import matplotlib.pyplot as plot
import numpy as np

X = np.linspace(-12, 5, 100)
Y = [ - x ** 2 - 6 * x + 28  for x in X]

plot.plot(X, Y)
plot.show()
