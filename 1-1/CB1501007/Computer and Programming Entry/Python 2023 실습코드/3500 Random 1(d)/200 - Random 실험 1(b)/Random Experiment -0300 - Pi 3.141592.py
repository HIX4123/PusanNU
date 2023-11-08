
import random   # for random

random.seed( 2016)  # 초기 random 값을 설

def odist(x,y):
    return x*x + y*y


def in_circle(x,y) :
    val = odist(x,y)
    if val < 1.0 :    return( True)
    else :              return(False)





print(in_circle(0.95, 0.93))
print(in_circle(0.21, 0.63))
print(in_circle(0.86, 0.95))
print(in_circle(0.33, 0.23))
print(in_circle(0.91, 0.89))
print(in_circle(0.712, 0.217))