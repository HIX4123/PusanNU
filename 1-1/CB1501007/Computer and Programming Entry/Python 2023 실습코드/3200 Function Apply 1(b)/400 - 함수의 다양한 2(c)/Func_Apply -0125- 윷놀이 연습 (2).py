#-------------------------------------------------------------------------------
# Purpose:     2022 Zoh's Work     "過猶不及" 메롱..
# Author:      Cho
# Created:     2022-04-05
#-------------------------------------------------------------------------------

import random

def onestick():
    rval = random.random( ) #[0,1]
    if rval < 0.52 : return("Up")
    else :           return("Down")


def yut( ):
    upcount=0
    for i in range(4):
        result=onestick()
        if result == "Up":
            upcount += 1

    yutmal=list("모또게걸윷")
    return( yutmal[ upcount ])


mocount=0
N = 100000
for i,w in enumerate( range( N )):
    R= yut()
    target="모"
    if R == target :
        mocount += 1


print(f"총수 = {N}, T:{target}={mocount}, rate={mocount/N}")
