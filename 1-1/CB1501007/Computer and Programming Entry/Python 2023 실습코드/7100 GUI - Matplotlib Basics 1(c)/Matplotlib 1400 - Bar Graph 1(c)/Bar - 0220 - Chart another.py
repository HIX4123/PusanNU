import matplotlib.pyplot as plot

yd = [5., 25., 50., 20., 34, 5, 7, 19, 13, 12]


ymax = max(yd)
plot.ylim(0, ymax*1.2)
plot.xlim(-2, len(yd)+3)

plot.bar(list(range(len(yd))), yd, width = 0.7, color='g')

plot.show()
