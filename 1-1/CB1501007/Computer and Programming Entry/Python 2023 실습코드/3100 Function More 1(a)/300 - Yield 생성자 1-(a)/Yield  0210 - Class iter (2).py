"""
사용자가 정의한 클래스가 이터레이터를 지원하려면
__iter__() 메쏘드(method)를 정의하면 된다.

iter() 는 객체의 __iter__() 메쏘드가 돌려주는 값을 이터레이터로 사용한다.
next() 에 iterator를 전달하면 이터레이터의 __next__() 메쏘드를 호출한다.
이 때문에 사용자가 직접 만드는 이터레이터는 이렇게 구성할 수 있다.
"""


class Range:
     def __init__(self, n):
         self.n = n
         self.c = 0
     def __iter__(self):
         return self # 이터레이터인 경우는 자신을 돌려주면 됩니다.
     def __next__(self):
         if self.c < self.n:
            v = self.c
            self.c += 1
            return v
         else :
            raise StopIteration
     next = __next__



myran = Range(10)

for x in myran :
     print(x)

