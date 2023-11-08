
fa = open("test.txt", "r")

print(fa.readline())
print(fa.readline())
print(fa.readline())

x = fa.tell()
print(fa.readline())

fa.seek(x)
print(fa.readline())


