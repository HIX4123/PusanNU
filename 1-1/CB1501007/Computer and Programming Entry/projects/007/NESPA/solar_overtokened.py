# 그리드의 한 "껍데기"에 수를 매기는 함수
def walls(grid, wx, wy, stack, tmp):
    stack -= 1  # 보정항
    for i in range(1, wy):  # 좌하 -> 좌상
        grid[wy - i + stack][0 + stack] = tmp
        tmp += 1
    for j in range(0, wx - 1):  # 좌상 -> 우상
        grid[0 + stack][j + stack] = tmp
        tmp += 1
    for k in range(0, wy - 1):  # 우상 -> 우하
        grid[k + stack][wx - 1 + stack] = tmp
        tmp += 1
        if x == 1:
            break
    for m in range(1, wx):  # 우하 -> 좌하
        grid[wy - 1 + stack][wx - m + stack] = tmp
        tmp += 1
        if y == 1:
            break
    return grid, tmp


def find_index(n):
    for i, line in enumerate(grid):
        for j, value in enumerate(line):
            if value == n:
                print(j + 1, row - i)
                return
    print("0 0")


def find_value(a, b):
    print(grid[row - b][a - 1])


column, row = map(int, input().split())
x, y = column + 2, row + 2
grid = [[0 for _ in range(x)] for _ in range(y)]

tmp = 1
stack = 0
while x > 2 and y > 2:
    stack += 1
    x -= 2
    y -= 2
    grid, tmp = walls(grid, x, y, stack, tmp)

for _ in range(4):
    coord_or_number = list(map(int, input().split()))
    if len(coord_or_number) == 1:
        find_index(*coord_or_number)
    else:
        find_value(*coord_or_number)
