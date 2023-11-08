

# 사용자 정의 예외 처리
class Big(Exception) :
    pass

class Small(Big) :      # 정의한 예외 클래스를 상속 받는 클래스 선언
    pass

def raiseBig() :        # Big 클래스 예외 호출
    x = Big()
    raise x

try :
    raiseBig()
except Big :
    print(sys.exc_info())

def raiseSmall() :      # Small 클래스 예외 호출
    raise Small()

try :
    raiseSmall()
except Big :
    print(sys.exc_info())

print()

# 사용자 정의 예외 처리 변수 전달
class MyException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

try:
    raise MyException(2*2)      # Exception에 변수를 추가하여
except MyException as e:
    print('사용자가 정의한 예외를 호출합니다. 예외처리 내부 값은 다음과 같습니다. value:', e.value)

print()

# assert를 활용한 예외 처리
a = 30
margin = 2 * 0.2

assert margin > 10, 'not enough margin %s' % margin

