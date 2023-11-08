#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------

la =[ 3, 4, 5, 6, 3, 3, 9]
lb =[ 7, 5, 6, 7, 8, 9, 3]
lc =[ 9, 3, 1, 5, 5, 5, 2]

wulist=[]
for a,b,c in zip( la, lb, lc ):
    w = (a,b,c)
    wulist.append(w)

print(f"wulist={wulist}")


wulist.sort(reverse=True )
print( "\n After Reversing =",wulist )

wulist.sort( )
print( "\n After Sorting[0]=",wulist )
for w in wulist :
    print(w)


wulist.sort(key = lambda element : element[1] )
print( "After Sorting[1]=",wulist )

