

import numpy as np

np.random.seed(0) # seeding

x_data = np.linspace(-5, 5, num=50)
y_data = 2.9 * np.sin(1.5 * x_data) + np.random.normal(size=50)


import matplotlib.pyplot as plt # And plot it
plt.figure(figsize=(8, 6))
plt.scatter(x_data, y_data)
plt.show()