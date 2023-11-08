#-------------------------------------------------------------------------------
# Purpose:     2020 Prof. Zoh's Work
# Author:      Cho
# Created:     2020-11-11
#-------------------------------------------------------------------------------

import string


Upper= list(string.ascii_uppercase)

print( string.ascii_uppercase )
print( string.ascii_lowercase )
print( string.ascii_letters )
print( string.digits )
print( "문장끝 문자", string.punctuation )
w="r"
if w in string.ascii_lowercase :
    print("w는 소문자입니다" )