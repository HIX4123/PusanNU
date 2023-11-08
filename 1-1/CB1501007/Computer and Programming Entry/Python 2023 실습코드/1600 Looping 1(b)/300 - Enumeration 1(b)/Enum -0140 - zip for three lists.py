

x = [1,2,3,4]
y = [7,8,3,2]
z = ['a','b','c','d']
t = list("computer")

lx=  [(a,b,c) for a,b,c in zip(x,y,z)]
print(lx)

for x,y,z in zip(x,y,z):
    print((x, y, "O" if z in t else "X" ))

