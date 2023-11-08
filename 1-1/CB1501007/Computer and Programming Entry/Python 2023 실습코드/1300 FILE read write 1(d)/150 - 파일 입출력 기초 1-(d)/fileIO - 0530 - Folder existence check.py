#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------

import os


fname = input(" 읽을 파일의 이름 : ")
if ( not os.path.isfile(fname) ) :
    print(f' 오류! FILE: {fname}이 없습니다. 종료 땡')
    exit(0)

f = open( fname , 'r')


mydata = f.read( )
print(" mydata>>\n", mydata)
print(" 길이는 = ",  len(mydata))
print(" my data의 유형은 ",  type(mydata) )

multiline = mydata.split()
oneline = ''.join( multiline )
print("\noneline = ", len(oneline),"\n>", oneline )

print("\nWho\n")
print("Whom")

f.close()