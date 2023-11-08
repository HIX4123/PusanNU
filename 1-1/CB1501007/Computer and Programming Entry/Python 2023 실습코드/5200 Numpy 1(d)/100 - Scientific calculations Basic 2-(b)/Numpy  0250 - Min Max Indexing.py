
import numpy as np


a =  np.random.random((2,3)) # 2 by 3 matrix
print("실험 100: ", a)

print("실험 101: ",a.sum())
print("실험 102: ",a.min)
print("실험 103: ",a.max())

print()

print("실험 104: ", a.sum(axis=0)) #sum of each column
print("실험 105: ", a.sum(axis=1)) #sum of each row

print()

print("실험 106: ", a.min(axis=0)) #min of each column
print("실험 107: ", a.max(axis=1)) #max of each row

print()

a = np.arange(10)*3

print("실험 108: ",a[3])

print("실험 109: ",a[2:5])
print("실험 110: ",a[:7:2]) #index a[0] a[2] a[4] a[6]
print("실험 111: ",a[::-1]) #reverce

print()


b = np.arange(9).reshape(3,3)

for row in b :
    print(">>", row)