#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     "착하게 살지 말자."
# Author:      Cho
# Created:     2022-03-03
#-------------------------------------------------------------------------------


import re

mystr="""
이것은    무엇인가  bpat
songs for 45 + 90 )
goog               45 67 + -
"""
bpack = re.compile(r"\s+")

my_str = bpack.sub(" ", mystr).strip()
print(my_str)