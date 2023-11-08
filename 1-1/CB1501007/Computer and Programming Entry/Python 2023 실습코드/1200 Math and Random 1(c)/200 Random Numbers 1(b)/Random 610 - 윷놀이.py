#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-05-14
#-------------------------------------------------------------------------------

import random

def yut1():
    pan= [ '도', '개', '걸', '윷', '모']
    return   random.choice(pan)

def draw_yut(): # 윷가락 1개만 던짐
    rval = random.random() # [0,1]
    if rval <= 0.53 : return ("UP")
    else : return( "DOWN" )

def yut_real( ) :
    yut_all=[]
    for w in range(4) :
        yut_all.append( draw_yut() )

    yut_name=["모", "또", "개", "걸", "윷"]
    return( yut_name[ yut_all.count("UP") ]  )



i=1
for w in range(50) :
    print( f'{i:3}:  {yut_real()}' )
    i += 1