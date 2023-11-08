#-------------------------------------------------------------------------------
# Purpose:     2022 Zoh's Work     "過猶不及" 메롱..
# Author:      Cho
# Created:     2022-03-26
#-------------------------------------------------------------------------------


import numpy as np

P = np.array([ 30, 25, -43])
Q = np.array([-10, 2,   41])


Steps = 100
epsilon = 1/Steps
t=0

for w in range( Steps+1) :
    current= (1-t)*P + t*Q
    print(f"C[{t:5.3f}]= {current}" )
    t += epsilon
