#RPS1과 2가 다를 게 없다.
#아니 근데 진짜 왜 제출 안됐지 따흐흑

import sys

#입력
I = set(sys.stdin.readline().split()) #순서나 중복을 무시하는 집합을 선택

#가위바위보
if I == {'R', 'S'}:
    print('R')
elif I == {'P', 'R'}:
    print('P')
elif I == {'S', 'P'}:
    print('S')
else:
    print('D')