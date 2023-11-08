#--------------------------------------------------------
# Author:      Zoh Que
# Created:     30-01-2023
#--------------------------------------------------------

import itertools

def createPermutator(L):
    mylist = itertools.permutations(L)
    for val in mylist:
        yield val

L=[1,2,3,4,5,-1,-2,-3,-4,-5]
mygen  = createPermutator(L)

for w in range(300):
    print(f"i={w:3}, { next( mygen )}")
