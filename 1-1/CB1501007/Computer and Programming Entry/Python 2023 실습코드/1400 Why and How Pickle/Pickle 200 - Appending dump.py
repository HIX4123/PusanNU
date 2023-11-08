#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     "착하게 살지 말자."
# Author:      Cho
# Created:     2021-05-28
#-------------------------------------------------------------------------------

import pickle

My = [ {"Summer":"여름"}, (2,3,4), {"Dog", "Cat"}, [ 3,4,5,6,76],  "부산갈매기" ]

fp =open("padd.bin", "wb")  # wb는 write할꺼고,, 이것은 binary라는 것을 말함.

for w in My :
    pickle.dump(w,fp)       # 계속 쳐 넣는다.


fp.close( )


fr =open("padd.bin", "rb")
objs = []

# 서로 다른 type의 데이터가 여러개 있을 경우에는
# 이렇게 EOFE (end of file)에 나올 때까지 읽어야 한다.

while True:
    try:
        objs.append(pickle.load(fr))
    except EOFError:
        break


for w in objs :
    print(f" data= {w}, type= {type(w)}")

