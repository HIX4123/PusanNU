#-------------------------------------------------------------------------------
# Purpose:     2020 Prof. Zoh's Work
# Author:      Cho
# Created:     2020-10-16
#-------------------------------------------------------------------------------

L = [ '34', '56.7', 'good', "500", '45summer' ]


def check_int( NumberString ) :
    if NumberString.isdigit():
        Number = int(NumberString)
    else: return( NumberString )

    return( Number )


for w in L :
    w = check_int( w )
    print(f' type(w)={type(w)}, w={w}' )


