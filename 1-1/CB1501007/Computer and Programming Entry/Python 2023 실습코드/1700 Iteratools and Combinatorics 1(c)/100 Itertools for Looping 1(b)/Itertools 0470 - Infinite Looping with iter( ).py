
import  itertools

print("\nitertools count(): ")
for i in itertools.count(10):   # 10부터 시작한다.
    if i > 20:
        break
    else:
        print((i), end=' ')

print("\nitertools islice() :")
for i in itertools.islice( itertools.count(10), 5):  # 5개까지만
    print((i), end=' ')


count = 0
wlist = list("My-Boy-")
print("\nitertools cycle() 무한반복할 때 사용:")
for item in itertools.cycle( wlist ):
     if count > 30:
         break
     print((item), end=' ')
     count += 1









