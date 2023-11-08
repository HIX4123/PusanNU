#-------------------------------------------------------------------------------
# Purpose:     2022 Zoh's Work     "過猶不及" 메롱..
# Author:      Cho
# Created:     2022-04-07
#-------------------------------------------------------------------------------

import random

def inout(x,y):
    if (x**2 + y**2 <= 1) and (x-1)**2 + y**2 >= 1  :  return( True )
    else :                 return( False)

#random.seed( 101 ) # 무작위수 씨앗을 고정.
N = 10000000
C=0
for i,w in enumerate( range(N) ) :
    if i %500000 == 0 :
        print(" * ", i)
    x = random.random( ) #[0,1] 무작위수
    y = random.random( ) #[0,1] 무작위수
    if inout(x,y) : C+= 1


print(f"C/N={C/N}")
