

def foo():
    global a,b
    print("in foo() a,b = ", a, b)      # 출력은 가능하나
    a = a + 99         # 중간에 변수를 고칠 수는 없다.
    b = b + 99


a = 100
b = 200

foo()
print("Outside of foo()")
a += 99
b += 77
print(a,b)