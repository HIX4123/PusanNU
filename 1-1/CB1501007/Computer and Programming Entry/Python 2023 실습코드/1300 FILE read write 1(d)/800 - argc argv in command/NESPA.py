#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     "착하게 살지 말자."
# Author:      Cho
# Created:     2021-11-16
#-------------------------------------------------------------------------------
# 대상 파일에서 \n 공백을 무시합니다.
# 사용법
# > python NESPA.py  myBTS.cpp

import sys
import os


myfile = sys.argv[1]  # 크기를 측정한 대상 파일

if len(sys.argv) != 2:
    print(" Usage: > python NESPA.py  mycode.cpp")
    print(" NESPA size를 측정한 파일의 갯수는 1개만 가능")
    sys.exit()

print(" NESPA 크기를 측정할 파일 = ", myfile )

if ( not os.path.isfile( myfile ) ) :
    print(f' 오류 FILE: <{ myfile }>이 없습니다. 종료 땡')
    exit(0)
else :
    f = open( myfile, 'r')

mydata = f.read( )
print(" 파일의 물리적 크기 = ",  len(mydata))
Lines = mydata.split( )
Sines = map( len, Lines )
print(f"\n {myfile} 파일의 NESPA 크기 = {sum(Sines)} ")
