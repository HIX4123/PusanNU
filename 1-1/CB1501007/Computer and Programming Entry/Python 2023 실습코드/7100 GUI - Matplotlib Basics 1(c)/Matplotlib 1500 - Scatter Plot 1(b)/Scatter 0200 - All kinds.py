import matplotlib.pyplot as plt
import numpy as np


X = np.arange(20)
Y = np.random.randint(0, 20, 20)
S = np.abs(np.random.randn(20))*100
C = np.random.randint(0, 20, 20)


scatter = plt.scatter(X, Y, s=S, c=C, label='A')


plt.xlim(X[0]-1, X[-1]+1)
plt.ylim(np.min(Y-1), np.max(Y+1))


plt.title('scatter', pad=10)
plt.xlabel('X axis', labelpad=10)
plt.ylabel('Y axis', labelpad=10)


plt.xticks(np.linspace(X[0], X[-1], 11))
plt.yticks(np.linspace(np.min(np.append(Y, Y)), np.max(np.append(Y, Y)), 11))
plt.minorticks_on()
plt.tick_params(axis='both', which='both', direction='in', pad=8, top=True, right=True)


plt.show()