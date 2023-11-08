import matplotlib.pyplot as plot

data = [5., 25., 50., 20., 13.0]
xlabel=["some", "day", "we", "love", "forever"]

plot.bar( xlabel, data, width = 0.7, alpha=0.6)

#plot.ylim(0,100)
plot.show()
