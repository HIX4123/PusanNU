import numpy as np

# curve-fit() function imported from scipy
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt


x = np.linspace(0, 1, num = 40)
y = 3.45 * np.exp(1.334 * x) + np.random.normal(size = 40)

def test(x, a, b):  # model we made for fitting
    return a*np.exp(b*x)

# curve_fit() function takes the test-function
# x-data and y-data as argument and returns
# the coefficients a and b in param and
# the estimated covariance of param in param_cov
param, param_cov = curve_fit(test, x, y)


print("param a =", param[0] )
print("param b =", param[1] )
print("Covariance of coefficients: param_cov =", param_cov)


# ans stores the new y-data according to
# the coefficients given by curve-fit() function
ans = (param[0]*(np.exp(param[1]*x)))


plt.plot(x, y, 'o', color ='red', label ="data")
plt.plot(x, ans, '--', color ='blue', label ="optimized data")
plt.legend()
plt.show()


