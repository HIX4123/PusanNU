#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     "착하게 살지 말자."
# Author:      Cho
# Created:     2021-05-28
#-------------------------------------------------------------------------------




#To append to a pickle file
import pickle

p= {"Summer":"여름", "Fall":"가을"}
q= [ 3,4,5,6,76]
r= "부산갈매기"

fp =open("padd.bin", "wb") # wb는 write할꺼고,, 이것은 binary라는 것을 말함.


pickle.dump(p,fp)
pickle.dump(q,fp)
pickle.dump(r,fp)

fp.close( )

#To load from pickle file
fr =open("padd.bin", "rb")
objs = []
while 1:
    try:
        objs.append(pickle.load(fr))
    except EOFError:
        break


for w in objs :
    print(f" data={w}, type= {type(w)}")

