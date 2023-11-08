
import matplotlib.pyplot as plot

x = [1, 2, 3, 4, 8,15]    # x값
y = [1, 4, 9, 16, 25, 17] # 해당되는 y=f(x) 값

plot.ylim(0, 40)
plot.xlim(-3,20)
plot.plot(x, y, 'r-')
plot.plot(x, y, 'ko')
plot.show() # show the plot on the screen