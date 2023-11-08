def spiralize_grid(grid, column, row):
    x, y = row - 1, 0  # 시작 지점: 좌측 하단
    dx, dy = 0, -1  # 이동 방향: 오른쪽과 "아래"가 양의 방향
    for i in range(column * row):
        grid[x][y] = i + 1
        if (
            x + dx < 0  # 다음 칸의 x좌표가 0이 되는 경우 -> 왼쪽 벽에 다다른 경우
            or y + dy < 0  # 다음 칸의 y좌표가 0이 되는 경우 -> 위쪽 벽에 다다른 경우
            or x + dx == row  # 다음 칸의 x좌표가 column이 되는 경우 -> 오른쪽 벽에 다다른 경우
            or y + dy == column  # 다음 칸의 y좌표가 row가 되는 경우 -> 아래쪽 벽에 다다른 경우
            or grid[x + dx][y + dy]  # 다음 칸에 숫자가 채워져 있는 경우 (integer에서 0이 아니면 참으로 판단하므로)
        ):
            dx, dy = dy, -dx  # 방향 바꾸기((0, -1) -> (1, 0) -> (0, 1) -> (-1, 0))
        # else:
        #     pass
        x, y = x + dx, y + dy  # 이동 방향으로 1칸 이동
    return grid  # 결과 내놔


# 숫자가 주어졌을 때 좌표를 찾는 함수
def find_index(grid, n):
    for i, line in enumerate(grid):
        for j, value in enumerate(line):
            if value == n:
                print(j + 1, row - i)
                return
    print("0 0")


# 좌표가 주어졌을 때 숫자를 찾는 함수
def find_value(grid, a, b):
    print(grid[row - b][a - 1])


# main
# 입력
column, row = map(int, input().split())

# 그리드 생성
grid = spiralize_grid([[0] * column for _ in range(row)], column, row)

# 입력을 받고 위치나 수를 찾는 부분
for _ in range(4):
    coord_or_number = list(map(int, input().split()))
    if len(coord_or_number) == 1:
        find_index(grid, *coord_or_number)
    else:
        find_value(grid, *coord_or_number)
