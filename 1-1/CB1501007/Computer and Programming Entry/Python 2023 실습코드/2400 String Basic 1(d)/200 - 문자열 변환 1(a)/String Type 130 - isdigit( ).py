#-------------------------------------------------------------------------------
# Purpose:     2020 Prof. Zoh's Work
# Author:      Cho
# Created:     2020-10-16
#-------------------------------------------------------------------------------

L = [ '34', '56.7', 'good', "500", '45summer' ]



for w in L :
    if w.isdigit( ) :
        vali = int(w)
        valf = float(w)
        print( f' w={w}, vali={vali}   valf={valf}')