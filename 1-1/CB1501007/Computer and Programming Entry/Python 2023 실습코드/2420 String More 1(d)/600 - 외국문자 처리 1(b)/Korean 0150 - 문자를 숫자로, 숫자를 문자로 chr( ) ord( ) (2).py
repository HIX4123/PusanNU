#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-05-07
#-------------------------------------------------------------------------------

mstr = "단결♥단결♥단결"

stringToInt = ord('a')


for w in range(10,200) :
    print ( f' chr({w}) = {chr(w)}')


print("\n 한글 처리")
for w in list(mstr):
    print ( f' ord({w}) = {ord(w)}')

print("\n 숫자를 한글로")
for w in range(45800,46000) :
    print ( f' chr({w}) = {chr(w)}')

