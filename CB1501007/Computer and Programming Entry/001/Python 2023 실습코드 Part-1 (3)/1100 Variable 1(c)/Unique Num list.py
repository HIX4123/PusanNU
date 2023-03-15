#-------------------------------------------------------------------------------
# Name:        module1
# Author:      algor
# Created:     16-03-2022
#-------------------------------------------------------------------------------
import random

N= 30
gap = 50
start= 1000
Num=[]
for w in range(N):
    jump = random.randrange(gap, 3*gap)
    start = start + jump
    Num.append(start)


random.shuffle( Num )
print(Num)
