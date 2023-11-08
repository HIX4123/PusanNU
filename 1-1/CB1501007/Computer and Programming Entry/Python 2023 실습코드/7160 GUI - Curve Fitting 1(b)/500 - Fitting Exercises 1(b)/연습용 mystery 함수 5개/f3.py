#-----알고리즘 공학론 2022 -----------------------------

import os
import random
import math
import time

def f1( v ):
    x = v
    val =  0.1 * x * x  + 5*x + 120
    return(val + random.randint(-20,-20))

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

os.system('del f3.py')
print("All experiment done")

