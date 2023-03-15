#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2020-01-17
#-------------------------------------------------------------------------------

import math

fa=0.12345678912345
fb=fa*fa
print("fb=   ",fb)
print("fb= %45.40f" %fb)
print("fb= %75.70f" %fb)

print("60!=", math.factorial(60))

import fractions

a = fractions.Fraction(5,11)
b = fractions.Fraction(11,13)
c = a*b
print(a,b)
print(c)       # (5/11)*(11/13)
print("c= %10.8f"%c)
print("c= %34.30f"%c)
