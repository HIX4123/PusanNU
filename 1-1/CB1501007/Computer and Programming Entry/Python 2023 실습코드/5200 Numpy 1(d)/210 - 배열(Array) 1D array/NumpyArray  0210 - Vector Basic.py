# -------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
# -------------------------------------------------------------------------------

import math
import numpy as np


a = np.array([5, -2, -3])
b = np.array([3, 5, 6])

print(a + b)
print(0.3 * a - 0.12 * b)
print(a * b)


def turn(d):
    return 1 if d >= 31 else 0


Mon = np.array([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])

LS = [turn(i) for i in Mon]
print(LS)