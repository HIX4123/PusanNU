#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2019-07-06
#-------------------------------------------------------------------------------

import csv

with open('Ball.csv', 'r') as reader:
    for i, line in enumerate(reader):
        fields = line.split(',')
        print( "i=%4d,  %2d"%( i, len( fields))  )
        if i > 110 : break


for i,w in enumerate(fields) :
    print(i, type(w))