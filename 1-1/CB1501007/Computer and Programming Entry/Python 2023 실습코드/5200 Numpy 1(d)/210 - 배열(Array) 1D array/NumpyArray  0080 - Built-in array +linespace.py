


import numpy as np

array1 = np.zeros((2,4))
print(f"> array1 = {array1}")
print(f"> array1 shape = {array1.shape}")


array2 = np.ones((3,4))
print(f"> array2 = {array2}")
print(f"> array2 shape = {array2.shape}")


# The empty function creates an array.
# Its initial content is random and depends on the state of the memory.
array3 = np.empty((5,4))
print(f"> array3 = {array3}")
print(f"> array3shape = {array3.shape}")


array = np.full((5,4), -2)
print(f"> array = {array}")
print(f"> array shape = {array.shape}")

# The function linspace returns evenly spaced numbers over a specified interval. For example,
# the below function returns four equally spaced numbers between the interval 0 and 10.
array = np.linspace(0, 10, num=8)  # 8개로 나눔.
print(f"> array = {array}")


