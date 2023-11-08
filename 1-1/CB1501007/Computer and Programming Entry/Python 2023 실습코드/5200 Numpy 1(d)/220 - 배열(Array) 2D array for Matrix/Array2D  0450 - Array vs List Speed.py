

import time
from array import array

# Create an empty int array.
a = array("i")

N =10000000
start_time = time.time()
# Append ten million ints.
for i in range(0, N ):
    a.append(i)

# Finished.
print("DONE")
print("Array processing time = ", time.time()-start_time)

# Python program that uses int list


b = list()

start_time = time.time()
for i in range(0, N ):
    b.append(i)

# Finished.
print("DONE")
print("List processing time = ", time.time()-start_time)

# Memory usage
#
# 43.8 MB    Array
# 710.9 MB    List