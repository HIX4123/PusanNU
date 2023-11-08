#-------------------------------------------------------------------------------
# Purpose:     Zoh's Work     "過猶不及"
#-------------------------------------------------------------------------------

def cmp1(a):
    return( a[1] )

def cmp2(a):
    return( a[0] )

def cmp3(a):
    return( a[0],-a[1] )

ml = [(5,2), (5,4), (4,5), (4,3), (1,4), (3,1), (3,3), (2,3)]

x1 = sorted( ml, key= cmp1 )
x2 = sorted( ml, key= cmp2 )
x3 = sorted( ml, key= cmp3 )
print( x1 )
print( x2 )
print( x3 )