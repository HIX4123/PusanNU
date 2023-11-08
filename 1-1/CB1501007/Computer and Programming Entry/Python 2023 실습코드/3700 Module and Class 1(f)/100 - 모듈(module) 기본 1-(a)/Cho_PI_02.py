# 왜 module을 만들어야 하는가 ?

import mytool

N= 10000000
inner = 0 # 안쪽에 떨어진 점의 수를 기록

for w in range(N) :
    px, py = mytool.xy_point()
    if mytool.in_circle(px,py) : inner += 1

print("N= ", N )
print("inner= ", inner)
print("PI의 근사값 = ", 4*inner/N )
