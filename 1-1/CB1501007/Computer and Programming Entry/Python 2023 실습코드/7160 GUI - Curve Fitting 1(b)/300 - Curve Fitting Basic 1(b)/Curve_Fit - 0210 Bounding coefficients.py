# fitting할 함수의 계수 범위를 제한할 수 있다.

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def func(x, a, b, c):
    return a * np.exp(-b * x) + c


# Define the data to be fit with some noise:
xdata = np.linspace(0, 4, 50)
y = func(xdata, a=2.5, b=1.3, c=0.5)
plt.figure(figsize=(8, 6))

np.random.seed(1729)
y_noise = 0.2 * np.random.normal(size=xdata.size)
ydata = y + y_noise
plt.plot(xdata, ydata, 'bo', label='data, ae^(-bx)+c')


# Fit for the parameters a, b, c of the function func:
popt, pcov = curve_fit(func, xdata, ydata)

print(popt) # array([ 2.55423706,  1.35190947,  0.47450618])
plt.plot(xdata, func(xdata, *popt), 'r-',\
         label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))

# 계수의 범위를 제한할 수 있다.
# Optimization to the region of 0 <= a <= 3, 0 <= b <= 1 and 0 <= c <= 0.5:
popt, pcov = curve_fit(func, xdata, ydata, bounds=(0, [3., 1., 0.5]))
print(popt) # array([ 2.43708906,  1.        ,  0.35015434])
plt.plot(xdata, func(xdata, *popt), 'g--',\
         label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))


plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

