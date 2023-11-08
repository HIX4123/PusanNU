
x="""In the case you have different sample sizes,
it may be difficult to compare the distributions
with a single y-axis. For example:"""

import numpy as np
import matplotlib.pyplot as plt

#makes the data
y1 = np.random.normal(-2, 2, 1000)
y2 = np.random.normal(2, 2, 5000)
colors = ['tomato','khaki']

#plots the histogram
fig, ax1 = plt.subplots()
ax1.hist([y1,y2],color=colors, alpha=0.4)
ax1.set_xlim(-10,10)
ax1.set_ylabel("Count")
plt.tight_layout()
plt.show()
