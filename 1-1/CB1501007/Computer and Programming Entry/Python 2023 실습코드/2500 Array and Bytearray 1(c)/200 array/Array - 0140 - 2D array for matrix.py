#-------------------------------------------------------------------------------
# Purpose:     2020 Prof. Zoh's Work
# Author:      Cho
# Created:     2020-09-15
#-------------------------------------------------------------------------------

# Creates a list containing 5 lists, each of 8 items, all set to 0
w, h = 8, 5;
Matrix = [[0 for x in range(w)] for y in range(h)]

Matrix[3][3]= 199;
Matrix[4][2]= 34 ;
print( "Matrix =\n", Matrix)


import numpy
R = numpy.zeros((5, 5))
R[2][2]= 13
print( "R=\n", R )

T=[]
T.append( numpy.arange(25).reshape((5, 5))  )       # create a 1-d range and reshape
T.append( numpy.array(range(25)).reshape((5, 5)) )   # pass a Python range and reshape
T.append( numpy.array([5] * 25).reshape((5, 5))  )  # pass a Python list and reshape
T.append( numpy.empty((5, 5))    )                  # allocate, but don't initialize
T.append( numpy.ones((5, 5)) )

print ( T )