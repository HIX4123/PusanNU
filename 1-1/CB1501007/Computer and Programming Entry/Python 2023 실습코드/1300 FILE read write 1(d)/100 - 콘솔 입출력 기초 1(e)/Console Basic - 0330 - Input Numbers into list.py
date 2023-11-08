#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     롯데 만만세
# Author:      Cho
# Created:     2021-03-18
#-------------------------------------------------------------------------------

import sys


print(" 입력 라인수 n을 입력하시오: " )

n = int( sys.stdin.readline())
data = []
for i in range(n):
    print(n-i, "줄 남았습니다" )
    data.append(list(map(int,sys.stdin.readline().split())))


print("\n 입력 리스트= " )

for w in data :
    print(w)