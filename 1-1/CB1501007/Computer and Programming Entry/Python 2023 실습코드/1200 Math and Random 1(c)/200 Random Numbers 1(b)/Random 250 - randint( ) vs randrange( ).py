#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2020-09-17
#-------------------------------------------------------------------------------

#  random.randint( b,e), [b, e], 즉 b와  e 정수가 포함됨.
#  random.randrange(b,e,step) , [b, e] 그리고 step, e가 포함되지 않음
#

import random

print("\n\n random.randint( )", end="")
for w in range(100):
    if w %10 == 0 : print("")
    print( random.randint(1,6), end=" ") # 1과 6을 포함


print("\n\n random.randrange( )", end="")
for w in range(100):
    if w %10 == 0 : print("")
    print( random.randrange(1,6), end=" ")

print("\n\n random.randrange(0,21,2 )", end="")
for w in range(100):
    if w %10 == 0 : print("")
    print( f'{random.randrange(0, 21 ,2):2}', end=" ")