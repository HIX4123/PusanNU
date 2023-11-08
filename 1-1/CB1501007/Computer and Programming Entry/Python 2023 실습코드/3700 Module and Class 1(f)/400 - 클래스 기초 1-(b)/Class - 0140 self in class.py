#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-05-06
#-------------------------------------------------------------------------------

class Foo:
    def func1():
            print(" func1( )")
    def func2(self):
            print( f' id(self)= {id(self)}')
            print(" func2( )")


f = Foo()
f.func2() #function 2

#f.func1()  # error 발생
##TypeError: func1() takes 0 positional arguments but 1 was given
# 그렇다면 func1 메서드처럼 메서드를 정의할 때부터
# 아무 인자도 없는 경우에는 어떻게 될까요?
# func1()을 호출해보면 오류가 발생합니다.
# 오류 메시지는 func1( )이 변수가 없지만... 1개가 주어졌다라고 하네요.
# 이는 앞서 설명한 것처럼 파이썬 메서드의 첫 번째 인자로
# 항상 인스턴스가 전달되기 때문에 발생하는 문제입니다.

print( f' id(f) = {id(f)} ')

# 실행 결과를 살펴보면 43219856이라는 값이 출력을 확인할 수 있다.
# Foo 클래스를 정의할 때 id(self)를 출력하게 했는데
# id(self)의 값이 바로 43219856이다. 이 값은 f라는 변수가 바인딩하고
# 있는 인스턴스의 주솟값과 동일하다.
# 즉  클래스 내에 정의된 self는 클래스 인스턴스와 동일함을 알 수 있다.

f2 = Foo()
print( f' id(f2) = {id(f2)} ')
f2.func2()

# 이제 Class에서 직접 member function을 불러보자.
Foo.func1()

# 그러나 self 매개변수가 있는 func2( )를 Class에서 직접 부를 수는 없다.
#Foo.func2()

f3 = Foo()
Foo.func2(f3)
f3.func2()
