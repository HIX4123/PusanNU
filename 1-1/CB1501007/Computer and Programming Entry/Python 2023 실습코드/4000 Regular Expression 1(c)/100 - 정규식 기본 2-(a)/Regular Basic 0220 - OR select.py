#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-05-25
#-------------------------------------------------------------------------------

import re

txt="The book in the  all an reserve books for \
     a Mr.Tammes an Adelina and the a Cho who\
    an   Party the last night in The 2020 May, 23"


mr= r"(the|The|a|A|An|an)\s+\w+\b"


tmp02 = re.finditer( mr, txt ) # 리스트

for (i,w) in enumerate( tmp02)  :
    print( f'i={i:2} ({w.start():3},{w.end():3}), match= "{ w.group()}"', end=" ")
    print( f'g(1)={w.group(1)}')

