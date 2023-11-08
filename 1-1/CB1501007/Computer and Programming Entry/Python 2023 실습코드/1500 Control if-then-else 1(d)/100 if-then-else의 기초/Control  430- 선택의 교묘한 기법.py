
a=10
b= 0

if a > b :
    print("a>b")
else :
    print("a<=b")

print(["a>b","a<=b"] [a > b])  # 리스트 indexing 0이면 앞, 1이면 뒤

A="YES3"
B="NO3"

X=3 ; Y=5 ; Z=10

print([A,B][X<5 and Y<5]) #24 Chars
print([A,B][X<5>Y])       #19 Chars

print([A,B][X>0 and X<10]) #25 Chars
print([A,B][0<X<10])       #20 Chars

print([A,B][X>0 and Z>0 and Y<X]) #31 Chars
print([A,B][Z>0<X>Y])             #21 Chars


t= [3,4][a<b]
print("t=", t)
