#-------------------------------------------------------------------------------
# Purpose:     2022 Zoh's Work     "過猶不及"
# Author:      Cho
# Created:     2022-03-07
#-------------------------------------------------------------------------------

# stdin을 일반 파일로 대치해서 읽어들이는 방법
# 우리가 준비한 파일 my.txt를 stdin으로 읽어서 처리하는 방법
#
# 실행방법
# > python that.py
#
# 이렇게 수행한 뒤에 한 줄씩 직접 입력을 해야 한다.
# 끝에는 ^z 를 치면 입력이 종료된다.

import sys

for line in sys.stdin:
    print('Output:', line.rstrip())


