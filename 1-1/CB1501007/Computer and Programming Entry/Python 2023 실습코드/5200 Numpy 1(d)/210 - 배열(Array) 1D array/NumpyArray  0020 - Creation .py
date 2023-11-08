
import numpy as np

a0 = np.array([7, 6, 5, 4])
a1 = np.array([1, 2, 3, 4])
a2 = np.array([[1, 2], [3, 4]])
a3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
a4 = np.array([127, 128, 129], dtype=np.int8)
a5 = np.array([2, 3, 4], dtype=np.uint32)
a6 = np.array([5, 6, 7], dtype=np.uint32)
a7 = np.array( [a0, a1] )


for i,w in enumerate([a0, a1, a2, a3, a4, a5, a6, a7]):
    print(f"\n\n i={i} \n {w}")



c_unsigned32 = a5 - a6
print('unsigned c:', c_unsigned32, c_unsigned32.dtype)

c_signed32 = a5 - a6.astype(np.int32)
print('signed c:', c_signed32, c_signed32.dtype)
