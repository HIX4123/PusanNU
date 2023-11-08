#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     롯데 만만세
# Author:      Cho
# Created:     2021-03-18
#-------------------------------------------------------------------------------

# input( ) 보다 훨씬 빠르게 읽어들일 수 있다.
# 특히 코딩 test일 경우에는 이것을 사용해야 한다.

import sys

print("한 줄에 여러 숫자를 공백으로 분리하여 입력하시오: " )

number = list( map (int,sys.stdin.readline().split()))

print("number[] = ", number )
print("합계 = sum(number) = ", sum(number) )
