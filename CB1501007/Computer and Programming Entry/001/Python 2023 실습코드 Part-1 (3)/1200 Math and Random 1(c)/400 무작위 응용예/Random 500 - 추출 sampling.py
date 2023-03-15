#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     "착하게 살지 말자."
# Author:      Cho
# Created:     2021-12-23
#-------------------------------------------------------------------------------

import random

values=[4, 6, 8, 9, 11, 12, 14, 15, 30]

k = random.randint(0,len(values)//2)
choice = random.sample(values, k=k)

print(f'choice[]= {choice}')

