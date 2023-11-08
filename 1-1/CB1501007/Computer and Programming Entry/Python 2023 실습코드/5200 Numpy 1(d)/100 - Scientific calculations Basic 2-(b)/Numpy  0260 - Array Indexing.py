

import numpy as np
#import numpy
#from numpy import *


a = np.arange(10)*3

print("실험 51", a[3])

print("실험 52", a[2:5])
print("실험 53", a[:7:2]) #index a[0] a[2] a[4] a[6]
print("실험 54", a[::-1]) #reverce

print()


b = np.arange(9).reshape(3,3)

for row in b :
    print("row=", row)