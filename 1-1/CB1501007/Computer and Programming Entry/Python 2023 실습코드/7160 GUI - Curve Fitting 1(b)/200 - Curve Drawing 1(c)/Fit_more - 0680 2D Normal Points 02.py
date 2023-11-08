
import numpy as np
import matplotlib.pyplot as plot

N = 500
mu, sigma = 500, 200                # mean and standard deviation
x = np.random.normal(mu, sigma, N )
y = np.random.normal(mu, sigma, N )

for p in zip(x,y) :
    print(p)

plot.ylim(0, 2000)
plot.xlim(0, 2500)
plot.plot(x, y, 'x')
#plot.axis('equal')
plot.show()
