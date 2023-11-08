# -------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-04-27
# -------------------------------------------------------------------------------

import numpy as np

equation1 = np.poly1d([1, 2, -1, 4], True, variable="a")
    d
equation2 = np.poly1d([1, 0, -1], True)
# True이면 root로 사용 즉 (x-1)(x)(x11)

equation3 = np.poly1d([3, 0, 1, 2], False)
# False면 계수로 사용함.

print(equation1)
print(equation2)
print(equation3)
