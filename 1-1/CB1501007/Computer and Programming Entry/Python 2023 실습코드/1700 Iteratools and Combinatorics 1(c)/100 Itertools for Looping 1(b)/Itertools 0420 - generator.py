
a = (x*x for x in range(10))
print(type(a))
print("sum =",  sum(a))



def generator(n):
    i = 0
    while i < n:
        yield i
        i += 1


print("\ngenerator로 생성")
for x in generator(5):
    print("we made ", x)

def fibonacci_func(n):
    a,b = 0, 1
    i = 0
    while True:
        if (i > n):    return
        yield a
        a, b = b, a+b
        i += 1


fib = fibonacci_func(10)

print("We print fibonacci number")
for x in fib:
    print(x, end=' ')



