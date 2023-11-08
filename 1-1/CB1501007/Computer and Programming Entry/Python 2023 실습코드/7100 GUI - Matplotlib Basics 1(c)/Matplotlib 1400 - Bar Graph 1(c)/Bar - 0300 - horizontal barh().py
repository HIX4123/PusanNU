import matplotlib.pyplot as plot

data = [5., 25., 50., 20., 34., 12., 6., 9.]

plot.xlim(0,70)
plot.barh( list(range(len(data))), data, color='green' )
plot.show()
