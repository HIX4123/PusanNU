

import matplotlib.pyplot as plt
import numpy as np
y = np.arange(1,3)
plt.title("A Plotting with Different Lines")
plt.plot(y,   ':',  color='y'  ) # yellow
plt.plot(y+1, '--', color='m') # magenta
plt.plot(y+2, '-.', color='c') # cyan
plt.show()
