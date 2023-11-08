#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------

import random

T=[]
random.seed(2019)

for w in range(10):
    Q=[]
    Q.append( random.randrange(100) )
    Q.append( random.randrange(100) )
    Q.append( random.randrange(100) )
    print("Q=", Q )
    T.append( Q )


print("\n T=", T)


ST = sorted(T)
print("\n ST=", ST)

T.sort()
print("\n After T=", T)