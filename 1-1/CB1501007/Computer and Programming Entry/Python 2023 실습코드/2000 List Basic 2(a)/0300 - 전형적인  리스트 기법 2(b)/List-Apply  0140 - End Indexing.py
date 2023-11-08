# List에 원소를 넣고 빼고 해 봅시다.

a = list("Computer")



print("a=", a)
print("a[:-1]=", a[:-1])
print("a[::-1]=", a[::-1])


print("a[:None:-1]=", a[:None:-1])

print("a[:-len(a)-1:-1]=", a[:-len(a)-1:-1])




print("a[6:2:-1]=", a[6:2:-1]) #꺼꾸로 간다.

print("a[::]=", a[::])
print("a[0:None:1]", a[0:None:1])
print("a[-1:None:-1]=", a[-1:None:-1])
print("a[-2:None:-1]=", a[-2:None:-1])
