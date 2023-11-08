#-------------------------------------------------------------------------------
# Purpose:     2019 Power Python
# Author:      Cho
#-------------------------------------------------------------------------------

import re
inputString = """
According to some, dreams express "profound aspects of personality"
(Foulkes 184), though others disagree.' Was good "이것은 무엇이냐" 고
그녀가 물었다. 너거들 "바보 아니냐?"  이것들아... "
"""

#^X은 X가 아닌 모든 문자


w = re.findall(r'"([^"]*)"', inputString)
print(w)
