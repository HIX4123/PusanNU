
"""
The accepted answers gives the code for a histogram with overlapping bars,
but in case you want each bar to be side-by-side (as I did),
try the variation below:
"""
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-deep')

x = np.random.normal(1, 2, 5000)
y = np.random.normal(-1, 3, 2000)
bins = np.linspace(-10, 10, 20)

plt.hist([x, y], bins, label=['x', 'y'])
plt.legend(loc='upper left')
plt.show()