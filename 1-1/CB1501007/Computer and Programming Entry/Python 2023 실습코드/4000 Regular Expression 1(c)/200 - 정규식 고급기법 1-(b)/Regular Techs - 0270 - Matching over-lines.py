#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-05-25
#-------------------------------------------------------------------------------

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

