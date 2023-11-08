#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     "착하게 살지 말자."
# Author:      Cho
# Created:     2021-04-30
#-------------------------------------------------------------------------------

"""
sys.exit()메서드로 Python 프로그램 종료
이 메서드는quit()및exit()메서드보다 낫습니다.

구문은 다음 sys.exit([arg])

arg는 구문에서 선택 사항입니다.
대부분 정수 값이지만 문자열 값도 전달할 수 있습니다.
0 인수 값은 성공적인 종료에서 가장 좋은 경우로 간주됩니다.

차이점
    exit : interactive interpreter shell에서
    sys.exit : program에서
"""

import sys
weight =  70

if weight < 80:
    sys.exit("weight less than 80")
else:
    print("weight is not less than 80")
