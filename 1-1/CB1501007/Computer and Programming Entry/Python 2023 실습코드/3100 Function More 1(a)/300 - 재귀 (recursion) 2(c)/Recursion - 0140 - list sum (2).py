#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-05-19
#-------------------------------------------------------------------------------

L = [ 4, 5, 2, 1, 6, 9 , 6]  # L[1:] L[1]부터 끝까지 list


def lsum( L ) :
    mysum = 0
    for w in L :
        mysum += w
    return( mysum )

def recursum( L ) :
    if len(L) == 0 : return(0) # 아주아주 중요함. base 조건
    else : return( L[0] + lsum(L[1:]) )


print( f' lsum(L)= { lsum(L) }')

