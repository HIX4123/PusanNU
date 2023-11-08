
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


def func(X, a, b, c):
    x,y = X
    return np.log(a) + b*np.log(x) + c*np.log(y)

# some artificially noisy data to fit
x = np.linspace(0.1, 1.1,   30)
y = np.linspace(1.,   2.,   30)
a, b, c = 10., 4., 6.
z = func((x,y), a, b, c) * 1 + np.random.random()*10

# initial guesses for a,b,c:
p0 = 8., 2., 7.
print ( curve_fit(func, (x,y), z, p0) )

plt.plot(x,z, 'ro') #, x, fit_fn1(x), '--k')
plt.xlim(0, 1.5)
plt.show( )