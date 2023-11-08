#-*- coding: cp949 -*-
#-------------------------------------------------------------------------------
# Purpose:     2018 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------

it = iter(list(range(3)))
print(next(it))
print(next(it))
print(next(it))

print("next( ) with default value")
it = iter(list(range(3)))
print(next(it, 10))
print(next(it, 10))
print(next(it, 10))
print(next(it, 10))
print(next(it, 10))
print(next(it, 10))


