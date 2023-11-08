#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------

import math
import random

print("\n fun1")
x= [5, 11, 15, 44, 60, 70, 75, 100, 120, 200]
for w in x:
    y= 4* math.sqrt(w + 10) - 10 + random.randrange(-5,5)
    print( "%d  %10.3f" % (w, y))


print("\n fun2")
x= [5, 6, 7, 9, 13, 15, 21, 25, 32, 33]
for w in x:
    y=  - 0.5* w*w + 18 *w + 100 + random.randrange(-10,10)
    print( "%d  %d" % (w, y))


print("\n fun3")
x= [5, 11, 12, 15, 26, 37, 45, 60, 80, 100]
for w in x:
    y =    1500.0/((w-2)*(w-2))
    print( "%d  %10.3f" % (w, y))

print("\n fun4")
x= [5, 11, 12, 15, 26, 37, 45, 60, 70, 72]
for w in x:
    y =   0.05*(w-3)*(w-3) - 10 + random.randrange(-15,15)
    print( "%d  %10.3f" % (w, y))