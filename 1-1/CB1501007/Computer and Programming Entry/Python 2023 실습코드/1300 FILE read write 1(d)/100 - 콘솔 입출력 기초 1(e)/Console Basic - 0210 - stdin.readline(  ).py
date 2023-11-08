#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     롯데 만만세
# Author:      Cho
# Created:     2021-03-18
#-------------------------------------------------------------------------------

# input( ) 보다 훨씬 빠르게 읽어들일 수 있다.
# 특히 코딩 test일 경우에는 이것을 사용해야 한다.

import sys

print("한 줄 문자열을 입력하시오: " )
for x in sys.stdin.readline():
    print("stdin 입력= ", x)


print("\n 한 줄 문자열을 입력하시오: " )
for i,x in enumerate( sys.stdin.readline()) :
    print( i, "=> ", x)
