#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------

import itertools


def createGenerator():
    mylist = range(10)
    for i in mylist:
        yield i*i

mygenerator = createGenerator() # create a generator
print(mygenerator) # mygenerator is an object!

for i,w in enumerate(mygenerator):
    print(f"i={i:3}, w={w:5}")


def createPermutator(L):
    mylist = itertools.permutations(L)
    for i in mylist:
        yield i

L=[1,2,3,-1,-2,-3]
mygenerator = createPermutator(L)
print(mygenerator) # mygenerator is an object!

for i,w in enumerate(mygenerator):
    print(f"i={i:3}, w={w}")


print(f">> {next(createPermutator(L)) }")
print(f">> {next(createPermutator(L)) }")
print(f">> {next(createPermutator(L)) }")
print(f">> {next(createPermutator(L)) }")