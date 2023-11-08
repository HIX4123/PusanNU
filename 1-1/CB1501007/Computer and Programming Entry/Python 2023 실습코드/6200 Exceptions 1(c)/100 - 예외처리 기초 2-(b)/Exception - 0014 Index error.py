"""

1. python ValueError
2. python IndexError
3. python SyntaxError
4. python NameError
5. python ZeroDivisionError
6. python FileNotFoundError
7. python TypeError
8. python AttributeError
9. python KeyError
10. python OverFlowError
11. 기타 에러들은 어디서 보는가

"""

arr = ['a', 'b', 'c', 'd', 'e']
x = arr[50]


a = 1
b = 2

print(c) # Name Error

a = 1 + "abc"   # type error

# Attribute Error
import math # 정상 접근
a = math.ceil(1.2)
print(a) # math ceil2 라는 메서드는 없습니다.
b = math.ceil2(1.2)
print(b)


d = {"a": 12, "b": 33} # KeyError 없는 키값에 접근
result = d["z"]