#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     "착하게 살지 말자."
# Author:      Cho
# Created:     2021-04-27
#-------------------------------------------------------------------------------

import random

def birth( ) :
    pro = random.random() #[0,1]
    if pro < 0.53 : return("m")
    return( "f" )



def two_boy( ) :
    S=""
    c = 0
    while( True ):
        baby = birth( )
        S += baby
        if baby == "m" : c += 1
        if c >= 2 : break ;
    return(S)

def two_girl( ) :
    S=""
    c = 0
    while( True ):
        baby = birth( )
        S += baby
        if baby == "f" : c += 1
        if c >= 2 : break ;
    return(S)

# 100명의 집안

total = 0
for (i,w) in enumerate( range(100)) :
    bstring =  two_girl()
    print( i, "==>", bstring  )
    total += len( bstring )


print(total/100)
