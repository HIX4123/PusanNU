from sys import stdin
from enum import IntEnum

input = stdin.readline


class CROSS(IntEnum):
    NULL = 1
    POINT = 0
    LINE = -1


# 두 점을 비교하여 상태를 반환하는 함수
# 아래 주석에서 a, d와 b, c끼리만 판단해도 도형의 상태를 결정할 수 있음
def compare_points(pos1, pos2):
    return CROSS.NULL if pos1 < pos2 else (CROSS.POINT if pos1 == pos2 else CROSS.LINE)


# 한 차원으로 정사영시켜서 비교하는 함수
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

#main
for _ in range(4):
    # 입력
    x1_start, y1_start, x1_end, y1_end, x2_start, y2_start, x2_end, y2_end = map(
        int, input().split()
    )

    # 차원 단위로 분류해서 연산하기
    intersection_X = compare_in_projection([x1_start, x1_end, x2_start, x2_end])
    intersection_Y = compare_in_projection([y1_start, y1_end, y2_start, y2_end])

    # 교차하는 경우의 수에 따라 출력
    if intersection_X == CROSS.LINE and intersection_Y == CROSS.LINE:
        print("FACE")  # 두 직선이 교차하는 경우
    elif intersection_X == CROSS.POINT and intersection_Y == CROSS.POINT:
        print("POINT")  # 두 점이 일치하는 경우
    elif intersection_X == CROSS.NULL or intersection_Y == CROSS.NULL:
        print("NULL")  # 교차하지 않는 경우
    else:
        print("LINE")  # 처리해야하는 경우의 수가 가장 많은 LINE을 예외로 처리