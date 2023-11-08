# time.clock( )은 더이상 지원되지 않습니다. 2021년 3월 봄날에


import time
import string
import random

def ranword(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


N=[ 1000000,
    2000000,
    4000000,
    8000000,
   16000000,
   32000000,
   64000000, ]
#  128000000  ]

U=[]
V=[]
for w in N :
    mstart = time.process_time()

    mystring = ranword( w )
    U.append( mystring )
    V.append( mystring )
    mend = time.process_time()
    print(f"w = {w}, delta= {mend-mstart}")

for x,y in zip(U,V) :
    mstart = time.process_time()
    if x == y :
        print("Equal")
    else :
        print("Different")
    mend = time.process_time()
    delta = mend - mstart     #
    print(f" Size= {len(x)}, Time={delta} " )

for x,y in zip(U,V) :
    mstart = time.perf_counter()
    if x == y :
        print("> Equal")
    else :
        print("> Different")
    mend = time.perf_counter()
    delta = mend - mstart     #
    print(f" Size= {len(x)}, perf= {delta:10.4e} " )






