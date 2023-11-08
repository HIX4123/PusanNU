
import sys

# 클래스 내장 예외 발생
class SquareSeq:
    def __init__(self, n):
        self.n = n

    def __getitem__(self, k):   # 함수 내부에서 특정 범위를 넘을 경우 예외 발생
        if k >= self.n or k < 0 :
            raise IndexError
        return k * k

    def __len__(self):
        return self.n

try :
    squarelist = SquareSeq(10)

    for i in range(0, 15) :
        print(i, "=", squarelist[i])
except IndexError :
    print("Index Error Raise")

print()

# Exception 내부 변수 알아보기
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))     # the exception instance
    print(inst.args)      # arguments stored in .args
    print(inst)           # __str__ allows args to printed directly
    x, y = inst.args
    print('x =', x)
    print('y =', y)

print()

# Dictionary를 활용한 예외처리 예제
family = {'father':'john','mother':'mary','sister':'jene'}

def checkFamily(value, dic) :   # Dictionary에 찾고자 하는 이름이 있는지 검색
    if value in dic :
        print('You are my family')
    else :                      # 찾는 이름이 없을 경우 예외 발생
        raise Exception

try :
    checkFamily('Tom', family)
except Exception :
    print('You are not my family')