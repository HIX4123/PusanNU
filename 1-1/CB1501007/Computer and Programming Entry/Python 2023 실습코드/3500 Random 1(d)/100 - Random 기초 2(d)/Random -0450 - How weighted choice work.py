#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-05-14
#-------------------------------------------------------------------------------

import numpy as np
import random

yut= list("도개걸윷모")
p  = [10, 15, 14, 7, 5]


def wesam( p ) :
    sp = np.cumsum(p)
    val = random.randint(1, sp[-1])
    #print(sp, val )
    index=0

    for w in sp :
        if val < w : return(index)
        index += 1

    return(index)

for (i,w) in enumerate(list(range(50))) :
    print( f'{i:2}, choice={wesam( p )}' )

