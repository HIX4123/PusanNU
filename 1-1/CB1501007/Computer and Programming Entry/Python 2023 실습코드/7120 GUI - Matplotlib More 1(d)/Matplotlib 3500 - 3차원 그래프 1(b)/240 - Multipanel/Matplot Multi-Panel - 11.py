import numpy as np
from matplotlib import pyplot as plot

X = numpy.linspace(-2, 10, 1024)
plot.plot(X, numpy.sinc(X))

#plot.xticks([])
plot.xticks(np.arange(5), ('Tom', 'Dick', 'Harry', 'Sally', 'Sue'))
plot.yticks(np.arange(5), ('Tom', 'Dick', 'Harry', 'Sally', 'Sue'))
plot.ylim(-1,10)
plot.show()
