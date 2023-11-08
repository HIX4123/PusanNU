
def gen():
    for i in range(10000):  #이것을 미리 만들어 두지 않는다.
        yield i ** 3


print(type(myx))

myx =  gen()

print(next(myx))
print(next(myx))
print(next(myx))
print(next(myx))
print(next(myx))