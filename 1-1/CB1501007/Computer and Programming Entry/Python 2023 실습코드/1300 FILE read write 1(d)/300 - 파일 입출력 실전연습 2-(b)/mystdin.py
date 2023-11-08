#-*- coding: cp949 -*-
# Console에서 standard input으로 읽고 standard output으로 출력
#
#
# 사용방법
# DOS cmd 모드에서
# > python mystdin.py
# 를 수행하면 된다.
# > python stdin.py < data.txt
#
# 만일 다른 화일 xxx.txt에 stndard output 결과를 담으려면
# > python stdin.py < data.txt > xxx.txt
#

import sys
buffer = []
while True:
    userinput = sys.stdin.readline().rstrip('\n')
    print "your input=", userinput
    if userinput == 'quit':
        break
    else:
        buffer.append(userinput)