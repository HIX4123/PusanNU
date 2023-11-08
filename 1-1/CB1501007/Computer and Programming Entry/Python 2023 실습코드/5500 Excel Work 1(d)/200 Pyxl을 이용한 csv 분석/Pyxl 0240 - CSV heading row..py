#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------

import csv

f = open('Ball.csv', 'r')
rdr = csv.reader(f)
heading = next( rdr)
print("cvs_head=", heading )

bcall = heading.index("PitchCall")
print("bcall=", bcall)
bheight = heading.index("PlateLocHeight")
print("bheight=", bheight)
bside = heading.index("PlateLocSide")
print("bside=", bside)

count=0
Call=[]
Hpoint=[]
Vpoint=[]
for line in rdr:
    count+=1
    Call.append( line[bcall])
    Hpoint.append( line[bheight] )
    Vpoint.append(  line[bside]  )

    print("Line", count, "=", line[bcall], line[bheight], line[bside])
    if count > 50 : break



f.close()