#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     "착하게 살지 말자."
# Author:      Cho
# Created:     2021-04-30
#-------------------------------------------------------------------------------

import string

X= "computer 2021 PNU 456 XYE"

for w in X:
    if w in string.digits :
        print("숫자당 ", w)