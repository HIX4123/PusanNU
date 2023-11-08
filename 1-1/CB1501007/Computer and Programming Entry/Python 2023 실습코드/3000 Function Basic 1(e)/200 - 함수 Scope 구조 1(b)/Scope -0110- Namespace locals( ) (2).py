a = 2023
b = 'Hello'

print(f" 외부에서 a = {a}")
print(f" 외부에서 b = {b}")


def func1():
    global a
    c = a + 999
    print(f" func1( )에서 a = {a}")
    a = 100
    b = 'python'
    t = "oh my god"
    print(' 함수 func1( ) namespace', locals())

def func2():
    a = "삼겹살"
    b = 67.45e4
    print(' 함수 func2( ) namespace', locals())



func1()
func2()

print(f" 외부에서 a = {a}")
print(f" 외부에서 b = {b}")

