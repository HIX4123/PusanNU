
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


def func(x, a, b, c):  # Gaussian model을 리턴합니다.
    return a*np.exp(-(x-b)**2/(2*c**2))

# 마찬가지로 0~10까지 100개 구간으로 나눈 x를 가지고 noise를 y값으로 추가
x = np.linspace(0, 10, 100)
y = func(x, 1, 5, 2)
yn = y + 0.2*np.random.normal(size=len(x))

## 그런 후에 curve_fit을 하고 best fit model의 결과를 출력합니다.
popt, pcov = curve_fit(func, x, yn)
print(popt) # [ 1.01217827  5.06673512 -2.09600457]
print(pcov)

linestyles = ['-', '--', '-.', ':']

plt.figure(figsize=(8, 6))
plt.scatter(x, yn, marker='.', color='darkgray')
plt.plot(x, y, linewidth=2, color='blue')
plt.plot(x, func(x, *popt), color='red', linestyle=':', linewidth=2)
plt.legend(['Original', 'Best Fit'], loc=2)
plt.show()