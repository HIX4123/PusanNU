#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     "착하게 살지 말자."
# Author:      Cho
# Created:     2021-04-30
#-------------------------------------------------------------------------------


L = [ 5, 6, 12, 3, 34, 8, 1]

mymax = -1000  # 김이름
for w in L :
    if w > mymax :
        mymax = w


print( f" mymax= {mymax}")


def recur_max( L ):
    if len(L)<= 1 : # L의 원소가 1개
        return( L[0])
    else :
        lmax = recur_max( L[1:])
        if L[0]> lmax : return(L[0])
        else : return( lmax )


def recur_sum( L ) :
    if len(L)<= 1 : # L의 원소가 1개
        return( L[0])
    else :
        lsum = recur_sum (L[1:]) # 뒤의 줄의 합
        return( lsum + L[0] )

