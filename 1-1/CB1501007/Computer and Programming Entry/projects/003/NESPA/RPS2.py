# RPS1과 2가 다를 게 없다.
# 아니 근데 진짜 왜 제출 안됐지 따흐흑

import sys
input = sys.stdin.readline

# 입력
I = set(input().split())  # 순서나 중복을 무시하는 집합을 선택

# 가위바위보
if I == {"R", "S"}:     # 바위 vs 가위
    print("R")
elif I == {"P", "R"}:   # 보 vs 바위
    print("P")
elif I == {"S", "P"}:   # 가위 vs 보
    print("S")
else:
    print("D")
