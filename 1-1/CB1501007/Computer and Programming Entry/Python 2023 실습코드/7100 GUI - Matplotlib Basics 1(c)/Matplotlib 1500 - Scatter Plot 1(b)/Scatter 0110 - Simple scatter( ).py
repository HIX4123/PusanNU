import numpy as np
import matplotlib.pyplot as plt


data1=[5, 9, 11, -3, 7, -3, 13, 2,  8]
data2=[9, 11, 3, 6, -3, 13, 5,  8, 9]
plt.figure()

plt.scatter(data1, data2, s=53, c="red", alpha=0.5,  label='Inline label' )
plt.xlim([-10,30])
plt.ylim([-10,30])
#plt.autoscale(enable=True, axis='y')

plt.legend()
plt.show()


