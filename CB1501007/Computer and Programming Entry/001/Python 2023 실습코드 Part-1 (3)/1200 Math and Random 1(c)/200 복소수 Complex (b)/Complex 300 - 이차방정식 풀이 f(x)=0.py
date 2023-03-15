#-------------------------------------------------------------------------------
# Purpose:     2022 Zoh's Work     "過猶不及" 메롱..
# Author:      Cho
# Created:     2022-03-25
#-------------------------------------------------------------------------------


Quad=(4, -3, 5) # f(x)=4x**2 -3*x + 5

import math

def Qsol(a, b, c):
    D =  b**2 - 4*a*c

    if D < 0 : # 허근
        hu = math.sqrt(-D)
        isola = complex(-b/2*a,  hu/2*a )
        isolb = complex(-b/2*a,  -hu/2*a )
        return(isola, isolb)

    if D == 0 :
        return( -b/2*a)


    if D > 0 : # 실근
        hu = math.sqrt(D)
        isola = (-b+ hu)/(2*a)
        isolb = (-b- hu)/(2*a)
        return(isola, isolb)


Prob=[ (2, 3, 1), (1, 2, 1), (1, -5, 6), (7,3, -3), (1,1,1)]

for w in Prob :
    a=w[0]; b=w[1] ; c=w[2]
    roots = Qsol(a,b,c)
    print(f" 입력={w}, 결과={roots}" )




