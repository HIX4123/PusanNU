import numpy
import matplotlib.pyplot as plot

X = numpy.linspace(-3, 2, 30) # -3���� 2���� ������ ������ 100��
Y = X ** 2 - 2 * X + 1.
Z = X ** 3 - 10 * X - 5

plot.plot(X, Y, '.b-')
plot.plot(X, Z, 'xr')  # ���� x�� ��ŷ�ϰ� �̾� �ִ� �۾��� ����.
plot.show()
