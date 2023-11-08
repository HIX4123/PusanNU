#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-05-25
#-------------------------------------------------------------------------------


# re.DOTALL(= re.S)
# .(마침표) 문자는 원래 \n(뉴라인) 문자를 제외한 아무 문자와 일치한다.
# 만약, re.DOTALL(re.S) 옵션을 주면, .(마침표) 문자가
# \n(뉴라인)까지 포함해 모든 문자와 일치할 수 있게 해준다.
para = """
{ apple, milk ,
   [
       coffee ,
       wine ,
       bread
    ] ,
  orange
}
"""

import re

out =  re.findall(r"\[.*\]", para )
print( "\n ex01= ", out )
out =  re.findall(r"\[.*\]", para, re.DOTALL )
print( "\n ex02= ", out )

