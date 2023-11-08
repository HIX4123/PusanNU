import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

arr3 = np.stack((arr1, arr2), axis=0)
print(f"arra3[]= {arr3}")


arr4 = np.stack((arr1, arr2), axis=1)
print(f"arra4[]= {arr4}")

arr5 = np.concatenate((arr1, arr2))
print(f"arra5[]= {arr5}")
