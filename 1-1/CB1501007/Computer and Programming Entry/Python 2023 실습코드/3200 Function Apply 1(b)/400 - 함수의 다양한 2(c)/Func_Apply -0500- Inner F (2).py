
# 함수 안에 함수가 또 들어간 경우

def fxx():
    x = 88
    def f2():
        print("in fxx() = ",  x)
    f2()

fxx()                  # prints 88

def fyy():
     x = 99
     print("fyy()가 불려졌습니다")
     def f21():
         def f31():
             print("in f31() = ", x)
         f31()  #이것은 함수 f21() 안이다.
     f21() #이것은 함수 fyy() 안이다.

fyy()
