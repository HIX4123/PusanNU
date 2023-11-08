#-------------------------------------------------------------------------------
# Name:        module1
# Author:      algor
# Created:     13-03-2022
#-------------------------------------------------------------------------------

try:
    for i in range(100):
        for j in range(1000):
            for k in range(10000):
               if i + j + k == 777:
                  raise Exception
except Exception:
    print( i, j, k)