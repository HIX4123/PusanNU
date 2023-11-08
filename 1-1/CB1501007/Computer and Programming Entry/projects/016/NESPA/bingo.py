import sys

# input
board = [list(i) for i in sys.stdin.read().splitlines()]


# 2차원 리스트 45도 회전 함수
def rotate_45(matrix):
    n, m = len(matrix), len(matrix[0])
    new_matrix = [[] for _ in range(n + m - 1)]
    for i in range(n):
        for j in range(m):
            new_matrix[i + j].append(matrix[i][j])
    return new_matrix


# 리스트의 가로줄에서 1만 추출하는 함수
def get_ones(arg):
    return [j for i in arg for j in "".join(i).split("0") if j]


# board의 4방향에서 get_ones 각각 실시
horizontal = get_ones(board)
vertical = get_ones(zip(*board))
diagnoal = get_ones(rotate_45(board))
ardiagnoal = get_ones(rotate_45(list(reversed(board))))

# 리스트 병합 및 정렬, output
results = sorted(horizontal + vertical + diagnoal + ardiagnoal, reverse=True)
max_result = results[0]
print(len(max_result), results.count(max_result))
