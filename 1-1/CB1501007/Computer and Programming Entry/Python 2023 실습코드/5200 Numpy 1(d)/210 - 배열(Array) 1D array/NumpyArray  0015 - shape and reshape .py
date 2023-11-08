


import numpy as np

array = np.arange(20)
print(f"> array = {array}")
print(f" array shape = {array.shape}")


array = np.arange(20).reshape(4,5)
print(f"> array = {array}")
print(f"> array(4,5) shape = {array.shape}")


array = np.arange(27).reshape(3,3,3)
print(f"> array = {array}")
print(f"> array(27) shape = {array.shape}")

array = np.arange(22).reshape(3,3,3)
print(f"> array = {array}")
print(f"> array(27) shape = {array.shape}")