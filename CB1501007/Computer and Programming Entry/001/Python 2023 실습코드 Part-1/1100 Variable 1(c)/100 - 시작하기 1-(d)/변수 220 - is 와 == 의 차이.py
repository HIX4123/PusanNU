
"""
'is'와 '=='의 차이

is와 ==는 모두 변수의 동등을 비교하지만 다음과 같은 차이점이 있다.

 - is는 변수의 Object(객체)가 같을 때 True를 리턴
 - ==는 변수의 Value(값)이 같을 때 True를 리턴

 동수의 돈 10000원의 가치 == 달수의 돈 10000원의 거치
 동수의 돈 10000원  is not  달수의 돈 10000원
 //돈 자체로는 다른 물건이다.
"""


a = []
b = []
c = a

result = (a is b)
print("a is b ?", result)

result = (a is c)
print("a is c ?", result)

result = (b is c)
print("b is c ?", result)