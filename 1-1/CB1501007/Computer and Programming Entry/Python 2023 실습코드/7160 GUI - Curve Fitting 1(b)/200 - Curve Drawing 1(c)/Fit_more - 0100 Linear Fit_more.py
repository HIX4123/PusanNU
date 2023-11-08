
import numpy as np
from scipy.optimize import curve_fit


def func(x, a, b):  # f(x) = ax + b를 리턴합니다.
    return a*x + b

x = np.linspace(0, 10, 100) #0에서 10까지 100개의 구간으로 나눕니다.
print("data point x =", x)

y = func(x, 1, 2)
print("function f(x) =",y)

np.random.seed(1)
yn = y + 1.4*np.random.normal(size=len(x))  # Noise를 넣어서  y 값을 만듬
print(yn)

popt, pcov = curve_fit(func, x, yn)
print("popt=", popt) #popt는 주어진 func 모델에서 가장 최고의 fit values를 보여줍니다.
# [ 1.02977602  1.90564447]
print("pcov=", pcov) #pcov의 대각성분들은 각 parameter들의 variances 입니다.
# [[ 0.00075267 -0.00376335]  [-0.00376335  0.02521572]]

import matplotlib.pyplot as plt
plt.figure(figsize=(8, 6))
plt.scatter(x, yn, marker='.', color='gray')
plt.plot(x, y, linewidth=2, color='green')
plt.plot(x, func(x, *popt), color='red', linewidth=2)
plt.legend(['Original', 'Best Fit'], loc='best')
plt.show()

