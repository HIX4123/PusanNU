
# https://lmfit.github.io/lmfit-py/model.html

from numpy import exp, linspace, random

def gaussian(x, amp, cen, wid):
     return amp * exp(-(x-cen)**2 / wid)

# We want to use this function to fit to data
# y(x)  represented by the arrays y and x. With scipy.optimize.curve_fit, this would be:

from scipy.optimize import curve_fit
x = linspace(-10, 10, 101)
y = gaussian(x, 2.33, 0.21, 1.51) + random.normal(0, 0.2, len(x))

init_vals = [1, 0, 1]  # for [amp, cen, wid]
best_vals, covar = curve_fit(gaussian, x, y, p0=init_vals)
print(("best_vals=", best_vals)) # [ 2.39499424  0.19942179  1.50909389]

print("Ampltude=", best_vals[0])
print("Center=", best_vals[1])
print("Variance=", best_vals[2])

