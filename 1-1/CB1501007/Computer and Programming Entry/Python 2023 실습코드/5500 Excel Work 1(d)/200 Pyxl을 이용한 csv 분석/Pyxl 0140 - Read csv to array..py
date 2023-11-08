#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------

import csv

count = 0

with open('small.csv', newline='') as csvfile:
    count += 1
    data = list(csv.reader(csvfile))
    print(count, "= ", len(data))

#print(data)
