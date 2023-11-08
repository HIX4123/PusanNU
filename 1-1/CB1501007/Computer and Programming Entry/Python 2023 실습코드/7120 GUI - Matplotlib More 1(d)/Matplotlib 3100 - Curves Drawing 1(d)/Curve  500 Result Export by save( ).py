
import matplotlib.pyplot as plot

x = [1, 2, 3, 4, 8,15]    # x값
y = [1, 4, 9, 16, 25, 17] # 해당되는 y=f(x) 값
plot.plot(x, y)
plot.savefig('Myfirst.png') #반드시 show( )전에 먼저 save해야 한다.
plot.show() # show the plot on the screen



