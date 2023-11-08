
import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3,  8, 9]
y = [3, 5, 7, 10, 11]

fit_1 = np.polyfit(x,y,1)  # 1차로 mapping 함. 결과는 2개의 실수(기울기와 절편)
print("Linear Fitted data = ", fit_1)
fit_fn1 = np.poly1d(fit_1)
# fit_fn is now a function which takes in x and returns an estimate for y


plt.plot(x,y, 'ro')

nx = np.linspace(1,15,30)
plt.plot(nx, fit_fn1(nx), '--k')

plt.xlim(0, 12)
plt.ylim(0, 15)
plt.show( )