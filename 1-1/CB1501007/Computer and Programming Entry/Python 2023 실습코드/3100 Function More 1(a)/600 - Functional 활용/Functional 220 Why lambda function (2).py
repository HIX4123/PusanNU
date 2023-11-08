#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2019-08-31
#-------------------------------------------------------------------------------

def plus_ten(x):
    return x + 10

print("type(plus_ten)= ", type(plus_ten))
print("plus_ten(1)=", plus_ten(1) )


plus_ten2 = lambda x: x + 100
print("type(plus_ten2)= ", type(plus_ten2))
print("plus_ten2(1) = ", plus_ten2(1) )


w =  ( lambda x: x%20 )( 132 )
print("w=", w)

myl = list( map(plus_ten, [1, 2, 3]))
yourl = list( map(  lambda x: x*(-11) , [1, 2, 3, 4, 5]))
print("myl= ", myl)
print("yourl= ", yourl)

"""
람다 표현식 안에서 조건부 표현식 if, else를 사용할 때는
:(콜론)을 붙이지 않는다.
일반적인 if, else와 문법이 다르므로 주의해야 한다.
조건부 표현식은 식1 if 조건식 else 식2 형식으로 사용하며
식1은 조건식이 참일 때, 식2는 조건식이 거짓일 때 사용할 식이다.

특히 람다 표현식에서 if를 사용했다면 반드시 else를  사용해야 한다.
다음과 같이 if만 사용하면 문법 에러가 발생하므로 주의해야 한다.


>>> list(map(lambda x: str(x) if x % 3 == 0, a))
>>> SyntaxError: invalid syntax

"""
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
wl = list( map(lambda x: str(x) if x % 3 == 0 else x, a))
print("wl= ", wl )

a = [ 1, 2, 3, 4,  5]
b = [ 2, 4, 6, 8, 10]
wwl = list(map(lambda x, y: x * y, a, b))
print("wwl= ", wwl )