
import matplotlib.pyplot as plot

X, Y, Z = list(zip(*[[float(s) for s in line.split()] for line in open('sample.txt', 'r')]))

print(f'X[]= {X}')
print(f'Y[]= {Y}')
print(f'Z[]= {Z}')

plot.plot( X, Y, 'red'   , marker='o', alpha=0.3, linewidth=4)
plot.plot( X, Z, 'orange', marker='D', alpha=0.3, linewidth=4)
plot.show()
