# -*- encoding: utf-8 -*-

import sys

input = sys.stdin.readline


# list의 처음부터 index번째까지의 값을 합산
def partial_sum(list, index):
    tmp = 0
    for i in range(index - 1):
        tmp += list[i]
    return tmp


# 요일 딕셔너리
yoday_dict = {1: "월", 2: "화", 3: "수", 4: "목", 5: "금", 6: "토", 0: "일"}
yoday_dict_reverse = {"월": 1, "화": 2, "수": 3, "목": 4, "금": 5, "토": 6, "일": 0}

# 초기 입력
month_init = int(input())  # 달의 수
Days_init = list(map(int, input().split()))  # 각 달에 포함된 일 수
yoday_init = input().rstrip()  # 1월 1일의 요일

# 메인
for _ in range(3):
    m, d = map(int, input().split())  # 월/일 입력
    try:  # case "땡" : Days_init 리스트에 m - 1번째 인덱스가 존재하지 않는 경우 -> except로 이동
        if Days_init[m - 1] < d:  # case "땡" -> m월에 d일이 없는 경우
            print("땡")
        else:
            yoday = (
                partial_sum(Days_init, m) + d + yoday_dict_reverse[yoday_init] - 1
            ) % 7
            # partial_sum(list, index):list의 index 이전까지의 값을 반환하는 함수.
            # partial_sum(Days_init, m) + d는 1월 1일부터 당일까지 날의 수
            # 여기에 yoday_dict_reverse[yoday_init]으로 1월 1일의 요일에 따른 가중치 부여
            # 7로 나눈 나머지로 요일 계산. -1은 보정항
            print(yoday_dict[yoday])
    except:
        print("땡")
