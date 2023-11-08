#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     "착하게 살지 말자."
# Author:      Cho
# Created:     2021-05-03
#-------------------------------------------------------------------------------


def is_float( Fstring ) :
    try:
        result = float( Fstring ) # i를 float로 바꾸려고 함
    except:
        result= None

    return( result )

Nlist=[ "45", "67.456", "Summer", 0.005, "adn345"]


for w in Nlist :
    print( is_float( w ) )