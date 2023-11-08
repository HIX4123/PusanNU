
"""
Unless you are not already familiar with it, you should have
a look at the matplotlib gallery.
There you will find lots of examples hot to use the
add_subplot and subplots commands.
A minimal example of what you propably want to achieve is """

import matplotlib.pyplot as plt
import numpy as np

data=np.random.random((100,50))
xaxes = ['x1','x2','x3','x4']
yaxes = ['y1','y2','y3','y4']
titles = ['t1','t2','t3','t4']
myc= ['yellow', 'red', 'blue', 'green']

f,a = plt.subplots(2,2)
a = a.ravel()
for idx,ax in enumerate(a):
    ax.hist(data[idx], color=myc[idx], rwidth=0.9)
    ax.set_title(titles[idx])
    ax.set_xlabel(xaxes[idx])
    ax.set_ylabel(yaxes[idx])
plt.tight_layout()

plt.show()
