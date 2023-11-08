#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-05-15
#-------------------------------------------------------------------------------

import random

random.seed( 1245 )
N = 5000000

def inout(x,y) :
    if x**2 + y**2 <= 1.0 : return(1)
    else : return(0)


inpoint = 0
for w in range( N ) :
    x = random.random()
    y = random.random()
    #if w % 4000 == 0 :
    #    print(f'[{w:6}]==>  {x:6.5f}   {y:6.5f}  INOUT- {inout(x,y)}')
    if inout(x,y) == 1 : inpoint += 1


expi = 4*inpoint/N
print(f' N={N}, 원안의 점{inpoint}, 파이={expi}')
