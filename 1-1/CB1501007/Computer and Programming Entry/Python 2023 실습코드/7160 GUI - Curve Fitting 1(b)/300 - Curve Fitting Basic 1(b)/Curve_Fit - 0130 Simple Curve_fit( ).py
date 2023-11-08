# 미지의 함수를 이용해서 데이터를 fitting 한다.
# 그 목적은 사용하지 않은 x값에 대하여 f(x)를 추정하는 것이다.

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(x, a, b, c ):
     return a  / b**x + c  #f(x)= a / b**x + c


# Define the data to be fit with some noise:
np.random.seed(1729)
xdata = np.linspace(4, 14, 10) #
xreal = np.linspace(4, 14, 20)
y     = func( xdata, 1.2 , 2.0, 1)

Nscale = 0.007 # 노이즈를 조정하는 변수

y_noise = Nscale * np.random.normal(size=xdata.size)
ydata   = y  + y_noise
plt.plot(xdata, ydata, 'bo', label='data', alpha=0.5)


# Fit for the parameters a, b, c of the function func:
popt, pcov = curve_fit(func, xdata, ydata)
print("popt 1=", popt)

plt.plot(xreal, func(xreal, *popt), 'r-', \
          label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))


plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

