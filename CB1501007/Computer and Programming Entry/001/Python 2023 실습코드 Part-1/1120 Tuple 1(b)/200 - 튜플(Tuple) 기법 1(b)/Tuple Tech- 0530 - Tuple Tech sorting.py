#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------

la =[ 3, 4, 5, 6, 7, 8, 9]
lb =[ 4, 5, 6, 7, 8, 9, 3]
lc =[ 9, 3, 1, 5, 7, 5, 2]

ltuple=[]
for a,b,c in zip( la, lb, lc ):
    w = (a,b,c)
    ltuple.append(w)
    print( w )


ltuple.sort(reverse=True )
print( "After Reversing =", ltuple )

ltuple.sort( )
print( "After Sorting[0]=", ltuple )


ltuple.sort(key = lambda element : element[1] )
print( "After Sorting[1]=", ltuple )

