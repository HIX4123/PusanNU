#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2020-02-29
#-------------------------------------------------------------------------------

import sys

md={}
md["good"]=1234

La = [ True , 'a', 100, "summer", "summer-time", 3.145, 31.1456789, [], [4], [4,5],\
      [4,5,6], [4,5,6,7], [[]], 2+3j,  "대", "대한", "대한뽕", \
      (2,3), md, range(500) ]

for w in La :
    print(  type(w), ": ",  sys.getsizeof(w), "  ", w )