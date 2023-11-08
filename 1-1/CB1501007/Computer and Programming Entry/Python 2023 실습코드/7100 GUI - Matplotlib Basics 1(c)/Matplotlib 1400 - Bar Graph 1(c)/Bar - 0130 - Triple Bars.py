
import matplotlib.pyplot as plot

data = [[5., 25., 50., 20.],
        [4., 13., 51., 17.],
        [6., 22., 45., 19.]]

plot.bar(list(range(4)), data[0], width = 0.25)
plot.bar([x + 0.25 for x in range(4)], data[1], width = 0.25)
plot.bar([x + 0.50 for x in range(4)], data[2], width = 0.25)

plot.show()
