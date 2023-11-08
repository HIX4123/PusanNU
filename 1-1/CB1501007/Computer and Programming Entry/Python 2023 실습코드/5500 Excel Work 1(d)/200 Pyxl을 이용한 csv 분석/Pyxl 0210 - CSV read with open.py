#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------


import csv
count=0
with open('Ball.csv', newline='') as csvfile:
    track = csv.reader(csvfile, delimiter=',', quotechar='|')

    for row in track :
        print("\n>>", ', '.join(row))


        count += 1
        if count > 50 :  break