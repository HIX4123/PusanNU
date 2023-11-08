
import matplotlib.pyplot as plt

x=5
y=6

plt.plot( x, y, 'ko')    # black with 'o' mark
plt.axis([0, 6, 0, 20])  # x축은 [0,6], y축은 [0,20]

plt.ylabel('Y-value PLOT')
plt.xlabel('X-value PLOT')
#plt.autoscale(False)
plt.show()