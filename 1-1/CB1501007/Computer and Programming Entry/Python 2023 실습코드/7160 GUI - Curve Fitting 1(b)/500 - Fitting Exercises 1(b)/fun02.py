

import os
import random
import math
import time

def f1( v ):
    x = v
    val =  3 * x * math.sqrt(x) + 7*x + 100
    return(val + random.randint(10,20))


print(" N < 0이면 프로그램이 종료됩니다. ")
print(" 50 < N < 10000, 측정은 최대 10회만 가능 ")

c = 5

while( True ):
    x = eval(input("Type N:"))
    if x < 0 or c <= 0 :
        print("End of Experiment")
        break
    if x > 10000  or x < 50 :
        print("N boundary error")
        break
    print("input N=", x,  "f(", x,")=", f1(x))
    c -= 1
    time.sleep(3)

os.system('del fun02.pyc')
print("All experiment done")

