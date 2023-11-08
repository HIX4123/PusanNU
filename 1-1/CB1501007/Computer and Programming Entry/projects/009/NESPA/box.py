# rectangle에서의 변경점
# Z 차원 추가
# count로 처리

from sys import stdin
from enum import IntEnum

input = stdin.readline


# 교차 상태를 나타내는 열거형
class CROSS(IntEnum):
    NULL = 1
    POINT = 0
    LINE = -1


# 두 점의 위치를 비교하여 교차 상태를 반환하는 함수
# 아래 주석에서 a, d와 b, c끼리만 판단해도 도형의 상태를 결정할 수 있음
def compare_points(pos1, pos2):
    return CROSS.NULL if pos1 < pos2 else (CROSS.POINT if pos1 == pos2 else CROSS.LINE)


# 투영된 차원에서 두 선분의 교차 상태를 반환하는 함수
#     a------b
# c------d
# 1*-1=-1

#         a--b
# c--d
# -1*-1=1

# a------b
#     c------d
# 1*-1=-1


# a--b
#         c--d
# 1*1=1
def compare_in_projection(dimension):
    return compare_points(dimension[0], dimension[3]) * compare_points(
        dimension[1], dimension[2]
    )


# main
for _ in range(4):
    # 입력
    (
        x1_start,
        y1_start,
        z1_start,
        x1_end,
        y1_end,
        z1_end,
        x2_start,
        y2_start,
        z2_start,
        x2_end,
        y2_end,
        z2_end,
    ) = map(int, input().split())

    # 차원 단위로 분류해서 연산하기
    intersection_X = compare_in_projection([x1_start, x1_end, x2_start, x2_end])
    intersection_Y = compare_in_projection([y1_start, y1_end, y2_start, y2_end])
    intersection_Z = compare_in_projection([z1_start, z1_end, z2_start, z2_end])

    # 리스트화
    cross_state = [intersection_X, intersection_Y, intersection_Z]

    # 교차하는 경우의 수에 따라 출력
    if cross_state.count(CROSS.LINE) == 3:
        print("VOL")  # 세 개의 선분이 교차하는 경우
    elif cross_state.count(CROSS.LINE) == 2 and cross_state.count(CROSS.POINT) == 1:
        print("FACE")  # 두 개의 선분이 교차하고, 나머지 두 개의 선분이 한 점에서 만나는 경우
    elif cross_state.count(CROSS.POINT) == 3:
        print("POINT")  # 세 개의 선분이 한 점에서 만나는 경우
    elif cross_state.count(CROSS.NULL) >= 1:
        print("NULL")  # 어떤 선분도 교차하지 않는 경우
    else:
        print("LINE")  # 처리해야하는 경우의 수가 많은 LINE을 예외로 처리
