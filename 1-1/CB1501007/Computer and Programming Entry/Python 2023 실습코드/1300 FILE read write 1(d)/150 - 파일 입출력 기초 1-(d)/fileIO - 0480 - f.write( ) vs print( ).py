#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------


# writedata.py
f = open("exer.txt", 'w')

for i in list("아름다운 우리강산"):
    token = i*5
    #f.write( token )
    print( token, file=f)

f.close()