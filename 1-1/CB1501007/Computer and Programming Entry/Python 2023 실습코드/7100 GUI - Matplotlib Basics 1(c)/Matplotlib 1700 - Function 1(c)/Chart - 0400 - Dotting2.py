
import numpy
import matplotlib.pyplot as plot

X = numpy.linspace(0, 2 * numpy.pi, 50)
Ya = numpy.sin(X)
Yb = numpy.cos(X)

plot.plot(X, Ya, 'rx')
plot.plot(X, Yb, 'bo')
plot.show()
