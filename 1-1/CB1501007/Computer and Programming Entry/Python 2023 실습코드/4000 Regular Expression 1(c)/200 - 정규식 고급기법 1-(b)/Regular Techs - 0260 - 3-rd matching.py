#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-05-27
#-------------------------------------------------------------------------------

import re

pat=r"(?:.*?\$[0-9.]+){2}.*?(\$[0-9.]+)"

txt="thiscanbeanything$25.74thiscanbesomethingelse\
alsowithnewlines$533.63thisonetoo$54.32plusthis\
$62.42thisneverends"

print( re.findall(pat, txt))