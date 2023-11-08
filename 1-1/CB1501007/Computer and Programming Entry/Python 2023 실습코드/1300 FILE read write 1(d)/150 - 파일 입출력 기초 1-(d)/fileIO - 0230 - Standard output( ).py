#-------------------------------------------------------------------------------
# Purpose:     2021 Prof. Zoh's Work     롯데 만만세
# Author:      Cho
# Created:     2021-03-18
#-------------------------------------------------------------------------------

import sys


f = open('console.log', 'a' ,encoding='cp949' )  # 로그를 저장할 파일 open

sys.stdout = f

print('파일 로그 시험입니다')

sys.stdout = sys.__stdout__   # 원래의 stdout으로 복구

f.close()                     # 로그 파일 닫기




