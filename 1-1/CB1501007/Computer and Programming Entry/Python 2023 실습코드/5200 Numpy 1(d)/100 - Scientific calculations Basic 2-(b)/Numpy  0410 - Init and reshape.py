
import numpy as np
#import numpy
#from numpy import *


# basic create
a= np.arange(10).reshape(2,5)
print("실험 1: ", a)
a = np.array([(2.1, 3, 4), (3.1, 4.5, 1)])
print("실험 2: ", a)
# a=np.array(1,2,3,4,)    #Wrong Syntex
a=  np.array([1,2,3,4])   #RIGHT
print("실험 3: ", a)
print()

#advance create
a= np.zeros((3,3),int)
print("실험 4: ", a)
a= np.ones((3,3),int)
print("실험 5: ", a)
a= np.empty((3,4))
print("실험 6: ", a)
print()

#linspace
a= np.linspace (0,1,9)
print(a)
a= np.linspace (0,np.pi,91) #useful array
print(a)




