#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2020-04-12
#-------------------------------------------------------------------------------



for w in range(1,10000, 567):
    print(f'{w:07}', f'{w:+7}') # Preferred method, python >= 3.6



import random

for w in range(50):
    val = random.randrange(1,1000) - 500
    print(f' val= {val:+5d}' )