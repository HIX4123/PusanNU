#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     "착하게 살지 말자."
# Author:      Cho
# Created:     2021-04-14
#-------------------------------------------------------------------------------

import random

def xy_point( ) :           # 무작위 점 생성
    x = random.random( )
    y = random.random( )
    return( x,y )

def in_circle(x,y):         # 점(X,y)가 4분원 안쪽인지의 여부
    if(x*x + y*y)<= 1.0 : return(True )
    else    :             return(False)