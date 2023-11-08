# 다양한 if-then-else 처리기법 모음
# 중요한 것은 하나의 줄로 처리한다는 것이다.

x = 3 if 4 > 5 else -1
print("x=", x)

a= 10 ; b = 20
if a < b :
    x = 60
else :
    x = 90

x = 60 if a < b else 90

print("x=", x )

x, y = 2,1

z = 3 +  ( x if x > y else y )
print("x,y,z=", x,y,z)

z = (6 + x) if x > y else y
print("x,y,z=", x,y,z)


a = 1
b = 2
t = 1 if a > b else -1
w = 1 if a > b else -1 if a < b else 0
print("t,w=", t,w)

print("Cola" if x == 0 else "Cider")

q = ("Summer", "Spring") [ 4 > 2 ]

print(q)