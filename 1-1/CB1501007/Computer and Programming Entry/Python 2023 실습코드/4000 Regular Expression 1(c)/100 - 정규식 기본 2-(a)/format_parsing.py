#-------------------------------------------------------------------------------
# Author:      Zoh
# Created:     2019-06-22
#-------------------------------------------------------------------------------

import re

text="""
삼국지연의 / 나관중 CHINA / 한글사 / 34500
사랑하는 사람들아/Berns Berros / Benguin Books / 45000
C언어 기초 /   /  부산대 출판부 / 55000
Compiler Design Tutorial /  우균 / Amazon Books / 84000
"""

mypat=r"([\w ]+)\s*/\s*([\w ]+)\s*/\s*([\w ]+)"
la = re.findall( mypat, text, re.M|re.I )
for w in la :
    print(w)



