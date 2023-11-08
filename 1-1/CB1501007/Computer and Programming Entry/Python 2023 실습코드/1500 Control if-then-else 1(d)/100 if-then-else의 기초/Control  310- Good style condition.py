#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     "착하게 살지 말자."
# Author:      Cho
# Created:     2021-05-03
#-------------------------------------------------------------------------------

a,b,c,d=1,2,3,4


cond1 =  (a<b) and (c**2 - 3 > a) or (d*2+c < a*b)
cond2 =  (b**2 - 2) < (a+b*c-3) or ( d**2 + c**2 > 100)


def do_this( ) :
    print("\n In do_this( )")

def do_that( ) :
    print("\n In do_that( )")

if cond1 and cond2:
    do_this( )
else :
    do_that( )


