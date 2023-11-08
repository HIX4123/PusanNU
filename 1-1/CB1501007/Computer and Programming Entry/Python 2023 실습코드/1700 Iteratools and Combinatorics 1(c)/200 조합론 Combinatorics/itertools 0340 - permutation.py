#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2019-10-07
#-------------------------------------------------------------------------------

import itertools
prev=""
mylist = ["a", "a", "b", "n"],
mypermuatation =  itertools.permutations(mylist)
count = 0
for i in list(mypermuatation):
    print(i)
#
    if word != prev :
        count += 1
        if word == 'banana' :
            print("--------------")
        print ( count, ": ", "".join(i))
        prev = word
