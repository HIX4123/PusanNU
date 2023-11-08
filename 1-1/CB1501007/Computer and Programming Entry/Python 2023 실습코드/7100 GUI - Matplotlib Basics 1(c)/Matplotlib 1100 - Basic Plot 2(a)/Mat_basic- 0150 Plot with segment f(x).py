
import matplotlib.pyplot as plot
X=  [ 1, 2,  3,  4,   7]
Y = [51, 54, 59, 66, 61]
plot.plot( X, Y, color="purple", marker='+', linewidth=4, alpha=0.30)

plot.ylim(45, 70)
#plot.xlim(-2, 10)

plot.title( "How to Segment Graph!!!")
plot.ylabel('some numbers')
plot.xlabel('numbers in x-axis')
plot.show()