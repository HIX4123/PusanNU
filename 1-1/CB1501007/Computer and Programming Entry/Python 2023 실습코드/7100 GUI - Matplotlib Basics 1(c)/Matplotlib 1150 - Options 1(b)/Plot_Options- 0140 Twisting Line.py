import matplotlib.pyplot as plot

N = 16
for i in range(N):
	plot.gca().add_line(plot.Line2D((0, i), (N - i, 0), color = '.5'))

plot.grid(True)
plot.axis('scaled')  #이것은 문자가 아니라 PARAMETER 입니다.
plot.show()