#-----알고리즘 공학론 2022 -----------------------------

import os
import random
import math
import time

def f1( v ):
    x = v
    val = 12*x + 45
    return( val + random.randint(-12,12))

print("> N < 0이면 프로그램이 종료됩니다. ")
print("> 50 < N < 10000, 측정은 최대 10회만 가능 \n\n")

c = 10

while( True ):
    x = eval(input("Type N:"))
    if x < 0 or c <= 0 :
        print("End of Experiment")
        break
    if x > 10000  or x < 50 :
        print("N boundary error")
        break
    print(f"> N={x:5}, f({x:5})= {f1(x):10.3f}")
    c -= 1
    time.sleep(1)

os.system('del xfunc( )-05.py')
print("All experiment done")

