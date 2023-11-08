import numpy
import matplotlib.pyplot as plot

X = numpy.linspace(0, 6, 1024)
Y1 = numpy.sin(X)
Y2 = numpy.cos(X)
Y3 = 0.5*numpy.cos(2*X)

plot.title("Well Done!!! ")
plot.xlabel('x-axis points')
plot.ylabel('sin(x) and cos(x) function')

plot.plot(X, Y1, c = 'blue'  ,             lw = 4., label = 'sin(X)', alpha=0.3)
plot.plot(X, Y2, c = 'green' , ls = '--',  lw = 4., label = 'cos(X)', alpha=0.5)
plot.plot(X, Y3, c = 'red'   , ls = ':',   lw = 2., label = 'cos(2X)', alpha=0.7)

plot.legend()
plot.show()
