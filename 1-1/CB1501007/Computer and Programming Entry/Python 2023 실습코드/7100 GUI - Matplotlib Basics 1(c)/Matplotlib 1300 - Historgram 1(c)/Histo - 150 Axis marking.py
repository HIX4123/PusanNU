#!/usr/bin/python

import matplotlib.pyplot as plt
plt.title("A Plotting with axis Labeling")
x=[5, 3, 7, 2, 4, 1]
plt.plot(x)
plt.xticks(list(range(len(x))), ['Jan', 'Feb', 'March', 'Apr', 'May', 'June'])
plt.yticks(list(range(1, 11, 2)), [ 'bad', 'fair', 'average', 'good', 'excellent' ])
plt.show()
