import random
import matplotlib.pyplot as plot

count = 1000
X = [random.randrange(1,100) for i in range(count)]

plot.hist(X, bins = 20, rwidth=0.9)
plot.show()
