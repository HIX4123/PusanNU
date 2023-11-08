# 미지의 함수를 이용해서 데이터를 fitting 한다.
# 그 목적은 사용하지 않은 x값에 대하여 f(x)를 추정하는 것이다.

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(x, a, b, c ):
     return a  / b**x + c  #f(x)= a / b**x + c


# Define the data to be fit with some noise:
xdata = [ 2,        3,    5,    6,   8,  10,  11, 12]
ydata = [ 10000, 6500, 4300, 2411, 560, 200, 123, 34]
xreal = np.linspace(2, 12, 40)


plt.plot(xdata, ydata, 'bo', label='data', alpha=0.5) # 점 찍기


# 목표 함수의 미지수 a,b,c를 계산한다. fitting 작업

popt, pcov = curve_fit(func, xdata, ydata)
print("예측한 계수값은 popt=", popt)

# 예측한 커브를 그려서 맞추어 봄
plt.plot(xreal, func(xreal, *popt), 'r-', \
          label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))


plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

