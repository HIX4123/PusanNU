# 미지의 함수를 이용해서 데이터를 fitting 한다.
# 그 목적은 사용하지 않은 x값에 대하여 f(x)를 추정하는 것이다.

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(x, a, b, c):
     return a * np.exp(-b * x) + c


# Define the data to be fit with some noise:
xdata = np.linspace(0, 4, 50)
y = func(xdata, 2.5, 1.3, 0.5)
np.random.seed(1729)
y_noise = 0.2 * np.random.normal(size=xdata.size)
ydata = y + y_noise
plt.plot(xdata, ydata, 'bo', label='data', alpha=0.5)


# Fit for the parameters a, b, c of the function func:
popt, pcov = curve_fit(func, xdata, ydata)
print("popt 1=", popt)

plt.plot(xdata, func(xdata, *popt), 'r-', \
          label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))


# 변수를 특정 범위로 제한할 수도 있다.
# Constrain the optimization to the region of
# 0 <= a <= 3, 0 <= b <= 1 and 0 <= c <= 0.5:
popt, pcov = curve_fit(func, xdata, ydata, bounds=(0, [3., 1., 0.3]))
print("popt 2 =", popt)
plt.plot(xdata, func(xdata, *popt), 'g--', \
     label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))



plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

