#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-05-14
#-------------------------------------------------------------------------------


import random

def wegchoice( Popu, Weight ) :
    if len( Popu ) != len( Weight) :
        print("error, diff size "); return()

    ans = random.choices( Popu, Weight)
    return( ans )



P = list("도개걸윷모")
W = [ 0.2, 0.27, 0.23, 0.19, 0.11]
W = [ 20, 27, 23, 19, 11]
W = [ 20,  4,  3,  2,  1]

for w in range( 1, 21 ) :
    print( f'{w:3d} >  {wegchoice ( P, W )}' )

