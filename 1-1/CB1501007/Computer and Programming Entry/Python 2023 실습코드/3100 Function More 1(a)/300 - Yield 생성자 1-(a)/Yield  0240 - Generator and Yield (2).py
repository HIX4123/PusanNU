#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------

import itertools


def createGenerator():
    mylist = range(20)
    for i in mylist:
        yield i*i

mygenerator = createGenerator() # create a generator
print(mygenerator) # mygenerator is an object!

for i,w in enumerate(mygenerator):
    print(f"i={i:3}, w={w:5}")
