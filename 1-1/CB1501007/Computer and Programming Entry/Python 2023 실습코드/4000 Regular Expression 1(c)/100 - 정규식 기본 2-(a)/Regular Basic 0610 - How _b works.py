#-------------------------------------------------------------------------------
# Purpose:     2020 컴퓨터및 프로그래밍 입문
# Author:      Cho
# Created:     2020-05-27
#-------------------------------------------------------------------------------

import re

my= " stfoo1$ foobar foo3. foo8 sfoo,  foobar foo7uuu b56foo6"

print( re.findall( r"\bfoo\d\b", my )  )
print( re.findall( r"foo\d", my )  )
# This means that r'\bfoo\b' matches
# 'foo', 'foo.', '(foo)', 'bar foo baz' but not 'foobar' or 'foo3'.
