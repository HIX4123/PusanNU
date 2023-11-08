
import numpy as np
import matplotlib.pyplot as plt
#matplotlib inline

t = np.arange(0, 10, 0.01)
y = 3*t + 5
y_noise = y + np.random.randn(len(y))

fp1 = np.polyfit(t, y_noise, 1)
f1 = np.poly1d(fp1)
print(f1)
print(fp1)


plt.figure(figsize=(9,6))
plt.plot(t, y_noise)
plt.plot(t, y, "tomato")
plt.show()

##
##plt.figure(figsize=(12,8))
##plt.plot(t, y)
##plt.show()
##
##plt.figure(figsize=(12,8))
##plt.plot(t, y_noise, label='noise', color='y')
##plt.plot(t, y, ls='dashed', lw=3, color='b', label='original')
##plt.plot(t, f1(t), lw=2, color='r', label='polyfit')
##plt.grid()
##plt.legend()
##plt.show()