#-------------------------------------------------------------------------------
# Purpose:     2020 Prof. Zoh's Work
# Author:      Cho
# Created:     2020-10-16
#-------------------------------------------------------------------------------

L = [ '34', '56.7', 'good', "5.00", '45sum' ]


def check_int_float( NumberString ) :
    if NumberString.isdigit():
        Number = int(NumberString)
    else:
        Number = float(NumberString)

    return( Number )


for w in L :
    if w.isdigit( ) :
        w = check_int_float( w )
        print(f' type(w)={type(w)}, w= {w}, 숫자' )
    else :
        print(f' type(w)={type(w)}, w= {w}' )