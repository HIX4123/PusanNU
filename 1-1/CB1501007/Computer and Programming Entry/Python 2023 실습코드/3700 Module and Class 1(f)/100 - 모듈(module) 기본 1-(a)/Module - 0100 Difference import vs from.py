#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     "착하게 살지 말자."
# Author:      Cho
# Created:     2021-10-19
#-------------------------------------------------------------------------------
"""
import X
X.this( D ) 로 사용하는 것 보다

from X import this
this( D )로 사용하는 것에 메모리 면에서 유리하다.
"""

import random

for w in range(10):
    print(f' random w = {random.randint(0,101)}')




from random import randint

for w in range(10):
    print(f' random w = {randint(100,201)}')


