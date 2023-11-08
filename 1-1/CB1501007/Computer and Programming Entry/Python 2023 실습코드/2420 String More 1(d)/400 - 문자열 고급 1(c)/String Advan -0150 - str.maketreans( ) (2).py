#-------------------------------------------------------------------------------
# Purpose:     2022 Zoh's Work     "過猶不及" 메롱..
# Author:      Cho
# Created:     2022-04-26
#-------------------------------------------------------------------------------

import string

intab = "개똥뽕짱"
outtab = "?+&*"
trantab = str.maketrans(intab, outtab)

str = "짱짱 즐거운 work 개어려운 string 뽕 문자열 wow!!!";
print (str.translate(trantab))