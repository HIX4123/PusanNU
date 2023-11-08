
import string

a = '345.789'

b = float(a)
print(a, b)
print(a+"10", b+10)


x = '567'
y = int(x)
print(y)

# 만일 str 오류가 나면 >del str
# 따라서 함수 이름을 변수로 쓰면 좋지 않다.
# 예상하지 못하는 오류가 발생한다.

z = str( 345.789)
print("str( 345.789 )=", z)

w = float(z)* 100.0
print("w=", w)