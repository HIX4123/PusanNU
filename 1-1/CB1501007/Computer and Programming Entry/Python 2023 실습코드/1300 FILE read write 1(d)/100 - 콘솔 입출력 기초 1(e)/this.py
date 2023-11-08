#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     "착하게 살지 말자."
# Author:      Cho
# Created:     2021-12-29
#-------------------------------------------------------------------------------

# stdin 으로 화일 읽기
# 사용방법
# python.exe this.py < data.txt

import sys


fstdin = open(sys.stdin.fileno(),encoding='cp949')

i=0
for line in fstdin :  #파일을 끝까지 읽고 자동적으로 마
    i += 1
    cline=line.strip()
    print( f'i= {i:2},  {cline}')

fstdin.close()
