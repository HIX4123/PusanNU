
num=[1,  2,   3,  4,  5,  6,  7]
char = list("My Style")

lb = [ w**2 for w in num ]  # 제곱수 만들기

lc = [ "["+w+"]" for w in char ]


print("lb=", lb)
print("lc=", lc)


