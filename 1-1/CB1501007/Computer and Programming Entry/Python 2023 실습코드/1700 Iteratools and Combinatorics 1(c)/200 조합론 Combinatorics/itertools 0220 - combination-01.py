#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2019-10-07
#-------------------------------------------------------------------------------

import itertools

chars = sorted(list("banana")) ;
print("chars  =", chars )


c = itertools.combinations(chars, 4)  # 조합

for word in c :
    print( word )