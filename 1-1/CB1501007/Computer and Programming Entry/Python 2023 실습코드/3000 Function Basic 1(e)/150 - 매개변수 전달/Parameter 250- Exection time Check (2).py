
import time
import random

def myloop(N) :
    cnt = 0
    for i in range(N):
        x = random.random()
        y = random.random()
        z = x * y

        if z > 0.88 :
            cnt += 1

    return ( cnt)
#----- end of myloop() --------


start = time.time()

N= 100000
print("i=", myloop(N))

end = time.time() - start     # end에 코드가 구동된 시간 저장

print("Ellasped =", aend)



