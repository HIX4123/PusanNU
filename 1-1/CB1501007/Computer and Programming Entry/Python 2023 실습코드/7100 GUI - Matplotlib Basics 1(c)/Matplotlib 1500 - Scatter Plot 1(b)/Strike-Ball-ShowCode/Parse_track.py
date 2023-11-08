#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------

import csv
ftrac = open('Ball.csv', 'r')
rdr = csv.reader( ftrac )
heading = next( rdr )
#print("cvs_head=", heading )

myhead = open("myhead.txt", "r")
pophead=[]
for line in myhead:
    lcode = line.strip()
    pophead.append( lcode )



print("pophead[]=", pophead)
ftrac.close()
myhead.close()