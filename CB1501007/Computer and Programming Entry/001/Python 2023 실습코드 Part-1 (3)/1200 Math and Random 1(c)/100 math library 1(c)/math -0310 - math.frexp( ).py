#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-05-14
#-------------------------------------------------------------------------------


"""
It returns mantissa and exponent as a pair (m, e) of
a given value x, where mantissa m is a floating point
number and e exponent is an integer value.
m is a float and e is an integer such that

x == m * 2**e exactly.

If x is zero, returns (0.0, 0), otherwise 0.5 <= abs(m)
 < 1. This is used to “pick apart” the internal
 representation of a float in a portable way.
"""

import math


lst = [1024.0, 13.76, 17.5, 21,-15.85, -41.24, -11.2, 54]

for w in lst :
    print(f'{w:10.3f}, {math.frexp(w)}')

