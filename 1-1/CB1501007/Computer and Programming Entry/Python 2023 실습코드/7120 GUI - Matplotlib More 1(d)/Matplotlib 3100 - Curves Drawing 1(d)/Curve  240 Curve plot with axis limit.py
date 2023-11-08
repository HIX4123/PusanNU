
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1, 6)
plt.plot(x, x*1.5, x, x*3.0, x, x/3.0)
plt.axis([0, 7, -5, 20])
plt.show()