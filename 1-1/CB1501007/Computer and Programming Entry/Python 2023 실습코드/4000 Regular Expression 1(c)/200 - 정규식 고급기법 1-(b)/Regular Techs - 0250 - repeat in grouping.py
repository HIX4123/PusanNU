#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-05-27
#-------------------------------------------------------------------------------

import re

txt = 'cgggargaqWqtgcgWqtgcgWqtgcgWqtgcgtcgagagagctacgagWqtgcgWqtgcgcgaga'

out = re.search(r'(.+)\1+', txt)
print( out.group(), out.group(1) )


out = re.finditer(r'(.+)\1+', txt)
for w in out :
    print("w>", w.group(), w.group(1))

out = re.finditer(r'(.+?)\1+', txt)
for w in out :
    print("z>", w.group(), w.group(1))
