import sys

# 입력을 받아서 2차원 리스트로 만듦
board = [list(i) for i in sys.stdin.read().splitlines()]

# 45도 회전 함수
def rotate_45(matrix):
    n, m = len(matrix), len(matrix[0])
    new_matrix = [[] for _ in range(n + m - 1)]
    for i in range(n):
        for j in range(m):
            new_matrix[i + j].append(matrix[i][j])
    return new_matrix

# 1로 이루어진 문자열을 찾아서 리스트로 반환하는 함수
def get_ones(arg):
    return [j for i in arg for j in "".join(i).split("0") if j]

# 가로, 세로, 대각선, 역대각선에서 1로 이루어진 문자열을 찾아서 리스트로 만듦
horizontal = get_ones(board)
vertical = get_ones(zip(*board))
diagnoal = get_ones(rotate_45(board))
ardiagnoal = get_ones(rotate_45(list(reversed(board))))

# 모든 리스트를 합쳐서 내림차순으로 정렬하고, 가장 긴 문자열의 길이와 그 길이를 가진 문자열의 개수를 출력함
results = sorted(horizontal + vertical + diagnoal + ardiagnoal, reverse=True)
max_result = results[0]
print(len(max_result), results.count(max_result))
