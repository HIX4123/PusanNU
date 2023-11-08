#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     "착하게 살지 말자."
# Author:      Cho
# Created:     2021-04-14
#-------------------------------------------------------------------------------

from mytool import xy_point, in_circle

N= 1000000
inner = 0 # 안쪽에 떨어진 점의 수를 기록

for w in range(N) :
    px, py = xy_point()
    if in_circle(px,py) : inner += 1

print("N= ", N )
print("inner= ", inner)
print("PI의 근사값 = ", 4*inner/N )
