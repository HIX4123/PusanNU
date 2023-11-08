
import matplotlib.pyplot as plt
import numpy as np
import math

t = np.arange(0., 5., 0.2) # evenly sampled time at 200ms intervals

# red dashes, blue squares and green triangles
plt.plot(t, 6*t+5, 'r--', t, t**2, 'bo', t, t**3, 'g^')
plt.plot(t, 12*t+11, 'g-')
plt.show()
