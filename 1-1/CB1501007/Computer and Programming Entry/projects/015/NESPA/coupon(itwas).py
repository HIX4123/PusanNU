from sys import stdin

# input 함수 대신 사용할 input_stream 정의
input_stream = stdin.readline

# 리스트의 부분집합을 구하는 함수
def get_subsets(lst):
    subsets = [[]]
    for i in lst:
        subsets += [j + [i] for j in subsets]
    return subsets[1:]

# 물건의 개수와 최대 비용 입력받기
num_items, max_cost = map(int, input_stream().split())

# 물건의 비용과 번호를 입력받아 리스트로 저장
item_costs = [(int(input_stream()), i + 1) for i in range(num_items)]

# 조건에 맞는 부분집합 구하기
result = [
    subset
    for subset in get_subsets(item_costs)
    if sum([i[0] for i in subset]) <= max_cost
    and max_cost
    - min([i[0] for i in set(item_costs) - set(subset)], default=min(subset))
    < sum([i[0] for i in subset])
]

# 부분집합 출력
for subset in sorted(result, key=lambda x: list(zip(*x))[1]):
    print(*list(zip(*subset))[1])
