#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------
a0=[0, 3 ]
a1=[0, [3]]
a2=[[0], [3]]
b0= [[0, 3]]
b1= [ [0, [3]] ]
b2= [[0],[0],3 ]
c0 = [ 3, 0]
c1= [ 0, [ ], 3]
c2= [ [ ], 0, 3 ]


BL= [b0, b1, a2, b2, a0, a1, c0, c1, c2 ]
print("before=", BL)
CL = sorted(BL)  # Error 같은 종류의 데이터끼리만 비교가
print("after =", CL)

w1 =(a0 == c0)
print("w1=", w1)