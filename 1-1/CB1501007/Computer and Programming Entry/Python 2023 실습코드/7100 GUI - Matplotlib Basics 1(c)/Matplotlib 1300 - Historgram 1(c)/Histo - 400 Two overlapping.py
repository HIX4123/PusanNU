
import random
import numpy
from matplotlib import pyplot

x = [random.gauss(3,1) for _ in range(400)]
y = [random.gauss(4,2) for _ in range(400)]

bins = numpy.linspace(-3, 14, 30)

pyplot.hist(x, bins, alpha=0.5, label='x', rwidth=0.9)
pyplot.hist(y, bins, alpha=0.5, label='y', rwidth=0.9)
pyplot.legend(loc='upper right')
pyplot.show()