


import numpy as np
import matplotlib.pyplot as plt

## creating dummy data for two plots

## plot 1 data
x1 = np.arange(-10,100)
y1 = 2*x1

## plot 2 data
x2 = np.arange(-50,25)
y2 = 3*(x2**2)

## plotting them
plt.xlim(-10,10)
plt.ylim(0,100)

plt.plot(x1, y1)
plt.plot(x2,y2)
plt.show()

plt.xlim(-2.5,1)
plt.ylim(-5,10)
plt.plot(x1, y1)
plt.plot(x2,y2)

plt.show()


## setting the limits on the x-axis and y-axis

