#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2019-07-06
#-------------------------------------------------------------------------------


import csv

f = open('Ball.csv', 'r')
rdr = csv.reader(f)

count=0
for line in rdr:
    count+=1
    print("Line", count, "=", line[9], len(line))
    if count > 50 : break

f.close()
