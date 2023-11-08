

def foo():
    global c

    if c >= 4 :
        print("4번 이상 call은 불가능")
        return
    else :
        c += 1
    x = -10
    print(("local x:", x))


c= 0
foo()

print("global x:", x)

foo()
foo()
print("c=", c)
foo()
foo()
print("c=", c)
