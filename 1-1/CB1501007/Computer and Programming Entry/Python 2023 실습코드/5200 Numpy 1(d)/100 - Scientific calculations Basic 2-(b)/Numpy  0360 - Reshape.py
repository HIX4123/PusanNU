
import numpy as np
#import numpy
#from numpy import *



a = np.array( [20,30,40,50] )
b = np.arange( 4 )
c = a-b
print("실험 0: ", "a=", a, "b=", b, "c=", c)

print("실험 1: ", c)
print("실험 2: ", b**2)
print("실험 3: ", 10*np.sin(a))
print("실험 4: ", a<35)

print()


a = np.arange(2,9, 2).reshape(2,2)
b = np.arange( 4 ).reshape(2,2)

print("실험 4.2: ", "a=", a)
print("실험 4.3: ", "b=", b)
print("실험 5:a+b \n",a+b)
print("실험 6:a*b \n",a*b)
print("실험 7:a DOT b \n",np.dot(a,b))


