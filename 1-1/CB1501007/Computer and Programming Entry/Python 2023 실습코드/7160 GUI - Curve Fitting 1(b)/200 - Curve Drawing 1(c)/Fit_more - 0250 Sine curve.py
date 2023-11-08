
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0) # seeding

x_data = np.linspace(-5, 5, num=50)
y_data = 2.9 * np.sin(1.5 * x_data) + np.random.normal(size=50)


import matplotlib.pyplot as plt # And plot it
plt.figure(figsize=(8, 6))
plt.scatter(x_data, y_data)
plt.show()


from scipy import optimize

def test_func(x, a, b):
    return a * np.sin(b * x)

params, params_covariance = optimize.curve_fit\
       (test_func, x_data, y_data, p0=[2, 2])


print(params)
plt.figure(figsize=(8, 6))
plt.scatter(x_data, y_data, label='Data')
plt.plot(x_data, test_func(x_data, params[0], params[1]), color='red', label='Fitted function')
plt.legend(loc='best')

plt.show()
