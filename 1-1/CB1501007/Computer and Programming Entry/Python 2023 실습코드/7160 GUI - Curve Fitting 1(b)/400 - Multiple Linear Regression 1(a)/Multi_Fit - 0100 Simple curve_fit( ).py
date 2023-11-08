
import numpy as np
from scipy.optimize import curve_fit

def func(X, a, b, c):
    x,y = X
    return np.log(a) + b*np.log(x) + c*np.log(y)

# some artificially noisy data to fit
x = np.linspace(0.1,1.1,101)
y = np.linspace(1.,2., 101)
a, b, c = 10., 4., 6.
z = func((x,y), a, b, c) * 1 + np.random.random(101) / 100

# a,b,c의 초기값을 넣어주어야 한다.
p0 = 8., 2., 7.
answ =  curve_fit(func, (x,y), z, p0)

for w in answ :
    print(w)

