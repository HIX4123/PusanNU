#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     롯데 만만세
# Author:      Cho
# Created:     2021-04-02
#-------------------------------------------------------------------------------

from itertools import cycle

yoil= list("월화수목금토일")

pool = cycle( yoil )

i=0
for w in pool :
    i += 1
    if i > 20 : break
    print(w)


while(i<50) :
    print(i, next(pool))
    i += 1

