
import  itertools

count=0
wlist = list("부산갈매기타령")
print("\nitertools cycle() 무한반복할 때 사용:")

for item in itertools.cycle( wlist ):
     if count > 30:  #30번에서 끊 #30번에서 끊어요.... 무한반복은 할 수 없어서어요.... 무한반복은 할 수 없어서 #30번에서 끊어요.... 무한반복은 할 수 없어서
         break
     print((item), end=' ')
     count += 1









