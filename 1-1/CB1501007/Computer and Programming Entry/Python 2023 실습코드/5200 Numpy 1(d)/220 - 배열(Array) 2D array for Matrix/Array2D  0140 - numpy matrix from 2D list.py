#-------------------------------------------------------------------------------
# Purpose:     2022 Zoh's Work     "過猶不及" 메롱..
# Author:      Cho
# Created:     2022-05-24
#-------------------------------------------------------------------------------

import numpy

my="""\
01100010101
10010010000
10001011110
10000101011
00000110110
10100101100
10000101100
01001001001
00111011001
11111101001
11101001111"""

lines=my.split()
n = len(lines)
print(f"행렬의 크기 N={n}")
mynum = numpy.zeros(shape=(n,n))

L=[]
for w in lines :
    L.append( list(w))


mymatrix= numpy.array(L)

print("\n [0] 칼럼")
for w in range(n):
    print(f"(i,0)={(w,0)}, {mymatrix[w][0]}")

print("\n 대각선 성분")
for w in range(n):
    print(f"(i,0)={(w,0)}, {mymatrix[w][0]}")





