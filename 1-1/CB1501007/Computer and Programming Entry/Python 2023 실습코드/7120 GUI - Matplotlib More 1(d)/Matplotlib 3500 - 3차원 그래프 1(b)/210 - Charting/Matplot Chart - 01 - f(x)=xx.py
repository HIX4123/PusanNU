import matplotlib.pyplot as plot

X = range(50)
Y = [x ** 2 for x in X]

plot.plot(X, Y)
plot.show()
