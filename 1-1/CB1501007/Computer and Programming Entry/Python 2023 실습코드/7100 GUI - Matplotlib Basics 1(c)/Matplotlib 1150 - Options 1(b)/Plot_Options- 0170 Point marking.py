
import numpy as np
import matplotlib.pyplot as plt

xs = np.linspace(-np.pi, np.pi, 30)
ys = np.sin(xs)
markers_on = [12, 17, 18, 19, 25]  #번째, k-th marker

plt.plot(xs, ys, '-gD', markevery=markers_on)
plt.show()
