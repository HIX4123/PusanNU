#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2021-03-20
#-------------------------------------------------------------------------------



from scipy.optimize import curve_fit
import scipy
import numpy as np

def fn(x, a, b, c): # fitting할 모형함수
    return a + b*x[0] + c*x[1]


def gn(x, a, b, c): # fitting할 모형함수
    return a * b*x[0] + c*x[1]**2

x = scipy.array([[ 0,  1,  2,  3, 4,   6,  8,   9,  12,],\
                 [ 1,  3,  4,  5, 6,   1,  2,   3,   4 ]])
y = scipy.array( [ 2, 14, 26, 31, 42, 72, 82, 100, 114 ])

print("\n fn( ) 함수로 fitting")
popt, pcov = curve_fit(fn, x, y)
print ( "\n popt= \n", popt )
print ( "\n pcov= \n", pcov )
print ( "\n 오차 표준편차 \n", np.sqrt(np.diag(pcov)))


print("\n gn( ) 함수로 fitting")
popt, pcov = curve_fit(gn, x, y)
print ( "\n popt= \n", popt )
print ( "\n pcov= \n", pcov )



"""
Returns:
popt : array
    Optimal values for the parameters so that the sum
    of the squared error of f(xdata, *popt) -
    ydata is minimized

pcov : 2d array
    The estimated covariance of popt. The diagonals provide the variance
    of the parameter estimate. To compute one standard deviation errors on
    the parameters use perr = np.sqrt(np.diag(pcov)).
    How the sigma parameter affects the estimated covariance depends on
    absolute_sigma argument, as described above.
"""