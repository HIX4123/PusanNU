

form = "a=%2d를 b=%2d로 나누면 그 값은 %10.5f"

x=[ 53, 55, 13, 79, 62]
y=[ 11,  8,  7,  8, 33]

for (a,b) in zip(x,y):
    outform = form %(a,b, a/b)
    print(outform)
