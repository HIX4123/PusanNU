#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------

import csv

head = [ "TIME", "Fp1-F7", "F7-T7", "T7-P7", "P7-O1", "Fp2-F8", \
     "F8-T8", "T8-P8", "P8-O2", "Fp1-F3", "F3-C3", "C3-P3", \
      "P3-O1", "Fp2-F4", "F4-C4", "C4-P4", "P4-O2", "Fz-Cz", \
      "Cz-Pz", "Loc-A1", "Roc-A2", "ECG", "PHOT" ]

N = len(head)

wave_list= [ [ ] for i in range(N)]
print("wave_list=", wave_list)

with open('small.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        for i,x in enumerate(row) :
            if i >= 1 :
                wave_list[i].append( float(row[i]))
            else :
                wave_list[i].append(       row[i])

print("\n Time= ", wave_list[0])
print("\n ECG= ", wave_list[21])