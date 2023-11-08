#--------------------------------------------------------
# Author:      Zoh Que
# Created:     07-02-2023
#--------------------------------------------------------

import numpy as np
import math

L = [ [x, x*x, f'{math.sqrt(x):.3f}'] for  x in range(12)]

#print(f"\n1 > L ={L}")

ex_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0,-1,-2], [-3,-4,-5]]

W1 = [inner[:2] for inner in ex_list ]
print(f"\n W1 = {W1}")



alist = np.array( ex_list )
blist = alist[:2,:2].tolist() # [[1, 2], [4, 5]]
print(f"\n blist = {blist}")


clist = list(map(lambda lst: lst[-2:], ex_list))
print(f"\n clist = {clist}")