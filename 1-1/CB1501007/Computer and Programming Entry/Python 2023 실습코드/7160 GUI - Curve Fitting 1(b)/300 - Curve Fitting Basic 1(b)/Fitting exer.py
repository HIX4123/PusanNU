
import math
import random

random.seed(2018)

funlist=[ mylog, mylinear ]

def gendata( code ):
    x=[] ; y=[]
    if not ( 1 <= code <= 5 ) :
        print("입력코드 오류", code)
        return ("Error")

    if code == 1 :
        for w in range(1,1000, 100):
            myx = w + random.randint(1,80)
            x.append( myx )
            d = 12 * math.log( myx + 10, 2 ) + 10
            y.append( d )
        return (x,y)




code = eval(input("1-5의 번호를 입력하시오. "))
a, b = gendata(code)

print(a)
print(b)




