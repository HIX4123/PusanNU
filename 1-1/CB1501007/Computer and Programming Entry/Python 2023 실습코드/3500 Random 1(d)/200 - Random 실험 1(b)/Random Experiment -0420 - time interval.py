
# time interval generator based on Poisson
# distribution,
# mu는 time interval의 평균 예를 들면 평균 10분
import random
import math
random.seed()

def timegap( mu ):
   u = random.random()
   x = math.log(1.0 - u)*(-mu )
   return( int(x+0.51))

s = 0
mu = 10
N= 100

fn =      input("Type a File name")
N  =  int(input("Type Number of intervals"))
mu =  int(input("Type Average Gap"))
print("fname= %s, N= %d, mu= %d " % ( fn, N, mu ))

myfile = open( fn, "w")
print(N, mu, file=myfile)
clock = 1
for x in range(1,N+1):
    gap = timegap( mu )
    house = random.randrange(3,40)
    print("%4d %3d" % ( clock, house), file=myfile)
#   if ( x % 10 == 0 ) : print "\n"
    clock += gap


print("\n Average=", s/float(N))

myfile.close()
