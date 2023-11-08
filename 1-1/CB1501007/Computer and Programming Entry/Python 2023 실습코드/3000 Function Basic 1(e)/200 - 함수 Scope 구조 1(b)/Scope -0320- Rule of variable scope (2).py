
x = "summer"

def foo1():
    print(("Inside foo1(): x=", x ))
    y = x+"time"
    print(("Inside foo1(): y=", y )) # access는 외부변수가 가능

def foo2():
    #x="coco"
    z = x * 2     # 값을 바꾸면 local 변수가 자동으로 된다.
    print(("Inside foo2(): z=", z))




foo1()
print(("Outside1 x=:", x))
foo2()
print(("Outside1 x=:", x))

#print("Outside1 y=:", y) # 함수의 local variable을 밖에서 출력할 수 없다.