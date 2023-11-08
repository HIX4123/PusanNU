#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-05-25
#-------------------------------------------------------------------------------


import re
p1 = re.compile("\b[Pp]ython\b")# 처음 시작하는 라인에서


data = """
python one
life is too short python
banana next Python word
Python two Pythonnnnnn good boy
you need python
Python three
"""

out =  re.findall(p1, data)

print( "ex01= ", out )
