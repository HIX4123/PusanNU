# 미지의 함수를 이용해서 데이터를 fitting 한다.
# 그 목적은 사용하지 않은 x값에 대하여 f(x)를 추정하는 것이다.

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(x, a, b, c ):
     #return a  / b**x + c  #f(x)= a / b**x + c
    return a * ( b / x ) ** c

def func2(x, a, b, c):
    return a * ( np.exp(1) ) ** (-b * x + c)

def func3(x, a, b, c):
    return a * ( 1 / x ) ** b

# Define the data to be fit with some noise:
xdata    = [     1,    2,   3,   4,  5,  6,  7, 8, 9, 10, 11 ]
yseoul   = [ 11785, 1563, 426, 117, 37, 28, 12, 2, 3,  4, 0  ] # 서울시
yincheon = [  7375,  595, 106,  34, 13,  9,  2, 3, 2,  2, 0  ]
ypusan   = [  7376,  713, 140,  32, 14,  3,  2, 1, 0,  0, 0  ]
xreal    = np.linspace(1, 12, 40) # 2부터 12까지 40개 구간을 만들어 커브 그릴 때 사용

ydata = yseoul
plt.plot(xdata, ydata, 'bo', label='Pusan', alpha=0.5)

# 목표 함수의 미지수 a,b,c를 계산한다. fitting 작업
# popt, pcov = curve_fit(func, xdata, ydata)
# print("예측한 계수값은 popt=", popt)

# 예측한 커브를 그려서 맞추어 봄
#plt.plot(xreal, func(xreal, *popt), 'r-', label='fit: a=%5.3f, b=%5.3f' % tuple(popt))
popt, pcov = curve_fit(func, xdata, ypusan)
print("예측한 계수값은 popt=", popt)
plt.loglog( xreal, func(xreal, *popt), 'r-', label='fit: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
plt.clf()
