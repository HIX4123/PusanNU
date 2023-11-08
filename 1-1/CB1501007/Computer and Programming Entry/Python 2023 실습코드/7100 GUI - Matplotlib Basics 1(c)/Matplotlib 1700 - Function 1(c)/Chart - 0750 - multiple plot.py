
import numpy
import matplotlib.pyplot as plot

data = numpy.loadtxt('sample.txt')
print(data.T)

for column in data.T:
	plot.plot(data[:,0], column, "tomato", marker="d", )

plot.show()

