#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-04-27
#-------------------------------------------------------------------------------


import numpy as np

p = np.poly1d([1, -6, 8])
x = 5
equation1 = np.polyval(p, x)  # f(x=5)

# x를 5x+5를 넣어봄
equation2 = np.polyval([1, -6, 8], np.poly1d([x, x]))

# x에 x^2 -x + 1을 넣어봄
equation3 = np.polyval([1, -6, 8], np.poly1d([1,-1,1]))
print(equation1)
print(equation2)
print(equation3)



