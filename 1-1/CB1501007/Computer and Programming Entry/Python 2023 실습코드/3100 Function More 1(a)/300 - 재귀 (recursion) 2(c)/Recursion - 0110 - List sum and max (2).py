#-------------------------------------------------------------------------------
# Purpose:     2022 Zoh's Work     "過猶不及" 메롱..
# Author:      Cho
# Created:     2022-04-07
#-------------------------------------------------------------------------------


def Lsum( L ):
    if len(L) == 1 :
        return( L[0] )
    elem = L[0]
    psum = Lsum( L[1:])
    return( elem + psum )


def Lmax( L ) :
    if len(L) == 1 :
        return( L[0] )
    first = L[0]
    other = Lmax( L[1:])
    return( max(first, other) )

def Lsecond(L): # 과제물
    return

W=[1, 2, 13, 4, 5, 6, 17, 8, 9, 10 ]

print( Lsum(W))
print( Lmax(W))