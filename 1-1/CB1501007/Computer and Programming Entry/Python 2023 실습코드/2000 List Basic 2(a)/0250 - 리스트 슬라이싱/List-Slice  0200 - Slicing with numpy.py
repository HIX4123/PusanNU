#--------------------------------------------------------
# Author:      Zoh Que
# Created:     07-02-2023
#--------------------------------------------------------

import numpy as np

x = np.array([w for w in range(1,30)])
print(f"\n x = {x}")
print(f"\n x[3] = {x[3]}")
print(f"\n x[3:8] = {x[3:8]}")
print(f"\n x[3::4] = {x[3::4]}")



y = np.arange(42).reshape(6,7)
for w in y :
    print(f"{w}")
print("--------------------")

print(f" 특정 원소 y[2,3] = {y[2,3] }") # 특정 원소

print(f" y[0] = {y[0]}")
print(f" y[-1] = {y[-1]}")
print(f" y[3] = {y[3]}")
print(f" 세로 칼럼 y[:, 0] = {y[:, 0]}")
print(f" 세로 칼럼 y[:, 3] = {y[:, 3]}")

# Get first three elements of second column.
print(f" Submatrix y[0:3, 1] = {y[0:3, 1]}")

print(f" Submatrix y[1:4, 0:2] = {y[1:4, 0:2]}")


