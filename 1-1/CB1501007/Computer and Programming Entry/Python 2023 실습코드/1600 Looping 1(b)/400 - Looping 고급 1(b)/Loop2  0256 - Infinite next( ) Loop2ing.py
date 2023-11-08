#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     롯데 만만세
# Author:      Cho
# Created:     2021-04-02
#-------------------------------------------------------------------------------

from itertools import cycle

yoil= list("월화수목금토일")

pool = cycle( yoil )

i=0

while(i<50) :
    print( f'{i:3}= {next(pool)}')
    i += 1

