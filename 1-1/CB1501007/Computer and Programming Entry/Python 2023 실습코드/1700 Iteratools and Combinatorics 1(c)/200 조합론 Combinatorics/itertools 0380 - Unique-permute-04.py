#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2019-10-07
#-------------------------------------------------------------------------------

from itertools import permutations

def unique_permutations(iterable, r=None):
    previous = tuple()
    for p in permutations(sorted(iterable), r):
        if p > previous:
            previous = p
            yield p

count=0
this = 'banana'
this = 'pizza'
for p in unique_permutations(this):
    word =   "".join(p)
    count += 1
    print ( "%3d : %10s" % ( count, word) )
    if word == this : print("*********")
