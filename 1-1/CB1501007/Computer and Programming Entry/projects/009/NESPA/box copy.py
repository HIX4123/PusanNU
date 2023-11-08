
from sys import stdin
from enum import IntEnum

input_str = stdin.readline

class CROSS(IntEnum):
    NULL = 1
    POINT = 0
    LINE = -1

# 두 점의 위치를 비교하여 교차 상태를 반환하는 함수
def compare_points(pos1, pos2):
    return CROSS.NULL if pos1 < pos2 else (CROSS.POINT if pos1 == pos2 else CROSS.LINE)

# 투영된 차원에서 두 선분의 교차 상태를 반환하는 함수
def compare_in_projection(dimension):
    return compare_points(dimension[0], dimension[3]) * compare_points(
        dimension[1], dimension[2]
    )

# 4개의 선분에 대해 교차 상태를 판단하여 결과 출력
for _ in range(4):
    (x1_start, y1_start, z1_start, x1_end, y1_end, z1_end, x2_start, y2_start, z2_start, x2_end, y2_end, z2_end) = map(int, input_str().split())
    intersection_x = compare_in_projection([x1_start, x1_end, x2_start, x2_end])
    intersection_y = compare_in_projection([y1_start, y1_end, y2_start, y2_end])
    intersection_z = compare_in_projection([z1_start, z1_end, z2_start, z2_end])
    cross_state = [intersection_x, intersection_y, intersection_z]
    if cross_state.count(CROSS.LINE) == 3:
        print("VOL") # 세 개의 선분이 교차하는 경우
    elif cross_state.count(CROSS.LINE) == 2 and cross_state.count(CROSS.POINT) == 1:
        print("FACE") # 두 개의 선분이 교차하고, 나머지 두 개의 선분이 한 점에서 만나는 경우
    elif cross_state.count(CROSS.POINT) == 3:
        print("POINT") # 세 개의 선분이 한 점에서 만나는 경우
    elif cross_state.count(CROSS.NULL) >= 1:
        print("NULL") # 어떤 선분도 교차하지 않는 경우
    else:
        print("LINE") # 두 개의 선분이 한 직선 위에 있는 경우
