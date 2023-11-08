#-------------------------------------------------------------------------------
# Purpose:     2020 Prof. Zoh's Work
# Author:      Cho
# Created:     2020-10-15
#-------------------------------------------------------------------------------


def fun1( myList ) :
    X= myList
    X.append( -L[0] )
    X.append( -L[1] )
    X.append( -L[2] )
    return(X)



L = [ 1, 2, 3 ]
W = fun1(L)
print( f'1> L[]={L}, \n   W[]={W}')

W.pop(0)
W.pop(0)

print( f'2> L[]={L}, \n   W[]={W}')
