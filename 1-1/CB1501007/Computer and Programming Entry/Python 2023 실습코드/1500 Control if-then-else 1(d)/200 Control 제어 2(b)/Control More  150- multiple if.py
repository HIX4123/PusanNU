#

a = b = c = d = 0

if a == b == c == d == 0 : # 모두가 0인가를 검사
    print("Call 1")
else :
    print("Not equal")

x=10
y=40

if 5 < x < 30 :  # if( 5 < x ) and (x < 30 ) :
    print("Call 2")
else :
    print("Not True 1")


if 5 < x < y < 50 :
     print("Call 3")
else :
    print("Not True 2")


if  2  <  ( y < 50)  :  # (y<50)은 결과로 1이 된다.
     print("Call 4")
else :
    print("Not True 3")