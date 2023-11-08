
import random   # for random

random.seed(14)   # 씨앗(seed)값 설정하기. 시간 정보에 의해 초기화됨
# 사용하지 않을 경우에는 system clock
i = 1
for w in range(10):
    val = random.random( ) # 의사(PSEUDO) 무작위수 [0,1]
    print(f' {i:2} >  {val:8.5f}')
    i += 1