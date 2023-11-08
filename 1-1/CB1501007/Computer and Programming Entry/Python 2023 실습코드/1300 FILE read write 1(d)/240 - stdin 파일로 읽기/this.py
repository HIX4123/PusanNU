#-------------------------------------------------------------------------------
# Purpose:     2022 Zoh's Work     "過猶不及"
# Author:      Cho
# Created:     2022-03-07
#-------------------------------------------------------------------------------

# stdin을 일반 파일로 대치해서 읽어들이는 방법
# 우리가 준비한 파일 my.txt를 stdin으로 읽어서 처리하는 방법
#
# 실행방법
# > python this.py "my.txt"

import fileinput

for line in fileinput.input():
    print(line.rstrip())