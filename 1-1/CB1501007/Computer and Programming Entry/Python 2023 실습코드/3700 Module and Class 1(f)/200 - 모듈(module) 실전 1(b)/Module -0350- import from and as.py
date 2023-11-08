
print(dir())

import os
print(dir())

from os import listdir
print(dir())



import math

mypi = math.pi/2
print("math.sin( )= ",  math.sin( mypi ))

import math as suhak  #내가 사용하기 편한 suhak

print("suhak.cos( )= ", suhak.cos( mypi ))

from math import sin  # math.sin을 붙이지 않아도 된다.
print("sin( )= ", sin(0.3))

