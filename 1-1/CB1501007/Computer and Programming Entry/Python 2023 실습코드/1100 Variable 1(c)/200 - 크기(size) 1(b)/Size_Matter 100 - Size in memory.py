#-------------------------------------------------------------------------------
# Purpose:     2020 Prof. Zoh's Work
# Author:      Cho
# Created:     2020-09-05
#-------------------------------------------------------------------------------

import sys

def foo() :
    return

D=[ 1, 23.34, "G", "Go", [ ], [1], True, foo ]

for w in D :
    print( f'{w}, size= {sys.getsizeof(w)}' )