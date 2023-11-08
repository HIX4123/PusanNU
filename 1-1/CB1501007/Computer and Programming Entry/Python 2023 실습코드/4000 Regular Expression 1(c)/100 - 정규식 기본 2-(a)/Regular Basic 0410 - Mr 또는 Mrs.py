#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-05-25
#-------------------------------------------------------------------------------

import re

txt="We all reserve books for Mr.Tammes and Ms.Adelina and Mr.Cho who\
    attened out Party last night in 2020 May, 23"


mr= r"M[sr]\.[A-Z][a-z]+"


tmp01 = re.findall( mr, txt)
print("Mr.의 이름을 가진", tmp01)

tmp02 = re.finditer( mr, txt ) # 리스트

for (i,w) in enumerate( tmp02)  :
    print( f'i={i:3} span={w.span()}, match= { w.group()}')



mr= r"M[sr]\.([A-Z][a-z]+)"
tmp02 = re.findall( mr, txt ) # 리스트

print(tmp02)