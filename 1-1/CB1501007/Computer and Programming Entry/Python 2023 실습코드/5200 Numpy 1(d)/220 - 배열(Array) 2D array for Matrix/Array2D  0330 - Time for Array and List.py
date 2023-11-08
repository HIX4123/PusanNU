


import time
from array import array

# Create an int array, and a list.
mlist = list(range(0, 50))
arr = array("i", mlist)

t1 = time.time()
print("시작시간 = ", t1)

# Version 1: loop over array.
for i in range(0, 1000000):
    sum = 0
    for value in arr:
	   sum += value

t2 = (time.time())
print("Array 처리시간 = ", t2 - t1)

# Version 2: loop over list.
for i in range(0, 1000000):
    sum = 0
    for value in mlist:
	   sum += value

t3 = (time.time())
print("List 처리시간 = ", t3 - t2)

