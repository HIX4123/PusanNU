import matplotlib.pyplot as plot

shape = plot.Circle((0, 0), radius = 1., color = 'green', alpha=0.4)
plot.gca().add_patch(shape)

plot.grid(False)
plot.axis('scaled')
plot.xlim([-2,2])
plot.ylim([-2,2])
plot.show()
