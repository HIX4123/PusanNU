
import numpy
import matplotlib.pyplot as plot

X = numpy.linspace(-3, 2, 30) # -3에서 2까지 구간의 개수는 100개
Y = X ** 2 - 2 * X + 1.
Z = X ** 3 - 10 * X - 5

plot.plot(X, Y, '.b-')
plot.plot(X, Z, 'xr')  # 점은 x로 마킹하고 이어 주는 작업은 없다.
plot.show()
