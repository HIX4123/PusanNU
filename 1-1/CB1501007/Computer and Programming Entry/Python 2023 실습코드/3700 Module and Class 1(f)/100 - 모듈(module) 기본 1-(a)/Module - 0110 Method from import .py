

# 봐라. 아래에 사용되는 sqrt는 math에서 가져온 것이다.

#from math import sqrt, pi
import math

def sqrt(a):
    return(a*a)

for w in range(10) :
    print( f'{w}의 제곱근은 {math.sqrt(w):7.4f}')

for w in range(10) :
    print( f'원주율 pi*{w}= {math.pi*(w):7.4f}')